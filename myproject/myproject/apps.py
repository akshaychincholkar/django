import time
from django.apps import AppConfig
from threading import Thread

class MyAppConfig(AppConfig):
    name = 'myproject'

    def ready(self):
        # Start the delayed task in a separate thread to avoid blocking the server
        Thread(target=self.start_after_delay).start()

    def start_after_delay(self):
        # Delay the task for 5 seconds
        time.sleep(5)

        # Your code to run after the delay
        print("This code runs 5 seconds after the server starts.")
        # Example: Call a custom task
        self.run_my_task()

    def run_my_task(self):
        # Your custom task logic here
        print("Running the custom task...")
