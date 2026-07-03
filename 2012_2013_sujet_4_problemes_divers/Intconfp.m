function [Ic] =Intconfp( N,n,a )
%UNTITLED5 Summary of this function goes here
%   Detailed explanation goes here
m=n/N;
s=sqrt(m*(1-m));
t=qnorm(1-a/2);
a= m-s*t/sqrt(N);
b=m+s*t/sqrt(N);
Ic=[a,b];
end

