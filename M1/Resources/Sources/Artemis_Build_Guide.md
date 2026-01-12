# Artemis Long-Range Research UAV Build Guide

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

This build guide covers the complete assembly of an **Artemis ERS-class long-range autonomous research UAV** based on the Mugin 3220mm V-Tail platform. The system features:

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

### 8.3 Scientific/Industrial Grade Build (~$80,000-150,000)

| Category | Selected Components | Subtotal |
|----------|-------------------|----------|
| **Motor** | T-Motor U15L KV43 | $1,300 |
| **ESC** | APD 200F3 HV | $400 |
| **Propeller** | T-Motor NS28×9 CF | $200 |
| **Flight Controller** | Auterion Skynode X (Enterprise) | $10,000 |
| **AI Computer** | NVIDIA Jetson AGX Orin 64GB | $2,000 |
| **GPS** | NovAtel OEM7 + CRPA Antenna | $8,000 |
| **Cameras** | Industrial 4K GS + PTZ gimbal | $5,000 |
| **Thermal** | FLIR Boson 640 + integration | $8,000 |
| **Altimeter** | Radar + LiDAR redundant | $1,000 |
| **Datalink** | Doodle Labs encrypted mesh | $5,000 |
| **Satcom** | Iridium Certus 9810 terminal | $5,000 |
| **Battery** | Custom 90+ kg Li-ion pack | $15,000 |
| **Power System** | Industrial-spec PDB, BMS, converters | $3,000 |
| **Airframe** | Custom 3.5m CF delta wing | $25,000 |
| **Servos** | 6× Industrial-spec servo actuators | $2,000 |
| **Integration** | Wiring, EMI shielding, testing | $10,000 |
| **Software** | Auterion Suite commercial license | $5,000 |
| **TOTAL** | | **~$105,900** |
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
