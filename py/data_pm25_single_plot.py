import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties as font
from datetime import datetime
import glob

plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定一个支持中文的字体，例如 'SimHei'
mpl.rcParams['axes.unicode_minus'] = False

filenames = glob.glob(r'*HOU_CHEN_DU.txt')

for i in range(len(filenames)):
    if i != 1:
        data = {"date" : [],
                "time" : [],
                "pm25" : []}
        with open(filenames[i], "r") as f:
            for line in f:
                d1 = line.split()
                t = datetime.strptime(d1[1], "%H:%M:%S")
                if t > datetime.strptime("12:56:00", "%H:%M:%S") and t < datetime.strptime("13:15:00", "%H:%M:%S"):
                    data["time"].append(datetime.strptime(d1[1], "%H:%M:%S"))
                    data["pm25"].append(int(d1[5]))
            plt.plot(data["time"], data["pm25"], color = (0, i / len(filenames), 0), label = d1[0])
            plt.legend()
plt.title("PM2.5 Levels Over Time at 好成嘟 Restaurant")
plt.show()
