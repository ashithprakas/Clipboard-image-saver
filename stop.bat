@echo off
REM Check if PID file exists
if not exist scripts.pid (
    echo PID file not found.
    exit /b 1
)

REM Read PID from file
set /p PID=<scripts.pid

REM Validate that PID is not empty
if "%PID%"=="" (
    echo PID is empty in the PID file.
    exit /b 1
)

REM Terminate the process
taskkill /PID %PID% /F

REM Check if termination was successful
if %ERRORLEVEL% neq 0 (
    echo Failed to terminate process with PID %PID%.
    exit /b 1
)

REM Remove PID file
del scripts.pid

echo Process terminated.
pause
