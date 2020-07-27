FROM gouchicao/tensorflow:2.2.0-gpu-jupyter-opencv4-pillow-wget-curl-git-nano
LABEL maintainer="wang-junjian@qq.com"

WORKDIR /
RUN git clone https://github.com/fizyr/keras-retinanet.git
RUN mkdir -p /root/.keras/models/ && \
    wget -O /root/.keras/models/ResNet-50-model.keras.h5 https://github.com/fizyr/keras-models/releases/download/v0.0.1/ResNet-50-model.keras.h5

WORKDIR /keras-retinanet
# 提前安装指定版本 keras==2.3.1 解决错误 TypeError: type object got multiple values for keyword argument 'training'
RUN pip install keras==2.3.1 && \
    pip install . && \
    python setup.py build_ext --inplace

COPY voc2csv.py ./
COPY cmd ./
