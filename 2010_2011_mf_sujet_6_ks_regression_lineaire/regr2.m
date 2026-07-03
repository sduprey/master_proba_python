function [ bhat,sigma ] = regr2(Y,MX )
%UNTITLED11 Summary of this function goes here
%   Detailed explanation goes here
n=length(Y)
k=size(MX,2)
u=ones(1,n)';
M2=[u,MX];
g=(M2'*M2)^(-1);
bhat=g*M2'*Y;
sigma=norm(Y-M2*bhat)/sqrt(n-k)


end

