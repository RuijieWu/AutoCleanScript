'''AutoCleanEasyPythonScriptForWindows'''
from os import system
import asyncio
import config
#你可以在这里添加你想要删除的文件后缀名
async def clean_system_disk():
    '''Clean SystemDisk'''
    for suf in config.suf_list:
                system(f"del /f /s /q %systemdrive%\*.{suf} 2>nul")

    system("del /f /s /q %systemdrive%\\thumbs.db 2>nul")
    system("rd /s /q %windir%\\temp md %windir%\\temp 2>nul")
    system("del /f /s /q %systemdrive%\recycled\*.* 2>nul")
    system("del /f /s /q %windir%\prefetch\*.* 2>nul")
    system("del /f /q %userprofile%\AppData\Roaming\Microsoft\Windows\Cookies\*.* 2>nul")
    system("del /f /s /q \"%userprofile%\AppData\Local\Microsoft\Windows\Temporary Internet Files\*.*\" 2>nul") 
    system("cls")

async def clean_other_disks():
    '''Clean other disks'''
    for disk in config.disk_list:
        system(f"{disk}:")
        system("cd\\")
        system("del /f /s /q *.log 2>nul")
        system("del /f /s /q *.tmp 2>nul")
        system("del /f /s /q thumbs.db 2>nul")
    system("cls")

async def clean_reg():
    '''Clean register'''
    system("regsvr32 /u /s igfxpph.dll")
    system("reg delete HKEY_CLASSES_ROOT\Directory\Background\shellex\ContextMenuHandlers /f")
    system("reg add HKEY_CLASSES_ROOT\Directory\Background\shellex\ContextMenuHandlers\new /ve /d {D969A300-E7FF-11d0-A93B-00A0C90F2719}")
    system("reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v HotKeysCmds /f")
    system("reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v IgfxTray /f")      
    system("cls")

async def clean_netuser():
    '''Clean netuser'''
    system("net user HelpAssistant /del")
    system("net user SUPPORT_388945a0 /del")
    system("cls")

async def clean_explorer():
    '''restart explorer.exe'''
    system("powercfg -h off")
    system("taskkill /f /im Explorer.exe >nul 2>nul")
    system("ping localhost -n 3 >nul 2>nul")
    print("重启explorer进程，屏幕会暂时闪烁，请勿关闭本程序")
    system("start \"explorer.exe\" \"%windir%\explorer.exe\"")
    system("cls")

async def clean_page():
    '''clean wmic'''
    system("wmic pagefile list /format:list")
    system("wmic computersystem where name=\"%computername%\" set AutomaticManagedPagefile=False")
    system("wmic pagefileset where name=\"C:\pagefile.sys\" set InitialSize=2048,MaximumSize=5120")
    system("cls")

async def main():
    '''enrtrance of this script'''
    input("Press Enter to start AFTER ensure important files dumped!")
    while True:
        try:
            system("@echo off")
            system("ipconfig /flushdns")
            await clean_system_disk()
            await clean_other_disks()
            await clean_reg()
            await clean_netuser()
            await clean_explorer()
            await clean_page()
            system("exit")
        except:
            continue  
        break    
if __name__ == "__main__":
    help = '''
    清理脚本会清理电脑中的缓存文件，清理前请做好备份或者注释掉对应代码
    '''
    asyncio.run(main())
