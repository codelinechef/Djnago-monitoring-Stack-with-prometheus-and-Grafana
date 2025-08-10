import psutil

def get_system_health():
    return{
        "cpu" : psutil.cpu_percent(interval=1),
        "memory" : psutil.virtual_memory().percent,
        "disk" : psutil.disk_usage('/').percent
    }