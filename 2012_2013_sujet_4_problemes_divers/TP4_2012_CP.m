%% 1
A=[0 1/3 2/3;1/3 0 2/3;2/3 1/3 0];
P=[0.35 0.25 0.4];
P*A
%%
p0=[0.05 0.9 0.05];
p5=p0*A^5
p10=p0*A^10
p50=p0*A^50
p100=p0*A^100
p0=[0 1 0]
p0*A^10
p0*A^50
clf
for n=1:5000
X=1;
for k=1:1000
X=Markov(X);
end
Y(n)=X;
end
plotrep(Y)
hold on
stairs(cumsum(P),'r')
hold off
%% 2
X=randn(1,1000);
Intconf(X,std(X),0.05)
k=0;
for i=1:20
    X=randn(1,1000);
Ic=Intconf(X,std(X),0.05)
if (0>Ic(1) && 0<Ic(2)) k=k+1;
end
end
k % k suit a peu pres une loi  binomiale de parametre (20,0.9)
%%
X=randn(1,1000);
a=[0.01:0.01:0.99];
m=length(a);
I1=zeros(1,m);
I2=zeros(1,m);
for i=1:m
    Ic=Intconf(X,std(X),a(i));
    I1(i)=Ic(1);
    I2(i)=Ic(2);
end
clf
plot(a,I1);
hold on
plot(a,I2);
%% 3
Intconfp(100,64,0.05)
Intconfp(400,212,0.05)

sondage(400,212)
sondage(100.52)
sondage(100,60)
