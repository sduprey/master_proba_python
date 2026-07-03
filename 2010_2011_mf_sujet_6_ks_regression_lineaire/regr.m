function [ droite,s,Ica,Icb] = regr(Y,X )
%UNTITLED10 Summary of this function goes here
%   Detailed explanation goes here
n=length(X);
u=ones(1,n)';
M(:,1)=u; M(:,2)=X;
h=M'*M;
g=h^(-1);
droite=g*M'*Y
s=norm(Y-M*droite)/sqrt(n-2)
eca=sqrt(g(1,1))*s;
Ica=[droite(1)-eca*qt(0.975,n-2), droite(1)+eca*qt(0.975,n-2)]
ecb=sqrt(g(2,2))*s;
Icb=[droite(2)-ecb*qt(0.975,n-2), droite(2)+ecb*qt(0.975,n-2)]

plot(X,Y,'o');
hold on;
plot(X,droite(1)*u+droite(2)*X,'r');
plot(X,Ica(1)*u+Icb(1)*X,'g');
plot(X,Ica(2)*u+Icb(2)*X,'m');

hold off;

figure
A=h(1,1); B=h(2,2); C=2*h(1,2);
D=2*s^2*qf(0.975,2,n-2);
t=[0:2*pi/300:2*pi];
r=sqrt(D./(A*cos(t).^2+B*sin(t).^2+C*cos(t).*sin(t)));
xel=droite(1)+r.*cos(t);
yel=droite(2)+r.*sin(t);
plot(xel,yel);
end

