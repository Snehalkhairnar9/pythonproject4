# File          : pythonproject1.py
# Author        : Snehal Khairnar
# Version       : v1.0
# Created Date  : 08/10/2021
# Description   : Testing the functionality of List, Tuples
# Licensing     : Snehal Khairnar, LYIT
# ----------------------------------
import platform

p = platform.uname()
def os_info():

    print("machine :", p.machine)
    print("system :", p.system)
    print("node :", p.node)
    print("version :", p.version)
    print("processor :", p.processor)
    print("release :", p.release)

if "__name__" == "__main__":
   print("details are as below")

os_info()
