function pos = Rz(theta,d)
    %UNTITLED5 Summary of this function goes here
    %   Detailed explanation goes here
    pos = [cos(theta), -sin(theta), 0, d(1);
         sin(theta),  cos(theta), 0, d(2);
         0         ,  0         , 1, d(3);
         0         ,  0         , 0, 1];
end

