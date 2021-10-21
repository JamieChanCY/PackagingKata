import numpy as np


def generate_random_normal(n, mean, sd):
    """
    Returns array of normally-distribute data

    :param n: How many values to generate
    :param mean: the mean of the normal distribution
    :param sd: the standard deviation of the normal distribution
    :return: array of random data
    """
    return np.random.randn(n) * sd + mean

