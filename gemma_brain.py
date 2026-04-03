class Gemma4Edge:
    """
    Simulates the local Gemma 4 AI processing complex room states
    to optimize comfort and energy usage.
    """
    def analyze_and_predict(self, state):
        print("[GEMMA 4] Analyzing room state vectors...")
        commands = {}

        # Scenario 1: Guest just left the room (Key card removed)
        if not state["key_card"]:
            print("[GEMMA 4 DECISION] Room is vacant. Engaging deep energy saving mode.")
            commands["ac"] = "OFF"
            commands["lights"] = {"bed": "OFF", "ceiling": "OFF", "bathroom": "OFF"}
            return commands

        # Scenario 2: Guest is in the room, but the window is open
        if state["window"]:
            print("[GEMMA 4 DECISION] Window contact open. Disabling AC to prevent energy waste.")
            commands["ac"] = "OFF"
            commands["lights"] = {"ceiling": "ON"} # Keep lights on, they are in the room
            return commands

        # Scenario 3: Standard active room climate control
        if state["current_temp"] > state["target_temp"]:
            print("[GEMMA 4 DECISION] Cooling required. Optimizing AC via RS-485 network.")
            commands["ac"] = "COOLING_MODE"
        else:
            print("[GEMMA 4 DECISION] Optimal temperature reached. AC to standby.")
            commands["ac"] = "STANDBY"
            
        # Ensure default lighting if card is in
        commands["lights"] = {"ceiling": "ON", "bathroom": "OFF", "bed": "OFF"}

        return commands
