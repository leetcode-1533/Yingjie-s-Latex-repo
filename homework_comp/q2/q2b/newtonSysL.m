function [ x,f ] = newtonSysL( fnon, fjac, x0, tol, maxIt )

% Basic Newton algorithm for systems of nonlinear equations
%  function [ x,f ] = newtonSysL( fnon, fjac, x0, tol, maxit )
% Input: fnon - function handle for nonlinear system
%        fjac - function handle for Jacobian matrix 
%        x0 - initial state (column vector)
%        tol - convergence tolerance
%        maxIt - maximum allowed number of iterations
% Output: x - final point
%         f - final function value
%
% Example: [x,f]=newtonSysL( @example2, @fdJacobian, [1; 1], 1e-8, 40 )
% compare: [x,f] = newtonSys( @example2, @fdJacobian, [1; 1], 1e-8, 40 )
% compare: [x,f,flag]=fsolve( @example2, [ 1; 1 ], optimset('Display','Iter') )

maxstep = 4; % max number of line search steps per iteration

fprintf(' it    |f(x)|\n')

n = length(x0);

x = x0;             % initial point
f = feval(fnon,x);  % initial function values
normf = norm(f);
it = 0;
fprintf(' %d %12.6f\n',it,normf);

while (normf>tol) && (it<maxIt) 
  
  J = feval( fjac, n, x, f, fnon ); % build Jacobian
  delta = -J\f;                           % solve linear system

  step = 0;
  lambda = 1;
  x1 = x + delta;        % first update of x
  f1 = feval(fnon,x1);   % new function values
  normf1 = norm(f1);
  fprintf('     alpha    |f(x)|\n')
  fprintf('   %8.4f %12.6f\n',lambda,normf1)
  while ( normf1 > normf )  && ( step < maxstep ) % line search
    step = step + 1;
    lambda = lambda/2;
    x1 = x + lambda*delta;  % update x
    f1 = feval(fnon,x1);
    normf1 = norm(f1);
    fprintf('   %8.4f %12.6f\n',lambda,normf1)
  end

  x = x1;   % accept final value
  f = f1;
  normf = normf1;
 
  it = it + 1;
  % Print the new estimate and function value.
  fprintf(' %d %12.6f\n',it,normf)
 
end

if( it==maxIt)
    fprintf(' WARNING: Not converged\n')
else
    fprintf(' SUCCESS: Converged\n')
end
