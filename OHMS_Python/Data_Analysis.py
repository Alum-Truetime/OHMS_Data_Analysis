import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#from pandas_profiling import ProfileReport as pp

pd.set_option('display.max_columns', 89)

df = pd.read_csv('Data/Clean_Data/OpsCalculations.csv')

#profile = ProfileReport(df, title="Pandas Profiling Report")

df.head()

plt.scatter(df.fldNumberOfInstallers, df.fldCarryUpHours)
plt.title('Number of Installers vs Install Hours')
plt.ylabel('Number of Hours')
plt.xlabel('Number of Installers')
plt.show()
