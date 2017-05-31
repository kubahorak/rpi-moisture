#scp -r ../Moisture-Sensor pi@raspberrypi:~
rsync -av --exclude '.git' ../Moisture-Sensor pi@raspberrypi:~
