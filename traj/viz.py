import numpy as np 
from matplotlib import pyplot as plt
from cartopy import crs as ccrs

KDFW = [-96.973496106, 32.584330996] # lon, lat

def plot_setup():
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(projection=ccrs.LambertConformal())
    ax.coastlines()
    ax.add_feature(ccrs.cartopy.feature.STATES)

    # Set the map bounds
    # ax.set_extent([-120, -70, 20, 55], crs=ccrs.PlateCarree())
    ax.set_extent([-105, -85, 25, 45], crs=ccrs.PlateCarree())

    # KDFW airport
    ax.scatter(KDFW[0], KDFW[1], color='red', transform=ccrs.PlateCarree())
    ax.text(KDFW[0], KDFW[1]+0.75, 'KDFW', color='red', transform=ccrs.PlateCarree())

    # Show the longitude and latitude grid lines
    ax.gridlines(draw_labels=True, linewidth=2, color='gray', alpha=0.5, linestyle='--')

    return fig, ax

def plot_traj(lons, lats, ax = None):
    # Plot the veril using cartopy

    if ax is None:
        fig = plt.figure(figsize=(10, 10))
        ax = plt.axes(projection=ccrs.LambertConformal())
        ax.coastlines()
        ax.add_feature(ccrs.cartopy.feature.STATES)

        # Set the map bounds
        # ax.set_extent([-120, -70, 20, 55], crs=ccrs.PlateCarree())
        ax.set_extent([-105, -85, 25, 45], crs=ccrs.PlateCarree())

    # Plot the trajectory
    ax.plot(lons, lats, color='blue', transform=ccrs.PlateCarree())

def plot_traj_from_df(dfx, callsign, ax = None):
    df = dfx[dfx['callsign'] == callsign]
    lons = df['longitude'].values
    lats = df['latitude'].values
    plot_traj(lons, lats, ax)

def plot_traj_from_np_array(x, ax = None):
    lats = x[0, :]
    lons = x[1, :]
    plot_traj(lons, lats, ax)