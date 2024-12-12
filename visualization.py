# my_camera_package/utils/visualization.py

import cv2
import matplotlib.pyplot as plt

def visualize_reprojection(image, original_points, projected_points, errors, window_name):
    """
    可視化重新投影結果。
    
    參數:
    - image: 原始圖像
    - original_points: 原始2D點
    - projected_points: 重新投影的2D點
    - errors: 誤差值
    - window_name: 顯示窗口名稱
    """
    desired_display_size = (900, 700)  # (寬度, 高度)
    scale_x = desired_display_size[0] / image.shape[1]
    scale_y = desired_display_size[1] / image.shape[0]
    image_resized = cv2.resize(image, desired_display_size, interpolation=cv2.INTER_AREA)
    original_points_scaled = original_points.copy()
    original_points_scaled[:, 0] *= scale_x
    original_points_scaled[:, 1] *= scale_y
    projected_points_scaled = projected_points.copy()
    projected_points_scaled[:, 0] *= scale_x
    projected_points_scaled[:, 1] *= scale_y
    image_copy = image_resized.copy()
    for idx, (orig_pt, proj_pt, error) in enumerate(zip(original_points_scaled, projected_points_scaled, errors)):
        x_orig, y_orig = int(orig_pt[0]), int(orig_pt[1])
        x_proj, y_proj = int(proj_pt[0]), int(proj_pt[1])
        # 繪製原始點（藍色）
        cv2.circle(image_copy, (x_orig, y_orig), 5, (255, 0, 0), -1)
        # 繪製重投影點（綠色）
        cv2.circle(image_copy, (x_proj, y_proj), 5, (0, 255, 0), -1)
        # 顯示誤差值
        cv2.putText(image_copy, f"{error:.2f}", (x_orig, y_orig - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    # 轉換顏色空間以在 Matplotlib 中正確顯示
    image_rgb = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(12, 8))
    plt.imshow(image_rgb)
    plt.title(window_name)
    plt.axis('off')
    plt.show()
