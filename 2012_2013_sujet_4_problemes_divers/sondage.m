function [ re] = sondage(N,n)
%UNTITLED6 Summary of this function goes here
%   Detailed explanation goes here
p=n/N;
s=sqrt(p*(1-p));
re(1)=p;
re(2)=2*(1-pnorm(abs(0.5-p)*sqrt(N)/s));

end

