
#auther: linwincloud

from ast import Return
import os
import getpass
from pickle import TRUE
from pickletools import read_uint1
import socket
import command


def GetUsers():
    UsersName = getpass.getuser()
    return UsersName

def GetHostName():
    HostName = socket.gethostname()
    return HostName

def GetWorkPath():
    WorkPath = os.getcwd()

    return WorkPath

def GetHome():
    Home = os.environ['HOME']
    return Home

def RunNowPath():
    Getrun= open("/opt/KylinShell/config/path.txt")
    nowPath = Getrun.read()
    return nowPath

def main():
    print('''
    Welcome to KyLin Shell
    You can visit URL: https://github.com/LinWin-Cloud
    ''')
    #read the version info
    OpenVersion = open("/opt/KylinShell/config/version.txt")
    Version = OpenVersion.read()
    print("    [!]Version: "+Version)
    print('')
    #empty the path file
    with open("/opt/KylinShell/config/path.txt" , "w") as f:
        home = GetHome()
        f.write(home)
    Work = GetHome()
    Command_Line(Work)

def Command_Line(Work):
    Users = GetUsers()
    HostName = GetHostName()
    NowPath = RunNowPath()
    home = GetHome()
    Command = input(Users+"@"+HostName+": "+Work+" $ ")

    GetLen = len(Command)
    #cd command
    if "cd" in Command:
        char_cd = "cd "
        try:
            if Command.index(char_cd) == 0:
                cdPATH = Command[3:GetLen]
                if "/" in cdPATH:
                    if os.path.exists(cdPATH):
                        with open("/opt/KylinShell/config/path.txt" , "w") as f:
                            f.write(cdPATH)
                        Command_Line(cdPATH)
                        return True
                    else:
                        Command_Line(NowPath)
                        return False
                else:
                    Dircd = NowPath+"/"+cdPATH
                    if os.path.exists(Dircd):
                        if os.path.isfile(Dircd):
                            print('[!]Target is a file')
                            return False
                        else:
                            with open("/opt/KylinShell/config/path.txt" , "w") as f:
                                f.write(Dircd)
                            Command_Line(Dircd)
                            return True
                    else:
                        print('Do not Find Path: '+cdPATH)
                        Command_Line(RunNowPath())
                        return False
            if Command == "cd ~":
                with open("/opt/KylinShell/config/path.txt" , "w") as f:
                    f.write(home)
                Command_Line(Dircd)
        except:
            Command_Line(NowPath)
            return False
        return True
    if Command == "exit":
        exit()
    elif Command == "dir":
        print("=[]= List The Dir: "+NowPath)
        try:
            filename_list = os.listdir(NowPath)
            for i in range(len(filename_list)):   
                new_path = os.path.join(NowPath,filename_list[i])    
                if os.path.isdir(new_path):
                    print("  ||-----Dir: "+filename_list[i])
                if os.path.isfile(new_path):     
                    print("  ||-----File: "+filename_list[i])
            Command_Line(NowPath)
            return True
        except:
            Command_Line(NowPath)
            return False
    
    elif Command == "webstart":
        #start the web browser
        command.startweb()
        Command_Line(NowPath)
        return True
    elif Command == "whois":
        #whois look
        command.Whois()
        Command_Line(NowPath)
        return True
    elif Command == "":
        Command_Line(NowPath)
        return True
    elif Command == "get-sysinfo":
        command.Get_sysinfo()
        Command_Line(NowPath)
    elif Command == "cls":
        os.system('clear')
        Command_Line(NowPath)
        return True 
    elif Command == "get-netinfo":
        #get the network information
        command.Get_netinfo()
        Command_Line(NowPath)
        return True
    elif Command == "about":
        #print the about info
        command.about()
        Command_Line(NowPath)
        return True
    elif Command == 'debbuild':
        #create deb path
        command.DebBuild()
        Command_Line(NowPath)
        return True
    elif Command == "help":
        openhelp = open("/opt/KylinShell/config/help.txt")
        Help = openhelp.read()
        print(Help)
        Command_Line(NowPath)
        return True
    else:
        NowPath = RunNowPath()
        os.system("cd "+NowPath+" && "+Command) #use bash command
        Command_Line(Work)
        return False

main()