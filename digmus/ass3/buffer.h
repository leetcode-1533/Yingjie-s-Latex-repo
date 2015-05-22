#include <stdlib.h>
#include "mbed.h"


struct circle{
    float num;
    struct circle * next;
    struct circle * before;
};

struct circle * create(int size);

struct circle * rotate(struct circle * head);

