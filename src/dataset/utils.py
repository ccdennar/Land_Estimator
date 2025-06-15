import os
import logging
import pandas as pd
import geopandas as gpd
from pathlib import Path

# Configuration settings
CONFIG = {
    'data_dir': Path('data'),
    'raw_data_dir': Path('data/raw'),
    'processed_data_dir': Path('data/processed'),
    'models_dir': Path('models'),
    'api_key_google': os.getenv('GOOGLE_API_KEY', 'your-google-api-key'),  # Store in environment variable
    'api_key_plotai': os.getenv('PLOTAI_API_KEY', 'your-plotai-api-key'),
    'default_crs': 'epsg:4326',  # Standard WGS84 coordinate reference system
    'log_file': 'land_estimator.log',
    'model_params': {
        'random_forest': {'n_estimators': 100, 'random_state': 42},
        'learning_rate': 0.01,  # For neural networks, if used
    }
}

# Set up logging
logging.basicConfig(
    filename=CONFIG['log_file'],
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def setup_directories():
    """Create necessary directories if they don't exist."""
    for dir_path in [CONFIG['raw_data_dir'], CONFIG['processed_data_dir'], CONFIG['models_dir']]:
        dir_path.mkdir(parents=True, exist_ok=True)
    logging.info("Directories set up successfully")

def load_csv(file_path):
    """Load a CSV file and log the operation."""
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Loaded CSV from {file_path}")
        return df
    except Exception as e:
        logging.error(f"Error loading CSV {file_path}: {str(e)}")
        raise

def load_geojson(file_path):
    """Load a GeoJSON file using geopandas."""
    try:
        gdf = gpd.read_file(file_path)
        logging.info(f"Loaded GeoJSON from {file_path}")
        return gdf
    except Exception as e:
        logging.error(f"Error loading GeoJSON {file_path}: {str(e)}")
        raise

def save_data(data, output_path, geojson=False):
    """Save data as CSV or GeoJSON."""
    try:
        if geojson:
            data.to_file(output_path, driver='GeoJSON')
        else:
            data.to_csv(output_path, index=False)
        logging.info(f"Saved data to {output_path}")
    except Exception as e:
        logging.error(f"Error saving data to {output_path}: {str(e)}")
        raise

def validate_data(df, required_columns):
    """Validate that required columns exist in the dataframe."""
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        logging.error(f"Missing required columns: {missing_cols}")
        raise ValueError(f"Missing required columns: {missing_cols}")
    logging.info("Data validation passed")
    return True

def get_api_key(service):
    """Retrieve API key from config."""
    key_map = {'google': CONFIG['api_key_google'], 'plotai': CONFIG['api_key_plotai']}
    if service not in key_map:
        logging.error(f"Invalid API service: {service}")
        raise ValueError(f"Invalid API service: {service}")
    return key_map[service]