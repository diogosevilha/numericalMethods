import numpy as np

# Physical constants
g = 9.8
L = 2  # pend lenght
mu = 0.1 # air resist coef

theta_0 = np.pi/3  # 60 degrees
theta_dot_0 = 0    # No Initial angular velocity

# Definition of EDO  --- rate variation of variation of theta in a infinitesimal time  "theta_double_dot" ---
def get_theta_double_dot(theta, theta_dot):
    '''
    abstract the rate variation of variation of theta in a infinitesimal time  "theta_double_dot"
    '''
    return -mu * theta_dot - (g/L) * np.sin(theta)

# Solution of the diferential equation in a given time "t"
def theta(t):
    # Initialize changing values
    theta = theta_0
    theta_dot = theta_dot_0
    delta_t = 0.01 # Time step
    for time in np.arange(0, t, delta_t):
        theta_double_dot = get_theta_double_dot(
            theta, theta_dot
        )
        theta += theta_dot * delta_t
        print(theta)
        theta_dot += theta_double_dot * delta_t
    
    return theta     


run = theta(10)