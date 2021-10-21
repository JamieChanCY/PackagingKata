from scipy import stats


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


