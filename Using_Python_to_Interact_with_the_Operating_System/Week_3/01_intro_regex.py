import re


log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

# -----
# El modificador "-i" "/i" es para que no diferencie entre mayúsculas y minúsculas.

# Nos explica como usar "grep" en Linux:
# grep -i python /usr/share/dict/words

# El equivalente para windows es "findstr":
# findstr /i "python" words.txt

# returns:
# Python
# Python's
# python
# python's
# pythons

# -----
# El "." se usa como comodín.

# grep l.rts /usr/share/dict/words
# findstr "l.rts" words.txt

# returns:
# alerts
# blurts
# flirts

# -----
# El "^" se pone antes de la palabra y se usa para encontrar líneas 
# que empiecen con esa palabra.

# grep ^fruit /usr/share/dict/words
# findstr "^fruit" words.txt

# Returns:
# fruit
# fruit's
# fruitcake
# fruitcake's
# fruitcakes
# fruited
# fruitful
# fruitfully
# fruitfulness
# fruitfulness's
# fruitier
# fruitiest
# fruiting
# fruition
# fruition's
# fruitless
# fruitlessly
# fruitlessness
# fruitlessness's
# fruits
# fruity

# -----
# El "$" se pone después de la palabra y se usa para encontrar líneas 
# que terminen con esa palabra.

# grep fruit$ /usr/share/dict/words
# findstr "fruit$" words.txt

# Returns:
# breadfruit
# fruit
# grapefruit

# -----
