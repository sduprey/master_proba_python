for i =1:3
    for j=1:3
        M(i,j)=1/(i+j-1);
    end
end
M
det(M)
inv(M)
eig(M)