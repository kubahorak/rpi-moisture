# Moisture sensor

## Hardware components

- Raspberry Pi
- Soil Moisture Hygrometer Detection Modul
- Witty Pi 2
- Big powerbank


## Installation

1. Install latest Raspbian on the Pi
1. Boot with HDMI monitor connected, connect to WiFi and enable SSH 
1. Install Ansible requirements `sudo ansible-galaxy install -r requirements.yml`
1. Run playbook `ansible-playbook -i hosts playbook.yml`
1. Install WittyPi 2
