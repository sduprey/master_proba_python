function Y = Ehrenfest3(d,X)
%UNTITLED6 Simule un pas d'Ehrenfest
%   Detailed explanation goes here
U=rand(1);
if (U<d/(d+1))
    V=rand(1);
    Y=X +(V>(X/d))-(V<(X/d));
else Y=X;
end
end

