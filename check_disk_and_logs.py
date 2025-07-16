import sys
import shutil
import re
import os

def check_disk_and_logs(threshold, log_file, search_pattern):
    total, used, free = shutil.disk_usage("/")  # בודק דיסק root, לשנות אם צריך
    free_percent = free / total * 100

    print(f"Free disk space: {free_percent:.2f}% (Threshold: {threshold}%)")

    if free_percent < threshold:
        print("Not enough disk space, checking logs...")
        if not os.path.exists(log_file):
            print(f"Log file {log_file} does not exist.")
            return 1  # מחזיר כישלון

        with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                if re.search(search_pattern, line):
                    print(f"Pattern '{search_pattern}' found in logs!")
                    return 1  # כישלון
        print("Pattern not found in logs.")
    else:
        print("Enough disk space.")

    return 0  # הצלחה

if __name__ == "__main__":
    # פרמטרים: threshold, log_file, pattern
    if len(sys.argv) != 4:
        print("Usage: python check_disk_and_logs.py <threshold> <log_file> <pattern>")
        sys.exit(1)

    threshold = float(sys.argv[1])
    log_file = sys.argv[2]
    search_pattern = sys.argv[3]

    sys.exit(check_disk_and_logs(threshold, log_file, search_pattern))
