import os
import shutil
from urllib.parse import unquote, urlparse

import matplotlib.image
import numpy as np
import supervisely as sly
from cv2 import connectedComponents
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import get_file_name, get_file_name_with_ext, mkdir, remove_dir
from tqdm import tqdm

import src.settings as s


def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

        fsize = api.file.get_directory_size(team_id, teamfiles_dir)
        with tqdm(
            desc=f"Downloading '{file_name_with_ext}' to buffer...",
            total=fsize,
            unit="B",
            unit_scale=True,
        ) as pbar:
            api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                fsize = api.file.get_directory_size(team_id, teamfiles_dir)
                with tqdm(
                    desc=f"Downloading '{file_name_with_ext}' to buffer...",
                    total=fsize,
                    unit="B",
                    unit_scale=True,
                ) as pbar:
                    api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)
            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path


def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    ### Function should read local dataset and upload it to Supervisely project, then return project info.###
    images_path = (
        "/home/alex/DATASETS/TODO/multimodal-material-segmentation/multimodal_dataset/polL_color"
    )
    material_masks_path = (
        "/home/alex/DATASETS/TODO/multimodal-material-segmentation/multimodal_dataset/GT"
    )
    nir_path = (
        "/home/alex/DATASETS/TODO/multimodal-material-segmentation/multimodal_dataset/NIR_warped"
    )

    dopl_pathes = (
        "/home/alex/DATASETS/TODO/multimodal-material-segmentation/multimodal_dataset/polL_dolp"
    )
    aopl_pathes = (
        "/home/alex/DATASETS/TODO/multimodal-material-segmentation/multimodal_dataset/polL_aolp_sin"
    )

    dataset_path = "/home/alex/DATASETS/TODO/multimodal-material-segmentation/multimodal_dataset"

    # train + val + test == 439 image name, 500 images in real. So train == all - val - test
    val_names_path = "/home/alex/DATASETS/TODO/multimodal-material-segmentation/multimodal_dataset/list_folder/val.txt"
    test_names_path = "/home/alex/DATASETS/TODO/multimodal-material-segmentation/multimodal_dataset/list_folder/test.txt"

    batch_size = 15
    group_tag_name = "im id"
    images_ext = ".png"

    def create_ann(image_path):
        labels = []
        tags = []
        group_tag = sly.Tag(group_tag_meta, value=get_file_name(image_path))
        tags.append(group_tag)

        img_height = 1024  # ann_np.shape[0]
        img_wight = 1224  # ann_np.shape[1]

        image_name = get_file_name_with_ext(image_path)

        scene_value = image_name[8:-15]
        scene = sly.Tag(scene_meta, value=scene_value)
        tags.append(scene)

        material_mask_path = os.path.join(material_masks_path, image_name)
        ann_np = sly.imaging.image.read(material_mask_path)[:, :, 0]
        unique_pixels = np.unique(ann_np)
        for pixel in unique_pixels:
            obj_class = idx_to_class.get(pixel)
            if obj_class is not None:
                mask = ann_np == pixel
                ret, curr_mask = connectedComponents(mask.astype("uint8"), connectivity=8)
                for i in range(1, ret):
                    obj_mask = curr_mask == i
                    curr_bitmap = sly.Bitmap(obj_mask)
                    if curr_bitmap.area > 50:
                        curr_label = sly.Label(curr_bitmap, obj_class)
                        labels.append(curr_label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=tags)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    group_tag_meta = sly.TagMeta(group_tag_name, sly.TagValueType.ANY_STRING)
    scene_meta = sly.TagMeta("scene", sly.TagValueType.ANY_STRING)
    meta = sly.ProjectMeta(tag_metas=[group_tag_meta, scene_meta])

    # https://github.com/kyotovision-public/multimodal-material-segmentation/blob/main/dataloaders/utils.py
    color_to_material = {
        (44, 160, 44): "asphalt",
        (31, 119, 180): "concrete",
        (255, 127, 14): "metal",
        (214, 39, 40): "road marking",
        (140, 86, 75): "fabric leather",
        (127, 127, 127): "glass",
        (188, 189, 34): "plaster",
        (255, 152, 150): "plastic",
        (23, 190, 207): "rubber",
        (174, 199, 232): "sand",
        (196, 156, 148): "gravel",
        (197, 176, 213): "ceramic",
        (247, 182, 210): "cobblestone",
        (199, 199, 199): "brick",
        (219, 219, 141): "grass",
        (158, 218, 229): "wood",
        (57, 59, 121): "leaf",
        (107, 110, 207): "water",
        (156, 158, 222): "human body",
        (99, 121, 57): "sky",
    }

    os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH")

    idx_to_class = {}
    idx = 0
    for color, name in color_to_material.items():
        obj_class = sly.ObjClass(name, sly.Bitmap, color=color)
        idx_to_class[idx] = obj_class
        idx += 1
        meta = meta.add_obj_class(obj_class)

    api.project.update_meta(project.id, meta.to_json())
    api.project.images_grouping(id=project.id, enable=True, tag_name=group_tag_name)

    val_names = []
    with open(val_names_path) as f:
        content = f.read().split("\n")
        val_names = [im_name + images_ext for im_name in content if len(im_name) > 0]

    test_names = []
    with open(test_names_path) as f:
        content = f.read().split("\n")
        test_names = [im_name + images_ext for im_name in content if len(im_name) > 0]

    all_names = os.listdir(images_path)

    train_names = list(set(all_names) - set(val_names) - set(test_names))

    ds_name_to_images = {"train": train_names, "val": val_names, "test": test_names}

    for ds_name, images_names in ds_name_to_images.items():
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

        for img_names_batch in sly.batched(images_names, batch_size=batch_size):
            pathes_batch = []
            names_batch = []
            temp_folder_dopl = os.path.join(dataset_path, "temp_dopl")
            temp_folder_aopl = os.path.join(dataset_path, "temp_aopl")
            mkdir(temp_folder_dopl)
            mkdir(temp_folder_aopl)
            for image_name in img_names_batch:
                names_batch.append(image_name)
                pathes_batch.append(os.path.join(images_path, image_name))
                nir_im_name = "nir_" + image_name
                names_batch.append(nir_im_name)
                pathes_batch.append(os.path.join(nir_path, image_name))

                dopl_im_name = "dolp_" + image_name
                names_batch.append(dopl_im_name)
                dopl_path = os.path.join(dopl_pathes, get_file_name(image_name) + ".npy")
                dolp_np = np.load(dopl_path)
                temp_dopl_path = os.path.join(temp_folder_dopl, dopl_im_name)
                matplotlib.image.imsave(temp_dopl_path, dolp_np)
                pathes_batch.append(temp_dopl_path)

                aopl_im_name = "aolp_" + image_name
                names_batch.append(aopl_im_name)
                aopl_path = os.path.join(aopl_pathes, get_file_name(image_name) + ".npy")
                aolp_np = np.load(aopl_path)
                temp_aopl_path = os.path.join(temp_folder_aopl, aopl_im_name)
                matplotlib.image.imsave(temp_aopl_path, aolp_np)
                pathes_batch.append(temp_aopl_path)

            img_infos = api.image.upload_paths(dataset.id, names_batch, pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = []
            for i in range(0, len(pathes_batch), 4):
                ann = create_ann(pathes_batch[i])
                anns.extend([ann, ann, ann, ann])

            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(img_names_batch))

            remove_dir(temp_folder_dopl)
            remove_dir(temp_folder_aopl)

    return project
