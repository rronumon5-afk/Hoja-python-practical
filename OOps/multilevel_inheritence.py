class grandfather:
    def feature_grandfather(self):
        print("feature_grandfather")
        
class father(grandfather):
    def feature_father(self):
        print("feature_father")
        
class child (father):
    def feature_child(self):
        print("feature_child")
        
c=child()
c.feature_father() 
c.feature_grandfather()                        
c.feature_child()