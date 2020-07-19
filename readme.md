# Linear Regression

Regression analysis is one of the most important fields in statistics and machine learning. There are many regression methods available. Linear regression is one of them. In regression analysis, you usually consider some phenomenon of interest and have a number of observations. Each observation has two or more features. Following the assumption that (at least) one of the features depends on the others, you try to establish a relation among them.In other words, you need to find a function that maps some features or variables to others sufficiently well.


## Count and model prediction
The graph represent the number of daily cases.

![daily](/results/daily_cases.png)

The graph represent the number of total daily cases.

![generated_image](/results/daily_total.png)


## Installation

pip:

    pip install -U scikit-learn
    pip install matplotlib
    pip install requests

## How to Use

To using this repo, some things you should to know:

* The api.py can be used create the dataset
* `collect.js` can be used to scrape from the website
* To execute run  `python graphRegression.py`

## Documentation

You can find the API documentation on the websites:

* https://scikit-learn.org/stable/modules/classes.html
* https://matplotlib.org/contents.html