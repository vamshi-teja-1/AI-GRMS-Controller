#  AI-Powered Smart Hotel Room Controller (GRMS)

Building a modern Guest Room Management System (GRMS) isn't just about connecting wires; it's about creating an intelligent environment. In this project, I engineered a Python-based simulation of a GRMS Room Controller Unit (RCU) that uses a simulated **Google Gemma 4 Edge AI** model to manage hotel room climate, lighting, and energy efficiency.

Traditional systems use rigid, rule-based logic (e.g., "if keycard removed, cut power"). I wanted to build something smarter. By treating the hardware (relays, RS-485 network) as the "nervous system," I implemented an AI "brain" that analyzes the entire state of the room simultaneously to make contextual, energy-saving decisions.

##  System Architecture

I designed this project to strictly mirror real-world hotel wiring diagrams. The architecture is split into two distinct layers:

### 1. The Hardware Layer (`rcu_hardware.py`)
This script simulates the physical inputs and outputs of the RCU:
* **Inputs (Sensors/Switches):** Key Card Switch, Door/Window Contacts, and DND/MUR (Do Not Disturb / Make Up Room) panels.
* **Outputs (Relays/Dry Contacts):** Lighting control relays (Bed, Ceiling, Bathroom) and RS-485/Dry Contacts communicating with the AC Unit (FCU).

### 2. The AI Engine (`gemma_brain.py`)
This script acts as the lightweight Gemma 4 Edge model. Instead of relying on external cloud servers, the AI processes the room's sensor vectors locally. It evaluates:
* **Occupancy vs. Context:** If the room is occupied but a window is opened, the AI turns off the AC to prevent energy waste, while keeping the lights on.
* **Predictive Energy Management:** When a guest leaves, the system doesn't just cut power blindly; it steps down the climate control into a deep energy-saving mode.

##  How to Run the Simulation Locally

To see the AI logic interacting with the physical hardware simulation, you can run the execution script directly on your machine.

1. Ensure you have Python 3 installed.
2. Clone this repository:
   `git clone https://github.com/yourusername/AI-GRMS-Controller.git`
3. Navigate into the directory:
   `cd AI-GRMS-Controller`
4. Run the main execution script:
   `python main.py`

Watch the console output as the AI reacts to different guest scenarios (entering the room, opening a window, and leaving)!
