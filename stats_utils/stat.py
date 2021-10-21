import numpy as np
from matplotlib import pyplot as plt
from scipy import stats


def correlation_statistic(group1, group2, kind='pearson'):
    """
    Returns the correlation statistic between two groups

    :param group1: an array of data
    :param group2: an array of data
    :param kind: "pearson", "spearman", or "kendall"
    :return:
    """
    if kind == 'pearson':
        return stats.pearsonr(group1, group2)[0]
    elif kind == 'spearman':
        return stats.spearmanr(group1, group2).correlation
    elif kind == 'kendall':
        return stats.kendalltau(group1, group2)[0]
    else:
        raise ValueError("kind {} not recognized, should be 'pearson', 'spearman', or 'kendall'".format(kind))


def correlation_pvalue(group1, group2, kind='pearson'):
    """
    Returns the correlation statistic between two groups

    :param group1: an array of data
    :param group2: an array of data
    :param kind: "pearson", "spearman", or "kendall"
    :return:
    """
    if kind == 'pearson':
        return stats.pearsonr(group1, group2)[1]
    elif kind == 'spearman':
        return stats.spearmanr(group1, group2).pvalue
    elif kind == 'kendall':
        return stats.kendalltau(group1, group2)[1]
    else:
        raise ValueError("kind {} not recognized, should be 'pearson', 'spearman', or 'kendall'".format(kind))


def generate_random_normal(n, mean, sd):
    """
    Returns array of normally-distribute data

    :param n: How many values to generate
    :param mean: the mean of the normal distribution
    :param sd: the standard deviation of the normal distribution
    :return: array of random data
    """
    return np.random.randn(n) * sd + mean


def scatter_plot(group1, group2):
    """
    Shows scatter plot of data

    :param group1: array of data
    :param group2: array of data
    :return:
    """
    plt.scatter(group1, group2)
    plt.show()


def ttest_t_stat(group1, group2=None, independent=True):
    """
    :param group1: an array of data
    :param group2: (optional) another array of data
    :param independent: whether the two groups should be considered independent or not
    :return: (float), the t-value
    """
    if group2 is None:
        return stats.ttest_1samp(group1, popmean=0).statistic
    elif independent:
        return stats.ttest_ind(group1, group2).statistic
    else:
        return stats.ttest_rel(group1, group2).statistic


def ttest_p_value(group1, group2=None, independent=True):
    if group2 is None:
        return stats.ttest_1samp(group1, popmean=0).pvalue
    elif independent:
        return stats.ttest_ind(group1, group2).pvalue
    else:
        return stats.ttest_rel(group1, group2).pvalue