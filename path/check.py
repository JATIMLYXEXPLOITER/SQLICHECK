import os 
import time

print("""\n]=========== Menu ============[
  1. Get Information Website
  2. Path Finder\n""")
  
def Information():
  file = "./path/inf.py"
  os.system("python3 {}".format(file))
  
def path():
  file = "./path/find.py"
  os.system("python3 {}".format(file))

def main():
  while True:
    lyx_put = input("root@tpnet> ")
    if lyx_put == "2":
      path()
    elif lyx_put == "1":
      Information()
    elif lyx_put == "exit":
      print("exit.")
      break
    else:
      print("wrong input")
      
if __name__ == "__main__":
  main()
