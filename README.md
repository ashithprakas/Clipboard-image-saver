
# Clipboard Image Saver

Clipboard Image Saver is a python script that automatically saves clipboard images as a PNG file with the desired name with time of creation.
Particularly helpful with the windows screenshot shortcut 
Window + Shift + S where the screenshot is saved to the defined folder


## How to Install

1 . Install latest version of Python > 3  
Get the latest version from : http://www.python.org/getit/

2 . Set python to system Path :  
Learn to set it from : https://geek-university.com/python/add-python-to-the-windows-path/

3 . Clone Repositiory to a directory :
```bash
 git clone https://github.com/ashithprakas/Clipboard-image-saver.git
```

4 . CD to directory 
```bash
 cd Clipboard-image-saver
```

5 . Execute install.bat  
```bash
 .\install.bat
```

This will  create the necessary shortcut in the startup folder "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup" and execute "start.bat" will start the python script.

## How to Uninstall

1 . CD to directory 
```bash
 cd Clipboard-image-saver
```
3 . Execute unistall.bat :
```bash
 .\uninstall.bat
```

This will remove all files related to the program from "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup" and "%TEMP%" and run "stop.bat" to stop execution of script
## Environment Variables

To run this project, you will need to add the following environment variables to your configs.py file

`IMAGE_SAVE_PREFIX` : Set the prefix to be added to the file name of saved screenshot

`IMAGE_SAVE_DIRECTORY_WINDOWS` : Set directory where screenshot needs to be saved

`MAX_DELAY_SECONDS` : Set delay between saving a screenshot

