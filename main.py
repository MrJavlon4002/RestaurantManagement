from restaurant import Restaurant
restaurant = Restaurant()
from staff import Staff
staff = Staff()
from customer import Customer
customer = Customer()

while True:
    # choosing the role
    role = input(f"\n\n\nAre you staff of Customer (1 - Customer; 2 - Staff; 0 - Exit): ")
    # Actions for user role 
    if role == '1':
        while True:
            action_num = input(f"\n\n\n Choose one of the actions: \n\t1. View the menu \n\t2. Make a reservation \n\t3. View reservation \n\t4. Send request \n\t5. View the information of Restaurant\n\t6. Search food\n\t0. Exit \n-> ")
            if action_num == '1':
                customer.show_menu()
            elif action_num == '2':
                customer.make_revervation()
            elif action_num == '3':
                customer.show_reservation()
            elif action_num == '4':
                customer.send_request()
            elif action_num == '5':
                print(restaurant.restaurant_info)
            elif action_num == '6':
                customer.search_food()
            elif action_num == '0':
                break
    elif role == '2':
    # Actions for user role 
        # Autorication for staff members
        name_surename = customer.make_reservation_name()
        if name_surename not in restaurant.staff_members:
            print("there is no such worker!!!")
        else:
            while True:
                action_num = int(input(f'\n\n\nChoose one of the actions: \n\t1. View the menu \n\t2. Add food \n\t3. Update food \n\t4. Remove food \n\t5. Update reservation \n\t6. Delete reservation \n\t7. Show reservation \n\t8. Show all reservations \n\t9. View the information of Restaurant \n\t10. Show requests \n\t0. Exit \n-> '))
                if action_num == '1':
                    staff.show_menu()
                elif action_num == '2':
                    staff.add_new_food()
                elif action_num == '3':
                    staff.update_food()
                elif action_num == '4':
                    staff.remove_food()
                elif action_num == '5':
                    staff.update_reservation()
                elif action_num == '6':
                    staff.remove_reservation()
                elif action_num == '7':
                    staff.show_reservation()
                elif action_num == '8':
                    staff.show_all_reservation()
                elif action_num == '9':
                    print(restaurant.restaurant_info)
                elif action_num == '10':
                    staff.show_requests()   
                elif action_num == '0':
                    break
    else: break  