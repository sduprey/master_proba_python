%% 1. Histogramme-densite loi normale
X=randn(1000,1);
histo(X,20,0,1)
hold on
fplot(@(x)1./sqrt(2*pi)*exp(-x.^2./2),[-3 3],'r')
% ou bien
fplot('dnorm',[-3 3],'g')
hold off
[m,e]=me(X)
%% 2. Histogramme-Proba loi binomiale
help stixbox
Xbinom=rbinom(1000,10,0.3);
[m,s]=me(Xbinom)
histo(Xbinom,11,1,1)
% ou mieux
histo(Xbinom,max(Xbinom)-min(Xbinom)+1,1,1)
%On prend assez de classes dans l'histogramme pour couvrir les valeurs de
%Xbinom, mais pas plus, sinon on se retrouve avec des classes vides (car
%Xbinom est discrete)
hold on
stem([0:10],dbinom(0:10,10,0.3),'r')
%stem permet un diagramme en baton, utile pour les lois discretes.
figure
histo(Xbinom,max(Xbinom)-min(Xbinom)+1,0,1)
hold off
%% 3. Histo-densite loi de Poisson
Xpoi=rpoiss(1000,2);
[m,s]=me(Xpoi)
histo(Xpoi,max(Xpoi)-min(Xpoi)+1,1,1)
hold on
val=[0:10];
ppois=exp(-2)*2.^val./factorial(val);
stem(val,ppois,'r')
hold off
%% 4 Fonction de repartition loi normale 
Xn=randn(1000,1);
Y=sort(Xn);
stairs(Y,[1:1000]/1000)
hold on
fplot('pnorm',[-3 3],'r')
hold off
%%
plotrep(Xn)
%% 6 Lois uniformes continues
X=rand(1000,1);
XU=rand(1000,1)+1;
histo(XU)
XU2=2*rand(1000,1);
histo(XU2)
XU3=2*rand(1000,1)-1;
histo(XU3)
%% 8
XU4=runif(1000,-3,4);
histo(XU4)
%% 9 Bernoulli(0.5)
Pilface=X<0.5;
histo(Pilface)
mean(Pilface)
%% 10 Bernoulli(1/5)
Ber=X<(1/5);
histo(Ber)
%% 10 Bernoulli(p)
Ber=rbernou(1000,1,1/5);
histo(Ber);
%% 11 Uniforme sur (1,2,...,10)
D=ceil(10*rand(1000,1));
histo(D,10,1,1)
mean(D)
%% 12 Lancer de des
De=runifd(1000,6);
histo(De,6,1,1)
%% 13 Loi discrete sur (1,2,3)
Xd1=discrete1(1000);
histo(Xd1,3,1,1)
%% 13 Loi discrete generale
Xd2=discrete2(1000,[0.3,0.2,0.4,0.1]);
histo(Xd2,4,1,1)
%% 14 Par inversion de fonction de repartition : loi exponentielle
E=rexp(1000,2);
mean(E)
histo(E,20,0,1)
hold on
fplot(@(x)2*exp(-2.*x),[0 4])
hold off
figure
plotrep(E);
hold on
fplot(@(x)1-exp(-2*x),[0 4],'r')
hold off
%%
S=rbino2(500,10,0.3);
histo(S,11,1,1)
hold on;
S2=rbinom(500,10,0.3);
histo(S2,11,1,1,'r')
hold off;
type rbinom
%%
geom=zeros(1000,1);
for i=1:1000
    j=1;
    while (rand>1/6)
        j=j+1;
    end
    geom(i)=j;
end
mean(geom)
histo(geom,max(geom)-min(geom)+1,1,1)
hold on;
xg=[1:40]; stem(xg, 1/6*(5/6).^(xg-1),'r')
hold off;
type rgeom;
%%
Xn=10+randn(1000,1)*5;
histo(Xn,20,0,1)
hold on
fplot(@(x)1./sqrt(2*pi*25)*exp(-(x-10).^2/2/25),[-10 30])
hold off
% ou bien
histo(Xn,20,0,1)
hold on
fplot(@(x)dnorm(x,10,5),[-10 30])
hold off
type rnorm
%%
%%
X=2*rand(10000,1)-1;
Y=2*rand(10000,1)-1;
I=find((X.^2+Y.^2)<1);
Xd=X(I); Yd=Y(I);
plot(Xd,Yd,'d')
hold on
t=[0:pi/30:2*pi]; plot(exp(i*t))
%ou bien
t=[0:pi/30:2*pi]; polar(t,ones(1,61))
hold off
%%
figure;
histo(Xd,15,0,1);
%%
figure;
r=rand(10000,1);
t=2*pi*rand(10000,1);
plot(r.*exp(i*t),'.')
%%
Abs1=runif(10000,-1/4,2);
Ord1=runif(10000,-3*sqrt(3)/4, 3*sqrt(3)/4);
[T,R]=cart2pol(Abs1,Ord1);
I=find(R-cos(T)<1);
Cardx=Abs1(I); Cardy=Ord1(I);
plot(Cardx,Cardy,'d')
hold on
t=[0:pi/30:2*pi]; plot((1+cos(t)).*exp(i*t))
%ou bien
t=[0:pi/30:2*pi];polar(t,1+cos(t))
hold off