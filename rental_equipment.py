from abc import ABC, abstractmethod


class RentalEquipment(ABC):
    """
    Abstract parent class for any item that can be rented.
    Ski and Snowboard both inherit from this class.
    """

    def __init__(self, equipment_id):
        self._equipment_id = equipment_id
        self._is_rented = False

    # ---------- Properties (encapsulation) ----------

    @property
    def equipment_id(self):
        return self._equipment_id

    @property
    def is_rented(self):
        return self._is_rented

    @is_rented.setter
    def is_rented(self, value):
        self._is_rented = bool(value)

    # ---------- Abstract members (abstraction) ----------

    @property
    @abstractmethod
    def hourly_rate(self):
        """Each subclass must define its own hourly rate."""
        pass

    @property
    @abstractmethod
    def daily_rate(self):
        """Each subclass must define its own daily rate."""
        pass

    @property
    @abstractmethod
    def weekly_rate(self):
        """Each subclass must define its own weekly rate."""
        pass

    @abstractmethod
    def get_equipment_type(self):
        """Returns a string describing the type of equipment."""
        pass

    # ---------- Shared behavior ----------

    def calculate_best_price(self, rental_period, quantity):
        """
        Calculates the lowest available price for this piece of
        equipment given a rental period (hourly, daily, or weekly)
        and a quantity (number of hours, days, or weeks).

        Automatically applies a better rate if one is cheaper.
        Example: 4 hours of skis = $60 hourly, but the daily rate
        of $50 is cheaper, so $50 is charged instead.
        """
        rental_period = rental_period.lower()

        if rental_period == "hourly":
            hourly_total = self.hourly_rate * quantity
            return min(hourly_total, self.daily_rate)

        elif rental_period == "daily":
            daily_total = self.daily_rate * quantity
            if quantity >= 7:
                return min(daily_total, self.weekly_rate)
            return daily_total

        elif rental_period == "weekly":
            return self.weekly_rate * quantity

        else:
            raise ValueError("rental_period must be 'hourly', 'daily', or 'weekly'")

    def __str__(self):
        # Polymorphism: get_equipment_type() returns different text
        # depending on whether this is a Ski or Snowboard.
        return f"{self.get_equipment_type()} (ID: {self.equipment_id})"


class Ski(RentalEquipment):
    """Represents a single pair of skis available for rent."""

    HOURLY_RATE = 15.00
    DAILY_RATE = 50.00
    WEEKLY_RATE = 200.00

    @property
    def hourly_rate(self):
        return Ski.HOURLY_RATE

    @property
    def daily_rate(self):
        return Ski.DAILY_RATE

    @property
    def weekly_rate(self):
        return Ski.WEEKLY_RATE

    def get_equipment_type(self):
        return "Ski"


class Snowboard(RentalEquipment):
    """Represents a single snowboard available for rent."""

    HOURLY_RATE = 10.00
    DAILY_RATE = 40.00
    WEEKLY_RATE = 160.00

    @property
    def hourly_rate(self):
        return Snowboard.HOURLY_RATE

    @property
    def daily_rate(self):
        return Snowboard.DAILY_RATE

    @property
    def weekly_rate(self):
        return Snowboard.WEEKLY_RATE

    def get_equipment_type(self):
        return "Snowboard"
