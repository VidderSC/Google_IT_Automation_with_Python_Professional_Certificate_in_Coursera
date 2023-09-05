# Capturing groups

import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
# <re.Match object; span=(0, 13), match='Lovelace, Ada'>

print(result.groups())
# ('Lovelace', 'Ada')

print(type(result.groups()))

print(result[0])
# Lovelace, Ada
print(result[1])
# Lovelace
print(result[2])
# Ada
print()

print(f"{result[2]} {result[1]}")
# Ada Lovelace


def rearrange_name(pattern, name):
    result = re.search(pattern, name)
    if result is None:
        return name
    return f"{result[2]} {result[1]}"


pattern = r"^(\w*), (\w*)$"

print(rearrange_name(pattern, "Lovelace, Ada"))
# Ada Lovelace
print(rearrange_name(pattern, "Ritchie, Dennis"))
# Dennis Ritchie
print(rearrange_name(pattern, "Ritchie, Dennis Jr."))
# Ritchie, Dennis Jr.
print()

# With this new pattern we can capture the Middlenames, titles and punctuations.
new_pattern = r"^([\w \.-]*), ([\w \.-]*)$"

print(rearrange_name(new_pattern, "Ritchie, Dennis Jr."))
# Dennis Jr. Ritchie
print(rearrange_name(new_pattern, "Hopper, Grace M."))
# Grace M. Hopper
print()


# More on Repetition Qualifiers


# Let's match any string of 5 letters:
print(re.search(r"[a-zA-Z]{5}", "a ghost"))
# <re.Match object; span=(2, 7), match='ghost'>

# With search will return only the first match
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# <re.Match object; span=(2, 7), match='scary'>

# With find all will return all of 5 or more letters.
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# ['scary', 'ghost', 'appea']

# To find only the words that are exactly 5 letters long we use \b to set boundaries
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))
# ['scary', 'ghost']

# Let's find words from 5 to 10 letters
print(re.findall(r"\b\w{5,10}\b", "I really like strawberries"))
# ['really']

# Let's find words of 5 or more letters
print(re.findall(r"\b\w{5,}\b", "I really like strawberries"))
# ['really', 'strawberries']

# Let's find words starting with "s" and that have up to 20 characters (including 0)
print(re.search(r"s\w{,20}", "I really like strawberries"))
['I', '', '', '', 'like', '', '', '']
# <re.Match object; span=(14, 26), match='strawberries'>
print()


# This function returns all words that are at least 7 characters.
def long_words(text):
    pattern = r"\w{7,}"
    result = re.findall(pattern, text)
    return result


print(long_words("I like to drink coffee in the morning."))
# ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon."))
# ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night."))
# []
print()


# Stracting a PID Using regexes in Python


log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
# 12345


def extract_pid(pattern, log_line):
    resultado = re.search(pattern, log_line)
    if resultado is None:
        return ""
    return resultado[1]


def extract_pid_groups(pattern, log_line):
    # we use the re.compile to indicate to python that the pattern is not a simple string but a regex expression
    pattern = re.compile(pattern)
    resultado = re.search(pattern, log_line)
    if resultado is None:
        return ""
    return f"{resultado[1] ({resultado[2]})}"


def extract_pid_groups2(regex, log_line):
    # In this case we don't use the re.compile so we access to the groups using .group()
    result = re.search(regex, log_line)
    if result is None:
        return None
    return f"{result.group(1)} ({result.group(2)})"


print(extract_pid(regex, "this is a test [661222]"))
# 661222
print(extract_pid(regex, "321 this is another [test]"))
#

new_regex = r"\[(\d+)\]: ([A-Z]*)"

print(extract_pid_groups2(new_regex,
      "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))
# 12345 (ERROR)
print(extract_pid_groups2(new_regex, "99 elephants in a [cage]"))
# None
print(extract_pid_groups2(
    new_regex, "A string that also has numbers [34567] but no uppercase message"))
# None
print(extract_pid_groups2(new_regex,
      "July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))
# 67890 (RUNNING)
print()


# Splitting and Replacing


print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))
# ['One sentence', ' Another one', ' And the last one', '']

print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))
# ['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']

print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]",
      "Received an email from go_nuts95@my.example.com"))
# Received an email from [REDACTED]

print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))
# Ada Lovelace

# This regular expression uses "the" and "a" as delimiters,
# no matter where they are in the text, even in the middle of other
# words like "Another" and "last".
print(re.split(r"the|a", "One sentence. Another one? And the last one!"))
['One sentence. Ano', 'r one? And ', ' l', 'st one!']
