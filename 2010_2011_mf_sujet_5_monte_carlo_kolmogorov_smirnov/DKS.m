function [ ac ] = DKS(X,F0,alpha)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
Y=F0(sort(X));
n=length(X);
Z1=[1:n]/n;
Z2=[0:n-1]/n;
T1=Z2-Y;
T2=Y-Z1;
d1=max(T1);
d2=max(T2);
d3=max(d1,d2)*sqrt(n);
ac=1-pks(d3);
if (ac>alpha) rep = 'OUI'
else rep = 'NON'
end
end

