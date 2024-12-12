# scripts/run_calibration.py

import argparse
from single_calibration import single_camera_calibration
from triple_calibration import global_triangulation_optimization

def main():
    parser = argparse.ArgumentParser(description='Run camera calibration.')
    parser.add_argument('--single_calib', action='store_true', help='Run single camera calibration.')
    parser.add_argument('--triple_calib', action='store_true', help='Run triple camera calibration.')
    parser.add_argument('--save_path', type=str, default='calibration_results.npz', help='Path to save calibration results.')
    parser.add_argument('--calib_data_path', type=str, default='single_camera_calibration.npz', help='Path to single calibration data.')
    
    args = parser.parse_args()
    
    if args.single_calib:
        calibration_results = single_camera_calibration(
            chessboard_size=(9, 6),
            square_size=3.0,
            image_paths_left=r"D:\20241112\CAM_LEFT\Cam2-*.jpeg",
            image_paths_center=r"D:\20241112\CAM_MIDDLE\Cam1-*.jpeg",
            image_paths_right=r"D:\20241112\CAM_RIGHT\Cam0-*.jpeg",
            image_size=(1920, 1200),
            save_path='single_camera_calibration.npz'
        )
    if args.triple_calib:
        global_triangulation_optimization(
            calib_data_path=args.calib_data_path,
            save_path=args.save_path
        )

if __name__ == '__main__':
    main()
