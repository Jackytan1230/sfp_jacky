# Create a function called check_string that takes one string argument
# Return "Found it!" if it starts with "The", otherwise return "Nope."

def check_string(text):
    if text.startswith("The"):
        return "Found it!"
    else:
        return "Nope."

# Test cases
str1 = 'The'
str2 = 'Thumbs up'
str3 = 'Theatre can be boring'

print(check_string(str1))    # ➜ Found it!
print(check_string(str2))    # ➜ Nope.
print(check_string(str3))    # ➜ Found it!
