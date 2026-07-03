function [Y] = rcauchy(n)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
X=rand(n,1);Y=-tan(pi*(X-0.5));
end

