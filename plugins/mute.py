import datetime

class User:
    def __init__(self, name):
        self.name = name
        self.muted = False
        self.mute_expiry = None

class Group:
    def __init__(self):
        self.users = []

    def mute_user(self, user, duration_minutes):
        if user in self.users:
            user.muted = True
            mute_duration = datetime.timedelta(minutes=duration_minutes)
            user.mute_expiry = datetime.datetime.now() + mute_duration

    def unmute_user(self, user):
        if user in self.users:
            user.muted = False
            user.mute_expiry = None

    def send_message(self, user, message):
        if user in self.users:
            if user.muted:
                if datetime.datetime.now() < user.mute_expiry:
                    print(f"{user.name} is muted. Message not sent.")
                    return
                else:
                    self.unmute_user(user)

            print(f"{user.name}: {message}")

# Example usage
group = Group()

# Create users
user1 = User("Manu")
user2 = User("John")

# Add users to the group
group.users.extend([user1, user2])

# Mute user1 for 60 minutes
group.mute_user(user1, 60)

# Send messages
group.send_message(user1, "Hello, everyone!")  # Output: Manu is muted. Message not sent.
group.send_message(user2, "Hi, Manu!")  # Output: John: Hi, Manu!

# Wait for mute duration to expire
import time
time.sleep(60)

# Send message again
group.send_message(user1, "Hello, everyone!")  # Output: Manu: Hello, everyone!
