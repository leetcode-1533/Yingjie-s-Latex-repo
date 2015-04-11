% This script test the time efficiency of the newton method.
% It do the same evalution for 10 times and then calculate its average
% value.

sum = 0;
for i = 1: 10
id = tic;
mynewton(@compressible,@fin_num_j,4,1e-7,30)
time_costing = toc(id);
sum = sum + time_costing;
end

sum = sum/10