from setuptools import setup, find_packages

setup(
    name='pris',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'opencv-python==4.3.0.38',
        'scikit-learn'
    ],
    author='long',
    description='Photometric Stereo Package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/flzt11/TEST',  # 修改为你的 GitHub 仓库地址
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)