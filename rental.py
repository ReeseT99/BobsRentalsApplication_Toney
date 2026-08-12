FAMILY_DISCOUNT_MIN_ITEMS = 3
FAMILY_DISCOUNT_MAX_ITEMS = 5
FAMILY_DISCOUNT_RATE = 0.25
COUPON_SUFFIX = "BBP"
COUPON_DISCOUNT_RATE = 0.10


class Rental(object):
    """
    Represents one customer's rental transaction. A rental can
    include any combination of skis and snowboards, but all
    equipment in the rental must share the same rental period.
    """

    def __init__(self, customer, rental_period, coupon_code=None):
        self._customer = customer
        self._rental_period = rental_period.lower()
        self._coupon_code = coupon_code
        self._equipment_list = []

    # ---------- Properties ----------

    @property
    def customer(self):
        return self._customer

    @property
    def rental_period(self):
        return self._rental_period

    @property
    def coupon_code(self):
        return self._coupon_code

    @coupon_code.setter
    def coupon_code(self, value):
        self._coupon_code = value

    @property
    def equipment_list(self):
        return list(self._equipment_list)  # return a copy to protect the original

    @property
    def item_count(self):
        return len(self._equipment_list)

    # ---------- Methods ----------

    def add_equipment(self, equipment):
        """Adds a piece of RentalEquipment to this rental."""
        self._equipment_list.append(equipment)

    def calculate_subtotal(self, quantity):
        """
        Calculates the pre-discount total for all equipment in the
        rental, using the best available price for each item.
        `quantity` is the number of hours, days, or weeks rented.
        """
        subtotal = 0.0
        for equipment in self._equipment_list:
            subtotal += equipment.calculate_best_price(self._rental_period, quantity)
        return subtotal

    def qualifies_for_family_discount(self):
        return FAMILY_DISCOUNT_MIN_ITEMS <= self.item_count <= FAMILY_DISCOUNT_MAX_ITEMS

    def qualifies_for_coupon_discount(self):
        return bool(self._coupon_code) and self._coupon_code.upper().endswith(COUPON_SUFFIX)

    def apply_discounts(self, subtotal):
        """
        Applies the family discount first (if it qualifies), then
        the coupon discount (if it qualifies), and returns the
        final discounted total.
        """
        total = subtotal

        if self.qualifies_for_family_discount():
            total -= total * FAMILY_DISCOUNT_RATE

        if self.qualifies_for_coupon_discount():
            total -= total * COUPON_DISCOUNT_RATE

        return round(total, 2)

    def calculate_estimate(self, quantity):
        """Returns the estimated total cost before equipment is rented."""
        subtotal = self.calculate_subtotal(quantity)
        return self.apply_discounts(subtotal)

    def calculate_final_bill(self, actual_quantity):
        """
        Returns the final total cost when equipment is returned,
        based on the actual rental duration.
        """
        subtotal = self.calculate_subtotal(actual_quantity)
        return self.apply_discounts(subtotal)

    def __str__(self):
        return (f"Rental for {self._customer.name} - "
                f"{self.item_count} item(s), {self._rental_period} period")
