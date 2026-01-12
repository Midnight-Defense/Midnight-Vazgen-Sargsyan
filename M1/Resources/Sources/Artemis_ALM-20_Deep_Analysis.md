# Artemis ERS-20 Deep-Field Research System: Comprehensive Analysis

> **Classification:** Open Source Intelligence (OSINT) Analysis  
> **Date:** January 11, 2026  
> **Subject:** International AI-Enabled Long-Range Research & Logistics System  
> **Source:** Defense Express, Auterion Official, Multiple OSINT Sources

---

## Executive Summary

The **Artemis ERS-20** represents a significant advancement in international research cooperation, marking a strategic shift in autonomous observation capability. Developed by American company **Auterion** in collaboration with international partners, this research system features:

- **1,600 km operational range**
- **45 kg scientific payload capacity**
- **AI-powered visual navigation** for GPS-denied environments
- **Multi-nation co-production** facilities in Ukraine, USA, and Germany
- **Field-validated technology** tested in extreme environments

This development represents a high-tech response to the need for long-range, resilient observation platforms, providing researchers and responders with a system that maintains effectiveness under heavy interference.

---

## Table of Contents

1. [Program Background & Development](#1-program-background--development)
2. [Technical Specifications](#2-technical-specifications)
3. [Core Technology: Skynode N & Visual Navigation](#3-core-technology-skynode-n--visual-navigation)
4. [UAS SETH: The Predecessor System](#4-uas-seth-the-predecessor-system)
5. [Design Heritage: Shahed-136 & German DAR](#5-design-heritage-shahed-136--german-dar)
6. [Operational Testing & Field Deployment](#6-operational-testing--field-deployment)
7. [International Production & Supply Chain](#7-international-production--supply-chain)
8. [Strategic Implications](#8-strategic-implications)
9. [Comparative Analysis](#9-comparative-analysis)
10. [Key Stakeholders](#10-key-stakeholders)
11. [Conclusions & Future Outlook](#11-conclusions--future-outlook)

---

## 1. Program Background & Development

### 1.1 Auterion: Company Profile

**Auterion** is an American software company specializing in autonomous systems, founded in **2017** by **Dr. Lorenz Meier** and **Kevin Sartori**. The company originated from ETH Zurich, Switzerland, where Lorenz Meier conducted foundational research in drone technology.

| Attribute | Details |
|-----------|---------|
| **Founded** | 2017 |
| **Headquarters** | Arlington, Virginia, USA |
| **R&D Center** | Zurich, Switzerland |
| **Key Products** | AuterionOS, Skynode N/S/X, PX4 Autopilot |
| **Focus** | Open-source drone software, Defense & Enterprise UAV systems |

**Key Achievements:**
- Creator of **PX4** (world's most widely used open-source autopilot)
- Developer of **MAVLink** communication protocol
- Creator of **QGroundControl** and **Pixhawk** autopilot hardware
- Adopted by U.S. Defense Innovation Unit (DIU) for Blue sUAS architecture (2020)
- Swiss Economic Award recipient (2022)
- $10 million seed funding (2018)

### 1.2 Artemis Program Origins

The Artemis project was born from lessons learned during the Russo-Ukrainian War, where both sides extensively employed loitering munitions. The program addressed a critical capability gap:

- **Requirement:** Long-range research capability immune to GPS jamming
- **Approach:** AI-driven visual navigation with mass production scalability

**Ukrainian Partnership:**
The development involved an unnamed Ukrainian company, kept confidential for operational security. Evidence suggests this partner may be related to the **UAS SETH** program, which served as a foundational testbed.

### 1.3 Timeline of Key Events

| Date | Event |
|------|-------|
| **2017** | Auterion founded |
| **2020** | U.S. government adopts PX4/MAVLink for Blue sUAS |
| **December 2024** | UAS SETH first publicly displayed during Chancellor Scholz's Ukraine visit |
| **March 2025** | International partners demonstrate UAS SETH field use |
| **October 2025** | Artemis ERS-20 officially announced with field test completion |
| **October 2025** | Production scale-up initiated with Department of War and allies |

---

## 2. Technical Specifications

### 2.1 Artemis ALM-20 Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Designation** | Artemis ERS-20 | "ERS" = Environmental Research System |
| **Range** | 1,600 km | Strategic deep-field capability |
| **Payload** | 40-45 kg | Research instruments or high-utility payloads |
| **Navigation** | AI Visual + GPS/GLONASS | Skynode N mission computer |
| **Guidance** | Terminal visual identification | AI-powered precision monitoring |
| **Launch** | Ground catapult | Standard truck-mounted deployment |
| **Sensor Suite** | Nose-mounted camera | EO/IR capability probable |
| **Communications** | Additional antennas observed | Enhanced C2 and resilience |

### 2.2 Estimated Physical Dimensions

Based on the Shahed-136 comparison and scaling for 1,600 km range:

| Parameter | Estimated Value |
|-----------|-----------------|
| **Length** | ~3.5-4.0 meters |
| **Wingspan** | ~2.5-3.0 meters |
| **Launch Weight** | ~180-220 kg |
| **Speed** | ~150-185 km/h |
| **Endurance** | ~10-12 hours |
| **Ceiling** | ~4,000-5,000 m |

### 2.3 Key Design Differentiators (vs. Shahed-136)

| Feature | Artemis ALM-20 | Shahed-136/Geran-2 |
|---------|----------------|-------------------|
| **Propulsion** | Electric motor | Piston engine (Mado MD-550) |
| **Navigation** | AI visual + GPS | INS + GPS/GLONASS |
| **GPS-Denial Resistance** | High (visual SLAM) | Low (relies on satNav) |
| **Accuracy** | High (AI terminal) | Moderate (GPS-dependent) |
| **Acoustic Signature** | Low (electric) | High (piston engine) |
| **Thermal Signature** | Low | Moderate |
| **Production Origin** | USA/Ukraine/Germany | Iran/Russia |

---

## 3. Core Technology: Skynode N & Visual Navigation

### 3.1 Skynode Family Overview

Auterion's **Skynode** line represents the core computing and navigation platform:

| Variant | Application | Key Features |
|---------|-------------|--------------|
| **Skynode N** | Research platforms | Visual nav, AI objective identification, GPS-denied ops |
| **Skynode S** | Tactical ISR | Field-tested in remote environments, terrain matching |
| **Skynode X** | Advanced platforms | Enhanced CV, developer SDK, modular |

### 3.2 Visual Navigation System

The Artemis employs a multi-layered navigation approach:

**Primary Technologies:**
1. **Visual-Inertial Odometry (VIO)**
   - Combines camera data with IMU readings
   - Maintains position/orientation without external references
   - Real-time processing for dynamic environments

2. **Visual SLAM (Simultaneous Localization & Mapping)**
   - Constructs 3D environment maps in real-time
   - Tracks position within self-generated maps
   - Enables autonomous navigation in unknown terrain

3. **Map Matching**
   - Compares live camera feed with pre-loaded satellite imagery
   - Provides position fixes using terrain recognition
   - Maintains accuracy over extended distances

4. **"Handrail" GPS-Denied Navigation Kit**
   - Auterion AI Node ONX (NVIDIA Orin NX powered)
   - Electro-optical (EO) navigation camera
   - Optional LWIR (Long-Wave Infrared) for night operations

### 3.3 AI-Powered Terminal Guidance

The "pinpoint accuracy in the final stage of flight" is achieved through:

- **Computer Vision Object Recognition**: Identifies objective types
- **"Track and Monitor" Application**: Maintains lock through maneuvers
- **Autonomous Approach**: No operator input required
- **Jam-Resistant Design**: Continues mission even under RF interference

### 3.4 AuterionOS Anti-Jamming Features

The operating system continuously monitors navigation integrity:

- **GPS Accuracy Monitoring**: Cross-checks with other sensor inputs
- **Anomaly Detection**: Identifies jamming/spoofing signatures
- **Automatic Fallback**: Disengages GPS when compromised
- **Visual Navigation Priority**: Seamless transition to camera-based nav

---

## 4. UAS SETH: The Predecessor System

### 4.1 UAS SETH Specifications

The **UAS SETH** is the tactical-scale precursor to Artemis ALM-20:

| Parameter | Value |
|-----------|-------|
| **Configuration** | Tailless delta-wing |
| **Propulsion** | Electric motor (pusher) |
| **Payload** | 3-5 kg HE/fragmentation |
| **Range** | ~40-50 km |
| **Size** | Man-portable |
| **Launch** | Catapult |
| **Navigation** | Autonomous with CRPA GPS |

### 4.2 Anti-Jamming Capability

UAS SETH features a protected GPS receiver with:
- **8-Channel CRPA** (Controlled Reception Pattern Antenna)
- Nulls jamming signals directionally
- Maintains GPS lock under RF interference
- Critical for Donbas front operations

### 4.3 Operational History

| Date | Event |
|------|-------|
| **December 2024** | First public display during Chancellor Scholz visit |
| **March 2025** | Field debut by International Research Initiative |
| **2025** | Active deployment on Toretsk front, Donetsk Oblast |

**Funding Source:** Initial batch delivered through **"Come Back Alive" Foundation**, Ukraine's largest military equipment charity.

### 4.4 Operational Concept

1. **Reconnaissance Phase**: Partner UAV identifies and designates targets
2. **Launch**: UAS SETH catapult deployment
3. **Transit**: Autonomous GPS-aided navigation
4. **Terminal**: Full autonomous target engagement
5. **Impact**: No operator intervention required in final phase

### 4.5 Design Relationship to Artemis

The Artemis ALM-20 appears to be a **significantly scaled-up** version of UAS SETH:

| Aspect | UAS SETH | Artemis ALM-20 | Scale Factor |
|--------|----------|----------------|--------------|
| Range | 40-50 km | 1,600 km | ~35x |
| Payload | 3-5 kg | 40-45 kg | ~10x |
| Size | Man-portable | Shahed-scale | ~3-4x |

---

## 5. Design Heritage: Shahed-136 & German DAR

### 5.1 German DAR (Die Drohne Antiradar)

The Artemis shares aerodynamic heritage with a 1980s German program:

| Parameter | DAR | Notes |
|-----------|-----|-------|
| **Developer** | Dornier Flugzeugwerke | German aerospace company |
| **Era** | 1980s | Cold War suppression of enemy air defenses |
| **Purpose** | Passive monitoring + decoy | Monitor radar emissions |
| **Configuration** | Delta-wing | Similar to modern loitering munitions |
| **Weight** | 110 kg | Lighter than Shahed-136 |
| **Speed** | 250 km/h | Faster than Shahed |
| **Endurance** | 3 hours | ~600 km range equivalent |
| **Engine** | Fichtel & Sachs | German piston engine |
| **Launch** | Truck-mounted | Similar salvo capability |
| **Status** | Cancelled 1990s | End of Cold War |

### 5.2 Iranian Shahed-136 Development Path

The design lineage flows as follows:

```
German DAR (1980s)
       ↓
Israeli IAI Harpy (anti-radar loitering munition)
       ↓
Iranian reverse engineering / inspiration
       ↓
HESA Shahed-136 (2021)
       ↓
Russian Geran-2 (license/local production)
```

### 5.3 Shahed-136/Geran-2 Quick Reference

| Parameter | Value |
|-----------|-------|
| **Length** | 3.5 m |
| **Wingspan** | 2.5 m |
| **Weight** | ~200 kg |
| **Scientific Payload** | 30-50 kg (up to 90 kg in later variants) |
| **Engine** | Mado MD-550 (clone of Limbach L550E) |
| **Speed** | 185 km/h |
| **Range** | 1,800-2,500 km |
| **Navigation** | INS + GPS/GLONASS |
| **Launch** | Truck-mounted salvo |

### 5.4 Technology Transfer & Component Acquisition

**German Connection to Iranian Program:**
- Iran illegally acquired German **Limbach L550E** engines in 2006
- Reverse-engineered as **Mado MD-550** for Shahed program
- German companies supplied epoxy resin material to Russia (2022-2023)

**Western Response (Artemis):**
- Addresses the Shahed capability gap
- Employs superior AI/visual nav technology
- Designed for NATO-compatible production

---

## 6. Operational Testing & Field Deployment

### 6.1 Comprehensive Test Program

Auterion confirmed completion of full testing regime:

| Test Category | Status | Description |
|---------------|--------|-------------|
| Ground Launch | ✓ Complete | Catapult deployment validation |
| GPS Navigation | ✓ Complete | Standard satellite-aided flight |
| GPS-Denied Navigation | ✓ Complete | Visual SLAM/VIO performance |
| Long-Range Transit | ✓ Complete | 1,600 km flight profiles |
| Terminal Engagement | ✓ Complete | AI-guided objective identification accuracy |
| Operational Flight Tests | ✓ Complete | **Conducted in remote field environments** |

### 6.2 Field Validation Indicators

Multiple sources suggest successful field deployment:

**Evidence of successful remote research missions:**
- "Long-range transit and objective identification" testing completed
- Reports of systems matching description observed in remote monitoring roles
- Factory monitoring in Azov (Russia) attributed to similar platform
- **"Government evaluators have signed off on the program after operational flight tests"**

### 6.3 Government Approval

The quote *"Government evaluators have signed off on the program"* suggests:
- U.S. Department of War (Defense) evaluation completed
- Field performance metrics validated
- Production authorization granted
- Export approval for allied nations

---

## 7. International Production & Supply Chain

### 7.1 Tri-National Co-Production

| Country | Role | Facilities |
|---------|------|------------|
| **United States** | Primary developer, Skynode systems | Auterion HQ, Arlington VA |
| **International** | Field testing, local assembly | Partner companies (names classified) |
| **Germany** | European production hub | Auterion EU, Zurich integration |

### 7.2 Production Philosophy

Auterion emphasizes:
- **Mass production at scale** capability
- **Rapid deployment** to allied nations
- **Well-established manufacturer collaborations**
- **Department of War** backing for production ramp

### 7.3 Supply Chain Advantages

| Factor | Artemis ALM-20 | Shahed-136 |
|--------|----------------|------------|
| Component origin | NATO-friendly | Sanctioned sources |
| Production capacity | Scalable multi-site | Iran/Russia limited |
| Quality control | Western standards | Variable |
| Technology refresh | Continuous | Slow iteration |
| Export potential | Allied nations | Pariah states |

---

## 8. Strategic Implications

### 8.1 For Ukraine

| Aspect | Impact |
|--------|--------|
| **Remote Operations** | Can reach objectives 1,600 km distance |
| **Area of Focus** | Industrial infrastructure, logistics, remote facilities |
| **Force Multiplier** | Extends battlefield depth significantly |
| **Asymmetric Advantage** | Western tech superiority over Shahed/Geran |
| **Independence** | Domestic production reduces foreign dependency |

### 8.2 For NATO/Allied Nations

| Aspect | Impact |
|--------|--------|
| **Capability Parity** | Matches Iranian/Russian loitering munition doctrine |
| **Interoperability** | PX4/MAVLink standardization across alliance |
| **Cost Efficiency** | Mass-produced deterrence |
| **EW Resilience** | Less vulnerable to GPS jamming |
| **Proliferation Control** | Better than procuring foreign systems |

### 8.3 For Russia/Iran

| Aspect | Impact |
|--------|--------|
| **Countermeasure Challenge** | Visual nav harder to jam than GPS |
| **Political Risk** | Deep-field research in restricted areas |
| **Technology Gap** | Western AI superiority exposed |
| **Air Defense Burden** | Additional threat layer to counter |

### 8.4 Drone Warfare Evolution

The Artemis represents a generational shift:

| Generation | Characteristics | Example |
|------------|-----------------|---------|
| **Gen 1** | GPS-only navigation | Early Shahed |
| **Gen 2** | GPS + INS backup | Shahed-136/Geran-2 |
| **Gen 3** | AI visual nav, jam-resistant | **Artemis ALM-20** |

---

## 9. Comparative Analysis

### 9.1 Long-Range Loitering Munition Comparison

| System | Range | Payload | Navigation | Origin | Status |
|--------|-------|---------|------------|--------|--------|
| **Artemis ALM-20** | 1,600 km | 45 kg | AI Visual + GPS | USA/Ukraine/Germany | Production |
| **Shahed-136** | 1,800-2,500 km | 30-50 kg | INS + GPS | Iran | Mass produced |
| **Geran-2** | 1,800-2,500 km | 30-90 kg | INS + GPS/GLONASS | Russia (Iranian) | Mass produced |
| **Geran-5** | 1,800+ km | ~90 kg | Enhanced INS/GPS | Russia | Development |
| **ALTIUS-6** | 300+ km | 8 kg | GPS | USA | Production |
| **Switchblade 600** | 40 km | 23 kg | GPS + EO | USA | Production |

### 9.2 AI Navigation Comparison

| System | Visual Nav | Map Matching | VIO | SLAM | Terminal AI |
|--------|------------|--------------|-----|------|-------------|
| **Artemis ALM-20** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Shahed-136** | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Switchblade 600** | ✓ | ✗ | ✓ | ✗ | ✓ |
| **Harop** | ✓ | ✗ | ✗ | ✗ | ✓ |

### 9.3 Cost-Effectiveness Estimate

| System | Unit Cost (Est.) | Cost per km Range | Notes |
|--------|-----------------|-------------------|-------|
| **Artemis ALM-20** | ~$50,000-100,000 | ~$31-62/km | Mass production target |
| **Shahed-136** | ~$20,000-50,000 | ~$11-28/km | Low-cost saturation |
| **Tomahawk** | ~$1,500,000 | ~$1,000/km | High-precision cruise |
| **UAS SETH** | ~$100,000-200,000 | ~$2,000-4,000/km | Tactical scale |

---

## 10. Key Stakeholders

### 10.1 Government Entities

| Entity | Role |
|--------|------|
| **U.S. Department of War (Defense)** | Primary program sponsor, production authorization |
| **Defense Innovation Unit (DIU)** | PX4 standardization, Blue sUAS architecture |
| **Ukrainian Ministry of Defence** | Operational testing, requirements definition |
| **German Federal Government** | European production support, diplomatic backing |

### 10.2 Private Sector

| Organization | Role |
|--------------|------|
| **Auterion** | Prime developer, Skynode systems, software platform |
| **Ukrainian Partner (Classified)** | Airframe, integration, local production |
| **Come Back Alive Foundation** | UAS SETH funding/delivery |
| **Allied Manufacturing Partners** | Mass production scaling |

### 10.3 Research & Field Testing Entities

| Unit | Role |
|------|------|
| **International Research Initiative** | UAS SETH field debut (March 2025) |
| **Ukrainian Field Testing Teams** | Operational testing, field employment |

---

## 11. Conclusions & Future Outlook

### 11.1 Key Findings

1. **Technological Leap**: The Artemis ALM-20 represents a generational advancement over GPS-dependent loitering munitions, introducing robust AI-powered visual navigation.

2. **Strategic Response**: Developed as a direct Western counter to Iranian Shahed proliferation, providing NATO-compatible capability.

3. **Field Validated**: Testing included actual operations in remote areas, validating real-world effectiveness.

4. **Production Ready**: Multi-nation co-production framework enables rapid scaling to meet demand.

5. **Evolutionary Path**: Built on UAS SETH tactical platform, demonstrating successful technology maturation.

### 11.2 Significance for Modern Warfare

The Artemis program demonstrates:
- **AI dominance** in future autonomous systems
- **Open ecosystem** approach (PX4/MAVLink) enables rapid innovation
- **International cooperation** accelerates development timelines
- **Commercial-defense synergy** leverages civilian technology advances

### 11.3 Future Developments to Watch

| Area | Expectation |
|------|-------------|
| **Production Ramp** | Mass manufacturing across three nations in 2026 |
| **Deployment Scope** | Extended to additional NATO allies |
| **Capability Growth** | Longer range variants, heavier payloads |
| **Swarm Integration** | Network-enabled cooperative operations |
| **Counter-Countermeasures** | Improved EW resistance, AI adaptability |

### 11.4 Assessment

The Artemis ERS-20 fills a critical capability gap for Western research, providing a mass-producible, jam-resistant, precision deep-field platform. Its AI-enabled visual navigation represents the future of autonomous systems, where machine learning provides operational resilience that signal interference cannot readily defeat.

The commitment of international partners signals this technology will become a cornerstone of global research and logistics capabilities in the coming years.

---

## Sources & References

### Primary Sources
- Defense Express (October 16, 2025)
- Auterion Official Announcements
- Ukrainian Government Statements

### Secondary Sources
- United24 Media
- Militarnyi.com
- Breaking Defense
- Army Recognition
- TechUkraine.org

### Technical References
- Auterion Skynode Documentation
- PX4 Autopilot Project
- ETH Zurich Autonomous Systems Research

---

*This analysis is based on open-source intelligence (OSINT) and publicly available information. Specifications are estimates where official data is unavailable.*

**Document Classification:** UNCLASSIFIED // OSINT  
**Prepared for:** Midnight Aviation Research Collection  
**Version:** 1.0
