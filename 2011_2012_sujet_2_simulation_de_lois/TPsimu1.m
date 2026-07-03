
%% 1. Histogramme-densite loi normale
X=randn(1000,1);
histo(X,20,0,1)
hold on
fplot(@(x)1./sqrt(2*pi)*exp(-x.^2./2),[-3 3],'r')
% ou bien
fplot('dnorm',[-3 3],'g')
hold off
mean(X)
std(X)
%% 2. Histogramme-Proba loi binomiale
help stixbox
Xbinom=rbinom(1000,10,0.3);
mean(Xbinom)
10*0.3
std(Xbinom)
sqrt(10*0.3*0.7)
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
mean(Xpoi)
std(Xpoi)
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