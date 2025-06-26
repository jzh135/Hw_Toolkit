import numpy as np
import csv

# Calculation of Two-Wire Line
def cal_two_wire_params (d: float,          # Radius of each conductor
                         D: float,          # Center-to-center distance between the two conductors
                         epsilon_r: float,  # Relative Permittivity (dielectric constant) = 1 in air
                         mu_ri: float,      # Relative Magnetic permeability of the insulator (1 for air)
                         mu_rc: float,      # Relative Magnetic Permeability of the conductor
                         sigma: float,      # Electrical Conductivity of insulator (air)
                         sigma_c: float,    # Electrical Conductivity of conductor
                         length: float,     # Length of the cable
                         freq: float) -> dict:
    
    # Constants
    epsilon_0 = 8.854e-12 # Vacuum permittivity (F/m)
    epsilon = epsilon_0 * epsilon_r
    mu_0 = 4 * np.pi * 1e-7 # Vacuum permeability (H/m)
    mu_c = mu_0 * mu_rc
    mu_i = mu_0 * mu_ri

    # Calculate surface resistance (due to skin effect)
    Rs = np.sqrt(np.pi * freq * mu_c / sigma_c)
    # Calculate the unit resistance
    R_per_m = 2 * Rs / (np.pi * d)

    # Calculate the unit inductance
    L_per_m = mu_i/np.pi * np.log(D/d + np.sqrt((D/d)**2 - 1))

    # Calculate the unit capacitance
    C_per_m = np.pi * epsilon / np.log((D/d) + np.sqrt((D/d)**2 - 1))

    # Calculate the unit conductance
    G_per_m = np.pi * sigma / np.log((D/d) + np.sqrt((D/d)**2 - 1))

    R = R_per_m * length
    L = L_per_m * length
    C = C_per_m * length
    G = G_per_m * length

    return {
        "R": R,
        "L": L,
        "C": C,
        "G": G
    }

def cal_coaxial_params (a: float,           # Inner conductor radius (meters)
                        b: float,           # Outer conductor radius (meters)
                        epsilon_r: float,   # Relative Permittivity (dielectric constant) = 1 in air
                        mu_ri: float,       # Relative Magnetic permeability of the insulator (1 for air)
                        mu_rc: float,       # Relative Magnetic Permeability of the conductor
                        sigma: float,       # Electrical Conductivity of insulator
                        sigma_c: float,     # Electrical Conductivity of conductor
                        length: float,      # Length of the cable
                        freq: float) -> dict:
    
    # Constants
    epsilon_0 = 8.854e-12 # Vacuum permittivity (F/m)
    epsilon = epsilon_0 * epsilon_r
    mu_0 = 4 * np.pi * 1e-7 # Vacuum permeability (H/m)
    mu_c = mu_0 * mu_rc
    mu_i = mu_0 * mu_ri

    # Calculate surface resistance (due to skin effect)
    Rs = np.sqrt(np.pi * freq * mu_c / sigma_c)
    # Calculate the resistance per unit length
    R_per_m = Rs/(2*np.pi) * (1/a + 1/b)

    # Calculate the resistance per unit length
    L_per_m = mu_i/(2*np.pi) * np.log(b/a)

    # Calculate the capacitance per unit length
    C_per_m = 2 * np.pi * epsilon / np.log(b/a)

    # Calculate the conductance per unit length
    G_per_m = 2 * np.pi * sigma / np.log(b/a)
    
    R = R_per_m * length
    L = L_per_m * length
    C = C_per_m * length
    G = G_per_m * length

    return {
        "R": R,
        "L": L,
        "C": C,
        "G": G
    }



if __name__ == "__main__":
    # Define parameters
    
    # Parameters for the 14-gauge two-wire transmission line
    d = 0.000813            # Radius of each conductor (14 AWG)
    D = 0.02                # Center-to-center distance between the two conductors
    epsilon_r = 1           # Relative Permittivity (air)
    mu_ri = 1               # Relative Magnetic permeability of the medium (1 for air)
    mu_rc = 1               # Relative Magnetic Permeability of the conductor (copper)
    sigma = 3.0e-15         # Electrical Conductivity of insulator (air)
    sigma_c = 5.8e7         # Electrical Conductivity of conductor (copper)
    freq = 60               # Frequency (Hz)

    # Calculate for cable lengths from 100m to 5000m in 100m increments
    print("Two-Wire Transmission Line Parameters")
    print("=" * 60)
    print(f"{'Length (m)':<12} {'R (Ohm)':<15} {'L (H)':<15} {'C (F)':<15} {'G (S)':<15}")
    print("-" * 60)
    
    # Prepare data for CSV export
    csv_data = []
    csv_data.append(['Length (m)', 'R (Ohm)', 'L (H)', 'C (F)', 'G (S)'])  # Header row

    for length in range(100, 5100, 100):  # 100m to 5000m in 100m steps
        params = cal_two_wire_params(d, D, epsilon_r, mu_ri, mu_rc, sigma, sigma_c, length, freq)
        print(f"{length:<12} {params['R']:<15.6e} {params['L']:<15.6e} {params['C']:<15.6e} {params['G']:<15.6e}")

        # Add data to CSV list
        csv_data.append([length, params['R'], params['L'], params['C'], params['G']])

    # Export to CSV file
    csv_filename = 'transmission_line_results.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_data)
    
    print(f"\nResults exported to {csv_filename}")

