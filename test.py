class PasswordChecker():
    def check_strength(self, password):
        strength = 0
        if(len(password)<6):
            strength += 1
        elif(len(password)<10):
            strength += 2
        else:
            strength += 3
        has_number = False
        
        for c in password:
            if(c.isdigit()):
                has_number = True
        if(has_number == True):
            strength +=1
        common_passwords = ["Password", "qwerty", "1234567890", "111111", "12345678", "1q2w3e", "qwerty123", "password", "123456789", "123456", "12345"]
        if password in common_passwords:
            strength = 0
        match strength:
            case 1:
                return("Very Weak")
            case 2:
                return("Weak")
            case 3:
                return("Moderate")
            case 4:
                return("Strong")
def Main():
    history = []
    while True:
        if(len(history) > 0):
           print(history)
                
        user_input = input("Enter Password\t")
        checker = PasswordChecker()
        print(checker.check_strength(user_input))
        history.append(user_input)
Main()