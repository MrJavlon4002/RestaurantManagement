from customer import Customer
from menu import Menu
from restaurant import Restaurant
class Staff(Customer, Menu,Restaurant):

    def remove_reservation(self):
        reservation_name =  self.check_reservarion_name()
        del self.reservations[reservation_name]
        
    
    def update_reservation(self):
        reservation_name =  self.check_reservarion_name()
        if reservation_name == '': return
        self.reservations[reservation_name] = self.make_reservation_details()
    
    def show_reservation(self):
        reservation_name = self.check_reservarion_name()
        if reservation_name == '': 
            return
        print(f"\n\n\n\nCustomer name: {reservation_name} \nReservation date: {self.reservations[reservation_name]['date']} \nReservation Time: {self.reservations[reservation_name]['time']} \nCustomer numbers {self.reservations[reservation_name]['cust_num']} \n Dishes: ")
        total_price = 0
        for dish in self.reservations[reservation_name]['dishes']:
            dish_name = list(dish.keys())[0]
            dish_values = list(dish.values())[0]
            print(f"\t{dish_name} -- ${dish_values['price']}")
            total_price = total_price + dish_values['price']
        print(f'\tTotal price: ${total_price}')
    
    def show_all_reservation(self):
        for reservation in self.reservations:
            print(reservation)
            print(f"\n\n\n\nCustomer name: {reservation} \nReservation date: {self.reservations[reservation]['date']} \nReservation Time: {self.reservations[reservation]['time']} \nCustomer numbers {self.reservations[reservation]['cust_num']} \n Dishes: ")
            total_price = 0
            for dish in self.reservations[reservation]['dishes']:
                dish_name = list(dish.keys())[0]
                dish_values = list(dish.values())[0]
                print(f"\t{dish_name} -- ${dish_values['price']}")
                total_price = total_price + dish_values['price']
            print(f'\tTotal price: ${total_price}')

    
    def check_reservarion_name(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        if (first_name + ' '+ last_name) in self.reservations:
            return (first_name + ' '+ last_name)
        else: 
            print("There is no such Revervation!!!")
            return ''
    
    def show_requests(self):
        for request in self.requests:
            print(f"{request['owner']}: \t{request['text']}")
    
