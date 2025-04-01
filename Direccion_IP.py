class IPAddress:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def get_octets(self):
        return self.ip_address.split('.')

