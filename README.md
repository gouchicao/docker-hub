# Docker Hub
[狗吃草 Docker Hub](https://hub.docker.com/u/gouchicao)

## 使用
```bash
# Pull Image
docker pull gouchicao/<image list name>

# Run 需要GPU的要使用--runtime=nvidia
docker run --runtime=nvidia -it --rm gouchicao/<image list name>
```

## Image List

### 框架＆工具
* [tensorflow:2.2.0-gpu-jupyter-opencv-pillow-wget-git-nano](dockerfile/tensorflow2.2.0-gpu-jupyter-opencv4-pillow-wget-curl-git-nano)
* [tensorflow:2.3.0-gpu-jupyter-opencv-pillow-wget-git-nano](dockerfile/tensorflow2.3.0-gpu-jupyter-opencv4-pillow-wget-curl-git-nano)
* [tensorflow2-yolov4-tflite](dockerfile/tensorflow2-yolov4-tflite)
* [keras-retinanet](https://github.com/gouchicao/keras-retinanet/blob/master/Dockerfile)

### 软路由
* [lede](dockerfile/openwrt-lede)
    * [lede:x86 带编译环境](dockerfile/openwrt-lede-x86)
    * [lede:x86-bin](dockerfile/openwrt-lede-x86-bin)
