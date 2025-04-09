import numpy as np
from mayavi import mlab
from scipy.ndimage import binary_dilation, binary_erosion
if __name__ == "__main__":
    # s = np.load("D:/data/PCB10011008700.npy")
    # s = np.load("D:\data/UNetPP_800_50/numpy/kerry3d.npy")
    s = np.load("D:\PCB10011008700_R.npy")
    # s = s + f*50
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
    # mlab.outline()
    mlab.show()