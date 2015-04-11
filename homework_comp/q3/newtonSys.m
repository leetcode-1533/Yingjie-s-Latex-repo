function [ x,f ] = newtonSys( fnon, fjac, x0, tol, maxIt )

% Basic Newton algorithm for systems of nonlinear equations
%  function [ x,f ] = newtonSys( fnon, fjac, x0, tol, maxit )
% Input: fnon - function handle for nonlinear system
%        fjac - function handle for Jacobian matrix 
%        x0 - initial state (column vector)
%        tol - convergence tolerance
%        maxIt - maximum allowed number of iterations
% Output: x - final point
%         f - final function value

fprintf(' x     |f(x)|\n')


x = x0;             % initial point
f = feval(fnon,x);  % initial function values
it = 0;
fprintf(' %d %12.6f\n',it,norm(f));

while (norm(f)>tol) && (it<maxIt) 
  
  J = feval( fjac, x ); % build Jacobian
  delta = -J\f;                           % solve linear system
  
  x = x + delta;       % update x
  f = feval(fnon,x);   % new function values
 
  it = it + 1;
  % Print the new estimate and function value.
  fprintf(' %d %12.6f\n',it,norm(f))
  
end

if( it==maxIt)
    fprintf(' WARNING: Not converged\n')
else
    fprintf(' SUCCESS: Converged\n')
end
