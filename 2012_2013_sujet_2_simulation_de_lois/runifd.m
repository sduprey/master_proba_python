function [ X] = runifd(n,N )
% genere une loi uniforme discrete sur {1,...,N}
X=ceil(N*rand(n,1));

end

