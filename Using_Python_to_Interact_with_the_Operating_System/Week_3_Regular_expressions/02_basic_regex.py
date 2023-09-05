import re

"""
- Wildcards: . (Any), ^ (Beggining of line), $ (end of line)
- Character Classes: [Pp] [a-z] [A-Z] [0-9] [a-zA-Z0-9] 
    - to exclude we use [^] for example: [^a-Z] will exclude all lower case letters.
    - OR we use the symbol "|" example: "cat|dog"
- Repetition Qualifiers: 
    - .* (any number including zero), + (once or more), ? (zero or one)
- Special Characters: .*+?^$[]
- Escaping Characters: \
    - In case that we want to use an Special character to match, we use \
    for example "\." will include the "." in the match instead of any character.
    - "\w" will match any alphanumeric character including "_"
    - "\d" will match digits
    - "\s" will match whitespace characters (Space, Tab or New line)
    - "\b" will macth word boundaries

To test and analyze your regex, visit www.regex101.com
"""

# We use "r" before the string to let python know that it's a RAW String.


result = re.search(r"aza", "plaza")
print(result)
# <re.Match object; span=(2, 5), match='aza'>

result = re.search(r"aza", "bazaar")
print(result)
# <re.Match object; span=(1, 4), match='aza'>

result = re.search(r"aza", "maze")
print(result)
# None

print(re.search(r"^x", "xenon"))
# <re.Match object; span=(0, 1), match='x'>

print(re.search(r"p.ng", "penguin"))
# <re.Match object; span=(0, 4), match='peng'>

print(re.search(r"p.ng", "clapping"))
# <re.Match object; span=(4, 8), match='ping'>

print(re.search(r"p.ng", "sponge"))
# <re.Match object; span=(1, 5), match='pong'>

print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
# <re.Match object; span=(0, 4), match='Pang'>

print(re.search(r"[Pp]ython", "Python"))
# <re.Match object; span=(0, 6), match='Python'>

print(re.search(r"[a-z]way", "The end of the highway"))
# <re.Match object; span=(18, 22), match='hway'>

print(re.search(r"[a-z]way", "What a way to go"))
# None

print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
# <re.Match object; span=(0, 6), match='cloudy'>

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
# <re.Match object; span=(4, 5), match=' '>

print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
# <re.Match object; span=(30, 31), match='.'>

print(re.search("cat|dog", "I like cats."))
# <re.Match object; span=(7, 10), match='cat'>

print(re.search("cat|dog", "I like dogs."))
# <re.Match object; span=(7, 10), match='dog'>

print(re.search("cat|dog", "I like both dogs and cats."))
# <re.Match object; span=(12, 15), match='dog'>

print(re.findall("cat|dog", "I like both dogs and cats."))
# ['dog', 'cat']

print(re.search(r"Py.*n", "The Pygmalion"))
# <re.Match object; span=(4, 13), match='Pygmalion'>

print(re.search(r"Py.*n", "Python Programming"))
# <re.Match object; span=(0, 17), match='Python Programmin'>

print(re.search(r"Py[a-z]*n", "Python Programming"))
# <re.Match object; span=(0, 6), match='Python'>

print(re.search(r"Py[a-z]*n", "Pyn"))
# <re.Match object; span=(0, 3), match='Pyn'>

print(re.search("o+l+", "goldfish"))
# <re.Match object; span=(1, 3), match='ol'>

print(re.search("o+l+", "wooly"))
# <re.Match object; span=(1, 4), match='ool'>

print(re.search("o+l+", "boil"))
# None

print(re.search(r"p?each", "To each their own"))
# <re.Match object; span=(3, 7), match='each'>

print(re.search(r"p?each", "I like peaches"))
# <re.Match object; span=(7, 12), match='peach'>

print(re.search(r".com", "welcome"))
# <re.Match object; span=(2, 6), match='lcom'>

print(re.search(r"\.com", "welcome"))
# None

print(re.search(r"\.com", "mydomain.com"))
# <re.Match object; span=(8, 12), match='.com'>

print(re.search(r"\w*", "This is an example"))
# <re.Match object; span=(0, 4), match='This'>

print(re.search(r"\w*", "And_this_is_another example"))
# <re.Match object; span=(0, 19), match='And_this_is_another'>
