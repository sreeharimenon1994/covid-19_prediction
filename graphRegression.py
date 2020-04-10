from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from ast import literal_eval
from time import strftime, localtime
from datetime import datetime

graph_init = literal_eval(open('data/graph.json','r').read())

start = graph_init[0][0]
perday = 86400000
predictFor = 5 # number of days to be predicted
omit = 37
degree = 2
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

def calculateCases(cf, feat):
    val = 0
    for x in range(degree):
        val += feat[x]*cf[0][x]
    return val

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
plt.show()

# predict for a date
predictDate = '2020-03-27'
preDate = int(datetime.strptime(predictDate, '%Y-%m-%d').timestamp())*1000
diffDays = int((preDate - (start+omit*perday))/perday)
t = features.fit_transform([[diffDays]])
val = calculateCases(coef, t[0])
print('Cases in',predictDate,':', val)
