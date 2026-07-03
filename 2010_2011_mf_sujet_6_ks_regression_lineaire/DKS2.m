function [ac,rep ] = DKS2(X,Y,alpha )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
Z=[X,Y];
n=length(X);
m=length(Y);
T=zeros(1,n+m);
Z=sort(Z);
for k=1:(n+m)
    T(k)=abs(frep2(X,Z(k))-frep2(Y,Z(k)));
end
d=sqrt(n*m/(n+m))*max(T)
ac=1-pks(d);
if (ac>alpha) rep = 'OUI'
else rep = 'NON'
end
end

