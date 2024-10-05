import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv(r'C:\Users\user\Downloads\CLOUDCREDITS\air_quality_monitoring\data\global air pollution dataset.csv')

# Print the column names to confirm what exists
print("Columns in the dataset:", data.columns)

# Fix for the deprecated fillna method
data.ffill(inplace=True)

# Update feature selection based on actual column names
features = ['PM2.5 AQI Value', 'NO2 AQI Value', 'CO AQI Value', 'Ozone AQI Value']  # Adjusted feature names

# Check if all features exist in the dataset
missing_features = [feature for feature in features if feature not in data.columns]
if not missing_features:
    X = data[features]
    print("Feature selection was successful!")

    # Clustering using KMeans
    kmeans = KMeans(n_clusters=3)
    data['Cluster'] = kmeans.fit_predict(X)

    # Visualize the clusters
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=data, x='PM2.5 AQI Value', y='AQI Value', hue='Cluster', palette='viridis')
    plt.title('KMeans Clustering on Air Quality Data')
    plt.show()

    # Regression Analysis: Predict AQI from pollutant levels
    y = data['AQI Value']
    reg_model = LinearRegression()
    reg_model.fit(X, y)

    # Predictions and plot
    data['AQI_Pred'] = reg_model.predict(X)

    # Plot actual vs predicted AQI
    plt.figure(figsize=(10,6))
    plt.plot(data['AQI Value'], label='Actual AQI')
    plt.plot(data['AQI_Pred'], label='Predicted AQI')
    plt.legend()
    plt.title('Actual vs Predicted AQI')
    plt.show()

    # Print regression coefficients
    print("Regression Coefficients: ", reg_model.coef_)
else:
    print(f"Missing features in dataset: {missing_features}")
