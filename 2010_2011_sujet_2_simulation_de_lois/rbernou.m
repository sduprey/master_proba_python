function [ X ] = rbernou(n,m,p )
% Genere un n-echantillon de Bernoulli de parametre p
X=rand(n,m)<p;
end

