%   Grid Search script: for question 2
%
%   This script will using matlab built in function fsolve to try to solve 
%   the loran.m function. 
%   The starting points are giving at the interval of 10,starting from
%   -400 to 400 along x axis and y axis
%
%   This program will produce 81*81 answers, and it will took approximatly
%   5 minuts to run through.

clear all;
[x_mesh,y_mesh] = meshgrid(-400:10:400);
flag = zeros(length(x_mesh),length(x_mesh));
answ = cell(length(x_mesh),length(x_mesh));
f = zeros(length(x_mesh),length(x_mesh));
error_rec = cell(length(x_mesh),length(x_mesh));
for x_axis = 1:length(x_mesh)
    for y_axis = 1:length(x_mesh)   
        start_p = [x_mesh(x_axis,y_axis),y_mesh(x_axis,y_axis)];
        try
        [answ_temp,f_temp,flag_temp]=fsolve(@(x)loran(x,[103.5070,226.2602,450.8810]),start_p);
        answ{x_axis,y_axis} = answ_temp;
        f(x_axis,y_axis) = f_temp;
        flag(x_axis,y_axis) = flag_temp;
        catch err
            warning('failed');
            error_rec{x_axis,y_axis} = err.identifier;
            answ{x_axis,y_axis} = nan;
            f(x_axis,y_axis) = nan;
        end           
    end
end

ind = find(flag==0);
answ(ind)={nan};
f(ind) = nan;

ind = find(flag==-2);
answ(ind)={nan};
f(ind) = nan;

