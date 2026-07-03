function res=discrete1(n)
% Remarque : 5/6 = 1/2+ 1/3
X=rand(1,n);
res=(X<1/2) + 2*(X>1/2 & X<5/6) + 3*(X>5/6);
% la ligne precedente renvoit 1 si X<1/2, 2 si 1/2<X<(1/2+1/3), 3 si
% X>1/2+1/3
end
