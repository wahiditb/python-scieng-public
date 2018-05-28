import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read in data
head = pd.read_table('ScatMieData.csv', sep='=', nrows=4,
                     comment=',', header=None)
scat = pd.read_csv('ScatMieData.csv', skiprows=4)

theta = (180./np.pi)*np.arccos(scat.Cos_theta)

plt.close('all')
fig, ax = plt.subplots(figsize=(6, 4))

ax.semilogy(theta, scat.F1, 'o', color='black', label="F1")
ax.semilogy(theta, scat.F2, 's', mec='black', mfc='white',
            zorder=-1, label="F2")
ax.legend(loc="lower left")
ax.set_xlabel("theta (degrees)")
ax.set_ylabel("intensity")
for i in range(4):
    ax.text(0.95, 0.9-i/18, "{} = {}".format(head[0][i],
            head[1][i]), ha='right', fontsize=10,
            transform=ax.transAxes)
plt.tight_layout()
plt.show()
# fig.canvas.manager.window.raise_()
plt.savefig('ScatMiePlot.pdf')