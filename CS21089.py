
def short(a, b):
    with open(a, 'r') as quesfile, open(b, 'r') as ansfile:
        list1 = [ques.strip() for ques in quesfile.readlines()]
        list2 = [ans.strip() for ans in ansfile.readlines()]
    score = 0
    for ques, ans in zip(list1, list2):
        user_ans = input(ques)
        if user_ans.lower() == ans.lower():
            print('correct')
            score += 1
        else:
            print("incorrect")
    print('your score is', score)


def short1(m, n):
    with open(m, 'a+') as quesfile, open(n, 'a+') as ansfile:
        userquestion = input("append your question\n")
        useranswer = input("append your asnwer\n")
        quesfile.write(userquestion)
        ansfile.write(useranswer)
        print("Thank you for your time")

while True:
    ask=input('Do you want to play again YES[Y] NO[N]: ').lower()
    if ask =='y':
        print("\t\t Login")
        name = input('Enter name with @ ned.com\n').lower()
        password = input('Enter password: your password should contain atleast 8 chara\n').lower()
        if '@ned.com' in name and len(password) >= 8:
            print('login successful')
            # intro
            print('\t\tASSALAMUALAIKUM\n\t\tWELCOME,TO QUIZ APPLICATION')
            # first choice
            print('[1]    TAKE QUIZ')
            # second choice
            print('[2]    MANAGE  QUIZZ APPLICATION ')
            # taking input from user
            choice = int(input('=====PRESS 1 OR PRESS 2=====\n'))
            # now going to taking quiz
            if choice == 1:
                # select the category from user
                print('WE ARE GOING TO TAKE QUIZ\nSELECT KNOWLEDGE AREA\n[a] SCIENCE\n[b] GENERAL KNOWLEDGE')
                # selecting knowledge area
                chose = input('=====PRESS a OR PRESS b=====\n').lower()
                # Science category
                if chose == 'a':
                    level = input('select difficulty level\nEASY[E]\nHARD[H]\n').lower()
                    if level == 'e':
                        short('sc_questione.txt', 'sc_answere.txt')
                    elif level == 'h':
                        short('sc_questionh.txt', 'sc_answere.txt')
                    else:
                        print('OPPS!!,YOU CHOSE WRONG ALPHABET\nPLEASE CHOSE E OR H')
                # General knowledge category
                elif chose == 'b':
                    level = input('select difficulty level\nEASY[E]\nHARD[H]\n').lower()
                    if level == 'e':
                        short('gk_questione.txt','gk_answere.txt')
                    if level == 'h':
                        short('gk_questionh.txt', 'gk_answerh.txt')
                    else:
                        print('OPPS!!,YOU CHOSE WRONG ALPHABET\nPLEASE CHOSE E OR H')
                else:
                    print('OPPS!!,YOU CHOSE WRONG ALPHABET\nPLEASE CHOSE a OR b')
                # now going to manage quiz application
            elif choice == 2:
                # select the category from user
                print('YOU ARE IN MANAGE QUIZ AREA\nSELECT KNOWLEDGE AREA\n[a] SCIENCE\n[b] GENERAL KNOWLEDGE')
                chose2 = input('=====PRESS a OR PRESS b====\n').lower()
                # Science category
                if chose2 == 'a':
                    level = input('select difficulty level\nEASY[E]\nHARD[H]\n').lower()
                    if level == 'e':
                        short1('sc_questione.txt','sc_answere.txt')
                    elif level == 'h':
                        short1('sc_questionh.txt','sc_answerh.txt')
                    else:
                        print('OPPS!!,YOU CHOSE WRONG ALPHABET\nPLEASE CHOSE E OR H')
                # General knowledge category
                elif chose2 == 'b':
                    level = input('select difficulty level\nEASY[E]\nHARD[H]\n').lower()
                    if level == 'e':
                        short1('gk_questione.txt','gk_answere.txt')
                    elif level == 'h':
                        short1('gk_questionh.txt','gk_answerh.txt')
                    else:
                        print('OPPS!!,YOU CHOSE WRONG ALPHABET\nPLEASE CHOSE E OR H')
                else:
                    print('OPS!!,YOU CHOSE WRONG ALPHABET\nPLEASE CHOSE a OR b')
            else:
                print('OPS!!,YOU CHOSE WRONG NUMBER\nPLEASE CHOSE 1 OR 2')
        else:
            print('invalid password or username')
    else:
        print('Thank you for your precious ')
        break





