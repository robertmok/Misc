#Description: A simulation of a poker game with one user and three computers.

##-----------------------------------------------------------------------------

import random

##-----------------------------------------------------------------------------
#Functions

#--------------------- Card Deal Functions
def carddeal (player,suitlist): #Deal cards to players
    x = 0
    while x == 0:
        suit = random.randrange(0,4) #Random suit
        card = random.randrange(0,13) #Random card
        if deck[suit][card] == 0: #if a card is already dealt, redeal another card
            suit = random.randrange(0,4)
            card = random.randrange(0,13)
        else:
            x = 1
            player.append(deck[suit][card])
            suitlist.append(suit)
            deck[suit][card] = 0 #Change the card to a 0 after it is dealt

def burncard (deck): #Burns the 1st card of the deck
    z = 0
    while z == 0:
        suit = random.randrange(0,4) #Random Suit
        card = random.randrange(0,13) #Random Card
        if deck[suit][card] == 0: #if card is already dealt, deal another
            suit = random.randrange(0,4)
            card = random.randrange(0,13)
        else:
            z = 1
            deck[suit][card] = 0 #Change a dealt card to a 0

def dealplaycards (cardshown,dealsuit): #deals the flop,river,...
    v = 0
    while v == 0:
        suit = random.randrange(0,4)
        card = random.randrange(0,13)
        if deck[suit][card] == 0:
            suit = random.randrange(0,4)
            card = random.randrange(0,13)
        else:
            v = 1
            cardshown.append(deck[suit][card])
            dealsuit.append(suit)
            deck[suit][card] = 0

def CombineSort (testing, testingsuit): #Sorting cards with the suits
    temp = 0
    temp1 = 0
    change = 0
    num = 0
    cards = len(testingsuit)
    card = cards
    while change == 0:
        num = 0
        for count in range(0,card-1):
            for count in range (0,cards-1):
                if testing[count]>testing[count+1]:
                    temp = testing[count]
                    testing[count]= testing[count+1]
                    testing[count+1]= temp

                    temp1 = testingsuit[count]
                    testingsuit[count]= testingsuit[count+1]
                    testingsuit[count+1]= temp1

                    num = num+1

                elif testingsuit[count]<testingsuit[count+1]:
                    num = num+0
                else:
                    change = 1
        if num == 0:
            change = 1
    return testing,testingsuit;

#------------------------- Poker Hands Functions
def StraightFlush (testing,testingsuit): #Checks for a straightflush
    z = 0
    straightflushcard = 0
    straightflushsuit = 0
    straightflushnum = 0
    while z == 0:
        y = len(testing)
        for count in range(0,y-1):
            x = testing[count]
            w = testingsuit[count]
            if x == testing[count-1]: #if it is the same card
                straightflushnum = straightflushnum+0
            else:
                if testing.count(x+1) and w == testingsuit[w+1]: #checks for a straight and same suit
                    straightflushnum = straightflushnum+1
                    straightflushsuit = w
                    straightflushcard = x
                else:
                    straightflushnum = straightflushnum+0
        z = 1
    return straightflushnum, straightflushsuit, straightflushcard

def Quad (testing): #Checks for quad
    cont = 0
    x = 0
    quadcard = 0
    while x == 0:
        for count in range(len(testing)):
            if cont > 0:
                x = 1
            else:
                if testing.count(testing[count]) == 4: #checks if there is 4 same cards
                    cont = cont+1
                    quadcard = testing[count]
                    x = 1
                else:
                    cont = 0
        x = 1
    return cont, quadcard

def FullHouse (testing): #Checks for a fullhouse
    cont = 0
    useless = 0
    num = []
    num1 = []
    fullhouse = 0
    fullhousepair = []
    x = 0
    s = 0
    m = 0
    n = 0
    L = 0
    J = 0
    cont1 = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    while x == 0:
        for count in range(len(testing)): #checks for a triple
            if testing.count(testing[count]) == 3:
                while s == 0:
                    cont = cont+1
                    s = 1
                    num.append(testing[count])
            elif testing.count(testing[count]) == 4:
                while m == 0:
                    cont = cont+1
                    m = 1
                    num.append(testing[count])
            elif testing.count(testing[count])== 5:
                while n == 0:
                    cont = cont+1
                    n = 1
                    num.append(testing[count])
            elif testing.count(testing[count])== 6:
                while L == 0:
                    cont = cont+2
                    L = 1
                    num.append(testing[count])
            elif testing.count(testing[count]) == 7:
                while J == 0:
                    cont = cont+2
                    J = 1
                    num.append(testing[count])
            else:
                cont = cont+0
        x = 1
        s = 1
        m = 1
        n = 1
        L = 1
        k = 1
        J = 1
    while a == 0:
        for count in range(len(testing)): #checks for a pair
            if testing.count(testing[count]) == 2:
                while b == 0:
                    cont1 = cont1+1
                    b = 1
                    num1.append(testing[count])
            elif testing.count(testing[count]) == 3:
                while c == 0:
                    cont1 = cont1+1
                    c = 1
                    num1.append(testing[count])
            elif testing.count(testing[count])== 4:
                while d == 0:
                    cont1 = cont1+2
                    d = 1
                    num1.append(testing[count])
            elif testing.count(testing[count])== 5:
                while e == 0:
                    cont1 = cont1+2
                    e = 1
                    num1.append(testing[count])
            elif testing.count(testing[count]) == 6:
                while f == 0:
                    cont1 = cont1+3
                    f = 1
                    num1.append(testing[count])
            elif testing.count(testing[count]) == 7:
                while g == 0:
                    cont1 = cont1+3
                    g = 1
                    num1.append(testing[count])
            else:
                cont1 = cont1+0
        if len(num1) > 1:
            for count in range(len(num1)):
                if num[0] == num1[count]: #if the triple is the same card as the pair
                    fullhouse = 0 #no fullhouse
                else:
                    fullhouse = 1
                    fullhousepair.append(num1[count])
        else:
            useless = 1
        a = 1
        b = 1
        c = 1
        d = 1
        e = 1
        f = 1
        g = 1
    return fullhouse, num, fullhousepair

def Flush (testingsuit): #Checks for a flush
    cont = 0
    x = 0
    flushsuit = 0
    while x == 0:
        for count in range(len(testingsuit)):
            if cont > 0:
                x = 1
            else:
                if testingsuit.count(testingsuit[count]) == 5: #checks for 5 of same suit
                    cont = cont+1
                    flushsuit = testingsuit[count]
                    x = 1
                else:
                    cont = 0
        x = 1
    return cont, flushsuit

def Straight (testing): #Checks for a straight
    z = 0
    straightnum = 0
    straightcard = 0
    while z == 0:
        y = len(testing)
        for count in range(0,y-1):
            x = testing[count]
            if x == testing[count-1]: #if same card
                straightnum = straightnum+0
            else:
                if testing.count(x+1) > 0:
                    straightnum = straightnum+1
                    straightcard = x
                else:
                    straightnum = straightnum+0
        z = 1
    return straightnum, straightcard

def Triple (testing): #checks for a triple
    cont = 0
    triplecard = []
    x = 0
    s = 0
    m = 0
    n = 0
    L = 0
    J = 0
    while x == 0:
        for count in range(len(testing)):
            if testing.count(testing[count]) == 3: #if theres only 3 cards
                while s == 0:
                    cont = cont+1
                    triplecard.append(testing[count])
                    s = 1
            elif testing.count(testing[count]) == 4: #if theres only 4 cards
                while m == 0:
                    cont = cont+1
                    triplecard.append(testing[count])
                    m = 1
            elif testing.count(testing[count])== 5: #if theres only 5 cards
                while n == 0:
                    cont = cont+1
                    triplecard.append(testing[count])
                    n = 1
            elif testing.count(testing[count])== 6: #if theres only 6 cards
                while L == 0:
                    cont = cont+2
                    for count in range(0,2): #there can only be 2 triple
                        for b in range(len(testing)):
                            if testing.count(testing[b]) == 3:
                                triplecard.append(testing[b])
                            elif testing.count(testing[b]) == 5:
                                triplecard.append(testing[b])
                            elif testing.count(testing[b]) == 4:
                                triplecard.append(testing[b])
                            else:
                                cont = cont+0
                    L = 1
            elif testing.count(testing[count]) == 7: #if there is 7 cards
                while J == 0:
                    cont = cont+2
                    for count in range(0,2): #there can only be 2 triple
                        for b in range(len(testing)):
                            if testing.count(testing[b]) == 3:
                                triplecard.append(testing[b])
                            elif testing.count(testing[b]) == 5:
                                triplecard.append(testing[b])
                            elif testing.count(testing[b]) == 4:
                                triplecard.append(testing[b])
                            else:
                                cont = cont+0
                    J = 1
            else:
                cont = cont+0
        x = 1
        s = 1
        m = 1
        n = 1
        L = 1
        k = 1
        J = 1
    return cont, triplecard

def Pair (testing): #Checks for a pair
    cont = 0
    paircard = []
    x = 0
    y = 0
    while x == 0:
        for count in range(len(testing)):
            if testing.count(testing[count])== 2 or testing.count(testing[count])== 3: #only 2 or 3 cards
                if len(paircard) == 0: #if theres is no pair in the record
                    paircard.append(testing[count])
                    cont = cont+1
                elif len(paircard) == 1: #if there is a pair in the record
                    if testing[count] == paircard[0]: #checks if its the same card
                        cont = cont+0
                    else:
                        paircard.append(testing[count]) #if not, then record that card
                        cont = cont+1
                elif len(paircard) == 2: #if there are two pairs in the record
                    if testing[count] == paircard[0] or testing[count] == paircard[1]: #Checks if the card is the same as the 2 pairs in the record
                        cont = cont+0
                    else:
                        paircard.append(testing[count]) #if not then record that card
                        cont = cont+1
                elif len(paircard) == 3: #if there are three pair in the record
                    if testing[count] == paircard[0] or testing[count] == paircard[1] or testing[count] == paircard[2]: #checks if the card is the same as the 3 pairs in the record
                        cont = cont+0
                    else:
                        paircard.append(testing[count]) #if not then record that card
                        cont = cont+1
            elif testing.count(testing[count])== 4 or testing.count(testing[count])== 5: #if there is 4 or 5 cards
                while y == 0:
                    paircard.append(testing[count])
                    paircard.append(testing[count])
                    cont = cont+2
                    y = 1
            else:
                cont = cont+0
        x = 1
        y = 1
    return cont, paircard

def Highcard (playercards, playersuit): #Finds the high card
    x = len(playercards)
    highc = playercards[x-1]
    highs = playersuit[x-1]
    return highs, highc;

def WinCombineSort (testing, testingsuit,testingwho): #A sort used in the winning pokerhands checks
    temp = 0
    temp1 = 0
    temp2 = 0
    change = 0
    num = 0
    cards = len(testingsuit)
    card = cards
    while change == 0:
        num = 0
        for count in range(0,card-1):
            for count in range (0,cards-1):
                if testing[count]>testing[count+1]:
                    temp = testing[count]
                    testing[count]= testing[count+1]
                    testing[count+1]= temp

                    temp1 = testingsuit[count]
                    testingsuit[count]= testingsuit[count+1]
                    testingsuit[count+1]= temp1

                    temp2 = testingwho[count]
                    testingwho[count]= testingwho[count+1]
                    testingwho[count+1]= temp2

                    num = num+1

                elif testingsuit[count]<testingsuit[count+1]:
                    num = num+0
                else:
                    change = 1
        if num == 0:
            change = 1
    return testing,testingsuit,testingwho

#-------------------------- Processes Functions

def USERprocesses (USER,Playcards,USERsuit,Playcardssuit): #lists used for checking hands for user
    USERtesting = []
    USERtestingsuit = []
    USERtesting.extend(USER)
    USERtesting.extend(Playcards)
    USERtestingsuit.extend(USERsuit)
    USERtestingsuit.extend(Playcardssuit)
    return USERtesting, USERtestingsuit

def CPU1processes (CPU1,Playcards,CPU1suit,Playcardssuit): #lists used for checking hands for CPU1
    CPU1testing = []
    CPU1testingsuit = []
    CPU1testing.extend(CPU1)
    CPU1testing.extend(Playcards)
    CPU1testingsuit.extend(CPU1suit)
    CPU1testingsuit.extend(Playcardssuit)
    return CPU1testing, CPU1testingsuit

def CPU2processes (CPU2,Playcards,CPU2suit,Playcardssuit): #lists used for checking hands for CPU2
    CPU2testing = []
    CPU2testingsuit = []
    CPU2testing.extend(CPU2)
    CPU2testing.extend(Playcards)
    CPU2testingsuit.extend(CPU2suit)
    CPU2testingsuit.extend(Playcardssuit)
    return CPU2testing, CPU2testingsuit

def CPU3processes (CPU3,Playcards,CPU3suit,Playcardssuit): #lists used for checking hands for CPU3
    CPU3testing = []
    CPU3testingsuit = []
    CPU3testing.extend(CPU3)
    CPU3testing.extend(Playcards)
    CPU3testingsuit.extend(CPU3suit)
    CPU3testingsuit.extend(Playcardssuit)
    return CPU3testing, CPU3testingsuit

#-------------------------- CPU Choices Functions

def CPU1choice (choice,CPU1straightflush,bet,CPU1bet,c1,pool,CPU1raise,CPU1quad,CPU1fullhouse,CPU1flush,CPU1straight,CPU1triple,CPU1pair,CPU1highcard,CPU1fold,USERfold,CPUbasebet): #Choices for CPU1
    if choice == 2: #User Bets
        if CPU1straightflush >= 4: #if there is a straight flush
            CPU1bet = bet*2
            c1 = c1-CPU1bet
            pool = pool+CPU1bet
            print "CPU1 has Raised by", CPU1bet
            print c1, "CPU1 Money"
            print pool, "Pool"
            CPU1raise = CPU1raise+1
            bet = CPU1bet

        elif CPU1quad > 0: #if there is a quad
            CPU1bet = bet*2
            c1 = c1-CPU1bet
            pool = pool+CPU1bet
            print "CPU1 has Raised by", CPU1bet
            print c1, "CPU1 Money"
            print pool, "Pool"
            CPU1raise = CPU1raise+1
            bet = CPU1bet

        elif CPU1fullhouse > 0: #if there is a fullhouse
            CPU1bet = bet*2
            c1 = c1-CPU1bet
            pool = pool+CPU1bet
            print "CPU1 has Raised by", CPU1bet
            print c1, "CPU1 Money"
            print pool, "Pool"
            CPU1raise = CPU1raise+1
            bet = CPU1bet

        elif CPU1flush > 0: #if there is a flush
            CPU1bet = bet*2
            c1 = c1-CPU1bet
            pool = pool+CPU1bet
            print "CPU1 has Raised by", CPU1bet
            print c1, "CPU1 Money"
            print pool, "Pool"
            CPU1raise = CPU1raise+1
            bet = CPU1bet

        elif CPU1straight >= 4: #if there is a straight
            CPU1bet = bet*2
            c1 = c1-CPU1bet
            pool = pool+CPU1bet
            print "CPU1 has Raised by", CPU1bet
            print c1, "CPU1 Money"
            print pool, "Pool"
            CPU1raise = CPU1raise+1
            bet = CPU1bet

        elif CPU1triple > 0: #if there is a triple
            c1 = c1-bet
            pool = pool+bet
            print "CPU1 has Called/putted in the same amount of money as you"
            print c1, "CPU1 Money"
            print pool, "Pool"

        elif CPU1pair > 0: #if there is a pair
            c1 = c1-bet
            pool = pool+bet
            print "CPU1 has Called/putted in the same amount of money as you"
            print c1, "CPU1 Money"
            print pool, "Pool"

        elif CPU1highcard >= 6: #if there is a high card
            c1 =c1-bet
            pool = pool+bet
            print "CPU1 has Called/putted in same amount of money as you"
            print c1, "CPU1 Money"
            print pool, "Pool"

        else: #if there is nothing
            print "CPU1 has Folded"
            CPU1fold = 1

    elif USERfold == 1: #User Folds
        if CPU1straightflush >= 4:
            c1 = c1-(CPUbasebet*2)
            pool = pool+(CPUbasebet*2)
            print "CPU1 has Raised by", bet
            print c1, "CPU1 Money"
            print pool, "Pool"
            CPU1raise = CPU1raise+1
            bet = (CPUbasebet*2)

        elif CPU1quad > 0:
            c1 = c1-(CPUbasebet*2)
            pool = pool+(CPUbasebet*2)
            print "CPU1 has Raised by", CPUbasebet*2
            print c1, "CPU1 Money"
            print pool, "Pool"
            CPU1raise = CPU1raise+1
            bet = (CPUbasebet*2)

        elif CPU1fullhouse > 0:
            c1 = c1-(CPUbasebet*2)
            pool = pool+(CPUbasebet*2)
            print "CPU1 has Raised by", CPUbasebet*2
            print c1, "CPU1 Money"
            print pool, "Pool"
            CPU1raise = CPU1raise+1
            bet = (CPUbasebet*2)

        elif CPU1flush > 0:
            c1 = c1-CPUbasebet*2
            pool = pool+CPUbasebet*2
            print "CPU1 has Raised by", CPUbasebet*2
            print c1, "CPU1 Money"
            print pool, "Pool"
            CPU1raise = CPU1raise+1
            bet = CPUbasebet*2

        elif CPU1straight >= 4:
            c1 = c1-(CPUbasebet*2)
            pool = pool+(CPUbasebet*2)
            print "CPU1 has Raised by", CPUbasebet*2
            print c1, "CPU1 Money"
            print pool, "Pool"
            CPU1raise = CPU1raise+1
            bet = CPUbasebet*2

        elif CPU1triple > 0:
            c1 = c1-CPUbasebet
            pool = pool+CPUbasebet
            print "CPU1 has Raised by", CPUbasebet
            print c1, "CPU1 Money"
            print pool, "Pool"
            bet = CPUbasebet

        elif CPU1pair > 0:
            c1 = c1-CPUbasebet
            pool = pool+CPUbasebet
            print "CPU1 has Raised by", CPUbasebet
            print c1, "CPU1 Money"
            print pool, "Pool"
            bet = CPUbasebet

        elif CPU1highcard >= 6:
            c1 =c1-CPUbasebet
            pool = pool+CPUbasebet
            print "CPU1 has Raised by", CPUbasebet
            print c1, "CPU1 Money"
            print pool, "Pool"
            bet = CPUbasebet

        else:
            print "CPU1 has Folded"
            CPU1fold = 1

    elif choice == 1: #User Checks
        print "CPU1 has Checked"
    return bet,CPU1bet,c1,pool,CPU1raise,CPU1fold

def CPU2choice (choice,CPU2straightflush,bet,CPU2bet,c2,pool,CPU2raise,CPU2quad,CPU2fullhouse,CPU2flush,CPU2straight,CPU2triple,CPU2pair,CPU2highcard,CPU2fold,USERfold,CPUbasebet,CPU1fold): #Choices for CPU2
    if choice == 2: #User Bets
        if CPU2straightflush >= 4:
            CPU2bet = bet*2
            c2 = c2-CPU2bet
            pool = pool+CPU2bet
            print "CPU2 has Raised by", CPU2bet
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPU2bet

        elif CPU2quad > 0:
            CPU2bet = bet*2
            c2 = c2-CPU2bet
            pool = pool+CPU2bet
            print "CPU2 has Raised by", CPU2bet
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPU2bet

        elif CPU2fullhouse > 0:
            CPU2bet = bet*2
            c2 = c2-CPU2bet
            pool = pool+CPU2bet
            print "CPU2 has Raised by", CPU2bet
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPU2bet

        elif CPU2flush > 0:
            CPU2bet = bet*2
            c2 = c2-CPU2bet
            pool = pool+CPU2bet
            print "CPU2 has Raised by", CPU2bet
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPU2bet

        elif CPU2straight >= 4:
            CPU2bet = bet*2
            c2 = c2-CPU2bet
            pool = pool+CPU2bet
            print "CPU2 has Raised by", CPU2bet
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPU2bet

        elif CPU2triple > 0:
            c2 = c2-bet
            pool = pool+bet
            print "CPU2 has Called/putted in the same amount of money as you"
            print c2, "CPU2 Money"
            print pool, "Pool"

        elif CPU2pair > 0:
            c2 = c2-bet
            pool = pool+bet
            print "CPU2 has Called/putted in the same amount of money as you"
            print c2, "CPU2 Money"
            print pool, "Pool"

        elif CPU2highcard >= 6:
            c2 =c2-bet
            pool = pool+bet
            print "CPU2 has Called/putted in same amount of money as you"
            print c2, "CPU2 Money"
            print pool, "Pool"

        else:
            print "CPU2 has Folded"
            CPU2fold = 1

    elif CPU1fold == 1 and USERfold == 0: #CPU1 Folds
        if CPU2straightflush >= 4:
            CPU2bet = bet*2
            c2 = c2-CPU2bet
            pool = pool+CPU2bet
            print "CPU2 has Raised by", CPU2bet
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPU2bet

        elif CPU2quad > 0:
            CPU2bet = bet*2
            c2 = c2-CPU2bet
            pool = pool+CPU2bet
            print "CPU2 has Raised by", CPU2bet
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPU2bet

        elif CPU2fullhouse > 0:
            CPU2bet = bet*2
            c2 = c2-CPU2bet
            pool = pool+CPU2bet
            print "CPU2 has Raised by", CPU2bet
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPU2bet

        elif CPU2flush > 0:
            CPU2bet = bet*2
            c2 = c2-CPU2bet
            pool = pool+CPU2bet
            print "CPU2 has Raised by", CPU2bet
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPU2bet

        elif CPU2straight >= 4:
            CPU2bet = bet*2
            c2 = c2-CPU2bet
            pool = pool+CPU2bet
            print "CPU2 has Raised by", CPU2bet
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPU2bet

        elif CPU2triple > 0:
            c2 = c2-bet
            pool = pool+bet
            print "CPU2 has Called/putted in the same amount of money as you"
            print c2, "CPU2 Money"
            print pool, "Pool"

        elif CPU2pair > 0:
            c2 = c2-bet
            pool = pool+bet
            print "CPU2 has Called/putted in the same amount of money as you"
            print c2, "CPU2 Money"
            print pool, "Pool"

        elif CPU2highcard >= 6:
            c2 =c2-bet
            pool = pool+bet
            print "CPU2 has Called/putted in same amount of money as you"
            print c2, "CPU2 Money"
            print pool, "Pool"

        else:
            print "CPU2 has Folded"
            CPU2fold = 1

    elif USERfold == 1 and CPU1fold == 0: #User Folds
        if CPU2straightflush >= 4:
            CPU2bet = bet*2
            c2 = c2-CPU2bet
            pool = pool+CPU2bet
            print "CPU2 has Raised by", CPU2bet
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPU2bet

        elif CPU2quad > 0:
            CPU2bet = bet*2
            c2 = c2-CPU2bet
            pool = pool+CPU2bet
            print "CPU2 has Raised by", CPU2bet
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPU2bet

        elif CPU2fullhouse > 0:
            CPU2bet = bet*2
            c2 = c2-CPU2bet
            pool = pool+CPU2bet
            print "CPU2 has Raised by", CPU2bet
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPU2bet

        elif CPU2flush > 0:
            CPU2bet = bet*2
            c2 = c2-CPU2bet
            pool = pool+CPU2bet
            print "CPU2 has Raised by", CPU2bet
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPU2bet

        elif CPU2straight >= 4:
            CPU2bet = bet*2
            c2 = c2-CPU2bet
            pool = pool+CPU2bet
            print "CPU2 has Raised by", CPU2bet
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPU2bet

        elif CPU2triple > 0:
            c2 = c2-bet
            pool = pool+bet
            print "CPU2 has Called/putted in the same amount of money as CPU1"
            print c2, "CPU2 Money"
            print pool, "Pool"

        elif CPU2pair > 0:
            c2 = c2-bet
            pool = pool+bet
            print "CPU2 has Called/putted in the same amount of money as CPU1"
            print c2, "CPU2 Money"
            print pool, "Pool"

        elif CPU2highcard >= 6:
            c2 =c2-bet
            pool = pool+bet
            print "CPU2 has Called/putted in same amount of money as CPU1"
            print c2, "CPU2 Money"
            print pool, "Pool"

        else:
            print "CPU2 has Folded"
            CPU2fold = 1

    elif USERfold == 1 and CPU1fold == 1: #User and CPU1 Folds
        if CPU2straightflush >= 4:
            c2 = c2-(CPUbasebet*2)
            pool = pool+(CPUbasebet*2)
            print "CPU2 has Raised by", CPUbasebet*2
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPUbasebet*2

        elif CPU2quad > 0:
            c2 = c2-CPUbasebet*2
            pool = pool+CPUbasebet*2
            print "CPU2 has Raised by", CPUbasebet*2
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPUbasebet*2

        elif CPU2fullhouse > 0:
            c2 = c2-CPUbasebet*2
            pool = pool+CPUbasebet*2
            print "CPU2 has Raised by", CPUbasebet*2
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPUbasebet*2

        elif CPU2flush > 0:
            c2 = c2-CPUbasebet*2
            pool = pool+CPUbasebet*2
            print "CPU2 has Raised by", CPUbasebet*2
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPUbasebet*2

        elif CPU2straight >= 4:
            c2 = c2-(CPUbasebet*2)
            pool = pool+(CPUbasebet*2)
            print "CPU2 has Raised by", CPUbasebet*2
            print c2, "CPU2 Money"
            print pool, "Pool"
            CPU2raise = CPU2raise+1
            bet = CPUbasebet*2

        elif CPU2triple > 0:
            c2 = c2-CPUbasebet
            pool = pool+CPUbasebet
            print "CPU2 has Raised by", CPUbasebet
            print c2, "CPU2 Money"
            print pool, "Pool"
            bet = CPUbasebet

        elif CPU2pair > 0:
            c2 = c2-CPUbasebet
            pool = pool+CPUbasebet
            print "CPU2 has Raised by", CPUbasebet
            print c2, "CPU2 Money"
            print pool, "Pool"
            bet = CPUbasebet

        elif CPU2highcard >= 6:
            c2 =c2-CPUbasebet
            pool = pool+CPUbasebet
            print "CPU2 has Raised by", CPUbasebet
            print c2, "CPU2 Money"
            print pool, "Pool"
            bet = CPUbasebet

        else:
            print "CPU2 has Folded"
            CPU2fold = 1

    elif choice == 1: #User Checks
        print "CPU2 has Checked"
    return bet,CPU2bet,c2,pool,CPU2raise,CPU2fold

def CPU3choice (choice,CPU3straightflush,bet,CPU3bet,c3,pool,CPU3raise,CPU3quad,CPU3fullhouse,CPU3flush,CPU3straight,CPU3triple,CPU3pair,CPU3highcard,CPU3fold,USERfold,CPUbasebet,CPU1fold,CPU2fold): #Choices for CPU3
    if choice == 2: #User Bets
        if CPU3straightflush >= 4:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3quad > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3fullhouse > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3flush > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3straight >= 4:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3triple > 0:
            c3 = c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in the same amount of money as you"
            print c3, "CPU3 Money"
            print pool, "Pool"

        elif CPU3pair > 0:
            c3 = c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in the same amount of money as you"
            print c3, "CPU3 Money"
            print pool, "Pool"

        elif CPU3highcard >= 6:
            c3 =c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in same amount of money as you"
            print c3, "CPU3 Money"
            print pool, "Pool"

        else:
            print "CPU3 has Folded"
            CPU3fold = 1

    elif CPU1fold == 1 and USERfold == 0 and CPU2fold == 0: #CPU1 Folds
        if CPU3straightflush >= 4:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3quad > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3fullhouse > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3flush > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3straight >= 4:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3triple > 0:
            c3 = c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in the same amount of money as you"
            print c3, "CPU3 Money"
            print pool, "Pool"

        elif CPU3pair > 0:
            c3 = c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in the same amount of money as you"
            print c3, "CPU3 Money"
            print pool, "Pool"

        elif CPU3highcard >= 6:
            c3 =c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in same amount of money as you"
            print c3, "CPU3 Money"
            print pool, "Pool"

        else:
            print "CPU3 has Folded"
            CPU3fold = 1

    elif USERfold == 1 and CPU1fold == 0 and CPU2fold == 0: #User Folds
        if CPU3straightflush >= 4:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3quad > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3fullhouse > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3flush > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3straight >= 4:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3triple > 0:
            c3 = c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in the same amount of money as CPU1"
            print c3, "CPU3 Money"
            print pool, "Pool"

        elif CPU3pair > 0:
            c3 = c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in the same amount of money as CPU1"
            print c3, "CPU3 Money"
            print pool, "Pool"

        elif CPU3highcard >= 6:
            c3 =c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in same amount of money as CPU1"
            print c3, "CPU3 Money"
            print pool, "Pool"

        else:
            print "CPU3 has Folded"
            CPU3fold = 1

    elif USERfold == 1 and CPU1fold == 1 and CPU2fold == 0: #User and CPU1 Folds
        if CPU3straightflush >= 4:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3quad > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3fullhouse > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3flush > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3straight >= 4:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3triple > 0:
            c3 = c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in the same amount of money as CPU2"
            print c3, "CPU3 Money"
            print pool, "Pool"

        elif CPU3pair > 0:
            c3 = c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in the same amount of money as CPU2"
            print c3, "CPU3 Money"
            print pool, "Pool"

        elif CPU3highcard >= 6:
            c3 =c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in same amount of money as CPU2"
            print c3, "CPU3 Money"
            print pool, "Pool"

        else:
            print "CPU3 has Folded"
            CPU3fold = 1

    elif USERfold == 1 and CPU2fold == 1 and CPU1fold == 0: #User and CPU2 Folds
        if CPU3straightflush >= 4:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3quad > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3fullhouse > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3flush > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3straight >= 4:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3triple > 0:
            c3 = c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in the same amount of money as CPU1"
            print c3, "CPU3 Money"
            print pool, "Pool"

        elif CPU3pair > 0:
            c3 = c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in the same amount of money as CPU1"
            print c3, "CPU3 Money"
            print pool, "Pool"

        elif CPU3highcard >= 6:
            c3 =c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in same amount of money as CPU1"
            print c3, "CPU3 Money"
            print pool, "Pool"

        else:
            print "CPU3 has Folded"
            CPU3fold = 1

    elif CPU1fold == 1 and CPU2fold == 1 and USERfold == 0: #CPU1 and CPU2 Folds
        if CPU3straightflush >= 4:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3quad > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3fullhouse > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3flush > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3straight >= 4:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3triple > 0:
            c3 = c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in the same amount of money as you"
            print c3, "CPU3 Money"
            print pool, "Pool"

        elif CPU3pair > 0:
            c3 = c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in the same amount of money as you"
            print c3, "CPU3 Money"
            print pool, "Pool"

        elif CPU3highcard >= 6:
            c3 =c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in same amount of money as you"
            print c3, "CPU3 Money"
            print pool, "Pool"

        else:
            print "CPU3 has Folded"
            CPU3fold = 1

    elif CPU1fold == 1 and USERfold == 0 and CPU2fold == 0: #CPU1 Folds
        if CPU3straightflush >= 4:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3quad > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3fullhouse > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3flush > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3straight >= 4:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3triple > 0:
            c3 = c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in the same amount of money as you"
            print c3, "CPU3 Money"
            print pool, "Pool"

        elif CPU3pair > 0:
            c3 = c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in the same amount of money as you"
            print c3, "CPU3 Money"
            print pool, "Pool"

        elif CPU3highcard >= 6:
            c3 =c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in same amount of money as you"
            print c3, "CPU3 Money"
            print pool, "Pool"

        else:
            print "CPU3 has Folded"
            CPU3fold = 1

    elif CPU2fold == 1 and USERfold == 0 and CPU1fold == 0: #CPU2 Folds
        if CPU3straightflush >= 4:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3quad > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3fullhouse > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3flush > 0:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3straight >= 4:
            CPU3bet = bet*2
            c3 = c3-CPU3bet
            pool = pool+CPU3bet
            print "CPU3 has Raised by", CPU3bet
            print c3, "CPU3 Money"
            print pool, "Pool"
            CPU3raise = CPU3raise+1
            bet = CPU3bet

        elif CPU3triple > 0:
            c3 = c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in the same amount of money as you"
            print c3, "CPU3 Money"
            print pool, "Pool"

        elif CPU3pair > 0:
            c3 = c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in the same amount of money as you"
            print c3, "CPU3 Money"
            print pool, "Pool"

        elif CPU3highcard >= 6:
            c3 =c3-bet
            pool = pool+bet
            print "CPU3 has Called/putted in same amount of money as you"
            print c3, "CPU3 Money"
            print pool, "Pool"

        else:
            print "CPU3 has Folded"
            CPU3fold = 1

    elif USERfold == 1 and CPU1fold == 1 and CPU2fold == 1: #User, CPU1 and CPU2 Folds
        print "CPU3 Wins the Game!"

    elif choice == 1: #User Checks
        print "CPU3 has Checked"
    return bet,CPU3bet,c3,pool,CPU3raise,CPU3fold

#-------------------------- Win Check Function

def Checkwin (winner, CPU1fold, CPU2fold, CPU3fold, USERfold): #Checks if there is a winner after each round
    if winner != []:
        if CPU1fold == 1 and CPU2fold == 1 and CPU3fold == 1: #if CPU1 , CPU2 and CPU3 folds
            winner.append(1) #winner is USER
        elif USERfold == 1 and CPU2fold == 1 and CPU3fold == 1: #if USER, CPU2 and CPU3 folds
            winner.append(2) #winner is CPU1
        elif USERfold == 1 and CPU1fold == 1 and CPU3fold == 1: #if USER, CPU1 and CPU3 folds
            winner.append(3) #winner is CPU2
        else:
            winner = [] #no winner yet
    ##--------------------
    return winner

##----------------------------------------------------------------------------

deckbase = []
deck = [[2,3,4,5,6,7,8,9,10,11,12,13,14],[2,3,4,5,6,7,8,9,10,11,12,13,14],[2,3,4,5,6,7,8,9,10,11,12,13,14],[2,3,4,5,6,7,8,9,10,11,12,13,14]]

#-------------------
CPU1 = []
CPU1suit = []
c1 = 500
CPU1raise = 0
CPU1bet = 0
CPU1fold = 0
CPU1win = 0

CPU2 = []
CPU2suit = []
c2 = 500
CPU2raise = 0
CPU2bet = 0
CPU2fold = 0
CPU2win = 0

CPU3 = []
CPU3suit = []
c3 = 500
CPU3raise = 0
CPU3bet = 0
CPU3fold = 0
CPU3win = 0

USER = []
USERsuit = []
umoney = 500
USERbet = 0
USERfold = 0
USERwin = 0

#-------------------
y = 0
redraw = 0
Playcards = []
Playcardssuit = []
pool = 0
gameplayed = 0
bet = 0
CPUbasebet = 20
winner = []
playagain = 0
playing = 0

#-------------------
quadnum = 0
flushnum = 0
triplenum = 0
pairnum = 0

#-------------------
CPU1testing = []
CPU1testingsuit = []
CPU1straightflush = 0
CPU1straightflushsuit = 0
CPU1straightflushcard = 0
CPU1quad = 0
CPU1quadcard = 0
CPU1fullhouse = 0
CPU1fullhousetriple = []
CPU1fullhousepair = []
CPU1flush = 0
CPU1flushsuit = 0
CPU1straight = 0
CPU1straightcard = 0
CPU1triple = 0
CPU1triplecard = []
CPU1pair = 0
CPU1paircard = []
CPU1highcard = []
CPU1highsuit = []

CPU2testing = []
CPU2testingsuit = []
CPU2straightflush = 0
CPU2straightflushsuit = 0
CPU2straightflushcard = 0
CPU2quad = 0
CPU2quadcard = 0
CPU2fullhouse = 0
CPU2fullhousetriple = []
CPU2fullhousepair = []
CPU2flush = 0
CPU2flushsuit = 0
CPU2straight = 0
CPU2straightcard = 0
CPU2triple = 0
CPU2triplecard = []
CPU2pair = 0
CPU2paircard = []
CPU2highcard = []
CPU2highsuit = []

CPU3testing = []
CPU3testingsuit = []
CPU3straightflush = 0
CPU3straightflushsuit = 0
CPU3straightflushcard = 0
CPU3quad = 0
CPU3quadcard = 0
CPU3fullhouse = 0
CPU3fullhousetriple = []
CPU3fullhousepair = []
CPU3flush = 0
CPU3flushsuit = 0
CPU3straight = 0
CPU3straightcard = 0
CPU3triple = 0
CPU3triplecard = []
CPU3pair = 0
CPU3paircard = []
CPU3highcard = []
CPU3highsuit = []

USERtesting = []
USERtestingsuit = []
USERstraightflush = 0
USERstraightflushsuit = 0
USERstraightflushcard = 0
USERquad = 0
USERquadcard = 0
USERfullhouse = 0
USERfullhousetriple = []
USERfullhousepair = []
USERflush = 0
USERflushsuit = 0
USERstraight = 0
USERstraightcard = 0
USERtriple = 0
USERtriplecard = []
USERpair = 0
USERpaircard = []
USERhighcard = []
USERhighsuit = []

#Program Start
##----------------------------------------------------------------------------
# Dealing Cards

while playing == 0:
    while y == 0:
        for count in range (0,2): #deal two cards to CPU1
            player = CPU1
            suitlist = CPU1suit
            carddeal (player,suitlist)

        for count in range (0,2): #deal two cards to CPU2
            player = CPU2
            suitlist = CPU2suit
            carddeal (player, suitlist)

        for count in range (0,2): #deal two cards to CPU3
            player = CPU3
            suitlist = CPU3suit
            carddeal (player, suitlist)

        for count in range (0,2): #deal two cards to USER
            player = USER
            suitlist = USERsuit
            carddeal (player, suitlist)
        print USER, "USER", USERsuit, "USER Suit"

        if redraw == 1: #can only redraw/discard once
            y = 1
        else:
            discard = input ("Would you like to discard your cards? Press 1 to discard or Press 2 to keep them!:")
            if discard == 1:
                CPU1 = []
                CPU1suit = []
                CPU2 = []
                CPU2suit = []
                CPU3 = []
                CPU3suit = []
                USER = []
                USERsuit = []
                y = 0
                redraw = 1
                print "----------------------------------------"
            else:
                y = 1

    ##-----------------------------------------------------------------------------
    #Dealing 1st round of cards

    for count in range (0,1): #burns a card before dealing
        burncard (deck)

    for count in range (0,3): #deals 3 cards for 1st round
        cardshown = Playcards
        dealsuit = Playcardssuit
        dealplaycards (cardshown,dealsuit)
    print Playcards, "Playcards", Playcardssuit, "Playcard Suit","(1st Round)"

    ##-----------------------------------------------------------------------------
    #Processes

    USERtesting, USERtestingsuit = USERprocesses(USER,Playcards,USERsuit,Playcardssuit) #info for checking hands of USER

    CPU1testing, CPU1testingsuit = CPU1processes(CPU1,Playcards,CPU1suit,Playcardssuit) #info for checking hands of CPU1

    CPU2testing, CPU2testingsuit = CPU2processes(CPU2,Playcards,CPU2suit,Playcardssuit) #infor for checking hands of CPU2

    CPU3testing, CPU3testingsuit = CPU3processes(CPU3,Playcards,CPU3suit,Playcardssuit) #infor for checking hands of CPU3

    ##-----------------------------------------------------------------------------
    #USER

    for count in range(0,1): #Sorts out User's hand
        testing = USER
        testingsuit = USERsuit
        USER,USERsuit = CombineSort(testing,testingsuit)

    for count in range(0,1): #Sorts out the info card for checking
        testing = USERtesting
        testingsuit = USERtestingsuit
        USERtesting,USERtestingsuit = CombineSort(testing,testingsuit)

    for count in range(0,1): #Checks for a straightflush
        testing = USERtesting
        testingsuit = USERtestingsuit
        USERstraightflush, USERstraightflushsuit, USERstraightflushcard = StraightFlush(testing,testingsuit)

    for count in range(0,1): #Checks for a quad
        testing = USERtesting
        quadnum, USERquadcard = Quad(testing)
        USERquad = quadnum
        quadnum = 0

    for count in range(0,1): #checks for fullhouse
        testing = USERtesting
        USERfullhouse, USERfullhousetriple, USERfullhousepair = FullHouse(testing)

    for count in range(0,1): #checks for a flush
        testingsuit = USERtestingsuit
        flushnum, USERflushsuit = Flush(testingsuit)
        USERflush = flushnum
        flushnum = 0

    for count in range(0,1): #checks for a straight
        testing = USERtesting
        USERstraight, USERstraightcard = Straight(testing)

    for count in range(0,1): #checks for a triple
        testing = USERtesting
        triplenum, USERtriplecard = Triple(testing)
        USERtriple = triplenum
        triplenum = 0

    for count in range(0,1): #checks for a pair
        testing = USERtesting
        pairnum, USERpaircard = Pair(testing)
        USERpair = pairnum
        pairnum = 0

    for count in range (0,1): #finds the high card
        playercards = USER
        playersuit = USERsuit
        USERhighsuit, USERhighcard = Highcard(playercards, playersuit)

    ##-----------------------------------------------------------------------------
    #CPU1

    for count in range(0,1): #same process as USER (above)
        testing = CPU1
        testingsuit = CPU1suit
        CPU1,CPU1suit = CombineSort(testing,testingsuit)

    for count in range(0,1):
        testing = CPU1testing
        testingsuit = CPU1testingsuit
        CPU1testing,CPU1testingsuit = CombineSort(testing,testingsuit)

    for count in range(0,1):
        testing = CPU1testing
        testingsuit = CPU1testingsuit
        CPU1straightflush, CPU1straightflushsuit, CPU1straightflushcard = StraightFlush(testing,testingsuit)

    for count in range(0,1):
        testing = CPU1testing
        quadnum, CPU1quadcard = Quad(testing)
        CPU1quad = quadnum
        quadnum = 0

    for count in range(0,1):
        testing = CPU1testing
        CPU1fullhouse, CPU1fullhousetriple, CPU1fullhousepair = FullHouse(testing)

    for count in range(0,1):
        testingsuit = CPU1testingsuit
        flushnum, CPU1flushsuit = Flush(testingsuit)
        CPU1flush = flushnum
        flushnum = 0

    for count in range(0,1):
        testing = CPU1testing
        CPU1straight, CPU1straightcard = Straight(testing)

    for count in range(0,1):
        testing = CPU1testing
        triplenum, CPU1triplecard = Triple(testing)
        CPU1triple = triplenum
        triplenum = 0

    for count in range(0,1):
        testing = CPU1testing
        pairnum, CPU1paircard = Pair(testing)
        CPU1pair = pairnum
        pairnum = 0

    for count in range (0,1):
        playercards = CPU1
        playersuit = CPU1suit
        CPU1highsuit, CPU1highcard = Highcard(playercards, playersuit)

    ##-----------------------------------------------------------------------------
    #CPU2

    for count in range(0,1): #same process as CPU1 and USER (above)
        testing = CPU2
        testingsuit = CPU2suit
        CPU2,CPU2suit = CombineSort(testing,testingsuit)

    for count in range(0,1):
        testing = CPU2testing
        testingsuit = CPU2testingsuit
        CPU2testing,CPU2testingsuit = CombineSort(testing,testingsuit)

    for count in range(0,1):
        testing = CPU2testing
        testingsuit = CPU2testingsuit
        CPU2straightflush, CPU2straightflushsuit, CPU2straightflushcard = StraightFlush(testing,testingsuit)

    for count in range(0,1):
        testing = CPU2testing
        quadnum, CPU2quadcard = Quad(testing)
        CPU2quad = quadnum
        quadnum = 0

    for count in range(0,1):
        testing = CPU2testing
        CPU2fullhouse, CPU2fullhousetriple, CPU2fullhousepair = FullHouse(testing)

    for count in range(0,1):
        testingsuit = CPU2testingsuit
        flushnum, CPU2flushsuit = Flush(testingsuit)
        CPU2flush = flushnum
        flushnum = 0

    for count in range(0,1):
        testing = CPU2testing
        CPU2straight, CPU2straightcard = Straight(testing)

    for count in range(0,1):
        testing = CPU2testing
        triplenum, CPU2triplecard = Triple(testing)
        CPU2triple = triplenum
        triplenum = 0

    for count in range(0,1):
        testing = CPU2testing
        pairnum, CPU2paircard = Pair(testing)
        CPU2pair = pairnum
        pairnum = 0

    for count in range (0,1):
        playercards = CPU2
        playersuit = CPU2suit
        CPU2highsuit, CPU2highcard = Highcard(playercards, playersuit)

    ##-----------------------------------------------------------------------------
    #CPU3

    for count in range(0,1): #same process as CPU1, CPU2 and USER (above)
        testing = CPU3
        testingsuit = CPU3suit
        CPU3,CPU3suit = CombineSort(testing,testingsuit)

    for count in range(0,1):
        testing = CPU3testing
        testingsuit = CPU3testingsuit
        CPU3testing,CPU3testingsuit = CombineSort(testing,testingsuit)

    for count in range(0,1):
        testing = CPU3testing
        testingsuit = CPU3testingsuit
        CPU3straightflush, CPU3straightflushsuit, CPU3straightflushcard = StraightFlush(testing,testingsuit)

    for count in range(0,1):
        testing = CPU3testing
        quadnum, CPU3quadcard = Quad(testing)
        CPU3quad = quadnum
        quadnum = 0

    for count in range(0,1):
        testing = CPU3testing
        CPU3fullhouse, CPU3fullhousetriple, CPU3fullhousepair = FullHouse(testing)

    for count in range(0,1):
        testingsuit = CPU3testingsuit
        flushnum, CPU3flushsuit = Flush(testingsuit)
        CPU3flush = flushnum
        flushnum = 0

    for count in range(0,1):
        testing = CPU3testing
        CPU3straight, CPU3straightcard = Straight(testing)

    for count in range(0,1):
        testing = CPU3testing
        triplenum, CPU3triplecard = Triple(testing)
        CPU3triple = triplenum
        triplenum = 0

    for count in range(0,1):
        testing = CPU3testing
        pairnum, CPU3paircard = Pair(testing)
        CPU3pair = pairnum
        pairnum = 0

    for count in range (0,1):
        playercards = CPU3
        playersuit = CPU3suit
        CPU3highsuit, CPU3highcard = Highcard(playercards, playersuit)

    ##-----------------------------------------------------------------------------
    #USER Choice

    print "----------------------------------------"
    print "Your money:", umoney
    choice = input ("Press 1 to Check or Press 2 to Raise/Bet or Press 3 to Fold:")
    if choice == 2: #if user raise or bets
        USERbet = input ("How much would you like to Raise/Bet?:")
        umoney = umoney-USERbet
        pool = pool+USERbet
        print "You have Raised by", USERbet
        print umoney, "Your amount of money left"
        print pool, "Pool"
        bet = USERbet
    elif choice == 3: #if user folds
        USERfold = 1
    else:
        print USER, "USER's Cards"

    ##-----------------------------------------------------------------------------
    #CPU1 Choice

    bet,CPU1bet,c1,pool,CPU1raise,CPU1fold = CPU1choice (choice,CPU1straightflush,bet,CPU1bet,c1,pool,CPU1raise,CPU1quad,CPU1fullhouse,CPU1flush,CPU1straight,CPU1triple,CPU1pair,CPU1highcard,CPU1fold,USERfold,CPUbasebet)

    ##-----------------------------------------------------------------------------
    #CPU2 Choice

    bet,CPU2bet,c2,pool,CPU2raise,CPU2fold = CPU2choice (choice,CPU2straightflush,bet,CPU2bet,c2,pool,CPU2raise,CPU2quad,CPU2fullhouse,CPU2flush,CPU2straight,CPU2triple,CPU2pair,CPU2highcard,CPU2fold,USERfold,CPUbasebet,CPU1fold)

    ##-----------------------------------------------------------------------------
    #CPU3 Choice

    bet,CPU3bet,c3,pool,CPU3raise,CPU3fold = CPU3choice (choice,CPU3straightflush,bet,CPU3bet,c3,pool,CPU3raise,CPU3quad,CPU3fullhouse,CPU3flush,CPU3straight,CPU3triple,CPU3pair,CPU3highcard,CPU3fold,USERfold,CPUbasebet,CPU1fold,CPU2fold)

    ##-----------------------------------------------------------------------------
    #2nd round of Betting (Maybe)


    ##-----------------------------------------------------------------------------
    #Checks if theres a winner

    winner = Checkwin(winner, CPU1fold, CPU2fold, CPU3fold, USERfold)

    ##-----------------------------------------------------------------------------
    #Dealing 2nd round of cards

    print "----------------------------------------"
    if winner == []:
        for count in range (0,1): #burns a card
            burncard (deck)

        for count in range (0,1): #deals one card
            cardshown = Playcards
            dealsuit = Playcardssuit
            dealplaycards (cardshown,dealsuit)
        print Playcards, "Playcards", Playcardssuit, "Playcard Suit","(2nd Round)"

     ##-----------------------------------------------------------------------------
    #Clear Varibles for 2nd round

    if winner == []: #if there is no winner
        CPU1raise = 0
        CPU1bet = 0

        CPU2raise = 0
        CPU2bet = 0

        CPU3raise = 0
        CPU3bet = 0

        USERbet = 0

        #-------------------
        bet = 0

        #-------------------
        quadnum = 0
        flushnum = 0
        triplenum = 0
        pairnum = 0

        #-------------------
        if CPU1fold != 1: #if CPU1 didnt fold
            CPU1testing = []
            CPU1testingsuit = []
            CPU1straightflush = 0
            CPU1straightflushsuit = 0
            CPU1straightflushcard = 0
            CPU1quad = 0
            CPU1quadcard = 0
            CPU1fullhouse = 0
            CPU1fullhousetriple = []
            CPU1fullhousepair = []
            CPU1flush = 0
            CPU1flushsuit = 0
            CPU1straight = 0
            CPU1straightcard = 0
            CPU1triple = 0
            CPU1triplecard = []
            CPU1pair = 0
            CPU1paircard = []
            CPU1highcard = []
            CPU1highsuit = []
        else:
            CPU1fold = 1

        if CPU2fold != 1: #if CPU2 didnt fold
            CPU2testing = []
            CPU2testingsuit = []
            CPU2straightflush = 0
            CPU2straightflushsuit = 0
            CPU2straightflushcard = 0
            CPU2quad = 0
            CPU2quadcard = 0
            CPU2fullhouse = 0
            CPU2fullhousetriple = []
            CPU2fullhousepair = []
            CPU2flush = 0
            CPU2flushsuit = 0
            CPU2straight = 0
            CPU2straightcard = 0
            CPU2triple = 0
            CPU2triplecard = []
            CPU2pair = 0
            CPU2paircard = []
            CPU2highcard = []
            CPU2highsuit = []
        else:
            CPU2fold = 1

        if CPU3fold != 1: #if CPU3 didnt fold
            CPU3testing = []
            CPU3testingsuit = []
            CPU3straightflush = 0
            CPU3straightflushsuit = 0
            CPU3straightflushcard = 0
            CPU3quad = 0
            CPU3quadcard = 0
            CPU3fullhouse = 0
            CPU3fullhousetriple = []
            CPU3fullhousepair = []
            CPU3flush = 0
            CPU3flushsuit = 0
            CPU3straight = 0
            CPU3straightcard = 0
            CPU3triple = 0
            CPU3triplecard = []
            CPU3pair = 0
            CPU3paircard = []
            CPU3highcard = []
            CPU3highsuit = []
        else:
            CPU3fold = 1

        if USERfold != 1: #if USER didnt fold
            USERtesting = []
            USERtestingsuit = []
            USERstraightflush = 0
            USERstraightflushsuit = 0
            USERstraightflushcard = 0
            USERquad = 0
            USERquadcard = 0
            USERfullhouse = 0
            USERfullhousetriple = []
            USERfullhousepair = []
            USERflush = 0
            USERflushsuit = 0
            USERstraight = 0
            USERstraightcard = 0
            USERtriple = 0
            USERtriplecard = []
            USERpair = 0
            USERpaircard = []
            USERhighcard = []
            USERhighsuit = []
        else:
            USERfold = 1

    ##-----------------------------------------------------------------------------
    #2nd Round of Processes
    if winner == []: #if theres no winner
        USERtesting, USERtestingsuit = USERprocesses(USER,Playcards,USERsuit,Playcardssuit)

        CPU1testing, CPU1testingsuit = CPU1processes(CPU1,Playcards,CPU1suit,Playcardssuit)

        CPU2testing, CPU2testingsuit = CPU2processes(CPU2,Playcards,CPU2suit,Playcardssuit)

        CPU3testing, CPU3testingsuit = CPU3processes(CPU3,Playcards,CPU3suit,Playcardssuit)

    ##-----------------------------------------------------------------------------

    #USER 2nd Round

        if USERfold != 1: #same process as round 1
            for count in range(0,1):
                testing = USER
                testingsuit = USERsuit
                USER,USERsuit = CombineSort(testing,testingsuit)

            for count in range(0,1):
                testing = USERtesting
                testingsuit = USERtestingsuit
                USERtesting,USERtestingsuit = CombineSort(testing,testingsuit)

            for count in range(0,1):
                testing = USERtesting
                testingsuit = USERtestingsuit
                USERstraightflush, USERstraightflushsuit, USERstraightflushcard = StraightFlush(testing,testingsuit)

            for count in range(0,1):
                testing = USERtesting
                quadnum, USERquadcard = Quad(testing)
                USERquad = quadnum
                quadnum = 0

            for count in range(0,1):
                testing = USERtesting
                USERfullhouse, USERfullhousetriple, USERfullhousepair = FullHouse(testing)

            for count in range(0,1):
                testingsuit = USERtestingsuit
                flushnum, USERflushsuit = Flush(testingsuit)
                USERflush = flushnum
                flushnum = 0

            for count in range(0,1):
                testing = USERtesting
                USERstraight, USERstraightcard = Straight(testing)

            for count in range(0,1):
                testing = USERtesting
                triplenum, USERtriplecard = Triple(testing)
                USERtriple = triplenum
                triplenum = 0

            for count in range(0,1):
                testing = USERtesting
                pairnum, USERpaircard = Pair(testing)
                USERpair = pairnum
                pairnum = 0

            for count in range (0,1):
                playercards = USER
                playersuit = USERsuit
                USERhighsuit, USERhighcard = Highcard(playercards, playersuit)
        else:
            USERfold = 1

    ##-----------------------------------------------------------------------------
    #CPU1 #2nd Round

        if CPU1fold != 1: #same process in round 1
            for count in range(0,1):
                testing = CPU1
                testingsuit = CPU1suit
                CPU1,CPU1suit = CombineSort(testing,testingsuit)

            for count in range(0,1):
                testing = CPU1testing
                testingsuit = CPU1testingsuit
                CPU1testing,CPU1testingsuit = CombineSort(testing,testingsuit)

            for count in range(0,1):
                testing = CPU1testing
                testingsuit = CPU1testingsuit
                CPU1straightflush, CPU1straightflushsuit, CPU1straightflushcard = StraightFlush(testing,testingsuit)

            for count in range(0,1):
                testing = CPU1testing
                quadnum, CPU1quadcard = Quad(testing)
                CPU1quad = quadnum
                quadnum = 0

            for count in range(0,1):
                testing = CPU1testing
                CPU1fullhouse, CPU1fullhousetriple, CPU1fullhousepair = FullHouse(testing)

            for count in range(0,1):
                testingsuit = CPU1testingsuit
                flushnum, CPU1flushsuit = Flush(testingsuit)
                CPU1flush = flushnum
                flushnum = 0

            for count in range(0,1):
                testing = CPU1testing
                CPU1straight, CPU1straightcard = Straight(testing)

            for count in range(0,1):
                testing = CPU1testing
                triplenum, CPU1triplecard = Triple(testing)
                CPU1triple = triplenum
                triplenum = 0

            for count in range(0,1):
                testing = CPU1testing
                pairnum, CPU1paircard = Pair(testing)
                CPU1pair = pairnum
                pairnum = 0

            for count in range (0,1):
                playercards = CPU1
                playersuit = CPU1suit
                CPU1highsuit, CPU1highcard = Highcard(playercards, playersuit)
        else:
            CPU1fold = 1

    ##-----------------------------------------------------------------------------
    #CPU2 2nd Round

        if CPU2fold != 1: #same process as round 1
            for count in range(0,1):
                testing = CPU2
                testingsuit = CPU2suit
                CPU2,CPU2suit = CombineSort(testing,testingsuit)

            for count in range(0,1):
                testing = CPU2testing
                testingsuit = CPU2testingsuit
                CPU2testing,CPU2testingsuit = CombineSort(testing,testingsuit)

            for count in range(0,1):
                testing = CPU2testing
                testingsuit = CPU2testingsuit
                CPU2straightflush, CPU2straightflushsuit, CPU2straightflushcard = StraightFlush(testing,testingsuit)

            for count in range(0,1):
                testing = CPU2testing
                quadnum, CPU2quadcard = Quad(testing)
                CPU2quad = quadnum
                quadnum = 0

            for count in range(0,1):
                testing = CPU2testing
                CPU2fullhouse, CPU2fullhousetriple, CPU2fullhousepair = FullHouse(testing)

            for count in range(0,1):
                testingsuit = CPU2testingsuit
                flushnum, CPU2flushsuit = Flush(testingsuit)
                CPU2flush = flushnum
                flushnum = 0

            for count in range(0,1):
                testing = CPU2testing
                CPU2straight, CPU2straightcard = Straight(testing)

            for count in range(0,1):

                testing = CPU2testing
                triplenum, CPU2triplecard = Triple(testing)
                CPU2triple = triplenum
                triplenum = 0

            for count in range(0,1):
                testing = CPU2testing
                pairnum, CPU2paircard = Pair(testing)
                CPU2pair = pairnum
                pairnum = 0

            for count in range (0,1):
                playercards = CPU2
                playersuit = CPU2suit
                CPU2highsuit, CPU2highcard = Highcard(playercards, playersuit)
        else:
            CPU2fold = 1

    ##-----------------------------------------------------------------------------
    #CPU3 #2nd Round

        if CPU3fold != 1: #same process as round 1
            for count in range(0,1):
                testing = CPU3
                testingsuit = CPU3suit
                CPU3,CPU3suit = CombineSort(testing,testingsuit)

            for count in range(0,1):
                testing = CPU3testing
                testingsuit = CPU3testingsuit
                CPU3testing,CPU3testingsuit = CombineSort(testing,testingsuit)

            for count in range(0,1):
                testing = CPU3testing
                testingsuit = CPU3testingsuit
                CPU3straightflush, CPU3straightflushsuit, CPU3straightflushcard = StraightFlush(testing,testingsuit)

            for count in range(0,1):
                testing = CPU3testing
                quadnum, CPU3quadcard = Quad(testing)
                CPU3quad = quadnum
                quadnum = 0

            for count in range(0,1):
                testing = CPU3testing
                CPU3fullhouse, CPU3fullhousetriple, CPU3fullhousepair = FullHouse(testing)

            for count in range(0,1):
                testingsuit = CPU3testingsuit
                flushnum, CPU3flushsuit = Flush(testingsuit)
                CPU3flush = flushnum
                flushnum = 0

            for count in range(0,1):
                testing = CPU3testing
                CPU3straight, CPU3straightcard = Straight(testing)

            for count in range(0,1):
                testing = CPU3testing
                triplenum, CPU3triplecard = Triple(testing)
                CPU3triple = triplenum
                triplenum = 0

            for count in range(0,1):
                testing = CPU3testing
                pairnum, CPU3paircard = Pair(testing)
                CPU3pair = pairnum
                pairnum = 0

            for count in range (0,1):
                playercards = CPU3
                playersuit = CPU3suit
                CPU3highsuit, CPU3highcard = Highcard(playercards, playersuit)
        else:
            CPU3fold = 1

    ##-----------------------------------------------------------------------------
    #USER Choice #2nd Round

        print "----------------------------------------"
        print "Your money:", umoney
        if USERfold != 1: #if user didnt fold
            choice = input ("Press 1 to Check or Press 2 to Raise/Bet or Press 3 to Fold:")
            if choice == 2: #if user raise or bets
                USERbet = input ("How much would you like to Raise/Bet?:")
                umoney = umoney-USERbet
                pool = pool+USERbet
                print "You have Raised by", USERbet
                print umoney, "Your amount of money left"
                print pool, "Pool"
                bet = USERbet
            elif choice == 3: #if user folds
                USERfold = 1
            else:
                print USER, "USER's Cards"
        else:
            USERfold = 1

    ##-----------------------------------------------------------------------------
    #CPU1 Choice 2nd Round

        bet,CPU1bet,c1,pool,CPU1raise,CPU1fold = CPU1choice (choice,CPU1straightflush,bet,CPU1bet,c1,pool,CPU1raise,CPU1quad,CPU1fullhouse,CPU1flush,CPU1straight,CPU1triple,CPU1pair,CPU1highcard,CPU1fold,USERfold,CPUbasebet)

    ##-----------------------------------------------------------------------------
    #CPU2 Choice 2nd Round

        bet,CPU2bet,c2,pool,CPU2raise,CPU2fold = CPU2choice (choice,CPU2straightflush,bet,CPU2bet,c2,pool,CPU2raise,CPU2quad,CPU2fullhouse,CPU2flush,CPU2straight,CPU2triple,CPU2pair,CPU2highcard,CPU2fold,USERfold,CPUbasebet,CPU1fold)

    ##-----------------------------------------------------------------------------
    #CPU3 Choice 2nd Round

        bet,CPU3bet,c3,pool,CPU3raise,CPU3fold = CPU3choice (choice,CPU3straightflush,bet,CPU3bet,c3,pool,CPU3raise,CPU3quad,CPU3fullhouse,CPU3flush,CPU3straight,CPU3triple,CPU3pair,CPU3highcard,CPU3fold,USERfold,CPUbasebet,CPU1fold,CPU2fold)

    ##-----------------------------------------------------------------------------
    #2nd round of Betting (Maybe)


    ##-----------------------------------------------------------------------------
    #Checks if theres a winner 2nd Round

    if winner == []: #if theres no winner
        winner = Checkwin(winner, CPU1fold, CPU2fold, CPU3fold, USERfold)

    ##-----------------------------------------------------------------------------
    #Dealing 3rd Round of cards

    print "----------------------------------------"
    if winner == []:
        for count in range (0,1): #burns a card
            burncard (deck)

        for count in range (0,1): #deals the last card
            cardshown = Playcards
            dealsuit = Playcardssuit
            dealplaycards (cardshown,dealsuit)
        print Playcards, "Playcards", Playcardssuit, "Playcard Suit","(3rd Round)"

     ##-----------------------------------------------------------------------------
    #Clear Varibles for 3rd round

    if winner == []: #if theres no winner
        CPU1raise = 0
        CPU1bet = 0

        CPU2raise = 0
        CPU2bet = 0

        CPU3raise = 0
        CPU3bet = 0

        USERbet = 0

        #-------------------
        bet = 0

        #-------------------
        quadnum = 0
        flushnum = 0
        triplenum = 0
        pairnum = 0

        #-------------------
        if CPU1fold != 1: #if CPU1 didnt fold
            CPU1testing = []
            CPU1testingsuit = []
            CPU1straightflush = 0
            CPU1straightflushsuit = 0
            CPU1straightflushcard = 0
            CPU1quad = 0
            CPU1quadcard = 0
            CPU1fullhouse = 0
            CPU1fullhousetriple = []
            CPU1fullhousepair = []
            CPU1flush = 0
            CPU1flushsuit = 0
            CPU1straight = 0
            CPU1straightcard = 0
            CPU1triple = 0
            CPU1triplecard = []
            CPU1pair = 0
            CPU1paircard = []
            CPU1highcard = []
            CPU1highsuit = []
        else:
            CPU1fold = 1

        if CPU2fold != 1: #if CPU2 didnt fold
            CPU2testing = []
            CPU2testingsuit = []
            CPU2straightflush = 0
            CPU2straightflushsuit = 0
            CPU2straightflushcard = 0
            CPU2quad = 0
            CPU2quadcard = 0
            CPU2fullhouse = 0
            CPU2fullhousetriple = []
            CPU2fullhousepair = []
            CPU2flush = 0
            CPU2flushsuit = 0
            CPU2straight = 0
            CPU2straightcard = 0
            CPU2triple = 0
            CPU2triplecard = []
            CPU2pair = 0
            CPU2paircard = []
            CPU2highcard = []
            CPU2highsuit = []
        else:
            CPU2fold = 1

        if CPU3fold != 1: #if CPU3 didnt fold
            CPU3testing = []
            CPU3testingsuit = []
            CPU3straightflush = 0
            CPU3straightflushsuit = 0
            CPU3straightflushcard = 0
            CPU3quad = 0
            CPU3quadcard = 0
            CPU3fullhouse = 0
            CPU3fullhousetriple = []
            CPU3fullhousepair = []
            CPU3flush = 0
            CPU3flushsuit = 0
            CPU3straight = 0
            CPU3straightcard = 0
            CPU3triple = 0
            CPU3triplecard = []
            CPU3pair = 0
            CPU3paircard = []
            CPU3highcard = []
            CPU3highsuit = []
        else:
            CPU3fold = 1

        if USERfold != 1: #if user didnt fold
            USERtesting = []
            USERtestingsuit = []
            USERstraightflush = 0
            USERstraightflushsuit = 0
            USERstraightflushcard = 0
            USERquad = 0
            USERquadcard = 0
            USERfullhouse = 0
            USERfullhousetriple = []
            USERfullhousepair = []
            USERflush = 0
            USERflushsuit = 0
            USERstraight = 0
            USERstraightcard = 0
            USERtriple = 0
            USERtriplecard = []
            USERpair = 0
            USERpaircard = []
            USERhighcard = []
            USERhighsuit = []
        else:
            USERfold = 1

    ##-----------------------------------------------------------------------------
    #3rd Round of Processes

    if winner == []: #if theres no winner
        USERtesting, USERtestingsuit = USERprocesses(USER,Playcards,USERsuit,Playcardssuit)

        CPU1testing, CPU1testingsuit = CPU1processes(CPU1,Playcards,CPU1suit,Playcardssuit)

        CPU2testing, CPU2testingsuit = CPU2processes(CPU2,Playcards,CPU2suit,Playcardssuit)

        CPU3testing, CPU3testingsuit = CPU3processes(CPU3,Playcards,CPU3suit,Playcardssuit)

    ##-----------------------------------------------------------------------------
    #USER 3rd Round

    if winner == []: #if theres no winner
        if USERfold != 1: #if user didnt fold
            for count in range(0,1): #same process as round 1 and round 2
                testing = USER
                testingsuit = USERsuit
                USER,USERsuit = CombineSort(testing,testingsuit)

            for count in range(0,1):
                testing = USERtesting
                testingsuit = USERtestingsuit
                USERtesting,USERtestingsuit = CombineSort(testing,testingsuit)

            for count in range(0,1):
                testing = USERtesting
                testingsuit = USERtestingsuit
                USERstraightflush, USERstraightflushsuit, USERstraightflushcard = StraightFlush(testing,testingsuit)

            for count in range(0,1):
                testing = USERtesting
                quadnum, USERquadcard = Quad(testing)
                USERquad = quadnum
                quadnum = 0

            for count in range(0,1):
                testing = USERtesting
                USERfullhouse, USERfullhousetriple, USERfullhousepair = FullHouse(testing)

            for count in range(0,1):
                testingsuit = USERtestingsuit
                flushnum, USERflushsuit = Flush(testingsuit)
                USERflush = flushnum
                flushnum = 0

            for count in range(0,1):
                testing = USERtesting
                USERstraight, USERstraightcard = Straight(testing)

            for count in range(0,1):
                testing = USERtesting
                triplenum, USERtriplecard = Triple(testing)
                USERtriple = triplenum
                triplenum = 0

            for count in range(0,1):
                testing = USERtesting
                pairnum, USERpaircard = Pair(testing)
                USERpair = pairnum
                pairnum = 0

            for count in range (0,1):
                playercards = USER
                playersuit = USERsuit
                USERhighsuit, USERhighcard = Highcard(playercards, playersuit)
        else:
            USERfold = 1

        ##-----------------------------------------------------------------------------
        #CPU1 #3rd Round

        if CPU1fold != 1: #same process as round 1 and round 2
            for count in range(0,1):
                testing = CPU1
                testingsuit = CPU1suit
                CPU1,CPU1suit = CombineSort(testing,testingsuit)

            for count in range(0,1):
                testing = CPU1testing
                testingsuit = CPU1testingsuit
                CPU1testing,CPU1testingsuit = CombineSort(testing,testingsuit)

            for count in range(0,1):
                testing = CPU1testing
                testingsuit = CPU1testingsuit
                CPU1straightflush, CPU1straightflushsuit, CPU1straightflushcard = StraightFlush(testing,testingsuit)

            for count in range(0,1):
                testing = CPU1testing
                quadnum, CPU1quadcard = Quad(testing)
                CPU1quad = quadnum
                quadnum = 0

            for count in range(0,1):
                testing = CPU1testing
                CPU1fullhouse, CPU1fullhousetriple, CPU1fullhousepair = FullHouse(testing)

            for count in range(0,1):
                testingsuit = CPU1testingsuit
                flushnum, CPU1flushsuit = Flush(testingsuit)
                CPU1flush = flushnum
                flushnum = 0

            for count in range(0,1):
                testing = CPU1testing
                CPU1straight, CPU1straightcard = Straight(testing)

            for count in range(0,1):
                testing = CPU1testing
                triplenum, CPU1triplecard = Triple(testing)
                CPU1triple = triplenum
                triplenum = 0

            for count in range(0,1):
                testing = CPU1testing
                pairnum, CPU1paircard = Pair(testing)
                CPU1pair = pairnum
                pairnum = 0

            for count in range (0,1):
                playercards = CPU1
                playersuit = CPU1suit
                CPU1highsuit, CPU1highcard = Highcard(playercards, playersuit)
        else:
            CPU1fold = 1

        ##-----------------------------------------------------------------------------
        #CPU2 3rd Round

        if CPU2fold != 1: #same process as round 1 and round 2
            for count in range(0,1):
                testing = CPU2
                testingsuit = CPU2suit
                CPU2,CPU2suit = CombineSort(testing,testingsuit)

            for count in range(0,1):
                testing = CPU2testing
                testingsuit = CPU2testingsuit
                CPU2testing,CPU2testingsuit = CombineSort(testing,testingsuit)

            for count in range(0,1):
                testing = CPU2testing
                testingsuit = CPU2testingsuit
                CPU2straightflush, CPU2straightflushsuit, CPU2straightflushcard = StraightFlush(testing,testingsuit)

            for count in range(0,1):
                testing = CPU2testing
                quadnum, CPU2quadcard = Quad(testing)
                CPU2quad = quadnum
                quadnum = 0

            for count in range(0,1):
                testing = CPU2testing
                CPU2fullhouse, CPU2fullhousetriple, CPU2fullhousepair = FullHouse(testing)

            for count in range(0,1):
                testingsuit = CPU2testingsuit
                flushnum, CPU2flushsuit = Flush(testingsuit)
                CPU2flush = flushnum
                flushnum = 0

            for count in range(0,1):
                testing = CPU2testing
                CPU2straight, CPU2straightcard = Straight(testing)

            for count in range(0,1):

                testing = CPU2testing
                triplenum, CPU2triplecard = Triple(testing)
                CPU2triple = triplenum
                triplenum = 0

            for count in range(0,1):
                testing = CPU2testing
                pairnum, CPU2paircard = Pair(testing)
                CPU2pair = pairnum
                pairnum = 0

            for count in range (0,1):
                playercards = CPU2
                playersuit = CPU2suit
                CPU2highsuit, CPU2highcard = Highcard(playercards, playersuit)
        else:
            CPU2fold = 1

        ##-----------------------------------------------------------------------------
        #CPU3 #3rd Round

        if CPU3fold != 1: #same process as round 1 and round 2
            for count in range(0,1):
                testing = CPU3
                testingsuit = CPU3suit
                CPU3,CPU3suit = CombineSort(testing,testingsuit)

            for count in range(0,1):
                testing = CPU3testing
                testingsuit = CPU3testingsuit
                CPU3testing,CPU3testingsuit = CombineSort(testing,testingsuit)

            for count in range(0,1):
                testing = CPU3testing
                testingsuit = CPU3testingsuit
                CPU3straightflush, CPU3straightflushsuit, CPU3straightflushcard = StraightFlush(testing,testingsuit)

            for count in range(0,1):
                testing = CPU3testing
                quadnum, CPU3quadcard = Quad(testing)
                CPU3quad = quadnum
                quadnum = 0

            for count in range(0,1):
                testing = CPU3testing
                CPU3fullhouse, CPU3fullhousetriple, CPU3fullhousepair = FullHouse(testing)

            for count in range(0,1):

                testingsuit = CPU3testingsuit
                flushnum, CPU3flushsuit = Flush(testingsuit)
                CPU3flush = flushnum
                flushnum = 0

            for count in range(0,1):
                testing = CPU3testing
                CPU3straight, CPU3straightcard = Straight(testing)

            for count in range(0,1):
                testing = CPU3testing
                triplenum, CPU3triplecard = Triple(testing)
                CPU3triple = triplenum
                triplenum = 0

            for count in range(0,1):
                testing = CPU3testing
                pairnum, CPU3paircard = Pair(testing)
                CPU3pair = pairnum
                pairnum = 0

            for count in range (0,1):
                playercards = CPU3
                playersuit = CPU3suit
                CPU3highsuit, CPU3highcard = Highcard(playercards, playersuit)
        else:
            CPU3fold = 1

        ##-----------------------------------------------------------------------------
        #USER Choice #3rd Round

        print "----------------------------------------"
        print "Your money:", umoney
        if USERfold != 1: #if user didnt fold
            choice = input ("Press 1 to Check or Press 2 to Raise/Bet or Press 3 to Fold:")
            if choice == 2: #if user raise or bets
                USERbet = input ("How much would you like to Raise/Bet?:")
                umoney = umoney-USERbet
                pool = pool+USERbet
                print "You have Raised by", USERbet
                print umoney, "Your amount of money left"
                print pool, "Pool"
                bet = USERbet
            elif choice == 3: #if user folds
                USERfold = 1
            else:
                print USER, "USER's Cards"
        else:
            USERfold = 1

        ##-----------------------------------------------------------------------------
        #CPU1 Choice 3rd Round

        if CPU1fold != 1: #same process as round 1 and round 2
            if choice == 2: #User Bets
                if CPU1straightflush >= 4:
                    CPU1bet = bet*2
                    c1 = c1-CPU1bet
                    pool = pool+CPU1bet
                    print "CPU1 has Raised by", CPU1bet
                    print c1, "CPU1 Money"
                    print pool, "Pool"
                    CPU1raise = CPU1raise+1
                    bet = CPU1bet

                elif CPU1quad > 0:
                    CPU1bet = bet*2
                    c1 = c1-CPU1bet
                    pool = pool+CPU1bet
                    print "CPU1 has Raised by", CPU1bet
                    print c1, "CPU1 Money"
                    print pool, "Pool"
                    CPU1raise = CPU1raise+1
                    bet = CPU1bet

                elif CPU1fullhouse > 0:
                    CPU1bet = bet*2
                    c1 = c1-CPU1bet
                    pool = pool+CPU1bet
                    print "CPU1 has Raised by", CPU1bet
                    print c1, "CPU1 Money"
                    print pool, "Pool"
                    CPU1raise = CPU1raise+1
                    bet = CPU1bet

                elif CPU1flush > 0:
                    CPU1bet = bet*2
                    c1 = c1-CPU1bet
                    pool = pool+CPU1bet
                    print "CPU1 has Raised by", CPU1bet
                    print c1, "CPU1 Money"
                    print pool, "Pool"
                    CPU1raise = CPU1raise+1
                    bet = CPU1bet

                elif CPU1straight >= 4:
                    CPU1bet = bet*2
                    c1 = c1-CPU1bet
                    pool = pool+CPU1bet
                    print "CPU1 has Raised by", CPU1bet
                    print c1, "CPU1 Money"
                    print pool, "Pool"
                    CPU1raise = CPU1raise+1
                    bet = CPU1bet

                elif CPU1triple > 0:
                    c1 = c1-bet
                    pool = pool+bet
                    print "CPU1 has Called/putted in the same amount of money as you"
                    print c1, "CPU1 Money"
                    print pool, "Pool"

                elif CPU1pair > 0:
                    c1 = c1-bet
                    pool = pool+bet
                    print "CPU1 has Called/putted in the same amount of money as you"
                    print c1, "CPU1 Money"
                    print pool, "Pool"

                elif CPU1highcard >= 6:
                    c1 =c1-bet
                    pool = pool+bet
                    print "CPU1 has Called/putted in same amount of money as you"
                    print c1, "CPU1 Money"
                    print pool, "Pool"

                else:
                    print "CPU1 has Folded"
                    CPU1fold = 1

            elif USERfold == 1: #User Folds
                if CPU1straightflush >= 4:
                    c1 = c1-(CPUbasebet*2)
                    pool = pool+(CPUbasebet*2)
                    print "CPU1 has Raised by", bet
                    print c1, "CPU1 Money"
                    print pool, "Pool"
                    CPU1raise = CPU1raise+1
                    bet = (CPUbasebet*2)

                elif CPU1quad > 0:
                    c1 = c1-(CPUbasebet*2)
                    pool = pool+(CPUbasebet*2)
                    print "CPU1 has Raised by", CPUbasebet*2
                    print c1, "CPU1 Money"
                    print pool, "Pool"
                    CPU1raise = CPU1raise+1
                    bet = (CPUbasebet*2)

                elif CPU1fullhouse > 0:
                    c1 = c1-(CPUbasebet*2)
                    pool = pool+(CPUbasebet*2)
                    print "CPU1 has Raised by", CPUbasebet*2
                    print c1, "CPU1 Money"
                    print pool, "Pool"
                    CPU1raise = CPU1raise+1
                    bet = (CPUbasebet*2)

                elif CPU1flush > 0:
                    c1 = c1-CPUbasebet*2
                    pool = pool+CPUbasebet*2
                    print "CPU1 has Raised by", CPUbasebet*2
                    print c1, "CPU1 Money"
                    print pool, "Pool"
                    CPU1raise = CPU1raise+1
                    bet = CPUbasebet*2

                elif CPU1straight >= 4:
                    c1 = c1-(CPUbasebet*2)
                    pool = pool+(CPUbasebet*2)
                    print "CPU1 has Raised by", CPUbasebet*2
                    print c1, "CPU1 Money"
                    print pool, "Pool"
                    CPU1raise = CPU1raise+1
                    bet = CPUbasebet*2

                elif CPU1triple > 0:
                    c1 = c1-CPUbasebet
                    pool = pool+CPUbasebet
                    print "CPU1 has Raised by", CPUbasebet
                    print c1, "CPU1 Money"
                    print pool, "Pool"
                    bet = CPUbasebet

                elif CPU1pair > 0:
                    c1 = c1-CPUbasebet
                    pool = pool+CPUbasebet
                    print "CPU1 has Raised by", CPUbasebet
                    print c1, "CPU1 Money"
                    print pool, "Pool"
                    bet = CPUbasebet

                elif CPU1highcard >= 6:
                    c1 =c1-CPUbasebet
                    pool = pool+CPUbasebet
                    print "CPU1 has Raised by", CPUbasebet
                    print c1, "CPU1 Money"
                    print pool, "Pool"
                    bet = CPUbasebet

                else:
                    print "CPU1 has Folded"
                    CPU1fold = 1

            elif choice == 1: #User Checks
                print "CPU1 has Checked"
        else:
            CPU1fold != 1

        ##-----------------------------------------------------------------------------
        #CPU2 Choice #3rd Round

        if CPU2fold != 1: #same processs as round 1 and round 2
            if choice == 2: #User Bets
                if CPU2straightflush >= 4:
                    CPU2bet = bet*2
                    c2 = c2-CPU2bet
                    pool = pool+CPU2bet
                    print "CPU2 has Raised by", CPU2bet
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPU2bet

                elif CPU2quad > 0:
                    CPU2bet = bet*2
                    c2 = c2-CPU2bet
                    pool = pool+CPU2bet
                    print "CPU2 has Raised by", CPU2bet
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPU2bet

                elif CPU2fullhouse > 0:
                    CPU2bet = bet*2
                    c2 = c2-CPU2bet
                    pool = pool+CPU2bet
                    print "CPU2 has Raised by", CPU2bet
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPU2bet

                elif CPU2flush > 0:
                    CPU2bet = bet*2
                    c2 = c2-CPU2bet
                    pool = pool+CPU2bet
                    print "CPU2 has Raised by", CPU2bet
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPU2bet

                elif CPU2straight >= 4:
                    CPU2bet = bet*2
                    c2 = c2-CPU2bet
                    pool = pool+CPU2bet
                    print "CPU2 has Raised by", CPU2bet
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPU2bet

                elif CPU2triple > 0:
                    c2 = c2-bet
                    pool = pool+bet
                    print "CPU2 has Called/putted in the same amount of money as you"
                    print c2, "CPU2 Money"
                    print pool, "Pool"

                elif CPU2pair > 0:
                    c2 = c2-bet
                    pool = pool+bet
                    print "CPU2 has Called/putted in the same amount of money as you"
                    print c2, "CPU2 Money"
                    print pool, "Pool"

                elif CPU2highcard >= 6:
                    c2 =c2-bet
                    pool = pool+bet
                    print "CPU2 has Called/putted in same amount of money as you"
                    print c2, "CPU2 Money"
                    print pool, "Pool"

                else:
                    print "CPU2 has Folded"
                    CPU2fold = 1

            elif CPU1fold == 1 and USERfold == 0: #CPU1 Folds
                if CPU2straightflush >= 4:
                    CPU2bet = bet*2
                    c2 = c2-CPU2bet
                    pool = pool+CPU2bet
                    print "CPU2 has Raised by", CPU2bet
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPU2bet

                elif CPU2quad > 0:
                    CPU2bet = bet*2
                    c2 = c2-CPU2bet
                    pool = pool+CPU2bet
                    print "CPU2 has Raised by", CPU2bet
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPU2bet

                elif CPU2fullhouse > 0:
                    CPU2bet = bet*2
                    c2 = c2-CPU2bet
                    pool = pool+CPU2bet
                    print "CPU2 has Raised by", CPU2bet
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPU2bet

                elif CPU2flush > 0:
                    CPU2bet = bet*2
                    c2 = c2-CPU2bet
                    pool = pool+CPU2bet
                    print "CPU2 has Raised by", CPU2bet
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPU2bet

                elif CPU2straight >= 4:
                    CPU2bet = bet*2
                    c2 = c2-CPU2bet
                    pool = pool+CPU2bet
                    print "CPU2 has Raised by", CPU2bet
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPU2bet

                elif CPU2triple > 0:
                    c2 = c2-bet
                    pool = pool+bet
                    print "CPU2 has Called/putted in the same amount of money as you"
                    print c2, "CPU2 Money"
                    print pool, "Pool"

                elif CPU2pair > 0:
                    c2 = c2-bet
                    pool = pool+bet
                    print "CPU2 has Called/putted in the same amount of money as you"
                    print c2, "CPU2 Money"
                    print pool, "Pool"

                elif CPU2highcard >= 6:
                    c2 =c2-bet
                    pool = pool+bet
                    print "CPU2 has Called/putted in same amount of money as you"
                    print c2, "CPU2 Money"
                    print pool, "Pool"

                else:
                    print "CPU2 has Folded"
                    CPU2fold = 1

            elif USERfold == 1 and CPU1fold == 0: #User Folds
                if CPU2straightflush >= 4:
                    CPU2bet = bet*2
                    c2 = c2-CPU2bet
                    pool = pool+CPU2bet
                    print "CPU2 has Raised by", CPU2bet
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPU2bet

                elif CPU2quad > 0:
                    CPU2bet = bet*2
                    c2 = c2-CPU2bet
                    pool = pool+CPU2bet
                    print "CPU2 has Raised by", CPU2bet
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPU2bet

                elif CPU2fullhouse > 0:
                    CPU2bet = bet*2
                    c2 = c2-CPU2bet
                    pool = pool+CPU2bet
                    print "CPU2 has Raised by", CPU2bet
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPU2bet

                elif CPU2flush > 0:
                    CPU2bet = bet*2
                    c2 = c2-CPU2bet
                    pool = pool+CPU2bet
                    print "CPU2 has Raised by", CPU2bet
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPU2bet

                elif CPU2straight >= 4:
                    CPU2bet = bet*2
                    c2 = c2-CPU2bet
                    pool = pool+CPU2bet
                    print "CPU2 has Raised by", CPU2bet
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPU2bet

                elif CPU2triple > 0:
                    c2 = c2-bet
                    pool = pool+bet
                    print "CPU2 has Called/putted in the same amount of money as CPU1"
                    print c2, "CPU2 Money"
                    print pool, "Pool"

                elif CPU2pair > 0:
                    c2 = c2-bet
                    pool = pool+bet
                    print "CPU2 has Called/putted in the same amount of money as CPU1"
                    print c2, "CPU2 Money"
                    print pool, "Pool"

                elif CPU2highcard >= 6:
                    c2 =c2-bet
                    pool = pool+bet
                    print "CPU2 has Called/putted in same amount of money as CPU1"
                    print c2, "CPU2 Money"
                    print pool, "Pool"

                else:
                    print "CPU2 has Folded"
                    CPU2fold = 1

            elif USERfold == 1 and CPU1fold == 1: #User and CPU1 Folds
                if CPU2straightflush >= 4:
                    c2 = c2-(CPUbasebet*2)
                    pool = pool+(CPUbasebet*2)
                    print "CPU2 has Raised by", CPUbasebet*2
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPUbasebet*2

                elif CPU2quad > 0:
                    c2 = c2-CPUbasebet*2
                    pool = pool+CPUbasebet*2
                    print "CPU2 has Raised by", CPUbasebet*2
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPUbasebet*2

                elif CPU2fullhouse > 0:
                    c2 = c2-CPUbasebet*2
                    pool = pool+CPUbasebet*2
                    print "CPU2 has Raised by", CPUbasebet*2
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPUbasebet*2

                elif CPU2flush > 0:
                    c2 = c2-CPUbasebet*2
                    pool = pool+CPUbasebet*2
                    print "CPU2 has Raised by", CPUbasebet*2
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPUbasebet*2

                elif CPU2straight >= 4:
                    c2 = c2-(CPUbasebet*2)
                    pool = pool+(CPUbasebet*2)
                    print "CPU2 has Raised by", CPUbasebet*2
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    CPU2raise = CPU2raise+1
                    bet = CPUbasebet*2

                elif CPU2triple > 0:
                    c2 = c2-CPUbasebet
                    pool = pool+CPUbasebet
                    print "CPU2 has Raised by", CPUbasebet
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    bet = CPUbasebet

                elif CPU2pair > 0:
                    c2 = c2-CPUbasebet
                    pool = pool+CPUbasebet
                    print "CPU2 has Raised by", CPUbasebet
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    bet = CPUbasebet

                elif CPU2highcard >= 6:
                    c2 =c2-CPUbasebet
                    pool = pool+CPUbasebet
                    print "CPU2 has Raised by", CPUbasebet
                    print c2, "CPU2 Money"
                    print pool, "Pool"
                    bet = CPUbasebet

                else:
                    print "CPU2 has Folded"
                    CPU2fold = 1

            elif choice == 1: #User Checks
                print "CPU2 has Checked"
        else:
            CPU2fold = 1

        ##-----------------------------------------------------------------------------
        #CPU3 Choice 3rd Round

        if CPU3fold != 1: #same process as round 1 and round 2
            if choice == 2: #User Bets
                if CPU3straightflush >= 4:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3quad > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3fullhouse > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3flush > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3straight >= 4:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3triple > 0:
                    c3 = c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in the same amount of money as you"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                elif CPU3pair > 0:
                    c3 = c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in the same amount of money as you"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                elif CPU3highcard >= 6:
                    c3 =c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in same amount of money as you"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                else:
                    print "CPU3 has Folded"
                    CPU3fold = 1

            elif CPU1fold == 1: #CPU1 Folds
                if CPU3straightflush >= 4:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3quad > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3fullhouse > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3flush > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3straight >= 4:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3triple > 0:
                    c3 = c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in the same amount of money as you"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                elif CPU3pair > 0:
                    c3 = c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in the same amount of money as you"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                elif CPU3highcard >= 6:
                    c3 =c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in same amount of money as you"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                else:
                    print "CPU3 has Folded"
                    CPU3fold = 1

            elif USERfold == 1 and CPU1fold == 0 and CPU2fold == 0: #User Folds
                if CPU3straightflush >= 4:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3quad > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3fullhouse > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3flush > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3straight >= 4:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3triple > 0:
                    c3 = c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in the same amount of money as CPU1"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                elif CPU3pair > 0:
                    c3 = c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in the same amount of money as CPU1"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                elif CPU3highcard >= 6:
                    c3 =c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in same amount of money as CPU1"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                else:
                    print "CPU3 has Folded"
                    CPU3fold = 1

            elif USERfold == 1 and CPU1fold == 1 and CPU2fold == 0: #User and CPU1 Folds
                if CPU3straightflush >= 4:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3quad > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3fullhouse > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3flush > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3straight >= 4:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3triple > 0:
                    c3 = c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in the same amount of money as CPU2"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                elif CPU3pair > 0:
                    c3 = c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in the same amount of money as CPU2"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                elif CPU3highcard >= 6:
                    c3 =c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in same amount of money as CPU2"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                else:
                    print "CPU3 has Folded"
                    CPU3fold = 1

            elif USERfold == 1 and CPU2fold == 1 and CPU1fold == 0: #User and CPU2 Folds
                if CPU3straightflush >= 4:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3quad > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3fullhouse > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3flush > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3straight >= 4:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3triple > 0:
                    c3 = c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in the same amount of money as CPU1"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                elif CPU3pair > 0:
                    c3 = c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in the same amount of money as CPU1"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                elif CPU3highcard >= 6:
                    c3 =c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in same amount of money as CPU1"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                else:
                    print "CPU3 has Folded"
                    CPU3fold = 1

            elif CPU1fold == 1 and CPU2fold == 1 and USERfold == 0: #CPU1 and CPU2 Folds
                if CPU3straightflush >= 4:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3quad > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3fullhouse > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3flush > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3straight >= 4:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3triple > 0:
                    c3 = c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in the same amount of money as you"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                elif CPU3pair > 0:
                    c3 = c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in the same amount of money as you"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                elif CPU3highcard >= 6:
                    c3 =c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in same amount of money as you"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                else:
                    print "CPU3 has Folded"
                    CPU3fold = 1

            elif CPU1fold == 1 and USERfold == 0 and CPU2fold == 0: #CPU1 Folds
                if CPU3straightflush >= 4:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3quad > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3fullhouse > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3flush > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3straight >= 4:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3triple > 0:
                    c3 = c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in the same amount of money as you"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                elif CPU3pair > 0:
                    c3 = c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in the same amount of money as you"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                elif CPU3highcard >= 6:
                    c3 =c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in same amount of money as you"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                else:
                    print "CPU3 has Folded"
                    CPU3fold = 1

            elif CPU2fold == 1 and USERfold == 0 and CPU1fold == 0: #CPU2 Folds
                if CPU3straightflush >= 4:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3quad > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3fullhouse > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3flush > 0:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3straight >= 4:
                    CPU3bet = bet*2
                    c3 = c3-CPU3bet
                    pool = pool+CPU3bet
                    print "CPU3 has Raised by", CPU3bet
                    print c3, "CPU3 Money"
                    print pool, "Pool"
                    CPU3raise = CPU3raise+1
                    bet = CPU3bet

                elif CPU3triple > 0:
                    c3 = c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in the same amount of money as you"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                elif CPU3pair > 0:
                    c3 = c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in the same amount of money as you"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                elif CPU3highcard >= 6:
                    c3 =c3-bet
                    pool = pool+bet
                    print "CPU3 has Called/putted in same amount of money as you"
                    print c3, "CPU3 Money"
                    print pool, "Pool"

                else:
                    print "CPU3 has Folded"
                    CPU3fold = 1

            elif USERfold == 1 and CPU1fold == 1 and CPU2fold == 1: #User, CPU1 and CPU2 Folds
                winner.append(4)
            elif choice == 1: #User Checks
                print "CPU3 has Checked"
        else:
            CPU3fold = 1

    ##-----------------------------------------------------------------------------
    #Check if theres a winner 3rd Round

    if winner == []: #if theres no winner
        winner = Checkwin(winner, CPU1fold, CPU2fold, CPU3fold, USERfold)

    ##-----------------------------------------------------------------------------
    #Checking if anyone has a Straight Flush to win the game

    print "----------------------------------------"
    straightflushwincheck = []
    straightflushwhowin = []
    straightflushsuitwin = []
    straightflushcardwin =[]

    #------------------------------------------------------
    if winner == []: #if theres no winner
        if USERfold != 1: #if User didnt fold
            if USERstraightflush >= 4: #if user has a straight flush
                straightflushwhowin.append(1)
                straightflushwincheck.append(USERstraightflush)
                straightflushsuitwin.append(USERstraightflushsuit)
                straightflushcardwin.append(USERstraightflushcard)
            else:
                USERfold = 0
        else:
            USERfold = 1

        if CPU1fold != 1: #if CPU1 didnt fold
            if CPU1straightflush >= 4: #if CPU1 has a straight flush
                straightflushwhowin.append(2)
                straightflushwincheck.append(CPU1straightflush)
                straightflushsuitwin.append(CPU1straightflushsuit)
                straightflushcardwin.append(CPU1straightflushcard)
            else:
                CPU1fold = 0
        else:
            CPU1fold = 1

        if CPU2fold != 1: #if CPU2 didnt fold
            if CPU2straightflush >= 4: #if CPU2 has a straight flush
                straightflushwhowin.append(3)
                straightflushwincheck.append(CPU2straightflush)
                straightflushsuitwin.append(CPU2straightflushsuit)
                straightflushcardwin.append(CPU2straightflushcard)
            else:
                CPU2fold = 0
        else:
            CPU2fold = 1

        if CPU3fold != 1: #if CPU3 didnt fold
            if CPU3straightflush >= 4: #if CPU3 has a straight flush
                straightflushwhowin.append(4)
                straightflushwincheck.append(CPU3straightflush)
                straightflushsuitwin.append(CPU3straightflushsuit)
                straightflushcardwin.append(CPU3straightflushcard)
            else:
                CPU3fold = 0
        else:
            CPU3fold = 1
        #---------------------------------------------
        if straightflushwincheck.count(4) == 1: #if there is only 1 player with a straight flush
            winner.append(straightflushwhowin[0])
        elif straightflushwincheck.count(4) == 2: #if there is 2 player with a straight flush
            if straightflushsuitwin[0] != straightflushsuitwin[1]: #if it is a different straight flush
                testing = straightflushcardwin
                testingsuit = straightflushsuitwin
                testingwho = straightflushwhowin
                straightflushcardwin, straightflushsuitwin, straightflushwhowin = WinCombineSort(testing,testingsuit,testingwho)
                winner.append(straightflushwhowin[1])
            elif straightflushsuitwin[0] == straightflushsuitwin[1]: #if it is the same straight flush
                if straightflushcardwin[0] > straightflushcardwin[1]:
                    winner.append(straightflushwhowin[0])
                elif straightflushcardwin[1] > straightflushcardwin[0]:
                    winner.append(straightflushwhowin[1])
                else:
                    winner.append(straightflushwhowin[0])
                    winner.append(straightflushwhowin[1])
        elif straightflushwincheck.count(4) > 2: #if there is more than 2 players with a straight flush
            testing = straightflushcardwin
            testingsuit = straightflushsuitwin
            testingwho = straightflushwhowin
            straightflushcardwin, straightflushsuitwin, straightflushwhowin = WinCombineSort(testing,testingsuit,testingwho)
            sfw = len(straightflushcardwin) #sorted players from least to highest straight flush
            if straightflushsuitwin[sfw-1] == straightflushsuitwin[sfw-2]: # if the last two players has the same suit
                if straightflushcardwin[sfw-1] == straightflushcardwin[sfw-2]: #if the last two players has the same card
                    winner.append(straightflushwhowin[sfw-1])
                    winner.append(straightflushwhowin[sfw-2])
                else:
                    winner.append(straightflushwhowin[sfw-1])
            else:
                winner.append(straightflushwhowin[sfw-1])
        else:
            winner = [] #no winner
        if straightflushwhowin != []: #if there is a winner
            print "Player(s)", straightflushwhowin, "has a Straight Flush"

    ##-----------------------------------------------------------------------------
    #Checking if anyone has a Quad to win the game

    quadwincheck = []
    quadwhowin = []
    quadcardwin =[]

    #-----------------------
    if winner == []: #if theres no winner
        if USERfold != 1: #if USER didnt fold
            if USERquad == 1: #if User has a quad
                quadwhowin.append(1)
                quadwincheck.append(USERquad)
                quadcardwin.append(USERquadcard)
            else:
                USERfold = 0
        else:
            USERfold = 1

        if CPU1fold != 1: #if CPU1 didnt fold
            if CPU1quad == 1: #if CPU1 has a quad
                quadwhowin.append(2)
                quadwincheck.append(CPU1quad)
                quadcardwin.append(CPU1quadcard)
            else:
                CPU1fold = 0
        else:
            CPU1fold = 1

        if CPU2fold != 1: #if CPU2 didnt fold
            if CPU2quad == 1: #if CPU2 has a quad
                quadwhowin.append(3)
                quadwincheck.append(CPU2quad)
                quadcardwin.append(CPU2quadcard)
            else:
                CPU2fold = 0
        else:
            CPU2fold = 1

        if CPU3fold != 1: #if CPU3 didnt fold
            if CPU3quad == 1: #if CPU3 has a quad
                quadwhowin.append(4)
                quadwincheck.append(CPU3quad)
                quadcardwin.append(CPU3quadcard)
            else:
                CPU3fold = 0
        else:
            CPU3fold = 1
        #----------------------------------------
        if quadwincheck.count(1) == 1: #if there is only one player with a quad
            winner.append(quadwhowin[0])
        elif quadwincheck.count(1) == 2: #if there is 2 players with a quad
            if quadcardwin[0] != quadcardwin[1]: #if the 2 players have a different quad
                testing = quadcardwin
                testingsuit = quadwhowin
                quadcardwin, quadwhowin= CombineSort(testing,testingsuit) #sort least to greatest
                winner.append(quadwhowin[1])
            elif quadcardwin[0] == quadcardwin[1]: #if it is the same quad
                    winner.append(quadwhowin[0])
                    winner.append(quadwhowin[1])
            else:
                winner = []
        elif quadwincheck.count(1) > 2: #if there is more than 2 players with a quad
            testing = quadcardwin
            testingsuit = quadwhowin
            quadcardwin, quadwhowin = CombineSort(testing,testingsuit) #sort least to greatest
            qw = len(quadcardwin)
            if quadcardwin[qw-1] == quadcardwin[qw-2]: #if the last 2 players have the same quad
                winner.append(quadwhowin[qw-1])
                winner.append(quadwhowin[qw-2])
            else:
                winner.append(quadwhowin[qw-1])
        else:
            winner = [] #no winner
        if quadwhowin != []: #if there is a winner
            print "Player(s):", quadwhowin, "has a Quad"

    ##-----------------------------------------------------------------------------
    #Checking if anyone has a Full House to win the game

    fullhousewincheck = []
    fullhousewhowin = []
    fullhousecardwin =[]
    fullhousecard2win = []

    #------------------------------
    if winner == []: #if there is no winner
        if USERfold != 1: #if USER didnt fold
            if USERfullhouse == 1: #if user has a full house
                fullhousewhowin.append(1)
                fullhousewincheck.append(USERfullhouse)
                fullhousecardwin.append(USERfullhousetriple[0])
                fullhousecard2win.append(USERfullhousepair[0])
            else:
               USERfullhouse = 0
        else:
            USERfold = 1

        if CPU1fold != 1: #if CPU1 didnt fold
            if CPU1fullhouse == 1: #if CPU1 has a full house
                fullhousewhowin.append(2)
                fullhousewincheck.append(CPU1fullhouse)
                fullhousecardwin.append(CPU1fullhousetriple[0])
                fullhousecard2win.append(CPU1fullhousepair[0])
            else:
               CPU1fullhouse = 0
        else:
            CPU1fold = 1

        if CPU2fold != 1: #if CPU2 didnt fold
            if CPU2fullhouse == 1: #if CPU2 has a full house
                fullhousewhowin.append(3)
                fullhousewincheck.append(CPU2fullhouse)
                fullhousecardwin.append(CPU2fullhousetriple[0])
                fullhousecard2win.append(CPU2fullhousepair[0])
            else:
                CPU2fullhouse = 0
        else:
            CPU2fold = 1

        if CPU3fold != 1: #if CPU3 didnt fold
            if CPU3fullhouse == 1: #if CPU3 has a full house
                fullhousewhowin.append(4)
                fullhousewincheck.append(CPU3fullhouse)
                fullhousecardwin.append(CPU3fullhousetriple[0])
                fullhousecard2win.append(CPU3fullhousepair[0])
            else:
                CPU3fullhouse = 0
        else:
            CPU3fold = 1
        #------------------------------------------
        if fullhousewincheck.count(1) == 1: #if there is only 1 player with a full house
            winner.append(fullhousewhowin[0])
        elif fullhousewincheck.count(1) == 2: #if there is 2 players with a full house
            if fullhousecardwin[0] != fullhousecardwin[1]: #if they have a different full house
                testing = fullhousecardwin
                testingsuit = fullhousewhowin
                fullhousecardwin, fullhousewhowin= CombineSort(testing,testingsuit) #sort least to greatest
                winner.append(fullhousewhowin[1])
            elif fullhousecardwin[0] == fullhousecardwin[1]: #if they have the same full house
                if fullhousecard2win[0] > fullhousecard2win[1]: #Check which pair is higher
                    winner.append(fullhousewhowin[0])
                elif fullhousecard2win[1] > fullhousecard2win[0]:
                    winner.append(fullhousewhowin[1])
                else: #if the pair is the same
                    winner.append(fullhousewhowin[0])
                    winner.append(fullhousewhowin[1])
            else:
                winner = []
        elif fullhousewincheck.count(1) > 2: #if there is more than 2 players with a full house
            testing = fullhousecardwin
            testingsuit = fullhousewhowin
            fullhousecardwin, fullhousewhowin = CombineSort(testing,testingsuit) #sort least to greatest
            fhw = len(fullhousecardwin)
            if fullhousecardwin[fhw-1] == fullhousecardwin[fhw-2]: #if the last two players has the same full house
                if fullhousecard2win[fhw-1] > fullhousecard2win[fhw-2]: #check which pair is higher
                    winner.append(fullhousewhowin[fhw-1])
                elif fullhousecard2win[fhw-2] > fullhousecard2win[fhw-1]:
                    winner.append(fullhousewhowin[fhw-2])
                else:
                    winner.append(fullhousewhowin[fhw-1])
                    winner.append(fullhousewhowin[fhw-2])
            else:
                winner.append(fullhousewhowin[fhw-1])
        else:
            winner = [] #no winner
        if fullhousewhowin != []: #if there is a winner
            print "Player(s):", fullhousewhowin, "has a Full House"

    ##-----------------------------------------------------------------------------
    #Checking if anyone has a Flush to win the game

    flushwincheck = []
    flushwhowin = []
    flushsuitwin =[]

    #---------------------------
    if winner == []: #if there is no winner
        if USERfold != 1: #if USER didnt fold
            if USERflush == 1: #if USER has a flush
                flushwhowin.append(1)
                flushwincheck.append(USERflush)
                flushsuitwin.append(USERflushsuit)
            else:
                USERfold = 0
        else:
            USERfold = 1

        if CPU1fold != 1: #if CPU1 didnt fold
            if CPU1flush == 1: #if CPU1 has a flush
                flushwhowin.append(2)
                flushwincheck.append(CPU1flush)
                flushsuitwin.append(CPU1flushsuit)
            else:
                CPU1fold = 0
        else:
            CPU1fold = 1

        if CPU2fold != 1: #if CPU2 didnt fold
            if CPU2flush == 1: #if CPU2 has a flush
                flushwhowin.append(3)
                flushwincheck.append(CPU2flush)
                flushsuitwin.append(CPU2flushsuit)
            else:
                CPU2fold = 0
        else:
            CPU2fold = 1

        if CPU3fold != 1: #if CPU3 didnt fold
            if CPU3flush == 1: #if CPU3 has a flush
                flushwhowin.append(4)
                flushwincheck.append(CPU3flush)
                flushsuitwin.append(CPU3flushsuit)
            else:
                CPU3fold = 0
        else:
            CPU3fold = 1
        #------------------------------------
        if flushwincheck.count(1) == 1: #if there is only 1 player with a flush
            winner.append(flushwhowin[0])
        elif flushwincheck.count(1) == 2: #if there is 2 players with a flush
            if flushsuitwin[0] != flushsuitwin[1]: #if they have different a flush
                testing = flushsuitwin
                testingsuit = flushwhowin
                flushsuitwin, flushwhowin= CombineSort(testing,testingsuit) #sort from least to highest
                winner.append(flushwhowin[1])
            elif flushsuitwin[0] == flushsuitwin[1]: #if they have the same flush
                    winner.append(flushwhowin[0])
                    winner.append(flushwhowin[1])
            else:
                winner = []
        elif flushwincheck.count(1) > 2: #if there is more than 2 players with a flush
            testing = flushsuitwin
            testingsuit = flushwhowin
            flushsuitwin, flushwhowin = CombineSort(testing,testingsuit) #sort least to highest
            fw = len(flushsuitwin)
            if flushsuitwin[fw-1] == flushsuitwin[fw-2]: #if the last two players has the same flush
                winner.append(flushwhowin[fw-1])
                winner.append(flushwhowin[fw-2])
            else:
                winner.append(flushwhowin[fw-1])
        else:
            winner = [] #no winner
        if flushwhowin != []: #if there is a winner
            print "Player(s):", flushwhowin, "has a Flush"

    ##-----------------------------------------------------------------------------
    #Checking if anyone has a Straight to win the game

    straightwincheck = []
    straightwhowin = []
    straightcardwin =[]

    #-----------------------
    if winner == []: #if there is no winners
        if USERfold != 1: #if USER didnt fold
            if USERstraight >= 4: #if USER has a straight
                straightwhowin.append(1)
                straightwincheck.append(USERstraight)
                straightcardwin.append(USERstraightcard)
            else:
                USERfold = 0
        else:
            USERfold = 1

        if CPU1fold != 1: #if CPU1 didnt fold
            if CPU1straight >= 4: #if CPU1 has a straight
                straightwhowin.append(2)
                straightwincheck.append(CPU1straight)
                straightcardwin.append(CPU1straightcard)
            else:
                CPU1fold = 0
        else:
            CPU1fold = 1

        if CPU2fold != 1: #if CPU2 didnt fold
            if CPU2straight >= 4: #if CPU2 has a straight
                straightwhowin.append(3)
                straightwincheck.append(CPU2straight)
                straightcardwin.append(CPU2straightcard)
            else:
                CPU2fold = 0
        else:
            CPU2fold = 1

        if CPU3fold != 1: #if CPU3 didnt fold
            if CPU3straight >= 4: #if CPU3 has a straight
                straightwhowin.append(4)
                straightwincheck.append(CPU3straight)
                straightcardwin.append(CPU3straightcard)
            else:
                CPU3fold = 0
        else:
            CPU3fold = 1
        #--------------------------------------
        if straightwincheck.count(4) == 1: #if there is only 1 player with a straight
            winner.append(straightwhowin[0])
        elif straightwincheck.count(4) == 2: #if there is 2 players with a straight
            if straightcardwin[0] != straightcardwin[1]: #if they have a different straight
                testing = straightcardwin
                testingsuit = straightwhowin
                straightcardwin, straightwhowin= CombineSort(testing,testingsuit) #sort least to highest
                winner.append(straightwhowin[1])
            elif straightcardwin[0] == straightcardwin[1]: #if they have the same straight
                    winner.append(straightwhowin[0])
                    winner.append(straightwhowin[1])
            else:
                winner = [] #no winner
        elif straightwincheck.count(4) > 2: #if there are more than 2 players with a straight
            testing = straightcardwin
            testingsuit = straightwhowin
            straightcardwin, straightwhowin = CombineSort(testing,testingsuit) #sort least to highest
            sw = len(straightcardwin)
            if straightcardwin[sw-1] == straightcardwin[sw-2]: #if the last two players has the same straight
                winner.append(straightwhowin[sw-1])
                winner.append(straightwhowin[sw-2])
            else:
                winner.append(straightwhowin[sw-1])
        else:
            winner = [] #no winner
        if winner != []: #if there is a winner
            print "Player(s)", straightwhowin, "has a Straight"

    ##-----------------------------------------------------------------------------
    #Checking if anyone has a Triple to win the game

    triplewincheck = []
    triplewhowin = []
    triplecardwin =[]

    #------------------------------
    if winner == []: #if there is no winner
        if USERfold != 1: #if USER didnt fold
            if USERtriple >= 1: #if USER has a triple
                triplewhowin.append(1)
                if USERtriple == 2: #if USER has 2 triples
                    triplewincheck.append(1)
                    triplecardwin.append(USERtriplecard[1])
                else: #1 triple
                    triplewincheck.append(USERtriple)
                    triplecardwin.append(USERtriplecard[0])
            else:
                USERfold = 0
        else:
            USERfold = 1

        if CPU1fold != 1: #if CPU1 didnt fold
            if CPU1triple >= 1: #if CPU1 has a triple
                triplewhowin.append(2)
                if CPU1triple == 2: #if CPU1 has 2 triple
                    triplewincheck.append(1)
                    triplecardwin.append(CPU1triplecard[1])
                else: #1 triple
                    triplewincheck.append(CPU1triple)
                    triplecardwin.append(CPU1triplecard[0])
            else:
                CPU1fold = 0
        else:
            CPU1fold = 1

        if CPU2fold != 1: #if CPU2 didnt fold
            if CPU2triple == 1: #if CPU2 has a triple
                triplewhowin.append(3)
                if CPU2triple == 2: #if CPU2 has 2 triple
                    triplewincheck.append(1)
                    triplecardwin.append(CPU2triplecard[1])
                else: #1 triple
                    triplewincheck.append(CPU2triple)
                    triplecardwin.append(CPU2triplecard[0])
            else:
                CPU2fold = 0
        else:
            CPU2fold = 1

        if CPU3fold != 1: #if CPU3 didnt fold
            if CPU3triple == 1: #if CPU3 has a triple
                triplewhowin.append(4)
                if CPU3triple == 2: #if CPU3 has 2 triple
                    triplewincheck.append(1)
                    triplecardwin.append(CPU3triplecard[1])
                else: #1 triple
                    triplewincheck.append(CPU3triple)
                    triplecardwin.append(CPU3triplecard[0])
            else:
                CPU3fold = 0
        else:
            CPU3fold = 1
        #----------------------------------------
        if triplewincheck.count(1) == 1: #if there is only 1 player with a triple
            winner.append(triplewhowin[0])
        elif triplewincheck.count(1) == 2: #if there is 2 players with a triple
            if triplecardwin[0] != triplecardwin[1]: #if they have a different triple
                testing = triplecardwin
                testingsuit = triplewhowin
                triplecardwin, triplewhowin= CombineSort(testing,testingsuit) #sort least to highest
                winner.append(triplewhowin[1])
            elif triplecardwin[0] == triplecardwin[1]: #if they have the same triple
                    winner.append(triplewhowin[0])
                    winner.append(triplewhowin[1])
            else:
                winner = [] #no winner
        elif triplewincheck.count(1) > 2: #if there are more than 2 players with a triple
            testing = triplecardwin
            testingsuit = triplewhowin
            triplecardwin, triplewhowin = CombineSort(testing,testingsuit) #sort least to highest
            tw = len(triplecardwin)
            if triplecardwin[tw-1] == triplecardwin[tw-2]: #if the last 2 players has the same triple
                winner.append(triplewhowin[tw-1])
                winner.append(triplewhowin[tw-2])
            else:
                winner.append(triplewhowin[tw-1])
        else:
            winner = [] #no winner
        if triplewhowin != []: #if there is a winner
            print "Player(s)", triplewhowin, "has a Triple"
    ##else:
    ##    triplewincheck = []

    ##-----------------------------------------------------------------------------
    #Checking if anyone has Pair(s) to win the game

    pairwincheck = []
    pairwhowin = []
    paircardwin =[]

    #--------------------------
    if winner == []: #if there is no winner
        if USERfold != 1: #if USER didnt fold
            if USERpair >= 1: #if USER has a pair
                pairwhowin.append(1)
                if USERpair == 2: #if USER has 2 pair
                    pairwincheck.append(1)
                    paircardwin.append(USERpaircard[1])
                elif USERpair == 3: #if USER has 3 pair
                    pairwincheck.append(1)
                    paircardwin.append(USERpaircard[2])
                else: #1 pair
                    pairwincheck.append(USERpair)
                    paircardwin.append(USERpaircard[0])
            else:
                USERfold = 0
        else:
            USERfold = 1

        if CPU1fold != 1: #if CPU1 didnt fold
            if CPU1pair >= 1: #if CPU1 has a pair
                pairwhowin.append(2)
                if CPU1pair == 2: #if CPU1 has 2 pair
                    pairwincheck.append(1)
                    paircardwin.append(CPU1paircard[1])
                elif CPU1pair == 3: #if CPU1 has 3 pair
                    pairwincheck.append(1)
                    paircardwin.append(CPU1paircard[2])
                else: #1 pair
                    pairwincheck.append(CPU1pair)
                    paircardwin.append(CPU1paircard[0])
            else:
                CPU1fold = 0
        else:
            CPU1fold = 1

        if CPU2fold != 1: #if CPU2 didnt fold
            if CPU2pair >= 1: #if CPU2 has a pair
                pairwhowin.append(3)
                if CPU2pair == 2: #if CPU2 has 2 pair
                    pairwincheck.append(1)
                    paircardwin.append(CPU2paircard[1])
                elif CPU2pair == 3: #if CPU2 has 3 pair
                    pairwincheck.append(1)
                    paircardwin.append(CPU2paircard[2])
                else: #1 pair
                    pairwincheck.append(CPU2pair)
                    paircardwin.append(CPU2paircard[0])
            else:
                CPU2fold = 0
        else:
            CPU2fold = 1

        if CPU3fold != 1: #if CPU3 didnt fold
            if CPU3pair >= 1: #if CPU3 has a pair
                pairwhowin.append(4)
                if CPU3pair == 2: #if CPU3 has 2 pair
                    pairwincheck.append(1)
                    paircardwin.append(CPU3paircard[1])
                elif CPU3pair == 3: #if CPU3 has 3 pair
                    pairwincheck.append(2)
                    paircardwin.append(CPU3paircard[2])
                else: #1 pair
                    pairwincheck.append(CPU3pair)
                    paircardwin.append(CPU3paircard[0])
            else:
                CPU3fold = 0
        else:
            CPU3fold = 1
        #----------------------------------
        if pairwincheck.count(1) == 1: #if there is only 1 player with a pair
            winner.append(pairwhowin[0])
        elif pairwincheck.count(1) == 2: #if there is 2 players with a pair
            if paircardwin[0] != paircardwin[1]: #if they have a different pair
                testing = paircardwin
                testingsuit = pairwhowin
                paircardwin, pairwhowin= CombineSort(testing,testingsuit) #sort least to highest
                winner.append(pairwhowin[1])
            elif paircardwin[0] == paircardwin[1]: #if they have the same pair
                    winner.append(pairwhowin[0])
                    winner.append(pairwhowin[1])
            else:
                winner = [] #no winner
        elif pairwincheck.count(1) > 2: #if there are more than 2 players with pair
            testing = paircardwin
            testingsuit = pairwhowin
            paircardwin, pairwhowin = CombineSort(testing,testingsuit) #sort least to highest
            pw = len(paircardwin)
            if paircardwin[pw-1] == paircardwin[pw-2]: #if the last two players has the same pair
                winner.append(pairwhowin[pw-1])
                winner.append(pairwhowin[pw-2])
            else:
                winner.append(pairwhowin[pw-1])
        else:
            winner = [] #no winner
        if pairwhowin != []: #if there is a winner
            print "Player(s):", pairwhowin, "has a Pair"

    ##-----------------------------------------------------------------------------
    #Checking if anyone has a High Card to win the game

    highcardwhowin = []
    highsuitwin = []
    highcardwin =[]

    #---------------------
    if winner == []: #if there is no winner
        if USERfold != 1: #if USER didnt fold
            highcardwhowin.append(1)
            highsuitwin.append(USERhighsuit)
            highcardwin.append(USERhighcard)
        else:
            USERfold = 1

        if CPU1fold != 1: #if CPU1 didnt fold
            highcardwhowin.append(2)
            highsuitwin.append(CPU1highsuit)
            highcardwin.append(CPU1highcard)
        else:
            CPU1fold = 1

        if CPU2fold != 1: #if CPU2 didnt fold
            highcardwhowin.append(3)
            highsuitwin.append(CPU2highsuit)
            highcardwin.append(CPU2highcard)
        else:
            CPU2fold = 1

        if CPU3fold != 1: #if CPU3 didnt fold
            highcardwhowin.append(4)
            highsuitwin.append(CPU3highsuit)
            highcardwin.append(CPU3highcard)
        else:
            CPU3fold = 1
        #-------------------------------------
        if len(highcardwin) > 0: #if there are players with a highcard
            testing = highcardwin
            testingsuit = highsuitwin
            testingwho = highcardwhowin
            highcardwin, highsuitwin, highcardwhowin = WinCombineSort(testing,testingsuit,testingwho) #sort least to highest
            hcw = len(highcardwin)
            if highcardwin[hcw-1] == highcardwin[hcw-2]: #if the last two players has the same high card
                if highsuitwin[hcw-1] == highsuitwin[hcw-2]: #if the last two players has the same suit
                    winner.append(highcardwhowin[hcw-1])
                    winner.append(highcardwhowin[hcw-2])
                else:
                    winner.append(highcardwhowin[hcw-1])
            else:
                winner.append(highcardwhowin[hcw-1])
        else:
            winner = [] #no winner
        if highcardwhowin != []: #if there is a winner
            print "Player(s):", highcardwhowin, "has a High Card"

    ##-----------------------------------------------------------------------------
    #Show Cards

    print "----------------------------------------"
    print "Play Cards/Deck Cards:" #prints out all five cards
    print "Suits:", Playcardssuit
    print "Cards:", Playcards
    if USERfold == 0: #if user didnt fold
        print "Your Suits:", USERsuit
        print "Your Cards:", USER
    else:
        USERfold = 1
    if CPU1fold == 0: #if CPU1 didnt fold
        print "CPU1 Suits:", CPU1suit
        print "CPU1 Cards:", CPU1
    else:
        CPU1fold = 1
    if CPU2fold == 0: #if CPU2 didnt fold
        print "CPU2 Suits:", CPU2suit
        print "CPU2 Cards:", CPU2
    else:
        CPU2fold = 1
    if CPU3fold == 0: #if CPU3 didnt fold
        print "CPU3 Suits:", CPU3suit
        print "CPU3 Cards:", CPU3
    else:
        CPU3fold = 1

    ##-----------------------------------------------------------------------------
    #Winner
    whowin = ['blank','USER/You','CPU1','CPU2','CPU3']

    print "----------------------------------------"
    if len(winner)== 2: #if there are two players
        first = winner[0]
        second = winner [1]
        split = pool/2
        print "The Winner of this game is:", whowin[first], "and", whowin[second]
        print "Split Plot"
        print whowin[first],"wins:", split, "of", pool,"(The Pool)"
        if first == 1:
            umoney = umoney+split
            print "USER's money:", umoney
            USERwin = USERwin+1
        elif first == 2:
            c1 = c1+split
            print "CPU1's money:", c1
            CPU1win = CPU1win+1
        elif first == 3:
            c2 = c2+split
            print "CPU2's money:", c2
            CPU2win = CPU2win+1
        else:
            c3 = c3+split
            print "CPU3's money:", c3
            CPU3win = CPU3win+1
        print whowin[second],"wins:", pool-split, "of", pool,"(The Pool)"
        if second == 1:
            umoney = umoney+(pool-split)
            print "USER's money:", umoney
            USERwin = USERwin+1
        elif second == 2:
            c1 = c1+(pool-split)
            print "CPU1's money:", c1
            CPU1win = CPU1win+1
        elif second == 3:
            c2 = c2+(pool-split)
            print "CPU2's money:", c2
            CPU2win = CPU2win+1
        else:
            c3 = c3+(pool-split)
            print "CPU3's money:", c3
            CPU3win = CPU3win+1
    else:
        onewinner = winner[0] #if there is only 1 winner
        print "The Winner of this game is:", whowin[onewinner]
        print whowin[onewinner], "wins $", pool
        if onewinner == 1:
            umoney = umoney+pool
            print "USER's money:", umoney
            USERwin = USERwin+1
        elif onewinner == 2:
            c1 = c1+pool
            print "CPU1's money:", c1
            CPU1win = CPU1win+1
        elif onewinner == 3:
            c2 = c2+pool
            print "CPU2's money:", c2
            CPU2win = CPU2win+1
        else:
            c3 = c3+pool
            print "CPU3's money:", c3
            CPU3win = CPU3win+1

    ##-----------------------------------------------------------------------------
    #Asks if USER wants to continue playing

    gameplayed = gameplayed+1

    playagain = input ("Do you want to continue playing? (Press 1 to Continue! Press 2 to Stop Playing):")
    if playagain == 1: #continue to play another game
        if c1 <= 0 or c2 <= 0 or c3 <=0 or umoney <= 0: #if any computer or user does not have any more money left
            print "Someone has lose all of their money, unable to continue playing..."
            playing = 1
        else:
            CPU1 = []       #Clears variables for new game
            CPU1suit = []
            CPU1raise = 0
            CPU1bet = 0
            CPU1fold = 0

            CPU2 = []
            CPU2suit = []
            CPU2raise = 0
            CPU2bet = 0
            CPU2fold = 0

            CPU3 = []
            CPU3suit = []
            CPU3raise = 0
            CPU3bet = 0
            CPU3fold = 0

            USER = []
            USERsuit = []
            USERbet = 0
            USERfold = 0

            y = 0
            redraw = 0
            Playcards = []
            Playcardssuit = []
            pool = 0
            bet = 0
            CPUbasebet = 20
            winner = []
            playagain = 0

            quadnum = 0
            flushnum = 0
            triplenum = 0
            pairnum = 0

            CPU1testing = []
            CPU1testingsuit = []
            CPU1straightflush = 0
            CPU1straightflushsuit = 0
            CPU1straightflushcard = 0
            CPU1quad = 0
            CPU1quadcard = 0
            CPU1fullhouse = 0
            CPU1fullhousetriple = []
            CPU1fullhousepair = []
            CPU1flush = 0
            CPU1flushsuit = 0
            CPU1straight = 0
            CPU1straightcard = 0
            CPU1triple = 0
            CPU1triplecard = []
            CPU1pair = 0
            CPU1paircard = []
            CPU1highcard = []
            CPU1highsuit = []

            CPU2testing = []
            CPU2testingsuit = []
            CPU2straightflush = 0
            CPU2straightflushsuit = 0
            CPU2straightflushcard = 0
            CPU2quad = 0
            CPU2quadcard = 0
            CPU2fullhouse = 0
            CPU2fullhousetriple = []
            CPU2fullhousepair = []
            CPU2flush = 0
            CPU2flushsuit = 0
            CPU2straight = 0
            CPU2straightcard = 0
            CPU2triple = 0
            CPU2triplecard = []
            CPU2pair = 0
            CPU2paircard = []
            CPU2highcard = []
            CPU2highsuit = []

            CPU3testing = []
            CPU3testingsuit = []
            CPU3straightflush = 0
            CPU3straightflushsuit = 0
            CPU3straightflushcard = 0
            CPU3quad = 0
            CPU3quadcard = 0
            CPU3fullhouse = 0
            CPU3fullhousetriple = []
            CPU3fullhousepair = []
            CPU3flush = 0
            CPU3flushsuit = 0
            CPU3straight = 0
            CPU3straightcard = 0
            CPU3triple = 0
            CPU3triplecard = []
            CPU3pair = 0
            CPU3paircard = []
            CPU3highcard = []
            CPU3highsuit = []

            USERtesting = []
            USERtestingsuit = []
            USERstraightflush = 0
            USERstraightflushsuit = 0
            USERstraightflushcard = 0
            USERquad = 0
            USERquadcard = 0
            USERfullhouse = 0
            USERfullhousetriple = []
            USERfullhousepair = []
            USERflush = 0
            USERflushsuit = 0
            USERstraight = 0
            USERstraightcard = 0
            USERtriple = 0
            USERtriplecard = []
            USERpair = 0
            USERpaircard = []
            USERhighcard = []
            USERhighsuit = []

            highcardwhowin = []
            highsuitwin = []
            highcardwin =[]

            pairwincheck = []
            pairwhowin = []
            paircardwin =[]

            triplewincheck = []
            triplewhowin = []
            triplecardwin =[]

            straightwincheck = []
            straightwhowin = []
            straightcardwin =[]

            flushwincheck = []
            flushwhowin = []
            flushsuitwin =[]

            fullhousewincheck = []
            fullhousewhowin = []
            fullhousecardwin =[]
            fullhousecard2win = []

            quadwincheck = []
            quadwhowin = []
            quadcardwin =[]

            straightflushwincheck = []
            straightflushwhowin = []
            straightflushsuitwin = []
            straightflushcardwin =[]
            print "----------------------------------------"
    else:
        playing = 1

##-----------------------------------------------------------------------------
#Statistics

print
print "Statistics:"
print
print "You have won:", USERwin,"time(s) out of:", gameplayed, "game(s)"
print "CPU1 have won:", CPU1win, "time(s) out of:", gameplayed, "game(s)"
print "CPU2 have won:", CPU2win, "time(s) out of:", gameplayed, "game(s)"
print "CPU3 have won:", CPU3win, "time(s) out of:", gameplayed, "game(s)"

##-----------------------------------------------------------------------------
#Program end