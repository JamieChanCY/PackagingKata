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


