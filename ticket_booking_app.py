class TicketBooking:

    def __init__(self):

        # Movie tickets availability
        self.movies = {
            "movie1": 40,
            "movie2": 10,
            "movie3": 0
        }


        # Food combos with price
        self.food_combos = {
            "combo1": {
                "name": "Popcorn + Coke",
                "price": 200
            },

            "combo2": {
                "name": "Burger + Coke",
                "price": 300
            },

            "combo3": {
                "name": "Pizza Combo",
                "price": 500
            }
        }


        # Store booked tickets
        self.bookings = {}

        self.ticket_price = 150



    # Show movies
    def show_movies(self):

        print("\nAvailable Movies")

        for movie, seats in self.movies.items():
            print(movie, ":", seats, "tickets")



    # Booking function
    def book_ticket(self):

        email = input("\nEnter your email : ")


        self.show_movies()


        movie = input("\nSelect movie : ")


        if movie not in self.movies:
            print("Invalid Movie")
            return


        if self.movies[movie] == 0:
            print("House Full!")
            return



        tickets = int(input("Enter number of tickets : "))


        if tickets > self.movies[movie]:
            print("Only", self.movies[movie], "tickets available")
            return



        total = tickets * self.ticket_price



        # Food section

        food_order = []

        food = input("\nDo you want food? yes/no : ")


        if food.lower() == "yes":


            print("\nFood Combos")

            for key,value in self.food_combos.items():

                print(
                    key,
                    "-",
                    value["name"],
                    "- ₹",
                    value["price"]
                )


            combo = input("\nSelect combo : ")


            if combo in self.food_combos:


                quantity = int(
                    input("Enter number of items : ")
                )


                food_amount = (
                    self.food_combos[combo]["price"]
                    *
                    quantity
                )


                total += food_amount



                food_order.append(
                    {
                        "combo":
                        self.food_combos[combo]["name"],

                        "quantity":
                        quantity
                    }
                )



        # reduce tickets

        self.movies[movie] -= tickets



        # store booking

        self.bookings[email] = {

            "movie": movie,

            "tickets": tickets,

            "food": food_order,

            "amount": total

        }



        print("\n------ Booking Successful ------")

        print("Email :",email)

        print("Movie :",movie)

        print("Tickets :",tickets)

        print("Food :",food_order)

        print("Total Amount : ₹",total)





    # Cancel ticket

    def cancel_ticket(self):

        email = input("\nEnter email : ")



        if email not in self.bookings:

            print("No booking found")

            return



        booking = self.bookings[email]


        movie = booking["movie"]

        tickets = booking["tickets"]



        # add tickets back

        self.movies[movie] += tickets



        del self.bookings[email]



        print("\nTicket Cancelled Successfully")

        print(tickets,"tickets added back to",movie)






# Object creation

app = TicketBooking()



while True:


    print("\n========= Movie Ticket App =========")

    print("1. Book Ticket")

    print("2. Cancel Ticket")

    print("3. Show Availability")

    print("4. Exit")



    choice = input("\nEnter choice : ")



    if choice == "1":

        app.book_ticket()


    elif choice == "2":

        app.cancel_ticket()


    elif choice == "3":

        app.show_movies()


    elif choice == "4":

        print("Thank you!")

        break


    else:

        print("Invalid Choice")