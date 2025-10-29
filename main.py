from Earthquake import Earthquake
from Plot import Plot
import pandas as pd

def main():
    df = pd.read_csv("./earthquake_data_tsunami.csv")
    print(df.head())

    earthquake = Earthquake()
    plot = Plot()

    #print(len(earthquake.getMagnitudeFromMonth(1)))
    #plot.plot_magnitude_scatter(1)
    #plot.plot_scatter_comparison(1, 2)
    #plot.plot_tsunami_caused_by_earthquake_for_year(2022)
    plot.plot_tsunami_caused_by_earthquake_for_month_and_year(1, 2022)

    return 

if __name__ == "__main__":
    main()