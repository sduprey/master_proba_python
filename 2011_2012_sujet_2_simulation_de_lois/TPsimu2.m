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
%% 16 Mystere permet de generer une loi geometrique de parametre p
geom=zeros(1000,1);
for i=1:1000
   geom(i)=mystere(1/6);
end
mean(geom)
histo(geom,max(geom)-min(geom)+1,1,1)
hold on;
xg=[1:40]; stem(xg, 1/6*(5/6).^(xg-1),'r')
hold off;
%% 17
Xn=10+randn(1000,1)*5;
histo(Xn,20,0,1)
hold on
fplot(@(x)1./sqrt(2*pi*25)*exp(-(x-10).^2/2/25),[-10 30],'r')
hold off
% ou bien
histo(Xn,20,0,1)
hold on
fplot(@(x)dnorm(x,10,5),[-10 30],'r')
hold off
type rnorm
%%
%% 18
clf
X=2*rand(10000,1)-1;
Y=2*rand(10000,1)-1;
I=find((X.^2+Y.^2)<1);
Xd=X(I); Yd=Y(I);
plot(Xd,Yd,'d')
hold on
clear i %i a ete utilise precedemment 
t=[0:pi/30:2*pi]; plot(exp(i*t),'r')
% ou bien
t=[0:pi/30:2*pi]; plot(cos(t),sin(t),'r')
%ou bien
t=[0:pi/30:2*pi]; polar(t,ones(1,61),'r')
hold off
%%
figure;
histo(Xd,15,0,1);%Xd ne suit pas une loi uniforme.
%%
figure;
r=rand(10000,1);
t=2*pi*rand(10000,1);
plot(r.*exp(i*t),'.') % La loi n'est pas uniforme.
%%
Abs1=runif(10000,-1/4,2);
Ord1=runif(10000,-3*sqrt(3)/4, 3*sqrt(3)/4);
[T,R]=cart2pol(Abs1,Ord1);
I=find(R-cos(T)<1);
Cardx=Abs1(I); Cardy=Ord1(I);
plot(Cardx,Cardy,'d')
hold on
t=[0:pi/30:2*pi]; plot((1+cos(t)).*exp(i*t),'r')
%ou bien
t=[0:pi/30:2*pi];polar(t,1+cos(t),'r')
hold off