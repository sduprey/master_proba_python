function [X] = Polyaloi(nech,n,r,b )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
X=zeros(nech,1);
for k=1:nech
    X(k)=r/(r+b);
for l = 1:n
    X(k) = (Urne(X(k)*(r+b+l-1),l-1,r,b))/(r+b+l); %Attention aux indices...
end
end
