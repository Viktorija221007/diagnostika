#Viktorija Štelmahere 18.10.24

Passwords = []

while True:
    Password = input("Enter the correct password: ")                 #ievada paroli
    if Password.lower() == 'python123':                              #ja ievada pareizi...
        Passwords.append(Password)
        break                                                        #beidzas cikls
    elif Password.lower() != 'python123':                            #ja ievada nepareizi-
         print("Piekļuve liegta, ievadiet vēlreiz: ")                #-tad izvada šo
print("Piekļuve atļauta!")                                           #...tad šo izvada