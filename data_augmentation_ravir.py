import os
import numpy as np
from skimage import io, transform

input_path = "RAVIR_Dataset\\train\\training_images\\"
target_path = "RAVIR_Dataset\\train\\training_masks\\"
output_path_img = "RAVIR_Dataset_DA\\training_images\\"
output_path_ground = "RAVIR_Dataset_DA\\training_masks\\"


def get_paths(input_dir, target_dir):
  input_img_paths = sorted(
      [
          os.path.join(input_dir, fname)
          for fname in os.listdir(input_dir)
          if fname.endswith(".png")
      ]
  )
  target_img_paths = sorted(
      [
          os.path.join(target_dir, fname)
          for fname in os.listdir(target_dir)
          if fname.endswith(".png") and not fname.startswith(".")
      ]
  )
  return input_img_paths, target_img_paths

def data_augmentation(input_path, target_path, output_path, output_target_path):
    i = 0
    for path_in, path_targ in zip(input_path, target_path):
        print("Image:", i)
        name = path_in.split("\\")[-1].split(".")[0]
        img = io.imread(path_in)
        target = io.imread(path_targ)
        img_90 = transform.rotate(img,90)
        target_90 = transform.rotate(target,90)
        img_180 = transform.rotate(img, 180)
        target_180 = transform.rotate(target, 180)
        img_270 = transform.rotate(img,270)
        target_270 = transform.rotate(target, 270)
        io.imsave(output_path + name + "_90.png", img_90)
        io.imsave(output_path + name + "_180.png", img_180)
        io.imsave(output_target_path + name + "_90.png", target_90)
        io.imsave(output_target_path + name + "_180.png", target_180)
        io.imsave(output_path + name + "_270.png", img_270)
        io.imsave(output_target_path + name + "_270.png", target_270)
        i += 1

        

path_inp, path_targ = get_paths(input_path, target_path)
data_augmentation(path_inp, path_targ, output_path_img, output_path_ground)
