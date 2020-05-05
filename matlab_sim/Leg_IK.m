function Theta = Leg_IK(xyz,L)
    %Inverse kinematic model of leg, with angles theta(1;2;3)
    %   L0: horizontal distance between the second joint (up down on hip) 
    %   and the end effector
    %   D:  absolute distance between the second joint (up down on
    %   hip) and the end effector
    %   Alpha: internal angle formed by the thigh and shin
    %   Beta: Angle fored between end effector and horizontal about theta2
    %   Gamma: Internal angle between thigh and end effector about theta2

    Theta = zeros(3,1);
    Theta(1) = atan2(xyz(2),xyz(1));

    
    L0 = sqrt(xyz(1)^2+xyz(2)^2)-L(1);
    D = sqrt(L0^2+xyz(3)^2);
    Alpha = acos((-D^2 + L(2)^2+L(3)^2)/(2*L(2)*L(3)));
    Beta = atan2(xyz(3),L0);
    Gamma = asin(L(3)*sin(Alpha)/D);

    Theta(2) = Gamma+Beta;
    Theta(3) = pi+Alpha;
end

