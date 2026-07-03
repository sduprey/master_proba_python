function [ X ] = rbernou(n,p )
% Genere un n-echantillon de Bernoulli de parametre p
X=rand(1,n)<p;
end

