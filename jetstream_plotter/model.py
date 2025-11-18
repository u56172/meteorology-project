import xarray as xr
import numpy as np

xr.set_options(file_cache_maxsize=1024)

url = {
    'Monday':    'https://nomads.ncep.noaa.gov/dods/gfs_1p00/gfs20251110/gfs_1p00_00z',
    'Tuesday':   'https://nomads.ncep.noaa.gov/dods/gfs_1p00/gfs20251111/gfs_1p00_00z',
    'Wednesday': 'https://nomads.ncep.noaa.gov/dods/gfs_1p00/gfs20251112/gfs_1p00_00z',
    'Thursday':  'https://nomads.ncep.noaa.gov/dods/gfs_1p00/gfs20251113/gfs_1p00_00z',
    'Friday':    'https://nomads.ncep.noaa.gov/dods/gfs_1p00/gfs20251114/gfs_1p00_00z'
}

xrds_week = {}
for day, link in url.items():
    xrds_week[day] = xr.open_dataset(link, decode_times=False)

pressure_levels = [100, 150, 200, 250, 300, 350, 400]

def boundry_box_usa(ds):
    return ds.sel(lon=slice(230, 300), lat=slice(10, 75))

def specific_level(ds, level):
    return ds.sel(lev=level)

def wind_vel(u_wind, v_wind):
    return np.sqrt(u_wind**2 + v_wind**2)
