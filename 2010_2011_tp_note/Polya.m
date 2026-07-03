function [R] = Polya(n,r,b )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
R=zeros(n+1,1);
R(1)=r;
for k = 1:n
    R(k+1) = Urne(R(k),k-1,r,b); %Attention aux indices, l'indice de R commence a 1
end
end

