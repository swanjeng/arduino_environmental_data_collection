import matplotlib.pyplot as plt
from datetime import datetime

filename = "FILENAME.txt" # change FILENAME to your file name

data = {"date" : [],
        "time" : [],
        "pm25" : [],
       }
with open(filename, "r") as f: 
    for line in f:
        d1 = line.split()
        
        data["date"].append(d1[0])
        data["time"].append(datetime.strptime(d1[0] + " " + d1[1], "%Y.%m.%d %H:%M:%S"))
        data["pm25"].append(int(d1[5]))

d = "pm25"
al = 0.3
Max = max(data[d])
plt.plot(data["time"], data[d], color = "#000000")
plt.fill_between(data["time"], [0] * len(data["date"]), [min(9, Max)] * len(data["date"]), color="#00FF00", alpha=al)
if Max > 9: plt.fill_between(data["time"], [9] * len(data["date"]), [min(35.5, Max)] * len(data["date"]), color="#FFFF00", alpha=al)
if Max > 35.5: plt.fill_between(data["time"], [35.5] * len(data["date"]), [min(55.5, Max)] * len(data["date"]), color="#FF8000", alpha=al)
if Max > 55.5: plt.fill_between(data["time"], [55.5] * len(data["date"]), [min(125.5, Max)] * len(data["date"]), color="#FF0000", alpha=al)
if Max > 125.5: plt.fill_between(data["time"], [125.5] * len(data["date"]), [min(225.5, Max)] * len(data["date"]), color="#8000FF", alpha=al)
if Max > 225.5: plt.fill_between(data["time"], [225.5] * len(data["date"]), [max(data[d])] * len(data["date"]), color="#800000", alpha=al)
plt.show()
