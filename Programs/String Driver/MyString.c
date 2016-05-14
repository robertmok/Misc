#include <stdio.h>
#include "stdlib.h"
#include "string.h"
#include "MyString.h"

int InitializeList (List *S) {
   NodeType *new = (NodeType *)malloc(sizeof(NodeType));
   if (new==NULL) return 0;
   new->info='#';
   new->left_link=new;
   new->right_link=new;
   (*S)=new;
   return 1;
}

/*inserts char X into position Pos of string S.*/
int InsertChar(char X, int Pos, List *S)
{
    int item = 0, i = 0;

    NodeType *new = (NodeType *)malloc(sizeof(NodeType));
    NodeType *point;
    point = (NodeType *)malloc(sizeof(NodeType));

    new->info = X;
    point = (*S)->right_link;
    for(i = 0; i <= Pos; i++)
    {
        point = point->right_link;
    }
    new->left_link = point->left_link;
    new->right_link = point;
    point->left_link->right_link = new;
    point->left_link = new;

    return 1;
}

/*copies String X into position Pos of string S.*/
int InsertString(List *S, int Pos, List *X)
{
    NodeType *point, *temp;
    point = (NodeType *)malloc(sizeof(NodeType));
    temp = (NodeType *)malloc(sizeof(NodeType));

    return 1;
}

/*Copies a substring of S into position Pos of string X.
  The substring is the substring of S from position start to position end inclusive.*/
int CopyString(List *X, int Pos, int start, int end, List *S)
{
    NodeType *point, *temp;
    point = (NodeType *)malloc(sizeof(NodeType));
    temp = (NodeType *)malloc(sizeof(NodeType));

    return 1;
}

/*deletes char in position Pos of string S.*/
int DeleteChar(int Pos, List *S)
{
    int i = 0;
    NodeType *point, *temp;
    point = (NodeType *)malloc(sizeof(NodeType));
    temp = (NodeType *)malloc(sizeof(NodeType));

    point = (*S)->right_link;
    for(i = 0; i < Pos; i++)
    {
        point = point->right_link;
    }
    temp = point->right_link;
    point->right_link = temp->right_link;
    temp->right_link->left_link = temp->left_link;
    free(temp);

    return 1;
}

/*deletes characters from position first to position last (inclusive) of S.*/
int DeleteString(int first, int last, List *S)
{
    NodeType *point, *temp;
    point = (NodeType *)malloc(sizeof(NodeType));
    temp = (NodeType *)malloc(sizeof(NodeType));

    point = (*S)->right_link;

    return 1;
}

/*reverses S by changing pointers*/
int ReverseString(List *S)
{

    return 1;
}

/*prints S as one string of characters followed by a newline.*/
int PrintString(List S)
{
    NodeType *point;
    if(EmptyList(S))
    {
        printf("**empty string**\n");
        return;
    }
    point = S->right_link;
    while(point != S)
    {
        printf("%c", point->info);
        point = point->right_link;
    }
    printf("\n");
    return 1;
}

/*loads C with the character at position Pos of S.*/
int GetChar(char *C, int Pos, List *S)
{
    int i = 0;
    NodeType *point;
    point = (NodeType *)malloc(sizeof(NodeType));
    point = (*S)->right_link;
    for(i = 0; i <= Pos; i++)
    {
        point = point->right_link;
    }
    *C = point->info;
    return 1;
}

/*loads len with the length of string S.*/
int Length(int *len, List S)
{
    NodeType *point;

    if(EmptyList(S))
    {
        *len = 0;
        return;
    }
    point = S->right_link;
    while(point != S)
    {
        *len = (*len) + 1;
        point = point->right_link;
    }
    return 1;
}

