"""
    This adt contains earthquake data extracted from the csv
    operations:
        getMagnitudeFromMonth
        getTsunamiLocationOfMonthAndYear
        getTsunamiLocationOfYear
"""
import pandas as pd
from typing import List

class Earthquake:
    """
    initialize earthquake data from csv file
    """
    def __init__(self, path:str = "./earthquake_data_tsunami.csv"):
        """
        Args:
            path: path to the earthquake csv file
        """
        self._earthquakeData = pd.read_csv(path)

    def getMagnitudeFromMonth(self, month: int) -> List[float]:
        """
        Get list of magnitudes for earthquakes in a specific month
        Args:
            month: integer representing the month(1-12)
        
        Returns:
            List of magnitude values for specific month
        """

        month_data = self._earthquakeData[self._earthquakeData["Month"] == month]
        mag_list = month_data['magnitude'].tolist()

        return mag_list
    
    def getTsunamiLocationOfYear(self, year:int) -> pd.DataFrame:
        """
        Get Tsunami locations for a specific year
        Args:
            year: integer representing the year. Assumming from 2000-2022
        
        Returns:
            Data frame that contains earthquake that causes tsunami, and its longitude and latitude of a specific year
        """
        tsunami_df = self._earthquakeData[(self._earthquakeData["Year"] == year) & 
                                          (self._earthquakeData["tsunami"] == 1)]
        
        return tsunami_df[["latitude", "longitude", "Year", "magnitude"]]





    
