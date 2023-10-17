# Backup Cisco

Script for automatic configuration backup of multiple Cisco devices

## Features

- Automate backup of device running-config
- No user interaction is required
- CSV list with all devices to back up
- Different credentials per device are possible
- Stores unreachable devices in file `down_devices.txt`
- Stores failed devices in file `failed_devices.txt`


## Usage

```
$ python backup.py csv_file backup_dir
```

Use help to see all arguments:

```
$ python backup.py -h
```

## Installation

If `pipenv` not already installed:

```
$ pip install pipenv --user
```

To install all dependencies:

```
$ pipenv install
```
