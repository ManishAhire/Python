
import math


def validate_metric(server, metric_name):
    if metric_name not in server:
        return None, f"{metric_name} is missing"

    value = server[metric_name]

    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None, f"{metric_name} must be numeric"

    if not math.isfinite(value):
        return None, f"{metric_name} must be finite"

    if not 0 <= value <= 100:
        return None, f"{metric_name} must be between 0 and 100"

    return value, None
