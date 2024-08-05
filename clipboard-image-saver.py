import os 
from datetime import datetime
from time import sleep
import configs
import tempfile

def create_temp_and_store_processId():
    try:
        temp_dir = tempfile.gettempdir()
        sub_dir = "clipboard_image_saver.temp"

        new_dir_path = os.path.join(temp_dir,sub_dir)

        os.makedirs(new_dir_path,exist_ok=True)
        pid = os.getpid()
        pid_file_path = os.path.join(new_dir_path,'clipboard_image_saver.pid')

        print(pid_file_path)
        with open(pid_file_path,'w') as file:
            file.write(str(pid))

    except IOError as e:
        exit()

def main():
    if os.name =='nt' :
        IMAGE_SAVE_DIRECTORY = configs.IMAGE_SAVE_DIRECTORY_WINDOWS
        from windows_helpers import\
        show_notification,is_image_present,get_image_from_clipboard,\
        get_pixels_from_image,save_image_to_directory

    create_temp_and_store_processId()

    delay = configs.MAX_DELAY_SECONDS
    show_notification('Clipboard Image Saver is running')

    old_hash = 0
    while True:
        delay = min(delay + 1, configs.MAX_DELAY_SECONDS)
        try:
            if not is_image_present():
                continue
            image = get_image_from_clipboard()

            if image is None:
                continue

            new_hash = hash(tuple(get_pixels_from_image(image)))
            if new_hash == old_hash:
                continue
        
            old_hash = new_hash
            timestamp = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')

            delay = max(delay // 2, configs.MIN_DELAY_SECONDS)
            save_image_to_directory(image, IMAGE_SAVE_DIRECTORY, configs.IMAGE_SAVE_PREFIX,timestamp)

        except Exception as e :
            continue
        
if __name__ == "__main__":
    main()