import subprocess

# dir and cls will work on windows, sleep and date only on linux.
# To use it with VS Code on windows, you can change the terminal to gitbash.

result = subprocess.run(["dir"], shell=True)
print(f"Return Code of 'dir': {result.returncode}")
print()
print("waiting 2 seconds to clear the screen..")
subprocess.run(["sleep", "2"])
subprocess.run(["cls"], shell=True)
print("Todays date is:")
subprocess.run(["date"])

print()

result = subprocess.run(["host", "8.8.8.8"], shell=True, capture_output=True)
print(f"Return Code of 'host': {result.returncode}")
print(f"Stdout of host: {result.stdout.decode().split()}")

print()

result = subprocess.run(["rm", "does_not_exist.txt"], capture_output=True)
print(f"Return Code of 'rm'': {result.returncode}")
print(f"Stdout of 'rm': {result.stdout}")
print(f"Stderr of 'rm': {result.stderr}")
