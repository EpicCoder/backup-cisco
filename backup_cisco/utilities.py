"""Miscellaneous utility functions"""

import os
import csv
import sys

from colorama import Fore, Style
from ping3 import ping


def color_print(msg, color):
    """Print a message in color"""
    print(f"{color}{msg}{Style.RESET_ALL}")


def check_dir_exists(dir_path):
    """Check if a directory exists"""
    if not os.path.isdir(dir_path):
        color_print(f"Invalid directory [{dir_path}]", Fore.RED)
        sys.exit(1)


def check_file_exists(file_path):
    """Check if a file exists"""
    if not os.path.isfile(file_path):
        color_print(f"Invalid file [{file_path}]", Fore.RED)
        sys.exit(1)


def check_device_reachable(device, backup_dir):
    """Check if a device is reachable"""
    check_dir_exists(backup_dir)
    if ping(device, 10) is None:
        color_print(f"Device [{device}] is not reachable", Fore.RED)
        with open(os.path.join(backup_dir, "down_devices.txt"), "a", encoding="utf-8") as f:
            f.write(f"{device}\n")
        return False
    return True


def store_failed_device(device, backup_dir):
    """Store failed devices in a file"""
    check_dir_exists(backup_dir)
    with open(os.path.join(backup_dir, "failed_devices.txt"), "a", encoding="utf-8") as f:
        f.write(f"{device}\n")


def read_csv_file(file_path):
    """Read a CSV file"""
    check_file_exists(file_path)
    with open(file_path, 'r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return list(csv_reader)
