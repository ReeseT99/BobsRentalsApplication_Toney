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
# show_inventory
#----------------------------------------------------------------------------
def show_inventory(shop):
    """Displays the equipment the shop has available right now."""

    print()
    print("---------------- Current Inventory ----------------")
    print("Skis available:", shop.ski_available, "of", shop.ski_total)
    print("Snowboards available:", shop.snowboard_available, "of", shop.snowboard_total)

#----------------------------------------------------------------------------
# get_yes_no
#----------------------------------------------------------------------------
def get_yes_no(prompt):
    """Asks a yes or no question until a valid answer is entered."""

    while True:
        answer = input(prompt)
        answer = answer.strip().lower()

        if answer == "y" or answer == "yes":
            return True
        elif answer == "n" or answer == "no":
            return False
        else:
            print("Please enter yes or no.")


#----------------------------------------------------------------------------
# get_name
#----------------------------------------------------------------------------
def get_name(prompt):
    """Asks for a name until something is actually entered."""

    while True:
        name = input(prompt)
        name = name.strip()

        if name == "":
            print("Name cannot be blank.")
        else:
            return name


#----------------------------------------------------------------------------
# get_rental_period
#----------------------------------------------------------------------------
def get_rental_period():
    """Asks for the rental period until a valid one is entered."""

    print()
    print("Rental periods: hourly, daily, weekly")

    while True:
        period = input("Enter the rental period: ")
        period = period.strip().lower()

        if period == "hourly" or period == "daily" or period == "weekly":
            return period
        else:
            print("Please enter hourly, daily, or weekly.")


#----------------------------------------------------------------------------
# get_length_word
#----------------------------------------------------------------------------
def get_length_word(rental_period):
    """Returns the word used for the length of a rental period."""

    if rental_period == "hourly":
        return "hours"
    elif rental_period == "daily":
        return "days"
    else:
        return "weeks"


#----------------------------------------------------------------------------
# display_price_details
#----------------------------------------------------------------------------
def display_price_details(active_rental, length, title):
    """Displays the price breakdown and returns the final amount."""

    rental = active_rental.rental
    subtotal = best_price_subtotal(rental, length)

    family_amount = 0.0
    if rental.qualifies_for_family_discount() == True:
        family_amount = subtotal * FAMILY_DISCOUNT_RATE

    after_family = subtotal - family_amount

    coupon_amount = 0.0
    if rental.qualifies_for_coupon_discount() == True:
        coupon_amount = after_family * COUPON_DISCOUNT_RATE

    final_amount = rental.apply_discounts(subtotal)
    length_word = get_length_word(rental.rental_period)

    print()
    print("--------------------", title, "--------------------")
    print("Customer number:", active_rental.customer_number)
    print("Customer name:", rental.customer.name)

    if active_rental.ski_count > 0:
        print("Skis:", active_rental.ski_count)
    if active_rental.snowboard_count > 0:
        print("Snowboards:", active_rental.snowboard_count)

    print("Rental period:", rental.rental_period)
    print("Rental length:", length, length_word)
    print("Price before discounts:", format_money(subtotal))

    if family_amount > 0:
        print("Family discount (25%): -", format_money(family_amount))
    if coupon_amount > 0:
        print("Coupon discount (10%): -", format_money(coupon_amount))

    print("Total:", format_money(final_amount))
    print("-------------------------------------------------------")

    return final_amount


#----------------------------------------------------------------------------
# process_new_rental
#----------------------------------------------------------------------------
def process_new_rental(shop, active_rentals, customer_number):
    """Walks through a new rental. Returns True if the rental was completed."""

    print()
    print("---------------- New Customer Rental ----------------")
    print("Skis available:", shop.ski_available)
    print("Snowboards available:", shop.snowboard_available)
    print()

    ski_count = get_whole_number("How many skis? ", 0)
    snowboard_count = get_whole_number("How many snowboards? ", 0)

    if ski_count == 0 and snowboard_count == 0:
        print()
        print("No equipment was requested. Returning to the main menu.")
        return False

    # check both types before any inventory is reduced
    if shop.is_available("ski", ski_count) == False:
        print()
        print("Sorry, only", shop.ski_available, "skis are available.")
        return False

    if shop.is_available("snowboard", snowboard_count) == False:
        print()
        print("Sorry, only", shop.snowboard_available, "snowboards are available.")
        return False

    rental_period = get_rental_period()
    length_word = get_length_word(rental_period)
    length = get_whole_number("How many " + length_word + "? ", 1)

    coupon_code = input("Enter a coupon code or press Enter to skip: ")
    coupon_code = coupon_code.strip()
    if coupon_code == "":
        coupon_code = None

    # the customer name is collected later, so a placeholder is used for now
    customer = Customer(customer_number, "Pending")
    rental = Rental(customer, rental_period, coupon_code)

    item_number = 1
    while item_number <= ski_count:
        rental.add_equipment(Ski("SKI-" + str(item_number)))
        item_number = item_number + 1

    item_number = 1
    while item_number <= snowboard_count:
        rental.add_equipment(Snowboard("SNB-" + str(item_number)))
        item_number = item_number + 1

    active_rental = ActiveRental(customer_number, rental, ski_count, snowboard_count, length)
    display_price_details(active_rental, length, "Rental Estimate")

    print()
    if get_yes_no("Complete this rental? (yes/no): ") == False:
        print()
        print("The rental was cancelled. Returning to the main menu.")
        return False

    print()
    customer.name = get_name("Enter the customer name: ")

    if ski_count > 0:
        shop.rent_equipment("ski", ski_count)
    if snowboard_count > 0:
        shop.rent_equipment("snowboard", snowboard_count)

    # revenue is added later, when the equipment is returned and paid for
    shop.record_rental(ski_count, snowboard_count, 0.00)
    active_rentals.append(active_rental)

    print()
    print("The rental was completed.")
    print("Customer number:", customer_number)
    print("Please give this number to the customer for the return.")
    return True

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
        rental_completed = process_new_rental(shop, active_rentals, next_customer_number)
        if rental_completed == True:
            next_customer_number = next_customer_number + 1

    elif menu_choice == 2:
        print("Coming soon")

    elif menu_choice == 3:
        show_inventory(shop)

    elif menu_choice == 4:
        shop_is_open = False