# Moisture sensors

Read the accompanying blog posts [Connecting plants to the internet](https://zee.cz/2017/07/connecting-plants-to-the-internet/).
and ... TODO

## Hardware components

- Raspberry Pi 3
- 2x Soil Moisture Hygrometer Detection Modul
- Witty Pi 2
- 3-6V Mini Submersible Water Pump

## Prerequisites

- ThingSpeak account for data results
- Datadog account for monitoring

## Configuration

Modify `moisture.py` `sensors` and `pumps` variables for your setup.

## Installation

1. Install latest Raspbian on the Pi
1. Boot with HDMI monitor connected, connect to WiFi and enable SSH 
1. Install Ansible requirements `sudo ansible-galaxy install -r requirements.yml`
1. Run playbook `sudo ansible-playbook -i hosts playbook.yml --extra-vars "datadog_api_key=XXX"` (add
   `--ask-pass` if SSH is set-up via password authentication)
1. Install WittyPi 2 following the [manual](http://www.uugear.com/doc/WittyPi2_UserManual.pdf) and configure it to use the `schedule.wpi` file provided here

