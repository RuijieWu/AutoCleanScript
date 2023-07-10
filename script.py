from os import system

if __name__ == "main":
    
    help = '''
    清理脚本会清理电脑中的缓存文件，清理前请做好备份或者注释掉对应代码
    '''
    input("Press Enter to start AFTER ensure important files dumped!")
    while True:
        try:
            system("@echo off")
            system("ipconfig /flushdns")
            system("del /f /s /q %systemdrive%\*.log 2>nul")
            system("del /f /s /q %systemdrive%\*.bak 2>nul")
            system("del /f /s /q %systemdrive%\*.chk 2>nul")
            system("del /f /s /q %systemdrive%\*.tmp 2>nul")
            system("del /f /s /q %systemdrive%\*._mp 2>nul")
            system("del /f /s /q %systemdrive%\*.ftg 2>nul")
            system("del /f /s /q %systemdrive%\*.gid 2>nul")
            system("del /f /s /q %systemdrive%\*.pnf 2>nul")
            system("del /f /s /q %systemdrive%\\thumbs.db 2>nul")
            system("rd /s /q %windir%\\temp md %windir%\\temp 2>nul")
            system("del /f /s /q %systemdrive%\recycled\*.* 2>nul")
            system("del /f /s /q %windir%\prefetch\*.* 2>nul")
            system("del /f /q %userprofile%\AppData\Roaming\Microsoft\Windows\Cookies\*.* 2>nul")
            system("del /f /s /q \"%userprofile%\AppData\Local\Microsoft\Windows\Temporary Internet Files\*.*\" 2>nul")
            system("cls")
            system("d:")
            system("cd\\")
            system("del /f /s /q *.log 2>nul")
            system("del /f /s /q *.tmp 2>nul")
            system("del /f /s /q thumbs.db 2>nul")
            system("e:")
            system("cd\\")
            system("del /f /s /q *.log 2>nul")
            system("del /f /s /q *.tmp 2>nul")
            system("del /f /s /q thumbs.db 2>nul")
            system("f:")
            system("cd\\")
            system("del /f /s /q *.log 2>nul")
            system("del /f /s /q *.tmp 2>nul")
            system("del /f /s /q thumbs.db 2>nul")
            system("g:")
            system("cd\\")
            system("del /f /s /q *.log 2>nul")
            system("del /f /s /q *.tmp 2>nul")
            system("del /f /s /q thumbs.db 2>nul")
            system("regsvr32 /u /s igfxpph.dll")
            system("reg delete HKEY_CLASSES_ROOT\Directory\Background\shellex\ContextMenuHandlers /f")
            system("reg add HKEY_CLASSES_ROOT\Directory\Background\shellex\ContextMenuHandlers\new /ve /d {D969A300-E7FF-11d0-A93B-00A0C90F2719}")
            system("reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v HotKeysCmds /f")
            system("reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v IgfxTray /f")
            system("net user HelpAssistant /del")
            system("net user SUPPORT_388945a0 /del")
            system("powercfg -h off")
            system("taskkill /f /im Explorer.exe >nul 2>nul")
            system("ping localhost -n 3 >nul 2>nul")
            print("重启explorer进程，屏幕会暂时闪烁，请勿关闭本程序")
            system("start \"explorer.exe\" \"%windir%\explorer.exe\"")
            system("wmic pagefile list /format:list")
            system("wmic computersystem where name=\"%computername%\" set AutomaticManagedPagefile=False")
            system("wmic pagefileset where name=\"C:\pagefile.sys\" set InitialSize=2048,MaximumSize=5120")
            system("exit")
    
        except:
            continue
        
        break
