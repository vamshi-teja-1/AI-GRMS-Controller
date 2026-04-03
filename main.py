import time
from rcu_hardware import GRMSController
from gemma_brain import Gemma4Edge

def run_simulation():
    print("Initializing AI-Powered GRMS Room Controller Unit (RCU)...")
    
    # Initialize the wiring diagram hardware and AI brain
    rcu = GRMSController()
    ai = Gemma4Edge()

    # --- SIMULATION SCENARIO 1: Guest enters the room ---
    print("\n>>> SCENARIO 1: Guest inserts Key Card.")
    rcu.key_card_inserted = True
    rcu.door_open = False
    
    state = rcu.read_room_state()
    commands = ai.analyze_and_predict(state)
    rcu.execute_commands(commands)
    time.sleep(2)

    # --- SIMULATION SCENARIO 2: Guest opens the window ---
    print(">>> SCENARIO 2: Guest opens the window.")
    rcu.window_open = True
    
    state = rcu.read_room_state()
    commands = ai.analyze_and_predict(state)
    rcu.execute_commands(commands)
    time.sleep(2)

    # --- SIMULATION SCENARIO 3: Guest removes key card and leaves ---
    print(">>> SCENARIO 3: Guest leaves and removes Key Card.")
    rcu.key_card_inserted = False
    rcu.window_open = False # They closed it before leaving
    
    state = rcu.read_room_state()
    commands = ai.analyze_and_predict(state)
    rcu.execute_commands(commands)

if __name__ == "__main__":
    run_simulation()
