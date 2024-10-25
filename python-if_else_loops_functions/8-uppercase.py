#!/usr/bin/python3
def uppercase(str):
    result = ""  # Initialize an empty string to build the uppercase result
    
    for char in str:  # Loop through each character in the input string
        if 97 <= ord(char) <= 122:  # Check if the character is a lowercase letter
            result += chr(ord(char) - 32)  # Convert to uppercase and add to result
        else:
            result += char  # If not lowercase, just add the character as is
    
    print(result)  # Print the final result

# This part is for testing the function
if __name__ == "__main__":
    uppercase("best")  # Example usage
    uppercase("Best School 98 Battery street")  # Another example
    uppercase("hello, world!")  # Test with punctuation
    uppercase("1234 abc DEF")    # Test with numbers and mixed case
    uppercase("PYTHON")           # Test with all uppercase
    uppercase("")                 # Test with an empty string
    uppercase("     ")            # Test with spaces
    uppercase("@#$%^&*()")        # Test with special characters
