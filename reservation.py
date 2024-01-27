from menu import Menu
menu = Menu()

from restaurant import Restaurant
class Reservation(Restaurant):

    # making name for reservation
    def make_reservation_name(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        return first_name + ' '+ last_name

    # taking all reservations details
    def make_reservation_details(self):
        reservation_date = input('Enter date for your reservation (01.01.2023): ')
        reservation_time = input('Enter time for your reservation (12:00): ')

        # Checking reservation date
        if reservation_date in self.dates:
            if len(self.dates[reservation_date])<=20 and reservation_time not in self.dates[reservation_date]:
                self.dates[reservation_date].append(reservation_time)
            else: 
                print("There is no more reservation available for this time!!!")
                return
        else: self.dates[reservation_date] = [reservation_time]

        customer_number = int(input('Please enter number of visitors to our restaurant: '))
        ordered_dishes = []

        # taking dishes for reservation
        while True:
            founded_food = menu.search_food()
            if founded_food == '':
                continue
            ordered_dishes.append(founded_food)
            choise = input("Do you want to order more food (1 - yes, 0 - no): ")
            if choise == '0' or len(ordered_dishes) == 10: break
            elif choise != '0' and choise != '1': 
                print('Choose on of them!!!')
                continue
        
        return {
            'date' : reservation_date,
            'time' : reservation_time,
            'cust_num' : customer_number,
            'dishes' : ordered_dishes
        }

    # main reservation manking function
    def make_revervation(self):
        # taking name for reservation
        reservation_name = self.make_reservation_name()
        # taking reservation details
        reservation_details = self.make_reservation_details()
        # saving the reservation
        self.reservations[reservation_name] = reservation_details
