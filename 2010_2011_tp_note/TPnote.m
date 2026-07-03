%% Exercice 1
%% 1 Generation par rejet
X=rand(10000,1);
Y=rand(10000,1);
I=find((X.^2+Y.^2)<1);
Xd=X(I); Yd=Y(I);
plot(Xd,Yd,'d')
hold on
t=[0:pi/30:pi/2]; plot(exp(i*t))
%% 2
clf
plotrep(sqrt(Xd.^2+Yd.^2))
hold on
fplot(@(t) t.^2,[0 1],'r')
%% 3
clf
plotrep(Xd)
hold on
fplot(@(t) 2/pi*(asin(t)+t.*sqrt(1-t.^2)),[0 1],'r')
%%
%% Exercice 2
%% 1 Non elles ne sont pas L1 : |x|/(1+x^2) equivalent a 1/x au vois de +infini
%% 2 arctan(x)/pi  + 1/2
%% 3 Generation de Cauchy par inversion de la fonction de repartition
clf;
n=1000;
X=rand(n,1);
Y=tan(pi*(X-0.5));
M=cumsum(Y)./[1:n]';
plot(M)
% on n'observe pas de convergence presque sure
%% 4 E[exp(itM)] = exp(-|t|/n)^n=exp(-|t|) par independance des Xi
%% 5 Donc Mn suit une loi Cauchy, en particulier Mn converge en loi vers une loi de Cauchy.
clf;
n=500; Nech=2000;
M=zeros(Nech,1);
for k=1:Nech
    X=rand(n,1);
    Y=tan(pi*(X-0.5));
    M(k)=mean(Y);
end
plotrep(M)
hold on
fplot(@(t) atan(t)/pi+1/2,[-4 4],'r')
%%
%% Exercice 3
%% 3 
clf;
R=Polya(500,1,1);
X=R./(2+[0:500]');
Y=1-X;
Z=X./Y;
hold on
plot(X,'r')
plot(Y)
plot(Z,'g')
% On observe une convergence presque sure de X,Y et Z, vers quelque chose
% d'aleatoire : il suffit de refaire l'experience.
%% 4 
clf;
X=Polyaloi(500,500,1,1);
plotrep(X); %on observe une convergence vers la loi uniforme si r=b=1
figure;
X=Polyaloi(500,500,4,6);
plotrep(X); % si on change r et b ce n'est plus vrai
%% 5a 
% Rn est uniforme discrete sur {1,..,n+1} : cela se montre par recurrence
% en utilisant la formule des probabilites totales
% On peut l'illustrer par exemple pour n=4, avec un histogramme ou la fonction de
% repartition empirique :
clf;
R=zeros(3000,1);
for k=1:3000
    R(k)=1;
for l = 1:4
    R(k) = Urne(R(k),l-1,1,1); 
end
end
histo(R,5,1,1);
figure;
plotrep(R);
hold on;
stairs(1/5*[1:5],'r');
%% 5b Le calcul fait intervenir la somme d'une suite geometrique
%% 5c E[e^(itXn)] s'obtient en appliquant la formule precedente a (t/(n+2)).
% Il suffit ensuite de prendre la limite en utilisant un DL a l'ordre 1 :
% e^(it/(n+2)) = 1+it/(n+2) + o(1/n) : on voit que la fonction
% caracteristique de Xn converge vers (e^(it)-1)/(it), c'est a dire la
% fonction caracteristique d'une loi uniforme sur [0,1] : on a donc bien
% prouve la convergence en loi observee a la question 4
%% 6 La densite beta(2,1) sur [0,1] est 2x, donc la fonction de repartition est x^2.
clf;
X=Polyaloi(500,500,2,1);
plotrep(X); 
hold on
fplot(@(t) t.^2,[0 1],'r');
% On peut tester avec d'autres valeurs de r et b, par exemple si on prend
% r=5 et b=1 
figure
X=Polyaloi(500,500,5,1);
plotrep(X); 
hold on
fplot(@(t) t.^5,[0 1],'r');
% Avec r=2, b=2 on peut calculer la fonction de repartition 3x^2-2x^3
figure
X=Polyaloi(500,500,2,2);
plotrep(X); 
hold on
fplot(@(t) 3*t.^2-2*t.^3,[0 1],'r');
%% Et avec r=2 et b=5 :
figure
X=Polyaloi(500,500,2,5);
plotrep(X); 
hold on
fplot(@(t) 30*(t.^2/2-4*t.^3/3+3*t.^4/2-4*t.^5/5+t.^6/6),[0 1],'r');
%%
%% Exercice 4
%1 Les calculs sur les chaines de Markov fournissent :
T=[0 0.4 0 0 0 0 0; 0.6 0 0.4 0 0 0 0 ; 0 0.6 0 0.4 0 0 0 ; 0 0 0.6 0 0.4 0 0 ; 0 0 0 0.6 0 0.4 0 ;0 0 0 0 0.6 0 0.4; 0 0 0 0 0 0.6 0 ];
M=inv(eye(7,7)-T);
B=[0.6 0 ; 0 0; 0 0 ;0 0;0 0; 0 0; 0 0.4 ];
M*B(3,2)
%% 2 La on peut calculer a la main :
0.4^2 + 0.4^2*0.6
%% 3  Les calculs sur les chaines de Markov fournissent :
T=[ 0 0.4 0 0 0 ; 0.6 0 0.4 0 0 ; 0 0.6 0 0.4 0 ; 0 0 0.6 0 0.4 ; 0 0.6 0 0 0 ]
M=inv(eye(5,5)-T)
B=[0.6 0 ; 0 0 ; 0 0 ; 0 0 ; 0 0.4 ]
M*B(3,2)
% La 2eme strategie est la plus efficace
%% Exercice 5
%% 1
P=[0 1 0 0 0 0;1/5 0 4/5 0 0 0;0 2/5 0 3/5 0 0;0 0 3/5 0 2/5 0;0 0 0 4/5 0 1/5;0 0 0 0 1 0] 
%% 2
Bin=dbinom([0:5],5,1/2)
Bin*P
%% 3 La chaine est irreductible et de periode 2
%% 4
X0=[1 0 0 0 0 0]
X20=X0*P^20
X50=X20*P^30
X51=X50*P
% La periode 2 fait que ces vecteurs ont des zeros soit aux places paires
% soit aux places impaires, donc il n'y a pas convergence vers la loi
% invariante. Mais on a bien convergence des soussuites X2n et  X(2n+1)
%% 5
X0=1/6*ones(1,6)
X20=X0*P^20
X50=X20*P^30
X51=X50*P
% Ici il y a bien convergence en loi vers la loi invariante
%% 6
X=zeros(1,100);
for k=1:99
    X(k+1) = Ehrenfest(X(k),5);
end
clf
plot(X)
%% 7
clf
X=zeros(1,5000);
for k=1:4999
    X(k+1) = Ehrenfest(X(k),5);
end
%m=0
Erg0=cumsum(X==0)./[1:5000];
Bin0=Bin(1)*ones(1,5000);
subplot(2,3,1)
plot(Erg0)
hold on
plot(Bin0)
%m=1
Erg1=cumsum(X==1)./[1:5000];
Bin1=Bin(2)*ones(1,5000);
subplot(2,3,2)
plot(Erg1)
hold on
plot(Bin1)
%m=2
Erg2=cumsum(X==2)./[1:5000];
Bin2=Bin(3)*ones(1,5000);
subplot(2,3,3)
plot(Erg2)
hold on
plot(Bin2)
%m=3
Erg3=cumsum(X==3)./[1:5000];
Bin3=Bin(4)*ones(1,5000);
subplot(2,3,4)
plot(Erg3)
hold on
plot(Bin3)
%m=4
Erg4=cumsum(X==4)./[1:5000];
Bin4=Bin(5)*ones(1,5000);
subplot(2,3,5)
plot(Erg4)
hold on
plot(Bin4)
%m=5
Erg5=cumsum(X==5)./[1:5000];
Bin5=Bin(6)*ones(1,5000);
subplot(2,3,6)
plot(Erg5)
hold on
plot(Bin5)
%La chaine semble effectivement ergodique
%% 8
%Cette nouvelle chaine est bien irreductible, et aperiodique. On sait donc
%que quelle que soit la distribution initiale, il y a convergence en loi
%vers l'unique loi invariante, dont on peut verifier que c'est toujours la
%loi binomiale.

P=(5/6).*P+(1/6).*eye(6);
Bin=dbinom([0:5],5,1/2)
Bin*P
%%
X0=[1 0 0 0 0 0]
X20=X0*P^20
X50=X20*P^30
X51=X50*P
% Il y a bien convergence
%%
X0=1/6*ones(1,6)
X20=X0*P^20
X50=X20*P^30
X51=X50*P
% Ici encore il y a bien evidemment convergence en loi vers la loi invariante
%%
X=zeros(1,100);
for k=1:99
    X(k+1) = Ehrenfest2(X(k),5);
end
clf
plot(X)
%% 
clf
X=zeros(1,5000);
for k=1:4999
    X(k+1) = Ehrenfest2(X(k),5);
end
%m=0
Erg0=cumsum(X==0)./[1:5000];
Bin0=Bin(1)*ones(1,5000);
subplot(2,3,1)
plot(Erg0)
hold on
plot(Bin0)
%m=1
Erg1=cumsum(X==1)./[1:5000];
Bin1=Bin(2)*ones(1,5000);
subplot(2,3,2)
plot(Erg1)
hold on
plot(Bin1)
%m=2
Erg2=cumsum(X==2)./[1:5000];
Bin2=Bin(3)*ones(1,5000);
subplot(2,3,3)
plot(Erg2)
hold on
plot(Bin2)
%m=3
Erg3=cumsum(X==3)./[1:5000];
Bin3=Bin(4)*ones(1,5000);
subplot(2,3,4)
plot(Erg3)
hold on
plot(Bin3)
%m=4
Erg4=cumsum(X==4)./[1:5000];
Bin4=Bin(5)*ones(1,5000);
subplot(2,3,5)
plot(Erg4)
hold on
plot(Bin4)
%m=5
Erg5=cumsum(X==5)./[1:5000];
Bin5=Bin(6)*ones(1,5000);
subplot(2,3,6)
plot(Erg5)
hold on
plot(Bin5)
