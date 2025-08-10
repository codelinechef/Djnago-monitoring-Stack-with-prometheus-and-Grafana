from prometheus_client import Gauge
from monitoring.utils.system_monitor import get_system_health

cpu = Gauge('cpu_usgae_percentage', 'CPU Usage %')
mem = Gauge('memory_usgae_percentage', 'Memory Usage %')
disk = Gauge('disk_usage_percentage', 'Disk usage %')

def update_metrics():
    data = get_system_health()
    cpu.set(data["cpu"])
    mem.set(data["memory"])
    disk.set(data["disk"])