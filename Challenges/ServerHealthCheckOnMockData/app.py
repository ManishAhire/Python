# Requirements
#     1. Check server health. For each server, check its CPU, memory, and disk usage.
#     2. Apply thresholds.
#         - CPU usage above 80% → warning
#         - Memory usage above 85% → warning
#         - Disk usage above 90% → critical
#     3. Determine overall status. If any metric is critical, mark the server CRITICAL. Otherwise, if any metric triggers a warning, mark it WARNING. If none trigger, mark it HEALTHY.
#     4. Use functions. Separate the health-checking logic from the reporting logic.
#     5. Generate a report. Print each hostname, its overall status, and the metrics that triggered warnings or critical alerts.
#     6. Save the report. Write the results to server_health_report.json using Python's json module.
#     7. Handle bad data. If a metric is missing or is not a valid number, report the issue instead of crashing. Don't silently treat invalid data as zero.


import json
from pathlib import Path
import validate_server_metrics as valid_metric

#  Mock Data:
servers = [
    {
        "hostname": "web-server-01",
        "cpu_usage": 45,
        "memory_usage": 70,
        "disk_usage": 60
    },
    {
        "hostname": "web-server-02",
        "cpu_usage": 96,
        "memory_usage": 89,
        "disk_usage": 60
    },
    {
        "hostname": "db-server-01",
        "cpu_usage": 92,
        "memory_usage": 88,
        "disk_usage": 95
    },
    {
        "hostname": "db-server-02",
        "cpu_usage": "92",
        "memory_usage": "88",
        "disk_usage": "95"
    },
    {
        "hostname": "web-server-03",
        "cpu_usage": 45,
        "memory_usage": 70
        # disk_usage is missing
    },
    {
        "hostname": "web-server-04",
        "cpu_usage": 105,
        "memory_usage": 70,
        "disk_usage": 60
    }
]


def check_server_health(servers):

    for server in servers:

        is_server_critical = False
        is_server_warning = False

        alerts = []
        errors = []

        try:

            value, error = valid_metric.validate_metric(server, "cpu_usage")
            if value is not None and value > 80:
                is_server_warning = True
                alerts.append("CPU usage is above 80%")
            elif error is not None:
                print(error)
                errors.append(error)

            value, error = valid_metric.validate_metric(server, "memory_usage")
            if value is not None and value > 85:
                is_server_warning = True
                alerts.append("Memory usage is above 85%")
            elif error is not None:
                print(error)
                errors.append(error)

            value, error = valid_metric.validate_metric(server, "disk_usage")
            if value is not None and value > 90:
                is_server_critical = True
                alerts.append("Disk usage is above 90%")
            elif error is not None:
                print(error)
                errors.append(error)

            if is_server_critical:
                server["status"] = "CRITICAL"
            elif is_server_warning:
                server["status"] = "WARNING"
            elif errors:
                server["status"] = "UNKNOWN"
            else:
                server["status"] = "HEALTHY"

            server["alerts"] = alerts
            server["errors"] = errors

        except TypeError:
            print("\nType Error: Metrics should be numeric value.")

        except KeyError:
            print("\nKey Error: Key is not found")

    return servers


def generate_reports(servers):

    try:
        server_report = []
        for server in servers:
            dict_server = {
                "hostname": server["hostname"],
                "status": server["status"],
                "alerts": server["alerts"],
                # returns an empty list if the key doesn't exist.
                "errors": server.get("errors", [])
            }
            server_report.append(dict_server)

        return server_report
    except KeyError:
        print("\nKey Error: Key is not found")


def save_reports_into_json(server_report):
    script_dir = Path(__file__).parent
    file_path = script_dir / "server_health_report.json"

    try:
        with open(file_path, "w") as file:
            json.dump(server_report, file, indent=4)
            print(
                "\nRecords saved successfully, please check the JSON file for more details: ")
    except FileNotFoundError:
        print("\nFile Error: File not found")
        return


servers_with_health_checks = check_server_health(servers)
server_records = generate_reports(servers_with_health_checks)
save_reports_into_json(server_records)
