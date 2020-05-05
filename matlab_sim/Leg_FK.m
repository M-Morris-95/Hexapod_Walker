function pos = Leg_FK(theta, Rz_off, d_off, L)
    %UNTITLED3 calculate forward kinematics of a leg
%     theta = deg2rad([90, 90, -90]);



    shoulder_len =L(1);
    thigh_len = L(2);
    shin_len = L(3);
    
    d = [0,0,0,0];
    alpha = [0, deg2rad(90),0,0];
    r = [d_off, shoulder_len, thigh_len, shin_len];
    theta = [Rz_off; theta];

    pos = zeros(4, 4, 3);
    pos(:,:,1) = DH(d(1), theta(1), alpha(1), r(1));

    for i = 2:4
        pos(:,:,i) = pos(:,:,i-1) * DH(d(i), theta(i), alpha(i), r(i));
    end

end

