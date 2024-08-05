import os 
from datetime import datetime
from time import sleep
import configs
import tempfile
import logging

def create_temp_and_store_processId():
    try:
        temp_dir = tempfile.gettempdir()
        sub_dir = "clipboard_image_saver.temp"

        new_dir_path = os.path.join(temp_dir,sub_dir)

        os.makedirs(new_dir_path,exist_ok=True)
        pid = os.getpid()
        pid_file_path = os.path.join(new_dir_path,'clipboard_image_saver.pid')

        with open(pid_file_path,'w') as file:
            file.write(str(pid))

    except IOError as e:
        exit()

def setup_logging_config():
    log_directory_name = 'logs'
    if not os.path.exists(log_directory_name):
        os.makedirs(log_directory_name)
    log_file_path = os.path.join(log_directory_name,'debug.log')
    logging.basicConfig(filename=log_file_path ,encoding="utf-8",filemode="a",format="{asctime} - {levelname} - {message}",style="{",datefmt="%Y-%m-%d %H:%M",level=logging.DEBUG)


def main():
    if os.name =='nt' :
        IMAGE_SAVE_DIRECTORY = configs.IMAGE_SAVE_DIRECTORY_WINDOWS
        from windows_helpers import\
        show_notification,is_image_present,get_image_from_clipboard,\
        get_pixels_from_image,save_image_to_directory

    create_temp_and_store_processId()
    setup_logging_config()

    delay = configs.MAX_DELAY_SECONDS
    show_notification('Clipboard Image Saver is running')
    logging.info('Clipboard Image Saver is running')

    old_hash = 0
    while True:
        sleep(delay)
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
            logging.info('Saving Image to Directory')
            save_image_to_directory(image, IMAGE_SAVE_DIRECTORY, configs.IMAGE_SAVE_PREFIX,timestamp)

        except Exception as e :
            logging.critical("Error: ", exc_info=True)
        
if __name__ == "__main__":
    main()