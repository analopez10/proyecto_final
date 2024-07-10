from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pandas as pd

import pandas as pd
from datetime import datetime
from meteostat import Point, Daily

def initialize_geocoder(unique_regions):
    """
    Inicializa el geocodificador, configura el RateLimiter y crea un DataFrame
    para almacenar las coordenadas de las regiones.

    Args:
        unique_regions (list): Lista de nombres de regiones.

    Returns:
        pd.DataFrame: DataFrame con las regiones y sus coordenadas geocodificadas.
    """
    # Inicializar el geocodificador con un tiempo de espera mayor
    geolocator = Nominatim(user_agent="wine_geocoder", timeout=10)

    # Crear un RateLimiter para manejar las tasas de solicitud
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

    # Crear un DataFrame para almacenar las coordenadas de las regiones
    regions_coords = pd.DataFrame(unique_regions, columns=['RegionName'])

    # Función para geocodificar con manejo de errores
    def geocode_with_error_handling(region):
        try:
            location = geocode(region)
            return location
        except Exception as e:
            print(f"Error geocoding {region}: {e}")
            return None

    # Aplicar la geocodificación a cada región
    regions_coords['Location'] = regions_coords['RegionName'].apply(geocode_with_error_handling)
    regions_coords['Latitude'] = regions_coords['Location'].apply(lambda loc: loc.latitude if loc else None)
    regions_coords['Longitude'] = regions_coords['Location'].apply(lambda loc: loc.longitude if loc else None)
    
    return regions_coords




def geocode_with_error_handling(region, geocode):
    """
    Geocodifica una región con manejo de errores.

    Args:
        region (str): Nombre de la región a geocodificar.
        geocode (function): Función de geocodificación con manejo de tasa.

    Returns:
        Location: Objeto de ubicación geocodificado, o None si hay un error.
    """
    try:
        location = geocode(region)
        return location
    except Exception as e:
        print(f"Error geocoding {region}: {e}")
        return None



def obtain_and_store_coordinates(regions_coords, geocode):
    """
    Aplica la geocodificación a todas las regiones en el DataFrame.

    Args:
        regions_coords (pd.DataFrame): DataFrame con los nombres de las regiones.
        geocode (function): Función de geocodificación con manejo de tasa.

    Returns:
        pd.DataFrame: DataFrame con las coordenadas geocodificadas.
    """
    regions_coords['Location'] = regions_coords['RegionName'].apply(lambda region: geocode_with_error_handling(region, geocode))
    regions_coords['Latitude'] = regions_coords['Location'].apply(lambda loc: loc.latitude if loc else None)
    regions_coords['Longitude'] = regions_coords['Location'].apply(lambda loc: loc.longitude if loc else None)
    return regions_coords




