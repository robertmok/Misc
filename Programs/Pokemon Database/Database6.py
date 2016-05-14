#Description: A friendly user pokemon database with searching in all fields, inserting
#             a record, saving a record, multi view and single view and editing a
#             a record.
#Note: the fields are numbered from 0 not 1

##-----------------------------------------------------------------------------
#Reading the Database
import os
import pickle
p = open('testpdatabase.bin', 'rb') #Test Reads the file with the records in it
pokemon = pickle.load(p) #Assign the records to a variable
#print pokemon #Check
p.close() #close the file

#pokemon = pickle.load(open("pdatabase.bin")) #incase the "Test" database is messed up
#this is used to overwrite the messed up "Test" database

##-----------------------------------------------------------------------------
#Functions

def PokeSort (testing): #sorting the records by number
    temp = 0
    x = 0
    y = 1
    cards = len(testing)
    card = cards
    for count in range (0,card-1):
        for count in range (0,cards-1):
            if testing[x][1]>testing[y][1]:
                temp = testing[x]
                testing[x]= testing[y]
                testing[y]= temp
                x = x+1
                y = y+1
                #print testing #Check
            elif testing[x][1]<testing[y][1]:
                x = x+1
                y = y+1
        x = 0
        y = 1
    return testing

def PokeLetter (Iput,pokemon,field): #searching a record by a letter or word
    word = len (pokemon)
    search = len (Iput)
    same = 0
    list1 = []
    list2 = []
    list3 = []
    results = []
    #print word, 'Word'
    #print search, 'Search'
    for letter1 in Iput:
        list1 += letter1
    for count in range(word):
        for letter1 in pokemon[count][field]:
            list2 += letter1
        #print list2 #Check
        list3.append(list2)
        #print list3 #Check
        list2 = []
    for x in range(word):
        for count in range(search):
            #print count, "Count"
            if x < word:
                if len(list3[x]) >= search:
                    if list3[x][count] == list1[count]:
                        #print list3[x][count] #Check
                        same = same+1
                        #print same, "Same" #Check
                        #print search, "Search" #Check
                        #print list3[x] #Check
                        if same == search:
                            results.append(x)
                            same = 0
                        else:
                            same = same
                    else:
                        #print "next" #Check
                        same = 0
                        x = x+1
                else:
                    same = same+0
            else:
                same = same+0
    #print same #Check
    return results

def PokeNum (Iput,pokemon,field): #searching a record by a number
    num = len (pokemon)
    num = num-1
    results = []
    for count in range(num):
        if Iput == pokemon[count][field]:
            results.append(count)
        else:
            num = num
    return results

def PokeTypes (type1,type2,pokemon,field1,field2): #searching in type 1 and type 2 for records
    word = len (pokemon)
    search = len (type1)
    same = 0
    list1 = []
    list2 = []
    list3 = []
    result1 = []
    for letter1 in type1:
        list1 += letter1
    for count in range(word):
        for letter1 in pokemon[count][field1]:
            list2 += letter1
        #print list2 #Check
        list3.append(list2)
        #print list3 #Check
        list2 = []
    for x in range(word):
        for count in range(search):
            if x < word:
                if len(list3[x]) >= search:
                    if list3[x][count] == list1[count]:
                        print list3[x][count]
                        same = same+1
                        #print same, "Same" #Check
                        #print search, "Search" #Check
                        #print list3[x] #Check
                        if same == search:
                            result1.append(x)
                            same = 0
                        else:
                            same = same
                    else:
                        #print "next" #Check
                        same = 0
                        x = x+1
                else:
                    same = same+0
            else:
                same = same+0
    #print same #Check
    #print result1, 'result 1'#Check
    #filters the records by searching in field type 2
    word2 = len (result1)
    search2 = len(type2)
    same1 = 0
    list4 = []
    list5 = []
    list6 = []
    result2 = []
    for letter3 in type2:
        list4 += letter3
        #print list4, "list 4" #Check
    for count in range(word2):
        for letter4 in pokemon[result1[count]][field2]:
            #print pokemon[result1[count]][field2] #Check
            list5 += letter4
        #print list5, 'list 5'#Check
        list6.append(list5)
        #print list6,'list 6'#Check
        list5 = []
    for y in range(word2):
        for count in range(search2):
            if y < word:
                if len(list6[y]) >= search2:
                    if list6[y][count] == list4[count]:
                        #print list6[y][count] #Check
                        same1 = same1+1
                        #print same1, "Same 1" #Check
                        #print search2, "Search 2" #Check
                        print list6[y]
                        if same1 == search2:
                            result2.append(result1[y])
                            same1 = 0
                        else:
                            same1 = same1
                    else:
                        #print "next 1" #Check
                        same1 = 0
                        y = y+1
                else:
                    same1 = same1+0
            else:
                same1 = same1+0
    #print same1 #Check
    return result2

def PokeEvol (pokemon, field, Iput): #search records by a number
    num = len(pokemon)
    results = []
    for count in range(num):
        if Iput == pokemon[count][field]:
            results.append(count)
        else:
            num = num
    return results

def AlphaSort (testing): #sorting by alphabet
    temp = 0
    x = 0
    y = 1
    cards = len(testing)
    card = cards
    for count in range (0,card-1):
        for count in range (0,cards-1):
            if testing[x][0]>testing[y][0]:
                temp = testing[x]
                testing[x]= testing[y]
                testing[y]= temp
                x = x+1
                y = y+1
                #print testing #Check
            elif testing[x][0]<testing[y][0]:
                x = x+1
                y = y+1

        x = 0
        y = 1
    return testing

##-----------------------------------------------------------------------------
#Variables

choice1 = 0
choice2 = 0
results = []
again1 = 0
again2 = 0
again3 = 0
again4 = 0
again5 = 0
again6 = 0
again7 = 0

##-----------------------------------------------------------------------------
print "00000 0000 0  0 0000 00       00 0000 00    0   0000  0000"
print "0   0 0  0 0 0  0    0 0     0 0 0  0 0 0   0   0   0 0  0"
print "00000 0  0 00   0000 0  0   0  0 0  0 0  0  0   0   0 0000"
print "0     0  0 0 0  0    0   0 0   0 0  0 0   0 0   0   0 0  0  000"
print "0     0000 0  0 0000 0    0    0 0000 0    00   0000  0000  000"
print
print"     `;-.          ___,"
print'       `.`\_...._/`.-"`'
print"         \        /      ,"
print"         /()   () \    .' `-._"
print"        |)  .    ()\  /   _.'"
print"        \  -'-     ,; '. <"
print"         ;.__     ,;|   > \'"
print"        / ,    / ,  |.-'.-'"
print"       (_/    (_/ ,;|.<`"
print"         \    ,     ;-`"
print"          >   \    /"
print"         (_,-'`> .'"
print"              (_,'"
print
print

##-----------------------------------------------------------------------------
#Inserting a New Record

choice1 = input("Press 1 to Insert A New Record or Press 2 to Search a Pokemon:")
if choice1 == 1:
    name = raw_input("The Pokemon Name is:")
    pokemon.append([name]) #places the pokemon name into a seperate array in the array
    number = input("The Pokemon Number is:")
    array = len(pokemon) #counts the records in the array
    array = array-1 #python starts from 0
    #Note: The pokemon name is saved at the end of the array
    pokemon[array].append(number)
    #Finds where it is in the array so that the following information is placed into the same place
    type1 = raw_input("The Type 1 of your Pokemon is:")
    pokemon[array].append(type1)
    types = input("Is there a Type 2 of your Pokemon? Press 1 if there is a Type 2 or Press 2 if there is no Type 2:")
    if types == 1:
        type2 = raw_input("The Type 2 of your Pokemon is:")
        pokemon[array].append(type2)
    elif types == 2:
        pokemon[array].append('N/A')
    evolution = input("Is there a Evolution Level of your Pokemon? Press 1 if there is, Press 2 if there isn't:")
    if evolution == 1:
        evolev = input("The Evolution Level of the Pokemon is:")
        pokemon[array].append(evolev)
    elif evolution == 2:
        pokemon[array].append("N/A")
    ability = raw_input("The Ability of the Pokemon is:")
    pokemon[array].append(ability)
    habitat = raw_input("The Habitat of the Pokemon is:")
    pokemon[array].append(habitat)
    colour = raw_input("The Colour of the Pokemon is:")
    pokemon[array].append(colour)
    #print pokemon #Check

##-----------------------------------------------------------------------------
#Sorting the pokemon

elif choice1 == 2:
    sorting = input ("Do you want to see the records by alphabet or by pokemon number after searching: Press 1 to see by alphabet or Press 2 to see by pokemon number:")
    if sorting == 1:
        #Sorting records by alphabet function
        testing = pokemon
        pokemon = AlphaSort (testing)
        #print pokemon #Check
    elif sorting == 2:
        #Sorting records by number function
        testing = pokemon
        pokemon = PokeSort (testing)
    else:
        print "Error in sorting"

##-----------------------------------------------------------------------------
#Searching a Pokemon
    print "Press 1 to search in Pokemon Name"
    print "Press 2 to search in Pokemon Number"
    print "Press 3 to search in Pokemon Type"
    print "Press 4 to search in Pokemon Evolution Level"
    print "Press 5 to search in Pokemon Ability"
    print "Press 6 to search in Pokemon Habitat"
    print "Press 7 to search in Pokemon Colour"
    choice2 = input("Which of the 7 fields would you like to search by?:")
    if choice2 == 1: #search in field 0
        while again1 == 0:
            Sname = raw_input("Enter the name of a Pokemon or first letters of the name:")
            for count in range(0,1):
                #Searching records by letter or word function
                field = 0
                Iput = Sname
                results = PokeLetter(Iput, pokemon, field) #keep the results into the results array
            #print results #Check
            if results == []: #results will be kept into the results array, if the array is empty there are no results
                print "There are no pokemon related to your search..."
                A1 = input("Would you like to search another name? Press 1 to Search or Press 2 to Quit:")
                if A1 == 1:
                    again1 = 0
                else:
                    again1 = 1
            else:
                again1 = 1
    elif choice2 == 2: #search in field 1
        while again2 == 0:
            Snumber = input("Enter the Pokemon Number:")
            for count in range(0,1):
                #Search by a number function
                Iput = Snumber
                field = 1
                results = PokeNum(Iput,pokemon,field) #keep the results into the results array
            #print results #Check
            if results == []: #results will be kept into the results array, if the array is empty there are no results
                print "There are no pokemon related to your search..."
                A2 = input("Would you like to search another number? Press 1 to Search or Press 2 to Quit:")
                if A2 == 1:
                    again2 = 0
                else:
                    again2 = 1
            else:
                again2 = 1
    elif choice2 == 3: #search in field 2
        while again3 == 0:
            Stypes = input("Do you want to search only 1 type or both types? Press 1 to search 1 type or Press 1 to search 2 types:")
            if Stypes == 1: #searching in  1 field
                Otype = input("Do you want to search in type 1 or in type 2? Press 1 to search in type 1 or Press 2 to search in type 2:")
                if Otype == 1: #searching in field 2
                    Stype1 = raw_input("Enter a Type for Type 1:")
                    #searching by a letter or word function
                    field = 2
                    Iput = Stype1
                    results = PokeLetter(Iput, pokemon, field) #keep the results into the results array
                    #print results #Check
                elif Otype == 2: #searching in field 3
                    Stype2 = raw_input("Enter a Type for Type 2:")
                    #searching by a letter or word function
                    field = 3
                    Iput = Stype2
                    results = PokeLetter(Iput,pokemon,field) #keep the results into the results array
                    #print results #Check
            elif Stypes == 2: #searching in 2 field
                StypeB1 = raw_input("Enter a Type for Type 1:")
                StypeB2 = raw_input("Enter a Type for Type 2:")
                #searching in 2 types/field function
                field1 = 2
                field2 = 3
                type1 = StypeB1
                type2 = StypeB2
                results = PokeTypes (type1,type2,pokemon,field1,field2) #keep the results into the results array
                #print results #Check
            else:
                print "Error in Searching Types"
            if results == []: #results will be kept into the results array, if the array is empty there are no results
                print "There are no pokemon related to your search..."
                A3 = input("Would you like to search another type? Press 1 to Search or Press 2 to Quit:")
                if A3 == 1:
                    again3 = 0
                else:
                    again3 = 1
            else:
                again3 = 1
    elif choice2 == 4: #searching in field 4
        while again4 == 0:
            print "-----------------------------------------------------"
            print "Enter a Number for Pokemon Evolution Level, Press 1"
            print "Search MAX Evolution Level Pokemons, Press 2"
            print "Search Special Evolution Level Pokemons, Press 3"
            print "Search No or (N/A) Evolution Level Pokemons, Press 4"
            evolchoice = input ("Your choice for searching in Evolution Level is:")
            if evolchoice == 1: #searching by a number
                Sevol = input("Enter the Evolution Level:")
                for count in range(0,1):
                    #searching by a number function
                    Iput = Sevol
                    field = 4
                    results = PokeNum(Iput,pokemon,field) #keep the results into the results array
                #print results #Check
            elif evolchoice == 2: #searching by a word
                for count in range(0,1):
                    #searching by a word function
                    Sevol2 = 'MAX'
                    field = 4
                    Iput = Sevol2
                    results = PokeEvol (pokemon,field,Iput) #keep the results into the results array
                print results #Check
            elif evolchoice == 3: #searching by a word
                for count in range(0,1):
                    #searching by a word function
                    Sevol3 = 'Special'
                    field = 4
                    Iput = Sevol3
                    results = PokeEvol (pokemon,field,Iput) #keep the results into the results array
                #print results #Check
            elif evolchoice == 4: #searching by a word
                for count in range(0,1):
                    #searching by a word function
                    Sevol4 = 'N/A'
                    field = 4
                    Iput = Sevol4
                    results = PokeEvol (pokemon,field,Iput) #keep the results into the results array
                #print results #Check
            else:
                print "Error in Searching Evolution Level"
            if results == []: #results will be kept into the results array, if the array is empty there are no results
                print "There are no pokemon related to your search..."
                A4 = input("Would you like to search another evolution level? Press 1 to Search or Press 2 to Quit:")
                if A4 == 1:
                    again4 = 0
                else:
                    again4 = 1
            else:
                again4 = 1
    elif choice2 == 5: #searhing in field 5
        while again5 == 0:
            Sability = raw_input("Enter the Ability of a Pokemon or first letters of the Ability:")
            for count in range(0,1):
                #searching by a letter or word function
                field = 5
                Iput = Sability
                results = PokeLetter(Iput, pokemon, field) #keep the results into the results array
            #print results #Check
            if results == []: #results will be kept into the results array, if the array is empty there are no results
                print "There are no pokemon related to your search..."
                A5 = input("Would you like to search another ability? Press 1 to Search or Press 2 to Quit:")
                if A5 == 1:
                    again5 = 0
                else:
                    again5 = 1
            else:
                again5 = 1
    elif choice2 == 6: #seaching in field 6
        while again6 == 0:
            Shabitat = raw_input("Enter the Habitat of a Pokemon or first letters of the Habitat:")
            for count in range(0,1):
                #searching by a letter or word function
                field = 6
                Iput = Shabitat
                results = PokeLetter(Iput, pokemon, field) #keep the results into the results array
            #print results #Check
            if results == []: #results will be kept into the results array, if the array is empty there are no results
                print "There are no pokemon related to your search..."
                A6 = input("Would you like to search another habitat? Press 1 to Search or Press 2 to Quit:")
                if A6 == 1:
                    again6 = 0
                else:
                    again6 = 1
            else:
                again6 = 1
    elif choice2 == 7: #searching in field 7
        while again7 == 0:
            Scolour = raw_input("Enter the Colour of a Pokemon or first letters of the Colour:")
            for count in range(0,1):
                #searching by a letter or word function
                field = 7
                Iput = Scolour
                results = PokeLetter(Iput, pokemon, field) #keep the results into the results array
            #print results #Check
            if results == []: #results will be kept into the results array, if the array is empty there are no results
                print "There are no pokemon related to your search..."
                A7 = input("Would you like to search another colour? Press 1 to Search or Press 2 to Quit:")
                if A7 == 1:
                    again7 = 0
                else:
                    again7 = 1
            else:
                again7 = 1
    else:
        print "Error in Search"

##-----------------------------------------------------------------------------
#Viewing Mode
rs = len(results) #count the number of thing in the array and keeps the number into "rs" variable
wrong = 0
vmore = 0
delchoice = 0

while vmore == 0:
    if results != []: #if the results array is not empty, do the following
        print "-----------------------------------------------------"
        print "There are a total of:", rs,"result(s) to your search."
        print
        choice3 = input("Do you want to see all results or separately? Press 1 to see all or Press 2 to see separately:")
        if choice3 == 1:
            print "Results Number...........Pokemon....Pokemon Number"
            for count in range(rs):
                print count+1,".....................",pokemon[results[count]][0:2]
            choice3 = 2
            print
        if choice3 == 2:
            while wrong == 0:
                view = input("Type in the results number that you want see:")
                if view > rs or view < 1: #if the "view" is greater than "rs" or "view is less than 1, do the following
                    print "Your results number was not found..."
                    print "Please choose another results number."
                    wrong = 0
                elif pokemon[results[view-1]] == []: #if the array chosen to see is empty, do the following
                    print "-----------------------------------------------------"
                    print "The record you want to see was deleted!"
                    print "Please choose another result to see or quit."
                    delchoice = input("Press 1 to view another result or Press 2 to Quit:")
                    if delchoice == 1:
                        wrong = 0
                    elif delchoice == 2:
                        vmore = 1
                        wrong = 1
                    else:
                        print "Error in seeing a deleted result"
                else:
                    wrong = 1

        if delchoice == 0:
##-----------------------------------------------------------------------------
    #View Files
            print "-----------------------------------------------------"
            print "Currently Viewing Result:", view
            print
            print "Pokemon Name:           ", pokemon[results[view-1]][0]
            print "Pokemon Number:         ", pokemon[results[view-1]][1]
            print "Pokemon Type 1:         ", pokemon[results[view-1]][2]
            print "Pokemon Type 2:         ", pokemon[results[view-1]][3]
            print "Pokemon Evolution Level:", pokemon[results[view-1]][4]
            print "Pokemon Ability:        ", pokemon[results[view-1]][5]
            print "Pokemon Habitat:        ", pokemon[results[view-1]][6]
            print "Pokemon Colour:         ", pokemon[results[view-1]][7]
            print
    ##-----------------------------------------------------------------------------
        #Choices
            print "-----------------------------------------------------"
            print "Press 1 to Edit the Current Record"
            print "Press 2 to Save the Current Record"
            print "Press 3 to Delete the Current Record"
            print "Press 4 to View another Record"
            print "Press 5 to Quit"
            choice4 = input("Your choice is:")
            if choice4 == 1: #Edit the record
                edit1 = input("Would you like to Edit the Pokemon Name? Press 1 to Edit, Press 2 to Continue:")
                if edit1 == 1:
                    edname = raw_input("Pokemon Name change to:")
                    pokemon[results[view-1]][0] = edname #change/overwrite the object in the array with "edname"
                edit2 = input("Would you like to Edit the Pokemon Number? Press 1 to Edit, Press 2 to Coninue:")
                if edit2 == 1:
                    ednum = input("Pokemon Number change to:")
                    pokemon[results[view-1]][1] = ednum #change/overwrite the object in the array with "ednum"
                edit3 = input("Would you like to Edit the Pokemon Type 1? Press 1 to Edit, Press 2 to Continue:")
                if edit3 == 1:
                    edtype1 = raw_input("Pokemon Type 1 change to:")
                    pokemon[results[view-1]][2] = edtype1 #change/overwrite the object in the array with "etype1"
                edit4 = input("Would you like to Edit the Pokemon Type 2? Press 1 to Edit, Press 2 to Continue:")
                if edit4 == 1:
                    edtype2 = raw_input("Pokemon Type 2 change to:")
                    pokemon[results[view-1]][3] = edtype2 #change/overwrite the object in the array with "etype2"
                edit5 = input("Would you like to Edit the Pokemon Evolution Level? Press 1 to Edit, Press 2 to Continue:")
                if edit5 == 1:
                    edevol1 = input("Do you want to change the Evolution Level to a number or word? Press 1 for a Number, Press 2 for a Word:")
                    if edevol1 == 1:
                        edevol2 = input("Pokmon Evolution Level change to (Number):")
                        pokemon[results[view-1]][4] = edevol2 #change/overwrite the object in the array with "edevol2"
                    elif edevol1 == 2:
                        edevol3 = raw_input("Pokemon Evolution Level change to (Word):")
                        pokemon[results[view-1]][4] = edevol3 #change/overwrite the object in the array with "edevol3"
                    else:
                        print "Error in Editing Evolution Level"
                edit6 = input("Would you like to Edit the Pokemon Ability? Press 1 to Edit, Press 2 to Continue:")
                if edit6 == 1:
                    edability = raw_input("Pokemon Ability change to:")
                    pokemon[results[view-1]][5] = edability #change/overwrite the object in the array with "edability"
                edit7 = input("Would you like to Edit the Pokemon Habitat? Press 1 to Edit, Press 2 to Continue:")
                if edit7 == 1:
                    edhabitat = raw_input("Pokemon Habitat change to:")
                    pokemon[results[view-1]][6] = edhabitat #change/overwrite the object in the array with "edhabitat"
                edit8 = input("Would you like to Edit the Pokemon Colour? Press 1 to Edit, Press 2 to Continue:")
                if edit8 == 1:
                    edcolour = raw_input("Pokemon Colour Change to:")
                    pokemon[results[view-1]][7] = edcolour #change/overwrite the object in the array with "edcolour"
            elif choice4 == 2: #Saves the record into a binary file
                pickle.dump(pokemon[results[view-1]], open (raw_input('Enter a filename: ').strip('.bin') + '.bin','wb'))
                #Asks for a name you want your save file to be called and saves the record into the binary file
            elif choice4 == 3: #Deletes the record
                Cdelete = input("Are you sure you want to delete this record?!?! Press 1 to Delete, Press 2 to Cancel:")
                if Cdelete == 1:
                    pokemon[results[view-1]] = [] #Emptys the information in the selected array in the array
                    #print pokemon #Check
                elif Cdelete == 2: #Cancel deleting the record
                    print "The record is not deleted!"
                else:
                    print "Error in Deleting Record"
            elif choice4 == 4: #User can view another record
                vmore = 0
                choice3 = 0
                wrong = 0
                view = 0
                choice4 = 0
            elif choice4 == 5: #Quits the program
                vmore = 1
                print "-----------------------------------------------------"
                print "Thank you for using Pokemon Database!"
            else:
                vmore = 1
                print "Error in Choices"
        else: #Quits the program
            vmore = 1
            choice4 = 5
            print "-----------------------------------------------------"
            print "Thank you for using Pokemon Database!"
    else:
        vmore = 1
    #print choice4, "choice4" #Check

    if choice1 != 1: #if user didnt select "insert a new record" at the beginning, do the following
        if choice4 == 1 or choice4 == 2 or choice4 == 3: #if the user didnt quit the program
            viewmore = input("Would you like to view another record?: Press 1 to View, Press 2 to Quit:")
            if viewmore == 1: #User can continue to see the other results
                vmore = 0
                choice3 = 0
                wrong = 0
                view = 0
                choice4 = 0
            elif viewmore == 2: #Quits the program
                vmore = 1
                print "-----------------------------------------------------"
                print "Thank you for using Pokemon Database!"
            else:
                vmore = 1
                print "Error in View More Records"
        elif choice4 == 5: #if the user already quited the program, do the following
            vmore = 1 #ends the loop
        else:
            vmore = 0 #loop continues
    else:
        vmore = 1 #ends the loop

##-----------------------------------------------------------------------------
#Updating Database
update = []

update.extend(pokemon) #put the "Changed" database into the update array

#print len(pokemon) #Check

for count in range(len(pokemon)):
    #print pokemon[count] #Check
    if pokemon[count]== []: #if the record's information was empty/deleted by the user, do the following
        update.remove(update[count]) #deletes the "emptied record" in the array
    else:
        nothing = 0

pokemon = [] #clears the pokemon array
pokemon.extend(update) #keeps the "update" array that was changed above, into pokemon array
#print pokemon #Check
#print update #Check

#print pokemon #Check
#Sorting by number function (default)
testing = pokemon
pokemon = PokeSort (testing)

#---------------------------------------
pread = open('testpdatabase.bin', 'wb') #Opens/reads the file that the records were kept in
pickle.dump(pokemon, pread) #Overwrites the records in the binary file with the "changed" records
pread.close() #Close the file

#pickle.dump(pokemon,open("testdatabase.bin", "wb")) #Checking

get = input("Press any key to exit program!")
##-----------------------------------------------------------------------------
#Program ends

