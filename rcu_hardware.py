class GRMSController:
    """
    Simulates the Room Controller Unit (RCU).
    Integrates physical wiring (RS-485/Dry Contacts) with advanced built-in
    environmental sensors (IAQ, Humidity, Light).
    """

    def __init__(self):
        # --- WIRING DIAGRAM INPUTS (Physical Contacts) ---
        self.key_card_inserted = False
        self.door_open = False
        self.window_open = False
        self.dnd_active = False
        self.mur_active = False

        # --- BUILT-IN SENSOR SUITE (Environmental) ---
        self.temperature_c = 24.0
        self.target_temp = 22.0
        self.humidity_rh = 55  # Range: 30-95%
        self.light_lux = 100  # Ambient light
        self.iaq_index = 40  # Indoor Air Quality (Lower is better)
        self.proximity_detected = False

        # --- OUTPUTS (Relays & Analog VFD) ---
        self.ac_unit_status = "OFF"
        self.vfd_fan_signal = 0.0  # 0-10V Analog Output for precise fan control
        self.lights = {
            "bed": "OFF",
            "ceiling": "OFF",
            "bathroom": "OFF"
        }

    def read_room_state(self):
        """Fetches the complete combined state of the room."""
        return {
            "key_card": self.key_card_inserted,
            "window": self.window_open,
            "dnd": self.dnd_active,
            "temp": self.temperature_c,
            "target": self.target_temp,
            "humidity": self.humidity_rh,
            "lux": self.light_lux,
            "iaq": self.iaq_index,
            "proximity": self.proximity_detected
        }

    def execute_commands(self, commands):
        """Executes AI commands to the physical relays and analog outputs."""
        if "ac" in commands:
            self.ac_unit_status = commands["ac"]
        if "vfd" in commands:
            self.vfd_fan_signal = commands["vfd"]
        if "lights" in commands:
            self.lights.update(commands["lights"])

        print("\n=== HARDWARE OUTPUTS UPDATED ===")
        print(f"AC Unit (RS-485):  {self.ac_unit_status}")
        print(f"VFD Fan (0-10V):   {self.vfd_fan_signal}V")
        print(
            f"Lighting Relays:   Bed={self.lights['bed']} | Ceiling={self.lights['ceiling']} | Bath={self.lights['bathroom']}")
        print("================================\n")