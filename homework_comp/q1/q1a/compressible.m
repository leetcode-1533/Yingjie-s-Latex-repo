function eval = compressible(p1)

% function [ eval ] = compressible(p1)
%
%   Indeed for solving the 1 question(a)
%
%   The reason for separating the function in 2 is due to the difficultly
%   in using function handle as a variable inside the function
%
%   Input p1 as a scalar 

d = 4.026;
eval = 433.54*520*(d^2.667)*0.7*(((p1^2-21.7^2)/(0.1894*0.7*530))^0.5)/14.7-2e6;
