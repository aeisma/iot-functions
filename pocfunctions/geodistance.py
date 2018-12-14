# *****************************************************************************
# © Copyright IBM Corp. 2018.  All Rights Reserved.
#
# *****************************************************************************

PACKAGE_URL = 'git+https://@github.com/aeisma/iot-functions.git@'

import pandas as pd
from iotfunctions.preprocessor import BaseTransformer
from math import pi, sin, cos, acos, nan

def _toRad(deg):
    return deg * pi / 180

class CalculateGeoDistance(BaseTransformer):
    '''
    Calculate geographical spherical distance traveled in km
    '''
    url = PACKAGE_URL

    def __init__(self, input_item_lat, input_item_lon, input_item_prev_lat, input_item_prev_lon, output_item):

        self.input_item_lat = input_item_lat
        self.input_item_lon = input_item_lon
        self.input_item_prev_lat = input_item_prev_lat
        self.input_item_prev_lon = input_item_prev_lon
        self.output_item = output_item
        super().__init__()

    def _calc_dist(self, row):
        lat = row[self.input_item_lat];
        lon = row[self.input_item_lon];
        prevLat = row[self.input_item_prev_lat];
        prevLon = row[self.input_item_prev_lon];
        if ( (prevLat != 0 or prevLon != 0) and (lat != 0 or lon != 0) ):
            phi1 = _toRad(lat)
            phi2 = _toRad(prevLat)
            delta_lambda = _toRad(prevLon - lon)
            R = 6371  # Earth radius, gives distance in km
            return acos(sin(phi1)*sin(phi2) + cos(phi1)*cos(phi2) * cos(delta_lambda)) * R
        else:
            return nan;

    def execute(self, df):
        df = df.copy()
        df[self.output_item] = df.apply(self._calc_dist, axis=1)
        return df

    '''
    # Run over a location series taking (current, previous) location tuples.
    # This would work if the AS data frame had a bigger window.
    execute_by = ['id']
    def _calc(self, df):
        df = df.copy()
        lat = df[self.input_item_lat][1:]
        prev_lat = df[self.input_item_lat].shift()[1:].rename('prev_lat')
        lon = df[self.input_item_lon][1:]
        prev_lon = df[self.input_item_lon].shift()[1:].rename('prev_lon')
        latlon = pd.concat([lat, lon, prev_lat, prev_lon], axis=1)
        df[self.output_item] = latlon.apply(_calc_dist, axis=1)
        return df
    '''
