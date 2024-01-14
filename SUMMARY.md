**Multimodal Material Segmentation Dataset (MCubeS)** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the construction and automotive industries. 

The dataset consists of 2000 images with 347900 labeled objects belonging to 20 different classes including *concrete*, *metal*, *leaf*, and other: *sky*, *wood*, *glass*, *asphalt*, *grass*, *rubber*, *plastic*, *brick*, *ceramic*, *road marking*, *fabric leather*, *sand*, *cobblestone*, *plaster*, *water*, *human body*, and *gravel*.

Images in the Multimodal Material Segmentation dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. All images are labeled (i.e. with annotations). There are 3 splits in the dataset: *train* (1208 images), *test* (408 images), and *val* (384 images). Additionally, images are grouped by ***im id***. Also every image contains information about its ***scene***. Explore it in supervisely supervisely labeling tool. The dataset was released in 2022 by the Graduate School of Informatics, Kyoto, Japan.

<img src="https://github.com/dataset-ninja/multimodal-material-segmentation/raw/main/visualizations/poster.png">
