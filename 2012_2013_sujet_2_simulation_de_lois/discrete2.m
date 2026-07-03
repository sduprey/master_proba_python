function res=discrete2(n,p)
m=length(p);
X=rand(1,n);
p2=cumsum(p);
res=X<p2(1);
for i=2:1:m
    res=res+i*(X>p2(i-1)&X<p2(i));
end
end