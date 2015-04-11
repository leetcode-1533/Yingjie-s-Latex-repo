%    This script draw out the acutal queastion's situation
%
%    By looking at the plot, we can have a rough guess of the final answer
%   whose x coordinator is around 200 and y coordinator is around 250

t1=[200,150];
t2=[0,150];
t3=[0,-150];

hold on
viscircles(t1,103.5070,'EdgeColor','b')
viscircles(t2,226.2602,'EdgeColor','g')
viscircles(t3,450.8810)

grid on;