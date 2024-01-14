The authors realized ***Multimodal Material Segmentation Dataset (MCubeS)*** from RGB, polarization, and near-infrared images. They introduced the MCubeS dataset, which contains 500 sets of multimodal images capturing 42 street scenes. The ability to identify materials based on their visual characteristics is crucial for computer vision applications, particularly those involving real-world interactions. Material segmentation, which involves the precise recognition of materials on a per-pixel basis, presents a significant challenge. Unlike objects, materials don't display distinct visual signatures in regular RGB appearances. However, diverse materials exhibit varying radiometric behaviors, which can be effectively captured using non-RGB imaging modalities. Ground truth annotations for material segmentation and semantic segmentation are provided for each image and pixel.

While advancements in object recognition enable computers to accurately identify objects in images, our human visual system goes beyond mere object identification. It can distinguish between a paper cup and a ceramic one, allowing us to plan our interactions before physically engaging with the objects. If computers could similarly discern the composition of an object, critical decisions could be made more swiftly and accurately. The task of densely recognizing materials at a pixel level in an image becomes imperative. Successful material segmentation holds particular benefits for road scene analysis, enabling an autonomous vehicle or advanced driver assistance system (ADAS) to differentiate between an asphalt road and a concrete one or identify a leaf on the road versus dirt, facilitating safer control.

Despite the significant progress in object recognition, outdoor material segmentation remains challenging due to the diverse range of materials encountered in the real world and the lack of annotated data. The complexity of material segmentation is compounded by the absence of well-defined visual features in regular RGB images for materials, in contrast to objects that often exhibit distinct shapes, contours, and surface textures.

## Dataset creation

The authorts realize multimodal material segmentation, the recognition of per-pixel material categories from a set of images from the same vantage point but of different imaging modalities. In particular, they consider the combination of regular RGB, polarization, and near-infrared images at each instance. They build an imaging system consisting of a binocular stereo of quad-Bayer RGB polarization cameras, a monocular near-infrared camera, and a LiDAR to capture outdoor road scenes.  In addition to materials, the authors also annotated semantic segmentation labels.

<img src="https://github.com/dataset-ninja/multimodal-material-segmentation/assets/120389559/c17b6d2d-54d5-4a68-a882-88b22004836e" alt="image" width="1200">

<span style="font-size: smaller; font-style: italic;">Per-pixel recognition of materials from multiple imaging modalities.</span>


MCubeS comprehensively captures the visual attributes of diverse materials encountered in everyday outdoor settings, observed from viewpoints situated on roads, pavements, or sidewalks. Employing three distinct imaging modalities—RGB, polarization, and near-infrared (NIR)—the authors obtained images at each viewpoint. The primary challenges revolved around achieving systematic image capture with precise spatio-temporal alignment and subsequent annotation with pixel-wise categorization of materials.

In the real world, surfaces composed of different materials exhibit unique subsurface compositions and surface structures at the mesoscopic scale. These distinctions result in varying behaviors of incident light, notably influencing its reflection, refraction, and absorption. Such differences are particularly evident in polarization properties, encompassing varying degrees of linear polarization (DoLP) or angles of linear polarization (AoLP), as well as in the absorption of NIR light. The MCubeS dataset meticulously captures these intricate radiometric characteristics of diverse materials through a camera system that integrates a stereo pair of RGB-polarization (RGB-P) cameras and a near-infrared (NIR) camera. Additionally, the image capture system features LiDAR technology to enhance label propagation accuracy.

<img src="https://github.com/dataset-ninja/multimodal-material-segmentation/assets/120389559/1b4cb415-7766-45b6-9653-41c4302ed509" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Example multimodal images from the MCubeS Dataset. Different imaging modalities capture characteristic radiometric behaviors of different materials.</span>

## Dataset description

The MCubeS dataset comprises two distinct categories of image sequences. The first type involves continuous forward movement of the imaging system, replicating the viewpoint of a moving vehicle. The second type consists of sequences captured at a stationary position while the imaging system pans, facilitating the inclusion of materials such as water, which are infrequently observed in road scenes. This second type of data enhances the diversity of sample images, particularly for less common materials.

The dataset encompasses 42 scenes of the first type (continuous forward movement), sampled at three frames per second, with an average sequence length of 309 seconds. The raw image sequences total 26,650 image sets, from which 424 image sets, evenly spaced in time, were annotated. Additionally, 19 scenes were captured for the second type of data (fixed-location panning). For each scene, eight image sets were acquired, covering a 360-degree view, and a total of 76 image sets from these sequences were annotated. Overall, the dataset includes 500 annotated image sets. The authors defined 20 distinct materials through a thorough examination of the data within the MCubeS dataset.

<img src="https://github.com/dataset-ninja/multimodal-material-segmentation/assets/120389559/e3135a9c-b032-4782-86f2-76351b5f9cfc" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Example regions for each class. The actual images are annotated densely for all pixels. Human body (skin
and hair), leaf, grass, and sky are object and stuff names selected to represent their unique materials.</span>


MCubeS scenes predominantly feature roadways and sidewalks, encompassing diverse elements ranging from pavements and roads to various objects like bicycles and manholes. Notably, these elements can be composed of distinct materials, even within the same category. For instance, pavements may be constructed from _asphalt_, _concrete_, _brick_, _cobblestone_, _gravel_, or _sand_. Special attention is given to _road markings_ and manholes, considering them as distinct materials due to their significance in driving scenarios. Vehicles are primarily constructed with _metal_, _rubber_, and _glass_ components. Human attire is labeled as _fabric_, attributes almost exclusive to people. In the case of natural elements, trees and _grass_ are prevalent in the scenes, with _wood_ and _leaves_ designated as material labels for trees (as _wood_) and fallen leaves (as leaves). _Water_, found in puddles, rivers, and ponds, is another noteworthy material.

The category encompasses materials like _ceramic_, _plaster_, _plastic_, and _sky_, which, while common, have lesser occurrences or significance in driving scenarios. The authors diligently annotate every image with per-pixel material classes. Initially, they annotate the left RGB image and subsequently propagate per-pixel labels to other views of the same frame. Additionally, a dense depth image for the left RGB-P camera is reconstructed by integrating RGB stereo and LiDAR 3D points.

<img src="https://github.com/dataset-ninja/multimodal-material-segmentation/assets/120389559/7fbb57f6-45d2-4130-9c5f-b0e43390da44" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">MCubeS dataset spans a wide range of road scenes (top row), including river sidewalks to railroad tracks, each densely annotated with materials (bottom row).</span>