import rsa

class User(object):
    def __init__(self, name):
        self.name = name
        self.public_key, self.private_key = rsa.newkeys(512)
        self.contact_keystore = {}

        ## POC
        self.message_store = []

    def encrypt_message_for_user(self, name, message):
        target_public_key = self.contact_keystore.get(name, None)
        if not target_public_key:
            print("Sorry, no public key for that contact!")
        else:
            target_encrypted_message = rsa.encrypt(message.encode(), target_public_key)
            self.message_store.append(target_encrypted_message)

    def obtain_message_store(self):
        return self.message_store

    def obtain_public_key(self):
        return self.public_key

    def perform_key_exchange(self, other_user):
        if other_user.name not in self.contact_keystore:
            self.contact_keystore[other_user.name] = other_user.obtain_public_key()
            other_user.perform_key_exchange(self)

    def decrypt_message(self, message):
        # It does not matter who the message is from, they encrypted with our key!
        decrypted_message = rsa.decrypt(message, self.private_key).decode()
        print(decrypted_message)

    @classmethod
    def exchange_keypair(cls, user, other_user):
        if user.name not in other_user.contact_keystore:
            other_user.contact_keystore[user.name] = user.obtain_public_key()
        if other_user.name not in user.contact_keystore:
            user.contact_keystore[other_user.name] = other_user.obtain_public_key()
