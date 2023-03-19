import os
import cv2
from paddleocr import PPStructure,draw_structure_result,save_structure_res

table_engine = PPStructure(show_log=True)

data_dir = "E:/ppstructure/PaddleOCR-release-2.6/doc/imgs_target"
for root, dirs, files in os.walk(data_dir):
    for name in files:
        img_dir = os.path.join(root,name)
        save_folder = './Save_picAexcel/table'
        img = cv2.imread(img_dir)
        result = table_engine(img)
        save_structure_res(result, save_folder, os.path.basename(img_dir).split('.')[0])

        for line in result:
            line.pop('img')
            print(line)

        from PIL import Image

        font_path = '../doc/fonts/simfang.ttf'  # PaddleOCR下提供字体包
        image = Image.open(img_dir).convert('RGB')
        im_show = draw_structure_result(image, result, font_path=font_path)
        im_show = Image.fromarray(im_show)



