# my_camera_package/triangulation/triangulation.py

import numpy as np
import cv2

def triangulate_points_nviews(proj_matrices, points_2d):
    """
    使用多個視角的投影矩陣和2D點，計算3D點坐標。
    
    參數:
    - proj_matrices: 投影矩陣列表
    - points_2d: 每個視角的2D點列表
    
    返回:
    - 3D點坐標
    """
    num_views = len(proj_matrices)
    A = np.zeros((num_views * 2, 4))
    for i in range(num_views):
        P = proj_matrices[i]
        x, y = points_2d[i]
        A[2 * i] = x * P[2, :] - P[0, :]
        A[2 * i + 1] = y * P[2, :] - P[1, :]
    
    # SVD 求解
    _, _, Vt = np.linalg.svd(A)
    X = Vt[-1]
    X /= X[3]
    return X[:3]
