import pandas as pd
import numpy as np
import os
from PIL import Image
import json


if __name__ == "__main__":


    class_type = ['root']
    root_path = "D:\project\zjx\wisdom tooth\data\label"
    save_path = r"D:\project\zjx\wisdom tooth\BBN\lib\utils\annotation.json"


    for phase in class_type:
        new_annos = []

        csv_path = os.path.join(root_path,"roi1588_%s.csv"%phase)

        csv = pd.read_csv(csv_path)
        for row in csv.iterrows():

            img_path = row[1]['img_path']
            category_id = row[1]['root_number']
            img = Image.open(img_path)
            im_height = img.height
            im_width  = img.width


            new_annos.append({"image_id": row[0] + 1,
                              "im_height": im_height,
                              "im_width": im_width,
                              "category_id": category_id,
                              "fpath": img_path})

            if phase == 'root':
                num_classes = 4
            else:
                num_classes = 2

        converted_annos = {"annotations": new_annos,
                            "num_classes": num_classes}

        with open(save_path, mode='w',encoding='utf-8') as f:
            json.dump(converted_annos, f,ensure_ascii=False)




            # print(rows[0])
            # print(rows[1])