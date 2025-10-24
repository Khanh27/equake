"""
This ADT plots the data from the Earthquake data
"""

import matplotlib.pyplot as plt
import seaborn as sns
from Earthquake import Earthquake
import plotly.express as px
import plotly.graph_objects as go

class Plot:
    """
    initialize earthquake data
    """
    def __init__(self):
        self.earthquakeData = Earthquake()
    
    def plot_magnitude_month_data_barplot(self, month:int)->None:
        """
        Plot magnitude data for a specific month as a bar chart.
        
        Args:
            month: Integer representing the month (1-12)
        """
        mag_list = self.earthquakeData.getMagnitudeFromMonth(month)
        
        if not mag_list:
            print(f"No data available for month {month}")
            return
        
        plt.figure(figsize=(12, 6))
        
        # Create x-axis as earthquake indices
        x_values = range(len(mag_list))
        
        plt.bar(x_values, mag_list, edgecolor='black', alpha=0.7, color='steelblue')
        plt.xlabel('Earthquake Amount')
        plt.ylabel('Magnitude')
        plt.title(f'Earthquake Magnitudes for Month {month}')
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.show()

    def plot_magnitude_scatter(self, month: int) -> None:
        """
        Plot magnitude data for a specific month as a scatter plot.
        
        Args:
            month: Integer representing the month (1-12)
        """
        mag_list = self.earthquakeData.getMagnitudeFromMonth(month)
        
        if not mag_list:
            print(f"No data available for month {month}")
            return
        
        plt.figure(figsize=(10, 6))
        plt.scatter(range(len(mag_list)), mag_list, alpha=0.6)
        plt.xlabel('Earthquake Amount')
        plt.ylabel('Magnitude')
        plt.title(f'Earthquake Magnitudes for Month {month}')
        plt.grid(True, alpha=0.3)
        plt.show()

    def plot_scatter_comparison(self, month1: int, month2: int) -> None:
        """
        Create scatter plot comparison between two different months.
        
        Args:
            month1: First month to compare (1-12)
            month2: Second month to compare (1-12)
        """
        mag_list1 = self.earthquakeData.getMagnitudeFromMonth(month1)
        mag_list2 = self.earthquakeData.getMagnitudeFromMonth(month2)
        
        if not mag_list1:
            print(f"No data available for month {month1}")
            return
        if not mag_list2:
            print(f"No data available for month {month2}")
            return
        
        plt.figure(figsize=(12, 6))
        
        plt.scatter(range(len(mag_list1)), mag_list1, 
                    alpha=0.6, label=f'Month {month1}', color='blue', s=50)
        plt.scatter(range(len(mag_list2)), mag_list2, 
                    alpha=0.6, label=f'Month {month2}', color='red', s=50)
        
        plt.xlabel('Earthquake Amount')
        plt.ylabel('Magnitude')
        plt.title(f'Earthquake Magnitude Comparison: Month {month1} vs Month {month2}')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()


    def plot_tsunami_caused_by_earthquake_for_year(self, year:int):
        """
        Plot earthquakes on an interactive world map using Plotly.
        Requires latitude, longitude, and magnitude data from your CSV.
        
        Args:
            month: integer representing month assuming from (1-12).
        """

        df = self.earthquakeData.getTsunamiLocationOfYear(year)

        fig = px.scatter_geo(df,
                            lat='latitude',
                            lon='longitude',
                            color='magnitude',
                            size='magnitude',
                            hover_data=['magnitude', 'Year'],
                            color_continuous_scale='Reds',
                            title=f'Earthquake Map that caused tsunami in{f" - Year {year}"}',
                            projection='natural earth'
                        )
        
        fig.update_layout(
                geo=dict(
                    showland=True,
                    landcolor='lightgray',
                    coastlinecolor='white',
                    showocean=True,
                    oceancolor='lightblue'
                )
            )
            
        fig.show()
