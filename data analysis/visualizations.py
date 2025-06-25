import matplotlib.pyplot as plt
import seaborn as sns

def plot_histograms(df):
    df.hist(bins=30, figsize=(10, 8))
    plt.tight_layout()
    plt.show()

def plot_boxplot_age_survival(df):
    sns.boxplot(x='Survived', y='Age', data=df)
    plt.title('Age Distribution by Survival')
    plt.show()
