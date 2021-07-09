from opal.opal import load_dataset
import matplotlib.pyplot as plt
import numpy as np 

ds = load_dataset('./', fname='awaDrive2YAG1.stat')

plt = ds.plot_envelope()

plt.show()
