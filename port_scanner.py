import socket

target = input("Enter target IP: ")

print(f"\nScanning {target}...\n")

for port in range(1, 1025):
    s = socket.socket()
    s.settimeout(0.5)

    try:
        s.connect((target, port))
        print(f"[OPEN] Port {port}")
    except:
        pass

    s.close()

print("\nScan finished!")
