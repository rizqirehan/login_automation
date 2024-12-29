from helium import start_chrome, write, press, ENTER

class DiscordBot:
    def __init__(self, email, password):
        """
        Initializes the DiscordBot object with an email and password.
        """
        self.email = email
        self.password = password

    def login(self):
        """
        Method to automate login to Discord.
        """
        # Open the browser and navigate to the Discord login page
        print("Opening the browser and navigating to the Discord login page...")
        browser = start_chrome("https://discord.com/login", headless=False)  # Set headless=True for headless mode

        # Fill in the "Email or Phone Number" field
        print("Filling in the email...")
        write(self.email, into="Email or Phone Number")

        # Fill in the "Password" field
        print("Filling in the password...")
        write(self.password, into="Password")

        # Press ENTER to log in automatically
        print("Pressing ENTER to log in automatically...")
        press(ENTER)

        # Add logic to handle successful or failed login
        print("Login attempt completed.")
        return browser

# Example usage of the DiscordBot class
if __name__ == "__main__":
    # Enter your email and password here
    email = "your_email@example.com"
    password = "your_password"

    # Create a bot object
    bot = DiscordBot(email, password)

    # Perform automatic login
    bot.login()
