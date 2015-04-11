function jc = cal_j(u)

% This is the jacobian matrix for question 3

G = 35.0;
k = 0.12;
a0 = 6.0;
a6 = 0.7;

jc = [1,0,0,0,0,k*u(1)/G;
    -1,1+k*u(6)/G,0,0,0,k*u(2)/G;
    0,-1,1+k*u(6)/G,0,0,k*u(3)/G;
    0,0,-1,1+k*u(6)/G,0,k*u(3)/G;
    0,0,0,-1,1+k*u(6)/G,k*u(5)/G;
    0,0,0,0,-1,k*a6/G];
