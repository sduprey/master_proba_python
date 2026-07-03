%% Test de comparaison de Kolmogorov Smirnov

X=rand(1,100);
frep2(X,0.4)
Y=rand(1,200);
DKS2(X,Y,0.05)
Y=randn(1,90);
DKS2(X,Y,0.05)

X=[0.2 3.8 7.6 4 4.1 -2.8 4.7 3.6 5.4 -0.2 1.6 5.6 -0.6 0.8 -5 0.1 2.9 3.7 3.9 1.1]
Y=[1.8 4 1.4 1.9 1.8 1.4 1.9 1.4 4.5 2.2 2.4 3.1 0.3 -1.4 0.4 2.3 0.2 1.5 4.8 0.6 1 1.5 5.5]
plotrep(X)
hold on
plotrep(Y)
hold off
DKS2(X,Y,0.05)

%% Regression lineaire

X=[1:50]/50;
Y=1+2*X+0.5*randn(1,50);
regr(Y',X')

Z=getdata(5);
regr(Z(:,2),Z(:,1))
I=[6,16,25]
Z(I,:)=[]
regr(Z(:,2),Z(:,1))

%% 
%(n-2)shat^2/s^2 est un chi2 a n-2 ddl
% Il est indep de (ahat,bhat) par Cochran : les 2 sous espaces sur lesquels
% on projette sont orthogonaux
% (ahat-a)/sqrt(var(ahat))s/shat  suit donc une loi de Student a n-2 ddl

%% 
g4=getdata(4)
X4=g4(:,1:3);
Y4=g4(:,4);
regr2(Y4,X4)
Y4=g4(:,5);
regr2(Y4,X4)
g11=getdata(11)
Y11=g11(:,7);
X11=g11(:,1:6);
regr2(Y11,X11)
