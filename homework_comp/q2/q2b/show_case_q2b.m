
% This script illustrate to us the physical meaning the the error e, the data is obtained from the question 2,b,1

t1=[200,150];
t2=[0,150];
t3=[0,-150];

hold on
viscircles(t1,100,'EdgeColor','b')
viscircles(t1,103.1250,'EdgeColor','b')
viscircles(t2,225,'EdgeColor','g')
viscircles(t3,450.8810)

plot(199.9756,  253.1250,'*')

grid on;
