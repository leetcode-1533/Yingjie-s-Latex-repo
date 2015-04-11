
% This script combining newton method and the homotopy continuation method.
% It use the homotopy continuation method to provide a good initial guess for the newton method.

% It was writeen to solve question 3

clear all
[init,less] = continuation(@q3c,@cal_j,[5;4;3;2;1;30],30);


[x,f] = newtonSys(@q3c,@cal_j,init,1e-4,30);
