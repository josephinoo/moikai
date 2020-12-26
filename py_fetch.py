import platform
from bcolors import *

print(f"{bcolors.FAIL}{bcolors.BOLD}    ──▐─▌──▐─▌──{bcolors.ENDC}"+"        |"+f"{bcolors.WARNING}{bcolors.BOLD}System: {platform.system()}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    ─▐▌─▐▌▐▌─▐▌─{bcolors.ENDC}"+"        |"+f"{bcolors.WARNING}{bcolors.BOLD}Name: {platform.uname()[0]}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    ─█▄▀▄██▄▀▄█─{bcolors.ENDC}"+"        |"+f"{bcolors.WARNING}{bcolors.BOLD}Platform: {platform.uname()[0]}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    ──▄──██▌─▄──{bcolors.ENDC}"+"        |"+f"{bcolors.WARNING}{bcolors.BOLD}Version: { platform.version()}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    ▄▀─█▀██▀█─▀▄{bcolors.ENDC}"+"        |"+f"{bcolors.WARNING}{bcolors.BOLD}Processor: {platform.processor()}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    ▐▌▐▌─▐▌─▐▌▐▌{bcolors.ENDC}"+"        |"+f"{bcolors.WARNING}{bcolors.BOLD}Machine: {platform.machine()}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    ─▐─█────█─▌─{bcolors.ENDC}")
print(f"{bcolors.FAIL}{bcolors.BOLD}    -───▌──▐────{bcolors.ENDC}")


