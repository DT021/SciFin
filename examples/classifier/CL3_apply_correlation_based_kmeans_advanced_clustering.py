# Standard library imports
# /

# Third party imports
import seaborn as sns
import matplotlib.pyplot as plt

# Local application imports
from scifin import timeseries as ts
from scifin import statistics as st
from scifin import montecarlo as mc
from scifin import classifier as cl

# Generate random walk processes
mc1 = mc.generate_series(n=100, names_base="RW-", series_model=ts.random_walk,
                         start_date="2000-01-01", end_date="2020-01-01", frequency='M',
                         start_value=1., sigma=0.01)

# Plot
ts.multi_plot(mc1)

# Build their covariance matrix
cov1 = st.covariance_from_ts(list_ts=mc1, min_periods=10)
corr1 = st.covariance_to_correlation(cov1)

# Plot this correlation matrix
sns.heatmap(corr1, cmap='viridis')
plt.title("Initial correlation matrix")
plt.show()

# Apply KMeans base clustering
resu1 = cl.kmeans_advanced_clustering(corr1,
                                     names_features=corr1.columns.tolist(),
                                     max_num_clusters=None,
                                     n_init=10)
clustered_corr1_adv, clusters1_adv, silh_score1_adv = resu1

# Plot the clustered correlation matrix
sns.heatmap(clustered_corr1_adv, cmap='viridis')
plt.title("Clustered correlation matrix")
plt.show()

# Print clusters content
print()
labels1_adv = cl.convert_clusters_into_list_of_labels(mc1, clusters1_adv)
cl.print_clusters_content(mc1, labels1_adv)
plt.show()

