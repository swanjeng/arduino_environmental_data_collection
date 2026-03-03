import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
import numpy as np

filename = "FILENAME.txt" # change FILENAME to your file name

data = {"date" : [],
        "time" : [],
        "pm25" : [],
       }

with open(filename, "r") as f: 
    for line in f:
        d1 = line.split()
        
        data["date"].append(d1[0])
        
        # Since there can be some delay when collecting and the interval may not be always the same, 
        # We should use the datetime format instead of pure strings.
        data["time"].append(datetime.strptime(d1[0] + " " + d1[1], "%Y.%m.%d %H:%M:%S"))
        
        data["pm25"].append(int(d1[5]))

plot_data = "pm25"
al = 0.3
window_size = 3
length = len(data[plot_data])
max_value = max(data[plot_data])

# 計算移動平均
pm25_smooth = np.convolve(data[plot_data], np.ones(
    window_size)/window_size, mode='valid')  # 使用窗口大小為 window_size 的移動平均
time_smooth = data["time"][window_size//2:-(window_size//2)]  # 對應的時間數據

# 只顯示時間，不顯示日期
time_formatter = mdates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(time_formatter)

plt.plot(time_smooth, pm25_smooth, color=(0, 0, 0))

# 顯示 AQI 範圍
plt.fill_between(data["time"], [0] * len(data["date"]),
                 [min(9, max_value)] * len(data["date"]), color="#00FF00", alpha=al)
if max_value > 9:
    plt.fill_between(data["time"], [9] * len(data["date"]),
                     [min(35.5, max_value)] * len(data["date"]), color="#FFFF00", alpha=al)
if max_value > 35.5:
    plt.fill_between(data["time"], [35.5] * len(data["date"]),
                     [min(55.5, max_value)] * len(data["date"]), color="#FF8000", alpha=al)
if max_value > 55.5:
    plt.fill_between(data["time"], [55.5] * len(data["date"]),
                     [min(125.5, max_value)] * len(data["date"]), color="#FF0000", alpha=al)
if max_value > 125.5:
    plt.fill_between(data["time"], [125.5] * len(data["date"]),
                     [min(225.5, max_value)] * len(data["date"]), color="#8000FF", alpha=al)
if max_value > 225.5:
    plt.fill_between(data["time"], [225.5] * len(data["date"]),
                     [max(data[plot_data])] * len(data["date"]), color="#800000", alpha=al)


plt.title("PM2.5 Levels Over Time with AQI Ranges")
plt.show()
