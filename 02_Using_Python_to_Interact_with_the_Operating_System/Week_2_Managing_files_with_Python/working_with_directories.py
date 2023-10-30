import os

# Mostramos el directorio actual
print(os.getcwd())

# Mostramos el contenido del directorio actual
print(os.listdir())

# Creamos un directorio
os.mkdir("test_dir")

# filtramos lo que muestra el listdir para solamente ver los directorios.
list_dir = os.listdir()
for file in list_dir:
    if os.path.isdir(file):
        print(file)

# Nos cambiamos a ese directorio
os.chdir("test_dir")

print(os.getcwd())

list_dir = os.listdir()
for file in list_dir:
    if os.path.isdir(file):
        print(file)

# Nos volvemos un directorio atrás
os.chdir("..")

print(os.getcwd())

# Borramos el directorio (Solo si está vacío)
os.rmdir("test_dir")

print(os.listdir())

print()

dir = "test_directory"

os.listdir(dir)

# We use os.path.join to use the relative path,
# as it will join using the correct slash for the OS.

for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print(f"{fullname} is a directory")
    else:
        print(f"{fullname} is a file")

print()


def parent_directory():
    # Create a relative path to the parent
    # of the current working directory
    print(os.getcwd())
    relative_parent = os.path.join(os.getcwd(), os.pardir)
    print(relative_parent)
    # Return the absolute path of the parent directory
    return os.path.abspath(relative_parent)


print(parent_directory())
