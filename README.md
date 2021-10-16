# s2-superres
### Sentinel-2 super-resolution preprocesing tool

A package using a convolutional neural network to convert 20 and 60 m resolution Sentinel-2 bands  to 10 m resolution.  
This package is based on [s2-superresolution] by UP42, which is based on [DSen-2] by lanha

## Requirements
- python >= 3.7
- numpy
- tensorflow >= 2.3
- rasterio
- pyproj

## Installation

```
git clone https://github.com/simonreise/s2-superres
cd s2-superres
python setup.py install
```


## Usage
```
from s2_superres import s2_superres

s2_superres(input_dir, output_dir, copy_original_bands, clip_to_aoi, geometry, bounds)
```
- input_dir - path to directory with sentinel-2 product data (both level 1 and level 2 are supported)
- output_dir - path to directory where final product will be saved (as a multiband tif file)
- copy_original_bands - by default all the bands are saved to output file. If set to False, original 10 m bands will not be saved.
- clip_to_aoi - if output image needs to be clipped. Default is false
- geometry - a geometry object to use while clipping
- bounds - bounds to use while clipping
> Note: `- clip_to_aoi` features were imported from s2-superresolution code 'as-is' and were not tested. They could probably work incorrectly, so it is not recommended to use it.



   [s2-superresolution]: <https://github.com/up42/s2-superresolution>
   [DSen-2]: <https://github.com/lanha/DSen2>

