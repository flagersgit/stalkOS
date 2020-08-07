from pypresence import Presence
import time
import platform
import os
import sys
import psutil

print("Running on " + platform.system() + " " + platform.release())

windows_client_id = '740910532734746646' # Client ID for Windows
darwin_client_id = '740908324039557262' # Client ID for Darwin
linux_client_id = '740910996217921546' # Client ID for Linux

# START WINDOWS SECTION

WinVerLookup = {
    "10240" : {
        "release" : "10",
        "version" : "1507"
    },
    "10586" : {
        "release" : "10",
        "version" : "1511"
    },
    "14393" : {
        "release" : "10",
        "version" : "1607"
    },
    "15063" : {
        "release" : "10",
        "version" : "1703"
    },
    "16299" : {
        "release" : "10",
        "version" : "1709"
    },
    "17134" : {
        "release" : "10",
        "version" : "1803"
    },
    "17763" : {
        "release" : "10",
        "version" : "1809"
    },
    "18362" : {
        "release" : "10",
        "version" : "1903"
    },
    "18363" : {
        "release" : "10",
        "version" : "1909"
    },
    "19041" : {
        "release" : "10",
        "version" : "2004"
    },
    "9200" : {
        "release" : "8"
    },
    "9600" : {
        "release" : "8.1"
    },
    "7601" : {
        "release" : "7",
        "version" : "Service Pack 1"
    }
}

# Windows 10
if platform.system() == "Windows":
    if platform.release() == str(10):
        LocalBuildNumber = str(sys.getwindowsversion().build)
        LocalReleaseID = str(WinVerLookup.get(LocalBuildNumber).get('version'))
        RPC = Presence(windows_client_id)
        RPC.connect()
        print(RPC.update(
            state="Processes running: {}".format(str(len(psutil.pids()))),
            details="Windows 10 [{}]".format(LocalReleaseID),
            large_image="win2012", 
            large_text="Windows 10 [{}]".format(LocalReleaseID),
            small_image="small_stalkos_logo",
            small_text="stalkOS Project by Flagers",
            start=int(psutil.boot_time())
        ))

# Windows 8
if platform.system() == "Windows":
    if platform.release() == str(6.2) or platform.release() == str(6.3):
        LocalBuildNumber = str(sys.getwindowsversion().build)
        if str(WinVerLookup.get(LocalBuildNumber).get('release')) == 8:
            RPC = Presence(windows_client_id)
            RPC.connect()
            print(RPC.update(
                state="Processes running: {}".format(str(len(psutil.pids()))), 
                details="Windows 8", 
                large_image="win2012", 
                large_text="Windows 8",
                small_image="small_stalkos_logo",
                small_text="stalkOS Project by Flagers",
                start=int(psutil.boot_time())
            ))
            
# Windows 8.1
if platform.system() == "Windows":
    if platform.release() == str(6.2) or platform.release() == str(6.3):
        LocalBuildNumber = str(sys.getwindowsversion().build)
        if str(WinVerLookup.get(LocalBuildNumber).get('release')) == 8.1:
            RPC = Presence(windows_client_id)
            RPC.connect()
            print(RPC.update(
                state="Processes running: {}".format(str(len(psutil.pids()))), 
                details="Windows 8.1", 
                large_image="win2012", 
                large_text="Windows 8.1",
                small_image="small_stalkos_logo",
                small_text="stalkOS Project by Flagers",
                start=int(psutil.boot_time())
            ))
            
# Windows 7
if platform.system() == "Windows":
    if platform.release() == str(6.1):
        LocalBuildNumber = str(sys.getwindowsversion().build)
        if str(WinVerLookup.get(LocalBuildNumber).get('release')) == 7:
            RPC = Presence(windows_client_id)
            RPC.connect()
            print(RPC.update(
                state="Processes running: {}".format(str(len(psutil.pids()))), 
                details="Windows 7 [Service Pack 1]", 
                large_image="win2008", 
                large_text="Windows 7 [Service Pack 1]", 
                small_image="small_stalkos_logo",
                small_text="stalkOS Project by Flagers",
                start=int(psutil.boot_time())
            ))
            
# STARTING DARWIN SECTION

# macOS Big Sur / 10.16.*
if platform.system() == "Darwin":
    if "10.16" in platform.mac_ver()[0]:
        RPC = Presence(darwin_client_id)
        RPC.connect()
        print(RPC.update(
            state="Processes running: {}".format(str(len(psutil.pids()))), 
            details="macOS Big Sur [{}]".format(platform.mac_ver()[0]),
            large_image="generic_macos",
            large_text="macOS Big Sur [{}]".format(platform.mac_ver()[0]),
            small_image="small_stalkos_logo",
            small_text="stalkOS Project by Flagers",
            start=int(psutil.boot_time())
        ))
        
# macOS Catalina / 10.15.*
if platform.system() == "Darwin":
    if "10.15" in platform.mac_ver()[0]:
        RPC = Presence(darwin_client_id)
        RPC.connect()
        print(RPC.update(
            state="Processes running: {}".format(str(len(psutil.pids()))), 
            details="macOS Catalina [{}]".format(platform.mac_ver()[0]),
            large_image="icon_catalina",
            large_text="macOS Catalina [{}]".format(platform.mac_ver()[0]),
            small_image="small_stalkos_logo",
            small_text="stalkOS Project by Flagers",
            start=int(psutil.boot_time())
        ))
        
# macOS Mojave / 10.14.*
if platform.system() == "Darwin":
    if "10.14" in platform.mac_ver()[0]:
        RPC = Presence(darwin_client_id)
        RPC.connect()
        print(RPC.update(
            state="Processes running: {}".format(str(len(psutil.pids()))), 
            details="macOS Mojave [{}]".format(platform.mac_ver()[0]),
            large_image="icon_mojave",
            large_text="macOS Mojave [{}]".format(platform.mac_ver()[0]),
            small_image="small_stalkos_logo",
            small_text="stalkOS Project by Flagers",
            start=int(psutil.boot_time())
        ))
        
# macOS High Sierra / 10.13.*
if platform.system() == "Darwin":
    if "10.13" in platform.mac_ver()[0]:
        RPC = Presence(darwin_client_id)
        RPC.connect()
        print(RPC.update(
            state="Processes running: {}".format(str(len(psutil.pids()))), 
            details="macOS High Sierra [{}]".format(platform.mac_ver()[0]),
            large_image="icon_highsierra",
            large_text="macOS High Sierra [{}]".format(platform.mac_ver()[0]),
            small_image="small_stalkos_logo",
            small_text="stalkOS Project by Flagers",
            start=int(psutil.boot_time())
        ))

# macOS Sierra / 10.12.*
if platform.system() == "Darwin":
    if "10.12" in platform.mac_ver()[0]:
        RPC = Presence(darwin_client_id)
        RPC.connect()
        print(RPC.update(
            state="Processes running: {}".format(str(len(psutil.pids()))), 
            details="macOS Sierra [{}]".format(platform.mac_ver()[0]),
            large_image="icon_sierra",
            large_text="macOS Sierra [{}]".format(platform.mac_ver()[0]),
            small_image="small_stalkos_logo",
            small_text="stalkOS Project by Flagers",
            start=int(psutil.boot_time())
        ))

# OS X El Capitan / 10.11.*
if platform.system() == "Darwin":
    if "10.11" in platform.mac_ver()[0]:
        RPC = Presence(darwin_client_id)
        RPC.connect()
        print(RPC.update(
            state="Processes running: {}".format(str(len(psutil.pids()))), 
            details="OS X El Capitan [{}]".format(platform.mac_ver()[0]),
            large_image="icon_elcapitan",
            large_text="OS X El Capitan [{}]".format(platform.mac_ver()[0]),
            small_image="small_stalkos_logo",
            small_text="stalkOS Project by Flagers",
            start=int(psutil.boot_time())
        ))

# OS X Yosemite / 10.10.*
if platform.system() == "Darwin":
    if "10.10" in platform.mac_ver()[0]:
        RPC = Presence(darwin_client_id)
        RPC.connect()
        print(RPC.update(
            state="Processes running: {}".format(str(len(psutil.pids()))), 
            details="OS X Yosemite [{}]".format(platform.mac_ver()[0]),
            large_image="icon_yosemite",
            large_text="OS X Yosemite [{}]".format(platform.mac_ver()[0]),
            small_image="small_stalkos_logo",
            small_text="stalkOS Project by Flagers",
            start=int(psutil.boot_time())
        ))

# OS X Mavericks / 10.9.*
if platform.system() == "Darwin":
    if "10.9" in platform.mac_ver()[0]:
        RPC = Presence(darwin_client_id)
        RPC.connect()
        print(RPC.update(
            state="Processes running: {}".format(str(len(psutil.pids()))), 
            details="OS X Mavericks [{}]".format(platform.mac_ver()[0]),
            large_image="icon_mavericks",
            large_text="OS X Mavericks [{}]".format(platform.mac_ver()[0]),
            small_image="small_stalkos_logo",
            small_text="stalkOS Project by Flagers",
            start=int(psutil.boot_time())
        ))

# OS X Mountain Lion / 10.8.*
if platform.system() == "Darwin":
    if "10.8" in platform.mac_ver()[0]:
        RPC = Presence(darwin_client_id)
        RPC.connect()
        print(RPC.update(
            state="Processes running: {}".format(str(len(psutil.pids()))), 
            details="OS X Mountain Lion [{}]".format(platform.mac_ver()[0]),
            large_image="icon_mountainlion",
            large_text="OS X Mountain Lion [{}]".format(platform.mac_ver()[0]),
            small_image="small_stalkos_logo",
            small_text="stalkOS Project by Flagers",
            start=int(psutil.boot_time())
        ))

# Mac OS X Lion / 10.7.*
if platform.system() == "Darwin":
    if "10.7" in platform.mac_ver()[0]:
        RPC = Presence(darwin_client_id)
        RPC.connect()
        print(RPC.update(
            state="Processes running: {}".format(str(len(psutil.pids()))), 
            details="Mac OS X Lion [{}]".format(platform.mac_ver()[0]),
            large_image="icon_lion",
            large_text="Mac OS X Lion [{}]".format(platform.mac_ver()[0]),
            small_image="small_stalkos_logo",
            small_text="stalkOS Project by Flagers",
            start=int(psutil.boot_time())
        ))
        
# Mac OS X Snow Leopard / 10.6.*
if platform.system() == "Darwin":
    if "10.6" in platform.mac_ver()[0]:
        RPC = Presence(darwin_client_id)
        RPC.connect()
        print(RPC.update(
            state="Processes running: {}".format(str(len(psutil.pids()))), 
            details="Mac OS X Snow Leopard [{}]".format(platform.mac_ver()[0]),
            large_image="icon_snowleopard",
            large_text="Mac OS X Snow Leopard [{}]".format(platform.mac_ver()[0]),
            small_image="small_stalkos_logo",
            small_text="stalkOS Project by Flagers",
            start=int(psutil.boot_time())
        ))
        
# START LOONIX SECTION

while True: # Keep the DRP going!
    time.sleep(15)