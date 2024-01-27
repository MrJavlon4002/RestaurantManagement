from restaurant import Restaurant
class Menu(Restaurant):

    # adding new food to the menu
    def add_new_food(self):
        if len(self.dishes) < 11:
            food_name = input('Enter the name of food: ')
            try: food_price = int(input('Enter the price of food ($): '))
            except: 
                print('Price should be number!')
                return
            food_description = input('Enter the description of food: ')
            food_category = input('Enter the category of food: ')
            new_food = {
                'price': food_price,
                'description': food_description,
                'category': food_category
            }
            self.dishes[food_name] = new_food
        else: print('Menu is full')
    
    # updating food in the menu
    def update_food(self):
        search_food_name = input("Enter the name of food you want to change: ")
        if search_food_name in self.dishes:
            try: new_food_price = int(input(f"Enter new price of {search_food_name}: "))
            except: 
                print('Price should be number!')
                return
            new_food_description = input(f"Enter new description of {search_food_name}: ")
            new_food_category = input(f"Enter new category of {search_food_name}: ")
            self.dishes[search_food_name]['price'] = new_food_price
            self.dishes[search_food_name]['description'] = new_food_description
            self.dishes[search_food_name]['category'] = new_food_category
            print('Food informations changed successfully')
        else: print('There is no such food')
    
    # removing food from the menu
    def remove_food(self):
        search_food_name = input("Enter the name of food you want to remove: ")
        if search_food_name in self.dishes:
            del self.dishes[search_food_name]
        else: print('There is no such food')

    # showing the whole menu
    def show_menu(self):
        for dish in self.dishes:
            print(f"{dish} -- ${self.dishes[dish]['price']} \n \t {self.dishes[dish]['category']} \n \t {self.dishes[dish]['description']} ")
    
    #searching food
    def search_food(self):
        search_food_name = input("Enter the name of food: ")
        if search_food_name in self.dishes:
            print(f"{search_food_name} -- ${self.dishes[search_food_name]['price']} \n \t {self.dishes[search_food_name]['category']} \n \t {self.dishes[search_food_name]['description']} ")
            return {search_food_name : self.dishes[search_food_name]}
        else:
            print('There is no such food')
            return ''

