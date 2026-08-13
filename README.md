Final Part 2 Readme
Name: Maurice Toney
Course: CPDM 120 Object-Oriented Programming 
-----------------------------------------------------------------
-----------------------------------------------------------------
Description
-----------------------------------------------------------------
A console application for Bob's Ski & Snowboard Rentals. It uses
the class library written by William Schoenling for Part 1. The
program asks for the starting inventory, then shows a menu that
stays open until the user picks End of Day.

-----------------------------------------------------------------
Running the program
-----------------------------------------------------------------
Run rental_application.py. All of the files need to be in the same
folder.

-----------------------------------------------------------------
Files
-----------------------------------------------------------------
Assigned class files, not changed:
customer.py, rental.py, rental_equipment.py, rental_shop.py,
test_classes.py

My files:
rental_application.py - the application
pricing_helper.py - pricing functions
active_rental.py - class for tracking rentals

-----------------------------------------------------------------
How I used the assigned classes
-----------------------------------------------------------------
RentalShop holds the inventory and daily totals. The application
calls set_starting_inventory, is_available, rent_equipment,
return_equipment, and record_rental.

A Customer and a Rental are made for each rental. Ski and Snowboard
objects are added one at a time with add_equipment so the item count
is right for the family discount.

The Rental class handles the discounts. The application calls
qualifies_for_family_discount, qualifies_for_coupon_discount, and
apply_discounts.

-----------------------------------------------------------------
Problems and limitations
-----------------------------------------------------------------
1. Daily pricing
calculate_best_price only checks the weekly rate at 7 or more days.
A ski week is $200 and 4 days is already $200, so 5 or 6 days gets
overcharged. It also charges one week for any rental over 7 days,
so 14 days costs the same as 7. I left the class file alone and put
the corrected math in pricing_helper.py. The subtotal still goes to
the Rental class for the discounts.

2. No rental storage
The library does not save rentals or track returns, so I added the
ActiveRental class and a list in the application. Each customer gets
a number to bring back at the return.

3. Recording revenue
record_rental adds the counts and the money together, but revenue
should only count after a return. The application calls it twice,
once with the counts and $0 at rental time, once with the money and
0 counts at return time.

4. Rental length
A Rental does not store its length. The application saves the
estimate in ActiveRental and asks for the actual length at the
return so the final bill uses the real time.

5. Money formatting
The library uses f-strings. I wrote format_money in pricing_helper.py
since I am not using f-strings.

-----------------------------------------------------------------
Reflection
-----------------------------------------------------------------
I had to read all of the class files and run the test file before I
could plan anything, since I could not assume they worked like mine.
His design was clear, but some things I  were missing, like
a way to store rentals.

The hardest part was finding the pricing problem. Everything looked
fine until I checked the math on a 5 day rental, so I learned not to
trust code just because it runs.

Leaving the original files alone also made more sense than fixing
them. Putting my changes in a separate file keeps it clear which
code is his and which is mine.
