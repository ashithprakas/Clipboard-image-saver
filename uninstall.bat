@echo off
REM Stop process if  it exists 
call stop.bat

REM Define the name of the shortcut and the path to the Startup folder
set SHORTCUT_NAME=ClipboardImageSaver
set STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

REM Define the full path to the shortcut file
set SHORTCUT_PATH=%STARTUP_FOLDER%\%SHORTCUT_NAME%.lnk

REM Check if the shortcut exists
if exist "%SHORTCUT_PATH%" (
    REM Remove the shortcut
    del "%SHORTCUT_PATH%"
    
    echo Shortcut "%SHORTCUT_NAME%.lnk" has been removed from the Startup folder.
    echo Unistall was successful
) else (
    echo Shortcut "%SHORTCUT_NAME%.lnk" not found in the Startup folder.
    echo Could not complete uninstall , Please manually remove shortcut from startup folder 
)

pause
