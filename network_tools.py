import re
import subprocess
import ctypes
import os

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

if isAdmin() == False:
    print(r"""
    ________   ____   .______          _______.     ___      
    |       /  |___ \  |   _  \        /       |    /   \     
    `---/  /     __) | |  |_)  |      |   (----`   /  ^  \    
    /  /     |__ <  |      /        \   \      /  /_\  \   
    /  /----. ___) | |  |\  \----.----)   |    /  _____  \  
    /________||____/  | _| `._____|_______/    /__/     \__\ """)
    print("\n****************************************************************")
    print("\n* Copyright of z3rsaM67, 2022                                  *")
    print("\n* https://github.com/z3rsaboi                                  *")
    print("\n****************************************************************")
    print(" Tolong gunakan Administator untuk menjalankan program ini!")
    os.system('cmd /k "pause & exit"')
else:
    print(r"""
    ________   ____   .______          _______.     ___      
    |       /  |___ \  |   _  \        /       |    /   \     
    `---/  /     __) | |  |_)  |      |   (----`   /  ^  \    
    /  /     |__ <  |      /        \   \      /  /_\  \   
    /  /----. ___) | |  |\  \----.----)   |    /  _____  \  
    /________||____/  | _| `._____|_______/    /__/     \__\ """)
    print("\n****************************************************************")
    print("\n* Copyright of z3rsaM67, 2022                                  *")
    print("\n* https://github.com/z3rsaboi                                  *")
    print("\n****************************************************************")

    print(" 1. WLAN Report")
    print(" 2. DNS Resolver")
    print(" 3. IP Address")
    print(" 4. Wi-Fi Password")
    print(" 5. Informasi Web")
    print(" 6. Setingan DNS\n")
    print(" 'e' untuk keluar dari program\n")

    user_input = input(" Pilih: ")

    if user_input == '1':
        os.system('cmd /k "netsh wlan show wlanreport & START C:\ProgramData\Microsoft\Windows\WlanReport\wlan-report-latest.html & cls & start network_tools.exe & exit"')
    elif user_input == '2':
        os.system('cmd /k "ipconfig /flushdns & ipconfig /release & ipconfig /renew & cls & start network_tools.exe & exit"')
    elif user_input == '3':
        os.system('cmd /k "ipconfig | findstr IPv4 & echo. & echo  Tekan enter untuk lanjut & pause >n & cls & start network_tools.exe & exit"')
    elif user_input == '4':
        # This Script Is From David Bombal
        command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
        profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
        wifi_list = []
        if len(profile_names) != 0:
            for name in profile_names:
                wifi_profile = {}
                profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
                if re.search("Security key           : Absent", profile_info):
                    continue
                else:
                    wifi_profile["ssid"] = name
                    profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
                    password = re.search("Key Content            : (.*)\r", profile_info_pass)
                    if password == None:
                        wifi_profile["password"] = None
                    else:
                        wifi_profile["password"] = password[1]
                        wifi_list.append(wifi_profile)
        for x in range(len(wifi_list)):
            print(wifi_list[x])
        
        os.system('cmd /k "pause & cls & start network_tools.exe & exit"')
    elif user_input == '5':
        web_input = input(" Masukan Domain: ")
        print("")
        os.system('cmd /c "nslookup "' + str(web_input))
        os.system('cmd /c "pause"')
        os.system('cmd /k "cls & start network_tools.exe & exit"')
    elif user_input == '6':
        os.system('cmd /c "netsh interface show interface"')
        print(" Diatas merupakan Interface yang sedang dipakai\n")
        interface_input = input(" Masukan Interface, contoh (Ethernet): ")
        print(" DNS yang tersedia: "  )
        print(" 1. Google DNS, (8.8.8.8) dan (8.8.4.4)")
        print(" 2. Cloudflare, (1.1.1.1) dan (1.0.0.1)")
        print(" 3. OpenDNS, (208.67.222.222) dan (208.67.220.220)")
        dns_input = input(" Pilih DNS yang diinginkan: ")
        interface_input_cap = interface_input.capitalize()
        dns = []
        if dns_input == '1':
            os.system('cmd /c "netsh interface ipv4 set dns name="' + interface_input_cap + " static 8.8.8.8")
            os.system('cmd /c "netsh interface ipv4 add dns name="' + interface_input_cap + " 8.8.4.4" + " index=2 validate=no")
            os.system('cmd /c "ipconfig /flushdns"')
            dns = "8.8.8.8"
        elif dns_input == '2':
            os.system('cmd /c "netsh interface ipv4 set dns name="' + interface_input_cap + " static 1.1.1.1")
            os.system('cmd /c "netsh interface ipv4 add dns name="' + interface_input_cap + " 1.0.0.1" + " index=2 validate=no")
            os.system('cmd /c "ipconfig /flushdns"')
            dns = "1.1.1.1"
        elif dns_input == '3':
            os.system('cmd /c "netsh interface ipv4 set dns name="' + interface_input_cap + " static 208.67.222.222")
            os.system('cmd /c "netsh interface ipv4 add dns name="' + interface_input_cap + " 208.67.220.220" + " index=2 validate=no")
            os.system('cmd /c "ipconfig /flushdns"')
            dns = "208.67.222.222"
        else:
            os.system('cmd /k "echo  Tidak ada pilihan tersebut! tekan enter untuk lanjut & pause >n & cls & python cmd_network.py"')
        os.system('cmd /c "netsh interface ip show dnsservers & powershell "Measure-Command { nslookup dns }" & pause"')
        os.system('cmd /k "cls & start network_tools.exe & exit"')
        
    elif user_input == 'e':
        exit()
    else:
        print(" Tidak ada pilihan tersebut!")
        os.system('cmd /c "echo  Tekan enter untuk lanjut & pause >n"')
        os.system('cmd /k "cls & start network_tools.exe & exit"')