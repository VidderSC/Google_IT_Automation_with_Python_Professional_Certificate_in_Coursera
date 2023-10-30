#!/usr/bin/env python3

def validate_user(username, minlen):
    assert (type(username) == str), "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if username.isalnum():
        return True
    if not username.isalnum():
        return False
    return True
