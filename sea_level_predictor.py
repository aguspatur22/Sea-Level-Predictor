import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')

    # Create first line of best fit
    # Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    res = linregress(x, y)
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = res.intercept + res.slope * x_pred
    plt.plot(x_pred, y_pred, 'r', label='Best Fit Line')

    # Create second line of best fit
    x2 = df[df['Year'] >= 2000]['Year']
    y2 = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    res2 = linregress(x2, y2)
    x2_pred = pd.Series([i for i in range(2000, 2051)])
    y2_pred = res2.intercept + res2.slope * x2_pred
    plt.plot(x2_pred, y2_pred, 'g', label='Best Fit Line 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()