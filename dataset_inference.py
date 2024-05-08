import cv2

import numpy as np
import os

import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--dir', type=str, default='images', help='input directory')
args=parser.parse_args()

# load images in images directory
dir=args.dir
file_names = sorted(os.listdir(dir), key=lambda x: int(x.split('_')[-1].split('.')[0]) if '_' in x else int(x.split('.')[0]))
images_path = [os.path.join(dir, file_name) for file_name in file_names if file_name.endswith('.JPG') or file_name.endswith('.png') or file_name.endswith('.jpg')]



for curr_path in images_path:
    os.system('python inference_realesrgan.py -n RealESRGAN_x4plus -i '+curr_path+' --face_enhance -s 1 --output '+dir+'_out')

print('Inference done!')

os.system('python visualizer.py --dir '+dir+'_out')