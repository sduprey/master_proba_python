function [] = TCLde(n,Nobs)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
for i=1:Nobs
    X=runifd(n,6);
    V(i)=(sum(X)/n-3.5)*sqrt(n)/sqrt(17.5/6);
end
    plotrep(V)
hold on
fplot('pnorm',[-3 3],'r')
end

