#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define max(a,b) a > b ? a:b
#define _CRT_SECURE_NO_WARNINGS
char first[1001], second[1001];
int first_len, second_len;
int count[1001][1001];



int main()
{
    scanf("%s %s",first, second);
    first_len = strlen(first);
    second_len = strlen(second);
    for(int i = 0 ; i < first_len+1; i++){
        for(int j = 0; j < second_len+1; j++){
            if(i == 0 || j == 0)
                count[i][j] = 0;
            else if(first[i-1] == second[j-1])
                count[i][j] = count[i-1][j-1] + 1;
            else
                count[i][j] = max(count[i-1][j], count[i][j-1]);
        }
    }

   
    printf("%d", count[first_len][second_len]);
    
    return 0;
}