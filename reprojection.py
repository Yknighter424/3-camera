# my_camera_package/reprojection/reprojection.py

import numpy as np
import cv2

def reproject_points(points_3d, rvec, tvec, mtx, dist):
    """
    重新投影3D點到2D圖像平面。
    
    參數:
    - points_3d: 3D點坐標
    - rvec: 旋轉向量
    - tvec: 平移向量
    - mtx: 相機內參矩陣
    - dist: 畸變係數
    
    返回:
    - 重新投影的2D點坐標
    """
    projected_points, _ = cv2.projectPoints(points_3d, rvec, tvec, mtx, dist)
    return projected_points.reshape(-1, 2)

def calculate_reprojection_error(original_points, projected_points):
    """
    計算重新投影誤差。
    
    參數:
    - original_points: 原始2D點
    - projected_points: 重新投影的2D點
    
    返回:
    - 每個點的誤差
    - 平均誤差
    """
    errors = np.linalg.norm(original_points - projected_points, axis=1)
    mean_error = np.mean(errors)
    return errors, mean_error
