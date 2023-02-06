from distutils.core import setup

setup(
    name='infiniai',
    packages=['infiniai'],
    version='0.0.1',
    license='MIT',
    description='Computer Vision Helping Library',
    author='InfiniAi',
    author_email='info@infiniai.tech',
    url="https://github.com/infiniai-tech/infiniai.git",
    keywords=['ComputerVision', 'HandTracking', 'FaceDetection', 'PoseEstimation','FaceMesh'],
    install_requires=[
        'opencv-python',
        'numpy',
        'mediapipe'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.6',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
)