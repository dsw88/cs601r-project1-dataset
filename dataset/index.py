import os
THIS_DIR = os.path.dirname(os.path.realpath(__file__))

def __get_image_paths(directory, suffix):
    file_paths = []
    for filename in os.listdir(directory):
        if filename.endswith(suffix):
            file_paths.append(filename)
    return file_paths

def __get_absolute_paths(dir, filenames):
    return list(map(lambda filename: __build_os_path(dir, filename), filenames))

def __build_os_path(*parts):
    return os.path.sep.join(parts)

def get_bird_images_paths():
    images_dir = __build_os_path(THIS_DIR, "birds")
    filenames = __get_image_paths(images_dir, '.jpg')
    return __get_absolute_paths(images_dir, filenames)

def get_butterflies_segmasks_paths():
    segmasks_dir = __build_os_path(THIS_DIR, "butterflies", "segmentations")
    filenames = __get_image_paths(segmasks_dir, '.png')
    return __get_absolute_paths(segmasks_dir, filenames)

def get_butterflies_images_paths():
    images_dir = __build_os_path(THIS_DIR, "butterflies", "images")
    filenames = __get_image_paths(images_dir, '.png')
    return __get_absolute_paths(images_dir, filenames)
