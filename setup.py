# setup.py

# setup.py

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='my_camera_package',  # 包的名稱
    version='0.1.0',           # 版本號
    author='您的名字',
    author_email='您的郵箱',
    description='一個用於多相機校正和3D重建的Python套件',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Yknighter424/3-camera/upload/main',  # 項目網址
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # 根據您的選擇修改
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'opencv-python',
        'numpy',
        'scipy',
        'glob2',  # 注意：標準庫中已經有 glob 模組，通常不需要安裝 glob2
        'mediapipe',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'run_calibration=scripts.run_calibration:main',
        ],
    },
)
