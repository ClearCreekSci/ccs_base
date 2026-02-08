# DBus BLE advertisement
CCS_DBUS_BLE_ADVERT_UUID     = 'a0ce0100-3bbf-11ee-89eb-00e04c400cc5'
# DBus BLE agent
CCS_DBUS_BLE_AGENT_UUID      = 'a0ce0101-3bbf-11ee-89eb-00e04c400cc5'
# Clear Creek Scientific Device Label
CCS_DEVICE_LABEL_UUID        = 'a0ce0120-3bbf-11ee-89eb-00e04c400cc5'
# Clear Creek Scientific Data Service
CCS_DATA_SERVICE_UUID        = 'a0ce0200-3bbf-11ee-89eb-00e04c400cc5'
# Station ID (UTF-8 string, 1-8 characters)
CCS_STATION_ID_UUID          = 'a0ce0201-3bbf-11ee-89eb-00e04c400cc5'
# Air Temperature (measured in celsius) (Characteristic):
CCS_AIR_TEMPERATURE_UUID     = 'a0ce0210-3bbf-11ee-89eb-00e04c400cc5'
# % Humidity (relative humidity) (Characteristic):
CCS_HUMIDITY_UUID            = 'a0ce0211-3bbf-11ee-89eb-00e04c400cc5'
# Barometric Pressure (measured in HectoPascals) (Characteristic):
CCS_AIR_PRESSURE_UUID        = 'a0ce0212-3bbf-11ee-89eb-00e04c400cc5'
# Wind speed (m/s)
CCS_WIND_SPEED_UUID          = 'a0ce0213-3bbf-11ee-89eb-00e04c400cc5'
# Wind direction (measured in degrees from where the wind is blowing. A north wind blows from north to south and is measured as 0°)
CCS_WIND_DIRECTION_UUID      = 'a0ce0214-3bbf-11ee-89eb-00e04c400cc5'
# Precipitation (mm)
CCS_PRECIPITATION_UUID       = 'a0ce0215-3bbf-11ee-89eb-00e04c400cc5'
# Water Temperature (Celsius)
CCS_WATER_TEMPERATURE_UUID   = 'a0ce0216-3bbf-11ee-89eb-00e04c400cc5'
# Water Velocity (m/s)
CCS_WATER_VELOCITY_UUID      = 'a0ce0217-3bbf-11ee-89eb-00e04c400cc5'
# Water Level (depth in m)
CCS_WATER_LEVEL_UUID         = 'a0ce0218-3bbf-11ee-89eb-00e04c400cc5'
# Turbidity (NTU)
CCS_TURBIDITY_UUID           = 'a0ce0219-3bbf-11ee-89eb-00e04c400cc5'

#    Photograph (path to saved graphics file) (Characteristic):
CCS_PHOTOGRAPH_UUID          = 'a0ce0300-3bbf-11ee-89eb-00e04c400cc5'

labels = {
    CCS_AIR_TEMPERATURE_UUID:'Air Temperature',
    CCS_HUMIDITY_UUID:'Relative Humidity',
    CCS_AIR_PRESSURE_UUID:'Air Pressure',
    CCS_WIND_SPEED_UUID :'Wind Speed',
    CCS_WIND_DIRECTION_UUID :'Wind Direction',
    CCS_PRECIPITATION_UUID :'Precipitation',
    CCS_WATER_TEMPERATURE_UUID :'Water Temperature',
    CCS_WATER_VELOCITY_UUID :'Water Velocity',
    CCS_WATER_LEVEL_UUID :'Water Level',
    CCS_TURBIDITY_UUID :'Turbidity',
    CCS_PHOTOGRAPH_UUID:'Photograph',
}
