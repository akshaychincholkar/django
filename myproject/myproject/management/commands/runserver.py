import time
from django.core.management.commands.runserver import Command as RunserverCommand
from threading import Thread

class Command(RunserverCommand):

    def inner_run(self, *args, **options):
        # Call the original inner_run logic first
        result = super().inner_run(*args, **options)

        # Start the delayed task in a separate thread to avoid blocking the server
        Thread(target=self.start_after_delay).start()

        return result

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
