computer = input(('Hi! Welcome Quiz Game. Are you ready ? '))
if computer != 'yes':
    quit()
questions = [
    'Where is the capital of Azerbaijan? ',
    'Where is the capital of England? ',
    'Where is the capital of USA? ',
    'Where is the capital of Russia? ',
    'Where is the capital of Germany? ',
    'Where is the capital of Spain? ',
]
answers = [
    'baku',
    'london',
    'washington',
    'moscow',
    'berlin',
    'madrid'
]
score = 0
for i in range(len(questions)):
    x = input(questions[i])
    if x.lower() == answers[i]:
        print('Correct!')
        score +=1 
    else:
        print('Sorry! You are failed')
        score-=1
print(f'Game over! your score is {score} ')
    