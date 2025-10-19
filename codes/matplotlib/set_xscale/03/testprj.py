import matplotlib.pyplot as plt
import numpy as np

grid = [32,64,128,256,512]
fft_spectral = [1.339154672220572e-16, 1.342489800590083e-16, 1.3269947532677886e-16, \
                1.4514549677756118e-16 , 1.485803753784319e-16]

# Create figure
fig, ax = plt.subplots()

ax.plot(grid, fft_spectral)
ax.set_xscale("log", base=2)
ax.set_yscale("log", base=10)
ax.set_ylim([1e-16, 0.2e-15])

plt.show()