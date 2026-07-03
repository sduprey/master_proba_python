%% I Convergence presque sure vers une constante
%% 2
X=rand(1,1000);
M=zeros(1,1000);
M(1)=X(1);
for i=2:1000
M(i)=max(M(i-1),X(i));
end;
plot(M);
% M converge ps vers 1
%% II Loi des grands nombres
%% 1
X=runifd(5000,6);
S=cumsum(X);
S2=S./[1:5000]';
%% 2
plot(S2)
hold on;
m=3.5;
plot([0,5000],[m,m],'r');
hold off;
%% 3 
X=rand(1,5000);
S=cumsum(X);
S2=S./[1:5000];
plot(S2)
hold on;
m=0.5;
plot([0,5000],[m,m],'r');
hold off;

%% III Question 1-2-3-4
clf
U=rand(1,30);
E=(U<1/2);
V=cumsum(E./2.^[1:30]);
plot(V);
hold on
U=rand(1,30);
E=(U<1/2);
V=cumsum(E./2.^[1:30]);
plot(V,'r');
%% Question 5
for i=1:2000
U=rand(1,30);
E=(U<1/2);
W(i)=sum(E./2.^[1:30]);
end
plotrep(W) % Convergence vers une loi uniforme sur [0,1]
%% Question 6
clf
U=rand(1,30);
E=(U<1/2)+(-1)*(U>1/2);
V=cumsum(E./2.^[1:30]);
plot(V);
hold on
U=rand(1,30);
E=(U<1/2)+(-1)*(U>1/2);
V=cumsum(E./2.^[1:30]);
plot(V,'r');
clf
for i=1:2000
U=rand(1,30);
E=(U<1/2)+(-1)*(U>1/2);
W(i)=sum(E./2.^[1:30]);
end
plotrep(W)

%% IV Moivre Laplace
%% 2
clf;
P=MLaplace(90,0.8,[-3:0.1:3]);
P2=pnorm([-3:0.1:3]);
plot([-3:0.1:3],P); hold on; plot([-3:0.1:3],P2); hold off;
%% 3
clf;
P=MLaplace(1000,0.8,[-3:0.1:3]);
P2=pnorm([-3:0.1:3]);
plot([-3:0.1:3],P); hold on; plot([-3:0.1:3],P2);
%%
clf;
P=MLaplace(90,0.99,[-3:0.1:3]);
P2=pnorm([-3:0.1:3]);
plot([-3:0.1:3],P); hold on; plot([-3:0.1:3],P2);
