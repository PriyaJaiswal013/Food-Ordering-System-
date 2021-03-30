
class Menu:
    def __init__(self,no,name,price,veg):
        self.no=no
        self.name=name
        self.price=price
        self.veg=veg
class Hotel:
    def __init__(self,hotel_Name,menu_card):
        self.menu_card=menu_card
        self.hotel_name=hotel_Name
    def Veg_menu(self):
        for i in self.menu_card:
           if i.veg==True:
                 print(i.no,"\t",i.name,"\t",i.price)
    
    def Non_veg_menu(self):
        for i in self.menu_card:
           if i.veg==False:
                 print(i.no,"\t",i.name,"\t",i.price)
        
    def Order(self,orderDic):
        total=0
        for key,value in orderDic.items():
            for j in self.menu_card:
                if j.no==key:
                    total+=j.price*value
        if total>500:
            print("You will get coke free")
                

        print("Your total bill is Rs.",end="")
        return total
        
        
        
if __name__ =="__main__":
    m1=Menu(1,"Matar Paneer",100,True)
    m2=Menu(2,"Pav Bhaji",50,True)
    m3=Menu(3,"Veg Birayani",80,True)
    m4=Menu(4,"Pulav",100,True)
    m5=Menu(5,"Veg Tost Sandwich",50,True)
    m6=Menu(6,"Paneer Frankie",80,True)
    m7=Menu(7,"Noodles Frankie",35,True)
    m8=Menu(8,"Chicken Biryani",150,False)
    m9=Menu(9,"Butter Chicken",120,False)
    m10=Menu(10,"Chicken Tikka (Half)",120,False)
    m11=Menu(11,"Chicken Tikka (Full)",200,False)
    m12=Menu(12,"Egg Shawarma",60,False)
    l=[]
    l.append(m1)
    l.append(m2)
    l.append(m3)
    l.append(m4)
    l.append(m5)
    l.append(m6)
    l.append(m7)
    l.append(m8)
    l.append(m9)
    l.append(m10)
    l.append(m11)
    l.append(m12)
    h1=Hotel("Khana Khazana",l)
    print("Welcome to hotel",h1.hotel_name)
    print(" ")
    c=int(input("Enter 1 for Veg and 2 for NonVeg: "))
    if c==1:
        h1.Veg_menu()
    elif c==2:
        h1.Non_veg_menu()
    else:
        print("Invalid Input")
    
    dic={}
    print("Place your Order_no & Quantity for eg.10 2")
    a=input("Enter your choice and quantity space seperated: ")
    
    while a!= "q" :
        lis=a.split()
        dic[int(lis[0])]=int(lis[1])
    
        a=input("Enter again for continue or press q to Quit: ")
    
    print(h1.Order(dic))





















