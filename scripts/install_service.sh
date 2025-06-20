#!/bin/bash

sudo cp /home/goat/projects/adafruit/scripts/systemd_unit /etc/systemd/system/adafruit.service
sudo systemctl daemon-reload
sudo systemctl enable adafruit.service
sudo systemctl start adafruit.service
sudo systemctl status adafruit.service