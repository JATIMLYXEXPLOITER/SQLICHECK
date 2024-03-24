import os, time

print("""1. Payload biasa '
2. Payload ' OR 1=1-- 1-- (check query SQL)
3. Payload? Hanya bisa digunakan untuk injection!
4. exit program
""")

def payload1():
  file = "./payload/method1.py"
  os.system("python3 {}".format(file))
    
def payload2():
  file = "./payload/method2.py"
  os.system("python3 {}".format(file))
    
def payload3():
  file = "./payload/method3.py"
  os.system("python3 {}".format(file))

def payload4():
  file = "./payload/method4.py"
  os.system("python3 {}".format(file))
    
def payload5():
  file = "./payload/method5.py"
  os.system("python3 {}".format(file))
  
def payload6():
  file = "./payload/method6.py"
  os.system("python3 {}".format(file))
  
def payload7():
  file = "./payload/method7.py"
  os.system("python3 {}".format(file))
  
def payload8():
  file = "./payload/method8.py"
  os.system("python3 {}".format(file))
  
def main():
    while True:
      lyx_put = input("root@tpnet> ")
      if lyx_put == "1":
        payload1()
      elif lyx_put == "2":
        payload2()
      elif lyx_put == "3":
        payload3()
      elif lyx_put == "4":
        payload4()
      elif lyx_put == "exit":
        print("kamu akan dikembalikan ke script awal")
        break
      else:
        print("wrong input, try again")
        
if __name__ == "__main__":
  main()
