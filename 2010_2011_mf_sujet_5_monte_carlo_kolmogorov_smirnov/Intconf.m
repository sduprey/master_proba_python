function Ic = Intconf(X,s,alpha)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
t = qnorm(1-alpha/2); 
n=length(X);
m = mean(X); 
a= m-s*t/sqrt(n);
b=m+s*t/sqrt(n);
Ic=[a,b];
end 


