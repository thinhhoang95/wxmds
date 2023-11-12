# Coordinate of KDFW
KDFW = [-96.973496106, 32.584330996] # lon, lat

# WXR region of interest, check the _plotting_and_roi.ipynb for details
# WX_ROI = [(-103, -90.5), (26.5, 38)] # lon, lat
WX_ROI = [(KDFW[0] - 3, KDFW[0] + 3), (KDFW[1] - 3, KDFW[1] + 3)] # lon, lat

ROI_RADIUS = 200 # in km