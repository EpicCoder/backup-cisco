"""Device Backup Module"""

import os
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException
from backup_cisco.utilities import color_print, check_dir_exists, store_failed_device, Fore


def backup_cisco(device, backup_dir, username, password):
    """Backup Cisco Config"""

    check_dir_exists(backup_dir)

    cisco_device = {
        'device_type': 'cisco_ios',
        'ip': device,
        'username': username,
        'password': password,
    }

    try:
        with ConnectHandler(**cisco_device) as net_connect:
            net_connect.enable()
            output = net_connect.send_command("show running-config")
            backup_path = os.path.join(backup_dir, f"{device}.txt")

            with open(backup_path, "w", encoding="utf-8") as backup_file:
                backup_file.write(output)

            color_print(
                f"Successfully saved running-config of device [{device}]", Fore.GREEN)
    except NetmikoAuthenticationException:
        color_print(f"Authentication to device [{device}] failed", Fore.RED)
        store_failed_device(device, backup_dir)
    except NetmikoTimeoutException:
        color_print(f"Timeout of device [{device}]", Fore.RED)
        store_failed_device(device, backup_dir)
