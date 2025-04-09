import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class NPyViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NPY 文件查看器")

        # 创建界面组件
        self.create_widgets()

    def create_widgets(self):
        # 文件选择按钮
        self.btn_open = tk.Button(
            self.root,
            text="选择 .npy 文件",
            command=self.open_file
        )
        self.btn_open.pack(pady=10)

        # 图像显示区域
        self.fig = plt.figure(figsize=(6, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def open_file(self):
        # 弹出文件选择对话框
        file_path = filedialog.askopenfilename(
            title="选择 .npy 文件",
            filetypes=[("NumPy 文件", "*.npy"), ("所有文件", "*.*")]
        )

        if not file_path:  # 用户取消选择
            return

        try:
            # 加载数据
            data = np.load(file_path)
            if data.ndim != 2:
                raise ValueError("文件必须是二维数组")

            # 清空旧图像
            self.fig.clf()

            # 绘制新图像
            ax = self.fig.add_subplot(111)
            im = ax.imshow(data, cmap='gray')
            self.fig.colorbar(im, ax=ax)
            ax.set_title(f"文件: {file_path}")
            ax.axis('off')

            # 更新画布
            self.canvas.draw()

        except Exception as e:
            # 错误提示弹窗
            tk.messagebox.showerror(
                "错误",
                f"无法加载文件:\n{str(e)}"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = NPyViewerApp(root)
    root.mainloop()