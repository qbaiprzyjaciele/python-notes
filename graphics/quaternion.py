import math

class Quaternion:
    def __init__(self,w=0,x=0,y=0,z=0):
        self.w = w
        self.x = x
        self.y = y
        self.z = z
    
    def multiply(self,other):
        multiplied = Quaternion()
        multiplied.w = self.w*other.w - self.x*other.x - self.y*other.y - self.z*other.z
        multiplied.x = self.w*other.x + self.x*other.w + self.y*other.z - self.z*other.y
        multiplied.y = self.w*other.y - self.x*other.z + self.y*other.w + self.z*other.x
        multiplied.z = self.w*other.z + self.x*other.y - self.y*other.x + self.z*other.w
        return multiplied;    
    
    def normalize(self):
        normalized = Quaternion()
        length = self.calcLength()
        normalized.w = self.w/length
        normalized.x = self.x/length
        normalized.y = self.y/length
        normalized.z = self.z/length
        return normalized

    def calcLength(self):
        return math.sqrt(self.w*self.w + self.x*self.x + self.y*self.y + self.z*self.z)

q1 = Quaternion(1.0, 0.2, 5.3, 2)
q2 = Quaternion(2.3, 0.1, 1.2, 1)

print("q1=[%s %s %s %s], length=%s" % (q1.w,q1.x,q1.y,q1.z,q1.calcLength()))
print("q2=[%s %s %s %s], length=%s" % (q2.w,q2.x,q2.y,q2.z,q2.calcLength()))
q3 = q1.multiply(q2)

print("q3=[%s %s %s %s], length=%s" % (q3.w,q3.x,q3.y,q3.z,q3.calcLength()))

q4 = q3.normalize()

print("q4=[%s %s %s %s, length=%s" % (q4.w, q4.x, q4.y, q4.z, q4.calcLength()))