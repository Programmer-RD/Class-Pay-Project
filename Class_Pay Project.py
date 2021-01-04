import datetime
import pickle

print(" < > Welcome to SCI Pay Calculator < > ")
Name = input(" > What is your Name ? \n > ")
age = int(input(" > How old are you ? \n > "))
if age < 18:
    quit()
    exit()
elif age > 18:
    pass
with open("Names.txt", "ab") as bg:
    pickle.dump(Name, bg)
    pickle.dump(age, bg)
    pickle.dump(" \n ", bg)


class Pay(object):
    def __init__(
        self, paid, unpaid, price, type_of_money, discount_class_owners, discount
    ):
        self.paid = float(paid)
        self.unpaid = float(unpaid)
        self.total = paid + unpaid
        self.cost = float(price)
        self.money_type = type_of_money
        self.negative_percentage = float(discount_class_owners)
        self.discount = discount * self.total

    def new_paid(self, paid_new):
        self.paid = paid_new

    def new_unpaid(self, unpaid_new):
        self.unpaid = unpaid_new

    def new_cost(self, new_cost):
        self.cost = new_cost

    def new_money_type(self, new_money_type):
        self.money_type = new_money_type

    def new_total(self):
        if self.paid > self.unpaid:
            self.total = self.paid + self.unpaid
        elif self.unpaid > self.paid:
            self.total = self.unpaid + self.paid

    def new_discount_owners(self, new_discount_owners):
        self.negative_percentage = new_discount_owners

    def new_discount(self, new_discounts):
        self.discount = new_discounts * self.total


class Prices(Pay):
    def Total(self):
        global cc
        if self.total > self.cost:
            c = self.total * self.cost
            print(f" > Total Collection (Without Discounts): {c} {self.money_type} \n ")
            print(f" > Total Collection (With Discounts) : {c - self.discount} \n ")
        else:
            c = self.cost * self.total
            print(f" > Total Collection (Without Discounts): {c} {self.money_type} \n ")
            print(f" > Total Collection (With Discounts) : {c - self.discount} \n ")
        if c < self.negative_percentage and 100:
            cc = self.negative_percentage / 100 * c
            print(
                f" > The Commission from the Collection for the institute (Without Discount): {self.money_type} {cc} \n "
            )
            print(
                f" > The Commission from the Collection for the institute (With Discount): {cc - self.discount} \n "
            )
        elif c > self.negative_percentage and 100:
            cc = c * self.negative_percentage / 100
            print(
                f" > The Commission from the Collection for the institute (Without Discount): {self.money_type} {cc} \n "
            )
            print(
                f" > The Commission from the Collection for the institute (With Discount): {cc - self.discount} \n "
            )
        if cc < c:
            ccc = c - cc
            print(
                f" > Allowance to the teacher (without discount) : {self.money_type} {ccc} \n "
            )
            print(
                f" > TAllowance to the teacher (with discount) : {ccc - self.discount} \n "
            )
        else:
            ccc = cc - c
            print(
                f" > Allowance to the teacher (without discount) : {self.money_type} {ccc} \n "
            )
            print(
                f" > TAllowance to the teacher (with discount) : {ccc - self.discount} \n "
            )
        quit_or_again = input(" > Do you want to quit or get more results ? \n > ")
        if (
            quit_or_again == "quit"
            or quit_or_again == "Quit"
            or quit_or_again == "q"
            or quit_or_again == "Q"
            or quit_or_again == "QuiT"
        ):
            quit()
        else:
            Enter_data()

    def Paid(self):
        global z, zzz
        if self.paid > self.cost:
            z = self.paid * self.cost
            print(f" > Paid : {self.money_type} {z} \n ")
            print(
                f" > Paid with Discount : {self.money_type} {z - self.negative_percentage} \n "
            )
        elif self.paid < self.cost:
            z = self.cost * self.paid
            print(f" > Paid : {self.money_type} {z} \n ")
            print(
                f" > Paid with Discount : {self.money_type} {z - self.negative_percentage} \n "
            )
        if self.negative_percentage and 100 > z:
            zzz = self.negative_percentage / 100 * z
        elif self.negative_percentage and 100 < z:
            zzz = z * 100 / self.negative_percentage
        if z < self.negative_percentage and 100:
            zzz = self.negative_percentage / 100 * z
            print(f" > The Commission is :  {self.money_type} {zzz} \n ")
            print(
                f" > The Commission with discount is : {zzz - self.negative_percentage} \n "
            )
        elif z > self.negative_percentage and 100:
            zzz = z * self.negative_percentage / 100
            print(f" > The Commission is :  {self.money_type} {zzz} \n ")
            print(
                f" > The Commission with discount is : {zzz - self.negative_percentage} \n "
            )
        if zzz < z:
            zzzz = z - zzz
            print(f" > The Commission for the Teacher : {self.money_type} {zzzz} \n ")
            print(
                f" > The Commission with discount to the teacher is : {zzz - self.negative_percentage} \n "
            )
        else:
            zzzz = zzz - z
            print(f" > The Commission for the Teacher : {self.money_type} {zzzz} \n ")
            print(
                f" > The Commission with discount to the teacher is : {zzz - self.negative_percentage} \n "
            )
        quit_or_again = input(
            " > Do you want to quit_or_again or get more results ? \n > "
        )
        if (
            quit_or_again == "quit"
            or quit_or_again == "Quit"
            or quit_or_again == "q"
            or quit_or_again == "Q"
        ):
            quit()
        else:
            Enter_data()

    def Unpaid(self):
        global yy, y
        if self.paid > self.cost:
            y = self.paid * self.cost
            print(f" > UnPaid : {y} \n ")
        elif self.paid < self.cost:
            y = self.cost * self.paid
            print(f" > UnPaid : {y} \n ")
        if y < self.negative_percentage and 100:
            yy = self.negative_percentage / 100 * y
            print(f" > The Commission is :  {self.money_type} {yy} \n ")
        elif z > self.negative_percentage and 100:
            yy = z * self.negative_percentage / 100
            print(f" > The Commission is :  {self.money_type} {yy} \n ")
        if yy < y:
            yyy = y - yy
            print(f" > The Commission for the Teacher : {self.money_type} {yyy} \n ")
        else:
            yyy = y - yy
            print(f" > The Commission for the Teacher : {self.money_type} {yyy} \n ")
        quit_or_again = input(
            " > Do you want to quit_or_again or get more results ? \n > "
        )
        if (
            quit_or_again == "quit"
            or quit_or_again == "Quit"
            or quit_or_again == "q"
            or quit_or_again == "Q"
        ):
            quit()
        else:
            Enter_data()

    def percentages(self):
        # Paid
        print(" > Paid : ")
        zz = 100 / (self.paid + 0)
        print(f" > The Percentage of children that has paid : {zz} % \n")
        # Unpaid
        print(" > Unpaid : ")
        mm = 100 / (self.unpaid + 0)
        print(f" > The Percentage of children that has not paid : {mm} % \n")
        quit_or_again = input(
            " > Do you want to quit_or_again or get more results ? \n > "
        )
        if (
            quit_or_again == "quit"
            or quit_or_again == "Quit"
            or quit_or_again == "Q"
            or quit_or_again == "q"
        ):
            quit()
        else:
            Enter_data()


class Price(Prices, Pay):
    def __init__(self, paid, unpaid, price, type_of_money):
        super().__init__(
            self.paid,
            self.unpaid,
            self.price,
            self.type_of_money,
            self.discount_class_owners,
            self.discount,
        )
        self.price = self.price
        self.type_of_money = self.type_of_money
        self.discount_class_owners = self.discount_class_owners
        if self.paid > self.cost:
            self.paid_amount = self.paid * self.cost
        else:
            self.paid_amount = self.cost * self.paid
        if self.unpaid > self.cost:
            self.unpaid_amount = self.unpaid * self.cost
        else:
            self.unpaid_amount = self.cost * self.unpaid

    def how_many_children_paid(self):
        self.paid_amount = self.paid * self.cost
        self.unpaid_amount = self.unpaid * self.cost
        if self.paid_amount > self.cost:
            x = self.paid_amount / self.cost
            print(f" > {x} Children has paid...")
        elif self.paid_amount < self.cost:
            x = self.cost / self.paid_amount
            print(f" > {x} Children has paid...")

    def how_many_children_unpaid(self):
        self.paid_amount = self.paid * self.cost
        self.unpaid_amount = self.unpaid * self.cost
        if self.unpaid_amount > self.cost:
            y = self.unpaid_amount / self.cost
            print(f" > {y} Children has paid...")
        elif self.unpaid_amount < self.cost:
            y = self.cost / self.unpaid_amount
            print(f" > {y} Children has'nt Paid...")

    def total_paid_and_unpaid(self):
        self.paid_amount = self.paid * self.cost
        self.unpaid_amount = self.unpaid * self.cost
        if self.unpaid_amount > self.cost:
            y = self.unpaid_amount / self.cost
            x = self.paid_amount / self.cost
            z = x + y
            print(f" > Total Children = {z} ")
        elif self.unpaid_amount < self.cost:
            y = self.cost / self.unpaid_amount
            x = self.cost / self.paid_amount
            z = x + y
            print(f" > Total Children = {z} ")


class Children_in_out(Price):
    def __init__(self, added, gone, paid, unpaid, price, type_of_money):
        super().__init__(paid, unpaid, price, type_of_money)
        self.added = added
        self.gone = gone

    def percentage(self, added, gone):
        self.added = added
        self.gone = gone
        i = 100 / self.added + 0
        x = 100 / self.gone + 0
        if i > x:
            z = i - x
            print(
                f" > {i} % of children has been joined \n {x} % of children quit \n the amount of Progress or "
                f"Non-Progress "
                f"( - integers = Bad | + integers = Good ) {z} "
            )
            x = {"Percentage": i}
            with open("Data.pickle", "wb") as f:
                pickle.dump(x, f)
            with open("Data.pickle", "rb") as f:
                l = pickle.load(f)
                m = l["Percentage"]
                print(f" > The Before Percentage : {m} \n > This time Percentage {i}..")
                if i < m:
                    print(f" > Bad improvement ! ({m - i}) ")
                elif i > m:
                    print(
                        f" > Great improvement ! \n > Keep up the good work... ({i - m})"
                    )
        elif i < x:
            z = x - i
            print(
                f" > {i} % of children has been joined \n {x} % of children quit \n the amount of Progress or "
                f"Non-Progress "
                f"( - integers = Bad | + integers = Good ) {z} "
            )
            x = {"Percentage": i}
            with open("Data.pickle", "wb") as f:
                pickle.dump(x, f)
            with open("Data.pickle", "rb") as f:
                l = pickle.load(f)
                m = l["Percentage"]
                print(f" > The Before Percentage : {m} \n > This time Percentage {i}..")
                if i < m:
                    print(f" > Bad improvement ! ({m - i}) ")
                elif i > m:
                    print(
                        f" > Great improvement ! \n > Keep up the good work... ({i - m})"
                    )


paid_students = int(input(" > How many Children did Pay ? \n > "))
unpaid_students = int(input(" > How many Children didn't Pay ? \n > "))
cost = int(input(" > How much is the cost ? \n > "))
money_type = input(" > What is the Money type ? (Rs or $ ) \n > ")
discount_OD = int(input(" > What is the owner discount ? \n > "))
discount = int(input(" > What is the discount for the child ? \n > "))
lll = Prices(
    paid=paid_students,
    unpaid=unpaid_students,
    price=cost,
    type_of_money=money_type,
    discount_class_owners=discount_OD,
    discount=discount,
)


def Enter_data():
    print(
        f"""

     > Paid Students : {paid_students}

     > Unpaid Students : {unpaid_students}

     > Cost : {cost}

     > Money type : {money_type}

     > Discount (Owner) : {discount_OD}

     > Children Discount : {discount}

    """
    )

    want_to_change = input(" > Do you want to change any thing ? (Yes or No) \n > ")
    if want_to_change == "No" or want_to_change == "no" or want_to_change == "NO":
        pass
    elif want_to_change == "Yes" or want_to_change == "yes":
        which_one = input(" > What is the one that you want to change ? \n > ")
        if which_one == "Paid students" or which_one == "paid students":
            new_paid_students = int(
                input(" > What is the new paid student value ? \n > ")
            )
            lll.new_paid(paid_new=new_paid_students)
        elif which_one == "Unpaid Students" or which_one == "unpaid students":
            new_unpaid_students = int(
                input(" > What is the new unpaid student value ? \n > ")
            )
            lll.new_unpaid(unpaid_new=new_unpaid_students)
        elif which_one == "Cost" or which_one == "cost":
            new_cost = int(input(" > What is the new cost ? \n > "))
            lll.new_cost(new_cost=new_cost)
        elif which_one == "money type" or which_one == "Money type":
            new_money_type = input(" > What is the new money type ? \n > ")
            lll.new_money_type(new_money_type=new_money_type)
        elif which_one == "Discount" or which_one == "discount":
            new_discount = int(input(" > What is the new discount ? \n > "))
            lll.new_discount(new_discounts=new_discount)
        elif which_one == "Owner_Discount" or which_one == "OD":
            new_OD = int(input(" > What is the new owner discount ? \n > "))
            lll.new_discount_owners(new_discount_owners=new_OD)
        else:
            print(" > Invalid Choice ! ")
    print(" > Functions : ")
    print(
        """
     > T = The total Cost
     
     > P = the Paid Cost
     
     > U = the unpaid cost
     
     > Pe = Percentage of the unpaid and paid
     
     > tc = calculates how many children paid totally
     
     > pc = calculates how many children Pay
     
     > Uc = calculates how many children didn't pay
     
     > GC = Calculates weather how many children went and came 
     
     > q = to quit
     
     > H  = Help
    """
    )

    what_is_the_funtion = input(" > What is your choice ? \n > ")
    if what_is_the_funtion == "T" or what_is_the_funtion == "t":
        print(" \n ")
        lll.Total()
        print(" \n ")
        Enter_data()
    elif what_is_the_funtion == "P" or what_is_the_funtion == "p":
        print(" \n ")
        lll.Paid()
        print(" \n ")
        Enter_data()
    elif what_is_the_funtion == "U" or what_is_the_funtion == "u":
        print(" \n ")
        lll.Unpaid()
        print(" \n ")
        Enter_data()
    elif what_is_the_funtion == "Pe" or what_is_the_funtion == "pe":
        print(" \n ")
        lll.percentages()
        print(" \n ")
        Enter_data()
    elif (
        what_is_the_funtion == "tc"
        or what_is_the_funtion == "TC"
        or what_is_the_funtion == "tC"
    ):
        print(" \n ")
        Price.total_paid_and_unpaid()
        print(" \n ")
        Enter_data()
    elif (
        what_is_the_funtion == "Pc"
        or what_is_the_funtion == "PC"
        or what_is_the_funtion == "Pc"
    ):
        print(" \n ")
        lkf = Price(unpaid=unpaid_students, price=cost, type_of_money=money_type)
        lkf.how_many_children_paid()
        print(" \n ")
        Enter_data()
    elif (
        what_is_the_funtion == "Uc"
        or what_is_the_funtion == "uc"
        or what_is_the_funtion == "UC"
    ):
        print(" \n ")
        lkd = Price(
            paid=paid_students,
            unpaid=unpaid_students,
            price=cost,
            type_of_money=money_type,
        )
        lkd.how_many_children_unpaid()
        print(" \n ")
        Enter_data()
    elif (
        what_is_the_funtion == "Gc"
        or what_is_the_funtion == "GC"
        or what_is_the_funtion == "gc"
    ):
        print(" \n ")
        Come = int(input(" > How many children did  join the classes ? \n > "))
        Gone = int(input(" > How many children did  quit the classes ? \n > "))
        print(" \n ")
        pai = Children_in_out(
            added=Come,
            gone=Gone,
            paid=lll.paid,
            unpaid=lll.unpaid,
            price=lll.cost,
            type_of_money=lll.money_type,
        )
        pai.percentage(added=Come, gone=Gone)
        print(" \n ")
        Enter_data()
    elif what_is_the_funtion == "q" or what_is_the_funtion == "Q":
        print(" > Thank you for using our Program ! ")
        quit()
    elif what_is_the_funtion == "H" or what_is_the_funtion == "h":
        print(
            """
         > This is a Simple Program that lets you calculate the prices (for the teacher or the class owners)
         > This is Made only for the staff of this company(SCI)
         > If you are not a staff person please exit this program ( ! Only for Staff ! )
        
        """
        )
    else:
        print(" > Invalid Choice ! ")
        Enter_data()


Enter_data()
The end of the Program
