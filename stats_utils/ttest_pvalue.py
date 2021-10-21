from scipy import stats


def ttest_p_value(group1, group2=None, independent=True):
    if group2 is None:
        return stats.ttest_1samp(group1, popmean=0).pvalue
    elif independent:
        return stats.ttest_ind(group1, group2).pvalue
    else:
        return stats.ttest_rel(group1, group2).pvalue