```python
import os
import shutil
import datetime

# Define the source and destination paths
source_path = "/path/to/database"
backup_path = "/path/to/backup"

def backup_data():
    try:
        # Get the current date and time
        now = datetime.datetime.now()
        date_time = now.strftime("%Y%m%d%H%M%S")

        # Create a backup directory with the current date and time
        dest = os.path.join(backup_path, date_time)
        os.makedirs(dest)

        # Copy the database files to the backup directory
        for file_name in os.listdir(source_path):
            if file_name.endswith('.db'):
                shutil.copy2(os.path.join(source_path, file_name), dest)

        print("Backup successful.")
    except Exception as e:
        print("Backup failed due to: ", str(e))

def trigger_backup():
    # Trigger the backup process
    backup_data()

if __name__ == "__main__":
    trigger_backup()
```