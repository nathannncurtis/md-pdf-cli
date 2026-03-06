@echo off
setlocal

set SIGNTOOL="C:\Program Files (x86)\Windows Kits\10\bin\10.0.22621.0\x64\signtool.exe"
set PFX_PATH=C:\Certs\RonsinCodeSign.pfx
set /p PFX_PASS="Enter PFX password: "

echo.
echo Building with Coil...
coil build . --mode portable --console
if %ERRORLEVEL% neq 0 (
    echo Build failed!
    pause
    exit /b 1
)

echo.
echo Signing md2pdf.exe...
%SIGNTOOL% sign /f "%PFX_PATH%" /p "%PFX_PASS%" /fd SHA256 /tr http://timestamp.digicert.com /td SHA256 /d "MD to PDF Converter" "dist\md2pdf.exe"
if %ERRORLEVEL% neq 0 (
    echo Signing failed!
    pause
    exit /b 1
)

echo.
echo Build and signing complete.
echo Compile installer.iss with Inno Setup to create the installer.
pause
