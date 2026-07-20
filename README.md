```markdown
# distro-check 🚀

An ultra-lightweight, zero-dependency enterprise system and hardware compatibility auditor written in pure Python. Designed to run out-of-the-box on clean, minimal Linux/Ubuntu environment clusters to validate system health and security states.

## Key Features

- **Zero External Dependencies:** Built entirely on top of the Python standard library for instant execution without needing package managers (`pip`).
- **Low-Level Direct Parsing:** Directly parses the Linux virtual filesystem (`/proc/meminfo`) to capture memory limits efficiently.
- **Enterprise-Ready Output UI:** Features a dual-mode interface—a highly readable, color-coded terminal UX for engineers, and a strict structured JSON stream mode for orchestration pipelines.
- **Cross-Platform Resilient:** Built-in hardware simulation engine allows flawless execution and testing across both Windows and Linux environments.

---

## Directory Architecture

```text
distro-check/
│
├── requirements.txt  # Manifest for code quality & styling tools
├── run.py            # Primary executable entrypoint
└── src/
    ├── __init__.py   # Component initialization
    ├── auditor.py    # Core system audit logic & virtual file parsing
    └── cli.py        # UX renderer, ANSI color flags, and arguments

```

---

## Installation & Setup

### Cloning the Project

To clone and set up this repository locally, execute the following commands in your terminal:

```bash
# Clone the repository
git clone [https://github.com/Surendra571/distro-check.git](https://github.com/Surendra571/distro-check.git)

# Navigate into the project directory
cd distro-check

```

### Prerequisites

* Python 3.10 or higher.
* A terminal supporting ANSI escape colors.

---

## Running the System Auditor

To execute a human-readable live environment sweep:

```bash
python run.py

```

To stream structured data directly into logging pipelines or automation arrays:

```bash
python run.py --format json

```

---

## Example Outputs

### 1. Standard Human Mode (`python run.py`)

```text
=== UBUNTU SYSTEM COMPATIBILITY REPORT ===

[Memory Check]
  Total Memory:     16.0 GB
  Available Memory: 9.42 GB
  Audit Verdict:    PASS

[Core System Services]
  UFW      -> PASS
  SSH      -> WARN (Inactive)

=========================================

```

### 2. Enterprise Automation Mode (`python run.py --format json`)

```json
{
    "memory": {
        "total_gb": 16.0,
        "available_gb": 9.42,
        "status": "PASS"
    },
    "services": {
        "ufw": "PASS",
        "ssh": "WARN (Inactive)"
    }
}

```

---

## How it Hooks into Linux Internals

1. **Memory Allocation Sweep:** Rather than wrapping high-level system tools, the application hooks directly into `/proc/meminfo`. It tracks `MemTotal` and `MemAvailable`, applying logic bounds to guarantee the environment has adequate compute resources.
2. **Service State Tracking:** The app invokes asynchronous system checks using low-level `subprocess` pipelines to query state responses from the `systemd` manager (`systemctl is-active`).

```

```