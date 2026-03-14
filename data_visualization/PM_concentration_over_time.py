import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime
from matplotlib.font_manager import FontProperties
import matplotlib.dates as mdates
import numpy as np

FILENAME = "set your file name here"

# set font (needed only if Chinese is needed)
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK JP']
mpl.rcParams['axes.unicode_minus'] = False

data = {"date": [],
        "time": [],
        "pm1": [],
        "pm25": [],
        "pm10": []
        }

with open(FILENAME, "r") as file:
    for line in file:
        line_contents = line.split()
        if int(line_contents[5]) >= 500:
            continue  # filter error values
        data["date"].append(line_contents[0])
        data["time"].append(datetime.strptime(
            line_contents[0] + " " + line_contents[1], "%Y.%m.%d %H:%M:%S"))
        data["pm1"].append(int(line_contents[4]))
        data["pm25"].append(int(line_contents[5]))
        data["pm10"].append(int(line_contents[6]))

plt.plot(data["time"], data["pm1"], color=(0.5, 0, 0), label="PM1")
plt.plot(data["time"], data["pm25"], color=(0, 0.5, 0), label="PM2.5")
plt.plot(data["time"], data["pm10"], color=(0, 0, 0.5), label="PM10")

plt.title("PM Concentration Over Time")

plt.legend()
plt.show()
