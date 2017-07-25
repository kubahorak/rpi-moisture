# Moisture sensor

Read the accompanying blog post [Connecting plants to the internet](https://zee.cz/2017/07/connecting-plants-to-the-internet/).

## Hardware components

- Raspberry Pi 3
- Soil Moisture Hygrometer Detection Modul
- Witty Pi 2
- Big powerbank


## Installation

1. Install latest Raspbian on the Pi
1. Boot with HDMI monitor connected, connect to WiFi and enable SSH 
1. Install Ansible requirements `sudo ansible-galaxy install -r requirements.yml`
1. Run playbook `ansible-playbook -i hosts playbook.yml`
1. Install WittyPi 2 following the [manual](http://www.uugear.com/doc/WittyPi2_UserManual.pdf) and configure it to use the `schedule.wpi` file provided here
