#ticket booking scenariocreate two class customer and ticket booking,in customer class get name and id ,
#generate id using random ,later it should verify i is valid or not condition: 4 character TICK it should start with TICK rest automatically generate.
import random

class Customer:
    def __init__(self, cus_id, name, phone):
        self.cus_id = cus_id
        self.name = name
        self.phone = phone

    @staticmethod
    def gen_rand_id():
        c_id = random.randint(1000, 9999)
        return f"TICK{c_id}"

    @staticmethod
    def verify_customer_id(cus_id):
        if len(cus_id) != 8:
            print("Customer ID should be 8 characters long.")
            return False
        elif not (cus_id.startswith("TICK") and cus_id[4:].isdigit()):
            print("Customer ID is invalid. It should start with 'TICK' followed by 4 digits.")
            return False
        else:
            print("Customer ID verified!")
            return True


class TicketBooking:
    def __init__(self):
        self.events = {
            "Concert": {"price": 1000, "seats": 100},
            "Movie": {"price": 250, "seats": 200},
            "Drama": {"price": 150, "seats": 100},
        }
        self.booked_tickets = []

    def view_events(self):
        print("Available Events:")
        for event, details in self.events.items():
            print(f"{event}: Price - {details['price']}, Seats Available - {details['seats']}")

    def book_tickets(self, event_name, quantity, customer):
        if event_name in self.events:
            event = self.events[event_name]
            if event["seats"] >= quantity:
                total_price = event["price"] * quantity
                event["seats"] -= quantity
                self.booked_tickets.append({
                    "customer_id": customer.cus_id,
                    "event": event_name,
                    "quantity": quantity,
                    "total_price": total_price,
                })
                print(f"Tickets booked successfully! Total Price: {total_price}")
            else:
                print("Not enough seats available!")
        else:
            print("Event not found!")

    def view_tickets(self, customer):
        print("************* Ticket Information *************")
        cus_tickets = [t for t in self.booked_tickets if t["customer_id"] == customer.cus_id]
        if not cus_tickets:
            print("No tickets booked.")
        else:
            for ticket in cus_tickets:
                print(f"Event: {ticket['event']}, Quantity: {ticket['quantity']}, Total Price: {ticket['total_price']}")


if __name__ == "__main__":
    print("************* Welcome to TICKET Booking Application *************")
    
    cus_id = input("Enter your Customer ID: ")
    customer = None

    if Customer.verify_customer_id(cus_id):
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        customer = Customer(cus_id, name, phone)
        print("Welcome back! You can view your booking details.")
    else:
        print("Invalid ID! Please register.")
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        cus_id = Customer.gen_rand_id()
        customer = Customer(cus_id, name, phone)
        print(f"Your new Customer ID is: {cus_id}")

    booking_system = TicketBooking()

    while True:
        print("\n**** Booking Menu ****")
        print("1. View Events")
        print("2. Book Tickets")
        print("3. View My Tickets")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            booking_system.view_events()
        elif choice == 2:
            event_name = input("Enter the event name: ")
            quantity = int(input("Enter the number of tickets: "))
            booking_system.book_tickets(event_name, quantity, customer)
        elif choice == 3:
            booking_system.view_tickets(customer)
        elif choice == 4:
            print("Thank you for using the Ticket Booking System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


