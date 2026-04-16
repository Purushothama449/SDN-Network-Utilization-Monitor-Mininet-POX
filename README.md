#  Network Utilization Monitor using Mininet & POX

##  Project Overview

This project implements a **Network Utilization Monitor** using **Software Defined Networking (SDN)** principles. It leverages:

* **Mininet** → Network emulation
* **POX Controller** → Control plane logic
* **OpenFlow Protocol** → Communication between switch & controller

The system continuously monitors network traffic and calculates:

*  Byte count
*  Bandwidth utilization (bits per second)
*  Real-time updates

---

##  Objectives

* Monitor network traffic dynamically
* Collect byte counters from OpenFlow switches
* Estimate bandwidth usage
* Display utilization periodically
* Demonstrate SDN-based monitoring

---

##  Technologies Used

* **Python**
* **Mininet**
* **POX Controller**
* **OpenFlow Protocol**
* **Open vSwitch**

---

##  Project Structure

```
SDN_PROJECT/
│
├── code/
│   ├── monitor.py
│   └── requirements.txt
│
└── screenshot/
    ├── 01_controller_start.png
    ├── 02_mininet_topology.png
    ├── 03_ping_test.png
    ├── 04_iperf_test.png
    ├── 05_bandwidth_output.png
    └── 06_flow_table.png
```

---

##  System Requirements

* Linux (Kali / Ubuntu recommended)
* Python ≥ 3.6
* Mininet
* Open vSwitch
* POX Controller

---

##  Installation & Setup

### 1️ Install Dependencies

```bash
sudo apt update
sudo apt install mininet openvswitch-switch -y
```

---

### 2️ Clone POX Controller

```bash
git clone https://github.com/noxrepo/pox.git
cd pox
```

---

##  How to Run the Project

###  Step 1: Start POX Controller

```bash
cd ~/pox
./pox.py openflow.of_01 forwarding.l2_learning misc.monitor
```

✔ This starts:

* OpenFlow controller
* Learning switch logic
* Network utilization monitor

---

###  Step 2: Start Mininet Topology

Open a new terminal:

```bash
sudo mn --topo single,2 --controller remote,ip=127.0.0.1,port=6633 --mac
```

✔ Creates:

* 2 Hosts → h1, h2
* 1 Switch → s1

---

###  Step 3: Test Connectivity

```bash
pingall
```

✔ Expected Output:

```
0% dropped (2/2 received)
```

---

###  Step 4: Generate Traffic

```bash
iperf h1 h2
```

✔ Generates TCP traffic for bandwidth calculation

---

##  Output Explanation

The controller prints real-time statistics like:

```
Flow (10.0.0.1 → 10.0.0.2) | Bytes=98 | Bandwidth=391.36 bps
```

###  Meaning:

* **Source IP → Destination IP**
* **Bytes** → Total data transferred
* **Bandwidth** → Data rate (bps)

---

##  Screenshots
###  Controller Initialization
![Controller Start](screenshots/01_controller_start.png)

###  Mininet Topology
![Topology](screenshots/02_mininet_topology.png)

###  Ping Test
![Ping](screenshots/03_ping_test.png)

###  Traffic Generation (iperf)
![Iperf](screenshots/04_iperf_test.png)

###  Bandwidth Monitoring Output 
![Bandwidth](screenshots/05_bandwidth_output.png)

###  Flow Table
![Flow Table](screenshots/06_flow_table.png)

---

##  Results

* Successfully established Mininet network
* Verified connectivity using ping
* Generated traffic using iperf
* Monitored real-time bandwidth usage
* Displayed byte counters and flow statistics

---

##  Notes

* POX may show Python version warnings (safe to ignore)
* Always run Mininet with `sudo`
* Ensure Open vSwitch is running
* Use separate terminals for controller and Mininet

---

##  Future Enhancements

* GUI dashboard for visualization
* Store metrics in database
* Alert system for high bandwidth usage
* Support for multi-switch topology

---

##  Author

**Purushothama K C**

---

##  Conclusion

This project demonstrates how **Software Defined Networking (SDN)** can be used to monitor and analyze network traffic efficiently. By combining Mininet and POX, we can simulate real-world networks and implement intelligent monitoring systems.

---
