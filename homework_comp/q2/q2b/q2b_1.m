function eval = q2b_1( x )

% This is the function handle for question 2,b,1

t1=[200,150];
t2=[0,150];
t3=[0,-150];

d = [100.0, 225.0, 450.0];

eval = [(x(1)-t1(1,1))^2+(x(2)-t1(1,2))^2-(d(1)+x(3))^2;
    (x(1)-t2(1,1))^2+(x(2)-t2(1,2))^2-d(2)^2;
    (x(1)-t3(1,1))^2+(x(2)-t3(1,2))^2-d(3)^2];
