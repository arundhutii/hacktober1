//c 1
#include<stdio.h>

struct Car {
    char brand[50];
    char model[50];
    int year;
};

int main()
{
    struct Car car1 = { "bmw","x5",1996,};
    return 0;
}