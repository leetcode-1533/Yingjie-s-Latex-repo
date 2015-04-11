
function f = loran( x, d )

% function f = loran( x, d )
% nonlinear system of 2 equations representing
% the Loran equations with
% t1(1:2),t2(1:2),t3(1:2) the coordinates of each transmitter
%
% Input:
% x(1:2) the location of the object
% d(1:3) the measured distance to transmitter (t1,t2,t3)
% Output:
% f(1:2) the nonlinear system evaluated at x(1:2)

t1=[200,150];
t2=[0,150];
t3=[0,-150];

c23 = 0.5*( t2(2) - t3(2) );
a23 = 0.5*( d(2) - d(3) );
c21 = 0.5*( t2(1) - t1(1) );
a21 = 0.5*( d(2) - d(1) );

f = [ (x(2)-0.5*(t2(2)+t3(2)))^2/a23^2 - (x(1)-0.5*(t2(1)+t3(1)))^2/(c23^2-a23^2) - 1 ; (x(1)-0.5*(t1(1)+t2(1)))^2/a21^2 - (x(2)-0.5*(t1(2)+t2(2)))^2/(c21^2-a21^2) - 1 ];

f = f(1)^2+f(2)^2;
end

