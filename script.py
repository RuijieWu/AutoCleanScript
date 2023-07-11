from os import system
import asyncio
import config
#你可以在这里添加你想要删除的文件后缀名
async def cleanSystemDisk():
    for suf in suf_list:
                system(f"del /f /s /q %systemdrive%\*.{suf} 2>nul")

    system("del /f /s /q %systemdrive%\\thumbs.db 2>nul")
    system("rd /s /q %windir%\\temp md %windir%\\temp 2>nul")
    system("del /f /s /q %systemdrive%\recycled\*.* 2>nul")
    system("del /f /s /q %windir%\prefetch\*.* 2>nul")
    system("del /f /q %userprofile%\AppData\Roaming\Microsoft\Windows\Cookies\*.* 2>nul")
    system("del /f /s /q \"%userprofile%\AppData\Local\Microsoft\Windows\Temporary Internet Files\*.*\" 2>nul")
    
    system("cls")

async def cleanOtherDisk():
    for disk in disk_list:
        system(f"{disk}:")
        system("cd\\")
        system("del /f /s /q *.log 2>nul")
        system("del /f /s /q *.tmp 2>nul")
        system("del /f /s /q thumbs.db 2>nul")
        
    system("cls")

async def cleanReg():
    system("regsvr32 /u /s igfxpph.dll")
    system("reg delete HKEY_CLASSES_ROOT\Directory\Background\shellex\ContextMenuHandlers /f")
    system("reg add HKEY_CLASSES_ROOT\Directory\Background\shellex\ContextMenuHandlers\new /ve /d {D969A300-E7FF-11d0-A93B-00A0C90F2719}")
    system("reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v HotKeysCmds /f")
    system("reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v IgfxTray /f")
        
    system("cls")
    
async def cleanNetUser():
    system("net user HelpAssistant /del")
    system("net user SUPPORT_388945a0 /del")
    
    system("cls")
    
async def cleanExplorer():
    system("powercfg -h off")
    system("taskkill /f /im Explorer.exe >nul 2>nul")
    system("ping localhost -n 3 >nul 2>nul")
    print("重启explorer进程，屏幕会暂时闪烁，请勿关闭本程序")
    system("start \"explorer.exe\" \"%windir%\explorer.exe\"")
    
    system("cls")

async def cleanPage():
    system("wmic pagefile list /format:list")
    system("wmic computersystem where name=\"%computername%\" set AutomaticManagedPagefile=False")
    system("wmic pagefileset where name=\"C:\pagefile.sys\" set InitialSize=2048,MaximumSize=5120")
    
    system("cls")

async def main():
    input("Press Enter to start AFTER ensure important files dumped!")
    while True:
        try:
            
            system("@echo off")
            system("ipconfig /flushdns")
            await cleanSystemDisk()
            await cleanOtherDisk()
            await cleanReg()
            await cleanNetUser()
            await cleanExplorer()
            await cleanPage()
            system("exit")
    
        except:
            
            continue
        
        break    
if __name__ == "__main__":
    
    help = '''
    清理脚本会清理电脑中的缓存文件，清理前请做好备份或者注释掉对应代码
    '''
    asyncio.run(main())
    
