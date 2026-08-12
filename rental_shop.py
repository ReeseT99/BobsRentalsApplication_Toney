class RentalShop(object):
    """
    Represents the rental shop itself. Tracks how much inventory
    is available, and keeps running totals for the day.
    """

    def __init__(self):
        self._ski_total = 0
        self._ski_available = 0
        self._snowboard_total = 0
        self._snowboard_available = 0

        self._skis_rented_today = 0
        self._snowboards_rented_today = 0
        self._daily_revenue = 0.0

    # ---------- Properties ----------

    @property
    def ski_total(self):
        return self._ski_total

    @property
    def ski_available(self):
        return self._ski_available

    @property
    def snowboard_total(self):
        return self._snowboard_total

    @property
    def snowboard_available(self):
        return self._snowboard_available

    @property
    def skis_rented_today(self):
        return self._skis_rented_today

    @property
    def snowboards_rented_today(self):
        return self._snowboards_rented_today

    @property
    def daily_revenue(self):
        return self._daily_revenue

    # ---------- Inventory setup ----------

    def set_starting_inventory(self, ski_count, snowboard_count):
        """Sets the shop's starting inventory. Called once at startup."""
        self._ski_total = ski_count
        self._ski_available = ski_count
        self._snowboard_total = snowboard_count
        self._snowboard_available = snowboard_count

    # ---------- Availability checks ----------

    def is_available(self, equipment_type, quantity):
        """Returns True if the requested quantity is currently available."""
        equipment_type = equipment_type.lower()
        if equipment_type == "ski":
            return quantity <= self._ski_available
        elif equipment_type == "snowboard":
            return quantity <= self._snowboard_available
        else:
            raise ValueError("equipment_type must be 'ski' or 'snowboard'")

    # ---------- Renting and returning ----------

    def rent_equipment(self, equipment_type, quantity):
        """
        Reduces available inventory when equipment is rented.
        Raises an error if there is not enough inventory available.
        """
        equipment_type = equipment_type.lower()

        if not self.is_available(equipment_type, quantity):
            raise ValueError(f"Not enough {equipment_type}s available to rent {quantity}")

        if equipment_type == "ski":
            self._ski_available -= quantity
        elif equipment_type == "snowboard":
            self._snowboard_available -= quantity
        else:
            raise ValueError("equipment_type must be 'ski' or 'snowboard'")

    def return_equipment(self, equipment_type, quantity):
        """Restores available inventory when equipment is returned."""
        equipment_type = equipment_type.lower()

        if equipment_type == "ski":
            self._ski_available = min(self._ski_available + quantity, self._ski_total)
        elif equipment_type == "snowboard":
            self._snowboard_available = min(self._snowboard_available + quantity, self._snowboard_total)
        else:
            raise ValueError("equipment_type must be 'ski' or 'snowboard'")

    # ---------- Daily totals ----------

    def record_rental(self, ski_count, snowboard_count, amount_charged):
        """
        Updates the shop's daily totals after a rental is completed.
        Called once a rental's final bill has been calculated.
        """
        self._skis_rented_today += ski_count
        self._snowboards_rented_today += snowboard_count
        self._daily_revenue += amount_charged

    def __str__(self):
        return (f"Skis: {self.ski_available}/{self.ski_total} available | "
                f"Snowboards: {self.snowboard_available}/{self.snowboard_total} available | "
                f"Today's revenue: ${self.daily_revenue:.2f}")
