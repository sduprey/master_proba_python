function [Y ] = Markov( X )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
U=rand(1);
if (X==1) Y=2*(U<1/3) + 3*(U>1/3); end
if (X==2) Y=1*(U<1/3) + 3*(U>1/3); end
if (X==3) Y=1*(U<2/3) + 2*(U>2/3); end

end

