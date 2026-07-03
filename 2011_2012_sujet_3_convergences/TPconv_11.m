%Illustration convergence presque sure
%% Question 1
m=mean(1:6)
sigma=sqrt(mean([1:6].^2) - m^2)
%% Question 2
X=runifd(5000,6);
S=cumsum(X);
S2=S./[1:5000]';
%% Question 3
plot(S2)
hold on;
plot(m*ones(1,5000))
%% Question 4
clf
plot((([1:5000]').^0.1).*(S2-m))
plot([1:5000]'.*(S2-m))
plot(sqrt([1:5000]').*(S2-m))
%% Question 5
clf
plotrep(X(1:100))
hold on
plotrep(X(1:500))
plotrep(X(1:1000))
plotrep(X(1:5000))
stairs([1:6],[1:6]/6,'r')
hold off
%% Question 6-7-8-9
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
%% Question 10
clf
for i=1:2000
U=rand(1,100);
E=(U<1/2);
W(i)=sum(E./2.^[1:100]);
end
plotrep(W)
%% Question 12
clf
U=rand(1,100);
E=(U<1/2)+(-1)*(U>1/2);
V=cumsum(E./2.^[1:100]);
plot(V);
hold on
U=rand(1,100);
E=(U<1/2)+(-1)*(U>1/2);
V=cumsum(E./2.^[1:100]);
plot(V,'r');
clf
for i=1:2000
U=rand(1,100);
E=(U<1/2)+(-1)*(U>1/2);
W(i)=sum(E./2.^[1:100]);
end
plotrep(W)
clf
% Theoreme central limite
%% Question 13
clf
stem([200:400],dbinom([200:400],1000,0.3));
hold on;
plot([200:400],dnorm([200:400],1000*0.3,sqrt(1000*0.3*0.7)),'r');
hold off;
%% Question 14 
TCLde(10,1000)
TCLde(50,1000)
TCLde(300,1000)
TCLde(1000,1000)
%% Question 15
clf
B=rbinom(5000,10,2/10);
hold on
plotrep(B)
a=[0:8];
poi=exp(-2)*2.^a./factorial(a);
stairs(a,cumsum(poi),'r')
B=rbinom(5000,100,2/100);
plotrep(B)
B=rbinom(5000,1000,2/1000);
plotrep(B)
%%
