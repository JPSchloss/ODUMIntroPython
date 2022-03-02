def main():
    count = 0
    string = input('Please enter a string here: ')
    character = input('Please enter the character to count: ')

    for char in string:
        if char == character:
            count += 1

    print('The count of', character, 'appears', count, 'times.')

main()

# Try using str.lower() to make this program more robust.
# Example: string = str.lower(string)

# What is happening here and why does this matter?