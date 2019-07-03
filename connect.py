from auth import MiBand3

MAC_ADDR = input("Band MAC address: ")
print('Attempting to connect to ', MAC_ADDR)

band = MiBand3(MAC_ADDR, debug=True)
band.setSecurityLevel(level = "medium")

if band.initialize():
    print("Initialized...")
    
else:
    band.authenticate()
