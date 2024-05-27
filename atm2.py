# ATM Machine
pw = 1404
balance = 1000
limit = 1
print()
print(' World #1 Bank, "INDIAN BANK" ')
print()
print(' Insert ATM Card ')
print(' Confirm --> 1. Yes  2. No ')
print()
check = int(input(' Enter 1 or 2 --> '))
if check == 1:
    while True:
        print()
        print(' 1. Cash Withdrawal ')
        print(' 2. Check Balance ')
        print(' 3. Exit --> ')
        print()
        choice = int(input(' Payment Method " 1 OR 2 OR 3 " : '))
        print()
        if choice == 1:
            if limit <= 3:
                print(' Cash Withdrawal ')
                print(' ---------------- ')
                amt =int(input(' Enter Amount Rs '))
                balance -= amt
                print()
                pin = int(input(' PIN '))
                if pin == pw:
                    if amt <= balance :
                        print()
                        print(' Transaction Process... ')
                        print()
                        print(' Transaction Completed. ')
                        print()
                        limit +=1
                    else:
                        print()
                        print(' Insufficient Balance !!! ')
                else:
                    print(' Wrong PIN ')
                    #print(' Transaction Failed. ')
                    print()
            else:
                print()
                print(' Today Limit Exceed ')
                print()
        elif choice == 2:
            print(' Check Balance ')
            print(' -------------- ')
            pin = int(input(' PIN '))
            if pin == pw:
                print('Rs ',balance)
            else:
                print(' Wrong PIN ')
        elif choice == 3:
            print(' Have a Good Day!!! ')
            break
        else:
            print(' XXX Wrong Option XXX ')
elif check == 2:
    print(' Insert ATM Card ')
    print(' Try Again ')
else:
    print(' Insert ATM Card (OR) Wrong Option ')