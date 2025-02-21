import os
import shutil

source_dir = 'dosya_yolunuz'

images_dir = 'images'
labels_dir = 'labels'

os.makedirs(images_dir, exist_ok=True)
os.makedirs(labels_dir, exist_ok=True)

for file_name in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file_name)
    if file_name.endswith('.jpg'):
        shutil.move(file_path, os.path.join(images_dir, file_name))
    elif file_name.endswith('.txt'):
        shutil.move(file_path, os.path.join(labels_dir, file_name))

print('Dosyalar başarıyla ayrıldı!')
