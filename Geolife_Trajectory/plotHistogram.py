"""
	Draw 2D histogram of one person
"""
from os import listdir
from os.path import join
import geoplotlib
from geoplotlib.utils import read_csvs, BoundingBox

#Plotting person 000
path = "Data_CSV/000"
dirs = list(map(lambda p: join(path,p),listdir(path)))

data = read_csvs(dirs)
data.rename({"longtitude": "lon", "latitude":"lat"})

geoplotlib.hist(data, colorscale='sqrt', binsize=8)
geoplotlib.set_bbox(BoundingBox.from_points(lons=data['lon'], lats=data['lat']))
geoplotlib.show()