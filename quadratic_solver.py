def get_new_velocity(mass, prev_vel, force, i):
    a = 0 - (mass/2)
    b = (force * segment_len_arr[i-1] / prev_vel ) + (mass * prev_vel)
    c = (K_a * A_m * segment_len_arr[i-1] * pow(prev_vel + (v_w * math.sin(abs(theta_rider[t] - theta_w))), 2) 
    + (g * gradient_rider[i] * mass * segment_len_arr[i-1]) + (K_r * mass * segment_len_arr[i-1]) 
    + ((mass * pow(prev_vel,2)) / 2))
    return (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
