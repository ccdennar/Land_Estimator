import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_price_distribution(data_path):
    df = pd.read_csv(data_path)
    sns.histplot(df['price_per_sqm'], bins=50)
    plt.title('price per Square Meter Distribution')
    plt.savefig('price_distribution.png')

def plot_parcel_map(geojson_path):
    gdf = gpd.read_file(geojson_path)
    gdf.plot(column= 'price_per_sqm', cmap= 'Y10rRd', legend=True)
    plt.title('Land Price Heatmap')
    plt.savefig('parcel_map.png')