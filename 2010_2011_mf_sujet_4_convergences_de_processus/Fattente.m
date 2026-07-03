function [ res ] = Fattente(X,p,q )
%UNTITLED7 Summary of this function goes here
%   Detailed explanation goes here
Y=rand(1)<p;
if (X==0) res=Y;
else Z=rand(1)<q;
    res=X+Y-Z;
end;

end

