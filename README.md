# DevOps Scripts Repository

This repository contains utility scripts and Jenkins pipelines designed for system health checks and automation tasks.

---

## 📂 Repository Structure

```
devops-scripts/
├── jenkins/
│   └── pipelines/
│   |   └── free_space_threshold_jenkinsfile    # Jenkins pipeline for disk-space and log analysis
|   └── jcasc
└── scripts/
    └── python/
        └── check_disk_and_logs.py             # Python script performing the actual check
```

---

## ✅ `check_disk_and_logs.py`

### **Purpose**
Checks disk space and, if below a defined threshold, searches a given log file for a specific pattern.

### **Usage (Standalone)**

```bash
python3 scripts/python/check_disk_and_logs.py <threshold> <log_file> <pattern>
```

**Example:**

```bash
python3 scripts/python/check_disk_and_logs.py 80 /var/log/syslog CoreDump
```

**Exit Codes:**

| Code | Meaning                                      |
|------|---------------------------------------------|
| 0    | Success – either enough space or no pattern found |
| 1    | Failure – pattern found in log file         |

---

## ✅ `free_space_threshold_jenkinsfile`

### **Purpose**
Automates the disk and log check in Jenkins.

### **Jenkins Job Setup**

#### **Option 1 – Recommended (Pipeline from SCM)**
1. In Jenkins, create a **Pipeline** job.
2. **Definition:** `Pipeline script from SCM`.
3. **SCM:** `Git`
   - **Repository URL:** `https://github.com/eamramw/devops-scripts.git`
   - **Branch:** `*/main`
   - **Script Path:** `jenkins/pipelines/free_space_threshold_jenkinsfile`
4. Save & run.

#### **Option 2 – Manual (Any Pipeline Job)**
If not using SCM integration, replace `checkout scm` with:

```groovy
git branch: 'main', url: 'https://github.com/eamramw/devops-scripts.git'
```

---

### **Parameters**

| Name                  | Default            | Description                             |
|----------------------- |--------------------|-----------------------------------------|
| `FREE_SPACE_THRESHOLD` | `70`               | Required free disk space (%)            |
| `LOG_FILE`             | `/var/log/syslog`  | Log file to scan                        |
| `SEARCH_PATTERN`       | `CoreDump`         | Pattern to search in the log            |

### **Behavior**

- ✅ Marks build **SUCCESS** if disk space is OK or pattern not found.
- ❌ Marks build **FAILURE** if disk space < threshold **and** pattern found.

---

## 📌 Notes

- This repo is designed to be extended with more health-check and automation scripts.
- Works best when Jenkins agents run on real hosts (with system logs available).

---

## 👤 Maintainer

- **Author**: Eyal Amram  
- **Contact**: [Your preferred email or GitHub link]
