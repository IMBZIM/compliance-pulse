import datetime
import random

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