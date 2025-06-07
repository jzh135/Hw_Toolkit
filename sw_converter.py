def calculate_peak_current(VIN, VOUT, n, fsw, L, Iout):
    """
    Calculate the inductor peak current for TPS61253 DC-DC converter.
    
    Parameters:
    VIN  : Input voltage (V)
    VOUT : Output voltage (V)
    n    : Efficiency factor (0 < n ≤ 1)
    fsw  : Switching frequency (Hz)
    L    : Inductor value (H)
    Iout : Output current (A)
    
    Returns:
    IL_peak : Inductor peak current (A)
    """
    D = 1 - (VIN * n / VOUT)  # Calculate duty cycle
    IL_peak = (VIN * D) / (2 * fsw * L) + (Iout / (1 - D))  # Peak current equation
    return IL_peak

# Example values
VIN = 3.6  # Input voltage in V
VOUT = 5.0  # Output voltage in V
n = 0.85  # Efficiency factor (85%)
fsw = 3.8e6  # Switching frequency in Hz (3.8 MHz)
L = 0.56e-6  # Inductance in H (0.56 µH)
Iout = 1  # Output current in A

IL_peak = calculate_peak_current(VIN, VOUT, n, fsw, L, Iout)
print(f"Inductor Peak Current: {IL_peak:.3f} A")