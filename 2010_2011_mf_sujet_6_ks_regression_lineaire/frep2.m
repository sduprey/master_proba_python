function [ res ] = frep2(X,x )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
n=length(X);
Y=sort(X);
k=1;
while((k<=n) & (Y(k)<=x))
    k=k+1;
end
res=(k-1)/n;


end

