defusername = "Alexjr24"
defpassword ="Alex2404"

while(True):
    username = input("Username:")
    password = input("Password:")
    if ((username == defusername) and (password == defpassword)):
        print ("welcome", username)
        break
    elif ((username != defusername) and (password == defpassword)):
        print("You entered wrong username")
    elif ((username == defusername) and (password != defpassword)):
        print("Did you for get your password?")
        print("Would you like to change your password?")
        cevap = input()
        if (answer == "YES"):

          newpassword = input("New password:")
          print("Please wait")
          defpassword = newpassword
          print("Password succesfuly changed")
else:
    print("ry again")