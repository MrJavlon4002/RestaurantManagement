from reservation import Reservation
from menu import Menu
menu = Menu()
from restaurant import Restaurant
restaurant = Restaurant()


class Customer(Reservation):

    def show_menu(self):
        menu.show_menu()

    def make_revervation(self):
        return super().make_revervation()

    def show_reservation(self):
        reservation_name = self.check_reservarion_name()
        if reservation_name == '': return
        print(f"\n\n\n\nCustomer name: {reservation_name} \nReservation date: {self.reservations[reservation_name]['date']} \nReservation Time: {self.reservations[reservation_name]['time']} \nCustomer numbers {self.reservations[reservation_name]['cust_num']} \n Dishes: ")
        total_price = 0
        for dish in self.reservations[reservation_name]['dishes']:
            dish_name = list(dish.keys())[0]
            dish_values = list(dish.values())[0]
            print(f"\t{dish_name} -- ${dish_values['price']}")
            total_price = total_price + dish_values['price']
        print(f'\tTotal price: ${total_price}')

    
    def send_request(self):
        request_owner = self.make_reservation_name()
        text = input("What is your request: ")
        request = {
            'owner' : request_owner,
            'text' : text
        }
        restaurant.requests.append(request)
    
    def search_food(self):
        menu.search_food()
    
        
    def check_reservarion_name(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        if (first_name + ' '+ last_name) in self.reservations:
            return (first_name + ' '+ last_name)
        else: 
            print("There is no such Revervation!!!")
            return ""