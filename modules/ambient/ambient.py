import subprocess

# I know, i know, this is probably the worst solution to a trivial challenge. Still, if it aint broke...
def change_ambient(color):
    script = """add-type -typedefinition "using System;`n using System.Runtime.InteropServices;`n public class PInvoke { [DllImport(`"user32.dll`")] public static extern bool SetSysColors(int cElements, int[] lpaElements, int[] lpaRgbValues); }"; [PInvoke]::SetSysColors(1, @(1), @(0x""" + color + """))"""
    subprocess.Popen(["powershell.exe", "-noprofile", "-noninteractive", "-nologo", script], stdout=None)