import datetime
import random
import pandas as pd

def get_compliance_metrics():
    """Calculates real-time RPO and Downtime metrics."""
    # Simulating 99.9% RPO logic: 
    # Data is 'compliant' if last backup was within 1 hour
    last_backup_mins = random.randint(5, 45)
    rpo_status = "HEALTHY" if last_backup_mins < 60 else "CRITICAL"
    
    # Simulating the 20% reduction in downtime
    # Historical avg: 100 mins -> Current avg: 80 mins
    current_avg_downtime = 80 + random.uniform(-2, 2)
    
    return {
        "rpo_mins": last_backup_mins,
        "rpo_status": rpo_status,
        "avg_downtime": round(current_avg_downtime, 2),
        "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
    }
def get_historical_data():
    """Generates 7 days of downtime data showing a downward trend."""
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    # Simulating a drop from ~100 mins to ~80 mins (20% reduction)
    downtime_values = [105, 102, 98, 90, 85, 82, 81] 
    
    df = pd.DataFrame({
        "Day": days,
        "Downtime (mins)": downtime_values
    })
    return df

def get_server_status():
    """Returns the status of specific company assets."""
    return [
        {"Asset": "Warehouse Hero WMS", "Type": "Application", "Status": "Online", "Health": "98%"},
        {"Asset": "Digital Rift Database", "Type": "Database", "Status": "Online", "Health": "100%"},
        {"Asset": "Digital Rift Main Server", "Type": "Infrastructure", "Status": "Online", "Health": "99.9%"},
        {"Asset": "Area 52", "Type": "Network", "Status": "Online", "Health": "100%"},
    ]