import time
from rcu_hardware import GRMSController
from gemma_brain import Gemma4Edge


def run_simulation():
    print("Initializing Hybrid AI-Powered GRMS Room Controller...")

    rcu = GRMSController()
    ai = Gemma4Edge()

    # --- SCENARIO 1: Guest enters, but air quality is bad ---
    print("\n>>> SCENARIO 1: Guest inserts Key Card. Room has poor air quality (IAQ: 90).")
    rcu.key_card_inserted = True
    rcu.iaq_index = 90

    state = rcu.read_room_state()
    commands = ai.analyze_and_predict(state)
    rcu.execute_commands(commands)
    time.sleep(3)

    # --- SCENARIO 2: Air quality improves, but it's sunny outside ---
    print(">>> SCENARIO 2: Air quality normalizes (IAQ: 40). Guest opens window. It is bright (Lux: 800).")
    rcu.iaq_index = 40
    rcu.window_open = True
    rcu.light_lux = 800

    state = rcu.read_room_state()
    commands = ai.analyze_and_predict(state)
    rcu.execute_commands(commands)
    time.sleep(3)

    # --- SCENARIO 3: Guest leaves the room ---
    print(">>> SCENARIO 3: Guest leaves and removes Key Card.")
    rcu.key_card_inserted = False
    rcu.window_open = False

    state = rcu.read_room_state()
    commands = ai.analyze_and_predict(state)
    rcu.execute_commands(commands)


if __name__ == "__main__":
    run_simulation()