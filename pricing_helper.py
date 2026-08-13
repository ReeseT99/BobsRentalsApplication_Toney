#----------------------------------------------------------------------------
# These helper functions were added because the assigned class library only
# compares the daily total to the weekly rate when 7 or more days are rented.
# The weekly rate is actually cheaper before 7 days are reached, so the
# original method charges too much on some rentals. These functions figure
# the correct best price. The discount work is still done by Rental
# class from my assigned library.
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
# best_price_for_item
#----------------------------------------------------------------------------
def best_price_for_item(equipment, rental_period, quantity):
    """Returns the lowest price for one piece of equipment."""

    rental_period = rental_period.lower()

    if rental_period == "hourly":
        best_price = equipment.hourly_rate * quantity
        if equipment.daily_rate < best_price:
            best_price = equipment.daily_rate
        if equipment.weekly_rate < best_price:
            best_price = equipment.weekly_rate
        return best_price

    elif rental_period == "daily":
        daily_total = equipment.daily_rate * quantity

        # count how many full weeks are in the number of days
        week_count = 0
        days_left = quantity
        while days_left >= 7:
            week_count = week_count + 1
            days_left = days_left - 7

        # charge the leftover days at whichever price is lower
        leftover_total = days_left * equipment.daily_rate
        if days_left > 0 and equipment.weekly_rate < leftover_total:
            leftover_total = equipment.weekly_rate

        week_total = week_count * equipment.weekly_rate
        mixed_total = week_total + leftover_total

        best_price = daily_total
        if mixed_total < best_price:
            best_price = mixed_total
        return best_price

    elif rental_period == "weekly":
        return equipment.weekly_rate * quantity

    else:
        raise ValueError("Rental period must be hourly, daily, or weekly. Value given: " + str(rental_period))


#----------------------------------------------------------------------------
# best_price_subtotal
#----------------------------------------------------------------------------
def best_price_subtotal(rental, quantity):
    """Returns the price of every item in a rental before discounts."""

    subtotal = 0.0
    for equipment in rental.equipment_list:
        subtotal = subtotal + best_price_for_item(equipment, rental.rental_period, quantity)
    return subtotal


#----------------------------------------------------------------------------
# format_money
#----------------------------------------------------------------------------
def format_money(amount):
    """Returns a dollar amount as text with two decimal places."""

    amount = round(amount, 2)
    dollars = int(amount)
    cents = int(round((amount - dollars) * 100))

    cents_text = str(cents)
    if cents < 10:
        cents_text = "0" + cents_text

    return "$" + str(dollars) + "." + cents_text