@echo off

ipconfig /flushdns

del /f /s /q %systemdrive%\*.log 2>nul

del /f /s /q %systemdrive%\*.bak 2>nul
 
del /f /s /q %systemdrive%\*.chk 2>nul

del /f /s /q %systemdrive%\*.tmp 2>nul

del /f /s /q %systemdrive%\*._mp 2>nul

del /f /s /q %systemdrive%\*.ftg 2>nul

del /f /s /q %systemdrive%\*.gid 2>nul

del /f /s /q %systemdrive%\*.pnf 2>nul

del /f /s /q %systemdrive%\thumbs.db 2>nul

rd /s /q %windir%\temp md %windir%\temp 2>nul

del /f /s /q %systemdrive%\recycled\*.* 2>nul

del /f /s /q %windir%\prefetch\*.* 2>nul

del /f /q %userprofile%\AppData\Roaming\Microsoft\Windows\Cookies\*.* 2>nul

del /f /s /q "%userprofile%\AppData\Local\Microsoft\Windows\Temporary Internet Files\*.*" 2>nul

cls

d:

cd\

echo 正在清理其他盘中的垃圾文件...

del /f /s /q *.log 2>nul

del /f /s /q *.tmp 2>nul

del /f /s /q thumbs.db 2>nul

e:

cd\

del /f /s /q *.log 2>nul

del /f /s /q *.tmp 2>nul

del /f /s /q thumbs.db 2>nul

f:

cd\

del /f /s /q *.log 2>nul

del /f /s /q *.tmp 2>nul

del /f /s /q thumbs.db 2>nul

g:

cd\

del /f /s /q *.log 2>nul

del /f /s /q *.tmp 2>nul

del /f /s /q thumbs.db 2>nul

echo 成功清除系统垃圾!

echo 正在清理多余桌面右键

regsvr32 /u /s igfxpph.dll

reg delete HKEY_CLASSES_ROOT\Directory\Background\shellex\ContextMenuHandlers /f

reg add HKEY_CLASSES_ROOT\Directory\Background\shellex\ContextMenuHandlers\new /ve /d {D969A300-E7FF-11d0-A93B-00A0C90F2719}

reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v HotKeysCmds /f

reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v IgfxTray /f

echo 清理多余桌面右键成功

net user HelpAssistant /del

net user SUPPORT_388945a0 /del

echo 优化C盘

powercfg -h off

echo 重启explorer进程，屏幕会暂时闪烁，请稍等。。。。

@echo   explorer进程重启中,请勿关闭程序...

taskkill /f /im Explorer.exe >nul 2>nul

ping localhost -n 3 >nul 2>nul

start "explorer.exe" "%windir%\explorer.exe"

wmic pagefile list /format:list

wmic computersystem where name="%computername%" set AutomaticManagedPagefile=False

wmic pagefileset where name="C:\pagefile.sys" set InitialSize=2048,MaximumSize=5120

echo 优化完毕

echo Powered By JeRyWu

exit