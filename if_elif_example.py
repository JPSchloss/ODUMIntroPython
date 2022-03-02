Score_A = 90
Score_B = 80
Score_C = 70
Score_D = 60

def main():
    score = int(input('Enter your test score: '))

    if score >= Score_A:
        print('Congrats! You got an A!')
    elif score >= Score_B:
        print('Good Job! You got a B!')
    elif score >= Score_C:
        print('Better Luck Next Time. You got a C.')
    elif score >= Score_D:
        print('Tough luck. You got a D.')
    else:
        print('Your grade is an F.')

main()
