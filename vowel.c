#include <stdio.h>

int main()
{
    char p;
    scanf("%c",&p);
    if((p=='a')||(p=='e')||(p=='i')||(p=='o')||(p=='u'))
    printf("Vowel");
    else if(p>='a' && p<='z')
    printf("Consonant");
    else
    printf("Invalid");
    return 0;
}
