"""
Using *only* the functions provided in this project, adjust this script wo it does the following:
"""
import stats_utils as su
# 1. generate two groups of 100 data points, one with a mean of 1 and the other with a mean of 1.4, both with sd  of 1.5
group1 = su.generate_random_normal(100, 1, 1.5)
group2 = su.generate_random_normal(100, 1.4, 1.5)


# 2. Can we tell that the two groups' populations have different means?
# Print the t statistic and pvalue comparing the two groups
t = su.ttest_t_stat(group1, group2)
p = su.ttest_p_value(group1, group2)
print(t, p)

# 3. Is the two groups' data correlated with each other?
# print the spearman correlation statistic and pvalue between the two groups
r = su.correlation_statistic(group1, group2, 'spearman')
p = su.correlation_pvalue(group1, group2, 'spearman')
print(r, p)

# 4. Plot the data
su.scatter_plot(group1, group2)
