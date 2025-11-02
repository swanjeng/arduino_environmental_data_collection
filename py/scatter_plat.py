import matplotlib.pyplot as plt
import glob

def subPlot(data, ax, t1, t2, x, y):
    ax[x - 1][y - 1].scatter(data[t1], data[t2], color = "#44A4FF", alpha = 0.1)
    ax[x - 1][y - 1].set_xlabel(t1.upper())
    ax[x - 1][y - 1].set_ylabel(t2.upper())

def r(x, y):
    # average
    avg_of_x = 0
    avg_of_y = 0
    for i in range(len(x)):
        avg_of_x += x[i]
        avg_of_y += y[i]

    avg_of_x /= len(x)
    avg_of_y /= len(x)

    # standard deviation
    sd_of_x = 0
    sd_of_y = 0
    for i in range(len(x)):
        sd_of_x += (x[i]**2)
        sd_of_y += (y[i]**2)

    sd_of_x /= len(x)
    sd_of_y /= len(x)

    sd_of_x -= (avg_of_x ** 2)
    sd_of_y -= (avg_of_y ** 2)

    sd_of_x **= 0.5
    sd_of_y **= 0.5

    # r
    r = 0
    for i in range(len(x)):
        r += (((x[i] - avg_of_x) / sd_of_x) * ((y[i] - avg_of_y) / sd_of_y))
    r /= len(x)
    return r

filenames = glob.glob(r'2025*.txt')

data = {"temperature" : [],
        "humidity" : [],
        "pm1" : [],
        "pm2.5" : [],
        "pm10" : [],
        "pressure" : []
       }

for filename in filenames:
    with open(filename, "r") as f: 
        for line in f:
            d1 = line.split()
            data["temperature"].append(float(d1[2]))
            data["humidity"].append(float(d1[3]))
            data["pm1"].append(int(d1[4]))
            data["pm2.5"].append(int(d1[5]))
            data["pm10"].append(int(d1[6]))
            data["pressure"].append(float(d1[7]))

f, ax = plt.subplots(2, 2)

subPlot(data, ax, "pm1", "pm2.5", 1, 1)
print(r(data["pm1"], data["pm2.5"]))

subPlot(data, ax, "pm1", "pm10", 1, 2)
print(r(data["pm1"], data["pm10"]))

subPlot(data, ax, "pm2.5", "pm10", 2, 1)
print(r(data["pm2.5"], data["pm10"]))

subPlot(data, ax, "humidity", "pm2.5", 2, 2)
print(r(data["humidity"], data["pm2.5"]))

plt.suptitle("Scatter Plots of Environmental Data")

plt.show()