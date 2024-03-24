import requests
import os
from colorama import Fore,Style
import platform
from bs4 import BeautifulSoup

fr = Fore.RED
fg = Fore.GREEN
fm = Fore.MAGENTA
fy = Fore.YELLOW
fc = Fore.CYAN
fres = Style.RESET_ALL

os.system("clear")

print("""by TpnetService                                            .!!!~:                                    coder by ./lyx                                             :Y^:~77!!!~:                                                                                          :?!  :~.:~7?!:                                                                                         ?!  ~.   .~??:                                                                                       .J~         ^J?.                                                                                       J!          ?Y.
                                                               .J:           ?Y.
                                                               ^J  !^         ?Y.
                                                               .Y^!PJ^         7J!~:.
                                                                :7J!.7~.        .::~!~:
                                                                      ::.         ^!!7J!
           ^~~^.        ^~~^.                 .::::::::::   .::::::::.  .::.      ~Y?~.
          ~GGPGY.     .JGPPG7                ~77~~~~~~~~^ ^77!~~~~~~!7!..??^        :!!~.
          !GP^YGY.    JG5^PG? :??^      ~J?. 7?!.         !?7.      :??:.7?^           .:
          !GP:.YGY. .JG5:.PG? ^GG~      7GG: .^~~~~~~!!~: !?7.      :??:.7?^
          !GP^ .YGJ.JG5: .PG? ^GG~      7GP:         .7?! !?7. .^~^.:??:.??^         .:::.
          !GP:  .JGPGY:  .PG? .?5Y?????7YGP: ~~~~~~~~!7!: :!7!~~!??77?~  ~77~~~~~~~~::~~~:
          .::     :^:     ::.  .:^~~~~~~YGP: ..........     ..:....:~7~:   .......... ...
                              :JJJJJJJJJJ7^                           ..
to show command use help""")

def help_menu():
  print(f"==================[ {fg}MENU{fres} ]====================")
  print(f"1. spay ({fg}ONLINE{fres})")
  print(f"2. singtar ({fg}ONLINE{fres})")
  print(f"3. multar ({fg}ONLINE{fres})")
  print(f"4. auto inject ({fr}OFFLINE{fres})")
  print(f"5. waf list ({fr}OFFLINE{fres})")
  print(f"6. dork fresh ({fg}OFFLINE{fres})")
  print(f"7. website information ({fg}ONLINE{fres})")
  print (f"\n=============[ {fg}Program Pack{fres} ]=================")
  print(f"8. Install Sqlmap ({fr}KALI LINUX{fres})")
  print(f"9. Install Sqlmap ({fr}TERMUX{fres})")
  print(f"\n==================[ {fg}Feature Menu{fres} ]=================")
  print(f"10. Mode Sqlmap ({fr}KALI LINUX{fres})")
  print(f"11. Mode Sqlmap ({fr}TERMUX{fres})")
  print(f"12. Auto Injection ({fr}OFF{fres})")
  print(f"13. Auto Injection ({fr}OFF{fres})")
  print(f"\n==================[ {fg}End Feature{fres} ]==================")
  print(f"14. To Show Menu Mode Sqlmap ({fr}KALI LINUX{fres})")
  print(f"15. To Show Menu Mode Sqlmap ({fr}TERMUX{fres})")
  print(f"\n================[ {fg}Feature Premium{fres} ]================")
  print(f"[{fy}+{fres}] Auto WAF ByPass")
  print(f"[{fy}+{fres}] Vuln Check")
  print(f"[{fy}+{fres}] Bypass ChatGPT")
  print(f"[{fy}+{fres}] ETC")
  print(f"[{fg}V{fres}.{fc}I{fres}.{fg}P{fres}] 16. To Buy Premium Feature: D")
  print(f"[{fc}\/{fres}] Powered /lyx")
  print(f"[{fc}\/{fres}] Terima Kasih telah menggunakan tools kami:)")
  print(f"\n========[ note: {fg}Command hanya bisa digunakan menggunakan angka/tulis manual!{fres}")

def spay():
  url = "https://raw.githubusercontent.com/payloadbox/sql-injection-payload-list/master/Intruder/exploit/Auth_Bypass.txt"
  response = requests.get(url)
  if response.status_code == 200:
    content = response.text
    print(content)
  else:
    print("gagal mengambil konten url")
  
def singtar():
  file = "./payload/check.py"
  os.system("python3 {}".format(file))

def multar():
  file = "./paymul/check.py"
  os.system("python3 {}".format(file))

def auto():
  file = "./auto/check.py"
  os.system("python3 {}".format(file))
  
def waf_list():
  print("sabar")

def dork_fresh():
  file = "./dork/check.py"
  os.system("python3 {}".format(file))

def install_sql():
  system_platform = platform.system()
  if system_platform == "Linux":
    print("sistem operasi sedang menginstall")
    os.system("sudo apt update")
    os.system("sudo apt install sqlmap")
    print("hey!, done install!")
  elif system_platform == "Android" and "Termux" in platform.release():
    print("sistem operasi sedang berjalan..")
    os.chdir(os.path.expanduser("~"))
    os.system("git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev")
    print("installasi berhasil!")
  else:
    print("warning: unsupported platform or installation method.")
    print("exitting program installasion")
    return

def modesqlnux():
  print(f"[{fm}JANDA{fres}] SCNYA OFFLINE BOS")
  
def modesqlmux():
  print(f"[{fm}JANDA{fres}] SCNYA OFFLINE BOS")

def menumodenux():
  print(f"[{fm}JANDA{fres}] SCNYA OFFLINE BOS")
  
def menumodemux():
  print(f"[{fm}JANDA{fres}] SCNYA OFFLINE BOS")

def path_find():
  file = "./path/check.py"
  os.system("python3 {}".format(file))

def buysc():
  print("you can buy it with IDR120k, $7USD, or with bitcoin. dm me in telegram.")
  
def main():
  while True:
    lyx_put = input("\nroot@tpnet> ")
    if lyx_put == "help":
      help_menu()
    elif lyx_put == "1":
      spay()
    elif lyx_put == "2":
      singtar()
    elif lyx_put == "3":
      multar()
    elif lyx_put == "4":
      auto()
    elif lyx_put == "5":
      waf_list()
    elif lyx_put == "6":
      dork_fresh()
    elif lyx_put == "7":
      path_find()
    elif lyx_put == "8":
      install_sql()
    elif lyx_put == "9":
      install_sql()
    elif lyx_put == "10":
      modesqlnux()
    elif lyx_put == "11":
      modesqlmux()
    elif lyx_put == "12":
      print("ongoing maszeh")
    elif lyx_put == "13":
      print("ongoing maszeh")
    elif lyx_put == "14":
      menumodenux()
    elif lyx_put == "15":
      menumodemux()
    elif lyx_put == "16":
      buysc()
    elif lyx_put == "exit":
      print("thank you for using me<3")
      break
    else:
      print("your input wrong")
      
if __name__ == "__main__":
  main()
      
