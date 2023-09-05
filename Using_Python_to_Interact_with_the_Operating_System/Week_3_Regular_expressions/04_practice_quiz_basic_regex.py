# Practice Quiz: Basic Regular Expressions

import re


def check_web_address(text):
    pattern = r"^[a-zA-Z0-9_.\-+]*[.a-zA-Z{2,3}]$"
    result = re.search(pattern, text)
    return result != None


print(check_web_address("gmail.com"))  # True
print(check_web_address("www@google"))  # False
print(check_web_address("www.Coursera.org"))  # True
print(check_web_address("web-address.com/homepage"))  # False
print(check_web_address("My_Favorite-Blog.US"))  # True

print()


def check_time(text):
    pattern = r"^[1-9]{1}[0-2]?:[0-5]{1}[0-9]{1}\s?am$|AM$|pm$|PM$"
    result = re.search(pattern, text)
    return result != None


print(check_time("12:45pm"))  # True
print(check_time("9:59 AM"))  # True
print(check_time("6:60am"))  # False
print(check_time("five o'clock"))  # False

print()


def contains_acronym(text):
    pattern = r"\({1}[0-9]?[A-Z]?[a-zA-Z]*\){1}"
    result = re.search(pattern, text)
    return result != None


print(contains_acronym(
    "Instant messaging (IM) is a set of communication technologies\
    used for text-based communication"))  # True
print(contains_acronym("American Standard Code for Information Interchange\
    (ASCII) is a character encoding standard for electronic communication"))  # True
print(contains_acronym("Please do NOT enter without permission!"))  # False
print(contains_acronym(
    "PostScript is a fourth-generation programming language (4GL)"))  # True
print(contains_acronym(
    "Have fun using a self-contained underwater breathing apparatus (Scuba)!"))  # True

print()

"""
Fill in the code to check if the text passed includes a possible U.S. zip code, formatted as follow:
exactly 5 digits, and sometimes, but not always, followed by a dash with 4 more digits.
The zip code needs to be preceded by at least one space, and cannot be at the start of the text.
"""


def check_zip_code(text):
    result = re.search(r" {1}\d{5}(-\d{4})?", text)
    return result != None


print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code(
    "The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False
