import matplotlib.pyplot as plt


def scatter_plot(group1, group2):
    """
    Shows scatter plot of data

    :param group1: array of data
    :param group2: array of data
    :return:
    """
    plt.scatter(group1, group2)
    plt.show()
