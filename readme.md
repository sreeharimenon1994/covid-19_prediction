# Linear Regression

The GAN generates new handwritten digits! We train a GAN to generate new handwritten digits after showing it pictures of many real handwritten digits. The basic idea behind GAN is that you have two networks (generator and discriminator) competing against each other. The Generator makes “fake” data to pass to the discriminator. The discriminator sees both generated and real training data and predicts if the data it received is real or fake. The generator is constantly trying to outsmart the discriminator by generating better and better fakes.


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