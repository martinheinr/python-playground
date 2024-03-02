import sys
import os
#Add comment here
def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    else:
        print("No reboot pendingasdasda")
#Function comment
main()
