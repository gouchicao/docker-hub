# Docker Hub
[狗吃草 Docker Hub](https://hub.docker.com/u/gouchicao)

## 使用
```bash
# Pull Image
docker pull gouchicao/<image list name>

# Run 需要GPU的要使用--runtime=nvidia
docker run --runtime=nvidia -it --rm gouchicao/<image list name>
```

## 操作系统
* [ubuntu20.04](dockerfile/ubuntu20.04)
    ```
    git wget curl nano cmake tree htop g++ opencv4 Pillow 
    cython scikit-image scikit-learn scipy numpy matplotlib pandas requests tqdm easydict
    ```

## 框架
* [tensorflow:2.2.0-gpu-jupyter-opencv-pillow-wget-git-nano](dockerfile/tensorflow2.2.0-gpu-jupyter-opencv4-pillow-wget-curl-git-nano)
* [tensorflow:2.3.0-gpu-jupyter](dockerfile/tensorflow2.3.0-gpu-jupyter-opencv4-pillow-wget-curl-git-nano)
    ```
    git wget curl nano cmake tree htop g++ opencv4 Pillow
    ```
* [horovod](dockerfile/horovod)

## 目标检测框架
* [TensorFlow2 Object Detection API](dockerfile/tensorflow-object_detection)

## 算法 
* [keras-retinanet](https://github.com/gouchicao/keras-retinanet/blob/master/Dockerfile)
* [efficientdet](https://github.com/gouchicao/efficientdet/blob/master/dockerfile/efficientdet)

## 软路由
* [lede](dockerfile/openwrt-lede)
    * [lede:x86 带编译环境](dockerfile/openwrt-lede-x86)
    * [lede:x86-bin](dockerfile/openwrt-lede-x86-bin)

## 实验
* [tensorflow2-yolov4-tflite](dockerfile/tensorflow2-yolov4-tflite)
* [insightface-cpu](dockerfile/insightface-cpu)
