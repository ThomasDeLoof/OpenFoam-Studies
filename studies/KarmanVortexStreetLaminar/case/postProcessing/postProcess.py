"""
Post-processing script for OpenFOAM forceCoeffs output.
"""

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.fft import fft, fftfreq

# ============================================================
# CONFIGURATION
# ============================================================

# Path to OpenFOAM coefficient file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "forces", "0", "coefficient.dat")

# Time after which the flow is considered statistically steady
T_START = 60.0  # seconds
# Characteristic length for Stouhal computation
L_REF = 0.2  # meters
# Free-stream velocity
U_INF = 0.075  # m/s
# Signal used for frequency analysis
SIGNAL_NAME = "Cl"

# ============================================================
# READ OPENFOAM FILE
# ============================================================

# Read all lines
with open(FILE_PATH, "r") as f:
    lines = f.readlines()

# Keep only non-comment lines
data_lines = [line for line in lines if not line.startswith("#")]

# Column names manually reconstructed from the header
columns = [
    "Time",
    "Cd", "Cd_f", "Cd_r",
    "Cl", "Cl_f", "Cl_r",
    "CmPitch", "CmRoll", "CmYaw",
    "Cs", "Cs_f", "Cs_r"
]

# Convert text data into numpy array
data = []

for line in data_lines:
    values = line.split()
    data.append([float(v) for v in values])

data = np.array(data)

# Create pandas DataFrame
df = pd.DataFrame(data, columns=columns)

print("Data successfully loaded.")
print(df.head())

# isolate steady regime for frequency analysis

steady_df = df[df["Time"] >= T_START].copy()

print(f"\nSteady regime starts at t = {T_START} s")
print(f"Number of samples in steady regime: {len(steady_df)}")

# compute basic statistics 

print("\n===== PERFORMANCE STATISTICS =====")

for coeff in ["Cd", "Cl"]:

    mean_val = steady_df[coeff].mean()
    rms_val = np.sqrt(np.mean((steady_df[coeff] - mean_val)**2))
    std_val = steady_df[coeff].std()

    print(f"\n{coeff}:")
    print(f"  Mean = {mean_val:.6f}")
    print(f"  RMS  = {rms_val:.6f}")
    print(f"  STD  = {std_val:.6f}")

# ============================================================
# FREQUENCY ANALYSIS
# ============================================================

signal = steady_df[SIGNAL_NAME].values
time = steady_df["Time"].values

# Detect peaks
peaks, _ = find_peaks(signal)

# Compute dominant frequency from peak spacing
if len(peaks) > 1:

    peak_times = time[peaks]

    periods = np.diff(peak_times)

    mean_period = np.mean(periods)

    shedding_frequency = 1.0 / mean_period

    print("\n===== FREQUENCY ANALYSIS =====")
    print(f"Dominant frequency from peaks = {shedding_frequency:.6f} Hz")

    # Strouhal number
    st = shedding_frequency * L_REF / U_INF

    print(f"Strouhal number = {st:.6f}")

else:
    print("Not enough peaks detected for frequency estimation.")

# FFT analysis

# Remove mean value before FFT
signal_detrended = signal - np.mean(signal)

# Estimate average time step
dt = np.mean(np.diff(time))

# Number of samples
N = len(signal_detrended)

# FFT
yf = fft(signal_detrended)

# Frequency axis
xf = fftfreq(N, dt)

# Keep only positive frequencies
positive_mask = xf > 0

xf = xf[positive_mask]
yf = yf[positive_mask]

# FFT amplitude
amplitude = 2.0 / N * np.abs(yf)

# Dominant FFT frequency
dominant_index = np.argmax(amplitude)
dominant_frequency_fft = xf[dominant_index]

print("\n===== FFT ANALYSIS =====")
print(f"Dominant FFT frequency = {dominant_frequency_fft:.6f} Hz")

# FFT-based Strouhal number
st_fft = dominant_frequency_fft * L_REF / U_INF

print(f"FFT-based Strouhal number = {st_fft:.6f}")

# ============================================================
# PLOTS
# ============================================================

# Time history of the signal

plt.figure(figsize=(10, 5))

plt.plot(df["Time"], df[SIGNAL_NAME], label=SIGNAL_NAME)

plt.axvline(
    T_START,
    color="red",
    linestyle="--",
    label="Steady regime start"
)

plt.xlabel("Time [s]")
plt.ylabel(SIGNAL_NAME)
plt.title(f"{SIGNAL_NAME} time history")
plt.grid(True)
plt.legend()

# FFT spectrum

plt.figure(figsize=(10, 5))

plt.plot(xf, amplitude)

plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.title(f"FFT spectrum of {SIGNAL_NAME}")
plt.grid(True)

# Optional zoom
plt.xlim(0, 5 * dominant_frequency_fft)

plt.show()

"""
# Saving steady regime data to CSV for further analysis

steady_df.to_csv("steady_regime.csv", index=False)

print("\nSteady regime data exported to steady_regime.csv")
"""