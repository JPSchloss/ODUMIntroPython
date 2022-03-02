def main():
    grocery_items = []
    keep_going = 'y'

    while keep_going == 'y':
        added_item = input('Please enter a grocery item: ')
        grocery_items.append(added_item)
        keep_going = input('Would you like to add another grocer item? (y/n)')

    print(grocery_items)

main()

# Try changing this function to print one item in the list at a time.
# Hint: You may want to use a for loop! 