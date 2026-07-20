import subprocess
import sys
from pathlib import Path

def check_memory():
    """Reads /proc/meminfo on Linux, or returns mock data if developing on Windows."""
    # Canonical Dev Tip: Add a fallback for local testing on cross-platform setups
    if sys.platform.startswith("win32"):
        return {
            "total_gb": 16.0,
            "available_gb": 9.42,
            "status": "PASS"
        }

    metrics = {"total_gb": 0.0, "available_gb": 0.0, "status": "FAIL"}
    meminfo_path = Path("/proc/meminfo")
    
    if not meminfo_path.exists():
        return {"error": "Not a Linux system or /proc/meminfo missing"}
        
    try:
        with open(meminfo_path, "r") as f:
            lines = f.readlines()
            
        for line in lines:
            if line.startswith("MemTotal:"):
                kb = int(line.split()[1])
                metrics["total_gb"] = round(kb / (1024 * 1024), 2)
            elif line.startswith("MemAvailable:"):
                kb = int(line.split()[1])
                metrics["available_gb"] = round(kb / (1024 * 1024), 2)
                
        if metrics["total_gb"] >= 2.0:
            metrics["status"] = "PASS"
            
    except Exception as e:
        return {"error": f"Failed to parse memory: {str(e)}"}
        
    return metrics

def check_security_services():
    """Checks systemctl services on Linux, or simulates them on Windows."""
    if sys.platform.startswith("win32"):
        return {
            "ufw": "PASS",
            "ssh": "WARN (Inactive)"
        }

    services = ["ufw", "ssh"]
    results = {}
    
    for service in services:
        try:
            result = subprocess.run(
                ["systemctl", "is-active", service],
                capture_output=True,
                text=True
            )
            is_active = result.stdout.strip() == "active"
            results[service] = "PASS" if is_active else "WARN (Inactive)"
        except FileNotFoundError:
            results[service] = "FAIL (systemd not found)"
            
    return results

def run_full_audit():
    return {
        "memory": check_memory(),
        "services": check_security_services()
    }