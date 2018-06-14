import numpy as np
import particle as par

class molecule:
      
    def __init__(self, x1, x2, m1, m2, k, l):
       
        self.p1 = par.Particle(x1, m1)   # initializing particle 1
        self.p2 = par.Particle(x2, m2)   # initializing particle 2
        self.k = k                       # spring constant of the bond
        self.L0 = l                      # equilibrium length of bond
        self.displ = []
        self.force = []
        
    def get_displ(self):
        self.displ = self.p2.pos - self.p1.pos #maybe sign should beoppositeThis seems r
        return self.displ
            
    def get_force(self):
        self.force = []
        for i,e in enumerate(self.get_displ()):
            self.force.append(1*(self.k)*self.displ[i])
        return self.force