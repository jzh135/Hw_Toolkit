import numpy as np

# Calculation of Two-Wire Line
def cal_two_wire_params (d: float,          # Radius of each conductor
                         D: float,          # Center-to-center distance between the two conductors
                         epsilon_r: float,  # Relative Permittivity (dielectric constant) = 1 in air
                         mu_ri: float,      # Relative Magnetic permeability of the insulator (1 for air)
                         mu_rc: float,      # Relative Magnetic Permeability of the conductor
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

    R = R_per_m * length
    L = L_per_m * length
    C = C_per_m * length

    return {
        "R": R,
        "L": L,
        "C": C
    }

def cal_coaxial_params (a: float,           # Inner conductor radius (meters)
                        b: float,           # Outer conductor radius (meters)
                        epsilon_r: float,   # Relative Permittivity (dielectric constant) = 1 in air
                        mu_ri: float,       # Relative Magnetic permeability of the insulator (1 for air)
                        mu_rc: float,       # Relative Magnetic Permeability of the conductor
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
    
    R = R_per_m * length
    L = L_per_m * length
    C = C_per_m * length

    return {
        "R": R,
        "L": L,
        "C": C
    }



if __name__ == "__main__":
    # Define parameters
    
    # Parameters for the 14-gauge two-wire transmission line
    d = 0.000813            # Radius of each conductor (14 AWG)
    D = 0.02                # Center-to-center distance between the two conductors
    epsilon_r = 1           # Relative Permittivity (air)
    mu_ri = 1               # Relative Magnetic permeability of the medium (1 for air)
    mu_rc = 1                # Relative Magnetic Permeability of the conductor (copper)
    sigma_c = 5.8e7         # Electrical Conductivity of conductor (copper)
    length = 2500           # Length of the cable (meters)
    freq = 60               # Frequency (Hz)


    
    params = cal_two_wire_params(d, D, epsilon_r, mu_ri, mu_rc, sigma_c, length, freq)

    # Print out results
    for key, value in params.items():
        print(f"{key}: {value:.6e}")

