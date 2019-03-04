import numpy as np


nwalks = 500
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
hints = (np.abs(walks) >= 30).any(1)
crossing_times = (np.abs(walks[hints]) >= 30).argmax(1)
print(crossing_times.mean())
