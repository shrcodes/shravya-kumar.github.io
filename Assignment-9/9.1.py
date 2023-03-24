#Create a program that will play the “cows and bulls” game with the user
def initiation():
    import random
    
    print('Welcome to the Cows and Bulls Game!')
    guess_log = ['']
    answer = random.randint(0,9999)
    answer = '{0:04d}'.format(answer)
    return guess_log, answer

def get_guess(guess_log):
    guess = input('Enter a number:')
    guess_log.append(guess)
    return guess_log

def compare(guess, answer):
    cow = 0
    bull = 0
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            cow += 1
        if guess[i] in answer:
            bull += 1 
    bull = bull - cow
    return cow, bull

def main():
    guess_log, answer = initiation()
    while guess_log[-1] != answer:
        guess_log = get_guess(guess_log)
        cow, bull = compare(guess_log[-1], answer)
        print('{} cows, {} bulls'.format(cow, bull))
    print('Your are right! After {} guess(es) you finally get it!\nYour logs:'.format(len(guess_log)-1), guess_log[1:])

if __name__ == "__main__":
    main()