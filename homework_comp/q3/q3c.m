function eval = q3c(u)

% This is the function for the question 3

G = 35.0;
k = 0.12;
a0 = 6.0;
a6 = 0.7;

eval = [k*u(6)*u(1)/G + u(1) - a0;
    k*u(6)*u(2)/G + u(2) - u(1);
    k*u(6)*u(3)/G + u(3) - u(2);
    k*u(6)*u(4)/G + u(4) - u(3);
    k*u(6)*u(5)/G + u(5) - u(4);
    k*u(6)*a6/G + a6 - u(5)];
