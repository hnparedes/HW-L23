# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the sine wave
frequency = 5  # Frequency in Hz
amplitude = 1  # Amplitude of the sine wave
time = np.linspace(0, 2 * np.pi, 500)  # Time values from 0 to 2π

# Generate the sine wave
sine_wave = amplitude * np.sin(2 * np.pi * frequency * time)

# Plot the sine wave
plt.plot(time, sine_wave)
plt.title('Sine Wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
