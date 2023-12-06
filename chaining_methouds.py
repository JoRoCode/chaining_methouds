class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        
    def Display_info(self):
            print(self.first_name)
            print(self.last_name)
            print(self.email)
            print(self.age)
            print(self.is_rewards_member)
            print(self.gold_card_points)
            return self
        
    def Enroll(self):
        if self.is_rewards_member == True:
            print("user already a member.")
            return self
        else:
            self.gold_card_points += 200
            self.is_rewards_member = True
            return self
        
    def Spend_points(self,amount):
        if self.gold_card_points < amount:
            print("We are sorry, but you do not have enough gold points accrued.")
            return self
        else:
            self.gold_card_points -= amount
            return self
        
        
Phil = User("Phil", "Stevenson", "philshero@pigsrus.com", 126)
Steven = User("Steven", "Phillips", "stevepvillian@yaycats.com", 31)
Mary = User("Mary Jo Sassafrass", "Johnson-Decker-Ashton", "ohmary@blessyourheart.com", 6)
Jed = User("Jed", "Ham", "ilovesamiches@sandwichmeat.com", 88)
        
        
Phil.gold_card_points = Phil.gold_card_points + 147392
        
Steven.Display_info().Enroll().Spend_points(80).Display_info().Enroll()
Phil.Display_info().Spend_points(50).Display_info()
Mary.Display_info().Spend_points(40).Display_info()
Jed.Display_info()