class Gemma4Edge:
    """
    Gemma 4 Edge AI simulating contextual comfort and predictive energy management.
    """

    def analyze_and_predict(self, state):
        print("[GEMMA 4 INFERENCE] Analyzing multi-dimensional room state...")
        commands = {}

        # 1. Vacancy Check (Priority 1)
        if not state["key_card"]:
            print("[GEMMA 4 DECISION] Room vacant. Engaging deep energy saving mode.")
            commands["ac"] = "OFF"
            commands["vfd"] = 0.0
            commands["lights"] = {"bed": "OFF", "ceiling": "OFF", "bathroom": "OFF"}
            return commands

        # 2. Open Window Check (Priority 2)
        if state["window"]:
            print("[GEMMA 4 DECISION] Window open. Disabling AC. Running VFD fan low for circulation.")
            commands["ac"] = "OFF"
            commands["vfd"] = 2.0

            # Smart Lighting: Only turn on lights if the room is dark (Lux < 200)
            if state["lux"] < 200:
                commands["lights"] = {"ceiling": "ON"}
            else:
                commands["lights"] = {"ceiling": "OFF"}
            return commands

        # 3. Climate & Air Quality Optimization (Active Room)
        commands["lights"] = {"ceiling": "ON"}  # Default active lighting

        if state["iaq"] > 80:
            print("[GEMMA 4 DECISION] Poor Indoor Air Quality detected. Maximizing VFD ventilation.")
            commands["ac"] = "VENTILATION_MODE"
            commands["vfd"] = 10.0  # Max 10V signal
            return commands

        if state["temp"] > state["target"] or state["humidity"] > 65:
            print("[GEMMA 4 DECISION] Cooling/Dehumidification required. Adjusting proportional valves.")
            commands["ac"] = "COOLING_MODE"
            commands["vfd"] = 7.5  # Medium-High fan speed
        else:
            print("[GEMMA 4 DECISION] Optimal climate reached. Maintaining steady state.")
            commands["ac"] = "STANDBY"
            commands["vfd"] = 3.0  # Low background circulation

        return commands