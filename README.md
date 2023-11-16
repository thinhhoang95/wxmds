# MDS-WXR Project

# Weather VIL

All the VIL values stored in GRIB2 files are downloaded with the help of the Herbie library. This is achieved by the HRRR_downloader notebook, which in the end, gives us the file hrrr17.tgz. These files need to be copied to HERBIE's temp folder (/root/data/hrrr).

Next, we run the HRRR_preprocessor notebook to filter dates with $VIL \geq 2.5$. It will also crop the array to the predefined Region of Interest (ROI), visualized in the plotting_and_roi notebook. The VIL radar images are then downsampled, named with the time of the storm, and everything is put into a single xarray dataset and saved under the name hrrr17x.zarr. This file is then compressed to yield the hrrr17x.tgz file. In this xarray, the dates attribute contain the date for the VIL image: 1 VIL image = 1 row of the xarray. 

# Trajectory

In the notebook atc_from_hrrr, we load the ZARR. From this, we extract the dates attribute and merge contiguous storms together. This provides the hrrr17x_catalogue_contiguous.csv file. Then we use the traffic library to download ADS-B trajectories corresponding to these contiguous thunderstorm datetime indexed in the catalogue file hrrr17x_catalogue_contiguous.csv. Each csv.gz file name contains the index of the thunderstorm datetime found in the catalogue, like this: hrrr17x_{storm_index}.csv.gz. Then everything is zipped to a tar.gz file, called hrrr17t.tgz.

Next, in the batch_preprocess_trajs notebook, we extract the tgz file. Each trajectory will be filtered for admissible trajectories (landed, not too near), resampled, trimmed and lengthened and then saved to a stx folder. Each file is a compressed npz file, whose name is the date of the thunderstorm, rounded to the timestamp of the trajectory. The trajectory enters the ROI_RADIUS at the later moment indicated on the filename, but not later than 30 minutes. Finally, everything is compressed to a stx17.tgz file.

Next, the mds notebook computes the MDS for all trajectories in the dataset. It outputs two files: mds_catalogue, which indicate the count of MDS points for each thunderstorm datetime. The thunderstorm datetime is then matched to each point through this information later. The second file is mds_pos.npz, which contains a 19000x2 matrix of MDS points. The row index corresponds to the thunderstorm datetime via the catalogue, as explained earlier.

Finally, we perform clustering of MDS representations with Kmeans in the mds_post_processing notebook. We also slice the original 19000x2 matrix of MDS points to smaller arrays, and each one we save to the bystorm folder, with the filename corresponding to the thunderstorm datetime. Likewise, the cluster label is then saved to bystormlabels folder. We compress everything into a new file called mds.tar.gz, and we will need this file for training with the ml/torch_mlp notebook.

We can move the files with move_bystorm_to_ml notebook in the mds folder (this is deprecated, due to the fact that we have use the .tar.gz file in the previous step).