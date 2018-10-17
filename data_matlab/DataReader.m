load('realitymining.mat');

fid = fopen( 'user_locs.csv', 'w' );

fprintf(fid, 'User_id, date, areaID.cellID\n');
for i = 2:106
    for m = 1: size(s(i).locs,1)
        a = sprintf('%.9f',s(i).locs(m,1));
        b = sprintf('%.5f',s(i).locs(m,2));
        fprintf(fid, '%d,%s,%s\n',i-1, a, b);
    end
end