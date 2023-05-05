def create_strings(string):
    char_count = {}
    first_string = ""
    second_string = ""

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in string:
        if char_count[char] == 1:
            first_string += char
        else:
            second_string += char

    return (first_string, second_string)

string = input("Enter the string:")
first_string, second_string = create_strings(string)
print("First String:", first_string)
print("Second String:", second_string)
