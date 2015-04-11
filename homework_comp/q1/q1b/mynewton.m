function [x,f] = mynewton(func,je,x0,tol,maxk)

% function [x,f] = myNewton( fnon, dfdx, x0, tol, maxk, para )
% Classic Newton Method for F(x)=0 
% Input: fnon - nonlinear function F(x) 
%        dfdx - derivative function dFdx(x)
%        x0 - initial guess for x
%        tol - convergence measure for |F(x)|
%        maxk - max number of iterations allowed
% Output: x - final point computed by Newton algorithm
%         f - F(x) evaluated at the final point

fprintf('   k      x_k   F(x_k)\n');

k = 0;
x = x0;
f = feval(func,x);

fprintf(' %3d %8.4g %8.3g\n',k,x,f);

while( norm(f)>tol && k<maxk)
    
    d = feval(je,func,x);
    
    k = k + 1;
    x = x- f/d;
    f = feval(func,x);
    fprintf(' %3d %8.4g %8.3g\n',k,x,f);
    
end

if( k == maxk )
    fprintf('Not converged\n');
else
    fprintf('Converged\n')
end

end

    






