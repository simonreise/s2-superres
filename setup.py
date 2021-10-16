import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
	name = 's2-superres',
	version = '0.0.1',
	author = 'Mikhail Moskovchenko',
	author_email = 'moskovchenkomike@gmail.com',
	description = 'Sentinel-2 superresolution',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	url = 'https://github.com/simonreise/s2-superres',
	project_urls = {
		'Bug Tracker': 'https://github.com/simonreise/s2-superres/issues'
	},
	classifiers = [
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Environment :: GPU :: NVIDIA CUDA',
		'Topic :: Scientific/Engineering :: GIS'
	],
	package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    setup_requires=['cython', 'numpy'],
    install_requires=[ 'numpy', 'h5py', 'tensorflow>=2.3', 'tqdm', 'scikit-image', 'rasterio', 'pyproj'],
    python_requires=">=3.7",
)