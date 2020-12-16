import platform
from bcolors import *


my_system = platform.uname()    



print(f"{bcolors.FAIL}{bcolors.BOLD}    ──▐─▌──▐─▌──{bcolors.ENDC}"+"        |"+f"{bcolors.WARNING}{bcolors.BOLD}System: {my_system.system}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    ─▐▌─▐▌▐▌─▐▌─{bcolors.ENDC}"+"        |"+f"{bcolors.WARNING}{bcolors.BOLD}Node Name: {my_system.node}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    ─█▄▀▄██▄▀▄█─{bcolors.ENDC}"+"        |"+f"{bcolors.WARNING}{bcolors.BOLD}Release: {my_system.release}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    ──▄──██▌─▄──{bcolors.ENDC}"+"        |"+f"{bcolors.WARNING}{bcolors.BOLD}Version: {my_system.version}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    ▄▀─█▀██▀█─▀▄{bcolors.ENDC}"+"        |"+f"{bcolors.WARNING}{bcolors.BOLD}Processor: {my_system.processor}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    ▐▌▐▌─▐▌─▐▌▐▌{bcolors.ENDC}"+"        |"+f"{bcolors.WARNING}{bcolors.BOLD}Machine: {my_system.machine}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    ─▐─█────█─▌─{bcolors.ENDC}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    -───▌──▐────{bcolors.ENDC}")


