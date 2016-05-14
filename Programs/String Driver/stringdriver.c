#include <stdio.h>
#include <stdlib.h>
#include "MyString.h"

int main(void)
{
    List S1, S2, S3;
    if (InitializeList(&S1)) {
        printf("List S1 Created.\n");
        }
    else {
      printf("Unable to create list S1\n");
      return 1;
    }
    if (InitializeList(&S2)) {
        printf("List S2 Created.\n");
        }
    else {
      printf("Unable to create list S2\n");
      return 1;
    }
    if (InitializeList(&S3)) {
        printf("List S3 Created.\n");
        }
    else {
      printf("Unable to create list S3\n");
      return 1;
    }
    printf("Enter selection and arguments where\n");
    printf("[char] is one character, [pos] is an integer, and\n");
    printf("[String], [fromString] [toString] are S1, S2 or S3:\n");
    printf("1. InsertChar [char] [pos] [String]\n");
    printf("2. InsertString [fromString] [pos] [toString]\n");
    printf("3. DeleteChar [pos] [String]\n");
    printf("4. DeleteString [pos] [pos] [String]\n");
    printf("5. CopyString [toString] [pos] [pos] [pos] [fromString]\n");
    printf("6. ReverseString [String]\n");
    printf("7. PrintLength [String]\n");
    printf("8. PrintChar [pos] [String]\n");
    printf("9. PrintString [String]\n");
    printf("P. Print this menu\n");
    printf("X. Exit program\n");

    int quit = 0, pos = 0, len = 0;
    int String = 0, fromString = 0, toString = 0, Start = 0, End =0, first = 0, last = 0;
    char C, Char;
    char input[25];

while (quit == 0)
  {
    gets(input);
    if (input[0] == 'P')              //Print Menu
    {
        quit = 0;
        printf("Enter selection and arguments where\n");
        printf("[char] is one character, [pos] is an integer, and\n");
        printf("[String], [fromString] [toString] are S1, S2 or S3:\n");
        printf("1. InsertChar [char] [pos] [String]\n");
        printf("2. InsertString [fromString] [pos] [toString]\n");
        printf("3. DeleteChar [pos] [String]\n");
        printf("4. DeleteString [pos] [pos] [String]\n");
        printf("5. CopyString [toString] [pos] [pos] [pos] [fromString]\n");
        printf("6. ReverseString [String]\n");
        printf("7. PrintLength [String]\n");
        printf("8. PrintChar [pos] [String]\n");
        printf("9. PrintString [String]\n");
        printf("P. Print this menu\n");
        printf("X. Exit program\n");
    }
    else if (input[0] == 'X')        //Exit
        quit = 1;
    else if (input[0]-'0' == 1)      //Insert Char
    {
        quit = 0;
        Char = input[2];
        pos = input[4] - '0';
        String = input[7]-'0';
        if(String == 1)
        {
            Length(&len, S1);
            if(pos > 0 && pos <= len+1)
                InsertChar(Char, pos, &S1);
            else
                printf("**error**\n");
        }
        else if(String == 2)
        {
            Length(&len, S2);
            if(pos > 0 && pos <= len+1)
                InsertChar(Char, pos, &S2);
            else
                printf("**error**\n");
        }
        else if(String == 3)
        {
            Length(&len, S3);
            if(pos > 0 && pos <= len+1)
                InsertChar(Char, pos, &S3);
            else
                printf("**error**\n");
        }
        else
            printf("**error**\n");
    }
    else if (input[0]-'0' == 2)      //Insert String
    {
        quit = 0;
        fromString = input[3]-'0';
        toString = input[8]-'0';
        pos = input[5]-'0';
        if(fromString == toString)
            printf("**error**\n");
        if(fromString <= 3 && fromString >= 1 && toString <= 3 && toString >= 1)
        {
            Length(&len, toString);
            if(pos > 0 && pos <= len+1)
            {
                if(fromString == 1)
                {
                    if(toString == 2)
                        InsertString(&S1, pos, &S2);
                    else
                        InsertString(&S1, pos, &S3);
                }
                else if(fromString == 2)
                {
                    if(toString == 1)
                        InsertString(&S2, pos, &S1);
                    else
                        InsertString(&S2, pos, &S3);
                }
                else
                {
                    if(toString == 3)
                        InsertString(&S3, pos, &S1);
                    else
                        InsertString(&S3, pos, &S2);
                }
            }
        }
        else
                printf("**error**\n");
    }
    else if (input[0]-'0' == 3)      //Delete Char   ex. 3 1 S1
    {
        quit = 0;
        pos = input[2]-'0';
        String = input[5]-'0';
        if(String <= 3 && String >= 1)
        {
            if(String == 1)
            {
                Length(&len, S1);
                if(pos > 0 && pos <= len+1)
                    DeleteChar(pos, &S1);
                else
                    printf("**error**\n");
            }
            else if(String == 2)
             {
                Length(&len, S2);
                if(pos > 0 && pos <= len+1)
                    DeleteChar(pos, &S2);
                else
                    printf("**error**\n");
             }
            else
            {
                Length(&len, S3);
                if(pos > 0 && pos <= len+1)
                    DeleteChar(pos, &S3);
                else
                    printf("**error**\n");
            }
        }
        else
            printf("**error**\n");
    }
    else if (input[0]-'0' == 4)      //Delete String ex. 4 1 3 S1
    {
        quit = 0;
        first = input[2]-'0';
        last = input[4]-'0';
        String = input[7]-'0';
        if(String <= 3 && String >= 1)
        {
            if(String == 1)
            {
                Length(&len, S1);
                if(first > 0 && first <= len && last > 0 && last <= len)
                    DeleteString(first, last, &S1);
                else
                    printf("**error**\n");
            }
            else if(String == 2)
            {
                Length(&len, S2);
                if(first > 0 && first <= len && last > 0 && last <= len)
                    DeleteString(first, last, &S2);
                else
                    printf("**error**\n");
            }
            else
            {
                Length(&len, S3);
                if(first > 0 && first <= len && last > 0 && last <= len)
                    DeleteString(first, last, &S3);
                else
                    printf("**error**\n");
            }
        }
        else
            printf("**error**\n");
    }
    else if (input[0]-'0' == 5)      //Copy String ex. 5 S2 6 1 2 S1
    {
        quit = 0;
        toString = input[3]-'0';
        pos = input[5]-'0';
        Start = input[7]-'0';
        End = input[9]-'0';
        fromString = input[12]-'0';


    }
    else if (input[0]-'0' == 6)      //Reverse String ex. 6 S1
    {
        quit = 0;
        String = input[3];
        if(String <= 3 && String >= 1)
        {
            if(String == 1)
                ReverseString(&S1);
            else if(String == 2)
                ReverseString(&S2);
            else
                ReverseString(&S3);
        }
        else
            printf("**error**\n");
    }
    else if (input[0]-'0' == 7)      //Print Length  ex. 7 S1
    {
        quit = 0;
        String = input[3]-'0';
        if(String <= 3 && String >= 1)
        {
            if(String == 1)
            {
                Length(&len, S1);
                printf("%d\n", len);
            }
            else if(String == 2)
             {
                Length(&len, S2);
                printf("%d\n", len);
             }
            else
            {
                Length(&len, S3);
                printf("%d\n", len);
            }
        }
        else
            printf("**error**\n");
    }
    else if (input[0]-'0' == 8)   //Print Char  ex. 8 1 S1
    {
        quit = 0;
        pos = input[2]-'0';
        String = input[5]-'0';
        if(String <= 3 && String >= 1)
        {
            if(String == 1)
            {
                Length(&len, S1);
                if(pos > 0 && pos <= len+1)
                {
                    GetChar(&C, pos, &S1);
                    printf("%c\n", C);
                }
                else
                    printf("**error**\n");
            }
            else if(String == 2)
             {
                Length(&len, S2);
                if(pos > 0 && pos <= len+1)
                {
                    GetChar(&C, pos, &S2);
                    printf("%c\n", C);
                }
                else
                    printf("**error**\n");
             }
            else
            {
                Length(&len, S3);
                if(pos > 0 && pos <= len+1)
                {
                    GetChar(&C, pos, &S3);
                    printf("%c\n", C);
                }
                else
                    printf("**error**\n");
            }
        }
        else
            printf("**error**\n");
    }
    else if (input[0]-'0' == 9)   //Print String
    {
        quit = 0;
        String = input[3]-'0';
        if(String <= 3 && String >= 1)
        {
            if(String == 1)
                PrintString(S1);
            else if(String == 2)
                PrintString(S2);
            else
                PrintString(S3);
        }
        else
            printf("**error**\n");
    }
    else
        printf("**error**\n");

    pos = len = 0;
    String = fromString = toString = Start = End = first = last = 0;
  }
  return 0;
}
