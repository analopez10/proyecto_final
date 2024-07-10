from meteostat import Point, Daily
from datetime import datetime
import pandas as pd

# Definir el rango de fechas
start = datetime(2015, 1, 1)
end = datetime(2024, 1, 1)

def get_season(date, latitude):
    Y = 2000  # Año bisiesto para obtener las fechas de estación
    # Estaciones para el hemisferio norte
    northern_seasons = [
        ('winter', (datetime(Y, 1, 1), datetime(Y, 3, 20))),
        ('spring', (datetime(Y, 3, 21), datetime(Y, 6, 20))),
        ('summer', (datetime(Y, 6, 21), datetime(Y, 9, 22))),
        ('autumn', (datetime(Y, 9, 23), datetime(Y, 12, 20))),
        ('winter', (datetime(Y, 12, 21), datetime(Y, 12, 31)))
    ]
    # Estaciones para el hemisferio sur (invertidas)
    southern_seasons = [
        ('summer', (datetime(Y, 1, 1), datetime(Y, 3, 20))),
        ('autumn', (datetime(Y, 3, 21), datetime(Y, 6, 20))),
        ('winter', (datetime(Y, 6, 21), datetime(Y, 9, 22))),
        ('spring', (datetime(Y, 9, 23), datetime(Y, 12, 20))),
        ('summer', (datetime(Y, 12, 21), datetime(Y, 12, 31)))
    ]

    # Seleccionar las estaciones adecuadas según la latitud
    seasons = northern_seasons if latitude >= 0 else southern_seasons

    if isinstance(date, datetime):
        date = date.replace(year=Y)
        return next(season for season, (start, end) in seasons if start <= date <= end)



# Función para obtener datos climáticos estacionales de Meteostat
def get_meteostat_seasonal_data(lat, lon, start, end):
    location = Point(lat, lon)
    data = Daily(location, start, end)
    data = data.fetch()

    if data.empty:
        print(f"No data found for coordinates: ({lat}, {lon})")
        return None

    # Crear una columna de latitud para la función get_season
    data['Latitude'] = lat

    # Agregar columnas de estación
    data['season'] = data.index.to_series().apply(lambda date: get_season(date, lat))

    # Agrupar por año y estación, y calcular los valores medios
    seasonal_data = data.groupby([data.index.year, 'season']).mean().reset_index()
    return seasonal_data









# Función para obtener datos climáticos estacionales de Meteostat
def get_meteostat_seasonal_data(lat, lon, start, end):
    location = Point(lat, lon)
    data = Daily(location, start, end)
    data = data.fetch()

    if data.empty:
        print(f"No data found for coordinates: ({lat}, {lon})")
        return None

    # Agregar columnas de estación
    def get_season(date, latitude):
        Y = 2000  # Año bisiesto para obtener las fechas de estación
        # Estaciones para el hemisferio norte
        northern_seasons = [
            ('winter', (datetime(Y, 1, 1), datetime(Y, 3, 20))),
            ('spring', (datetime(Y, 3, 21), datetime(Y, 6, 20))),
            ('summer', (datetime(Y, 6, 21), datetime(Y, 9, 22))),
            ('autumn', (datetime(Y, 9, 23), datetime(Y, 12, 20))),
            ('winter', (datetime(Y, 12, 21), datetime(Y, 12, 31)))
        ]
        # Estaciones para el hemisferio sur (invertidas)
        southern_seasons = [
            ('summer', (datetime(Y, 1, 1), datetime(Y, 3, 20))),
            ('autumn', (datetime(Y, 3, 21), datetime(Y, 6, 20))),
            ('winter', (datetime(Y, 6, 21), datetime(Y, 9, 22))),
            ('spring', (datetime(Y, 9, 23), datetime(Y, 12, 20))),
            ('summer', (datetime(Y, 12, 21), datetime(Y, 12, 31)))
        ]

        # Seleccionar las estaciones adecuadas según la latitud
        seasons = northern_seasons if latitude >= 0 else southern_seasons

        if isinstance(date, datetime):
            date = date.replace(year=Y)
            return next(season for season, (start, end) in seasons if start <= date <= end)

# Supongamos que 'data' es tu DataFrame con columnas 'Date' y 'Latitude'
# data = pd.read_csv('/path/to/data.csv', parse_dates=['Date'])

# Aplicar la función para agregar la columna de estaciones
    data['season'] = data.apply(lambda row: get_season(row['Date'], row['Latitude']), axis=1)

    # Agrupar por año y estación, y calcular los valores medios
    seasonal_data = data.groupby([data.index.year, 'season']).mean().reset_index()
    return seasonal_data










# Obtener datos climáticos estacionales para cada región
def obtain_and_store_seasonal_data(row):
    try:
        seasonal_data = get_meteostat_seasonal_data(row['Latitude'], row['Longitude'], start, end)
        return seasonal_data
    except Exception as e:
        print(f"Error fetching data for region {row['RegionName']}: {e}")
        return None
    
# Función para aplanar los datos estacionales y combinar con el dataset de vinos
def flatten_seasonal_data(row):
    seasonal_data = row['Seasonal_Climate']
    if seasonal_data is not None:
        seasonal_data['RegionName'] = row['RegionName']
        return seasonal_data
    else:
        return pd.DataFrame() 



        