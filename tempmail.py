import random
import time
import threading

class TempMail:
    def __init__(self, domain="tmailor.com"):
        self.domain = domain
        self.email = self._generate_email()
        self.inbox = []

    def _generate_email(self):
        username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))
        return f"{username}@{self.domain}"

    def get_email(self):
        return self.email

    def wait_for_messages(self, timeout=60, check_interval=5):
        """
        Wait for incoming messages with periodic status updates.
        """
        print(f"Waiting for incoming messages to {self.email}...")
        waited = 0
        while waited < timeout:
            if self.inbox:
                print(f"Received {len(self.inbox)} message(s).")
                return self.inbox
            print("Waiting for incoming messages..")
            time.sleep(check_interval)
            waited += check_interval
        print("Timeout reached, no messages received.")
        return []

    def add_message(self, message):
        self.inbox.append(message)

def simulate_incoming_message(mail):
    # Simulate delay before receiving a message
    time.sleep(random.randint(5, 15))
    mail.add_message("Sample incoming message")

if __name__ == "__main__":
    temp_mail = TempMail()
    print(f"Random email created successfully: {temp_mail.get_email()}")
    print("Done ✅ success")

    # Start background thread to simulate incoming message
    threading.Thread(target=simulate_incoming_message, args=(temp_mail,), daemon=True).start()

    messages = temp_mail.wait_for_messages(timeout=30)
    if messages:
        print("Received messages:")
        for msg in messages:
            print(f"- {msg}")
    else:
        print("No messages received.")

    print("Done ✅ success pending waiting for incoming messages")
