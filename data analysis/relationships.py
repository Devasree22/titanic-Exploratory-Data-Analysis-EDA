import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_heatmap(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Feature Correlation Heatmap')
    plt.show()

def plot_pairplot(df):
    sns.pairplot(df[['Survived', 'Pclass', 'Age', 'Fare']])
    plt.show()
