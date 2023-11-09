#include <stdio.h>
#include <time.h>
#include <unistd.h>
#include <string.h>

int main(){
/*    int age = 20;
    printf("My Age is %d\n", age);
    int newAge = age;
    newAge = 21;
    printf("Next year i will be %d but not %d\n", newAge, age);
    float myFloat = 20.3566793;
    printf("%1f\n", myFloat);

    time_t currentTimeSec = time(NULL);
    printf("%ld\n", currentTimeSec);
    
    time_t startTimeSec, endTimeSec;
    time(&startTimeSec);
    sleep(5);

    time(&endTimeSec);
    printf("%f\n", difftime(startTimeSec, endTimeSec));
*/
    char arr[50] = "I am not gay.";
    char *ptr = arr;

    printf("the string is \"%s\"\n", ptr);
    printf("the string is %p\n", ptr);

    return 0;
}