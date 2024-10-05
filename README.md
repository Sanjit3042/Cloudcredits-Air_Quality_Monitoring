# Air Quality Monitoring Project

## Overview
This project analyzes air quality data to identify trends and patterns in pollution levels across various cities. The project uses clustering and regression techniques to understand the factors affecting air quality and visualize predictions based on historical data. The analysis focuses on key air pollutants like PM2.5, NO2, CO, and ozone.

## Dataset
The dataset used contains air quality index (AQI) values and the levels of several pollutants. The dataset can be downloaded from Kaggle:

- [Global Air Pollution Dataset (Kaggle)](https://www.kaggle.com/datasets/hasibalmuzdadid/global-air-pollution-dataset)

The dataset includes the following columns:
- **AQI Value**: The overall air quality index.
- **PM2.5 AQI Value**: AQI value for particulate matter 2.5 microns or less.
- **NO2 AQI Value**: AQI value for nitrogen dioxide.
- **CO AQI Value**: AQI value for carbon monoxide.
- **Ozone AQI Value**: AQI value for ozone.

## Project Structure
```
air_quality_monitoring/
│
├── data/                        # Directory to store dataset files
│   └── global_air_pollution.csv  # Dataset file
├── main.py                      # Main Python script for analysis
└── README.md                    # Project description
```

## How to Run
1. **Install dependencies**: Ensure you have Python 3.x and install the required libraries:
    ```bash
    pip install pandas scikit-learn matplotlib seaborn
    ```

2. **Run the analysis**: Execute the script to analyze the dataset.
    ```bash
    python main.py
    ```

3. **Outputs**:
    - **Clustering Visualization**: The KMeans clustering groups cities with similar pollution levels.
    - **Regression Analysis**: A regression model is trained to predict AQI based on pollutant levels, with a plot comparing actual vs. predicted AQI values.

## Methods Used
- **KMeans Clustering**: Group cities based on similarity in AQI pollutant levels.
- **Linear Regression**: Predict AQI based on pollutant concentration levels (PM2.5, NO2, CO, and Ozone).
  
## Sample Visualizations
1. **Clustering Plot**: Shows cities grouped by similar pollutant patterns.
2. **Actual vs Predicted AQI**: Line plot showing how well the model predicts AQI based on historical data.

## Improvements and Future Work
- Add more features such as temperature, humidity, and time-based trends.
- Experiment with more advanced models such as Decision Trees or Random Forest for better predictions.
  
## License
This project is licensed under the MIT License.

## Acknowledgments
- Dataset from [Kaggle](https://www.kaggle.com/datasets/hasibalmuzdadid/global-air-pollution-dataset)
