L = [0.03375, 0.065, 0.1];

natural_stance = [0.12; 0 ;-0.04];



iters = linspace(0,2*pi,100);


T = 5;
xmin = -0.02;
xmax = 0.02;
zmin = -0.02;
zmax = 0.02;
precision = 10;
t_steps = linspace(0,T,precision);
x1 = zeros(precision,1);
x2 = x1;
z1 = x1;
z2 = x1;
for i = 1:precision/2
    t = t_steps(i);
    x1(i) = xmin + t*(xmax-xmin)/(T/2);
    x2(i) = xmax - t*(xmax-xmin)/(T/2);
    z1(i) = -8*t^2/625+4*t/125-0.01;
    z2(i) = -0.01;
    
end
for i = 1:precision/2
    t = t_steps(i);
    x2(i+precision/2) = xmin + t*(xmax-xmin)/(T/2);
    x1(i+precision/2) = xmax - t*(xmax-xmin)/(T/2);
    z2(i+precision/2) = -8*t^2/625+4*t/125-0.01;
    z1(i+precision/2) = -0.01;
end

plot(x1, 'r')
hold on
plot(x2, 'b')
plot(z1,'r')
plot(z2, 'b')


z_pos = sin(iters) * 0.05;

figure(1)
clf
set(gca,'DataAspectRatio',[1 1 1])

while(1)
for iter =  1:precision
    z = z_pos(iter);

    offset = [rot_z(natural_stance, 45),rot_z(natural_stance, 90),rot_z(natural_stance, 135),rot_z(natural_stance, -135),rot_z(natural_stance, -90),rot_z(natural_stance, -45)];
                
    desired_pos = [x1(iter), x2(iter), x1(iter), x2(iter), x1(iter), x2(iter);
               0,0,0,0,0,0;
                z1(iter),  z2(iter),  z1(iter),  z2(iter),  z1(iter),  z2(iter)]
 
            
    desired_pos =   offset +desired_pos;

    
    Thetas = zeros(3,6);
    true_pos = zeros(4,4,4,6);
    theta_off = deg2rad([-30,-90,-120,120,90,30]);
    offset = 0;

    for k = 1:6
        rot_mat = [cos(theta_off(k)),  sin(theta_off(k)), 0;
       -sin(theta_off(k)), cos(theta_off(k)), 0;
        0,0,1];
        desired_pos(:,k) = rot_mat*desired_pos(:,k);

        Thetas(:,k) = Leg_IK(desired_pos(:,k),L);

        true_pos(:,:,:,k) = Leg_FK(Thetas(:,k), theta_off(k), offset, L);
    end


    colors = [0,0,1;
            0,0,0;
            1,0,0;
            0,1,0;
            1,1,0;
            0,1,1;
            1,0,1;
            1,1,1];
        
        
    clf
    set(gca,'DataAspectRatio',[1 1 1])
    set(gca,'XMinorTick','on','YMinorTick','on','ZMinorTick','on')
    grid on
    grid minor
    grid on
    grid minor
    
    for j = 1:6
        for i = 1:3
            v1 = true_pos(1:3,4,i  ,j);
            v2 = true_pos(1:3,4,i+1,j);
            v=[v2,v1];
            plot3(v(1,:),v(2,:),v(3,:), 'color',colors(j,:))
            hold on
        end
    end
    hold off
    xlabel('x')
    ylabel('y')
    zlabel('z')
    xlim([-0.15,0.15]);
    xlim([-0.15,0.15]);
    zlim([-0.15,0.15]);
     pause(0.001)
end
end



