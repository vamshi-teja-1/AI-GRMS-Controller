import random

class GRMSController:
    """
    Simulates the Room Controller Unit (RCU) and the RS-485 network 
    based on the physical wiring diagram.
    """
    def __init__(self):
        # Inputs (Sensors & Switches)
        self.key_card_inserted = False
        self.door_open = False
        self.window_open = False
        self.dnd_active = False # Do Not Disturb
        self.mur_active = False # Make Up Room
        
        # Thermostat (Input/Output)
        self.current_temp = 24.0
        self.target_temp = 22.0

        # Outputs (Relays & RS-485 / Dry Contacts)
        self.ac_unit_status = "OFF"
        self.lights = {
            "bed": "OFF",
            "ceiling": "OFF",
            "bathroom": "OFF"
        }

    def read_room_state(self):
        """Fetches the current state of all wired inputs."""
        return {
            "key_card": self.key_card_inserted,
            "door": self.door_open,
            "window": self.window_open,
            "dnd": self.dnd_active,
            "mur": self.mur_active,
            "current_temp": self.current_temp,
            "target_temp": self.target_temp
        }

    def execute_commands(self, commands):
        """Executes the AI's commands through the hardware relays."""
        if "ac" in commands:
            self.ac_unit_status = commands["ac"]
        if "lights" in commands:
            self.lights.update(commands["lights"])
            
        print("\n--- PHYSICAL HARDWARE UPDATED ---")
        print(f"AC Unit: {self.ac_unit_status}")
        print(f"Lights: Bed={self.lights['bed']}, Ceiling={self.lights['ceiling']}, Bath={self.lights['bathroom']}")
        print("---------------------------------\n")
