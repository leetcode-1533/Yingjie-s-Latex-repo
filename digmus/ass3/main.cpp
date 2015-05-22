#include "mbed.h"
#include "buffer.h"
#define buffer_size 19

Serial pc(USBTX, USBRX);// not used
AnalogOut aout(p18);// output
Ticker ticker;// interrupt

float weight[buffer_size] = {0};
struct circle * buffer;


void give_weight(float * weight){
    // This function is the initialing function for the weight variable.
    weight[0] = -0.002693840;
    weight[1] = -0.002519748;
    weight[2] =  0.005014695;
    weight[3] =  0.015641050;
    weight[4] =  0.000000000;
    weight[5] = -0.046914239;
    weight[6] = -0.048021820;
    weight[7] =  0.083481298;
    weight[8] =  0.294332820;
    weight[9] =  0.400000000;
    weight[18] = -0.002693840;
    weight[17] = -0.002519748;
    weight[16] =  0.005014695;
    weight[15] =  0.015641050;
    weight[14] =  0.000000000;
    weight[13] = -0.046914239;
    weight[12] = -0.048021820;
    weight[11] =  0.083481298;
    weight[10] =  0.294332820;
}

float cal_elem(float * weight, struct circle * buffer){
    // This function calculate the output voltage according to the current buffer
    float sum = 0;

    for(int i = 0; i <= buffer_size-1; i++){
        sum += (buffer->num)*weight[i];
        buffer = buffer->next;
    }
    return sum;
}


void cal(){
    // This function is the wrapper for function cal_elem() and rotate(). Itself is called by the interrupt.
    float current;
    current = cal_elem(weight,buffer);
    buffer = rotate(buffer);
    current = current - 0.5;
    aout.write(current);
}



int main() {
    give_weight(weight);
    buffer= create(buffer_size-1);
    
    ticker.attach(&cal,0.0001);//10khz::22khz is the limit
    while(1);

}
