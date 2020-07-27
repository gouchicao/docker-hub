import os
import sys
import random
import shutil
import argparse
import csv
import xml.etree.ElementTree as ET


def parse_args(args):
    parser = argparse.ArgumentParser(description="Split dataset.")

    parser.add_argument(
        "--data_dir", help="dataset dir.", required=True, type=str
    )
    parser.add_argument(
        "--output_dir", help="output dir", type=str
    )
    parser.add_argument(
        "--ratio", help="Val data ratio. Default value: 0.1", default=0.1, type=float
    )

    return parser.parse_args(args)


def main(args=None):
    # parse arguments
    if args is None:
        args = sys.argv[1:]
    args = parse_args(args)

    data_dir = args.data_dir
    output_dir = args.output_dir
    if not output_dir:
        output_dir = data_dir
    val_ratio = args.ratio

    train_dir = os.path.join(output_dir, "train")
    val_dir = os.path.join(output_dir, "val")

    if os.path.exists(train_dir):
        shutil.rmtree(train_dir)
    if os.path.exists(val_dir):
        shutil.rmtree(val_dir)

    if os.path.exists(os.path.join(output_dir, "train.csv")):
        os.remove(os.path.join(output_dir, "train.csv"))
    if os.path.exists(os.path.join(output_dir, "val.csv")):
        os.remove(os.path.join(output_dir, "val.csv"))
    if os.path.exists(os.path.join(output_dir, "class.csv")):
        os.remove(os.path.join(output_dir, "class.csv"))

    image_name_list = list(
        filter(
            lambda x: not (x.startswith(".") or x.endswith("xml") or x.endswith("csv")),
            os.listdir(data_dir),
        )
    )
    images_num = len(image_name_list)

    os.makedirs(train_dir)
    os.makedirs(val_dir)

    val_list = random.sample(image_name_list, int(val_ratio * images_num))
    train_list = list(set(image_name_list) - set(val_list))

    for train_image_name in train_list:
        train_image = os.path.join(data_dir, train_image_name)
        shutil.copy(train_image, train_dir)
        label_path = os.path.splitext(train_image)[0] + ".xml"
        shutil.copy(label_path, train_dir)

    for val_image_name in val_list:
        val_image = os.path.join(data_dir, val_image_name)
        shutil.copy(val_image, val_dir)
        label_path = os.path.splitext(val_image)[0] + ".xml"
        shutil.copy(label_path, val_dir)

    gen_csv(output_dir)


def gen_csv(output_dir):
    for data_set in ["train", "val"]:
        data_set_dir = os.path.join(output_dir, data_set)
        csv_path = os.path.join(output_dir, "%s.csv" % data_set)

        image_name_list = list(
            filter(
                lambda x: not (x.startswith(".") or x.endswith("xml")),
                os.listdir(data_set_dir),
            )
        )
        anno_list = []
        for image_name in image_name_list:
            image_path = os.path.join(data_set_dir, image_name)
            print("Currently processing: %s" % image_path)
            class_dict, bbox_list, anno_list = read_annotation(data_set, image_path, anno_list)
            print("%s Done!" % image_path)
        with open(csv_path, "w") as f:
            writer = csv.writer(f)
            for row in anno_list:
                writer.writerow(row)

    class_csv_path = os.path.join(output_dir, "class.csv")

    with open(class_csv_path, "w") as f:
        writer = csv.writer(f)
        for k, v in class_dict.items():
            writer.writerow([k, str(v)])


def read_annotation(data_set, image_path, anno_list):
    class_dict = {}
    class_index = 0

    in_file = os.path.splitext(image_path)[0] + ".xml"

    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find("size")

    bbox_list = []

    for obj in root.iter("object"):
        cls = obj.find("name").text

        if cls not in class_dict:
            class_dict[cls] = class_index
            class_index += 1

        xmlbox = obj.find("bndbox")
        x1 = int(xmlbox.find("xmin").text)
        x2 = int(xmlbox.find("xmax").text)
        y1 = int(xmlbox.find("ymin").text)
        y2 = int(xmlbox.find("ymax").text)

        bbox_list.append([x1, y1, x2, y2])
        anno_list.append([data_set+"/"+image_path.split("/")[-1], str(x1), str(y1), str(x2), str(y2), cls])

    return class_dict, bbox_list, anno_list


if __name__ == "__main__":
    main()
