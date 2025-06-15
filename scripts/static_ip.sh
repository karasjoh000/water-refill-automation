#!/bin/bash
nmcli connection modify "Wired connection 1" ipv4.addresses 192.168.1.1/24 ipv4.method manual
nmcli connection up ifname enx000ec667e0b1