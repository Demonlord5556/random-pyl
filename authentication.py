# Initial Database and Security Questions list[cite: 5]
d = {'username': ['something@some.com', 'Qwerty@123', 'ques1', 'ans1', 'ques2', 'ans2']}

seq = ['Your Favorite Color?',
       'Your Favorite Place?',
       'Your Favorite Fruit?',
       'Your First Institution Name?',
       'Your First Pet Name?']

def checkPasswordStrength(passw):
    ac = dc = uc = lc = sc = 0
    strength = 0
    specChar = '!@#$%^&*()-_=+<>'
    for char in passw:
        if char.isalpha():
            ac = 1
            if char.islower(): lc = 1
            else             : uc = 1
        elif char.isdigit() : dc = 1
        elif char in specChar: sc = 1
    if len(passw) >= 8 and ac and dc and uc and lc and sc:
        return passw
    else:
        print('Password is weak...Please try again...')
        passw = input('Enter a new strong password: ')
        return checkPasswordStrength(passw) 
def securityQuestion():
    from random import choice
    temp = list(range(0, 5)) 
    index1 = choice(temp)     
    temp.pop(index1)          
    index2 = choice(temp)
    ques1 = seq[index1]
    ques2 = seq[index2]
    a = 'n'
    while a == 'n':
        ans1 = input(f'{ques1} ')
        ans2 = input(f'{ques2} ')
        a = input('Do you want to save the answers ? y/n: ').lower()
    return ques1, ans1, ques2, ans2 
def dbUpdate(username, email, password, ques1, ans1, ques2, ans2):
    d.update({username: [email, password, ques1, ans1, ques2, ans2]})
    return #[cite: 4, 5]
def verifyEmail(email):
    import random as r
    n = 4
    otp = ''
    for i in range(n):
        dig = r.randint(0,9)
        sdig = str(dig)
        otp = otp + sdig
    
    
    print(f"\n--- SYSTEM MESSAGE: An OTP ({otp}) was sent to {email} ---")
    
    
    user_otp = input("Enter the 4-digit OTP to verify your email: ")
    
    
    if user_otp == otp:
        print("Email verified successfully!")
        return True
    else:
        print("Invalid OTP. Email verification failed.")
        return False
def signUp():
    username = input('Enter a new username: ').lower()
    if username not in d:
        email = input('Enter your email address: ').lower()
        if not verifyEmail(email):
            print('Email verification failed. Please try again.')
            return signUp()
        password = input('Enter password: ')
        password = checkPasswordStrength(password)
        ques1, ans1, ques2, ans2 = securityQuestion()
        dbUpdate(username, email, password, ques1, ans1, ques2, ans2)
        print('Sign Up Successful')
        return
    else:
        print('Username already exists... Please try again...')
        return signUp() #[cite: 6]

def signIn():
    username = input('Enter your username: ').lower()
    if username in d:
        actualPassw = d[username][1]
        for i in range(3):
            passw = input('Enter password: ')
            if passw == actualPassw:
                print('SignIn Successful')
                return
            else:
                print(f'Wrong password. Try again. {2-i} tries left ')
        print('SignIn Unsuccessful')
        # accountLock()
        return
    else:
        b = input('''
Username doesnt exist in the database.
Press 1 to to SignUp
Press 2 to try again...
''')
        if b == '1': return signUp()
        elif b == '2': return signIn()
        else         : print('Invalid input...')
def forgotPassword():
    username = input('Enter your username: ').lower()
    if username in d:
        print('\n--- Security Question Verification ---')
        saved_ques1 = d[username][2]
        saved_ans1 = d[username][3]
        saved_ques2 = d[username][4]
        saved_ans2 = d[username][5]
        
        ans1 = input(f'{saved_ques1} ')
        ans2 = input(f'{saved_ques2} ')
        
        if ans1 == saved_ans1 and ans2 == saved_ans2:
            print('Verification Successful!')
            new_passw = input('Enter new password: ')
            new_passw = checkPasswordStrength(new_passw)
            d[username][1] = new_passw 
            print('Password Reset Successful!')
        else:
            print('Verification failed. Incorrect answers.')
    else:
        print('Username does not exist in the database.')
def driver():
    while True:
        mode = input('''
        Press 1 for SignUp
        Press 2 for SignIn
        Press 3 for Forgot Password
        Press 0 to Exit
        : ''')
        if mode == '1':
            signUp()
        elif mode == '2':
            signIn()
        elif mode == '3':
            forgotPassword()
        elif mode == '0':
            print('Thank you')
            return
        else:
            print('Invalid input')

driver()