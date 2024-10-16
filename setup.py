from setuptools import setup

setup(
    name='Sickle_Cell',
    version='1.0',
    packages=[''],
    package_dir={'': 'src'},
    url='https://github.com/AsishKumar/Sickle-Cell-Anemia-Detection',
    author='Asish Kumar',
    author_email='officialasishkumar@gmail.com',
    description='Computer Vision Sickle Cell Anemia Detection',
    install_requires = [
        "matplotlib",
        "opencv-python",
        "numpy",
        "scikit-image",
        "scikit-learn",
        "pillow",
        "scipy"
    ]
)
