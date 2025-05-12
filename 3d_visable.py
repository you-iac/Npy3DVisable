from mayavi import mlab
import matplotlib
matplotlib.use('Agg')  # 使用非交互式后端
import numpy as np
import matplotlib
matplotlib.use('Agg')  # 使用非交互式后端
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog
import os
import numpy as np
import matplotlib.pyplot as plt
def select_file():
    # 创建Tkinter根窗口并隐藏
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 弹出文件选择对话框
    file_path = filedialog.askopenfilename(
        title="选择文件",  # 对话框标题
        filetypes=[("所有文件", "*.*")]  # 可选文件类型过滤
    )

    # 关闭Tkinter窗口
    root.destroy()

    return file_path if file_path else None  # 返回路径，取消选择则返回None
if __name__ == "__main__":
    filename = select_file()

    s = np.load(filename)
    print(filename + ":" + str(np.shape(s)))
    #绘制两个方向的切平面
    mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s), #scalar_field获得数据的标量数据场
                                     plane_orientation="x_axes",    #设置切平面的方向
                                     slice_index=462 - 128
                                     )

    mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s),
                                     plane_orientation="y_axes",
                                     slice_index=384
                                     )
    mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s),
                                     plane_orientation="z_axes",
                                     slice_index=512
                                     )
    #为这个数据绘制外框
    mlab.outline()
    mlab.show()



