import random
import time
import threading

class TempMail:
    def __init__(self, domain="tmailor.com"):
        self.domain = domain
        self.email = self._generate_email()
        self.inbox = []
        self.status = "Pending"

    def _generate_email(self):
        username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))
        return f"{username}@{self.domain}"

    def get_email(self):
        return self.email

    def wait_for_messages(self, timeout=60, check_interval=5):
        """
        Wait for incoming messages with periodic status updates.
        """
        print(f"Email created successfully: {self.email}")
        print("Done ✅ success")
        print("Pending waiting for incoming messages...")

        waited = 0
        while waited < timeout:
            if self.inbox:
                self.status = "Received"
                print(f"Received {len(self.inbox)} message(s).")
                return self.inbox

            # Status updates at intervals
            if waited == 0:
                print("Waiting for incoming messages..")
            elif waited == check_interval * 1:
                print("In progress...")
            elif waited == check_interval * 2:
                print("Queued. Please wait ...")
            elif waited == check_interval * 3:
                print("Inbox email 📥")
                print("Inbox.")
                print("Email waiting for incoming messages... Please wait.")
            elif waited >= check_interval * 4:
                print("RUNNING... RUNNING running... Running... Running... Running...   Running...   On")

            time.sleep(check_interval)
            waited += check_interval

        self.status = "Timeout"
        print("Timeout reached, no messages received.")
        return []

    def add_message(self, message):
        self.inbox.append(message)

def simulate_incoming_message(mail):
    # Simulate delay before receiving a message
    time.sleep(random.randint(10, 20))
    mail.add_message("Sample incoming message")

if __name__ == "__main__":
    temp_mail = TempMail()
    print(f"Random email created successfully: {temp_mail.get_email()}")

    # Start background thread to simulate incoming message
    threading.Thread(target=simulate_incoming_message, args=(temp_mail,), daemon=True).start()

    messages = temp_mail.wait_for_messages(timeout=60)
    if messages:
        print("Received messages:")
        for msg in messages:
            print(f"- {msg}")
    else:
        print("No messages received.")

    print("Done ✅ success pending waiting for incoming messages")
