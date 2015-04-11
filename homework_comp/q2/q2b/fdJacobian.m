
function J =  fdJacobian( n, x0, f0, fnon )

% Finite difference approximation to the Jacobian
%  function J =  fdJacobian( n, x0, f0, fnon )
% Input: n - number of equations
%        x0 - current solution
%        f0 - current function value
%        fnon - nonlinear function handle
% Output: J - Jacobian matrix 

J = zeros(n);

h = 10*sqrt(eps); % perturbation 

for j = 1:n   % compute column by column

    x = x0;
    x(j) = x(j) + h;         % perturb variable x_j
    f = feval( fnon, x );    % perturbed residual
    J(1:n,j) = ( f - f0 )/h; % add in column j

end
