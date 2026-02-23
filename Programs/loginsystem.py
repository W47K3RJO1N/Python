saved_user = "admin"
saved_pass = "1234"

username = input("Username: ")
password = input("Password: ")

if username == saved_user and password == saved_pass:
    print("Login Successful ✅")
else:
    print("Login Failed ❌")
