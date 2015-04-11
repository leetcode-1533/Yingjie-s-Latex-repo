function re = conpnewl(fun,jac,x0,con,new)

% This function combining newton method and the homotopy continuation method.
% It use the homotopy continuation method to provide a good initial guess for the newton method.
% Input:
%       fun: function handle for the unsolved function
%       jac: jacobian matrix for the unsolved function
%       x0 : initial guess for the homotopy continuation method, written vertically
%       con: function handle for the solver of the homotopy continuation method
%       new: function handle for the sovler of the newton mehod
% Output:
%       re: the founded result, the format is as same as the x0

[init_p,less] = feval(con,fun,jac,x0,30);
init_p
fprintf('\n')
[p,less] = feval(new,fun,jac,init_p,1e-8,40);
re = p;
