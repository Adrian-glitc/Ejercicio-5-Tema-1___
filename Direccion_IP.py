class IPAddress:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def get_octets(self):
        return self.ip_address.split('.')
    
def main():
    ip = input("Introduce una dirección IP: ")
    ip_obj = IPAddress(ip)
    octets = ip_obj.get_octets()
    
    print("Los octetos de la dirección IP son:")
    for i, octet in enumerate(octets, start=1):
        print(f"Octeto {i}: {octet}")
