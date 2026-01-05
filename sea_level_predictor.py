import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv("epa-sea-level.csv")

def draw_plot():
    # Make a copy of data
    df_plot = df.copy()

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,6))
    ax.scatter(df_plot['Year'], df_plot['CSIRO Adjusted Sea Level'], color='blue')

    # First line of best fit: all data
    slope, intercept, r_value, p_value, std_err = linregress(df_plot['Year'], df_plot['CSIRO Adjusted Sea Level'])
    # Predict values from min year to 2050
    years_extended = pd.Series(range(df_plot['Year'].min(), 2051))
    ax.plot(years_extended, intercept + slope*years_extended, color='red', label='Fit: all data')

    # Second line of best fit: data from year 2000 onwards
    df_recent = df_plot[df_plot['Year'] >= 2000]
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_extended_recent = pd.Series(range(2000, 2051))
    ax.plot(years_extended_recent, intercept_recent + slope_recent*years_extended_recent, color='green', label='Fit: 2000 onwards')

    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save plot
    fig.savefig('sea_level_plot.png')
    return fig
