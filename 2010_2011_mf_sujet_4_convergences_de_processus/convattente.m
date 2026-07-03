function  convattente(p,q )
%UNTITLED9 Summary of this function goes here
%   Detailed explanation goes here
clf
Y=zeros(5,2000);
X=zeros(1,500);
for k=1:2000
    X(1)=0;
    for n=2:500
        X(n)=Fattente(X(n-1),p,q);
    end;
    Y(1,k)=X(10);
    Y(2,k)=X(20);
    Y(3,k)=X(50);
    Y(4,k)=X(150);
    Y(5,k)=X(500);
end
hold on
for k=1:5
    plotrep(Y(k,:))
end

if (p<q) pconv=plim(p,q)
    stairs([0:14],cumsum(pconv),'r');
end

end

