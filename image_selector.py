import os
import random
import shutil

root_path = 'classification'
all_classes = os.listdir(root_path)
all_file_paths = []

for i in all_classes:
    file_paths = os.listdir(root_path + '/' + i)
    for file_path in file_paths:
        all_file_paths.append(root_path + '/' + i + '/' + file_path)

# Select 'n' files from all files
n = 20000
result_file_paths = random.sample(all_file_paths, n)
result_path = 'classification_example'
if not os.path.isdir(result_path):
    os.mkdir(result_path)

# Copy 'n' files to new folder
count = 0
for i in result_file_paths:
    shutil.copy2(i, result_path + '/' + str(count) + '.png')
    count += 1

# 정상이 아닌 이미지는 나중에 오류 유발함.
# 따라서 이미지 선택 과정 처리 이후에, 정상이 아닌 이미지는 크기로 정렬한 뒤에 지워주기.
