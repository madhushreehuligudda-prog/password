import sys
#default values
Password = "12345678"
if len(sys.argv):
    script_name = sys.argv[0];
    Password = sys.argv[1];
    Confirm_password = sys.argv[2];
    print("user input password is:",Password)
else:
    print("no user input password, using default password:",Password)
    if Password == Confirm_Password:
        print("password matched")
    else:
        print("password did not match")

#display results
print("script_name:",script_name)
print("password:",Password)
print("confirm_password:",Confirm_password)