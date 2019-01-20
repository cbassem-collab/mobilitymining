"""
Example of animation and dynamic camera adjustment
"""
from geoplotlib.layers import BaseLayer
from geoplotlib.core import BatchPainter
import geoplotlib
from geoplotlib.utils import BoundingBox, read_csv
import numpy as np


class TrailsLayer(BaseLayer):
        

    def __init__(self):
        self.data = read_csv('Data_CSV/000/20081023025304.csv')
        self.i = 0
        self.t = self.data['timestamp'][self.i]
        self.painter = BatchPainter()


    def draw(self, proj, mouse_x, mouse_y, ui_manager):
        self.painter = BatchPainter()
        self.painter.set_color([0,0,255])
        #print(list(self.data['timestamp'])[self.i:(self.i+10)])
        df = self.data.range(self.i, self.i + 30)
        proj.fit(BoundingBox.from_points(lons=self.data['longtitude'], lats=self.data['latitude']), max_zoom=14)
        x, y = proj.lonlat_to_screen(df['longtitude'], df['latitude'])
        print(df['timestamp'])
        self.painter.linestrip(x, y, 10)
        self.i += 1
        try:
            self.t = self.data['timestamp'][self.i]
        except IndexError:
            self.i = 0
            self.t = self.data['timestamp'][self.i]

        self.painter.batch_draw()
        ui_manager.info(self.t)


geoplotlib.add_layer(TrailsLayer())
geoplotlib.show()
