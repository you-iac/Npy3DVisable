import numpy as np
from mayavi import mlab

if __name__ == "__main__":
    s = np.load("D:/0.npy")
    #绘制两个方向的切平面
    mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s), #scalar_field获得数据的标量数据场
                                     plane_orientation="x_axes",    #设置切平面的方向
                                     slice_index=500
                                     )

    mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s),
                                     plane_orientation="y_axes",
                                     slice_index=100
                                     )
    mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s),
                                     plane_orientation="z_axes",
                                     slice_index=100
                                     )
    #为这个数据绘制外框
    mlab.outline()
    mlab.show()