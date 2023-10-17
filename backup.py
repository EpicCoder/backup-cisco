"""Backup Cisco config from a CSV file"""
import argparse

from colorama import just_fix_windows_console
from backup_cisco.utilities import read_csv_file, check_device_reachable
from backup_cisco.core import backup_cisco


def main():
    """App entry point"""
    parser = argparse.ArgumentParser(description="Backup Cisco config")
    parser.add_argument("csv_file", help="Path to a csv file")
    parser.add_argument("backup_dir", help="Path to the backup directory")
    args = parser.parse_args()

    just_fix_windows_console()

    switch_list = read_csv_file(args.csv_file)

    for switch in switch_list:
        if check_device_reachable(switch["device"], args.backup_dir):
            backup_cisco(switch["device"], args.backup_dir,
                         switch["user"], switch["password"])


if __name__ == "__main__":
    main()
