import json, os, time
import duo_client
from rich.console import Console
from rich.table import Table
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file

load_dotenv()

# Initialize Duo Admin API client

admin_api = duo_client.Admin(
    ikey=os.getenv('DUO_IKEY'),
    skey=os.getenv('DUO_SKEY'),
    host=os.getenv('DUO_HOST')
)

def filter_logs(logs, action=None, app_name=None):

    # If action is None, return all logs

    if action == None:
        return logs

    # Otherwise, filter logs by action and optionally by application name

    if app_name:
        return [log for log in logs if log['action'] == action and log.get('object') == app_name]
    return [log for log in logs if log['action'] == action]


def display_logs(logs):

    # Display logs in a markdown table format using the rich library for a little flair

    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Timestamp", justify="center")
    table.add_column("Admin", justify="center")
    table.add_column("Action", justify="center")
    table.add_column("Object", justify="center")

    for log in logs:
        table.add_row(
            datetime.fromisoformat(log.get('isotimestamp')).strftime('%m-%d-%Y %I:%M:%S %p'),
            log.get('username', 'N/A'),
            log.get('action', 'N/A'),
            log.get('object', 'N/A')
        )

    console.print(table)


def main():
    # Calculate the mintime using Unix timestamp (seconds since epoch) for 90 days ago
    mintime = int(time.time()) - 60 * 60 * 24 * 90

    # Get all administrator logs
    logs = admin_api.get_administrator_log(mintime=mintime)

    # Ask the user to input the action to filter, set a default value of 'integration_policy_assign' and display that in the input prompt
    action = input("Enter action to filter (or \"all\" to show all) [integration_policy_assign]: ") or 'integration_policy_assign'

    # Filter logs by action and optionally by application name
    app_name = input("Enter application name to filter (or blank to show all): ")

    """In this example we are filtering logs for action 'integration_policy_assign' by default.
        You can choose any action you want to filter, or choose one from https://duo.com/docs/adminapi#administrator-logs"""

    # If action is 'all', display all logs
    if action == 'all':
        display_logs(logs)
        return

    # Otherwise, filter logs by action and optionally by application name
    filtered_logs = filter_logs(logs, action, app_name if app_name else None)
    if filtered_logs:
        display_logs(filtered_logs)
    else:
        print(f"No logs found for the applied filters.")


if __name__ == "__main__":
    main()
