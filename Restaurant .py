def hello():
    print(f'''Hi ,{name}.This Is our Menu ''')

    print('''          Starters    

    ->Cheese Bread Roll.                        ₹80
    ->Cheese Maggi Bread Roll                   ₹100
    ->Batata Kees (Spicy Grated Potato)         ₹50
    ->Bread Pizza                               ₹100

                        Meals

    ->Stuffed sweet potatoes                    ₹200
    ->Grain bowls                               ₹220
    ->Whole roasted chicken                     ₹330
    ->Sheet pan meals                           ₹190

                        Snacks

    ->Aloo Samosa(4 pices)                      ₹50
    ->Masala Sandwich(2 pices)                  ₹20
    ->Kachori                                   ₹12
    ->Pizza Puff's(7 pices)                     ₹47

                       Deserts

    ->Mango Cats                                ₹30
    ->Vannila  Slime                            ₹50
    ->Silence cherry                            ₹20
    ->Chacolate Hugs                            ₹90

    For Order Please copy your Desired Food and keep it in
    (Note:Only one order can be placed at a time.)

               ''')


def good(): print(f'Thank you {name} , have a nice day and bot 0112 will be alway be in your service :)')


def bad(): print(
    f'oo,sorry for this I will try my best next time :( {name}, have a nice day and bot 0112 will be alway be in your service :)')


def helpA():
    help_req = input('Do you want to chosee and item ')
    if (help_req == 'yes') or (help_req == 'Yes') or (help_req == 'YES') or (help_req == 's') or (help_req == 'y'):
        print('Wait page is loading')
        helpB()
    else:
        print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')


def helpB():
    need = input(f'What type of food do you wanna have  {name}')

    if need == 'Starters':
        Starter = input('What do  you want to have?? ')
        if Starter == 'Cheese Bread Roll':
            print(f'OK,It will take 5 minutes and bill is ₹80 {name}')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y') :
                print('So,here is your Cheese Bread Roll Please have it ')
                Anything= input('Do you want to ahve anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y') :
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y') :
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        elif Starter == 'Cheese Maggi Bread Roll':
            print('OK,it take 5 minutes will  cost ₹100')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Cheese Maggi Bread Roll  Please have it ')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(
                        f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        elif Starter == 'Batata Kees (Spicy Grated Potato)':
            print('OK,it take 5 minutes will  cost ₹50')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Batata Kees (Spicy Grated Potato) Please have it ')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(
                        f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(
                        f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        elif Starter == 'Bread Pizza':
            print('OK,it take 5 minutes will  cost ₹100')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Ice cream Please have it ')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(
                        f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(
                        f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

    elif need == 'Meals':
        Meals = input('What  do you want to have?? ')
        if Meals == 'Stuffed sweet potatoes':
            print(f'OK,It will take few minutes and bill is ₹200 {name}')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Stuffed sweet potatoes Please have it ')
                Anything = input('Do you want to ahve anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(
                        f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        elif Meals == 'Grain bowls':
            print('OK,it take 10 - 15 minutes will  cost ₹220')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Grain bowls  Please have it ')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        elif Meals == 'Whole roasted chicken':
            print('OK,it take 30 minutes will  cost ₹330')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Whole roasted chicken Please have it ')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print( f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        elif Meals == 'Sheet pan meals':
            print('OK,it take 5 minutes will  cost ₹190')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Sheet pan meals Please have it ')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

    elif need == 'Snacks':
        Snacks = input('What do you want to have?? ')
        if Snacks == 'Aloo Samosa(4 pices)':
            print(f'OK,It will take 2 minutes and bill is ₹50 {name}')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Aloo Samosa Please have it ')
                Anything = input('Do you want to ahve anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        elif Snacks == 'Masala Sandwich(2 pices)':
            print('OK,it take 3 minutes will  cost ₹20')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Masala Sandwich Please have it ')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        elif Snacks == 'Kachori':
            print('OK,it take 1 minutes will  cost ₹12')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Kachori Please have it ')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        else:
            print('OK,it take 5 minutes will  cost ₹47')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print("So,here is your Pizza Puff's Please have it ")
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

    else:
        Deserts = input('What  do you want to have?? ')
        if Deserts == 'Mango Cats':
            print(f'OK,It will take 5 minutes and bill is ₹30 {name}')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Mango Cats Please have it ')
                Anything = input('Do you want to ahve anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                                                                                                                                helpA()
                else:
                    print(
                        f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(
                        f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        elif Deserts == 'Vannila  Slime':
            print(f'OK,It will take 5 minutes and bill is ₹50 {name}')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Vannila  Slime Please have it ')
                Anything = input('Do you want to ahve anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        if Deserts == 'Silence cherry':
            print(f'OK,It will take 5 minutes and bill is ₹20 {name}')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Silence cherry Please have it ')
                Anything = input('Do you want to ahve anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        else:
            print(f'OK,It will take 5 minutes and bill is ₹90 {name}')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Chacolate Hugs Please have it ')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')


print("Welcome to Our Hotel ")
name = input('what is your name ')
hello()

need = helpA()

need = input(f'What type of food do you wanna have  {name}')

if need == 'Starters':
        Starter = input('What do  you want to have?? ')
        if Starter == 'Cheese Bread Roll':
            print(f'OK,It will take 5 minutes and bill is ₹80 {name}')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y') :
                print('So,here is your Cheese Bread Roll Please have it ')
                Anything= input('Do you want to ahve anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y') :
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y') :
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        elif Starter == 'Cheese Maggi Bread Roll ':
            print('OK,it take 5 minutes will  cost ₹100')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Cheese Maggi Bread Roll  Please have it ')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(
                        f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        elif Starter == 'Batata Kees (Spicy Grated Potato) ':
            print('OK,it take 5 minutes will  cost ₹50')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Batata Kees (Spicy Grated Potato) Please have it ')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(
                        f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(
                        f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        elif Starter == 'Bread Pizza ':
            print('OK,it take 5 minutes will  cost ₹100')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Ice cream Please have it ')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(
                        f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(
                        f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

elif need == 'Meals':
        Meals = input('What  do you want to have?? ')
        if Meals == 'Stuffed sweet potatoes':
            print(f'OK,It will take few minutes and bill is ₹200 {name}')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Stuffed sweet potatoes Please have it ')
                Anything = input('Do you want to ahve anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(
                        f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        elif Meals == 'Grain bowls ':
            print('OK,it take 10 - 15 minutes will  cost ₹220')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Grain bowls  Please have it ')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        elif Meals == 'Whole roasted chicken ':
            print('OK,it take 30 minutes will  cost ₹330')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Whole roasted chicken Please have it ')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print( f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        elif Meals == 'Sheet pan meals ':
            print('OK,it take 5 minutes will  cost ₹190')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Sheet pan meals Please have it ')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

elif need == 'Snacks':
        Snacks = input('What do you want to have?? ')
        if Snacks == 'Aloo Samosa(4 pices)':
            print(f'OK,It will take 2 minutes and bill is ₹50 {name}')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Aloo Samosa Please have it ')
                Anything = input('Do you want to ahve anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        elif Snacks == 'Masala Sandwich(2 pices) ':
            print('OK,it take 3 minutes will  cost ₹20')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Masala Sandwich Please have it ')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        elif Snacks == 'Kachori ':
            print('OK,it take 1 minutes will  cost ₹12')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Kachori Please have it ')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        else:
            print('OK,it take 5 minutes will  cost ₹47')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print("So,here is your Pizza Puff's Please have it ")
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

else:
        Deserts = input('What  do you want to have?? ')
        if Deserts == 'Mango Cats':
            print(f'OK,It will take 5 minutes and bill is ₹30 {name}')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Mango Cats Please have it ')
                Anything = input('Do you want to ahve anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(
                        f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(
                        f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        elif Deserts == 'Vannila  Slime':
            print(f'OK,It will take 5 minutes and bill is ₹50 {name}')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Vannila  Slime Please have it ')
                Anything = input('Do you want to ahve anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        if Deserts == 'Silence cherry':
            print(f'OK,It will take 5 minutes and bill is ₹20 {name}')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Silence cherry Please have it ')
                Anything = input('Do you want to ahve anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

        else:
            print(f'OK,It will take 5 minutes and bill is ₹90 {name}')
            choice = input('Do you want to have it ')
            if (choice == 'Yes')  or (choice == 'yes') or (choice == 'YES') or (choice == 's') or (choice == 'y'):
                print('So,here is your Chacolate Hugs Please have it ')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')

            else:
                print('ok')
                Anything = input('Do you want to have anything else ')
                if (Anything == 'Yes') or (Anything == 'yes') or (Anything == 'YES') or (Anything == 's') or (Anything == 'y'):
                    helpA()
                else:
                    print(f'Thank you for coming {name} , have a nice day and bot 0112 will be alway be in your service :)')
