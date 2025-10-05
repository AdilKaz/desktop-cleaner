import os, shutil

def move_file(file_path, dest_folder_path):
    os.makedirs(dest_folder_path, exist_ok=True)
    file_name, ext=os.path.splitext(os.path.basename(file_path))
    dest=os.path.join(dest_folder_path, f'{file_name}{ext}')
    counter=1
    while os.path.exists(dest):
        dest=os.path.join(dest_folder_path, f'{file_name}({counter}){ext}')
        counter+=1
    shutil.move(file_path, dest)

desktop=os.path.join(os.path.expanduser('~'), 'Desktop')

extension = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv'],
    'Music': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Others': []
}

for i in os.listdir(desktop):
    file_path=os.path.join(desktop, i)
    if os.path.isdir(file_path):
        continue
    _, ext=os.path.splitext(i)
    moved=False
    for folder, exts in extension.items():
        if ext.lower() in exts:
            folder_path=os.path.join(desktop, folder)
            move_file(file_path, folder_path)
            moved=True
            break
    if not moved:
        move_file(file_path, os.path.join(desktop, 'Others'))

print("Desktop cleaned correctly!")