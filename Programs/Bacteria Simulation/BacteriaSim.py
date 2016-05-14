#Bacteria Simulation
#Description: A program that simulates bacteria life according the following 3 rules:
# 1. An empty(dead) cell must have three live neighbours in order to give birth to a live cell.
# 2. Cells with four or more live neighbours die from over crowding. Cells with one or no live neighbours die from isolation.
# 3. Cells with two or three live neighbours survive for another generation.

import os
import random
import time
method = 0
disha = []
dishb =[]
dishc = []
dishx = []
lista = []
listb = []
num2 = 0
num3 = 0
position = 0
choice = 0
meth = 0
again = 0
repeat = 0
gen = 0
cells = 0
generation = 1
percent = 0
answer = 0
born = 0
dead = 0

#Program Starts
print "Welcome to Bacteria Life Simulation"
print "Please Select a Method to Input number of cells into Petri-Dish"
print "Method 1 (Randomly), Inputs a random number of cells into Petri-Dish"
print "Method 2 (Manually), You choose the position of the cells you like into Petri-Dish"
print "Enter 1 for Method 1 or 2 for Method 2:"
while meth == 0: #while "meth" is 0, continue doing the following
    method = input ("Choose your method:") #asks user to input a method
    if method == 1: #if method 1 is choosen do the following
        meth = 1 #stops the loop
        for count in range(1,226): #for 225 times, do the following
            num = random.randrange(0,11) #chooses a random number in range 0 and 11
            if num > 5: #if random number is bigger than 5, do the following
                num2 = 1
                disha.append(num2) #disha puts in num2 inside the list
            else:
                num2 = 0
                disha.append(num2) #disha puts in num2 inside the list
        dishb.extend(disha) #dishb puts in disha inside its list
    elif method == 2: #if method 2 is choosen, do the following
        meth = 1 #stops the loop
        for count in range (1,226): #for 225 times, do the following
            num3 = 0
            disha.append(num3) #disha puts in num3 inside the list
        for count in range (0,225): #for 224 times, do the following
            dishc.append(count) #dishc puts in count inside its list
        while repeat == 0: #while repeat is 0, continue
            print dishc[0:15],"                        ", disha[0:15] #prints out a section of dishc and a section of disha
            print dishc[15:30],"              ", disha[15:30]
            print dishc[30:45],"              ", disha[30:45]
            print dishc[45:60],"              ", disha[45:60]
            print dishc[60:75],"              ", disha[60:75]
            print dishc[75:90],"              ", disha[75:90]
            print dishc[90:105],"         ", disha[90:105]
            print dishc[105:120], disha[105:120]
            print dishc[120:135], disha[120:135]
            print dishc[135:150], disha[135:150]
            print dishc[150:165], disha[150:165]
            print dishc[165:180], disha[165:180]
            print dishc[180:195], disha[180:195]
            print dishc[195:210], disha[195:210]
            print dishc[210:225], disha[210:225]
            position = input ("Enter the position you like to put a cell in:") #asks user for the position of cell
            disha[position] = 1 #turn disha choosen position into 1
            dishb.extend(disha) #dishb puts disha inside its list
            print dishc[0:15],"                        ", disha[0:15] #prints out a section of dishc and a section of disha after the cells had been put in
            print dishc[15:30],"              ", disha[15:30]
            print dishc[30:45],"              ", disha[30:45]
            print dishc[45:60],"              ", disha[45:60]
            print dishc[60:75],"              ", disha[60:75]
            print dishc[75:90],"              ", disha[75:90]
            print dishc[90:105],"         ", disha[90:105]
            print dishc[105:120], disha[105:120]
            print dishc[120:135], disha[120:135]
            print dishc[135:150], disha[135:150]
            print dishc[150:165], disha[150:165]
            print dishc[165:180], disha[165:180]
            print dishc[180:195], disha[180:195]
            print dishc[195:210], disha[195:210]
            print dishc[210:225], disha[210:225]
            print
            print
            again = input("Would you like to input more cells? Press 1 to continue or Press 2 to stop:") #asks user if they want to continue inputing cells
            if again == 1: #if again is 1, do the following
                print '\n'*40 #clearscreen
            elif again == 2: #if again is 2, do the following
                repeat = 1
            else:
                print "Error"

print "Petri-Dish"

print disha[0:15],"1" #prints out a section of disha
print disha[15:30],"2"
print disha[30:45],"3"
print disha[45:60],"4"
print disha[60:75],"5"
print disha[75:90],"6"
print disha[90:105],"7"
print disha[105:120],"8"
print disha[120:135],"9"
print disha[135:150],"10"
print disha[150:165],"11"
print disha[165:180],"12"
print disha[180:195],"13"
print disha[195:210],"14"
print disha[210:225],"15"
print
begincells = disha.count(1) #keeps the number of "1"s in "begincells

os.system ("CLS")#clearscreen

while gen == 0: #while gen is 0, continue
    for count in range (0,226): #for 225 times, do the following.
#-----------------------------1st Row---------------------------------------
        if count == 0: #if count is 0, do the following
            if disha[count]==1: #if the position is 1, do the following
                if disha[count+1]+disha[count+15]+disha[count+16]>=2 and disha[count+1]+disha[count+15]+disha[count+16]<=3:
                    dishb[count]=1 #the position is still 1
                else:
                    dishb[count]=0 #the position is changed to 0
                    dead = dead+1 #adds 1 to "dead"
            elif disha[count]==0: #if the position is 0, do the following
                if disha[count+1]+disha[count+15]+disha[count+16]==3:
                    dishb[count]=1 #the position is changed to 1
                    born = born+1 #adds 1 to "born"
                else:
                    dishb[count]=0 #the position is still 0
        if count in range (1,14):
            if disha[count]==1:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]>=2 and disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count == 14:
            if disha[count]==1:
                if disha[count-1]+disha[count+14]+disha[count+15]>=2 and disha[count-1]+disha[count+14]+disha[count+15]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count-1]+disha[count+14]+disha[count+15]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
#-----------------------------2nd Row---------------------------------------
        if count == 15:
            if disha[count]==1:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]>=2 and disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count in range (16,29):
            if disha[count]==1:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]>=2 and disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count == 29:
            if disha[count]==1:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]>=2 and disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
#-----------------------------3rd Row---------------------------------------
        if count == 30:
            if disha[count]==1:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]>=2 and disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count in range (31,44):
            if disha[count]==1:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]>=2 and disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count == 44:
            if disha[count]==1:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]>=2 and disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
#-----------------------------4th Row---------------------------------------
        if count == 45:
            if disha[count]==1:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]>=2 and disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count+15]+dishb[count+16]+disha[count-14]+disha[count-15]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count in range (46,59):
            if disha[count]==1:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]>=2 and disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count == 59:
            if disha[count]==1:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]>=2 and disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
#-----------------------------5th Row---------------------------------------
        if count == 60:
            if disha[count]==1:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]>=2 and disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count in range (61,74):
            if disha[count]==1:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]>=2 and disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count == 74:
            if disha[count]==1:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]>=2 and disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
#-----------------------------6th Row---------------------------------------
        if count == 75:
            if disha[count]==1:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]>=2 and disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count in range (76,89):
            if disha[count]==1:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]>=2 and disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count == 89:
            if disha[count]==1:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]>=2 and disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
#-----------------------------7th Row---------------------------------------
        if count == 90:
            if disha[count]==1:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]>=2 and disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count in range (91,104):
            if disha[count]==1:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]>=2 and disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count == 104:
            if disha[count]==1:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]>=2 and disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
#-----------------------------8th Row--------------------------------------- CONTINUE HERE
        if count == 105:
            if disha[count]==1:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]>=2 and disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count in range (106,119):
            if disha[count]==1:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]>=2 and disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count == 119:
            if disha[count]==1:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]>=2 and disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
#-----------------------------9th Row---------------------------------------
        if count == 120:
            if disha[count]==1:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]>=2 and disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count in range (121,134):
            if disha[count]==1:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]>=2 and disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count == 134:
            if disha[count]==1:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]>=2 and disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
#-----------------------------10th Row---------------------------------------
        if count == 135:
            if disha[count]==1:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]>=2 and disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count in range (136,149):
            if disha[count]==1:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]>=2 and disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count == 149:
            if disha[count]==1:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]>=2 and disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
#-----------------------------11th Row---------------------------------------
        if count == 150:
            if disha[count]==1:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]>=2 and disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count in range (151,164):
            if disha[count]==1:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]>=2 and disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count == 164:
            if disha[count]==1:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]>=2 and disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
#-----------------------------12th Row---------------------------------------
        if count == 165:
            if disha[count]==1:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]>=2 and disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count in range (166,179):
            if disha[count]==1:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]>=2 and disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count == 179:
            if disha[count]==1:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]>=2 and disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
#-----------------------------13th Row---------------------------------------
        if count == 180:
            if disha[count]==1:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]>=2 and disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count in range (181,194):
            if disha[count]==1:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]>=2 and disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count == 194:
            if disha[count]==1:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]>=2 and disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
#-----------------------------14th Row---------------------------------------
        if count == 195:
            if disha[count]==1:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]>=2 and disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count in range (196,209):
            if disha[count]==1:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]>=2 and disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count-1]+disha[count+14]+disha[count+15]+disha[count+16]+disha[count-14]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count == 209:
            if disha[count]==1:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]>=2 and disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count-1]+disha[count+14]+disha[count+15]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
#-----------------------------15th Row---------------------------------------
        if count == 210:
            if disha[count]==1:
                if disha[count+1]+disha[count-14]+disha[count-15]>=2 and disha[count+1]+disha[count-14]+disha[count-15]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count-14]+disha[count-15]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count in range (211,224):
            if disha[count]==1:
                if disha[count+1]+disha[count-1]+disha[count-14]+disha[count-15]+disha[count-16]>=2 and disha[count+1]+disha[count-1]+disha[count-14]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count+1]+disha[count-1]+disha[count-14]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
        if count == 224:
            if disha[count]==1:
                if disha[count-1]+disha[count-15]+disha[count-16]>=2 and disha[count-1]+disha[count-15]+disha[count-16]<=3:
                    dishb[count]=1
                else:
                    dishb[count]=0
                    dead = dead+1
            elif disha[count]==0:
                if disha[count-1]+disha[count-15]+disha[count-16]==3:
                    dishb[count]=1
                    born = born+1
                else:
                    dishb[count]=0
    print dishb[0:15],"1" #prints out a section of dishb
    print dishb[15:30],"2"
    print dishb[30:45],"3"
    print dishb[45:60],"4"
    print dishb[60:75],"5"
    print dishb[75:90],"6"
    print dishb[90:105],"7"
    print dishb[105:120],"8"
    print dishb[120:135],"9"
    print dishb[135:150],"10"
    print dishb[150:165],"11"
    print dishb[165:180],"12"
    print dishb[180:195],"13"
    print dishb[195:210],"14"
    print dishb[210:225],"15"
    cells = dishb.count(1) #keep the count of "1"s in "cells
    disha = [] #clear disha
    disha.extend(dishb) #disha puts dishb into its list
    print "Number of Cells Alive:", cells #outputs the number of cells alive
    answer = '%.2f' % ((1.0*cells/begincells)*100) #calculates the percent of cells survived
    print "Percent of Cells Survived:", answer,"%" #outputs the percent of cells survived
    print "Generation:", generation #outputs the generation
    print "Number of Cells Born:", born #outputs the number of cells born
    print "Number of Cells Died:", dead #outputs the number of cells died
    dishx.append(born) #dishx puts born in its list
    dishx.append(dead) #dishx puts dead in its list
    dishx.append(cells) #dishx puts cells in its list
    if generation%2==0: #if the generation is an even number, do the following
        if dishx == listb and dishx == lista: #if dishx is equal to listb and dishx is equal to lista, do the following
            gen = 1 #stops loop
        else:
            dishx = [] #clear dishx
            lista = [] #clear lista
            lista.append(born) #lista puts in born in its list
            lista.append(dead) #lista puts in dead in its list
            lista.append(cells) #lista puts in cells in its list
            born = 0 #change born back to 0
            dead = 0 #change dead back to 0
            generation = generation+1 #adds one to generation
            time.sleep (0.2) #slows down by 0.2 seconds
            os.system ("CLS")#clear screen
    elif generation%2==1 or generation == 1: #if the generation is an odd number or equal to 1, do the following
        if dishx == lista and dishx == listb: #if dishx is equal to lista and dishx is equal to listb, do the following
            gen = 1 #stops the loop
        else:
            dishx = [] #clear dishx
            listb = [] #clear listb
            listb.append(born) #listb puts in born in its list
            listb.append(dead) #listb puts in dead in its list
            listb.append(cells) #listb puts in cells in its list
            born = 0 #change the born value to 0
            dead = 0 #change the dead value to 0
            generation = generation+1 #adds one to generation
            time.sleep (0.2) #slows down by 0.2 seconds
            os.system ("CLS")#clear screen

get = input ("Press any key to exit program:")
#program ends
