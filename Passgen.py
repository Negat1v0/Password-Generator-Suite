#PasswordGen Suite 2.0 
#Developed by SG

import random
char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!$%&/()=?^[]#@'
char_1 = 'abcdefghijklmnopqrstuvwxyz0123456789'
char_2 = 'ABCDEFGHIJKLMNOPQRSTUXYWZabcdefghijklmnopqrstuvwxyz0123456789'
char_3 = 'ABCDEFGHIJKLMNOPQRSTUXYWZabcdefghijklmnopqrstuvwxyz0123456789!£$%&/()=?^*+°#ç@;:_-<>'
char_4 = 'ABCDEFGHIJKLMNOPQRSTUXYWZabcdefghijklmnopqrstuvwxyz0123456789!£$%&/()=?^*+°#ç@;:_-<>èéòàùì'
char_5 = 'ABCDEFGHIJKLMNOPQRSTUXYWZabcdefghijklmnopqrstuvwxyz0123456789!£$%&/()=?^*+°#ç@;:_-<>èéòàùìdʒʒðθtʃu:aƒ¤﷼￥₵₴₳₲₱₰₯₭₫₠₡₢₣₤₥₦₧₨₩₪៛฿௹৳৲₮¥£€$¢ɪaʊeɪoʊɔɪeəɪəʊəŋʃʊɔ:ɒi:ɜ:ɪəeæɑ:ʌ⋈⋉⋊⋋⋌⋍⋎⋃⋂⋁⊿⋀⊾⊽⊼⊻⊺⊹⋏⋐⋑⋒⋓⋔⋘⋙⋬⋪⊨⊧⊪⊫⊭⊬⊡⊟⊞⊠⊜⊛⊙⊏⊐⊑⊒⊇≺≹≸⊂≥≦≧≨≜≛∀∛∜∍∌∔∉∈∰'

response = 'y'

def passgen():
    response_1 = 'y'

    print('Welcome to PasswordGen Suite 2.0!')
    print('')
    print('''Please, choose the mode you want:
    1. Basic: choose the password security level you want
    2. Advanced: choose the lenght and the characters you want to utilize for you password
    3. Easy to remember: generate the password from a word
    
    Press "e" to exit''')
    print('')
    
    
    
    while True:
        choose = input('Your response is: ')
        
        if choose == 'e':
            print('Goodbye!')
            break
            exit()

        if choose == '1':
            def passgen_1():
                print('Please, choose the security level you want: ')
                print('')
                print('''1. Very weak: a password of 6 characters with only lowercase letters and numbers
        2. Weak: a password of 6 characters with uppercase letters, lowercase letters and numbers
        3. Medium: a password of 8 characters with uppercase, lowercase, numbers and symbols
        4. Strong: a password of 12 characters with uppercase, lowercase, numbers, symbols and accents
        5. Incredible: a password of 24 characters with uppercase, lowercase, numbers, symbols, accents and some non-conventional characters''')
                print('')
                while True:
                    level_choose = input("What's your choice?: " )
                    if level_choose == '1':
                        try:
                            while True:
                                pass_count = int(input('How many passwords would you like: '))
                                for i in range(0,  pass_count):
                                    password = ''
                                    for i in range(0, 6):
                                        password_char = random.choice(char_1)
                                        password = password + password_char
                                    print('Here is your password: ', password)
                                break
                            break
                        except ValueError:
                            print ('Please insert an integer value')
                            continue
                            
                    if level_choose == '2':
                        try:
                            while True:
                                pass_count = int(input('How many passwords would you like: '))
                                for i in range(0,  pass_count):
                                    password = ''
                                    for i in range(0, 6):
                                        password_char = random.choice(char_2)
                                        password = password + password_char
                                    print('Here is your password: ', password)
                                break
                            break
                        except ValueError:
                            print ('Please insert an integer value')
                            continue                            
                            
                    if level_choose == '3':
                        try:
                            while True:
                                pass_count = int(input('How many passwords would you like: '))
                                for i in range(0,  pass_count):
                                    password = ''
                                    for i in range(0, 8):
                                        password_char = random.choice(char_3)
                                        password = password + password_char
                                    print('Here is your password: ', password)
                                break    
                            break    
                        except ValueError:
                            print ('Please insert an integer value')
                            continue                            
                            
                            
                    if level_choose == '4':
                        try:
                            while True:
                                pass_count = int(input('How many passwords would you like: '))
                                for i in range(0,  pass_count):
                                    password = ''
                                    for i in range(0, 12):
                                        password_char = random.choice(char_4)
                                        password = password + password_char
                                    print('Here is your password: ', password)
                                break    
                            break    
                        except ValueError:
                            print ('Please insert an integer value')
                            continue                            
                            
                    if level_choose == '5':
                        try:
                            while True:
                                pass_count = int(input('How many passwords would you like: '))
                                for i in range(0,  pass_count):
                                    password = ''
                                    for i in range(0, 24):
                                        password_char = random.choice(char_5)
                                        password = password + password_char
                                    print('Here is your password: ', password)
                                break    
                            break    
                        except ValueError:
                            print ('Please insert an integer value')
                            continue                            
                    
        
                            
                        break
                    else:
                        continue
                    

            while response_1 == 'y':
                passgen_1()
                response_1 = input('Whould you like to repeat the process (y/n): ').lower()
            if response_1 == 'n' or 'N':
                passgen()
                
        if choose == '2':
            def passgen_2():
                
                uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'
                lowercase_letters = uppercase_letters.lower()
                digits = '0123456789'
                symbols = '!£$%&/()=?^*+°#ç@;:_-<>'
                accents = 'èéòàùì'
                special = 'dʒʒðθtʃu:aƒ¤﷼￥₵₴₳₲₱₰₯₭₫₠₡₢₣₤₥₦₧₨₩₪៛฿௹৳৲₮¥£€$¢ɪaʊeɪoʊɔɪeəɪəʊəŋʃʊɔ:ɒi:ɜ:ɪəeæɑ:ʌ⋈⋉⋊⋋⋌⋍⋎⋃⋂⋁⊿⋀⊾⊽⊼⊻⊺⊹⋏⋐⋑⋒⋓⋔⋘⋙⋬⋪⊨⊧⊪⊫⊭⊬⊡⊟⊞⊠⊜⊛⊙⊏⊐⊑⊒⊇≺≹≸⊂≥≦≧≨≜≛∀∛∜∍∌∔∉∈∰'
                
                all_1 = ''
                
                while True:
                    try:
                        lenght_2 = int(input('Please, choose the lenght of your password: '))
                        break
                    except ValueError:
                        print ('Please insert an integer value')
                        continue
                
                all_1 += uppercase_letters
                
                while True:
                    quest_1 = input('Would you like lowercase letters in you password? (y/n): ')
                    if quest_1 == 'y':
                        quest_1 = True
                        all_1 += lowercase_letters
                        break
                    if quest_1 == 'n':
                        quest_1 = False
                        break
                    else:
                        continue            
                
                
                while True:
                    quest_2 = input('Would you like numbers in your password? (y/n): ')
                    if quest_2 == 'y':
                        quest_2 = True
                        all_1 += digits
                        break
                    if quest_2 == 'n':
                        quest_2 = False
                        break
                    else:
                        continue             
                

                while True:
                    quest_3 = input('Would you like symbols in your password? (y/n): ')
                    if quest_3 == 'y':
                        quest_3 = True
                        all_1 += symbols
                        break
                    if quest_3 == 'n':
                        quest_3 = False
                        break
                    else:
                        continue 


                while True:
                    quest_4 = input('Would you like accents in you password? (y/n)?: ')
                    if quest_4 == 'y':
                        quest_4 = True
                        all_1 += accents
                        break
                    if quest_4 == 'n':
                        quest_4 = False
                        break
                    else:
                        continue 


                while True:
                    quest_5 = input('Would you like special carachters in you password? (y/n)?: ')
                    if quest_5 == 'y':
                        quest_5 = True
                        all_1 += special
                        break
                    if quest_5 == 'n':
                        quest_5 = False
                        break
                    else:
                        continue

                
                
                while True:
                    try:
                        pass_count_2 = int(input('How many passwords would you like: '))
                        break
                    except ValueError:
                        print ('Please insert an integer value')
                        continue
                
                            
                
                for x in range(pass_count_2):
                    new_password_1 = ''.join(random.sample(all_1, lenght_2))
                    print(new_password_1)
            
            
            while response_1 == 'y':
                passgen_2()
                response_1 = input('Whould you like to repeat the process (y/n): ').lower()
            if response_1 == 'n' or 'N':
                passgen()    

            passgen_2()
            
            
                    
        if choose == '3':
            def passgen_3():
                new_password_3 = ''
                pass_list = input('Enter a word easy to remember: ')
                for i in pass_list:
                    if i in 'aA':
                        new_password_3 += '@'
                    elif i in 'sS':
                        new_password_3 += '$'
                    elif i == 'oO':
                        new_password_3 += '0'
                    elif i == 'cC':
                        new_password_3 += '('
                    elif i == 'iI':
                        new_password_3 += '!'
                    elif i == 'lL':
                        new_password_3 += '['
                    elif i == 'eE':
                        new_password_3 += '£'
                    else:
                        new_password_3 += i
                        
                print(new_password_3)
                
            while response_1 == 'y':
                passgen_3()
                response_1 = input('Whould you like to repeat the process (y/n): ').lower()
            if response_1 == 'n' or 'N':
                passgen()
                
            passgen_3()    
            


            break
        else:
            continue

passgen()
