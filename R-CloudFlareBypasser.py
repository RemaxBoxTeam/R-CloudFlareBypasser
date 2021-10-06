import colorama , pyfiglet
import socket , sys , os
if "win" in sys.platform:
  os.system("pip install colorama pyfiglet")
else:
  os.system("pip3 install colorama pyfiglet")
rd = colorama.Fore.RED
mag = colorama.Fore.MAGENTA
cv = colorama.Fore.WHITE
gn = colorama.Fore.GREEN
bl = colorama.Fore.LIGHTBLUE_EX
yl = colorama.Fore.LIGHTGREEN_EX
def banner():
  fg = pyfiglet.Figlet(font="small").renderText("RemaxBox Team")
  print (bl + fg)
  print (rd + "CloudFlare bypasser , Get Real IP of website")
  print (mag + "Created By Maximum Radikali")

banner()
site = input(bl + "Please Enter a url ex : (google.com)-> ")
f = open("dom.txt","r")
print (yl + "Waiting ...")
for i in f:
  k = i.strip()
  try:
    fs = socket.gethostbyname(k+site)
    print (gn + fs + cv)
    
  except:
    pass
print ("The operation has been successfully :)")
