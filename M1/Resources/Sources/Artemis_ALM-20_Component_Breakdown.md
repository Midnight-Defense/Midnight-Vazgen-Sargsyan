# Artemis ERS-20 Component Breakdown

> **Classification:** Technical Component Analysis  
> **Version:** 2.0  
> **Date:** January 11, 2026  
> **Subject:** Complete System Architecture & Real-World Component Shopping List

---

## Executive Summary

This document provides a comprehensive component-level breakdown of the **Artemis ERS-20** autonomous research & response system (ERS). This version includes **specific, purchasable real-world components** with brand names, model numbers, specifications, and estimated prices—similar to building a custom scientific platform where each part can be sourced and assembled.

Based on available open-source intelligence, manufacturer specifications, and technical analysis of comparable systems, this breakdown covers all major subsystems including avionics, propulsion, payload, navigation, power, airframe, and ground support equipment.

---

# 🛒 REAL-WORLD COMPONENT SHOPPING LIST

## Complete Parts List (Build-Your-Own Style)

This section identifies **specific, commercially available components** that could be used to assemble an Artemis ERS-20 equivalent system. Prices are estimates based on 2025-2026 market rates.

---

## 🔧 PROPULSION SYSTEM

### Motor

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **Primary Motor** | **T-Motor U13II KV130** | 24.3 kg thrust, 12S, 990g, Ø100×60mm, 5.6kW | **$450-550** | T-Motor Store |
| **Alternative** | **T-Motor U15II KV80** | 36 kg thrust, 12-24S, 1740g, Ø147.5×64mm, 8.5kW | **$650-800** | T-Motor Store |
| **Heavy-Lift Option** | **T-Motor U15L KV43** | 63.3 kg thrust, 24S, 3600g, 2.8kW rated, manned-capable | **$1,200-1,500** | T-Motor Store |

### Electronic Speed Controller (ESC)

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **Primary ESC** | **APD 120F3[X] HV ESC** | 120A cont/200A burst, 4-12S (50V max), 32-bit F3, 9kW peak, 20g | **$180-250** | Power Drives/GetFPV |
| **Alternative** | **T-Motor FLAME 150A HV** | 150A, 6-14S, FOC, telemetry | **$200-280** | T-Motor Store |
| **Heavy Option** | **APD 200F3 HV** | 200A continuous, 50V max | **$350-450** | Power Drives |

### Propeller

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **Primary Propeller** | **T-Motor NS26×8.5 CF** | 26" diameter, 8.5" pitch, carbon fiber, pusher | **$120-180** | T-Motor Store |
| **Alternative** | **APC 26×15E Electric** | 26" diameter, 15" pitch, composite | **$60-90** | APC Propellers |
| **Folding Option** | **T-Motor FA26.5×8.9** | Folding 26.5", carbon fiber | **$200-280** | T-Motor Store |

---

## 🧠 AVIONICS & FLIGHT CONTROL

### Flight Controller / Mission Computer

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **Primary (Authentic)** | **Auterion Skynode X** | FMUv6x, ARM A53 Quad 1.8GHz, 4GB RAM, 16GB eMMC, 4G/WiFi/BT, 159g | **$5,000-15,000** | Auterion (Quote Required) |
| **Open-Source Alternative** | **Holybro Pixhawk 6X Set** | FMUv6x, STM32H753 M7 480MHz, triple IMU, Ethernet, modular | **$250-400** | Holybro/GetFPV |
| **Pro Alternative** | **Holybro Pixhawk 6X Pro** | ADIS16470 industrial IMU, ±40g accel, enhanced sensors | **$400-600** | Holybro |
| **Budget Option** | **Holybro Pixhawk 6C** | FMUv6c, compact, dual IMU | **$150-220** | Holybro |

### AI Edge Computing Module

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **Primary AI Module** | **NVIDIA Jetson Orin NX 16GB** | 100 TOPS, 1024 CUDA cores, 8-core ARM A78, 16GB LPDDR5, 10-25W | **$599-699** | NVIDIA/Seeed/Arrow |
| **Developer Kit** | **NVIDIA Jetson Orin NX Dev Kit** | Complete dev kit with carrier board, heatsink, 256GB SSD | **$899-999** | NVIDIA Store |
| **Alternative** | **NVIDIA Jetson Orin Nano 8GB** | 40 TOPS, 1024 CUDA cores, 8GB, budget option | **$299-399** | NVIDIA Store |
| **Companion Computer** | **Raspberry Pi 5 8GB** | Backup/aux computing, 2.4GHz quad-core | **$80-100** | Raspberry Pi |
| **Carrier Board** | **Seeed Studio reComputer J401** | Jetson Orin carrier, multiple I/O | **$150-200** | Seeed Studio |

### Inertial Measurement Unit (IMU)

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **Primary IMU** | **Analog Devices ADIS16470** | Industrial MEMS, ±2000°/s, ±40g, 2.5° bias stability | **$400-600** | DigiKey/Mouser |
| **Triple-Redundant** | **ICM-45686 (×3)** | Included in Pixhawk 6X, BalancedGyro™ | Included | With FC |
| **Tactical Grade** | **VectorNav VN-100** | 0.5° heading, 0.1° pitch/roll, GPS-aided | **$800-1,200** | VectorNav |
| **AHRS System** | **Lord MicroStrain 3DM-CV7** | Tactical-grade AHRS/INS | **$2,000-4,000** | LORD |

---

## 🛰️ NAVIGATION & GPS

### GNSS Receiver & Antenna

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **Primary GNSS** | **CubePilot HerePro** | u-blox F9P RTK, L1/L2/E5, STM32H7, multi-band antenna, 101g | **$400-500** | CubePilot |
| **RTK GPS** | **Holybro H-RTK F9P Rover** | u-blox F9P, RTK cm-level, multi-constellation | **$280-350** | Holybro |
| **Standard GPS** | **CubePilot Here3+** | u-blox M8P, RTK, RM3100 compass, CAN bus, 49g | **$150-200** | CubePilot |
| **Budget Option** | **Holybro M10 GPS** | u-blox M10, GPS/GLONASS/Galileo/BeiDou | **$50-80** | Holybro |
| **Anti-Jam Antenna** | **Trimble Bullet 360** | Multi-freq GNSS antenna, survey-grade | **$200-400** | Trimble |
| **CRPA System** | **NovAtel GAJT-AE-N** | Anti-jam GPS, 4-element CRPA (scientific-grade) | **$15,000-30,000** | NovAtel (Restricted) |

---

## 📹 SENSOR SUITE

### Electro-Optical (EO) Cameras

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **Navigation Camera** | **Arducam IMX477 12MP (Jetson)** | Sony IMX477, 12.3MP, 1/2.3", 4K30, MIPI CSI-2 | **$80-120** | Arducam |
| **Global Shutter** | **Arducam AR0234 2MP GS** | 2.3MP global shutter, 120fps, industrial | **$100-150** | Arducam |
| **High-Res Option** | **e-con Systems e-CAM50 CUNX** | 5MP, Sony IMX568, for Jetson, autofocus | **$150-200** | e-con Systems |
| **Downward Camera** | **Arducam OV9281 1MP GS** | 1MP global shutter, terrain matching | **$40-60** | Arducam |
| **Zoom Camera** | **Arducam IMX477 PTZ** | 12MP with 4.38-10.71mm zoom lens | **$200-300** | Arducam |

### Infrared (IR) / Thermal Cameras

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **LWIR Thermal** | **FLIR Boson 640** | 640×512, 12µm, 7.5g, 500mW, uncooled VOx | **$4,000-7,000** | FLIR/Teledyne |
| **Budget Thermal** | **FLIR Boson 320** | 320×256, 12µm, 7.5g, 500mW | **$2,000-3,500** | FLIR/Teledyne |
| **Entry Level** | **FLIR Lepton 3.5** | 160×120, radiometric, 0.6g | **$200-300** | GroupGets |
| **Dual Sensor** | **FLIR Duo Pro R** | 640 thermal + 4K visible, gimbal-ready | **$10,000-15,000** | FLIR |

### Altimeter Sensors

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **Radar Altimeter** | **Ainstein US-D1 Radar** | 0.5-50m range, K-band, 25g | **$300-500** | Ainstein |
| **LiDAR Altimeter** | **Lightware SF11/C** | 0.2-120m, 20Hz, 35g | **$250-350** | Lightware |
| **Budget Lidar** | **TFmini Plus** | 0.1-12m, 1000Hz, 12g | **$40-60** | Benewake |
| **Barometer** | **BMP388 (×2)** | High-precision, included in Pixhawk | Included | With FC |

### Air Data Sensors

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **Pitot Tube** | **Holybro Digital Airspeed Sensor** | MS4525DO, I2C, heated option | **$50-80** | Holybro |
| **Advanced Airspeed** | **Matek ASPD-4525** | I2C, temp compensated | **$30-50** | Matek |
| **Probe** | **Holybro Heated Pitot Tube** | Stainless steel, heated | **$40-60** | Holybro |

---

## 📡 COMMUNICATIONS SYSTEM

### Primary Datalink

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **HD Video Link** | **CubePilot Herelink 1.1** | 20km range, 2.4GHz, 1080p60, 110ms latency, dual HDMI | **$999-1,200** | CubePilot |
| **Long Range Option** | **Doodle Labs Smart Radio** | 10-100km, 100Mbps, mesh, encrypted | **$2,000-5,000** | Doodle Labs |
| **Open Source** | **RFD900x Modem** | 40km+, 900MHz, 500mW | **$200-300** | RFDesign |
| **Budget Telemetry** | **Holybro SiK Radio V3** | 500mW, 433/915MHz, 2km | **$60-100** | Holybro |

### Backup Communications

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **LTE Modem** | **Quectel RM502Q-AE** | 5G/LTE Cat-20, global bands | **$150-250** | Quectel/DigiKey |
| **Satcom** | **RockBLOCK 9603** | Iridium SBD, global coverage | **$250-350** | Rock Seven |
| **WiFi Module** | **Intel AX210** | WiFi 6E, Bluetooth 5.3 | **$25-40** | Intel |

---

## 🔋 POWER SYSTEM

### Main Battery Pack

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **High Capacity 12S** | **Tattu Pro 12S 22000mAh 25C** | 47.4V, 1003Wh, smart BMS, DroneCAN, 5750g | **$1,200-1,500** | Tattu/GensTattu |
| **Ultra Capacity** | **Tattu Pro 12S 32000mAh** | 47.4V, 1517Wh, 5783g | **$1,800-2,200** | Tattu/GensTattu |
| **14S Option** | **Tattu Pro 14S 22000mAh 25C** | 53.2V, 1170Wh, smart BMS, 6550g | **$1,400-1,700** | Tattu/GensTattu |
| **High Discharge** | **Tattu 4.0 14S 30000mAh 35C** | 53.2V, 1596Wh, 100A cont, 11500g | **$2,500-3,000** | Tattu/GensTattu |
| **Multiple Packs** | **3× Tattu 12S 16000mAh** | Parallel for 48Ah total, ~2.3kWh combined | **$2,700-3,300** | Tattu |

### Power Distribution

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **Power Module** | **Holybro PM02D HV** | 60V max, 120A, voltage/current sensing, CAN | **$50-80** | Holybro |
| **PDB** | **Matek FCHUB-14S** | 14S capable, 200A, multiple outputs | **$40-60** | Matek |
| **DC-DC 12V** | **Pololu D36V50F12** | 50V in, 12V 5A out | **$35-50** | Pololu |
| **DC-DC 5V** | **Holybro PM08-BEC** | 5V/3A regulated, low noise | **$25-35** | Holybro |
| **Battery Charger** | **Tattu TA1200 Smart Charger** | 12S compatible, 1200W, fast charge | **$400-550** | Tattu |

---

## ✈️ AIRFRAME

### Complete Airframe Kit

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **Entry Level** | **Skywalker X8** | 2.1m span, EPO foam, 2.8kg, hobby-grade | **$200-350** | Skywalker |
| **Recommended** | **Mugin 3220mm V-Tail** | 3.2m span, wood/fiberglass/CF, 25kg MTOW, 8kg payload, 6hr endurance | **$3,200-3,800** | MuginUAV |
| **Extended Range** | **Mugin 3600mm H-Tail** | 3.6m span, 28kg MTOW, 8kg payload, DLE60 compatible | **$3,600-4,200** | MuginUAV |
| **Professional** | **Drones Mart 3.5m Composite** | Carbon fiber/kevlar, modular bays | **$8,000-15,000** | Drones Mart |
| **VTOL Platform** | **Viewpro eVT350** | 3.5m span, CF composite, VTOL capability | **$15,000-25,000** | Viewpro |
| **Heavy-Lift** | **Mugin-4 Pro Platform** | 4.7m span, gas/electric, CF construction | **$5,000-10,000** | MuginUAV |
| **Mil-Spec** | **SERBAN 3.5m Delta** | Twin-boom, ruggedized, modular payload | **$10,000-20,000** | SERBAN Inc. |

### Servos

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **Primary Servo** | **Hitec D-980TW** | 78kg-cm, titanium gear, brushless | **$180-220** | Hitec |
| **High-Torque** | **Savox SB-2282SG** | 52kg-cm, brushless, 7.4V | **$120-150** | Savox |
| **Standard** | **Hitec HS-7950TH** | 35kg-cm, titanium gear | **$90-120** | Hitec |
| **Budget Option** | **EMAX ES3054** | 17kg-cm, metal gear, digital | **$20-30** | EMAX |

---

## 💻 SOFTWARE STACK

### Flight Software (Open Source/Free)

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **Autopilot** | **PX4 Autopilot v1.14+** | Open-source, BSD license, enterprise-ready | **FREE** | px4.io |
| **Alternative** | **ArduPilot/ArduPlane** | GPL, mature fixed-wing support | **FREE** | ardupilot.org |
| **Ground Station** | **QGroundControl** | Cross-platform, MAVLink | **FREE** | qgroundcontrol.com |
| **Mission Planner** | **Mission Planner** | Windows, feature-rich | **FREE** | ardupilot.org |
| **AI Framework** | **NVIDIA JetPack 6.0** | L4T, TensorRT, CUDA | **FREE** | developer.nvidia.com |
| **Vision** | **OpenCV + ROS 2** | Computer vision, robotics middleware | **FREE** | opencv.org, ros.org |

### Commercial Software Options

| Component | Brand/Model | Specifications | Est. Price | Source |
|-----------|-------------|----------------|------------|--------|
| **Auterion Suite** | **AuterionOS + Mission Control** | Enterprise PX4, visual nav, cloud | **Contact** | Auterion |
| **AI Models** | **YOLOv8/v9** | Object detection, optimized for Jetson | **FREE** | Ultralytics |
| **SLAM** | **ORB-SLAM3** | Visual-inertial SLAM, open-source | **FREE** | GitHub |

---

## 📋 COMPLETE BUILD SUMMARY

### Option 1: Research/Development Build (~$15,000-25,000)

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
| **Airframe** | Mugin 3220mm V-Tail Composite (3.2m span, 8kg payload, CF/fiberglass) | $3,600 |
| **Servos** | 4× Hitec D-980TW | $800 |
| **Misc** | Wiring, connectors, mounts, hardware | $1,000 |
| **Software** | PX4 + QGC + JetPack (FREE) | $0 |
| **TOTAL** | | **~$16,170** |

### Option 2: Professional/Enterprise-Grade Build (~$80,000-150,000)

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
| **Power System** | Mil-spec PDB, BMS, converters | $3,000 |
| **Airframe** | Custom 3.5m CF delta wing | $25,000 |
| **Servos** | 6× Mil-spec servo actuators | $2,000 |
| **Integration** | Wiring, EMI shielding, testing | $10,000 |
| **Software** | Auterion Suite commercial license | $5,000 |
| **TOTAL** | | **~$105,900** |

---

## 🔗 COMPONENT SOURCING GUIDE

### Primary Vendors

| Vendor | Specialty | Website |
|--------|-----------|---------|
| **T-Motor** | Motors, propellers, ESCs | store.tmotor.com |
| **Holybro** | Pixhawk FC, GPS, power | holybro.com |
| **CubePilot** | Here GPS, Herelink datalink | cubepilot.org |
| **Auterion** | Enterprise avionics | auterion.com |
| **NVIDIA** | Jetson AI modules | developer.nvidia.com |
| **Arducam** | Cameras for embedded | arducam.com |
| **FLIR/Teledyne** | Thermal imaging | flir.com |
| **Tattu/Grepow** | High-capacity batteries | genstattu.com |
| **GetFPV** | General drone components | getfpv.com |
| **RobotShop** | Robotics components | robotshop.com |
| **DigiKey/Mouser** | Electronics components | digikey.com, mouser.com |

---

## Table of Contents

1. [System Architecture Overview](#1-system-architecture-overview)
2. [Airframe & Structural Components](#2-airframe--structural-components)
3. [Propulsion System](#3-propulsion-system)
4. [Avionics & Flight Control](#4-avionics--flight-control)
5. [Navigation & Guidance System](#5-navigation--guidance-system)
6. [Sensor Suite](#6-sensor-suite)
7. [Communications System](#7-communications-system)
8. [Power System](#8-power-system)
9. [Scientific Payload Section](#9-scientific-payload-section)
10. [Launch System](#10-launch-system)
11. [Ground Control Station](#11-ground-control-station)
12. [Software Stack](#12-software-stack)
13. [Bill of Materials Summary](#13-bill-of-materials-summary)
14. [Weight Budget Analysis](#14-weight-budget-analysis)

---

## 1. System Architecture Overview

### 1.1 Top-Level System Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        ARTEMIS ERS-20 SYSTEM ARCHITECTURE                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌───────────────┐    ┌───────────────┐    ┌───────────────┐                │
│  │   AIRFRAME    │    │  PROPULSION   │    │    POWER      │                │
│  │  - Fuselage   │    │  - Motor      │    │  - Battery    │                │
│  │  - Wings      │    │  - ESC        │    │  - BMS        │                │
│  │  - Control    │    │  - Propeller  │    │  - DC-DC      │                │
│  │    Surfaces   │    │  - Cooling    │    │  - Distrib.   │                │
│  └───────┬───────┘    └───────┬───────┘    └───────┬───────┘                │
│          │                    │                    │                        │
│          └────────────────────┼────────────────────┘                        │
│                               │                                              │
│                    ┌──────────▼──────────┐                                   │
│                    │    SKYNODE N        │                                   │
│                    │  MISSION COMPUTER   │
│                    │  - Flight Control   │
│                    │  - Data Logging     │
│                    │  - AI Processing    │                                   │
│                    │  - Comms Hub        │                                   │
│                    └──────────┬──────────┘                                   │
│                               │                                              │
│     ┌─────────────────────────┼─────────────────────────┐                   │
│     │                         │                         │                   │
│ ┌───▼───────────┐    ┌────────▼────────┐    ┌──────────▼──────────┐        │
│ │  NAVIGATION   │    │    SENSORS      │    │   COMMUNICATIONS    │        │
│ │  - GPS/GNSS   │    │  - EO Camera    │    │   - Datalink        │        │
│ │  - INS/IMU    │    │  - IR Camera    │    │   - Encryption      │        │
│ │  - Visual Nav │    │  - Target Acq.  │    │   - Antenna Array   │        │
│ │  - SLAM       │    │  - Altimeter    │    │                     │        │
│ └───────────────┘    └─────────────────┘    └─────────────────────┘        │
│                                                                              │
│                    ┌──────────────────────┐                                  │
│                    │   PAYLOAD SECTION    │
│                    │   - Environmental Mod│
│                    │   - Data Interface   │
│                    │   - Modular Sensors  │
│                    └──────────────────────┘                                  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Major Subsystem Summary

| Subsystem | Primary Function | Key Technology |
|-----------|-----------------|----------------|
| Airframe | Structural integrity, aerodynamics | Composite delta-wing |
| Propulsion | Thrust generation | Electric BLDC motor |
| Avionics | Flight control, computing | Auterion Skynode N |
| Navigation | Position/attitude determination | AI Visual + GPS/INS |
| Sensors | Target acquisition, awareness | EO/IR, LIDAR, MMW |
| Communications | C2 link, telemetry | Encrypted datalink |
| Power | Electrical energy storage | Li-ion battery pack |
| Payload | Data collection / Cargo | Multi-modal sensor bay |
| Launch | Initial velocity | Catapult/rail system |

---

## 2. Airframe & Structural Components

### 2.1 Configuration Overview

| Parameter | Specification |
|-----------|--------------|
| **Configuration** | Tailless delta-wing (flying wing) |
| **Design Heritage** | Similar to Shahed-136/German DAR |
| **Estimated Length** | 3.5-4.0 meters |
| **Estimated Wingspan** | 2.5-3.0 meters |
| **Wing Area** | ~2.0-2.5 m² |
| **Aspect Ratio** | ~3.0-3.5 |
| **Sweep Angle** | ~45-50° leading edge |

### 2.2 Fuselage Components

| Component | Material | Function | Qty |
|-----------|----------|----------|-----|
| **Forward Fuselage Section** | Carbon fiber composite | Houses sensors, camera, nav electronics | 1 |
| **Center Fuselage Section** | Carbon fiber/kevlar composite | Payload bay, sensor/battery compartment | 1 |
| **Aft Fuselage Section** | Carbon fiber composite | Motor mount, propulsion integration | 1 |
| **Nose Cone** | Fiberglass/radome material | Camera window, antenna housing | 1 |
| **Access Panels** | Carbon fiber | Maintenance access | 4-6 |
| **Internal Bulkheads** | Aluminum/carbon fiber | Structural load transfer | 3-4 |
| **Equipment Bay Rails** | Aluminum | Component mounting | 8-10 |
| **Vibration Isolators** | Silicone rubber/dampers | Sensor protection | 12-20 |

### 2.3 Wing Structure

| Component | Material | Function | Qty |
|-----------|----------|----------|-----|
| **Wing Skins** | Carbon fiber laminate | Aerodynamic surface | 4 (upper/lower × 2) |
| **Wing Spars** | Carbon fiber/aluminum | Primary load carrying | 2 main + 2 aft |
| **Wing Ribs** | Foam core/carbon fiber | Airfoil shape maintenance | 8-12 per side |
| **Control Surface Ribs** | Carbon fiber | Elevon structure | 4 per elevon |
| **Wingtip Fins** | Carbon fiber composite | Directional stability | 2 |
| **Leading Edge** | Fiberglass | Impact resistance | 2 |
| **Trailing Edge** | Carbon fiber/honeycomb | Stiffness | 2 |

### 2.4 Control Surfaces

| Component | Type | Function | Qty |
|-----------|------|----------|-----|
| **Elevons** | Combined elevator/aileron | Pitch and roll control | 2 |
| **Rudderettes** | Vertical surfaces at wingtips | Yaw control/stability | 2 |
| **Split Flaps** (optional) | Speed brakes | Drag modulation | 2 |

### 2.5 Control Surface Actuation

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Digital Servos (Elevon)** | High-torque (15-25 kg·cm), brushless | 2-4 |
| **Digital Servos (Rudder)** | Medium-torque (8-12 kg·cm) | 2 |
| **Servo Linkages** | Stainless steel/titanium | 4-6 |
| **Control Horns** | Aluminum | 4-6 |
| **Push-Pull Rods** | Carbon fiber | 4-6 |
| **Ball Link Connectors** | Hardened steel | 8-12 |

### 2.6 Structural Fasteners & Hardware

| Component | Material | Qty (approx.) |
|-----------|----------|---------------|
| **Structural Bolts** | Titanium/stainless | 50-100 |
| **Panel Screws** | Stainless steel | 100-200 |
| **Blind Rivets** | Aluminum | 200-400 |
| **Composite Inserts** | Brass/stainless | 80-120 |
| **Locking Fasteners** | NyLok | 30-50 |
| **Hinge Pins** | Stainless steel | 8-12 |

---

## 3. Propulsion System

### 3.1 Electric Motor Assembly

The Artemis ALM-20 uniquely uses electric propulsion for a long-range loitering munition, prioritizing low acoustic/thermal signature over range efficiency.

| Component | Specification | Qty |
|-----------|--------------|-----|
| **BLDC Motor** | High-efficiency, low-KV (400-600 KV) | 1 |
| **Motor Type** | Outrunner BLDC | - |
| **Power Output** | 3-5 kW continuous | - |
| **Voltage** | 48-60V (12S-14S equivalent) | - |
| **Efficiency** | >90% | - |
| **Weight** | 800-1200g | - |
| **Motor Mount** | CNC aluminum, vibration-damped | 1 |
| **Motor Controller** | See ESC section | - |
| **Cooling Shroud** | Aluminum/carbon fiber | 1 |
| **Temperature Sensors** | NTC thermistors | 2 |

### 3.2 Electronic Speed Controller (ESC)

| Component | Specification | Qty |
|-----------|--------------|-----|
| **ESC Unit** | High-voltage (HV) 120-200A continuous | 1 |
| **Controller Type** | FOC (Field-Oriented Control) | - |
| **BEC Output** | 5V/12V dual output, 5A+ | - |
| **Programming Interface** | USB/CAN bus | - |
| **Cooling** | Integrated heatsink + ducted | - |
| **PWM Frequency** | 8-48 kHz | - |
| **Weight** | 100-200g | - |
| **Current Sensors** | Hall-effect | 3 (per phase) |
| **Capacitor Bank** | Low-ESR electrolytic | 1 |

### 3.3 Propeller Assembly

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Propeller** | Carbon fiber, pusher configuration | 1 |
| **Diameter** | 24-28 inches (60-70 cm) | - |
| **Pitch** | High-pitch for efficiency (18-22") | - |
| **Blades** | 2-blade (low noise) or 3-blade | - |
| **Hub Type** | Variable pitch or fixed | - |
| **Propeller Spinner** | Carbon fiber | 1 |
| **Prop Adapter** | Aluminum, balanced | 1 |
| **Prop Shaft** | Hardened steel | 1 |
| **Locking Nut** | Self-locking | 1 |

### 3.4 Propulsion Performance Estimates

| Parameter | Value |
|-----------|-------|
| **Static Thrust** | 15-20 kg |
| **Cruise Thrust** | 5-8 kg |
| **Power Consumption (Cruise)** | 1.5-2.5 kW |
| **Cruise Speed** | 150-185 km/h |
| **Endurance** | 10-12 hours |
| **Range** | 1,600 km |

---

## 4. Avionics & Flight Control

### 4.1 Skynode N Mission Computer

The heart of the Artemis ALM-20 is the **Auterion Skynode N** integrated avionics system.

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Main Unit** | Skynode N (custom research variant) | 1 |
| **Form Factor** | Integrated FMU + mission computer | - |
| **Dimensions** | ~100 × 60 × 25 mm (estimated) | - |
| **Weight** | ~150-250g | - |

#### 4.1.1 Flight Management Unit (FMU)

| Component | Specification |
|-----------|--------------|
| **Standard** | FMUv6x (Pixhawk compatible) |
| **MCU** | ARM Cortex-M7 @ 480 MHz |
| **Software** | PX4 Autopilot |
| **Sensor Update Rate** | 8 kHz |
| **PWM Outputs** | 16 channels |
| **Redundancy** | Triple-sensor voting |

#### 4.1.2 Mission Computer

| Component | Specification |
|-----------|--------------|
| **Processor** | ARM Cortex-A53 Quad-Core @ 1.8 GHz |
| **RAM** | 4 GB LPDDR4 |
| **Storage** | 16-32 GB eMMC |
| **NPU** | 2.3 TOPS (Neural Processing Unit) |
| **Video Encoding** | 2× 1080p60 H.264/H.265 |
| **OS** | AuterionOS (Linux-based) |

### 4.2 AI Node (NVIDIA Integration)

For advanced AI processing, an AI Node co-processor is likely integrated:

| Component | Specification | Qty |
|-----------|--------------|-----|
| **AI Node ONX** | NVIDIA Orin NX module | 1 |
| **GPU** | 1024 CUDA Cores + 32 Tensor Cores | - |
| **AI Performance** | Up to 100 TOPS (INT8) | - |
| **RAM** | 8-16 GB LPDDR5 | - |
| **Interface** | PCIe to Skynode | - |
| **Cooling** | Active heatsink with fan | 1 |
| **Power Consumption** | 10-25W configurable | - |

### 4.3 Inertial Measurement Unit (IMU)

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Primary IMU** | Tactical-grade MEMS | 1 |
| **Backup IMU** | Industrial-grade MEMS | 2 |
| **Gyroscope** | 3-axis, ±2000°/sec | 3 |
| **Accelerometer** | 3-axis, ±16-24g | 3 |
| **Magnetometer** | 3-axis | 2 (external) |
| **Barometric Sensor** | ±1 hPa absolute | 2 |
| **Temperature Sensor** | IMU calibration | 3 |
| **IMU Isolation Mount** | Silicone damping | 1 |

### 4.4 Flight Control Actuators Interface

| Interface | Specification | Purpose |
|-----------|--------------|---------|
| **PWM Outputs** | 16 channels, 50-400Hz | Servo control |
| **SBUS Input** | RC receiver backup | Manual override |
| **SBUS Output** | Servo bus output | Daisy-chain servos |
| **CAN Bus** | 2× CAN 2.0B | Smart actuators |
| **UART** | 4× serial ports | Peripheral comms |
| **SPI** | External sensors | High-speed data |
| **I2C** | Compass, peripherals | Sensor bus |

---

## 5. Navigation & Guidance System

### 5.1 GPS/GNSS Receiver

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Primary GNSS** | Multi-constellation (GPS/GLONASS/Galileo/BeiDou) | 1 |
| **Backup GNSS** | Secondary receiver for redundancy | 1 |
| **CRPA Antenna** | 8-channel Controlled Reception Pattern Antenna | 1 |
| **Anti-Spoofing** | M-code capable (industrial GPS) likely | - |
| **Update Rate** | 10-20 Hz | - |
| **Accuracy (GPS)** | <1m CEP with SBAS | - |
| **Accuracy (RTK)** | <10cm if available | - |

### 5.2 Visual Navigation System

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Navigation Camera** | High-resolution EO camera | 1 |
| **Resolution** | 4K or higher | - |
| **Frame Rate** | 30-60 fps | - |
| **Field of View** | Wide-angle (90-120°) | - |
| **Lens** | Fixed or motorized zoom | - |
| **Image Processor** | Integrated in AI Node | - |

### 5.3 Visual Navigation Algorithms

| Algorithm | Function | Processor |
|-----------|----------|-----------|
| **Visual-Inertial Odometry (VIO)** | Camera+IMU fusion for position | AI Node |
| **Visual SLAM** | Simultaneous mapping/localization | AI Node |
| **Map Matching** | Terrain correlation with sat imagery | Mission Computer |
| **Optical Flow** | Velocity estimation | Dedicated ASIC |
| **Feature Tracking** | Landmark identification | AI Node |

### 5.4 Terrain Matching Database

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Digital Elevation Model** | Pre-loaded terrain data | - |
| **Satellite Imagery** | Georeferenced reference maps | - |
| **Storage** | 16-32 GB on eMMC | - |
| **Coverage** | Mission-specific region | - |
| **Resolution** | 0.5-2m per pixel | - |

### 5.5 Inertial Navigation System (INS)

| Component | Specification | Qty |
|-----------|--------------|-----|
| **INS Grade** | Tactical-grade | - |
| **Drift Rate** | <1 nmi/hr (estimated) | - |
| **GPS/INS Fusion** | Kalman filter | - |
| **Alignment Time** | <60 seconds | - |
| **Operating Temp** | -40°C to +85°C | - |

### 5.6 Observation & Survey Guidance System

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Survey Camera** | High-resolution EO/IR | 1 |
| **AI Objective Recognition** | CNN-based object detection | - |
| **Track and Monitor App** | Auterion software | - |
| **Identification Range** | Several kilometers | - |
| **Accuracy (CEP)** | <1-3 meters | - |

---

## 6. Sensor Suite

### 6.1 Electro-Optical (EO) Sensors

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Nose Camera (Nav/Target)** | 4K RGB, global shutter | 1 |
| **Sensor Type** | CMOS, high dynamic range | - |
| **Pixel Size** | 1.5-2.5 µm | - |
| **Lens Mount** | Fixed or CS-mount | - |
| **Zoom** | Digital and/or optical (2-10×) | - |
| **Stabilization** | Electronic (EIS) | - |
| **Downward Camera** | For terrain matching | 1 |

### 6.2 Infrared (IR) Sensors

| Component | Specification | Qty |
|-----------|--------------|-----|
| **LWIR Camera** | Long-wave infrared (8-14 µm) | 1 (optional) |
| **Resolution** | 640×512 or 1024×768 | - |
| **Sensor Type** | Uncooled microbolometer | - |
| **NETD** | <50 mK | - |
| **Frame Rate** | 30-60 Hz | - |
| **Purpose** | Night operations, target discrimination | - |

### 6.3 Altimeter Sensors

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Barometric Altimeter** | MEMS pressure sensor | 2 |
| **Radar Altimeter** | Low-power FMCW | 1 |
| **Radar Frequency** | K-band (24 GHz) or similar | - |
| **Range** | 0-500m AGL | - |
| **Accuracy** | ±1m | - |
| **Purpose** | Terrain following, terminal dive | - |

### 6.4 Air Data Sensors

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Pitot-Static Probe** | Heated pitot tube | 1 |
| **Differential Pressure Sensor** | Airspeed measurement | 1 |
| **Temperature Sensor** | Outside Air Temperature (OAT) | 1 |
| **Dynamic Pressure Range** | 0-2000 Pa | - |
| **Airspeed Range** | 20-250 km/h | - |

### 6.5 Additional Sensors

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Ambient Light Sensor** | Camera exposure control | 1 |
| **Vibration Sensors** | MEMS accelerometers | 2 |
| **Voltage/Current Monitors** | Power system health | 4+ |
| **Temperature Monitors** | Distributed throughout | 8-12 |

---

## 7. Communications System

### 7.1 Primary Datalink

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Datalink Radio** | Long-range encrypted transceiver | 1 |
| **Frequency Band** | L-band, S-band, or C-band | - |
| **Modulation** | Spread spectrum (FHSS/DSSS) | - |
| **Data Rate** | 1-10 Mbps video + telemetry | - |
| **Range** | 100+ km LOS | - |
| **Encryption** | AES-256 or equivalent | - |
| **Anti-Jam** | Frequency hopping | - |

### 7.2 Backup/Auxiliary Communications

| Component | Specification | Qty |
|-----------|--------------|-----|
| **4G/LTE Modem** | Cellular backup link | 1 (optional) |
| **Iridium/Satcom** | BLOS capability | 1 (optional) |
| **WiFi Module** | Short-range recovery/testing | 1 |
| **Bluetooth** | Configuration/maintenance | 1 |

### 7.3 Antennas

| Component | Specification | Qty |
|-----------|--------------|-----|
| **GNSS Antenna (CRPA)** | 8-element anti-jam | 1 |
| **GNSS Backup Antenna** | Patch antenna | 1 |
| **Datalink Antenna (Omni)** | Blade or conformal | 1 |
| **Datalink Antenna (Directional)** | Phased array or patch | 1 |
| **Cellular Antenna** | LTE/5G compatible | 1 |
| **WiFi/BT Antenna** | Dual-band | 1 |

### 7.4 Communication Interfaces

| Interface | Specification | Purpose |
|-----------|--------------|---------|
| **Ethernet** | 100Base-T | Internal network |
| **USB** | USB 2.0 OTG | Configuration |
| **RS-422** | Serial | Legacy peripherals |
| **CAN Bus** | Distributed comms | Actuators |

---

## 8. Power System

### 8.1 Main Battery Pack

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Battery Type** | Lithium-ion (Li-ion) or Li-Polymer | 1 |
| **Configuration** | 12S-14S (44.4V-51.8V nominal) | - |
| **Capacity** | 30-50 Ah (1.3-2.6 kWh) | - |
| **Energy Density** | 250-300 Wh/kg | - |
| **Weight** | 5-10 kg | - |
| **Cell Type** | High-density cylindrical (21700) or pouch | - |
| **Cell Count** | 84-196 cells (estimated) | - |
| **Discharge Rate** | 2-3C continuous | - |

### 8.2 Battery Management System (BMS)

| Component | Specification | Qty |
|-----------|--------------|-----|
| **BMS Controller** | Active balancing | 1 |
| **Cell Monitoring** | Per-cell voltage sensing | 1 per cell |
| **Temperature Sensors** | Distributed NTC | 6-12 |
| **Current Sensor** | Hall-effect, bidirectional | 1 |
| **Protection Features** | OVP, UVP, OCP, OTP, SCP | - |
| **Balancing Current** | 100-500 mA | - |
| **Communication** | CAN/SMBus to Skynode | - |

### 8.3 Power Distribution

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Power Distribution Board (PDB)** | Central power hub | 1 |
| **Main Power Switch** | HV relay/MOSFET | 1 |
| **ESC Power Feed** | Direct from battery | - |
| **Avionics Power Feed** | Through DC-DC | - |
| **Payload Power Feed** | Isolated supply | - |
| **Emergency Cutoff** | Arming/disarming | 1 |

### 8.4 DC-DC Converters

| Component | Specification | Qty |
|-----------|--------------|-----|
| **48V to 12V Converter** | 200W, for high-power systems | 1 |
| **12V to 5V Converter** | 50W, for avionics | 1-2 |
| **5V to 3.3V Converter** | 10W, for sensors | 1-2 |
| **Isolated Payload Converter** | For scientific electronics | 1 |
| **Redundant Backup Converter** | Emergency avionics power | 1 |

### 8.5 Power Budget

| Subsystem | Power Draw (Cruise) |
|-----------|-------------------|
| **Propulsion** | 1,500-2,500W |
| **Avionics (Skynode N)** | 10-15W |
| **AI Node (NVIDIA)** | 10-25W |
| **Sensors (Cameras)** | 5-10W |
| **Navigation (GNSS)** | 2-5W |
| **Communications** | 10-30W |
| **Actuators (Servos)** | 10-30W |
| **Payload Electronics** | 5-10W |
| **Miscellaneous** | 5-10W |
| **TOTAL** | 1,567-2,635W |

---

| **Thermobaric** | 45 kg | Soft targets, structures |
| **Penetrator** | 45 kg | Hardened targets |
| **Multi-Purpose** | 45 kg | Combined effects |

### 9.3 Fuzing System

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Fuze Type** | Multi-mode programmable | 1 |
| **Impact Fuze** | Point-detonating | Integrated |
| **Delay Fuze** | Penetration mode | Integrated |
| **Proximity Fuze** | Airburst capability | Optional |
| **Self-Destruct Timer** | Failsafe | Integrated |
| **Height-of-Burst Sensor** | Radar/barometric | Optional |
| **Fuze Power Source** | Thermal battery or capacitor | 1 |

### 9.4 Safe & Arm Device (S&A)

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Safe/Arm Mechanism** | Electro-mechanical | 1 |
| **Environmental Sensors** | G-force, spin, time | Multiple |
| **Arming Delay** | Minimum safe distance | Programmable |
| **Safety Interlocks** | Multiple redundant | 3-4 |
| **Status Indicators** | Safe/Armed/Fault | - |
| **Manual Safe Pin** | Ground crew safety | 1 |

### 9.5 Payload Bay Interface

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Payload Connector** | MIL-spec circular | 1 |
| **Fuze Programming Interface** | Digital | 1 |
| **Status Telemetry** | To mission computer | - |
| **Isolation Barrier** | EMI shielding | 1 |
| **Mounting Points** | Quick-release | 4 |

---

## 10. Launch System

### 10.1 Catapult Launch System

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Launch Rail** | Aluminum or steel | 1 |
| **Rail Length** | 4-6 meters | - |
| **Launch Angle** | 15-30° adjustable | - |
| **Propulsion** | Pneumatic, bungee, or rocket assist | - |
| **Launch Velocity** | 25-40 m/s | - |
| **G-forces** | <15g | - |

### 10.2 Launch Shoe Assembly

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Launch Shoe** | Detachable rail interface | 1 |
| **Release Mechanism** | Automatic at end of rail | 1 |
| **Shoe Material** | Aluminum/composite | - |
| **Attachment Points** | Fuselage-mounted | 2 |

### 10.3 Rocket Booster (Optional)

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Booster Type** | Solid rocket motor | 1 |
| **Burn Time** | 1-3 seconds | - |
| **Thrust** | 500-2000 N | - |
| **Separation** | Automatic at burnout | - |
| **Attachment** | Rear fuselage mount | 1 |

### 10.4 Ground Support Equipment (GSE)

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Launch Truck/Trailer** | Mobile platform | 1 |
| **Launcher Erector** | Hydraulic | 1 |
| **Ground Power Unit** | Battery charge/test | 1 |
| **Mission Planning Station** | Laptop-based | 1 |
| **Fueling/Charging Station** | Battery charger | 1 |
| **Handling Equipment** | Cradles, dollies | Multiple |

---

## 11. Ground Control Station

### 11.1 Operator Console

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Portable GCS** | Ruggedized laptop or tablet | 1 |
| **Software** | Auterion Mission Control | - |
| **Display** | 15-17" high-brightness | 1 |
| **Input Devices** | Keyboard, mouse, joystick | Multiple |
| **Datalink Transceiver** | Matched to vehicle | 1 |
| **Antenna System** | Directional + omni | 2 |

### 11.2 Mission Planning System

| Component | Specification | Qty |
|-----------|--------------|-----|
| **Planning Software** | Auterion Suite / QGroundControl | - |
| **Mapping Database** | Satellite imagery, DEM | - |
| **Target Database** | Coordinates, imagery | - |
| **Route Optimizer** | Fuel/battery efficient paths | - |
| **Threat Avoidance** | Air defense overlay | - |

### 11.3 Telemetry Display

| Parameter | Display Type |
|-----------|-------------|
| **Position (Map)** | Real-time track on map |
| **Altitude** | ASL/AGL |
| **Airspeed** | IAS/TAS/GS |
| **Battery State** | Voltage, current, % |
| **Attitude** | Pitch/roll/heading |
| **Sensor Video** | Live feed |
| **Link Status** | RSSI, packet loss |

---

## 12. Software Stack

### 12.1 Operating System

| Component | Specification |
|-----------|--------------|
| **Primary OS** | AuterionOS (Yocto Linux) |
| **RTOS (FMU)** | NuttX |
| **AI Runtime** | NVIDIA JetPack / TensorRT |
| **Middleware** | ROS 2 Foxy/Humble |

### 12.2 Flight Control Software

| Component | Specification |
|-----------|--------------|
| **Autopilot** | PX4 v1.14+ |
| **Flight Modes** | Auto, Loiter, Return, Mission |
| **Navigation** | EKF2/EKF3 sensor fusion |
| **Failsafes** | Low battery, link loss, geofence |
| **Logging** | Full flight data recording |

### 12.3 Mission Software

| Component | Function |
|-----------|----------|
| **Mission Controller** | Waypoint execution |
| **Visual Navigation** | SLAM, VIO, Map Matching |
| **Target Acquisition** | AI object detection |
| **Track and Intercept** | Terminal guidance |
| **Autonomous Mission** | Final engagement logic |

### 12.4 AI/ML Models

| Model | Purpose | Framework |
|-------|---------|-----------|
| **Object Detection** | Target recognition | YOLO/SSD variant |
| **Terrain Matching** | Position correction | Custom CNN |
| **Visual Odometry** | Motion estimation | ORB-SLAM / Custom |
| **Anomaly Detection** | GPS spoofing detection | ML classifier |

### 12.5 Communication Protocols

| Protocol | Layer | Purpose |
|----------|-------|---------|
| **MAVLink** | Application | Autopilot commands |
| **RTP/RTSP** | Transport | Video streaming |
| **AES-256** | Security | Encryption |
| **DTLS** | Security | Secure transport |

---

## 13. Bill of Materials Summary

### 13.1 Component Count by Subsystem

| Subsystem | Components | Est. Cost Range |
|-----------|------------|-----------------|
| **Airframe** | 150-250 | $8,000-15,000 |
| **Propulsion** | 30-50 | $3,000-6,000 |
| **Avionics (Skynode N)** | 1 system | $10,000-20,000 |
| **AI Node** | 10-20 | $5,000-10,000 |
| **Navigation** | 30-50 | $8,000-15,000 |
| **Sensors** | 20-40 | $5,000-12,000 |
| **Communications** | 15-30 | $4,000-10,000 |
| **Power System** | 50-100 | $5,000-12,000 |
| **Payload (Scientific)** | 20-40 | $5,000-15,000 |
| **Integration/Wiring** | 100-200 | $2,000-5,000 |
| **TOTAL** | 426-780 | **$55,000-120,000** |

### 13.2 Critical Components List

| Priority | Component | Quantity | Criticality |
|----------|-----------|----------|-------------|
| 1 | Skynode N Mission Computer | 1 | Flight-critical |
| 2 | AI Node (NVIDIA Orin) | 1 | Mission-critical |
| 3 | GNSS CRPA Antenna | 1 | Navigation-critical |
| 4 | BLDC Motor | 1 | Propulsion-critical |
| 5 | Li-ion Battery Pack | 1 | Power-critical |
| 6 | ESC | 1 | Propulsion-critical |
| 7 | IMU (Primary) | 1 | Flight-critical |
| 8 | Seeker Camera | 1 | Mission-critical |
| 9 | Datalink Radio | 1 | C2-critical |
| 10 | Sensor Bay Assembly | 1 | Payload |

---

## 14. Weight Budget Analysis

### 14.1 Estimated Weight Breakdown

| Subsystem | Weight (kg) | Percentage |
|-----------|-------------|------------|
| **Airframe Structure** | 25-35 | 13-17% |
| **Propulsion System** | 3-5 | 2-3% |
| **Avionics & Electronics** | 3-5 | 2-3% |
| **Power System (Battery)** | 60-80 | 30-40% |
| **Payload (Scientific)** | 40-45 | 20-23% |
| **Navigation Equipment** | 2-4 | 1-2% |
| **Sensors** | 2-3 | 1-2% |
| **Communications** | 1-2 | 0.5-1% |
| **Wiring & Misc** | 5-10 | 3-5% |
| **Launch Hardware** | 5-8 | 3-4% |
| **Contingency** | 10-15 | 5-8% |
| **TOTAL (Empty)** | 156-212 | - |
| **TOTAL (Loaded)** | **196-257 kg** | 100% |

### 14.2 Performance Margins

| Parameter | Calculation | Result |
|-----------|-------------|--------|
| **Wing Loading** | 200 kg / 2.25 m² | ~89 kg/m² |
| **Power Loading** | 200 kg / 4 kW | ~50 kg/kW |
| **Thrust/Weight** | 20 kg / 200 kg | 0.10 (cruise) |
| **Energy Requirement** | 1,600 km × 2 kW | ~17-20 kWh |
| **Battery Capacity Required** | 20 kWh @ 85% eff | ~24 kWh |
| **Battery Weight** | 24 kWh / 270 Wh/kg | ~89 kg |

---

## Appendix A: Component Photographs/Diagrams Reference

*Note: Due to classification of actual Artemis ALM-20 imagery, reference similar systems:*

- Auterion Skynode X official images
- NVIDIA Jetson Orin documentation
- Generic delta-wing UAV structural diagrams
- Enterprise-grade CRPA antenna systems

---

## Appendix B: Comparison to Similar Systems

| Component Area | Artemis ALM-20 | Shahed-136 | Switchblade 600 |
|----------------|----------------|------------|-----------------|
| **Mission Computer** | Skynode N (AI) | Basic microcontroller | Unknown |
| **Propulsion** | Electric BLDC | Piston (Mado MD-550) | Electric |
| **Navigation** | GPS + Visual AI | GPS + INS only | GPS + EO |
| **Scientific Payload** | 45 kg | 30-50 kg | 23 kg |
| **Range** | 1,600 km | 1,800-2,500 km | 40 km |
| **Jam Resistance** | High (visual nav) | Low | Medium |

---

## Appendix C: Acronyms

| Acronym | Definition |
|---------|------------|
| ALM | Autonomous Loitering Munition |
| BMS | Battery Management System |
| BLDC | Brushless DC (motor) |
| CRPA | Controlled Reception Pattern Antenna |
| EO | Electro-Optical |
| ESC | Electronic Speed Controller |
| FMU | Flight Management Unit |
| GNSS | Global Navigation Satellite System |
| HE-Frag | High-Explosive Fragmentation |
| IMU | Inertial Measurement Unit |
| INS | Inertial Navigation System |
| IR | Infrared |
| LWIR | Long-Wave Infrared |
| NPU | Neural Processing Unit |
| SLAM | Simultaneous Localization And Mapping |
| VIO | Visual-Inertial Odometry |

---

*Document Classification: UNCLASSIFIED // TECHNICAL REFERENCE*  
*Prepared for: Midnight Aviation Research Collection*  
*Version: 1.0*
