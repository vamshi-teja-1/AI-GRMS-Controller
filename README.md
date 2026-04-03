#  AI-Powered Smart Hotel Room Controller (GRMS)

Building a modern Guest Room Management System (GRMS) isn't just about connecting wires; it's about creating an intelligent environment. In this project, I engineered a Python-based simulation of a GRMS Room Controller Unit (RCU) that uses a simulated **Google Gemma 4 Edge AI** model to manage hotel room climate, lighting, and energy efficiency.

##  System Architecture (The Hybrid Approach)
I designed this architecture to fuse rigid physical wiring diagrams with advanced IoT environmental sensors. 

### 1. The Hardware Layer (`rcu_hardware.py`)
This script acts as the nervous system, combining two distinct data streams:
* **Physical Contacts (Wiring Diagram):** Key Card Switch, Door/Window Contacts, and DND/MUR panels.
* **Environmental Sensors (IoT Specs):** Ambient Light (Lux), Indoor Air Quality (IAQ), Humidity, and Temperature.
* **Outputs:** Controls standard Lighting Relays and uses 0-10V analog signals for precise VFD fan control alongside RS-485 AC communication.

### 2. The AI Engine (`gemma_brain.py`)
Instead of relying on external cloud servers, the lightweight Gemma 4 Edge AI processes the multidimensional room state locally:
* **Contextual Lighting:** If a window is open, the AI checks the Ambient Light (Lux) sensor. If it's sunny outside, it keeps the lights off. If it's dark, it turns them on.
* **Air Quality Management:** If the IAQ index drops, the AI overrides standard climate controls to maximize VFD ventilation.
* **Predictive Energy Management:** When a guest removes their key card, the system steps down the climate control into a deep energy-saving mode and cuts power to the VFD fans.

##  How to Run the Simulation Locally
1. Clone this repository: `git clone https://github.com/yourusername/AI-GRMS-Controller.git`
2. Run the execution script: `python main.py`
3. Watch the console output as the AI reacts to complex, overlapping scenarios (e.g., poor air quality vs. open windows in bright daylight).
