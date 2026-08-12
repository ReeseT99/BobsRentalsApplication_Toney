class Customer(object):
    """Stores information about the customer paying for a rental."""

    def __init__(self, customer_id, name):
        self._customer_id = customer_id
        self._name = name

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Customer name cannot be empty")
        self._name = value

    def __str__(self):
        return f"Customer {self.customer_id}: {self.name}"
