class Store:
    inventory = {"shirts": [10, 499], "phones": [5, 50000], "shoes": [15, 999]}

    def __init__(self, cust_name, cust_phone, cust_id, cust_addr, cust_cart):
        self.cust_name = cust_name
        self.cust_phone = cust_phone
        self.cust_id = cust_id
        self.cust_addr = cust_addr
        self.cust_cart = cust_cart

    def show_menu(self):
        print("1 - See what's for sale")
        print("2 - Check your details")
        print("3 - Put something in your cart")
        print("4 - Take something out of your cart")
        print("5 - Done shopping")

    def display_items(self):
        print("What we got:")
        for product, details in self.inventory.items():
            if details[0] > 0:
                print(product, ": We have", details[0], "left. Price:", details[1])

    def show_cust_info(self):
        print("Your info:")
        print("Name:", self.cust_name)
        print("Phone:", self.cust_phone)
        print("ID:", self.cust_id)
        print("Address:", self.cust_addr)
        print("Cart:", self.cust_cart)

    def add_to_basket(self):
        item = input("What do you want to add? ")
        if item in self.inventory:
            if self.inventory[item][0] > 0:
                qty = int(input("How many? "))
                if qty <= self.inventory[item][0]:
                    if item in self.cust_cart:
                        self.cust_cart[item][0] += qty
                    else:
                        self.cust_cart[item] = [qty, self.inventory[item][1]]
                    self.inventory[item][0] -= qty
                    print(qty, item, "(s) added!")
                else:
                    print("Sorry, not enough available.")
            else:
                print("Out of stock!")
        else:
            print("Nope, don't have that.")

    def remove_from_basket(self):
        item = input("What do you want to remove? ")
        if item in self.cust_cart:
            qty = int(input("How many? "))
            if qty >= 1 and qty <= self.cust_cart[item][0]:
                self.cust_cart[item][0] -= qty
                self.inventory[item][0] += qty
                if self.cust_cart[item][0] == 0:
                    del self.cust_cart[item]
                print(item, "quantity decreased.")
            else:
                print("Wrong number. Try again.")
        else:
            print("Not in your cart!")

    def main_loop(self):
        while True:
            self.show_menu()
            choice = int(input("Pick a number: "))
            if choice == 1:
                self.display_items()
            elif choice == 2:
                self.show_cust_info()
            elif choice == 3:
                self.add_to_basket()
            elif choice == 4:
                self.remove_from_basket()
            elif choice == 5:
                break
            else:
                print("Wrong choice. Try again.")

customer = Store("Thirumalaikumar", 8344505009, 101, "Tenkasi", {})
customer.main_loop()
