public_P=11 #public key
public_G=7  #public key

pr_alice=3 #alice's private key
pr_bob=9   #bob's private key
pr_hacker_1=6  #hacker's 1st private key
pr_hacker_2=8  #hacker's 2nd private key


def basic(private_key):
    return public_G**private_key%public_P
def intercept(key,pr):
    return key**pr%public_P

alice_generated=basic(pr_alice) 
bob_generated=basic(pr_bob)       


print("Alice sends key to Bob :",alice_generated)
print("Bob sends key to Alice :",bob_generated)

hacker_generated_1 =basic(pr_hacker_1)
hacker_generated_2 =basic(pr_hacker_2)

print("Hacker generating key to send to alice and bob respectively with his own set of private keys")
print("Generated keys :",hacker_generated_1,",",hacker_generated_2)

print("Hacker intercepts Alice's key and sends his(Hacker) generated key value to Bob")
print("Hacker intercepts Bob's key and sends his(Hacker) generated key value to Alice")

print("Alice calculates key using Hacker's sent key value.")
print("Decrypted key  :", intercept(hacker_generated_1,pr_alice))

print("Bob calculates key using Hacker's sent key value")
print("Derypted key  :", intercept(hacker_generated_2,pr_bob))

print("Alice's key which Hacker intercepted ",intercept(alice_generated,pr_hacker_1))
print("Bob's key which Hacker intercepted ",intercept(bob_generated,pr_hacker_2))