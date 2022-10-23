import matplotlib.pyplot as plt


def data_text_display(data: []):
    data_list = data['list']
    for x in data_list:
        print("Temperature: " + str(x['main']['temp']) + "F at " + str(x['main']['humidity']) + " percent humidity")
        print(x['weather'])


def plot_temp_data(data: []):
    plt.plot(data)
    plt.ylabel("Time")
    plt.xlabel("Temp (deg F)")