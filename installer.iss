[Setup]
AppId={{B8F2E4A1-3C57-4D89-9E16-A2F0B5D71C83}
AppName=MD to PDF
AppVersion=1.0
AppPublisher=Nathan Curtis
DefaultDirName={autopf}\MD to PDF
DefaultGroupName=MD to PDF
OutputBaseFilename=MD-to-PDF-Setup
Compression=lzma
SolidCompression=yes
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
PrivilegesRequired=admin
UninstallDisplayName=MD to PDF

[Files]
Source: "dist\md2pdf.exe"; DestDir: "{app}"; Flags: ignoreversion

[Registry]
; .md context menu
Root: HKCR; Subkey: "SystemFileAssociations\.md\shell\ConvertToPDF"; ValueType: string; ValueName: ""; ValueData: "Convert to PDF"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.md\shell\ConvertToPDF\command"; ValueType: string; ValueName: ""; ValueData: """{app}\md2pdf.exe"" ""%1"""; Flags: uninsdeletekey

; .markdown context menu
Root: HKCR; Subkey: "SystemFileAssociations\.markdown\shell\ConvertToPDF"; ValueType: string; ValueName: ""; ValueData: "Convert to PDF"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.markdown\shell\ConvertToPDF\command"; ValueType: string; ValueName: ""; ValueData: """{app}\md2pdf.exe"" ""%1"""; Flags: uninsdeletekey
