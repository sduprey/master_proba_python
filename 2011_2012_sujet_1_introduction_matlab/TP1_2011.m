a=4;b=pi
who
clear b
who
sqrt(a)
A=[1 2 3;4 5 6;7 8 9]
A(2,3)
%% Utilisation de :
X=[1:20]
Y=[1:2:20]
%% 1
[1:-0.5:-2]
%% Operations sur les matrices
b=A(2,:)
c=A(:,3)
B=A(1:2,1:2)
%% 2
C=A(:,1:2)
%%
help elmat
length(A)
C=A'
A+C
A*C
%%
n=4;I4=eye(n)
B=zeros(n)
C=ones(n)
p=2;A^p
ans
%% 3
E=5*ones(3)
%% 4
1+1:5
1+(1:5)
%%
A>2
%%
rca=sqrt(2:2:10)
%% Utilisation de .
A^2
A.^2
%%
A*C
A.*C
%% 6-7
V=[1:10].^2
V2=1./[1:10]
%% Boucles 
%% 8 Voir le fichier matTP1.m
matTP1
%% Representations graphiques
t=0:1/10:3; plot(t,exp(t)+3,'g')
%%
t=0:1/10:3; plot(t,exp(t),t,1+t)
%% 9
plot(t,cos(t),t,sin(t),t,t.^2)
% ou bien, par exemple
%% 9
fplot('cos',[-pi pi])
hold on
fplot('sin',[-pi pi])
t=[-pi:0.1:pi]; plot(t,t.^2)
hold off
%% Fonctions
toto(2)
fplot('toto',[-1 1])
%%
fplot(@toto,[-1 1])
%%
quad(@toto,0,1)
%%
fzero(@toto,1)
%% 10 voir le fichier q10.m
fplot(@q10,[0 1])
%% 10
quad(@q10,0,1)
pi/2-1
%%
toto2=@(x)cos(x).^2-sin(x).^2;
quad(toto2,0,pi)
fzero(@(x)x.^3-3,2)
%% 11
fzero(@(x)exp(x)-3*x,0)
%% Statistiques
rand
randn
X=rand(1000,1);
Y=rand(2,3);
s=sum(X)
m=mean(X)
v=var(X)
sigma=std(X)
std(X,1)
%% 12
mean(X.^3) %a comparer avec 1/4
%% Histogrammes 
help histo
X=rand(100,1);
histo(X)
%% 13
X=rand(1000,1);
histo(X,10,0,1)
%% 13
X=rand(1000,1);
histo(X,10,1,1)
%% 13
X=rand(10000,1);
histo(X,20,0,1)
%% 14
X=randn(1000,1);
histo(X,20,0,1)
hold on
fplot(@(x)1./sqrt(2*pi)*exp(-x.^2./2),[-3 3],'r')
% ou bien
fplot('dnorm',[-3 3],'g')
hold off
mean(X)
std(X,1)
%% 15
help stixbox
Xbinom=rbinom(1000,10,0.3);
histo(Xbinom,11,1,1)
% ou mieux
histo(Xbinom,max(Xbinom)-min(Xbinom)+1,1,1)
%On prend assez de classes dans l'histogramme pour couvrir les valeurs de
%Xbinom, mais pas plus, sinon on se retrouve avec des classes vides (car
%Xbinom est discrete)
hold on
stem([0:10],dbinom(0:10,10,0.3),'r')
%stem permet un diagramme en baton, utile pour les lois discretes.
mean(Xbinom)
std(Xbinom,1)
hold off
%% Et avec une loi exponentielle
Xexp=rexpweib(1000,2);
mean(Xexp)
std(Xexp,1)
histo(Xexp,20,0,1)
hold on
fplot(@(x)2*exp(-2*x),[0 3])
hold off
%% Avec une loi de Poisson
Xpoi=rpoiss(1000,2);
mean(Xpoi)
std(Xpoi,1)
histo(Xpoi,max(Xpoi)-min(Xpoi)+1,1,1)
hold on
abs=[0:10];
ppois=exp(-2)*2.^abs./factorial(abs);
stem(abs,ppois,'r')
hold off
