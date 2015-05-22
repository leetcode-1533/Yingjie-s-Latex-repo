#include "buffer.h"

AnalogIn inp(p20);//input 

struct circle * create(int size){
    // This is the initialing function for filling in the buffer.
    struct circle * head, *pf, *pb;
    head = (struct circle *) malloc(sizeof(struct circle));
    pb = head;
    // Initialing the circular linked list(fixed length queue)
    for(int i = 0; i<size ; i++){
        pf = (struct circle *) malloc(sizeof(struct circle));
        pb->num = inp.read();
        pb->next = pf;
        pf->before = pb;
        pb = pf;
    }
    pb->num = inp.read();
    pb->next = head;
    head->before = pb;
    return head;
} // 2 way linked list

struct circle * rotate(struct circle * head){
    // This is the rotation function for buffer rotation.
    head->num = inp.read();//write to the tail one
    return head->next;
}