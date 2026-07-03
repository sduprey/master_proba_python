function [res] = plim(p,q )
%UNTITLED5 Summary of this function goes here
%   Detailed explanation goes here
res=zeros(1,15);
res(1)=1-p/q;
res([2:15])=1/(1-q)*(1-p/q)*(p/q).^[1:14].*((1-q)/(1-p)).^[1:14];
end

