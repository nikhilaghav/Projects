# Duplicate File Removal Automation

## Overview

Duplicate File Removal Automation is a Python-based automation project designed to identify and delete duplicate files from a specified directory.

The application uses the **MD5 hashing algorithm** to compare file contents and identify duplicates. It automatically removes duplicate files while retaining one copy of each unique file.

The script also generates a detailed log file containing information about the scanning and deletion process and sends the log file as an email attachment using Gmail SMTP.

The automation is scheduled to execute every minute using Python's `schedule` library.

## Features

- Automatically scans directories and subdirectories.
- Identifies duplicate files using MD5 checksums.
- Detects duplicates based on file content rather than filenames.
- Deletes duplicate files while retaining one copy.
- Generates timestamp-based log files.
- Records total files scanned and duplicate files identified.
- Calculates the total execution time.
- Automatically sends log files through email.
- Uses environment variables for secure email authentication.
- Supports scheduled execution at regular intervals.

## Technologies Used

- **Programming Language:** Python
- **Libraries and Modules:**
  - `os` — Directory traversal and file deletion
  - `hashlib` — MD5 checksum generation
  - `schedule` — Automated task scheduling
  - `time` — Execution time measurement
  - `smtplib` — Sending emails through SMTP
  - `email.message` — Creating email messages and attachments

## Project Structure

```text
Duplicate_File_Removal/
│
├── DuplicateFileRemoval.py
├── requirements.txt
└── README.md
```

The program automatically generates log files during execution.


## How to Run

Execute the Python script:

```bash
python3 DuplicateFileRemoval.py
```

The application starts a scheduler that executes the duplicate removal operation every minute.

The program continues running until it is manually stopped.

Press `Ctrl + C` to stop execution.

## Working of the Application

### Step 1: Directory Validation

The application verifies whether the provided directory exists and is a valid directory.

### Step 2: File Scanning

The program recursively scans all files inside the specified directory and its subdirectories using `os.walk()`.

### Step 3: Checksum Generation

An MD5 checksum is generated for each file using the `hashlib` module.

Files containing identical data produce identical MD5 checksums.

### Step 4: Duplicate Identification

The generated checksums are stored in a dictionary.

Files having matching checksums are grouped together and treated as duplicates.

### Step 5: Duplicate Removal

The application retains the first encountered file from each duplicate group and deletes the remaining copies.

### Step 6: Log File Generation

A timestamp-based log file is created containing:

- Paths of detected duplicate files
- Total files scanned
- Total duplicate files identified
- Execution time
- Log creation timestamp

### Step 7: Email Notification

After the duplicate removal process, the application:

1. Creates an email message.
2. Attaches the generated log file.
3. Establishes a secure SMTP connection.
4. Authenticates using the Gmail App Password.
5. Sends the email to the configured recipient.

### Step 8: Task Scheduling

The `schedule` library executes the automation every minute.

## Example

Suppose the target directory contains:

```text
Test/
│
├── file1.txt
├── file2.txt
├── file3.txt
└── Backup/
    └── file4.txt
```

Assume:

- `file1.txt` and `file2.txt` contain identical data.
- `file3.txt` contains unique data.
- `file4.txt` contains the same data as `file1.txt`.

The program identifies three files with identical content.

It retains one copy and deletes the other two.

### Example Log Output

```text
----------------------------------------
 Marvellous Automation Script
----------------------------------------

Duplicate files:

Test/file1.txt
Test/file2.txt
Test/Backup/file4.txt

Total files scanned : 4
Total duplicate files : 2
Time required for execution: 0.0025

----------------------------------------
Log file gets created at : Tue Oct 27 14:00:00 2026
----------------------------------------
```

The generated log file is automatically attached to an email and sent to the configured recipient.

## Important Notes

- The application permanently deletes duplicate files.
- Deleted files are not moved to the Recycle Bin.
- The first file encountered in each duplicate group is retained.
- Files are compared using their contents, regardless of filenames.
- MD5 is used for duplicate detection, but hash collisions are theoretically possible.
- The application requires an internet connection to send email notifications.
- The application must remain running for scheduled execution.
- The current implementation does not provide a recovery mechanism for deleted files.

**Warning:** Test the application on a directory containing sample files before using it on important data
