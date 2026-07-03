%Illustration convergence presque sure
%% Question 1
m=mean(1:6)
%% Question 2
X=runifd(5000,6);
S=cumsum(X);
S2=S./[1:5000]';
%% Question 3
plot(S2)
hold on;
plot(m*ones(1,5000),'r')
%% Question 4
clf
plot(sqrt([1:5000]').*(S2-m))
figure
plot([1:5000]'.*(S2-m))
figure
plot((([1:5000]').^0.1).*(S2-m))
%% Question 5
clf
plotrep(X(1:100))
hold on
plotrep(X(1:500))
plotrep(X(1:1000))
plotrep(X(1:5000))
stairs([1:6],[1:6]/6,'r')
hold off
%% Question 6
clf
X=rand(1,5000);
S=cumsum(X);
S2=S./[1:5000];
plot(S2)
hold on;
plot(0.5*ones(5000,1))
clf
plotrep(X(1:100))
hold on
plotrep(X(1:500))
plotrep(X(1:1000))
plotrep(X(1:5000))
fplot(@(x)x,[0 1])
%% Question 7-8-9-10
clf
U=rand(1,100);
E=(U<1/2);
V=cumsum(E./2.^[1:100]);
plot(V);
hold on
U=rand(1,100);
E=(U<1/2);
V=cumsum(E./2.^[1:100]);
plot(V,'r');
%% Question 11
sigma=sqrt(mean([1:6].^2) - m^2)
clf
for i=1:2000
U=rand(1,30);
E=(U<1/2);
W(i)=sum(E./2.^[1:30]);
end
plotrep(W)
%% Question 13
clf
U=rand(1,30);
E=(U<1/2)+(-1)*(U>1/2);
V=cumsum(E./2.^[1:30]);
plot(V);
hold on
U=rand(1,30);
E=(U<1/2)+(-1)*(U>1/2);
V=cumsum(E./2.^[1:30]);
plot(V,'r');
clf
for i=1:2000
U=rand(1,30);
E=(U<1/2)+(-1)*(U>1/2);
W(i)=sum(E./2.^[1:30]);
end
plotrep(W)

% Theoreme central limite
%% Question 13 
TCLde(10,1000)
TCLde(50,1000)
TCLde(300,1000)
TCLde(1000,1000)
%% Question 14
clf
B=rbinom(5000,10,2/10);
hold on
plotrep(B)
a=[0:10];
poi=exp(-2)*2.^a./factorial(a);
stairs(a,cumsum(poi),'r')
B=rbinom(5000,100,2/100);
plotrep(B)
B=rbinom(5000,1000,2/1000);
plotrep(B)
%%
clf
hold on
stairs([0:10],pbinom([0:10],10,2/10))
stairs([0:10],pbinom([0:10],100,2/100),'r')
stairs([0:10],pbinom([0:10],1000,2/1000),'g')
stairs(a,cumsum(poi),'b')
%%
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