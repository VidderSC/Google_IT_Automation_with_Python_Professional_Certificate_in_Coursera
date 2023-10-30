import os

# Windows Powershell we can see them all listed with "dir Env:"

print("COMPUTERNAME: " + os.environ.get("COMPUTERNAME", ""))
print("OS: " + os.environ.get("OS", ""))
print("USERNAME: " + os.environ.get("USERNAME", ""))
