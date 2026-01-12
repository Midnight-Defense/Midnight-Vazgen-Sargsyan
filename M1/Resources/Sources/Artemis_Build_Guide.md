# Artemis Long-Range UAV Build Guide

> **Project:** Artemis-Class Long-Range Fixed-Wing UAV  
> **Version:** 1.0  
> **Date:** January 11, 2026  
> **Budget:** ~$16,170  
> **Estimated Build Time:** 40-60 hours

---

## 📋 Table of Contents

1. [Build Overview](#1-build-overview)
2. [Complete Parts List](#2-complete-parts-list)
3. [Required Tools & Equipment](#3-required-tools--equipment)
4. [Phase 1: Airframe Assembly](#4-phase-1-airframe-assembly)
5. [Phase 2: Power System Installation](#5-phase-2-power-system-installation)
6. [Phase 3: Propulsion System](#6-phase-3-propulsion-system)
7. [Phase 4: Avionics Installation](#7-phase-4-avionics-installation)
8. [Phase 5: Navigation & GPS](#8-phase-5-navigation--gps)
9. [Phase 6: Sensor Integration](#9-phase-6-sensor-integration)
10. [Phase 7: Communications Setup](#10-phase-7-communications-setup)
11. [Phase 8: AI Computer Integration](#11-phase-8-ai-computer-integration)
12. [Phase 9: Wiring & Connections](#12-phase-9-wiring--connections)
13. [Phase 10: Software Configuration](#13-phase-10-software-configuration)
14. [Phase 11: Testing & Calibration](#14-phase-11-testing--calibration)
15. [Phase 12: First Flight Procedures](#15-phase-12-first-flight-procedures)
16. [Troubleshooting Guide](#16-troubleshooting-guide)
17. [Maintenance Schedule](#17-maintenance-schedule)

---

## 1. Build Overview

### 1.1 Project Summary

This build guide covers the complete assembly of an **Artemis-class long-range autonomous UAV** based on the Mugin 3220mm V-Tail platform. The system features:

- **3.2 meter wingspan** composite airframe
- **AI-powered navigation** with NVIDIA Jetson Orin NX
- **Dual-redundant GPS** with RTK capability
- **Thermal + visual camera** payload
- **20+ km HD video datalink**
- **44 Ah battery capacity** (~2 kWh)
- **Estimated 3-4 hour endurance**

### 1.2 Skill Level Required

| Skill | Level Required |
|-------|----------------|
| RC aircraft building | Intermediate-Advanced |
| Soldering | Intermediate |
| Linux/command line | Basic-Intermediate |
| Electronics | Intermediate |
| Composite materials | Basic |

### 1.3 Build Cost Summary

| Category | Selected Components | Subtotal |
|----------|-------------------|----------|
| **Motor** | T-Motor U13II KV130 | $500 |
| **ESC** | APD 120F3 HV | $220 |
| **Propeller** | T-Motor NS26×8.5 CF | $150 |
| **Flight Controller** | Holybro Pixhawk 6X Pro Set | $500 |
| **AI Computer** | NVIDIA Jetson Orin NX 16GB Dev Kit | $900 |
| **GPS** | CubePilot HerePro + Here3+ backup | $550 |
| **Cameras** | Arducam IMX477 + AR0234 + OV9281 | $250 |
| **Thermal** | FLIR Boson 320 | $2,500 |
| **Altimeter** | Ainstein US-D1 + SF11/C | $600 |
| **Datalink** | Herelink 1.1 + RFD900x | $1,400 |
| **Battery** | 2× Tattu Pro 12S 22000mAh | $2,600 |
| **Power System** | PM02D + BECs + Charger | $600 |
| **Airframe** | Mugin 3220mm V-Tail Composite | $3,600 |
| **Servos** | 4× Hitec D-980TW | $800 |
| **Misc** | Wiring, connectors, mounts, hardware | $1,000 |
| **Software** | PX4 + QGC + JetPack (FREE) | $0 |
| **TOTAL** | | **~$16,170** |

---

## 2. Complete Parts List

### 2.1 Airframe Components

| Item | Model | Quantity | Source | Price |
|------|-------|----------|--------|-------|
| Airframe Kit | Mugin 3220mm V-Tail | 1 | MuginUAV | $3,200 |
| Landing Gear | Included with kit | 1 set | - | Incl. |
| Fuel Tank/Battery Bay | Included with kit | 1 | - | Incl. |
| Wing Joiner Tubes | Aluminum/CF | 2 | Kit | Incl. |
| Fuselage Hatches | Included | 2-3 | Kit | Incl. |

### 2.2 Propulsion Components

| Item | Model | Quantity | Source | Price |
|------|-------|----------|--------|-------|
| Motor | T-Motor U13II KV130 | 1 | T-Motor Store | $500 |
| ESC | APD 120F3[X] HV | 1 | PowerDrives | $220 |
| Propeller | T-Motor NS26×8.5 CF | 2 | T-Motor Store | $150 |
| Prop Adapter | 15mm shaft adapter | 1 | T-Motor | $25 |
| Spinner | 76mm CF spinner | 1 | T-Motor | $40 |
| Motor Mount | CNC aluminum | 1 | Custom/Kit | $50 |

### 2.3 Avionics Components

| Item | Model | Quantity | Source | Price |
|------|-------|----------|--------|-------|
| Flight Controller | Holybro Pixhawk 6X Pro Set | 1 | Holybro | $500 |
| Baseboard | Standard Baseboard V2 | 1 | Included | Incl. |
| Power Module | PM02D HV | 1 | Included | Incl. |
| GPS Cable | 6-pin JST-GH | 2 | Included | Incl. |
| I2C Splitter | 4-port | 1 | Holybro | $15 |
| Safety Switch | With LED | 1 | Included | Incl. |

### 2.4 AI & Computing

| Item | Model | Quantity | Source | Price |
|------|-------|----------|--------|-------|
| AI Computer | NVIDIA Jetson Orin NX 16GB Dev Kit | 1 | NVIDIA | $900 |
| NVMe SSD | Samsung 970 EVO Plus 256GB | 1 | Samsung | $50 |
| Carrier Board | Included with Dev Kit | 1 | - | Incl. |
| Heatsink/Fan | Active cooling | 1 | Included | Incl. |
| WiFi Antennas | 2.4/5GHz | 2 | Included | Incl. |

### 2.5 Navigation & GPS

| Item | Model | Quantity | Source | Price |
|------|-------|----------|--------|-------|
| Primary GPS | CubePilot HerePro | 1 | CubePilot | $400 |
| Backup GPS | CubePilot Here3+ | 1 | CubePilot | $150 |
| GPS Mast | Carbon fiber 150mm | 2 | Generic | $30 |
| Compass | External RM3100 | 1 | Inc. w/ Here3+ | Incl. |

### 2.6 Sensors & Cameras

| Item | Model | Quantity | Source | Price |
|------|-------|----------|--------|-------|
| Main Camera | Arducam IMX477 12MP | 1 | Arducam | $100 |
| Global Shutter | Arducam AR0234 2MP | 1 | Arducam | $120 |
| Downward Camera | Arducam OV9281 1MP | 1 | Arducam | $50 |
| Thermal Camera | FLIR Boson 320 | 1 | FLIR | $2,500 |
| Radar Altimeter | Ainstein US-D1 | 1 | Ainstein | $400 |
| LiDAR Altimeter | Lightware SF11/C | 1 | Lightware | $300 |
| Airspeed Sensor | Holybro Digital Airspeed | 1 | Holybro | $60 |
| Pitot Tube | Heated stainless | 1 | Holybro | $50 |

### 2.7 Communications

| Item | Model | Quantity | Source | Price |
|------|-------|----------|--------|-------|
| HD Video Link | CubePilot Herelink 1.1 | 1 | CubePilot | $1,100 |
| Telemetry Radio | RFD900x | 1 set | RFDesign | $300 |
| Air Unit Antennas | 2.4GHz omni | 2 | Included | Incl. |
| HDMI Cable | Mini HDMI 30cm | 2 | Generic | $15 |

### 2.8 Power System

| Item | Model | Quantity | Source | Price |
|------|-------|----------|--------|-------|
| Battery | Tattu Pro 12S 22000mAh 25C | 2 | Tattu | $2,600 |
| Power Module | PM02D HV | 1 | Holybro | $60 |
| BEC 12V | Pololu D36V50F12 | 1 | Pololu | $45 |
| BEC 5V | Holybro PM08-BEC | 2 | Holybro | $50 |
| Battery Charger | Tattu TA1200 | 1 | Tattu | $450 |
| XT90 Connectors | Anti-spark | 4 pairs | Generic | $25 |
| Power Distribution | Matek FCHUB-12S | 1 | Matek | $45 |

### 2.9 Servos & Actuation

| Item | Model | Quantity | Source | Price |
|------|-------|----------|--------|-------|
| Servos | Hitec D-980TW | 4 | Hitec | $800 |
| Servo Arms | Aluminum 25T | 4 | Hitec | $30 |
| Servo Extensions | 30cm | 4 | Generic | $15 |
| Control Horns | Nylon/Aluminum | 8 | Generic | $10 |
| Push Rods | 3mm threaded | 4 | Generic | $15 |

### 2.10 Miscellaneous Hardware

| Item | Description | Quantity | Price |
|------|-------------|----------|-------|
| Wire | 10-16 AWG silicone | 10m | $40 |
| Wire | 18-22 AWG signal | 20m | $25 |
| Connectors | JST-GH, Molex, XT60 | Assorted | $80 |
| Heat Shrink | Assorted sizes | 1 kit | $20 |
| Velcro Straps | Heavy-duty | 10 | $15 |
| Zip Ties | Assorted | 100 | $10 |
| Mounting Tape | 3M VHB | 1 roll | $20 |
| Thread Lock | Blue Loctite | 1 | $8 |
| Epoxy | 30-min | 2 tubes | $25 |
| CA Glue | Thin + Thick | 2 | $15 |
| Foam | Vibration damping | 1 sheet | $15 |
| Screws | M3/M4 assorted | 1 kit | $25 |

---

## 3. Required Tools & Equipment

### 3.1 Essential Tools

| Tool | Purpose |
|------|---------|
| Soldering Station | 60W+ adjustable temperature |
| Multimeter | Voltage, current, continuity |
| Hex Driver Set | 1.5mm - 5mm |
| Phillips Screwdrivers | #0, #1, #2 |
| Wire Strippers | 10-22 AWG |
| Wire Crimpers | JST, Molex terminals |
| Heat Gun | Heat shrink, CA acceleration |
| Hobby Knife | X-Acto or similar |
| Ruler/Calipers | Metric measurements |
| Level | For CG and motor alignment |
| Scale | 0-50kg digital |

### 3.2 Recommended Tools

| Tool | Purpose |
|------|---------|
| Oscilloscope | Signal debugging |
| USB-TTL Adapter | Serial debugging |
| LiPo Voltage Checker | Battery monitoring |
| Servo Tester | Servo testing |
| Thrust Stand | Motor testing |
| 3D Printer | Custom mounts |

### 3.3 Software Requirements

| Software | Purpose | Download |
|----------|---------|----------|
| QGroundControl | Mission planning, configuration | qgroundcontrol.com |
| PX4 Firmware | Flight controller firmware | px4.io |
| NVIDIA JetPack | Orin NX OS and tools | developer.nvidia.com |
| Balena Etcher | SD card flashing | balena.io |
| VS Code | Code editing | code.visualstudio.com |
| PuTTY/SSH | Remote access | putty.org |

---

## 4. Phase 1: Airframe Assembly

### 4.1 Unpack and Inventory (1-2 hours)

**Steps:**

1. **Carefully unpack** all airframe components
2. **Inventory check** - verify all parts against packing list
3. **Inspect for damage** - check for cracks, dents, or shipping damage
4. **Organize parts** by section (fuselage, wings, tail)

**Checklist:**
- [ ] Fuselage complete
- [ ] Left wing panel
- [ ] Right wing panel
- [ ] V-tail surfaces (2)
- [ ] Wing joiner tubes
- [ ] Landing gear assembly
- [ ] Hardware kit
- [ ] Wing mounting hardware

### 4.2 Fuselage Preparation (2-3 hours)

**Steps:**

1. **Clean fuselage interior** with isopropyl alcohol
2. **Mark component locations** with masking tape
   - Battery bay (forward CG)
   - Avionics bay (center)
   - Motor mount (rear)
3. **Install equipment rails** if not pre-installed
4. **Reinforce high-stress areas** with epoxy/fiberglass

**Component Bay Layout:**
```
NOSE ←────────────────────────────────────────────── TAIL
┌─────────────────────────────────────────────────────────┐
│ CAMERA │ AVIONICS │  BATTERIES   │ MOTOR │ PROP │
│   BAY  │   BAY    │     BAY      │ MOUNT │      │
│ 150mm  │  350mm   │    450mm     │ 150mm │      │
└─────────────────────────────────────────────────────────┘
```

### 4.3 Wing Assembly (3-4 hours)

**Steps:**

1. **Dry-fit wing joiner** tubes into fuselage
2. **Align wing panels** and check for twist
3. **Install wing joiner** with epoxy (if permanent) or bolts (if removable)
4. **Install servo hatches** and covers
5. **Route servo wiring** through wings
6. **Install wing servos**
   - Ailerons: 2× Hitec D-980TW
7. **Set servo horns** to neutral (90°)

**Servo Installation:**

```
Wing Root ←─────────────────────────── Wing Tip
┌────────────────────────────────────────────────┐
│    SERVO      │                    │           │
│   [D-980TW]   │     AILERON        │  WINGTIP  │
│    (25T arm)  │                    │           │
└────────────────────────────────────────────────┘
     ↓ Wire routing through wing spar
```

### 4.4 V-Tail Assembly (1-2 hours)

**Steps:**

1. **Locate V-tail mounting points** on fuselage
2. **Install V-tail actuator servos** (2× Hitec D-980TW)
3. **Mount V-tail surfaces** with bolts
4. **Connect control linkages**
5. **Check for free movement** (no binding)

**V-Tail Mixing:**
- PX4 will handle V-tail mixing in software
- Both surfaces move together = Elevator
- Surfaces move opposite = Rudder

### 4.5 Landing Gear Installation (1 hour)

**Steps:**

1. **Install main landing gear** mounting plates
2. **Attach gear legs** with bolts
3. **Install wheels** with wheel collars
4. **Check for alignment** - aircraft should track straight
5. **Adjust suspension** if equipped

### 4.6 Motor Mount Installation (1 hour)

**Steps:**

1. **Locate motor mount** on rear fuselage
2. **Check thrust line alignment** with inclinometer
3. **Install motor mount** with bolts and thread lock
4. **Verify clearance** for propeller arc

---

## 5. Phase 2: Power System Installation

### 5.1 Battery Bay Setup (2 hours)

**Steps:**

1. **Line battery bay** with foam padding (vibration isolation)
2. **Install battery mounting rails** or straps
3. **Route battery lead** wires forward to power distribution
4. **Install XT90 anti-spark** connectors

**Battery Placement:**
```
┌─────────────────────────────────────────┐
│      BATTERY 1         BATTERY 2        │
│   [Tattu 12S 22Ah]  [Tattu 12S 22Ah]   │
│      ~~~~~~~~          ~~~~~~~~         │
│        ↓                  ↓             │
│   XT90 ──────┬──────── XT90            │
│              │                          │
│         PARALLEL                        │
│         HARNESS                         │
│              ↓                          │
│         MAIN XT90                       │
│              ↓                          │
│         TO PDB                          │
└─────────────────────────────────────────┘
```

### 5.2 Power Distribution Board (1 hour)

**Steps:**

1. **Mount PDB** (Matek FCHUB-12S) in avionics bay
2. **Connect main battery input** via XT90
3. **Solder ESC power leads** to PDB (12AWG)
4. **Install current sensor** bypass if using PM02D

**PDB Wiring Diagram:**
```
BATTERY (+) ─────┬───────── ESC (+)
                 │
                 ├───────── PM02D (+)
                 │
                 └───────── PDB Vbat

BATTERY (-) ─────┬───────── ESC (-)
                 │
                 ├───────── PM02D (-)
                 │
                 └───────── PDB GND
```

### 5.3 BEC Installation (1 hour)

**Steps:**

1. **Install 12V BEC** (Pololu D36V50F12)
   - Input: 48V from PDB
   - Output: 12V for Jetson, cameras
2. **Install 5V BEC #1** (Holybro PM08-BEC)
   - Input: 12V
   - Output: 5V for servos, peripherals
3. **Install 5V BEC #2** (backup)
   - Redundant avionics power
4. **Mount with thermal pads** for heat dissipation

**Power Voltage Rails:**
```
48V (Battery) ──┬──────────→ ESC
                │
                ├──→ [12V BEC] ──┬──→ Jetson Orin (12V)
                │                 │
                │                 ├──→ Herelink Air (12V)
                │                 │
                │                 ├──→ [5V BEC] ──→ Servos
                │                 │
                │                 └──→ [5V BEC] ──→ Peripherals
                │
                └──→ [PM02D] ──→ Pixhawk 6X (5V)
```

### 5.4 Voltage/Current Monitoring (30 min)

**Steps:**

1. **Connect PM02D** power module inline
2. **Wire to Pixhawk** POWER1 port
3. **Verify ADC readings** in QGroundControl

---

## 6. Phase 3: Propulsion System

### 6.1 Motor Installation (1 hour)

**Steps:**

1. **Prepare motor mount** - clean and degrease
2. **Apply thread lock** to mounting bolts
3. **Mount T-Motor U13II** to motor mount
   - 4× M4 bolts (included with motor)
4. **Check motor rotation** - should spin freely
5. **Install motor wires** through fuselage

**Motor Orientation:**
```
       ┌─────────┐
       │  MOTOR  │
       │ U13II   │ ← Cable exit toward avionics bay
       └────┬────┘
            │
       ┌────┴────┐
       │  MOUNT  │
       └─────────┘
            ↓
       PROPELLER (pusher)
```

### 6.2 ESC Installation (1 hour)

**Steps:**

1. **Mount APD 120F3 ESC** in ventilated location
   - Ideally near motor to shorten phase wires
2. **Connect motor phases** (any order initially)
3. **Connect power leads** to PDB (12AWG min)
4. **Connect signal wire** to Pixhawk MAIN OUT 5 (throttle channel)

**ESC Connections:**
```
MOTOR ←───── 3× Phase wires (U, V, W)

BATTERY ←── (+) Red 12AWG
            (-) Black 12AWG

PIXHAWK ←── Signal wire (3-pin)
            - Signal (Orange)
            - Ground (Brown)
            - NC (Red - not connected)

TELEMETRY ←─ (Optional) for RPM/current
```

### 6.3 Propeller Installation (30 min)

**Steps:**

1. **Install prop adapter** on motor shaft
2. **Balance propeller** using magnetic balancer
3. **Mount propeller** - verify pusher rotation
4. **Install spinner** and tighten
5. **Check tip clearance** - min 25mm from fuselage

**CRITICAL: Verify rotation direction before first power-up!**

### 6.4 Motor Direction Test

**Before connecting propeller:**

1. Connect battery
2. Arm via QGroundControl
3. Give minimal throttle
4. Verify motor spins CLOCKWISE (when viewed from rear)
5. If wrong, swap any 2 motor phase wires

---

## 7. Phase 4: Avionics Installation

### 7.1 Pixhawk 6X Mounting (1 hour)

**Steps:**

1. **Apply vibration damping** foam to mounting location
2. **Orient Pixhawk** with arrow pointing forward
3. **Secure with Velcro** or mounting plate
4. **Verify level** with bubble level

**Mounting Location:**
```
┌─────────────────────────────────────────┐
│                 FUSELAGE                │
│                                         │
│      ┌─────────────────┐               │
│      │   PIXHAWK 6X    │ ← Center of   │
│      │   ↑ FORWARD ↑   │   aircraft    │
│      └─────────────────┘               │
│                                         │
└─────────────────────────────────────────┘
```

**Orientation Requirements:**
- Arrow pointing toward nose
- Level with aircraft
- Away from motors, ESCs, power wires
- Vibration isolated

### 7.2 Baseboard Connections (2 hours)

**Port Assignments:**

| Port | Connection | Cable |
|------|------------|-------|
| POWER1 | PM02D Power Module | 6-pin DF13 |
| POWER2 | Backup power (optional) | 6-pin DF13 |
| GPS1 | HerePro GPS | 6-pin JST-GH |
| GPS2 | Here3+ GPS | 6-pin JST-GH |
| TELEM1 | Herelink Air Unit | 6-pin JST-GH |
| TELEM2 | RFD900x Telemetry | 6-pin JST-GH |
| I2C | Airspeed sensor | 4-pin JST-GH |
| CAN1 | HerePro (CAN) | 4-pin JST-GH |
| CAN2 | Here3+ (CAN) | 4-pin JST-GH |
| USB | Config/Debug | Type-C |
| ETHERNET | Jetson Orin | RJ45 |

### 7.3 PWM Output Configuration

**MAIN OUT Assignments (FMU):**

| Channel | Function | Device |
|---------|----------|--------|
| MAIN 1 | Aileron L | Servo D-980TW |
| MAIN 2 | Aileron R | Servo D-980TW |
| MAIN 3 | V-Tail L (Elevator+Rudder) | Servo D-980TW |
| MAIN 4 | V-Tail R (Elevator+Rudder) | Servo D-980TW |
| MAIN 5 | Throttle (Motor) | APD 120F3 ESC |
| MAIN 6 | (spare) | - |
| MAIN 7 | (spare) | - |
| MAIN 8 | (spare) | - |

### 7.4 Safety Switch Installation

1. **Mount safety switch** in accessible location
2. **Connect to SWITCH** port on baseboard
3. **Test LED functions:**
   - Blinking = disarmed, ready to arm
   - Solid = armed

---

## 8. Phase 5: Navigation & GPS

### 8.1 Primary GPS (HerePro) Installation (1 hour)

**Steps:**

1. **Mount GPS mast** on fuselage top
2. **Install HerePro** on mast (minimum 150mm above fuselage)
3. **Route CAN cable** to Pixhawk CAN1
4. **Orient arrow** pointing forward
5. **Secure cable** to prevent vibration

**GPS Mounting:**
```
          ┌─────┐
          │GPS  │ ← Min 150mm above fuselage
          │MAST │
     ─────┴─────┴─────
          FUSELAGE
```

### 8.2 Backup GPS (Here3+) Installation (30 min)

**Steps:**

1. **Mount Here3+** at least 100mm from HerePro
2. **Route CAN cable** to Pixhawk CAN2
3. **Configure as secondary** GPS in parameters

**Separation Requirement:**
- Minimum 100mm between GPS antennas
- Prevents interference

### 8.3 Compass Calibration

**Calibration Steps:**

1. Take aircraft outdoors, away from metal structures
2. Open QGroundControl → Vehicle Setup → Sensors
3. Click "Compass" → Start
4. Rotate aircraft through all orientations
5. Repeat for each compass (HerePro, Here3+, internal)
6. Verify calibration quality (green = good)

---

## 9. Phase 6: Sensor Integration

### 9.1 Airspeed Sensor (30 min)

**Steps:**

1. **Mount pitot tube** on wing leading edge
2. **Connect tubing** to Holybro Digital Airspeed sensor
3. **Wire sensor** to Pixhawk I2C port
4. **Zero calibration** - cover pitot opening, calibrate in QGC

**Pitot Placement:**
```
    PITOT TUBE
        │
        ▼
  ──────┼──────────────────────
        │           WING
  ──────┴──────────────────────
  
  ← Place 200mm from fuselage, on wing LE
```

### 9.2 Altimeter Sensors (1 hour)

**Ainstein US-D1 Radar:**

1. Mount facing downward on fuselage bottom
2. Clear of obstructions (landing gear, etc.)
3. Wire to Pixhawk SERIAL4 or I2C
4. Configure RNGFND parameters in PX4

**Lightware SF11/C LiDAR:**

1. Mount facing downward, 100mm from radar
2. Wire to Pixhawk I2C (different address)
3. Configure as secondary rangefinder

### 9.3 Camera Mounts (1 hour)

**Main Camera (IMX477):**
- Mount in nose section
- Forward-facing for navigation/targeting
- Connect to Jetson CSI port

**Downward Camera (OV9281):**
- Mount in fuselage bottom
- Downward-facing for terrain matching
- Connect to Jetson secondary CSI

**Thermal Camera (FLIR Boson):**
- Mount adjacent to main camera
- Connect to Jetson via USB

---

## 10. Phase 7: Communications Setup

### 10.1 Herelink Air Unit (1 hour)

**Steps:**

1. **Mount air unit** in avionics bay
   - Good ventilation required
   - Keep antennas clear of carbon fiber
2. **Connect HDMI #1** to Jetson HDMI out
3. **Connect HDMI #2** (optional second camera)
4. **Connect telemetry** to Pixhawk TELEM1
5. **Connect power** (12V from BEC)
6. **Mount antennas** on fuselage sides

**Antenna Placement:**
```
        ┌─────────┐
ANT 1 ──│ FUSELAGE│── ANT 2
(side)  │         │  (side)
        └─────────┘
        
Antennas should be 90° apart for diversity
```

### 10.2 RFD900x Telemetry (30 min)

**Steps:**

1. **Mount RFD900x** air module
2. **Connect to Pixhawk** TELEM2
3. **Connect antenna** (900MHz)
4. **Configure baud rate** (57600 default)
5. **Pair with ground module**

### 10.3 Herelink Pairing

1. Power on Herelink controller
2. Power on air unit
3. Navigate to Settings → Pairing
4. Follow on-screen instructions
5. Verify video link active

---

## 11. Phase 8: AI Computer Integration

### 11.1 Jetson Orin NX Physical Install (1 hour)

**Steps:**

1. **Flash JetPack 6.0** to NVMe SSD
2. **Mount Jetson** in avionics bay
   - Ensure good airflow to heatsink
3. **Connect power** (12V, 3A minimum)
4. **Connect Ethernet** to Pixhawk
5. **Connect cameras** to CSI ports

**Jetson Connections:**
```
┌─────────────────────────────────────────────┐
│                JETSON ORIN NX               │
├─────────────────────────────────────────────┤
│ DC POWER (12V) ←---- From 12V BEC           │
│ ETHERNET ←---------- To Pixhawk 6X          │
│ CSI-0 ←------------- IMX477 Main Camera     │
│ CSI-1 ←------------- OV9281 Downward        │
│ USB 3.0 ←----------- FLIR Boson 320         │
│ HDMI ←-------------- To Herelink Air        │
│ USB 2.0 ←----------- (spare)                │
└─────────────────────────────────────────────┘
```

### 11.2 JetPack Installation

**Steps:**

1. Download JetPack 6.0 from NVIDIA
2. Use SDK Manager or manual flash
3. Boot and complete initial setup
4. Install required packages:

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y python3-pip python3-opencv
sudo apt install -y ros-humble-desktop  # If using ROS 2

# Install NVIDIA tools
sudo apt install -y nvidia-jetpack

# Install MAVROS for PX4 communication
sudo apt install -y ros-humble-mavros ros-humble-mavros-extras
```

### 11.3 Camera Configuration

**IMX477 Setup:**

```bash
# Test camera
nvgstcapture-1.0 --sensor-id=0

# Check V4L2 devices
v4l2-ctl --list-devices
```

**FLIR Boson Setup:**

```bash
# Install FLIR SDK
# Download from FLIR website

# Test thermal camera
python3 -c "import cv2; print(cv2.VideoCapture(1).isOpened())"
```

### 11.4 MAVLink Communication

**Configure Jetson-to-Pixhawk:**

```bash
# Edit MAVROS config
sudo nano /opt/ros/humble/share/mavros/launch/px4.launch

# Set connection
fcu_url: "udp://:14540@:14557"

# Or for Ethernet
fcu_url: "tcp://192.168.1.1:5760"
```

---

## 12. Phase 9: Wiring & Connections

### 12.1 Wire Routing Principles

**DO:**
- Keep power and signal wires separated
- Twist power wire pairs (reduces EMI)
- Use shielded cable for sensors
- Secure all wires with zip ties
- Leave service loops at connectors

**DON'T:**
- Route wires near motor/ESC
- Allow wires near propeller arc
- Create tight bend radii
- Leave loose wires in airstream

### 12.2 Complete Wiring Diagram

```
                    ARTEMIS WIRING DIAGRAM
                    ═══════════════════════

BATTERY (48V)
    │
    ├───────[ANTI-SPARK XT90]───────────────────────────────┐
    │                                                        │
    ▼                                                        ▼
┌───────┐                                              ┌───────────┐
│  PDB  │──────────[12AWG]──────────────────────────►│   ESC     │
│       │                                              │ APD 120F3 │
│       │◄─────────[12AWG]─────────────────────────────│           │
└───┬───┘                                              └─────┬─────┘
    │                                                        │
    │ ┌────────────────────────────────────────────────┐     │
    │ │                                                │     │
    ▼ ▼                                                │     ▼
┌───────┐     ┌───────────┐                            │ ┌───────┐
│ PM02D │────►│ PIXHAWK   │◄───[PWM CH5]───────────────┘ │ MOTOR │
│       │     │    6X     │                              │ U13II │
└───────┘     │           │                              └───────┘
              │  TELEM1   │◄──────[HERELINK AIR]
              │  TELEM2   │◄──────[RFD900x]
              │  GPS1/CAN1│◄──────[HEREPRO]
              │  GPS2/CAN2│◄──────[HERE3+]
              │  I2C      │◄──────[AIRSPEED]
              │  SERIAL4  │◄──────[US-D1 RADAR]
              │  ETHERNET │◄──────[JETSON ORIN]
              │  MAIN 1-4 │◄──────[SERVOS ×4]
              └───────────┘

12V RAIL (from PDB via 12V BEC)
    │
    ├───────► JETSON ORIN NX (12V, 3A)
    │
    ├───────► HERELINK AIR (12V)
    │
    └───────► [5V BEC]────► SERVOS (5V)
                    │
                    └────► PERIPHERALS (5V)
```

### 12.3 Connector Pinouts

**Pixhawk TELEM1 (to Herelink):**
```
Pin 1: VCC (5V)
Pin 2: TX
Pin 3: RX
Pin 4: CTS
Pin 5: RTS
Pin 6: GND
```

**Pixhawk GPS/CAN:**
```
Pin 1: VCC (5V)
Pin 2: TX/CAN_H
Pin 3: RX/CAN_L
Pin 4: SCL
Pin 5: SDA
Pin 6: GND
```

---

## 13. Phase 10: Software Configuration

### 13.1 PX4 Firmware Installation

**Steps:**

1. Connect Pixhawk via USB
2. Open QGroundControl
3. Go to Vehicle Setup → Firmware
4. Select PX4 Flight Stack
5. Click "OK" to flash latest stable

### 13.2 Airframe Configuration

**Steps:**

1. Vehicle Setup → Airframe
2. Select: **Flying Wing** → **Generic Flying Wing**
3. Or custom: **V-Tail** configuration
4. Apply and restart

### 13.3 Key Parameters

**Set the following parameters in QGC:**

```
# Airframe
SYS_AUTOSTART = 2100  (Flying Wing)

# V-Tail Mixing
VT_TYPE = 1  # V-Tail

# PWM Outputs
PWM_MAIN_FUNC1 = 201  # Aileron Left
PWM_MAIN_FUNC2 = 202  # Aileron Right
PWM_MAIN_FUNC3 = 203  # V-Tail Left
PWM_MAIN_FUNC4 = 204  # V-Tail Right
PWM_MAIN_FUNC5 = 101  # Throttle

# Battery
BAT1_N_CELLS = 12
BAT1_CAPACITY = 44000  # 2× 22Ah
BAT1_V_CHARGED = 50.4  # 12S fully charged
BAT1_V_EMPTY = 42.0    # 12S empty
BAT1_V_DIV = 18.0      # PM02D divider

# GPS
GPS_1_PROTOCOL = 7     # DroneCAN
GPS_2_PROTOCOL = 7     # DroneCAN
GPS_1_CONFIG = 104     # CAN1
GPS_2_CONFIG = 204     # CAN2

# Rangefinder
SENS_EN_RANGEFND = 1
RNGFND_TYPE = 14       # Ainstein US-D1

# Airspeed
SENS_EN_ASPD = 1
ASPD_PRIMARY = 1        # External
```

### 13.4 Sensor Calibration

**Calibration Sequence:**

1. **Compass** - rotate through all axes
2. **Accelerometer** - place on 6 sides
3. **Gyroscope** - keep still
4. **Level Horizon** - level on ground
5. **Airspeed** - cover pitot, calibrate
6. **Radio** - set stick endpoints

### 13.5 Flight Mode Configuration

**Recommended Modes:**

| Switch Position | Mode |
|-----------------|------|
| Position 1 | Manual |
| Position 2 | Stabilized |
| Position 3 | Altitude Hold |
| Position 4 | Position Hold |
| Position 5 | Mission |
| Position 6 | Return to Launch |

---

## 14. Phase 11: Testing & Calibration

### 14.1 Bench Testing Checklist

**Power System:**
- [ ] Battery voltage correct (50.4V charged)
- [ ] All BECs outputting correct voltage
- [ ] Current sensor reading accurate
- [ ] No hot spots on wiring

**Servos:**
- [ ] All servos move when commanded
- [ ] Correct direction for each surface
- [ ] No binding or interference
- [ ] Endpoints set correctly

**Motors:**
- [ ] Motor spins correct direction
- [ ] Smooth acceleration
- [ ] ESC temperature acceptable
- [ ] Propeller secure

**Avionics:**
- [ ] Pixhawk boots correctly
- [ ] All sensors recognized
- [ ] GPS gets fix
- [ ] Telemetry link works

### 14.2 Control Surface Verification

**Test each surface:**

| Input | Expected Response |
|-------|-------------------|
| Roll Right | Left aileron UP, Right aileron DOWN |
| Roll Left | Left aileron DOWN, Right aileron UP |
| Pitch Up | Both V-tail trailing edges UP |
| Pitch Down | Both V-tail trailing edges DOWN |
| Yaw Right | Left V-tail UP, Right V-tail DOWN |
| Yaw Left | Left V-tail DOWN, Right V-tail UP |

### 14.3 Center of Gravity

**CG Location:**
- Mark CG point at 25-30% of Mean Aerodynamic Chord
- For Mugin 3220mm: approximately 450-500mm from wing leading edge

**CG Check:**
1. Fully assembled with batteries
2. Lift at marked CG points
3. Aircraft should balance level or slightly nose-down
4. Adjust battery position to achieve correct CG

### 14.4 Motor Run-Up Test

**Safety First:**
- Secure aircraft to bench or ground
- All personnel clear of propeller arc
- Fire extinguisher nearby

**Test Procedure:**

1. Arm aircraft (require safety switch + arm command)
2. Slowly advance throttle to 25%
3. Monitor motor temperature
4. Advance to 50% - check thrust
5. Monitor current draw (should match spec)
6. Slowly reduce throttle
7. Disarm

---

## 15. Phase 12: First Flight Procedures

### 15.1 Pre-Flight Checklist

**Before leaving for field:**
- [ ] Batteries fully charged
- [ ] All firmware updated
- [ ] Ground station configured
- [ ] Tools and spares packed
- [ ] Weather conditions checked

**At the field:**
- [ ] Aircraft inspected
- [ ] Control surfaces verified
- [ ] GPS lock obtained (minimum 12 satellites)
- [ ] Compass healthy
- [ ] Battery voltage verified
- [ ] Failsafe modes configured
- [ ] RTL altitude set
- [ ] Geofence configured

### 15.2 First Flight Protocol

**Flight 1: Short Test/Manual (5 min)**

1. Take off in MANUAL mode
2. Climb to 50m altitude
3. Perform gentle turns
4. Verify control response
5. Land and inspect

**Flight 2: Stabilized Assessment (10 min)**

1. Take off and climb to 100m
2. Switch to STABILIZED mode
3. Perform maneuvers:
   - Straight and level
   - Gentle turns
   - Altitude changes
4. Verify PID tuning
5. Land and download logs

**Flight 3: Auto Modes (15 min)**

1. Take off and climb to 100m
2. Switch to POSITION mode
3. Release sticks - verify hold
4. Test simple mission (short pattern)
5. Test RTL
6. Land and evaluate

### 15.3 Initial Tuning

**Parameters to adjust based on flight test:**

| Issue | Parameter | Adjustment |
|-------|-----------|------------|
| Roll oscillation | FW_R_P | Decrease |
| Sluggish roll | FW_R_P | Increase |
| Pitch oscillation | FW_P_P | Decrease |
| Altitude hunting | FW_T_ALT_TC | Increase |
| Slow throttle response | FW_THR_CRUISE | Adjust |

---

## 16. Troubleshooting Guide

### 16.1 Common Issues

| Problem | Possible Cause | Solution |
|---------|---------------|----------|
| No GPS lock | Poor antenna placement | Move GPS higher, check sky view |
| Compass errors | Magnetic interference | Move away from power wires |
| Motor won't arm | Pre-arm checks failing | Check QGC messages |
| ESC beeping | No signal or low battery | Verify PWM connection |
| Video dropout | Antenna obstruction | Improve antenna placement |
| Servo jitter | Power brownout | Add capacitor, check BEC |
| CG too tail-heavy | Battery too far back | Move batteries forward |

### 16.2 Error Codes

**Pixhawk LED Codes:**

| Pattern | Meaning |
|---------|---------|
| Solid green | Ready to fly |
| Blinking green | Calibrating |
| Solid orange | Standby, not armed |
| Blinking orange | Compass cal required |
| Solid red | Error - check QGC |
| Blinking red/blue | Armed and dangerous |

### 16.3 Log Analysis

**After each flight:**

1. Download flight log (.ulg file)
2. Upload to logs.px4.io
3. Review flight analysis
4. Address any warnings/errors

---

## 17. Maintenance Schedule

### 17.1 Pre-Flight (Every Flight)

- [ ] Visual inspection of airframe
- [ ] Check propeller for damage
- [ ] Verify battery voltage
- [ ] Test control surfaces
- [ ] Confirm GPS lock

### 17.2 Every 10 Flights

- [ ] Tighten all screws
- [ ] Inspect wire connections
- [ ] Check servo horn screws
- [ ] Clean propeller
- [ ] Verify motor mount secure
- [ ] Check landing gear

### 17.3 Every 50 Flights

- [ ] Full compass calibration
- [ ] Replace servo linkage hardware
- [ ] Inspect motor bearings
- [ ] Deep clean airframe
- [ ] Battery health check
- [ ] Re-verify CG

### 17.4 Every 100 Flights

- [ ] Replace propeller
- [ ] ESC inspection
- [ ] Motor bearing replacement (if needed)
- [ ] Full avionics test
- [ ] Re-flash firmware

---

## Appendix A: Recommended Spares

| Item | Quantity |
|------|----------|
| Propeller | 2 |
| Servo | 1 |
| XT90 connectors | 2 pairs |
| Servo arm screws | 8 |
| Control horns | 4 |
| Pushrod ends | 4 |
| JST-GH connectors | 10 |
| Heat shrink assortment | 1 kit |
| Epoxy | 1 kit |
| CA glue | 1 bottle |

---

## Appendix B: Performance Specifications

### Expected Performance (at 25kg MTOW)

| Parameter | Value |
|-----------|-------|
| Stall Speed | ~45 km/h |
| Cruise Speed | 80-100 km/h |
| Max Speed | 140 km/h |
| Climb Rate | 3-5 m/s |
| Endurance | 3-4 hours |
| Range | 300+ km |
| Service Ceiling | 4,000m |

---

## Appendix C: Legal Requirements

Before flying, ensure compliance with:

- [ ] Local aviation regulations (FAA Part 107, EASA, etc.)
- [ ] Remote ID requirements
- [ ] Airspace authorization (if required)
- [ ] Insurance
- [ ] Registration

---

*Document created: January 11, 2026*  
*Build Guide Version: 1.0*  
*For Artemis Long-Range UAV Project*
