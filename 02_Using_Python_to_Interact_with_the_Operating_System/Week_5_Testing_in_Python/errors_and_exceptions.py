#!/usr/bin/env python3

"""
Try-Except Construct, Raise error and Assert.

- Try-Except: If we don't want our code to stop after encountering an error,
we can use the try-except construct to check for an error.
What this does is first try to do the operation that we want which in this
case is to open the file.
If there's an error, it then goes into the except part of the block that
matches the error and does whatever cleanup is necessary.

- Raise: We can raise a bunch of different errors that come already pre-built
with Python or we can create our own, if the standard ones aren't good enough.

- Assert: This keyword tries to verify that a conditional expression is true,
and if it's false it raises an assertion error with the indicated message.

We usually don't need to check the types of our parameters (Assert). 
Depending on what our function does, it might be perfectly okay for
it to allow scripts to call it with parameters of different types.
Assertions can be super helpful for debugging some code that's not
behaving the way we expect it to. We can add them at any point where
we want to ensure that the variables contain the values and types that
they should or when we think that's something that shouldn't happen
is happening.

Heads up though.

Assertions will get removed from our code if we ask the interpreter
to optimize it to run faster.
So as a rule, we should use raise to check for conditions that we
expect to happen during normal execution of our code and assert to
verify situations that aren't expected but that might cause our code
to misbehave. 
"""


def character_frequency(filename):
    """Counts the frequency of each character in the given file."""
    # First try to open the file
    try:
        f = open(filename)
    except OSError:
        return None

    # Now process the file
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close
    return characters


def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"

    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    if len(username) < minlen:
        return False

    if not username.isalnum():
        return False

    return True
