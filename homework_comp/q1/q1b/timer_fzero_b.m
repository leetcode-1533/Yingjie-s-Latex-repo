% This script test the time efficiency of the fzero method.
% It do the same evalution for 10 times and then calculate its average
% value.

sum = 0;
for i = 1: 10
id = tic;
fzero(@compressible,[4 8],optimset('Display','iter'))
time_costing = toc(id);
sum = sum + time_costing;
end

sum = sum/10