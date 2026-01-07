import subprocess
import sys
from pathlib import Path
import ctypes

def is_admin() -> bool:
    try:
        return bool(ctypes.windll.shell32.IsUserAnAdmin())
    except Exception:
        return False
    
def relaunch_as_admin() -> None:
    # Relaunch the current script with admin rights (UAC prompt)
    params = " ".join([f'"{arg}"' for arg in sys.argv])
    rc = ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",          # triggers UAC
        sys.executable,   # python.exe
        params,           # pass the same args back in
        None,
        1
    )
    # If the user cancels UAC, ShellExecuteW returns <= 32
    if rc <= 32:
        raise RuntimeError("Admin elevation was cancelled or failed.")
    sys.exit(0)  # quit non-admin instance

def main(): 
    #MAKE SURE THERE IS NO SPACE IN YOUR PATH 
    disable_open_tablet_driver_path = r"C:\Users\Thanh\OneDrive\Documents\Coding\OsuDriverSwitcher\DisableWacomDrivers.bat"
    open_tablet_driver_path = r"C:\Users\Thanh\OneDrive\Documents\OpenTabletDriver-0.6.5.1_win-x64\OpenTabletDriver.UX.Wpf.exe"
    osu_path = r"C:\Users\Thanh\AppData\Local\osu!\osu!.exe"

    p = Path(open_tablet_driver_path)
    print("Path:", p)
    print("Exists:", p.exists())
    print("Is file:", p.is_file())
    print("Suffix:", p.suffix)

    #open disable tablet driver 
    try:
        closeDriver = subprocess.run(
            [disable_open_tablet_driver_path],
            shell=True,
            check=True
        )
        print("Driver disabled successfully")
    except subprocess.CalledProcessError as e:
        print("Failed to disable driver")
        print(e)

    #open "opentabletdriver.ux"
    try: 
        open_tablet = subprocess.Popen([open_tablet_driver_path])
        print("Tablet driver open successfully!")
    except subprocess.CalledProcessError as e:
        print("Could not open driver")
        print(e)

    #choose whether to open osu std or osu lazer
    try:
        open_osu = subprocess.Popen([osu_path])
        print("osu opened successfully!")
    except subprocess.CalledProcessError as e:
        print("Could not open osu file: ", e)

if __name__ == "__main__":
    main()