import exifread

with open('./test_photo.jpg', 'rb') as f:
    tags = exifread.process_file(f)

for k, v in tags.items():
    print(f'{k}: {v}')
