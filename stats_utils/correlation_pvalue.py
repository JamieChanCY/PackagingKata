from scipy import stats


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