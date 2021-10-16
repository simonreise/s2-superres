from s2_superres.superres.superres import Superresolution


def s2_superres(input_dir, output_dir = input_dir, copy_original_bands = True, clip_to_aoi = False, geometry = None, bounds = None):
    Superresolution(input_dir = input_dir, output_dir = output_dir, copy_original_bands = copy_original_bands, clip_to_aoi = clip_to_aoi, geometry = geometry, bounds = bounds).start()