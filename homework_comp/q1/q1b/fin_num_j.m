function j_fin = fin_num_j(func,x)

% This function numerically calculate the scalar function's differential at
% the point where x = x.
%
% The input:
%   func : the function handle of the function
%   x : the value of x
%
% The output:
%   j_fin : the differential of function func at the point where x = x

h = 10*sqrt(eps);
j_fin = (feval(func,x+h)-feval(func,x))/h;