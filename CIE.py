import sys

# default values
Password = "12345678"
Confirm_password = "12345678"   # set default confirm password
script_name = sys.argv[0]

# check argument count
if len(sys.argv) >= 3:
    Password = sys.argv[1]
    Confirm_password = sys.argv[2]
    print("user input password is:", Password)
else:
    print("no user input password, using default password:", Password)

# password check
if Password == Confirm_password:
    print("password matched")
else:
    print("password did not match")

# display results
print("script_name:", script_name)
print("password:", Password)
print("confirm_password:", Confirm_password)
