# Get Student name And id using oops

class student_info:
    def info(self,id,name,subject):
        id = int(input("Enter Your id :"))
        name = input("Enter YOur Name :")
        subject = input("Enter Your Subject :")
        
class st1(student_info):
    
    def info(self, id, name, subject):
        return super().info(id, name, subject)
class st2(student_info):     
    def info(self, id, name, subject):
        return super().info(id, name, subject)
class st3(student_info):   
    def info(self, id, name, subject):
        return super().info(id, name, subject)
    

st1 = st1()

    
        
        
        