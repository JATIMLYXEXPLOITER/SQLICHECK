import os

print("""1. Start Multi Target
2. Start Single Target
3. Back""")

def multi():
  file = "./paymul/multi.py"
  os.system("python3 {}".format(file))

def tar():
  file = "./payload/method2.py"
  os.system("python3 {}".format(file))
  
def main():
  while True:
    lyx_put = input("root@tpnet> ")
    if lyx_put == "1":
      multi()
    elif lyx_put == "2":
      tar()
    elif lyx_put == "3":
      print("kamu akan dikembalikan ke script awal")
      break
    else:
      print("wrong try again!")
      
if __name__ == "__main__":
  main()
