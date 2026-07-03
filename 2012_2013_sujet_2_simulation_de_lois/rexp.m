function [ X ] = rexp( n,l )
%UNTITLED5 genere un n-echantillon de loi exponentielle de parametre l
%   Detailed explanation goes here
X=-log(rand(n,1))/l;

end

