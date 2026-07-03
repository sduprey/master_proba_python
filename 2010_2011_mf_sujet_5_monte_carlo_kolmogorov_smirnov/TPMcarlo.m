%% Methode de MonteCarlo

U=rand(1,500);
X=4*sqrt(1-U.^2);
mean(X)
std(X)
Intconf(X,std(X),0.05)

%%
N=0;
for k=1:100
    U=rand(1,500);
X=4*sqrt(1-U.^2);
Ic=Intconf(X,std(X),0.05);
N=N+(pi>Ic(1) && pi<Ic(2));
end
N
% N suit une loi binomiale (100,0.95)

%%
%E[X]=pi, Var(X)=16*(pi/4)(1-pi/4)=pi(4-pi)
U1=rand(1,500); U2=rand(1,500); 
X=4*((U1.^2 + U2.^2)<1);
mean(X)
std(X)
s=sqrt(mean(X)*(4-mean(X)))
Intconf(X,s,0.05)
%%
U1=rand(1,500); U2=rand(1,500); U3=rand(1,500);
X=6*((U1.^2 + U2.^2+U3.^2)<1);
mean(X)
Intconf(X,std(X),0.05)
%%
U1=2*rand(1,500)-1; U2=2*rand(1,500)-1; U3=2*rand(1,500)-1;
X=8*U1.^2.*((U1.^2 + U2.^2+U3.^2)<1);
mean(X)
Intconf(X,std(X),0.05)
% par symetrie et changement de variable spherique on trouve 3J=4pi/5
4*pi/15

%% Kolmogorov Smirnov

X=randn(1,100);
DKS(X,@pnorm,0.05)
X=rand(1,100);
DKS(X,@pnorm,0.05)
DKS(X,@(x)x,0.05)
X=rexp(100,1);
DKS(X',@(x)1-exp(-x),0.05)

%%
X=randn(1,1000);
Ic=Intconf(X,1,0.05)
DKS(X,@(x)pnorm(x,Ic(1),1),0.05)
DKS(X,@(x)pnorm(x,Ic(2),1),0.05)
