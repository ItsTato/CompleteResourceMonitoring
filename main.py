import os,sys,platform,time,random
from datetime import datetime

module = "tabulate"
try:
    exec(f"from tabulate import tabulate")
except ImportError as e:
    try:
        os.system(f"pip3 install {module}")
    except Exception as e:
        print("Uh oh! Something has broken :(")
        sys.exit(1)

module = "psutil"
try:
    exec(f"import {module}")
except ImportError as e:
    try:
        os.system(f"pip3 install {module}")
    except Exception as e:
        print("Uh oh! Something has broken :(")
        sys.exit(1)

def getSize(bytes,suffix="B"):
    for unit in ["","K","M","G","T","P"]:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= 1024

from tabulate import tabulate
import psutil

Side = "="*35

#            os.system("cls" if (os.name == "nt") else "clear")           
#            print(random.choice(loading))
#            time.sleep(.25)
#            # do thingies UwU
#            os.system("cls" if (os.name == "nt") else "clear")
#            # print thingies OwO
#            time.sleep(.5)

space = " "*25
loading = [f"\n\n{space}Complete Resource Monitoring\n{space}🛫 Loading\n\n",f"\n\n{space}Complete Resource Monitoring\n{space}🛬 Loading\n\n",f"\n\n{space}Complete Resource Monitoring\n{space}👉👈 Loading\n\n"]
useFreq = True

while True:
    try:
        os.system("cls" if (os.name == "nt") else "clear")  
        print("""

Welcome to complete resource monitoring!
1) System Information              5) Swap Memory
2) Boot Time                       6) Disk (Soon™)
3) CPU Information                 7) Network Information (Soon™)
4) Installed Memory                X) Close the program

Please select an option: 
        """)
        chose = input("")
        os.system("cls" if (os.name == "nt") else "clear")  
        try:
            if (str(chose) == "X" or str(chose) == "x"):
                sys.exit(1)
            
            while (int(chose) == 1): 
                string = tabulate([["System",platform.uname().system],["Node Name",platform.uname().node],["Release",platform.uname().release],["Version",platform.uname().version],["Machine",platform.uname().machine],["Processor",platform.uname().processor]],["System Information"],"fancy_grid")
                os.system("cls" if (os.name == "nt") else "clear")  
                print(string)
                time.sleep(500)
                print(random.choice(loading))

            while (int(chose) == 2):
                bt=datetime.fromtimestamp(psutil.boot_time())
                string = tabulate([["Unit","Time"],["Year",bt.year],["Month",bt.month],["Day",bt.day],["Hour",bt.hour],["Minute",bt.minute],["Second",bt.second]], ["Boot Time"], "fancy_grid")
                os.system("cls" if (os.name == "nt") else "clear")  
                print(string)
                time.sleep(500)
                print(random.choice(loading))

            while (int(chose) == 3):
                freq=psutil.cpu_freq()
                cpu=[["Physical Cores",psutil.cpu_count(logical=False)],["Total Cores",psutil.cpu_count(logical=True)]]
                for i, percentage in enumerate(psutil.cpu_percent(percpu=True,interval=1)):
                    cpu.append([f"CPU Core #{i}", f"{percentage}%"])
                cpu.append([f"Total CPU Usage",f"{psutil.cpu_percent()}%"])
                if (useFreq == True):
                    cpu.append(["Max Frequency",f"{freq.max:.2f}Mhz"])
                    cpu.append(["Min Frequency",f"{freq.min:.2f}Mhz"])
                    cpu.append(["Current Frequency",f"{freq.current:.2f}Mhz"])
                string = tabulate(cpu, ["CPU Information"], "fancy_grid")
                os.system("cls" if (os.name == "nt") else "clear")  
                print(string)
                time.sleep(.05)
                print(random.choice(loading))

            while (int(chose) == 4):
                svmem = psutil.virtual_memory()
                string = tabulate([["Total",getSize(svmem.total)],["Available",getSize(svmem.available)],["Used",getSize(svmem.used)],["Percentage",f"{svmem.percent}%"]], ["Installed Memory"], "fancy_grid")
                os.system("cls" if (os.name == "nt") else "clear")  
                print(string)
                time.sleep(.05)

            while (int(chose) == 5):
                swap = psutil.swap_memory()
                string = tabulate([["Total",getSize(swap.total)],["Free",getSize(swap.free)],["Used",getSize(swap.used)],["Percentage",f"{swap.percent}%"]], ["Swap Memory"], "fancy_grid")
                os.system("cls" if (os.name == "nt") else "clear")  
                print(string)
                time.sleep(.05)
        except KeyboardInterrupt:
            pass
        except Exception:
            os.system("cls" if (os.name == "nt") else "clear")
            print("[EXCEPT] Caught an exception, disabling possible causes")
            useFreq = False
            print(random.choice(loading))
            time.sleep(2.5)
    except KeyboardInterrupt:
        print("Did you mean to choose \"X\" instead? y/N")
        yn = input("")
        if (yn == "" or  yn == "n" or yn == "N"):
            pass
        elif (yn == "y" or yn == "Y"):
            sys.exit(1)

