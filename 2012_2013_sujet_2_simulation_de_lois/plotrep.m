function res = plotrep( X )
%plotrep dessine la fonction de repartition empirique de X
%   Detailed explanation goes here
n=length(X);
Y=sort(X);
stairs(Y,[1:n]/n)
end

