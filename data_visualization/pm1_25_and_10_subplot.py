# For this program, when files are sorted by name, they should also be sorted by time.

import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as mdates
from datetime import datetime
import glob

# 如需要中文字體才需要這兩行 / these two lines are needed only if displaying Chinese is needed.
# 中文版 OS 內建 Noto Sans CJK / Chinese version OSes already has Noto Sans CJK.
# Matplotlib 讀到的會是 JP / the font family seen by matplotlib is "JP".
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK JP']  
mpl.rcParams['axes.unicode_minus'] = False

def subPlot(data, ax, type, p, col):
    # show time only
    time_formatter = mdates.DateFormatter('%H:%M:%S')
    ax[p - 1].xaxis.set_major_formatter(time_formatter)
    
    ax[p - 1].plot(data["time"], data[type], color = col, label = data["date"][0])
    ax[p - 1].set_ylabel(type.upper())
    ax[p - 1].legend(loc = 'upper right')

filenames = glob.glob(r'*abc.txt') # change abc to your file suffix for the same location

types = ["pm1", "pm2.5", "pm10"]

fig, ax = plt.subplots(3,1)

for fileindex in range(len(filenames)):
    data = {"date" : [],
            "time" : [],
            "pm1" : [],
            "pm2.5" : [],
            "pm10" : []
            }
    
    with open(filenames[fileindex], "r") as f: 
        for line in f:
            dataInFile = line.split()
            
            t = datetime.strptime(dataInFile[1], "%H:%M:%S")
            data["date"].append(dataInFile[0])
            data["time"].append(datetime.strptime(dataInFile[1], "%H:%M:%S"))
                
            for i in range(3):
                data[types[i]].append(int(dataInFile[i + 4]))

        for i in range(len(types)):
            subPlot(data, ax, types[i], i + 1, (0, fileindex / len(filenames), 0))

plt.suptitle("PM1.0, PM2.5, and PM10 Levels Over Time at abc")
plt.legend()
# plt.tight_layout() # uncomment this if needed

plt.show()


