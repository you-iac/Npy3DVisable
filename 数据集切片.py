

import numpy as np
import os

def generate_slices(input_path, output_dir):
    """
    生成三维数据的三个维度切片
    :param input_path: 输入.npy文件路径
    :param output_dir: 输出目录
    """
    img_list = []
    for item in os.listdir(input_path):
        img_list.append(os.path.join(input_path, item))
        # 加载数据
        data = np.load(os.path.join(input_path, item))
        if data.ndim != 3 or data.shape[0] != 128 or data.shape[1] != 128 or data.shape[2] != 128:
            raise ValueError("输入文件必须是128x128x128的三维数组")
        # 获取原始文件名（不带后缀）
        base_name = os.path.splitext(item)[0]
        # 创建输出目录
        os.makedirs(output_dir, exist_ok=True)
        print("处理:"+item)
        # 遍历三个维度
        for axis in ['x', 'y', 'z']:
            for idx in range(128):
                # 提取切片
                if axis == 'x':
                    slice_data = data[idx, :, :]
                elif axis == 'y':
                    slice_data = data[:, idx, :]
                elif axis == 'z':
                    slice_data = data[:, :, idx]

                # 生成文件名
                slice_name = f"{base_name}_{axis}_{idx:03d}.npy"
                output_path = os.path.join(output_dir, slice_name)

                # 保存切片
                np.save(output_path, slice_data)


    # 加载数据
    # data = np.load(input_path)
    # if data.ndim != 3 or data.shape[0] != 128 or data.shape[1] != 128 or data.shape[2] != 128:
    #     raise ValueError("输入文件必须是128x128x128的三维数组")
    #
    # # 获取原始文件名（不带后缀）
    # base_name = os.path.splitext(os.path.basename(input_path))[0]
    #
    # # 创建输出目录
    # os.makedirs(output_dir, exist_ok=True)
    #
    # # 遍历三个维度
    # for axis in ['x', 'y', 'z']:
    #     for idx in range(128):
    #         # 提取切片
    #         if axis == 'x':
    #             slice_data = data[idx, :, :]
    #         elif axis == 'y':
    #             slice_data = data[:, idx, :]
    #         elif axis == 'z':
    #             slice_data = data[:, :, idx]
    #
    #         # 生成文件名
    #         slice_name = f"{base_name}_{axis}_{idx:03d}.npy"
    #         output_path = os.path.join(output_dir, slice_name)
    #
    #         # 保存切片
    #         np.save(output_path, slice_data)

if __name__ == "__main__":

    input_dir  = "D:/data_3D_800/train/y"
    output_dir = "D:/data_3D_800/train/y2d"
    # 执行切片生成
    generate_slices(input_dir, output_dir)
