# import random

# # Simplified elliptic curve parameters (y^2 = x^3 + ax + b)
# a = 2
# b = 2
# p = 17  # A prime number
# G = (15, 6)  # Generator point (x, y)

# # Random private key
# private_key = random.randint(1, p - 1)

# # Generating public key
# public_key = (private_key * G[0], private_key * G[1])

# # Message to sign
# message = "Hello, World!"

# # Signing the message
# def sign_message(private_key, message):
#     # Create a random value k
#     k = random.randint(1, p - 1)
    
#     # Calculate (x1, y1) = k * G
#     x1, y1 = (k * G[0], k * G[1])
    
#     # Calculate r = x1 % p
#     r = x1 % p
    
#     # Calculate s = (hash(message) + private_key * r) / k
#     h = hash(message)
#     s = ((h + private_key * r) * pow(k, -1, p)) % p
    
#     return (r, s)

# signature = sign_message(private_key, message)

# # Verifying the signature
# def verify_signature(public_key, message, signature):
#     r, s = signature
#     h = hash(message)
    
#     # Calculate w = s^-1 % p
#     w = pow(s, -1, p)
    
#     # Calculate u1 = (hash(message) * w) % p
#     u1 = (h * w) % p
    
#     # Calculate u2 = (r * w) % p
#     u2 = (r * w) % p
    
#     # Calculate (x1, y1) = u1 * G + u2 * public_key
#     x1, y1 = (u1 * G[0] + u2 * public_key[0], u1 * G[1] + u2 * public_key[1])
    
#     # Calculate v = x1 % p
#     v = x1 % p
    
#     return v == r

# verified = verify_signature(public_key, message, signature)
# print("Signature verified:", verified)


import random


prime = 23
a = 1
b = 1
Gx = 5
Gy = 19


def point_add(p, q, prime):
    if p is None:
        return q
    if q is None:
        return p
    x1, y1 = p
    x2, y2 = q
    if p != q:
        s = ((y2 - y1) * pow(x2 - x1, prime - 2, prime)) % prime
    else:
        s = ((3 * x1 * x1) * pow(2 * y1, prime - 2, prime)) % prime
    x3 = (s * s - x1 - x2) % prime
    y3 = (s * (x1 - x3) - y1) % prime
    return x3, y3


def scalar_mult(k, point, prime):
    result = None
    
    for i in range(min(k, 10)):  
        result = point_add(result, point, prime)
    return result



k = random.randint(1, 10)
print("Scalar (k):", k)


base_point = (Gx, Gy)
print("Base Point:", base_point)


result = scalar_mult(k, base_point, prime)
print("Result of Scalar Multiplication (limited steps):", result)

