#----------------------------------------------------------------------------
# The assigned class library does not store rentals or keep track of which
# rentals have been returned. This class was added to the application so the
# shop can look up a rental later when the customer brings the equipment
# back. It holds the Rental object from the assigned library along with the
# information the application needs.
#----------------------------------------------------------------------------


class ActiveRental(object):
    """Holds one rental so it can be found again at return time."""

    def __init__(self, customer_number, rental, ski_count, snowboard_count, estimated_length):
        self._customer_number = customer_number
        self._rental = rental
        self._ski_count = ski_count
        self._snowboard_count = snowboard_count
        self._estimated_length = estimated_length
        self._is_returned = False

    #------------------------------------------------------------------------
    # properties
    #------------------------------------------------------------------------
    @property
    def customer_number(self):
        return self._customer_number

    @property
    def rental(self):
        return self._rental

    @property
    def ski_count(self):
        return self._ski_count

    @property
    def snowboard_count(self):
        return self._snowboard_count

    @property
    def estimated_length(self):
        return self._estimated_length

    @property
    def is_returned(self):
        return self._is_returned

    @is_returned.setter
    def is_returned(self, value):
        self._is_returned = bool(value)