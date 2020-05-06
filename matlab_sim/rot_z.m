function pos = rot_z(xyz,theta)
    mat = [cosd(theta),  sind(theta), 0;
           -sind(theta), cosd(theta), 0;
           0,0,1];
    pos = mat*xyz;
end