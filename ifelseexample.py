def main():
    password = input('Enter a password: ')
    check_password(password)

def check_password(password):
    if password == 'Password':
        print('Password accepted.')
    else:
        print('That is the wrong password.')

main()