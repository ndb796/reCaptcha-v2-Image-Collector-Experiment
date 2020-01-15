from PIL import Image
import os
import random
import shutil

root_path = 'classification_example'
file_paths = os.listdir(root_path)
imgs = []

train_dataset_path = 'train_dataset'
if not os.path.isdir(train_dataset_path):
    os.mkdir(train_dataset_path)

test_dataset_path = 'test_dataset'
if not os.path.isdir(test_dataset_path):
    os.mkdir(test_dataset_path)

count = 0
# Make test dataset
for i in file_paths[:1000]:
    img = Image.open(root_path + '/' + i)
    for i in range(3):
        for j in range(3):
            area = (j * 100, i * 100, 100 + j * 100, 100 + i * 100)
            partial_img = img.crop(area)
            partial_img.save(test_dataset_path + '/' + str(count) + '.png')
            count += 1

count = 0
# Make train dataset
for i in file_paths[1000:]:
    img = Image.open(root_path + '/' + i)
    print('Processing:', (root_path + '/' + i))
    for i in range(3):
        for j in range(3):
            area = (j * 100, i * 100, 100 + j * 100, 100 + i * 100)
            partial_img = img.crop(area)
            partial_img.save(train_dataset_path + '/' + str(count) + '.png')
            count += 1