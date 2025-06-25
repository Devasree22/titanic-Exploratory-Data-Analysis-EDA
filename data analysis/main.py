from eda.load_data import load_dataset
from eda.summary_stats import show_info, show_describe
from eda.visualizations import plot_histograms, plot_boxplot_age_survival
from eda.relationships import plot_correlation_heatmap, plot_pairplot

# Load Data
df = load_dataset('data/titanic.csv')

# Explore
show_info(df)
show_describe(df)

# Visualize
plot_histograms(df)
plot_boxplot_age_survival(df)
plot_correlation_heatmap(df)
plot_pairplot(df)
