import subprocess
from ctypes import *
# I know, i know, this is probably the worst solution to a trivial challenge. Still, if it aint broke...


class Ambient:
    def __init__(self):
        self.user32 = WinDLL("user32.dll")

    def change_color(self, r,g,b):
        rgb = r + (g<<8) + (b<<16)
        self.user32.SetSysColors(1, byref(c_int(1)), byref(c_int(rgb)))

