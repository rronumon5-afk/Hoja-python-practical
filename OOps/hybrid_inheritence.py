class grandfather:
    def feature_grandfather(self):
        print("wise and experienced")
class father (grandfather):
    def feature_father(self):
        print("experiencing and working")
class aunt(grandfather):
    def feature_aunt(self):
        print("caring")
class child(father,aunt):
    def feature_child(self):
        print("energetic")
                                
c=child()
c.feature_grandfather()
c.feature_father()
c.feature_aunt()
c.feature_child()                            