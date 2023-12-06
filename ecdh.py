import random

# Simplified elliptic curve parameters
a = 2
b = 2
p = 17  # A prime number
G = (15, 6)  # Generator point (x, y)

# Alice's private key
private_key_alice = random.randint(1, p - 1)

# Bob's private key
private_key_bob = random.randint(1, p - 1)

# Alice's public key
public_key_alice = (private_key_alice * G[0], private_key_alice * G[1])

# Bob's public key
public_key_bob = (private_key_bob * G[0], private_key_bob * G[1])

# Key exchange
shared_secret_alice = (private_key_alice * public_key_bob[0], private_key_alice * public_key_bob[1])
shared_secret_bob = (private_key_bob * public_key_alice[0], private_key_bob * public_key_alice[1])

# Both parties should have the same shared secret
print("Shared Secret (Alice):", shared_secret_alice)
print("Shared Secret (Bob):", shared_secret_bob)
