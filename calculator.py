import numpy as np

# Universal artillery calculator
class Cannonball:
    def __init__(self, planet, m, R, C, v0, theta):
        """
        Parameters
        ----------
        planet: str
            'Earth' or 'Mars'
        m: float
            mass of the cannonbal (kg)
        R: float
            radius of the cannonball (m)
        C: float
            drag coefficient (unitless)
        v0: float
            initial velocity (m s^-1)
        theta: float
            initial angle (deg)
        """

        if planet == 'Earth':
            self.g     = 9.81	# m s^-2
            self.rho   = 1.22   # kg m^-3
        if planet == 'Mars':
            self.g     = 3.71   # m s^-2
            self.rho   = 0.20   # kg m^-3
        self.m     = 1.0	# kg
        self.C     = C	# unitless
        self.R     = R    # m
        self.h     = 0.001   # seconds
        self.theta = theta*(np.pi/180) # radians
        self.v0    = v0	# m s^-1
        self.const = (self.rho*C*np.pi*R**2)/(2.0*m)


    # define the equations of motion
    def f(self, r):
        x   = r[0]
        y   = r[1]
        vx  = r[2]
        vy  = r[3]
        fx  = vx
        fy  = vy
        fvx = -self.const*vx*np.sqrt(vx**2+vy**2)
        fvy = -self.g-self.const*vy*np.sqrt(vx**2+vy**2)
        return np.array([fx,fy,fvx,fvy],float)

    
    def RK(self):
        """
        Return x,y coordinates of the trajectory of the cannnonball by using fourth-order Runge-Kutta method
        """
        # containers for output
        r = np.array([0.0,0.0,self.v0*np.cos(self.theta),self.v0*np.sin(self.theta)],float)
        xpoints = []
        ypoints = []

        # use fourth-order Runge-Kutta
        while r[1]>=0:
            k1 = self.h*self.f(r)
            k2 = self.h*self.f(r+0.5*k1)
            k3 = self.h*self.f(r+0.5*k2)
            k4 = self.h*self.f(r+k3)
            r += (k1+2*k2+2*k3+k4)/6
            xpoints.append(r[0])
            ypoints.append(r[1])

        # output
        return xpoints, ypoints

