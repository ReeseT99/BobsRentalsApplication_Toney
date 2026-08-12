from rental_equipment import Ski, Snowboard
from customer import Customer
from rental import Rental
from rental_shop import RentalShop


def test_equipment_creation_and_polymorphism():
    print("--- Testing equipment creation and polymorphism ---")
    ski = Ski("SKI-001")
    board = Snowboard("SNB-001")

    # Polymorphism: same method name, different behavior/return value
    print(ski)
    print(board)
    print(f"Ski type: {ski.get_equipment_type()}")
    print(f"Snowboard type: {board.get_equipment_type()}")
    print()


def test_best_price_calculation():
    print("--- Testing best price calculation ---")
    ski = Ski("SKI-002")

    # 4 hours would normally be $60, but daily rate ($50) is cheaper
    price = ski.calculate_best_price("hourly", 4)
    print(f"Ski rented for 4 hours -> best price: ${price:.2f} (expected $50.00)")

    board = Snowboard("SNB-002")
    price = board.calculate_best_price("hourly", 2)
    print(f"Snowboard rented for 2 hours -> best price: ${price:.2f} (expected $20.00)")
    print()


def test_inventory_tracking():
    print("--- Testing inventory tracking ---")
    shop = RentalShop()
    shop.set_starting_inventory(ski_count=10, snowboard_count=8)
    print(shop)

    shop.rent_equipment("ski", 3)
    print(f"After renting 3 skis, skis available: {shop.ski_available} (expected 7)")

    shop.return_equipment("ski", 1)
    print(f"After returning 1 ski, skis available: {shop.ski_available} (expected 8)")

    try:
        shop.rent_equipment("snowboard", 20)
        print("ERROR: should have raised an exception for insufficient inventory")
    except ValueError as e:
        print(f"Correctly caught error: {e}")
    print()


def test_discounts_and_billing():
    print("--- Testing discounts and billing ---")
    customer = Customer(1, "Jamie Smith")

    # Family rental of 4 items -> should qualify for family discount
    rental = Rental(customer, rental_period="daily", coupon_code="SAVE10BBP")
    rental.add_equipment(Ski("SKI-010"))
    rental.add_equipment(Ski("SKI-011"))
    rental.add_equipment(Snowboard("SNB-010"))
    rental.add_equipment(Snowboard("SNB-011"))

    subtotal = rental.calculate_subtotal(quantity=1)
    print(f"Subtotal for 1 day (4 items): ${subtotal:.2f} (expected $180.00)")
    print(f"Qualifies for family discount: {rental.qualifies_for_family_discount()} (expected True)")
    print(f"Qualifies for coupon discount: {rental.qualifies_for_coupon_discount()} (expected True)")

    estimate = rental.calculate_estimate(quantity=1)
    # 180 -> 25% off = 135 -> 10% off = 121.50
    print(f"Estimate with both discounts applied: ${estimate:.2f} (expected $121.50)")

    final_bill = rental.calculate_final_bill(actual_quantity=1)
    print(f"Final bill: ${final_bill:.2f} (expected $121.50)")
    print()


def test_shop_daily_totals():
    print("--- Testing shop daily totals ---")
    shop = RentalShop()
    shop.set_starting_inventory(ski_count=10, snowboard_count=10)

    shop.record_rental(ski_count=2, snowboard_count=1, amount_charged=121.50)
    shop.record_rental(ski_count=1, snowboard_count=0, amount_charged=50.00)

    print(f"Skis rented today: {shop.skis_rented_today} (expected 3)")
    print(f"Snowboards rented today: {shop.snowboards_rented_today} (expected 1)")
    print(f"Daily revenue: ${shop.daily_revenue:.2f} (expected $171.50)")
    print()


def main():
    test_equipment_creation_and_polymorphism()
    test_best_price_calculation()
    test_inventory_tracking()
    test_discounts_and_billing()
    test_shop_daily_totals()
    print("All tests completed.")


if __name__ == "__main__":
    main()
