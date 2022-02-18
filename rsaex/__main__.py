# Dummy run
from rsaex.User import User

# Create the users, constructor generates keypair
bob = User("bob")
alice = User("alice")

# Initiate key exchange from either user or use classmethod
# alice.perform_key_exchange(bob)
User.exchange_keypair(bob, alice)

# Now alice has bob's public key, and vice versa.
alice_message = f"My name is {alice.name}, ntmy!"
bob_message = f"My name is {bob.name}, ntmy2!"

# Encrypt the messages
alice.encrypt_message_for_user("bob", alice_message)
bob.encrypt_message_for_user("alice", bob_message)

# For demo purposes, they're stored in User.message_store
alice_encrypted_message = alice.message_store.pop()
bob_encrypted_message = bob.message_store.pop()

print("Mallory Sees:")
print(alice_encrypted_message)
print(bob_encrypted_message)

# And we can easily decrypt
print("Bob Receives:")
bob.decrypt_message(alice_encrypted_message)

print("Alice Receives:")
alice.decrypt_message(bob_encrypted_message)
