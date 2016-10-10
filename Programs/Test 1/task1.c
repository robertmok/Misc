#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * Solution(char *S, size_t length){
    printf("%s\n", S);
    char *str = (char*)malloc(length * sizeof(char)); //dynamic allocate size
    strcpy(str,S);
    printf("S= %s, Str= %s\n", S, str);
    char *phone = (char*)malloc(length * sizeof(char));
    char *str2 = (char*)malloc(length * sizeof(char));
    int len;
    int i;
    int count = 0;
    len = strlen(str);
    printf("Length: %d\n", len);
    for(i = 0; i < len; i++){ //remove dash and space
        if (str[i] != '-' && str[i] != ' '){
            //printf("%c", str[i]);
            str2[count] = str[i];
            count++;
        }
    }
    str2[count] = '\0'; //end string
    printf("\n");
    printf("Str2 %s\n", str2);
    int len2 = strlen(str2);
    printf("Len2 = %d\n", len2);
    //if length 1
    if (len2 == 1){
        strcpy(phone,str2);
    }
    //if remaining 1
    else if (len2 % 3 == 1){
        printf("Remaining 1 \n");
        count = 0;
        for (i = 0; i < (len2-2); i++){
            phone[count] = str2[i];
            count++;
            if ((i+1) % 3 == 0){
                phone[count] = '-';
                count++;
            }
        }
        phone[count] = '-';
        count++;
        phone[count] = str2[len2-2];
        count++;
        phone[count] = str2[len2-1];
        count++;
        phone[count] = '\0';
    }
    //if remaining 0 or 2
    else {
        printf("Remaining 0 or 2 \n");
        count = 0;
        for (i = 0; i < (len2); i++){
            phone[count] = str2[i];
            count++;
            if ((i+1) % 3 == 0 && (i+1) != len2){
                phone[count] = '-';
                count++;
            }
        }
        phone[count] = '\0';
    }
    printf("Phone: %s \n", phone);
    return phone;
}



int main(void){
    char S[] = "   1------23- -4 56 7-8 9 ";
    char S2[] = "   1------";
    char S3[] = " 1 ---- 2-3- 4  -5--67";
    char *ans = (char*)malloc(strlen(S) * sizeof(char));

    ans = Solution(&S, sizeof (S) / sizeof (*S)); //input size of array
    printf("ans= %s\n------------------------------ \n", ans);

    ans = Solution(&S2, sizeof (S2) / sizeof (*S2)); //input size of array
    printf("ans= %s\n------------------------------ \n", ans);

    ans = Solution(&S3, sizeof (S3) / sizeof (*S3)); //input size of array
    printf("ans= %s\n------------------------------ \n", ans);

    return 0;
}
