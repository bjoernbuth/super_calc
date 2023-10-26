REM old stuff .\venv\Scripts\activate.bat
REM activate venv

@echo off
set VENVDIR=%~1

if "%VENVDIR%"=="" (
    set VENVDIR=venv
)

.\%VENVDIR%\Scripts\activate.bat

