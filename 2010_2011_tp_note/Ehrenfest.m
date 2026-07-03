function [X] = Ehrenfest(X,d )
%UNTITLED6 Simule un pas d'Ehrenfest
%   Detailed explanation goes here
U=rand(1);
X=X +(U>(X/d))-(U<(X/d));
end

