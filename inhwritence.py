class plane:
    def land(self):
         print("plane is landing")
    def takeoff(self):
         print("plane is taking off")
class passenger(plane):
     def carry_passenger(self):
          print("plane is carrying the passanger")
class cargo(plane):
     def carry_goods(self):
          print("plane is carry goods")
p=passenger()
p.land()
p.takeoff()
p.carry_passenger()
c=cargo
c.land()
c.takeoff()
c.carry_goods()
