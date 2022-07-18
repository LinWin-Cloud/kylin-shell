import os
import time
import requests
import webbrowser
import whois
import platform
import sys
import socket


def startweb():
    URL = input('Enter The URL: ')
    try:
        URLGet = requests.get(URL)
        if URLGet.status_code == 200:
            #ok
            webbrowser.open(URL)
            return True
        else:
            #error
            print('[!]Do not Find: '+URL)
            return False
    except:
        print('[!]Do not Find: '+URL)
        return False

def Whois():
    Website = input('Enter The Website: ')
    try:
        GetWhois = whois.whois(Website)
        print(GetWhois)
        return True
    except:
        print('[!]Do not Find Whois: '+Website)
        return False

def Get_sysinfo():

    arch = str(platform.architecture())
    uname = str(platform.uname())

    print('')
    print('  Work Path: '+os.getcwd())
    print('  Architecture: '+arch)
    print('  Computer Name: '+platform.node())
    print('  Processor: '+platform.processor())
    print('  OsName: '+os.name)
    print('  Os Version: '+ platform.version())
    print('  Uname: '+uname+'\n')
    print('  Encoding: '+sys.getdefaultencoding())
    print('  OS: '+platform.system())

    print('')
    return True

def Get_netinfo():

    nameinfo = socket.getnameinfo

    print('  HostName: '+socket.gethostname())
    print('  IP: ' + socket.gethostbyname(socket.gethostname()))
    print('  Name Info: '+str(nameinfo))

    return True

def about():
    a = open('/opt/KylinShell/config/about.txt')
    b = a.read()
    print('')
    print(b)
    print('')

def MakeFile(Name):
    os.system("echo > "+Name)

def DebBuild():
    Path = input('Enter The Target Path: ')
    if os.path.exists(Path):
        if os.path.isdir(Path):
            ProjectName = input('Enter the Project Name: ')
            
            print(
    "Build Info:\n"+
    "   Path: "+Path+"\n"+
    " Project Name: "+ProjectName
            )
            
            os.mkdir(Path+"/"+ProjectName)
            os.mkdir(Path+"/"+ProjectName+"/bin")
            os.mkdir(Path+"/"+ProjectName+"/DEBIAN")
            os.mkdir(Path+"/"+ProjectName+"/opt")
            os.mkdir(Path+"/"+ProjectName+"/etc")
            os.mkdir(Path+"/"+ProjectName+"/usr")
            os.mkdir(Path+"/"+ProjectName+"/usr/share")
            os.mkdir(Path+"/"+ProjectName+"/usr/share/applications")
            control = """"
Package: 
Version: 
Section: 
Priority: 
Architecture: 
Installed-Size: 
Maintainer: 
Provides: 
Description: 
Pre-Depends: 
Hompage: 

            """
            with open(Path+"/"+ProjectName+"/DEBIAN/control" , 'w') as f:
                f.write(control)
            time.sleep(1)
            print('[+]Build OK')
            return True
        else:
            print('[!]Target Path is a file')
            return False
    else:
        print('[!]Target Path is not exists')
        return False