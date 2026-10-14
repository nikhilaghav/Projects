Duplicate File Removal Automation

📌 Project Overview

The Duplicate File Removal Automation project is a Python-based automation tool that scans a specified directory, identifies duplicate files using MD5 checksums, deletes duplicate copies, and generates a log file containing the details of the operation.

The generated log file is automatically sent as an email attachment using Gmail SMTP over an SSL connection. The program uses the schedule library to execute the duplicate file removal task at regular intervals.

🎯 Objectives

Identify duplicate files in a specified directory.

Calculate file checksums using the MD5 hashing algorithm.

Delete duplicate copies while retaining one copy of each file.

Generate a timestamped log file containing execution details.

Automatically email the log file as an attachment.

Schedule the automation task to run every minute.

🛠️ Technologies Used

Programming Language: Python

Operating System: Ubuntu / Linux

Modules:

os – Directory traversal, path validation, and file deletion.

hashlib – Calculates MD5 checksums.

schedule – Schedules periodic execution.

time – Measures execution time and manages delays.

smtplib – Establishes an SMTP connection to Gmail.

email.message.EmailMessage – Creates email messages and attachmen
