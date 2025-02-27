import numpy as np
import matplotlib.pyplot as plt

data = np.load('/Users/nataliehuynh/practice_web/data/eeg-trials_2-per-class_run-2.npy')

# Select a specific slice (e.g., the first trial)
data_slice = data[0]  # This will select the first 8x350 matrix

# Plot one of the 350-length vectors
plt.plot(data_slice[0])  # Plot the first 350-length vector
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Plot of Selected Data Slice')
plt.show()
