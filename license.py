from constants import FREE_CREDITS

class License:
    def __init__(self):
        self.credits = FREE_CREDITS

    def check_credits_availability(self):
        return self.credits > 0

    def check_license_running_out(self):
        # Write the logic here
        return False

    def check_license(self):
        return self.check_credits_availability() and self.check_license_running_out()

license = License()
print(license.check_credits_availability())
print(license.check_license_running_out())
print(license.check_license())
