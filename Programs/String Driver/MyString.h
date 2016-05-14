#include <stdio.h>
#include <stdlib.h>

typedef struct NodeTag {
  char info;
  struct NodeTag *left_link;
  struct NodeTag *right_link;
} NodeType;

typedef NodeType *List;

extern int Initialize();

extern int InsertChar(char X, int Pos, List *S);
    /*inserts char X into position Pos of string S. Characters are assigned new positions
      as necessary. */

extern int InsertString();
    /*copies String X into position Pos of string S. Characters in S are assigned new
      positions as necessary. X is unchanged */

extern int CopyString();
    /*Copies a substring of S into position Pos of string X. The substring is the
      substring of S from position start to position end inclusive.  S is unchanged. */

extern int DeleteChar();
    /*deletes char in position Pos of string S. Characters are assigned new positions as
      necessary. */

extern int DeleteString();
    /*deletes characters from position first to position last (inclusive) of S.
      Characters are assigned new positions as necessary. */

extern int ReverseString();
    /*reverses S by changing pointers only (NO new nodes are allocated)*/

extern int PrintString();
    /*prints S as one string of characters followed by a newline. S is unchanged*/

extern int GetChar();
    /*loads C with the character at position Pos of S. S is unchanged*/

extern int Length();
    /*loads len with the length of string S. S is unchanged*/
