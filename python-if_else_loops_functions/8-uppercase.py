#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':  # Check if the character is lowercase
            result += chr(ord(char) - 32)  # Convert to uppercase
        else:
            result += char  # Keep the character as is
    print(result)  # Print the result

