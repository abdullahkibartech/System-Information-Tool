import platform 
import socket
import json
import datetime
import psutil

host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
cpu_usage = psutil.cpu_percent(interval = 0.9)
core_usage = psutil.cpu_percent(interval = 0.9 , percpu = True)
physical_core = psutil.cpu_count(logical = False)
logical_core = psutil.cpu_count(logical = True)
memory = psutil.virtual_memory()
disk = psutil.disk_usage('C:\\')
battery = psutil.sensors_battery()

system_info = {
    "OS" : platform.system(),
    "CPU" : platform.processor(),
    "MACHINE" : platform.machine(),
    "OS RELEASE" : platform.release(),
    "PYTHON VERSION" : platform.python_version(),
    "Host name" :host_name,
    "Ip Address" : ip,
    "CPU USAGE" : cpu_usage,
    "CORE USAGE" : core_usage,
    "PHYSICAL CORE" : physical_core,
    "LOGICAL CORE" : logical_core,
    "TOTAL RAM"  : f"{memory.total / 1024**3:.2f} GB",
    "AVAILABLE RAM" : f"{memory.available / 1024**3:.2f} GB",
    "USED RAM" : f"{memory.used / 1024**3:.2f} GB",
    "RAM USAGE" : f"{memory.percent}%",
    "Total SPACE" : f"{disk.total / (1024**3):.2f} GB",
    "Used SPACE" :  f"{disk.used / (1024**3):.2f} GB",
    "Free SPACE" :  f"{disk.free / (1024**3):.2f} GB",
    "Disk USAGE" :  f"{disk.percent}%",

}   
if battery == None:
    system_info["Battery Level"] = "No Battery Detected"
    system_info["Power Plugged"] = "N/A"
else:
    system_info["Battery Level"] = f"{battery.percent}%"
    system_info["Power Plugged"] = battery.power_plugged

for key , value in system_info.items():
    print(f"{key} : {value}")

with open("system_info_report.json" , "w") as file:
    json.dump(system_info , file , indent = 5)