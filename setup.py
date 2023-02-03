from distutils.core import setup

setup(
    name='infiniai',
    packages=['infiniai'],
    version='0.0.1',
    license='MIT',
    description='Computer Vision Helping Library',
    author='Computer Vision Zone',
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
        'python_requires = ">=3.6"'
    ],
)