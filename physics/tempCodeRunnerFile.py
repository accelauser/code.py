
    def update(self):
        self.tt.setheading(self.phi) #muda o ângulo da direção da trajetória        
        self.tt.fd(self.v0) #anda pra frente    
        self.vy = round(math.sin(math.radians(self.phi)) * self.v0) + self.g
        self.vx = round((math.cos(math.radians(self.phi)) * self.v0))