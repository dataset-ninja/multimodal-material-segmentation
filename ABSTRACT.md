The authors of **(MCubeS): Multimodal Material Segmentation Dataset** create it from RGB, polarization, and near-infrared images. Dataset contains 500 sets of multimodal images capturing 42 street scenes. The capacity to discern materials based on their visual attributes is fundamental for computer vision applications, especially those engaged in real-world scenarios. Material segmentation, requiring meticulous identification of materials at a per-pixel level, poses a substantial challenge. Unlike objects, materials lack clear visual signatures in standard RGB representations. Nonetheless, the distinct radiometric behaviors of diverse materials can be aptly captured through alternative imaging modalities beyond RGB. Each image and pixel within the dataset is meticulously annotated with ground truth information for both material segmentation and semantic segmentation.

While advancements in object recognition empower computers to precisely identify objects within images, the human visual system surpasses mere object identification. It possesses the ability to discriminate between, for example, a paper cup and a ceramic one, enabling thoughtful planning of interactions before physical engagement. If computers could emulate this discernment of object composition, critical decisions could be executed with enhanced speed and accuracy. The imperative task of densely recognizing materials at the pixel level in an image arises. Successful material segmentation offers notable advantages for road scene analysis, allowing autonomous vehicles or advanced driver assistance systems (ADAS) to differentiate between an asphalt road and a concrete one, or discern a leaf on the road from dirt, thereby enhancing control safety.

Despite the substantial strides in object recognition, outdoor material segmentation remains challenging due to the myriad materials encountered in the real world and the scarcity of annotated data. The intricacy of material segmentation is heightened by the lack of well-defined visual features in regular RGB images for materials, as opposed to objects that frequently exhibit distinctive shapes, contours, and surface textures.

## Dataset creation

The authorts realize multimodal material segmentation, the recognition of per-pixel material categories from a set of images from the same vantage point but of different imaging modalities. In particular, they consider the combination of regular RGB, polarization, and near-infrared images at each instance. They build an imaging system consisting of a binocular stereo of quad-Bayer RGB polarization cameras, a monocular near-infrared camera, and a LiDAR to capture outdoor road scenes.  In addition to materials, the authors also annotated semantic segmentation labels.

<img src="https://github.com/dataset-ninja/multimodal-material-segmentation/assets/120389559/c17b6d2d-54d5-4a68-a882-88b22004836e" alt="image" width="1200">

<span style="font-size: smaller; font-style: italic;">Per-pixel recognition of materials from multiple imaging modalities.</span>


MCubeS provides a comprehensive depiction of the visual features of various materials found in everyday outdoor environments, observed from viewpoints situated on roads, pavements, and sidewalks. The primary challenges centered around achieving systematic image capture with precise spatio-temporal alignment and subsequent annotation involving pixel-wise categorization of materials.

In the real world, surfaces composed of diverse materials exhibit distinct subsurface compositions and surface structures at the mesoscopic scale. These differences manifest in varying behaviors of incident light, influencing its reflection, refraction, and absorption. These nuances are particularly discernible in polarization properties, including degrees of linear polarization (DoLP) or angles of linear polarization (AoLP), as well as in the absorption of near-infrared (NIR) light. The MCubeS dataset meticulously captures these intricate radiometric characteristics of diverse materials through a camera system integrating a stereo pair of RGB-polarization (RGB-P) cameras and a near-infrared (NIR) camera. Additionally, the image capture system incorporates LiDAR technology to enhance the accuracy of label propagation.

<img src="https://github.com/dataset-ninja/multimodal-material-segmentation/assets/120389559/1b4cb415-7766-45b6-9653-41c4302ed509" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Example multimodal images from the MCubeS Dataset. Different imaging modalities capture characteristic radiometric behaviors of different materials.</span>

## Dataset description

The MCubeS dataset comprises two distinct categories of image sequences. The first type involves continuous forward movement of the imaging system, replicating the viewpoint of a moving vehicle. The second type consists of sequences captured at a stationary position while the imaging system pans, facilitating the inclusion of materials such as water, which are infrequently observed in road scenes. This second type of data enhances the diversity of sample images, particularly for less common materials.

The dataset encompasses 42 scenes of the first type (continuous forward movement), sampled at three frames per second, with an average sequence length of 309 seconds. The raw image sequences total 26,650 image sets, from which 424 image sets, evenly spaced in time, were annotated. Additionally, 19 scenes were captured for the second type of data (fixed-location panning). For each scene, eight image sets were acquired, covering a 360-degree view, and a total of 76 image sets from these sequences were annotated. Overall, the dataset includes 500 annotated image sets. The authors defined 20 distinct materials through a thorough examination of the data within the MCubeS dataset.

<img src="https://github.com/dataset-ninja/multimodal-material-segmentation/assets/120389559/e3135a9c-b032-4782-86f2-76351b5f9cfc" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Example regions for each class. The actual images are annotated densely for all pixels. Human body (skin and hair), leaf, grass, and sky are object and stuff names selected to represent their unique materials.</span>


MCubeS scenes predominantly feature roadways and sidewalks, encompassing diverse elements ranging from pavements and roads to various objects like bicycles and manholes. Notably, these elements can be composed of distinct materials, even within the same category. For instance, pavements may be constructed from _asphalt_, _concrete_, _brick_, _cobblestone_, _gravel_, or _sand_. Special attention is given to _road markings_ and manholes, considering them as distinct materials due to their significance in driving scenarios. Vehicles are primarily constructed with _metal_, _rubber_, and _glass_ components. Human attire is labeled as _fabric_, attributes almost exclusive to people. In the case of natural elements, trees and _grass_ are prevalent in the scenes, with _wood_ and _leaves_ designated as material labels for trees (as _wood_) and fallen leaves (as leaves). _water_, found in puddles, rivers, and ponds, is another noteworthy material.

The category encompasses materials like _ceramic_, _plaster_, _plastic_, and _sky_, which, while common, have lesser occurrences or significance in driving scenarios. The authors diligently annotate every image with per-pixel material classes. Initially, they annotate the left RGB image and subsequently propagate per-pixel labels to other views of the same frame. Additionally, a dense depth image for the left RGB-P camera is reconstructed by integrating RGB stereo and LiDAR 3D points.

<img src="https://github.com/dataset-ninja/multimodal-material-segmentation/assets/120389559/7fbb57f6-45d2-4130-9c5f-b0e43390da44" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">MCubeS dataset spans a wide range of road scenes (top row), including river sidewalks to railroad tracks, each densely annotated with materials (bottom row).</span>

## Imaging modalities


**Polarization** 
Light manifests as a transverse wave, characterized by perpendicular electric and magnetic fields. When the electric field of light lies within a singular plane, it is termed linearly polarized. The orientation angle of polarized light can be defined within the plane perpendicular to the transverse direction. In contrast, unpolarized light comprises electric fields uniformly oriented in all directions.

When the orientations of the electric fields form an ellipse on the plane perpendicular to the transverse direction, the light is considered partially linearly polarized. In this scenario, the major axis of the ellipse defines the angle of polarization, and the ratio of the magnitudes of the major and minor axes is denoted as the degree of polarization. The intensity of partially polarized light, with the angle of linear polarization (AoLP) and the degree of linear polarization (DoLP) measured using a polarization filter, plays a significant role.

**Near-infrared Light** 
Light comprises a spectrum of electromagnetic waves with varying wavelengths, leading to distinctive radiometric behaviors dependent on the wavelength. Objects exhibit diverse colors as their reflection is influenced by wavelength. Simultaneously, the absorption and scattering characteristics of light transmitted into a subsurface or a medium vary based on wavelength. For instance, shorter wavelength light tends to undergo more forward scattering compared to longer wavelength light. The absorption of light experiences pronounced changes, particularly beyond the visual spectrum.

The absorption of light, notably through water—a common element in our daily surroundings, including not just puddles but also natural surfaces like water-containing leaves—is highly sensitive to wavelength. In the near-infrared range spanning from 800nm to 1000nm, the absorption coefficient of light in water exhibits nearly linear growth from 0 to 1. Consequently, for a camera equipped with a near-infrared filter within this wavelength range observing water or water-containing surfaces, varying intensity levels encode the depth or "wetness" of the surface, with darker shades indicating greater depth or wetness.

## Image Capture System

The researchers devised a customized imaging system, affixing it to a cart to capture multimodal sequences of real-world scenes, replicating a viewpoint akin to that of a car. This system is augmented with a sparse LiDAR, strategically incorporated to facilitate the subsequent propagation of annotations across diverse image modalities. The imaging apparatus comprises a duo of RGB-polarization (RGB-P) cameras (LUCID TRI050S-QC, 2/3-inch sensor), an NIR camera (FLIR GS3-U3-41C6NIR-C, 1-inch sensor), and a LiDAR unit (Livox Mid-100).

