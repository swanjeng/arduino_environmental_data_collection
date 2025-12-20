# For this program, when files are sorted by name, they should also be sorted by time.

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties as font
from datetime import datetime
import glob

# 如需要中文字體才需要這兩行 / these two lines are needed only if displaying Chinese is needed.
# 中文版 OS 內建 Noto Sans CJK / Chinese version OSes already has Noto Sans CJK.
# Matplotlib 讀到的會是 JP / the font family seen by matplotlib is "JP".
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK JP']  
mpl.rcParams['axes.unicode_minus'] = False

filenames = glob.glob(r'*abc.txt') # change abc to your file suffix for the same location

for i in range(len(filenames)):
    data = {"date" : [],
            "time" : [],
            "pm25" : []}
    with open(filenames[i], "r") as f:
        for line in f:
            d1 = line.split()
            t = datetime.strptime(d1[1], "%H:%M:%S")
            data["time"].append(datetime.strptime(d1[1], "%H:%M:%S"))
            data["pm25"].append(int(d1[5]))
    plt.plot(data["time"], data["pm25"], color = (0, i / len(filenames), 0), label = d1[0])
    plt.legend()
plt.title("PM2.5 Levels Over Time at abc")
plt.show()



