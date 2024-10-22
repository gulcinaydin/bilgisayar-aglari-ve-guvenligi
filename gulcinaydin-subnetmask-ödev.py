import ipaddress

def hosts_from_subnet_mask(subnet_mask):
    network = ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}', strict=False)
    return network.num_addresses - 2  # Network ve broadcast adreslerini çıkartıyoruz

for subnet_mask in range(8, 31):
    total_hosts = hosts_from_subnet_mask(subnet_mask)
    print(f"Subnet mask: /{subnet_mask} - Toplam cihaz sayisi: {total_hosts}")
