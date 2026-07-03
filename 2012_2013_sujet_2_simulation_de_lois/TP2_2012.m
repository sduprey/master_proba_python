
%% 1. Histogramme-densite loi normale
X=randn(1000,1);
histo(X,20,0,1)
hold on
x=[-3:0.1:3];
plot(x,1./sqrt(2*pi)*exp(-x.^2./2),'r')
hold off
mean(X)
std(X)
%% 4 Fonction de repartition loi normale 
Xn=randn(1000,1);
Y=sort(Xn);
stairs(Y,[1:1000]/1000)
x=[-3:0.1:3];
hold on
plot(x,pnorm(x),'r')
hold off
%%
plotrep(Xn)
%% Question subsidiaire : loi binomiale
Z=rbinom(1000,10,0.3);
mean(Z)
std(Z)
plotrep(Z);
hold on;
k=[0:10];
stem(k,pbinom(k,10,0.3));
hold off;
%% 6 Lois uniformes continues
X=rand(1000,1);
XU=rand(1000,1)+1;
histo(XU)
XU2=2*rand(1000,1);
histo(XU2)
XU3=2*rand(1000,1)-1;
histo(XU3)
%% 7
XU4=runif(1000,-3,4);
histo(XU4)
%% 8 Bernoulli(0.3)
Pilface=X<0.3;
histo(Pilface)
mean(Pilface)
%% 9 Bernoulli(p)
Ber=rbernou(1000,1/5);
histo(Ber);
%% 10 Uniforme sur (1,2,...,10)
D=ceil(10*rand(1000,1));
histo(D,10,1,1)
mean(D)
%% 11 Lancer de des
De=runifd(1000,6);
histo(De,6,1,1)
%% 12 Loi discrete sur (1,2,3)
Xd1=discrete1(1000);
histo(Xd1,3,1,1)
%% 13 Loi discrete generale
Xd2=discrete2(1000,[0.3,0.2,0.4,0.1]);
histo(Xd2,4,1,1)
%% Inversion de la fonction de repartition 
%%  Par inversion de fonction de repartition : loi exponentielle
E=rexp(1000,2);
mean(E)
histo(E,20,0,1)
x=[0:0.1:4];
hold on
plot(x,2*exp(-2.*x))
hold off
figure
plotrep(E);
hold on
plot(x,1-exp(-2*x),'r')
hold off
%% Cauchy
X=rcauchy(1000);
plotrep(X);
hold on;
x=[-15:0.1:15];
plot(x,1/pi*(atan(x)+pi/2),'r');
hold off;
%% %% 16 Mystere permet de generer une loi geometrique de parametre p
geom=zeros(1000,1);
for i=1:1000
   geom(i)=mystere(1/6);
end
mean(geom)
%% 18
clf
X=2*rand(10000,1)-1;
Y=2*rand(10000,1)-1;
I=find((X.^2+Y.^2)<1);
Xd=X(I); Yd=Y(I);
plot(Xd,Yd,'d')
hold on
t=[0:pi/30:2*pi]; plot(cos(t),sin(t),'r')
hold off
%%
figure;
histo(Xd,15,0,1);%Xd ne suit pas une loi uniforme.
%% Question subsidiaire
figure
histo(sqrt(Xd.^2+Yd.^2),15,0,1)
hold on
fplot(@(x) 2*x,[0 1])
hold off
figure
plotrep(sqrt(Xd.^2+Yd.^2));
hold on
fplot(@(x) x.^2,[0 1],'r')
hold off
%%19
figure;
r=rand(10000,1);
t=2*pi*rand(10000,1);
plot(r.*cos(t), r.*sin(t),'.') % La loi n'est pas uniforme.
%% 20 Cardioide
Abs1=runif(10000,-1/4,2);
Ord1=runif(10000,-3*sqrt(3)/4, 3*sqrt(3)/4);
[T,R]=cart2pol(Abs1,Ord1); 
%cart2pol permet de passer des coord. cartesiennes aux coord. polaires
I=find(R-cos(T)<1);
Cardx=Abs1(I); Cardy=Ord1(I);
plot(Cardx,Cardy,'d')
hold on
t=[0:pi/30:2*pi]; plot((1+cos(t)).*cos(t),(1+cos(t)).*sin(t),'r')
hold off
