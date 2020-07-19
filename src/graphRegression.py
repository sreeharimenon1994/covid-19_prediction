from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from ast import literal_eval
from time import strftime, localtime, strptime, mktime
from datetime import datetime
import requests

# graph_init = literal_eval(open('data/graph.json','r').read())
url = 'https://c19downloads.azureedge.net/downloads/data/countries_latest.json'
data = requests.get(url).json()['E92000001']
degree = 6

def calculateCases(cf, feat):
    val = 0
    for x in range(degree):
        val += feat[x]*cf[0][x]
    return val


def predict(key, predict):
    graph_init = [[int(mktime(strptime(x['date'], '%Y-%m-%d'))), x['value']] for x in data[key]]
    start = graph_init[0][0]
    perday = 86400000
    predictFor = predict # number of days to be predicted
    omit = 25
    customDayStart = omit*perday + start

    graph = graph_init[omit:]
    # x_graph = [[x[0]] for x in graph]
    dateConverter = lambda x: strftime('%b %d', localtime((start + perday*x)/1000))
    x_graph_day = [dateConverter(omit+x) for x in range(0,len(graph)+predictFor)]

    x = [[i] for i in range(0, len(graph))]
    y = [[i[1]] for i in graph]

    features = PolynomialFeatures(degree=degree, include_bias=False)
    x_poly = features.fit_transform(x)
    lin_reg = LinearRegression()
    lin_reg.fit(x_poly, y)
    coef = lin_reg.coef_

    final_y = []
    for i in range(0, len(graph)):
        final_y.append(calculateCases(coef, x_poly[i]))

    x_temp = [[i+len(x)] for i in range(0, predictFor)]
    x_temp = features.fit_transform(x_temp)
    for i in range(len(x_temp)):
        final_y.append(calculateCases(coef, x_temp[i]))

    # plotting
    plt.scatter(x_graph_day[:-predictFor], y, color='black')
    plt.plot(x_graph_day[:-predictFor], final_y[:-predictFor], color='blue')
    plt.plot(x_graph_day[-predictFor:], final_y[-predictFor:], color='red')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


predict('dailyConfirmedCases', 2)
predict('dailyTotalConfirmedCases', 5)