# utils.py

import matplotlib.pyplot as plt


def plot_lines(x, y_pred, y_actual):
    plt.plot(x, y_pred, label="Prediction")
    plt.plot(x, y_actual, label="Actual")
    plt.legend()
    plt.show()
