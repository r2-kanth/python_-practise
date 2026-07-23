class programmer:
    company = "Microsoft"
    def __init__(self, name , salary , pincode , ):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = programmer("Ravi " , 1200000 , 520014)
print(p.name  , p.salary , p.pincode)

r= programmer("Sanjay" , 1400000 , 520009)
print(p.name , p.salary , p.pincode)

o = programmer("vk " , 3400000  , 540076)
print(p.name ,p.salary , p.pincode)