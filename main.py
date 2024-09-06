import os
import sys
import shutil
import subprocess
try:
    import yaml
except:
    os.system("python -m pip install pyyaml")
def sething(x):
    os.system(f"adb shell setprop debug.oculus.{x}")
    menu()
class qtt:None
qtt.version="Build 2"
qtt.loadDefault=True
print(f"Welcome to questools!\n",
      f"Detecting \"commands\" folder")
if os.path.isdir('commands'):
    print("Detected \"commands\" folder")
    theresCommands=True
else:
    print("Did not detect \"commands\" folder.\nDisabling commands option.")
    theresCommands=False
if shutil.which("adb") == None:
    print("Please add adb to your PATH.")
    exit()
else:
    print("adb detected.")

def menu():
    devices = str(subprocess.check_output("adb devices", shell=True).rstrip()).replace('\\n', '\n ').replace('\\t', '\t').replace('b\'', '').replace('\'', '')
    
    print(f"Questools {qtt.version}, Python {sys.version} on {sys.platform}\n",
          devices,
          f"\n rR - Change the refresh rate (HZ) of your device.\n",
          f"tW - Change the texture width of your device.\n",
          f"tH - Change the texture height of your device.\n",
          f"pL - Change the GPU/CPU Level of your device.\n",
          f"fC - Enable or disable chromatic aberration.\n"
          f"fRC - Set the capture HZ. (0 = Half, 1 = Full)")
    if theresCommands:
        print(" c - Commands")
    optioninput = input(f"?> ")
    match optioninput:
        case "rR":
            z = input("rR?> ")
            sething(f"refreshRate {z}")
            
        case "tW":
            z = input("tW?> ")
            sething(f"textureWidth {z}")
        case "tH":
            z = input("tH?> ")
            sething(f"textureHeight {z}")
        case "pL":
            z = input("pL?> ")
            sething(f"gpuLevel {z}")
            sething(f"cpuLevel {z}")
        case "fRC":
            z = input("fRC> ")
            sething(f"fullRateCapture {z}")
        case "fC":
            z = input("fC> ")
            sething(f"forceChroma {z}")
        case "c":
            os.system("dir commands/")
            if os.path.isfile("commands/default.yml"):
                z = "default.yml"
            elif os.path.isfile("commands/default.yaml"):
                z = "default.yaml"
            else:
                z = input("which?> ")
            setting = open(f"commands/{z}", 'r')
            try:
                settingasdict = yaml.safe_load(setting)
            except yaml.YAMLError as err: print(err)
            print(settingasdict)
            print("Executing.")
            globals().update(settingasdict)
            sething(f"refreshRate {rR}")
            sething(f"textureWidth {tW}")
            sething(f"textureHeight {tH}")
            sething(f"gpuLevel {pL}")
            sething(f"cpuLevel {pL}")
            sething(f"fullRateCapture {fRC}")
            sething(f"forceChroma {fC}")
            menu()
        case "q":
            quit()
        case _:
            print("Invalid option.")
            menu()
menu()
