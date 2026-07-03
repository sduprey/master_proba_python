function  plotergo(p,q,nmax )
%UNTITLED8 Summary of this function goes here
%   Detailed explanation goes here
clf;
X=zeros(1,nmax);
X(1)=0;
for k=2:nmax
    X(k)=Fattente(X(k-1),p,q);
end;
plimite=plim(p,q);
Y=zeros(15,nmax);
for m=0:14
    Y(m+1,:)=cumsum(X==m)./[1:nmax];
end
for m=1:15
    subplot(3,5,m); hold on;
    plot(Y(m,:));
    plot(plimite(m)*ones(1,nmax),'r');hold off;
end



end

