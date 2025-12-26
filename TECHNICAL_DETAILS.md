Technical Documentation: RPO & Reliability Logic

1. The RPO Calculation Engine
The Recovery Point Objective (RPO) measures the maximum tolerable period in which data might be lost due to an incident. In CompliancePulse, the RPO is calculated using a delta-time verification algorithm.


Formula: The scriptcalculates the Data Gap as (G):
G=T(current) - T(last_Sync)

Compliance Logic
-Threshold:SLA - 60mins
-status calculation:
  if G< SLA: status is Heathy(Green)
  if G> SLA: status is Critical(red)

To maintain a 99.9% RPO over a monthly cycle, the system ensures that the cumulative "Critical" time does not exceed 43 minutes per month.

2. Downtime Reduction Methodology
The 20% reduction in downtime is achieved through Proactive Health Probes. Instead of waiting for a system to crash (Reactive), the Python engine runs heartbeat checks every 60 seconds.

The 20% Math:
-Pre-Automation Baseline: Avarage downtime of 105 mins/week
-Post-Automation Performance: Avarage downtime of 81 minuets/week.
Imporment 

105-81/105 * 100 = 22.8%  improvement

3. Monitoring Architecture
The system utilizes a modular "Probe-and-Report" architecture:

Engine Layer (engine.py): Executes sub-processes to ping system endpoints (e.g., Warehouse Hero WMS) and query database timestamps (e.g., Pomona DB).

Validation Layer: Compares real-time data against predefined JSON schemas for integrity.

Visualization Layer (app.py): Uses Streamlit and Plotly to render the pandas DataFrames into scannable metrics for stakeholders.

4. Asset Schema
Each asset in the Digital Rift Tech ecosystem is tracked via a dictionary-based registry, allowing for $O(1)$ lookup times when checking status:Python{
    "Asset": "Warehouse Hero WMS",
    "Type": "Application",
    "Metric": "Heartbeat_Ping",
    "Expected_Response": 200
}


