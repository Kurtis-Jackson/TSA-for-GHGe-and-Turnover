import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from random import *

# Get Data
df = pd.read_excel("DATA - BALANCE ECO.xlsx","GHG TOTAL = CO2ekg2018",header=None)


# Pre-Processing
df = df.iloc[4:24,:]

df.columns = ["Sector","---", "Name"] + pd.date_range(start='1990', end='2020', freq='Y').tolist()
df = df.set_index("Sector")
df = df.iloc[:,1:]


# Get Formated Data
print(df)

agri = df.iloc[0,1:]

random()
fakemodel = []
badfakemodel = []
for val in agri:
    fakemodel.append(val + randint(-1000,1000))
    badfakemodel.append(val + randint(-5000,5000))
print(fakemodel)

# Look Nice
plt.style.use("bmh")
figure, axis = plt.subplots(1, 1) 


# Have Data
#graph = agri.plot()
axis.plot(agri.index.values,fakemodel, label="Model 1", color="green")
axis.plot(agri.index.values,badfakemodel, label="Model 2", color="blue")
axis.plot(agri, label="Original Graph", color="red", linestyle="--")
plt.title("C0₂e in Agriculture")
plt.ylabel("CO₂e (1000 Tonnes)")
plt.xlabel("Year")

# Get all the years instead of just the corperate mandated ones
plt.xlim(pd.Timestamp('31/12/1990'),pd.Timestamp('31/12/2019'))
plt.xticks(agri.index.values)

# Make the dates not look ugly
dater = DateFormatter("%Y")
axis.xaxis.set_major_formatter(dater)

# Show the graph
axis.legend()
plt.show()