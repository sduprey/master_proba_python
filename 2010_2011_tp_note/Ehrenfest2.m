function [X] = Ehrenfest2(X,d )
%UNTITLED6 Simule un pas d'Ehrenfest
%   Detailed explanation goes here
U=rand(1);
if (U<d/(d+1))
    V=rand(1);
    X=X +(V>(X/d))-(V<(X/d));
end
end

