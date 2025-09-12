ans = ['rises', 'go', 'sang', 'drinks', 'went', 'I drink coffee in the morning.', 'freind', 'short']
ban = ['administrator', 'superuser', 'pussy']
Invalid = ('\033[31mOops! Invalid input! Try again.\033[0m ')
user_score = ('Nice! Total score: ')
lvl2_user_score = ('Awesome! Total score: ')
user_name = input('What is your name: ')
if user_name in ban:
    print('\033[31mInvalid Username!\033[0m')
    exit()
elif user_name not in ban:
    print(f'Hello \033[1;32m{user_name}!\033[0m ')
wanna_play = input('Do you wanna play a game? (YES / NO) ').upper()
if wanna_play == 'YES':
    print(f'Okay let\'s start!')
    ready_check = input('Are you ready? (YES / NO) ').upper()
    if ready_check == 'YES':
        print(f'Fill in the blank.')
        question1 = input('The sun ___ in the east.\na) rise\nb) rises\nc) rising\n').lower()
        if question1 in ans:
            print(f'\033[34m{user_score}1\033[0m')
            question2 = input('Fill in the blank.\nI ___ to school every morning.\na) goes\nb) going\nc) go\n').lower()
            if question2 in ans:
                print(f'\033[34m{user_score}2\033[0m')
                question3 = input('Fill in the blank.\nShe ___ a beautiful song yesterday.\na) sings\nb) sang\nc) singing\n').lower()
                if question3 in ans:
                    print(f'\033[34m{user_score}3\033[0m')
                    question4 = input('Fill in the blank.\nMy father ___ coffee every day.\na) drink\nb) drinks\nc) drinking\n').lower()
                    if question4 in ans:
                        print(f'\033[34m{user_score}4\033[0m')
                        question5 = input('Fill in the blank.\nWe ___ to the park last Sunday.\na) go\nb) went\nc) goes\n').lower()
                        if question5 in ans:
                            print(f'\033[34mLevel 2 unlocked! Your English skills are leveling up fast!\033[0m')
                            level2 = input('Ready for new challenges? (LET\'S ROLL / MAYBE LATER) ').upper()
                            if level2 == 'LET\'S ROLL':
                                print('Arrange the words to make a sentence: ')
                                lvl2q1 = input ('\"morning / I / coffee / drink / .\"\na) I drink coffee morning\nb) I drink coffee in the morning\nc) Coffee I drink morning\n')
                                if lvl2q1 in ans:
                                    print(f'\033[34m{lvl2_user_score}1\033[0m')
                                    lvl2q2 = input('One word is spelled incorrectly. Spot it.\nfreind, school, book\n').lower()
                                    if lvl2q2 in ans:
                                        print(f'\033[34m{lvl2_user_score}2\033[0m')
                                        lvl2q3 = input('Give the opposite word.\ntall → ?\n').lower()
                                        if lvl2q3 in ans:
                                            print(f'\033[34m{lvl2_user_score}3\033[0m')
                                            lvl2q4 = input('Find the synonym for the given word.\nHappy → (a) sad (b) glad (c) angry\n ').lower()
                                        elif lvl2q3 not in ans:
                                            print(f'Oops! The correct answer is\033[1;32mshort\033[0m')
                                        else:
                                            print(Invalid)
                                    elif lvl2q2 not in ans:
                                        print(f'Oops! The correct answer is\033[1;32mfreind\033[0m')
                                    else:
                                        print(Invalid)
                                elif lvl2q1 not in ans:
                                    print(f'Oops! The correct answer is\033[1;32mI drink coffee in the morning\033[0m')
                                else:
                                    print(Invalid)
                            elif level2 == 'MAYBE LATER':
                                print('Aight! Maybe next time!')
                            else:
                                print(Invalid)
                        elif question5 not in ans:
                            print(f'Oops! The correct answer is b) \033[1;32went\033[0m')
                        else:
                            print(Invalid)
                    elif question4 not in ans:
                        print(f'Oops! The correct answer is b) \033[1;32drinks\033[0m')
                    else:
                        print(Invalid)
                elif question3 not in ans:
                    print(f'Oops! The correct answer is b) \033[1;32sang\033[0m')
                else:
                    print(Invalid)
            elif question2 not in ans:
                print(f'Oops! The correct answer is c) \033[1;32mgo\033[0m')
            else:
                print(Invalid)
        elif question1 not in ans:
            print('Oops! The correct answer is b) \033[1;32mrises\033[0m ')
        else:
            print(Invalid)
    elif ready_check == 'NO':
        print(f'Okay! Come Back When You Are Ready!!')
    else:
        print(Invalid)
elif wanna_play == 'NO':
    print('Okay Next Time!')
else:
    print(Invalid)

input("Press Enter to exit...")