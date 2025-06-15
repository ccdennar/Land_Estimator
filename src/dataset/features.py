import geopandas as gpd
from geopy.distance import geodesic

def build_features(parcel_path, amenity_path, output_path):
    parcel_gdf = gpd.read_file(parcel_path)
    amenity_gdf = gpd.read_file(amenity_path)
    parcel_gdf['distance_to_amenity'] = parcel_gdf.geometry.apply(
        lambda x: min([geodesic((x.y, x.x), (a.y, a.x)).km for a in amenity_gdf.geometry])
    )
    parcel_gdf.to_file(output_path, driver='GeoJSON')