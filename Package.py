from datetime import datetime
# Class for package objects.
class Package:

    def __init__(self, package_id, address_id, package_address, package_city, package_state, package_zip,
                 package_deadline, package_weight, package_notes):
        self.package_id = int(package_id)
        self.address_id = int(address_id)
        self.package_address = package_address
        self.package_city = package_city
        self.package_state = package_state
        self.package_zip = int(package_zip)
        self.package_deadline = package_deadline
        self.package_weight = package_weight
        self.package_notes = package_notes
        self.delivery_status = 'Warehouse'
        self.delivery_time = None

    # Overload method that prints the package object as a string.
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % ( self.package_id, self.address_id, self.package_address,
                                                    self.package_city, self.package_state, self.package_zip,
                                                    self.package_deadline, self.package_weight, self.package_notes,
                                                        self.delivery_status, self.delivery_time)

    def set_delivery_status(self, string):
        self.delivery_status = string

    def set_delivery_time(self, datetime):
        self.delivery_time = datetime.time()






