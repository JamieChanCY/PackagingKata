"""
Using *only* the functions provided in this project, adjust this script wo it does the following:
"""

# 1. generate two groups of 100 data points, one with a mean of 1 and the other with a mean of 1.4, both with sd  of 1.5
from gen_data import generate_random_normal
group1 = generate_random_normal(100, 1, 1.5)
group2 = generate_random_normal(100, 1.4, 1.5)


# 2. Can we tell that the two groups' populations have different means?
# Print the t statistic and pvalue comparing the two groups
from ttest import ttest_t_stat
from ttest_pvalue import ttest_p_value
t = ttest_t_stat(group1, group2)
p = ttest_p_value(group1, group2)
print(t, p)

# 3. Is the two groups' data correlated with each other?
# print the spearman correlation statistic and pvalue between the two groups
from correlation import correlation_statistic
from correlation_pvalue import correlation_pvalue
r = correlation_statistic(group1, group2, kind = 'spearman')
p = correlation_pvalue(group1, group2, 'spearman')
print(r, p)

# 4. Plot the data
from plots import scatter_plot
scatter_plot(group1, group2)
