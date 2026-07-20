import argparse
import json
import sys

# ANSI Escape Codes for crisp terminal color coding
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_BOLD = "\033[1m"
COLOR_RESET = "\033[0m"

def parse_arguments():
    """Defines and parses professional command line flags."""
    parser = argparse.ArgumentParser(
        description="distro-check: An enterprise system and hardware compatibility auditor."
    )
    
    parser.add_argument(
        "-f", "--format",
        choices=["text", "json"],
        default="text",
        help="Output format style (default: text)"
    )
    
    return parser.parse_args()

def render_text_ui(report):
    """Renders a clean, beautifully formatted human-readable terminal UX."""
    # Force Windows Command Prompt to handle ANSI escape color codes correctly
    import os; os.system('') 
    
    print(f"{COLOR_BOLD}=== UBUNTU SYSTEM COMPATIBILITY REPORT ==={COLOR_RESET}\n")
    # ... (keep the rest of the code inside this function exactly the same)
    
    # 1. Render Memory Audit
    mem = report.get("memory", {})
    if "error" in mem:
        print(f"[-] Memory Status: {COLOR_RED}ERROR{COLOR_RESET} ({mem['error']})")
    else:
        status_color = COLOR_GREEN if mem["status"] == "PASS" else COLOR_RED
        print(f"[{COLOR_BOLD}Memory Check{COLOR_RESET}]")
        print(f"  Total Memory:     {mem['total_gb']} GB")
        print(f"  Available Memory: {mem['available_gb']} GB")
        print(f"  Audit Verdict:    {status_color}{mem['status']}{COLOR_RESET}\n")
        
    # 2. Render Security Services Audit
    services = report.get("services", {})
    print(f"[{COLOR_BOLD}Core System Services{COLOR_RESET}]")
    for service, status in services.items():
        if "PASS" in status:
            color = COLOR_GREEN
        elif "WARN" in status:
            color = COLOR_YELLOW
        else:
            color = COLOR_RED
            
        # Left-align service names to make the terminal look like a professional dashboard
        print(f"  {service.upper().ljust(8)} -> {color}{status}{COLOR_RESET}")
        
    print(f"\n{COLOR_BOLD}========================================={COLOR_RESET}")

def display_output(report, output_format):
    """Routes the final audit report to the chosen UI format."""
    if output_format == "json":
        # Stream strict JSON directly to standard output for automation scripting
        print(json.dumps(report, indent=4))
    else:
        render_text_ui(report)