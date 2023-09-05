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

print(re.search(r"A.*a", "Argentina"))
# <re.Match object; span=(0, 9), match='Argentina'>

print(re.search(r"A.*a", "Azerbaijan"))
# <re.Match object; span=(0, 9), match='Azerbaija'>

print(re.search(r"^A.*a$", "Azerbaijan"))
# None

print(re.search(r"^A.*a$", "Australia"))
# <re.Match object; span=(0, 9), match='Australia'>

# The below patter is used to check for a valid variable name in Python.
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

print(re.search(pattern, "_this_is_a_valid_variable_name"))
# <re.Match object; span=(0, 30), match='_this_is_a_valid_variable_name'>

print(re.search(pattern, "this isn't a valid variable"))
# None

print(re.search(pattern, "my_variable1"))
# <re.Match object; span=(0, 12), match='my_variable1'>

print(re.search(pattern, "2my_variable1"))
# None
