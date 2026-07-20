
from src.auditor import run_full_audit
from src.cli import parse_arguments, display_output

def main():
    # 1. Read flags passed by the engineer in the command line
    args = parse_arguments()
    
    # 2. Execute the low-level Linux kernel checks
    report = run_full_audit()
    
    # 3. Present data in the requested formatting type
    display_output(report, args.format)

if __name__ == "__main__":
    main()