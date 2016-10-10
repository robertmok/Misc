def solution(S):

## Alternate to remove '-' and ' '
##    num = ""
##    for index in range(len(S)):
##        if (S[index] != ' ') & (S[index] != '-'):
##            #print "S index =", S[index]
##            num = num + S[index]
##    print num

    phone = ""
    #print length
    str1 = S.replace(" ","")
    str2 = str1.replace("-","")
    print str2
    length = len(str2)
    print "Length: ", length

    if (length == 1): #phone length of 1
        phone = str2

    elif (length % 3 == 1): #remaining 1
        print "Remaining 1"
        for index in range(length-2):
            phone = phone + str2[index]
            #print "Index = ", index
            if ((index+1) % 3 == 0):
                phone = phone + '-'
        phone = phone + '-' + str2[length-2] + str2[length-1]

    else:
        print "Remaining 0 or 2"
        for index in range(length):
            phone = phone + str2[index]
            #print "Index = ", index
            if ((index+1) % 3 == 0) & (index != length-1):
                #print "Index = ", (index+1) % 3
                phone = phone + '-'

    print "Phone:", phone
    return

if __name__ == '__main__':
    S = "00-44  48 5555 861    223"
    S2 = "   0-1--- 055"
    S3 = "---1  "
    solution(S)
    print "-----------------------------------------"
    solution(S2)
    print "-----------------------------------------"
    solution(S3)

















