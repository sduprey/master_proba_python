%%Chaine d'Ehrenfest
X=zeros(1,500);
X(1)=1;
for n=2:500
    X(n)=Ehrenfest3(5,X(n-1));
end
plot(X);
%%
Ehr900=zeros(1,5000);
Ehr1000=zeros(1,5000);
for k=1:5000
    C=1;
    for n=2:900 
        C=Ehrenfest3(5,C);
    end
    Ehr900(k)=C;
    for n=901:1000
    C=Ehrenfest3(5,C);
    end
    Ehr1000(k)=C;
end
plotrep(Ehr900);
hold on
plotrep(Ehr1000);
stairs([0:5],pbinom([0:5],5,0.5),'r');
hold off

%% Processus de Poisson
X=zeros(1,500);
X=rexp(500,1);
stairs(cumsum(X),[1:500]);%Dessin de Nt en fonction de t 
                            %(en fait Tn en abscisse et N_Tn en ordonnee)
plot(cumsum(X),[1:500]./cumsum(X)','r'); %Nt/t en fonction de t
hold on;
plot(ones(1,500));%la limite theorique
hold off;
Ic=[500/sum(X)-qnorm(0.975)*sqrt(500)/sum(X),500/sum(X)+qnorm(0.975)*sqrt(500)/sum(X)]

%% Minimum de lois uniformes
X=rand(1,500);
m=zeros(1,500);
m(1)=X(1);
for k=2:500
    if X(k)<m(k-1) m(k)=X(k);
    else m(k)=m(k-1);
    end;
end;
plot(m);% convergence ps vers 0
m=zeros(1,5000);
for k=1:5000
    X=rand(1,500);
    m(k)=500*min(X);
end;
plotrep(m);%conv en loi vers une loi exp.
hold on
fplot(@(x) 1-exp(-x),[0 3],'r');
hold off

%% File d'attente
X=zeros(1,1000);
X(1)=0;
for k=2:1000
    X(k)=Fattente(X(k-1),0.1,0.6);
end;
plot(X,'o');
hold on;
X(1)=0;
for k=2:1000
    X(k)=Fattente(X(k-1),0.5,0.5);
end;
plot(X,'r+');
X(1)=0;
for k=2:1000
    X(k)=Fattente(X(k-1),0.6,0.1);
end;
plot(X,'g*');
hold off;
%% 
plotergo(0.1,0.6,10000);%la chaine semble bien ergodique
plotergo(0.5,0.55,10000);
%%
convattente(0.1,0.6) %il y a bien convergence en loi vers la loi pi
convattente(0.5,0.5) % on n'observe pas de convergence en loi
convattente(0.6,0.1) % on n'observe pas de convergence en loi