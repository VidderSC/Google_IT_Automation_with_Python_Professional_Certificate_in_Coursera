import re


# 1
def transform_record(record):
    new_record = re.sub(r"(\w )*,([\d-]*),(\w )*", r"\1,+1-\2,\3", record)
    return new_record


print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist"))
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# Charlie Rivera,+1-698-746-3357,Web Developer

print()


# 2
def multi_vowel_words(text):
    pattern = r"\b\w*[aeiouAEIOU]{3,}\w*\b"
    result = re.findall(pattern, text)
    return result


print(multi_vowel_words("Life is beautiful"))
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words(
    "The rambunctious children had to sit quietly and await their delicious dinner."))
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))
# ['queue']

print(multi_vowel_words("Hello world!"))
# []


# 4
# Replace the comment in Python "#" to a comment in C++ "//"
# independently of how many # there are, it will be treated as one.
def transform_comments(line_of_code):
    result = re.sub(r"(\#)+", "//", line_of_code)
    return result


print(transform_comments("### Start of program"))
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable"))
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable"))
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)"))
# Should be "  return(number)"

print()

# 5
# Checks for an US phone number with format:
# xxx-xxx-xxxx (3 digits - 3 digits - 4 digits) and
# converts it to (xxx) xxx-xxxx.


def convert_phone_number(phone):
    result = re.sub(r"\b(\d{3})-(\d{3})-(\d{4})\b", r"(\1) \2-\3", phone)
    return result


print(convert_phone_number("My number is 212-345-9999."))
# My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234"))
# Please call (888) 555-1234
print(convert_phone_number("123-123-12345"))
# 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300"))
# Phone number of Buckingham Palace is +44 303 123 7300
