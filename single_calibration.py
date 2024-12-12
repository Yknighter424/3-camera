# my_camera_package/calibration/single_calibration.py

import cv2
import numpy as np
import glob

def single_camera_calibration(
    chessboard_size=(9, 6),
    square_size=1.0,
    image_paths_left=None,
    image_paths_center=None,
    image_paths_right=None,
    image_size=(1920, 1200),
    save_path='single_camera_calibration.npz'
):
    """
    執行單相機校正，並保存校正結果。
    
    參數:
    - chessboard_size: 棋盤格內角點數量 (寬, 高)
    - square_size: 棋盤格方格尺寸
    - image_paths_*: 三個相機的圖像路徑列表
    - image_size: 圖像尺寸 (寬, 高)
    - save_path: 校正結果保存路徑
    """
    nx, ny = chessboard_size
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 1e-5)
    
    # 準備物體點
    objp = np.zeros((ny * nx, 3), np.float32)
    objp[:, :2] = np.mgrid[0:nx, 0:ny].T.reshape(-1, 2) * square_size
    
    objpoints = []
    imgpoints_left = []
    imgpoints_center = []
    imgpoints_right = []
    
    # 加載並排序圖像
    image_paths_left = sorted(glob.glob(image_paths_left))
    image_paths_center = sorted(glob.glob(image_paths_center))
    image_paths_right = sorted(glob.glob(image_paths_right))
    
    for i in range(len(image_paths_left)):
        img_left = cv2.imread(image_paths_left[i])
        img_center = cv2.imread(image_paths_center[i])
        img_right = cv2.imread(image_paths_right[i])
        
        ret_left, corners_left = cv2.findChessboardCorners(img_left, (nx, ny), None)
        ret_center, corners_center = cv2.findChessboardCorners(img_center, (nx, ny), None)
        ret_right, corners_right = cv2.findChessboardCorners(img_right, (nx, ny), None)
        
        print(f"Processing image set {i+1}:")
        print(f"  Left corners found: {ret_left}")
        print(f"  Center corners found: {ret_center}")
        print(f"  Right corners found: {ret_right}")
        
        if ret_left and ret_center and ret_right:
            corners_left = cv2.cornerSubPix(cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY), 
                                           corners_left, (11, 11), (-1, -1), criteria)
            corners_center = cv2.cornerSubPix(cv2.cvtColor(img_center, cv2.COLOR_BGR2GRAY), 
                                             corners_center, (11, 11), (-1, -1), criteria)
            corners_right = cv2.cornerSubPix(cv2.cvtColor(img_right, cv2.COLOR_BGR2GRAY), 
                                            corners_right, (11, 11), (-1, -1), criteria)
            
            objpoints.append(objp)
            imgpoints_left.append(corners_left)
            imgpoints_center.append(corners_center)
            imgpoints_right.append(corners_right)
    
    # 校正每個相機
    ret_left, mtx_left, dist_left, rvecs_left, tvecs_left = cv2.calibrateCamera(
        objpoints, imgpoints_left, image_size, None, None)
    ret_center, mtx_center, dist_center, rvecs_center, tvecs_center = cv2.calibrateCamera(
        objpoints, imgpoints_center, image_size, None, None)
    ret_right, mtx_right, dist_right, rvecs_right, tvecs_right = cv2.calibrateCamera(
        objpoints, imgpoints_right, image_size, None, None)
    
    print("Calibration results:")
    print("Left camera:", ret_left)
    print("Center camera:", ret_center)
    print("Right camera:", ret_right)
    
    # 保存校正結果
    np.savez(save_path,
             mtx_left=mtx_left, dist_left=dist_left,
             rvecs_left=rvecs_left, tvecs_left=tvecs_left,
             mtx_center=mtx_center, dist_center=dist_center,
             rvecs_center=rvecs_center, tvecs_center=tvecs_center,
             mtx_right=mtx_right, dist_right=dist_right,
             rvecs_right=rvecs_right, tvecs_right=tvecs_right,
             image_size=image_size)
    
    print(f"Calibration results saved to {save_path}")
    return {
        'mtx_left': mtx_left, 'dist_left': dist_left,
        'mtx_center': mtx_center, 'dist_center': dist_center,
        'mtx_right': mtx_right, 'dist_right': dist_right
    }
