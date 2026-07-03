%% 1. Histogramme-densite loi normale
X=randn(1000,1);
histo(X,20,0,1)
hold on
fplot(@(x)1./sqrt(2*pi)*exp(-x.^2./2),[-3 3],'r')
% ou bien
fplot('dnorm',[-3 3],'g')
hold off
[m,e]=me(X)

%% 3 Fonction de repartition loi normale 
Xn=randn(1000,1);
Y=sort(Xn);
stairs(Y,[1:1000]/1000)
hold on
fplot('pnorm',[-3 3],'r')
hold off
%%
plotrep(Xn)
%% 5 Lois uniformes continues
X=rand(1000,1);
XU=X+1;
histo(XU)
XU2=2*X;
histo(XU2)
XU3=2*X-1;
histo(XU3)
%% 6
XU4=runif(1000,-3,4);
histo(XU4)
%% 7 Bernoulli(0.5)
Pilface=X<0.5;
histo(Pilface)
mean(Pilface)
%% 8 Bernoulli(p)
Ber=rbernou(1,1000,1/5);
histo(Ber)
%% 9 Uniforme sur (1,2,...,10)
D=ceil(10*rand(1000,1));
histo(D,10,1,1)
mean(D)
hold on
stem(1/10*ones(1,10))
hold off
%% 10 Lancer de des
De=runifd(1000,6);
histo(De,6,1,1)
%% 11 Loi discrete sur (1,2,3)
Xd1=discrete1(1000);
histo(Xd1,3,1,1)
%% 12 Loi discrete generale
Xd2=discrete2(1000,[0.3,0.2,0.4,0.1]);
histo(Xd2,4,1,1)