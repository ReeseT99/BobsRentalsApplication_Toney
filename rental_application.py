# Maurice Toney
 
from rental_equipment import Ski, Snowboard
from customer import Customer
from rental import Rental
from rental import FAMILY_DISCOUNT_RATE
from rental import COUPON_DISCOUNT_RATE
from rental_shop import RentalShop
from active_rental import ActiveRental
from pricing_helper import best_price_subtotal
from pricing_helper import format_money


#----------------------------------------------------------------------------
# get_whole_number
#----------------------------------------------------------------------------
def get_whole_number(prompt, smallest_allowed):
    """Asks for a whole number until a valid one is entered."""

    while True:
        entry = input(prompt)
        entry = entry.strip()

        if entry.isdigit() == False:
            print("Please enter a whole number.")
        else:
            number = int(entry)
            if number < smallest_allowed:
                print("Please enter", smallest_allowed, "or greater.")
            else:
                return number

#----------------------------------------------------------------------------
# get_menu_choice
#----------------------------------------------------------------------------
def get_menu_choice():
    """Displays the main menu and returns a valid choice."""

    print()
    print("Main Menu ")
    print("1. New Customer Rental")
    print("2. Rental Return")
    print("3. Show Inventory")
    print("4. End of Day")
    print()

    while True:
        choice = input("Enter your choice (1-4): ")
        choice = choice.strip()

        if choice == "1" or choice == "2" or choice == "3" or choice == "4":
            return int(choice)
        else:
            print("Please enter 1, 2, 3, or 4.")

#----------------------------------------------------------------------------
# Main
#----------------------------------------------------------------------------
print("----------------------------------")
print("   Bob's Ski & Snowboard Rentals")
print("----------------------------------")
print()
print("Enter the starting inventory for the day.")

shop = RentalShop()
starting_skis = get_whole_number("Number of skis: ", 0)
starting_snowboards = get_whole_number("Number of snowboards: ", 0)
shop.set_starting_inventory(starting_skis, starting_snowboards)

print()
print("The shop is open.")
print("Skis:", shop.ski_available, " Snowboards:", shop.snowboard_available)

active_rentals = []
next_customer_number = 1
shop_is_open = True

while shop_is_open == True:
    menu_choice = get_menu_choice()

    if menu_choice == 1:
        print("Coming soon")

    elif menu_choice == 2:
        print("Coming soon")

    elif menu_choice == 3:
        print("Coming soon")

    elif menu_choice == 4:
        shop_is_open = False