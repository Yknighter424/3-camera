# my_camera_package/calibration/triple_calibration.py

import cv2
import numpy as np
from scipy.optimize import least_squares

def load_calibration_data(calib_path):
    data = np.load(calib_path)
    return data

def calculate_fov(mtx, image_size):
    fx = mtx[0, 0]
    fy = mtx[1, 1]
    fov_x = 2 * np.arctan(image_size[0] / (2 * fx)) * (180 / np.pi)
    fov_y = 2 * np.arctan(image_size[1] / (2 * fy)) * (180 / np.pi)
    return fov_x, fov_y

def global_triangulation_optimization(calib_data_path, save_path='triple_camera_calibration.npz'):
    """
    執行全局三相機校正（固定內參），並保存結果。
    
    參數:
    - calib_data_path: 單相機校正結果的路徑
    - save_path: 儲存全局校正結果的路徑
    """
    # 加載單相機校正結果
    calib_data = load_calibration_data(calib_data_path)
    mtx_left = calib_data['mtx_left']
    dist_left = calib_data['dist_left']
    mtx_center = calib_data['mtx_center']
    dist_center = calib_data['dist_center']
    mtx_right = calib_data['mtx_right']
    dist_right = calib_data['dist_right']
    
    # 內參列表
    mtx_list = [mtx_left, mtx_center, mtx_right]
    dist_list = [dist_left, dist_center, dist_right]
    
    # 假設您已經有外參的初始估計（例如通過 solvePnP）
    # 此處省略外參的計算步驟，請參考您的代碼進行實現
    
    # 全局優化的具體實現
    # 這裡需要根據您的具體需求來實現優化過程
    
    # 儲存全局校正結果
    np.savez(save_path,
             mtx_left=mtx_left, dist_left=dist_left,
             mtx_center=mtx_center, dist_center=dist_center,
             mtx_right=mtx_right, dist_right=dist_right)
    
    print(f"Global calibration results saved to {save_path}")
