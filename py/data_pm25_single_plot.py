# For this program, when files are sorted by name, they should also be sorted by time.

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties as font
from datetime import datetime
import glob

plt.rcParams['font.sans-serif'] = ['SimSun']  # 中文字體
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


