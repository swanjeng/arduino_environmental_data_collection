import matplotlib.pyplot as plt # 繪圖套件
import matplotlib as mpl # 設定字體用
import matplotlib.dates as mdates # 處理時間格式用
from datetime import datetime # 將字串轉為時間格式的套件
import glob # 批次尋找符合條件的檔案

# 設定中文顯示
plt.rcParams['font.sans-serif'] = ['SimSun']
mpl.rcParams['axes.unicode_minus'] = False

# 子圖繪製函式
#          資料 dict, 子圖物件, 資料類型, 子圖位置, 線條顏色
def subPlot(data, ax, type, p, col):
    time_formatter = mdates.DateFormatter('%H:%M:%S')
    ax[p - 1].xaxis.set_major_formatter(time_formatter)
    ax[p - 1].plot(data["time"], data[type], color = col, label = data["date"][0])
    ax[p - 1].set_ylabel(type.upper())
    ax[p - 1].legend(loc = 'upper right')

filenames = glob.glob(r'*HOU_CHEN_DU.txt')

types = ["pm1", "pm2.5", "pm10"]

fig, ax = plt.subplots(3,1)

for fileindex in range(len(filenames)):
    if fileindex == 1: continue # 跳過資料偏差過大的檔案
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
            if t >= datetime.strptime("12:56:00", "%H:%M:%S") and t <= datetime.strptime("13:15:00", "%H:%M:%S"):
                data["date"].append(dataInFile[0])
                data["time"].append(datetime.strptime(dataInFile[1], "%H:%M:%S"))
                
                for i in range(3):
                    data[types[i]].append(int(dataInFile[i + 4]))

        for i in range(len(types)):
            subPlot(data, ax, types[i], i + 1, (0, fileindex / len(filenames), 0))

plt.suptitle("PM1.0, PM2.5, and PM10 Levels Over Time at 好成嘟 Restaurant")
plt.legend()
# plt.tight_layout()
plt.show()