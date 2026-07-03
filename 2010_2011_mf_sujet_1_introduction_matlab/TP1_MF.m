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
[1:-0.5:-2]
%% 2
1+1:5
1+(1:5)
%% 
b=A(2,:)
c=A(:,3)
B=A(1:2,1:2)
%% 3
C=A(:,1:2)
%% Operations sur les matrices
help elmat
length(A)
C=A'
A+C
A*C
%%
n=4;I4=eye(n)
B=zeros(n)
D=ones(n)
p=2;A^p
det(A),trace(A),eig(A)
ans
%% 4
E=5*ones(3)
%% 5
A(:,1)'*A(:,2)
%%
A>2
%% 6
rca=sqrt(2:2:10)
%% Utilisation de .
A^2
A.^2
%%
A*C
A.*C
%% 7-8
V=[1:10].^2
W=1./[1:10]
%% Boucles - 9
M=zeros(3);
for i =1:3
    for j=1:3
        M(i,j)=1/(i+j-1);
    end
end
M
%%
det(M)
inv(M)
eig(M)
%% Representations graphiques
t=0:1/10:3; plot(t,exp(t)+3)
%%
t=0:1/10:3; plot(t,exp(t),t,1+t)
%% 11
plot(t,cos(t),t,sin(t),t,t.^2)
% ou bien
%% 11
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
fzero(@toto,0)
%% 12
fplot(@q12,[0 1])
%% 12
quad(@q12,0,1)
%% 12
pi/2-1
%%
toto2=@(x)cos(x).^2-sin(x).^2;
quad(toto2,0,pi)
fzero(@(x)x.^3-3,0)
%% 13
fzero(@(x)exp(x)-3*x,0)
%% Statistiques
rand
randn
X=rand(1000,1);
s=sum(X)
m=mean(X)
v=var(X)
sigma=std(X)
%% 14
mean(X.^3)
%Z=(X-m)/sigma;
%mean(Z),std(Z)
%% Histogrammes 15
help hist
X=rand(100,1);
histo(X)
%%
X=rand(1000,1);
figure
histo(X)
%%
X=rand(10000,1);
figure
histo(X,100,0,1)
figure
histo(X,20,0,1)
%%
X=rand(100000,1);
figure
histo(X,100,0,1)
hold on
histo(X,1000,1,1)
hold off

%% 16
X=randn(1000,1);
histo(X,20,0,1)
hold on
fplot(@(x)1./sqrt(2*pi)*exp(-x.^2./2),[-3 3],'r')
% ou bien
fplot('dnorm',[-3 3],'g')
hold off
mean(X)
std(X)