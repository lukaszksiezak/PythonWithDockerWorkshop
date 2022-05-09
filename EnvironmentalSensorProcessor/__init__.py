import pandas as pd
import numpy as np

import azure.functions as func


TEMPERATURE = "temperature"
HUMIDITY = "humidity"
TIMESTAMP = "timestamp"
VALUE = "value"

POOR_CONDITIONS = 0
TOLERABLE_CONDITIONS = 1
GOOD_CONDITIONS = 2

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        # Convert request to json
        req_body = req.get_json()

        # If requst consists all of required keys,
        # convert it to series and process using process_environment
        # method.
        if TEMPERATURE in req_body and HUMIDITY in req_body:
            temperature = dict_to_series(req_body[TEMPERATURE])
            humidity = dict_to_series(req_body[HUMIDITY])
            
            kpi = process_environment(temperature, humidity)

    except ValueError as ex:
        return func.HttpResponse(status_code=401, body=str(ex))
    
    return func.HttpResponse(
        status_code=200, body=str(kpi)
    )

def dict_to_series(post_request: dict) -> pd.Series:
    """
    Convert given dict input to pandas.Series collection.
    """
    df = pd.DataFrame(post_request)
    df[TIMESTAMP] = pd.to_datetime(df[TIMESTAMP])
    df = df.set_index(TIMESTAMP)
    series = df.squeeze('columns')
    return series

def process_environment(temperature: pd.Series, humidity: pd.Series) -> int:
    """
    Returns a status of environmental conditions based on given
    temperature and humidity.

    Args:
        temperature - pd.Series
        humidity - pd.Series

    Returns:
        int:
            0 - poor conditions
            1 - tolerable conditions
            2 - good conditions
    """
    mean_temperature = np.mean(temperature)
    mean_humidity = np.mean(humidity)

    if 20 <= mean_temperature < 50 or 15 <= mean_humidity < 40:
        return GOOD_CONDITIONS
    elif 0 <= mean_temperature < 20 or 50 <= mean_temperature < 70 \
        or 10 <= mean_humidity < 15 or 40 <= mean_humidity < 50:
        return TOLERABLE_CONDITIONS
    else:
        return POOR_CONDITIONS