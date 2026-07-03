function res = Urne( Rouge,n,r,b )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
U=rand(1);
res=Rouge+(U<Rouge/(r+b+n));
end

