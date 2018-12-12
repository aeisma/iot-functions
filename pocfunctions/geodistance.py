# *****************************************************************************
# © Copyright IBM Corp. 2018.  All Rights Reserved.
#
# *****************************************************************************

PACKAGE_URL = 'git+https://@github.com/aeisma/iot-functions.git@'

import pandas as pd
from iotfunctions.preprocessor import BaseTransformer
from math import pi, sin, cos, acos

def _toRad(deg):
    return deg * pi / 180

def _calc_dist(row):
    phi1 = _toRad(row['lat'])
    phi2 = _toRad(row['prev_lat'])
    delta_lambda = _toRad(row['prev_lon'] - row['lon'])
    R = 6371  # Earth radius, gives distance in km
    return acos(sin(phi1)*sin(phi2) + cos(phi1)*cos(phi2) * cos(delta_lambda)) * R

class CalculateGeoDistance(BaseTransformer):
    '''
    Calculate geographical distance traveled in km forward from last item for the same entity instance
    '''
    url = PACKAGE_URL
    execute_by = ['id']

    def __init__(self, input_item_lat, input_item_lon, output_item):

        self.input_item_lat = input_item_lat
        self.input_item_lon = input_item_lon
        self.output_item = output_item
        super().__init__()

    def _calc(self, df):
        df = df.copy()
        lat = df[self.input_item_lat][1:]
        prev_lat = df[self.input_item_lat].shift()[1:].rename('prev_lat')
        lon = df[self.input_item_lon][1:]
        prev_lon = df[self.input_item_lon].shift()[1:].rename('prev_lon')
        latlon = pd.concat([lat, lon, prev_lat, prev_lon], axis=1)
        df[self.output_item] = latlon.apply(_calc_dist, axis=1)
        return df


# Amersfoort
lat1 = 52.1590354
lon1 = 5.3076119

# Apeldoorn
lat2 = 52.211509
lon2 = 5.9095931

data = {
    'id' : [1,1,1,1,1,2,2,2,2,2],
    'lat' : [lat1, lat2, lat1, lat2, lat1, lat2, lat1, lat2, lat1, lat2],
    'lon' : [lon1, lon2, lon1, lon2, lon1, lon2, lon1, lon2, lon1, lon2]
}
df = pd.DataFrame(data=data)
df

cdt = CalculateGeoDistance(input_item_lon='lon',input_item_lat='lat',output_item='dist')
test_df = cdt.execute(df)
test_df
