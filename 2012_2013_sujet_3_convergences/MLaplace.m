function [P] = MLaplace( n,p,x )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
P=pbinom(x*sqrt(n*p*(1-p))+n*p,n,p);

end

