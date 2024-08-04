import os 
from datetime import datetime
from time import sleep
import configs

if os.name =='nt' :
    IMAGE_SAVE_DIRECTORY = configs.IMAGE_SAVE_DIRECTORY_WINDOWS
    from windows_helpers import\
    show_notification,is_image_present,get_image_from_clipboard,\
    get_pixels_from_image,save_image_to_directory

delay:int = configs.MAX_DELAY_SECONDS
show_notification('Clipboard Image Saver is running')

old_hash = 0
while True:
    # delay = min(delay + 1, configs.MAX_DELAY_SECONDS)
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
        timestamp = tuple(datetime.now().strftime('%Y.%m.%d_%H.%M.%S'))

        # delay = max(delay // 2, configs.MIN_DELAY_SECONDS)
        save_image_to_directory(image, IMAGE_SAVE_DIRECTORY, timestamp)

    except Exception as e :
        print('error',e.args[0])
        