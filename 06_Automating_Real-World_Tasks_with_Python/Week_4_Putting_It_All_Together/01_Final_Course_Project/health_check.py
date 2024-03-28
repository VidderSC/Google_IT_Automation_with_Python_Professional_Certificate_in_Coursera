#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails
import time


def check_cpu_usage():
    """Check CPU usage and return True if it's over 80%, False otherwise."""
    usage = psutil.cpu_percent(1)
    return usage > 80


def check_disk_usage(disk):
    """Check disk usage and return True if it's less than 20%, False otherwise."""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free < 20


def check_memory_usage():
    """Check available memory and return True if it's less than 100MB, False otherwise."""
    svmem = psutil.virtual_memory()
    return svmem.available < 100 * 1024 * 1024  # 100MB


def check_localhost():
    """Check if localhost can be resolved to 127.0.0.1 and return False if not."""
    try:
        socket.gethostbyname('localhost')
        return False
    except:
        return True


def send_email_alert(error_type):
    """Send email alert for the specified error type."""
    sender = "automation@example.com"
    recipient = "student@example.com"
    subject = f"Error - {error_type}"
    body = "Please check your system and resolve the issue as soon as possible."
    email = emails.generate_email(sender, recipient, subject, body)
    emails.send_email(email)


def main():
    while True:
        if check_cpu_usage():
            send_email_alert("CPU usage is over 80%")
        if check_disk_usage("/"):
            send_email_alert("Available disk space is less than 20%")
        if check_memory_usage():
            send_email_alert("Available memory is less than 100MB")
        if check_localhost():
            send_email_alert("localhost cannot be resolved to 127.0.0.1")
        time.sleep(60)  # Check every 60 seconds


if __name__ == "__main__":
    main()
