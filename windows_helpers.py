from windows_toasts import Toast, WindowsToaster
from PIL.ImageGrab import grabclipboard , Image
from win32clipboard import IsClipboardFormatAvailable
import os

def show_notification(message):
    toaster = WindowsToaster(message)
    newToast = Toast()
    newToast.text_fields = [message]
    toaster.show_toast(newToast)

def is_image_present():
    return IsClipboardFormatAvailable(8)

def get_image_from_clipboard():
    return grabclipboard()

def get_pixels_from_image(image):
    return image.getdata()

def save_image_to_directory(image, save_directory, timestamp):
    if isinstance(save_directory, tuple):
        save_directory = ''.join(save_directory)
        
    filename = f"image_{ ''.join(timestamp) }.png"
    full_path = os.path.join(save_directory, filename)

    image.save(full_path, 'PNG')
