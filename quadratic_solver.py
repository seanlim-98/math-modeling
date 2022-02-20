# Updated quadratic function
def get_new_velocity(mass, prev_vel, force, i):
    a = (1 / 2) * (mass * prev_vel / segment_len_arr[i-1])
    b = 0 - force
    c = (K_a * A_m * prev_vel * pow(prev_vel + (v_w * math.sin((math.pi / 2) - abs(theta_rider[t] - theta_w))), 2) 
    - (g * gradient_rider[i] * mass * prev_vel) + (K_r * mass * prev_vel) 
    - ((mass * pow(prev_vel,3)) / (2 * segment_len_arr[i-1]))
    return (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
