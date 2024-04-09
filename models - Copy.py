import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from random import *
import locale
from locale import atof, setlocale

# Get Data
df = pd.read_excel("asgsdatatables20182021.xlsx","2",header=None, thousands=',')
gf = pd.read_excel("asgsdatatables20162017.xls","Table 2",header=None)


# Pre-Processing
df = df.iloc[7:21,0:5]
gf = gf.iloc[5:19,1:5]

df.columns = ["Sector"] + pd.date_range(start='2018', end='2022', freq='Y').tolist()
df = df.set_index("Sector")
gf.columns = ["Sector","---"] + pd.date_range(start='2016', end='2018', freq='Y').tolist()
gf = gf.set_index("Sector")

gf = gf.iloc[:,1:]

setlocale(locale.LC_NUMERIC, '')
df = df.applymap(atof) # Not sure why this is whited out

new = gf.merge(df,on='Sector')


# Get Formated Data
print(new)

elec = new.iloc[0,0:]
water = new.iloc[1,0:]
retail = new.iloc[2,0:]

# Look Nice
plt.style.use("bmh")
figure, axis = plt.subplots(1, 1) 


# Have Data
#graph = elec.plot()
axis.plot(elec, label="Electricity, Gas, Stream & Air Conditioning", color="red")
axis.plot(water, label="Water supply", color="blue")
#axis.plot(retail, label="Wholesale and retail trade services", color="green") # <--- This one is really big and makes everything look ugly
plt.title("Turnover of sampled industries")
plt.ylabel("Millions of £s")
plt.xlabel("Year")

# Get all the years instead of just the corperate mandated ones
plt.xlim(pd.Timestamp('31/12/2016'),pd.Timestamp('31/12/2021'))
plt.xticks(elec.index.values)


# Make the dates not look ugly
dater = DateFormatter("%Y")
axis.xaxis.set_major_formatter(dater)

# Show the graph
axis.legend()
plt.show()