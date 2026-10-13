Platform Surveillance System

📌 Project Overview

The Platform Surveillance System is a Python-based automation project that monitors system resources and running processes. It collects system information such as CPU usage, RAM utilization, network statistics, and process details, and stores the collected information in timestamped log files.

The program uses the schedule library to execute the monitoring task automatically at a user-defined time interval.

🎯 Objectives

-Monitor CPU usage and the number of CPU cores.

-Track RAM utilization and total memory.

-Collect network data sent and received.

-Retrieve details of running processes.

-Record process CPU and memory usage.

-Automatically generate timestamped log files.

-Schedule system monitoring at regular intervals.

✨ Features

CPU Monitoring: Retrieves the number of CPU cores and overall CPU utilization.

RAM Monitoring: Records memory utilization percentage and total RAM.

Network Monitoring: Tracks the total data sent and received over the network.

Process Monitoring: Collects process ID, process name, username, status, CPU usage, and memory usage.

Automatic Logging: Generates separate log files with date and time information.

Task Scheduling: Runs monitoring tasks automatically at a specified interval.

Command-Line Interface: Supports help and usage options.

🛠️ Technologies Used

Programming Language: Python 3

psutil: For collecting system and process information.

schedule: For scheduling periodic monitoring tasks.

os: For directory and file path operations.

sys: For handling command-line arguments.

time: For timestamps and execution delays.

