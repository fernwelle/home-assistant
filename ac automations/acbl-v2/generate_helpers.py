#!/usr/bin/env python3
"""
Generate ACBL v2 helpers for all 17 AC units.
Outputs:
  - helpers_input_select.yaml   (ac_mode per unit)
  - helpers_input_number.yaml   (target_temp, high_temp, min_off, qc baselines per unit)
  - helpers_input_datetime.yaml (start_time, end_time, last_off per unit)
  - helpers_input_boolean.yaml  (pre_outage_state per unit)
  - helpers_timer.yaml          (quick_cool timer per unit)
  - automations_from_blueprint.yaml (blueprint instances for all 17 units)
"""

import os

# ── Unit definitions ──────────────────────────────────────
# (suffix, display_name, temp_sensor, humidity_sensor, default_start, default_end, default_target, default_high, default_min_off)
units = [
    # V1
    ("v1_master",   "V1 Master",   "sensor.homenode_sense_temp_v1_master_bme280_temperature", "sensor.homenode_sense_temp_v1_master_bme280_humidity", "19:00:00", "05:00:00", 24.0, 27.5, 3),
    ("v1_raam",     "V1 Raam",     "sensor.temp_v1_raam_temperature",    "sensor.temp_v1_raam_humidity",    "19:00:00", "05:00:00", 24.5, 27.5, 3),
    ("v1_radhha",   "V1 Radhha",   "sensor.temp_v1_radhha_zb_temperature", "sensor.temp_v1_radhha_zb_humidity", "19:00:00", "05:00:00", 24.0, 27.0, 3),
    ("v1_yoga",     "V1 Yoga",     "none",                               "none",                             "19:00:00", "05:00:00", 24.0, 26.0, 3),
    # V2
    ("v2_study",    "V2 Study",    "none", "none", "19:00:00", "05:00:00", 24.0, 26.0, 3),
    ("v2_sk",       "V2 SK",       "none", "none", "19:00:00", "05:00:00", 24.0, 26.0, 3),
    ("v2_ck",       "V2 CK",       "none", "none", "19:00:00", "05:00:00", 24.0, 26.0, 3),
    # V3
    ("v3_master",   "V3 Master",   "none", "none", "19:00:00", "05:00:00", 24.0, 26.0, 3),
    ("v3_vrajraj",  "V3 Vrajraj",  "none", "none", "19:00:00", "05:00:00", 24.0, 26.0, 3),
    ("v3_dhaani",   "V3 Dhaani",   "none", "none", "19:00:00", "05:00:00", 24.0, 26.0, 3),
    ("v3_office",   "V3 Office",   "none", "none", "19:00:00", "05:00:00", 24.0, 26.0, 3),
    # V4 (non-inverter dining/living get longer min_off)
    ("v4_dining_1", "V4 Dining 1", "none", "none", "19:00:00", "05:00:00", 24.0, 26.0, 5),
    ("v4_dining_2", "V4 Dining 2", "none", "none", "19:00:00", "05:00:00", 24.0, 26.0, 5),
    ("v4_living_1", "V4 Living 1", "none", "none", "19:00:00", "05:00:00", 24.0, 26.0, 5),
    ("v4_living_2", "V4 Living 2", "none", "none", "19:00:00", "05:00:00", 24.0, 26.0, 5),
    ("v4_guest",    "V4 Guest",    "none", "none", "19:00:00", "05:00:00", 24.0, 26.0, 3),
    # V5
    ("v5_mandir",   "V5 Mandir",   "none", "none", "05:00:00", "21:00:00", 24.0, 26.0, 3),
]

OUT = "/home/claude/acbl-v2/generated"
os.makedirs(OUT, exist_ok=True)


# ══════════════════════════════════════════════════════════
# input_select — ac_mode per unit
# ══════════════════════════════════════════════════════════
lines = ["# ACBL v2 — AC Mode selectors (auto / quick_cool / off)", "input_select:"]
for suffix, name, *_ in units:
    lines.append(f"  ac_mode_{suffix}:")
    lines.append(f'    name: "AC Mode — {name}"')
    lines.append(f"    options:")
    lines.append(f"      - auto")
    lines.append(f"      - quick_cool")
    lines.append(f"      - off")
    lines.append(f"    initial: auto")
    lines.append(f'    icon: mdi:thermostat')
    lines.append("")

with open(f"{OUT}/helpers_input_select.yaml", "w") as f:
    f.write("\n".join(lines))


# ══════════════════════════════════════════════════════════
# input_number — target_temp, high_temp, min_off, qc baselines
# ══════════════════════════════════════════════════════════
lines = ["# ACBL v2 — Numeric helpers", "input_number:"]
for suffix, name, _, _, _, _, target, high, min_off in units:
    # target temp
    lines.append(f"  ac_target_temp_{suffix}:")
    lines.append(f'    name: "AC Target Temp — {name}"')
    lines.append(f"    min: 18")
    lines.append(f"    max: 30")
    lines.append(f"    step: 0.5")
    lines.append(f"    initial: {target}")
    lines.append(f'    unit_of_measurement: "°C"')
    lines.append(f'    icon: mdi:thermometer-low')
    lines.append("")
    # high temp
    lines.append(f"  ac_high_temp_{suffix}:")
    lines.append(f'    name: "AC ON Above — {name}"')
    lines.append(f"    min: 20")
    lines.append(f"    max: 38")
    lines.append(f"    step: 0.5")
    lines.append(f"    initial: {high}")
    lines.append(f'    unit_of_measurement: "°C"')
    lines.append(f'    icon: mdi:thermometer-high')
    lines.append("")
    # min off
    lines.append(f"  ac_min_off_{suffix}:")
    lines.append(f'    name: "AC Min OFF — {name}"')
    lines.append(f"    min: 1")
    lines.append(f"    max: 15")
    lines.append(f"    step: 1")
    lines.append(f"    initial: {min_off}")
    lines.append(f'    unit_of_measurement: "min"')
    lines.append(f'    icon: mdi:timer-sand')
    lines.append("")
    # qc baseline temp (automation-managed, hidden from dashboard)
    lines.append(f"  ac_qc_baseline_temp_{suffix}:")
    lines.append(f'    name: "QC Baseline Temp — {name}"')
    lines.append(f"    min: 0")
    lines.append(f"    max: 55")
    lines.append(f"    step: 0.1")
    lines.append(f"    initial: 0")
    lines.append(f'    icon: mdi:thermometer-chevron-down')
    lines.append("")
    # qc baseline humidity (automation-managed)
    lines.append(f"  ac_qc_baseline_humidity_{suffix}:")
    lines.append(f'    name: "QC Baseline Humidity — {name}"')
    lines.append(f"    min: 0")
    lines.append(f"    max: 100")
    lines.append(f"    step: 1")
    lines.append(f"    initial: 0")
    lines.append(f'    icon: mdi:water-percent')
    lines.append("")

with open(f"{OUT}/helpers_input_number.yaml", "w") as f:
    f.write("\n".join(lines))


# ══════════════════════════════════════════════════════════
# input_datetime — start_time, end_time, last_off
# ══════════════════════════════════════════════════════════
lines = ["# ACBL v2 — DateTime helpers", "input_datetime:"]
for suffix, name, _, _, start, end, *_ in units:
    lines.append(f"  ac_start_time_{suffix}:")
    lines.append(f'    name: "AC Start Time — {name}"')
    lines.append(f"    has_time: true")
    lines.append(f"    has_date: false")
    lines.append("")
    lines.append(f"  ac_end_time_{suffix}:")
    lines.append(f'    name: "AC End Time — {name}"')
    lines.append(f"    has_time: true")
    lines.append(f"    has_date: false")
    lines.append("")
    lines.append(f"  ac_last_off_{suffix}:")
    lines.append(f'    name: "AC Last OFF — {name}"')
    lines.append(f"    has_time: true")
    lines.append(f"    has_date: true")
    lines.append("")

with open(f"{OUT}/helpers_input_datetime.yaml", "w") as f:
    f.write("\n".join(lines))


# ══════════════════════════════════════════════════════════
# input_boolean — pre_outage_state
# ══════════════════════════════════════════════════════════
lines = ["# ACBL v2 — Pre-outage state booleans", "input_boolean:"]
for suffix, name, *_ in units:
    lines.append(f"  ac_pre_outage_{suffix}:")
    lines.append(f'    name: "AC Pre-Outage State — {name}"')
    lines.append(f"    initial: false")
    lines.append(f'    icon: mdi:power-plug-off-outline')
    lines.append("")

with open(f"{OUT}/helpers_input_boolean.yaml", "w") as f:
    f.write("\n".join(lines))


# ══════════════════════════════════════════════════════════
# timer — quick_cool per unit
# ══════════════════════════════════════════════════════════
lines = ["# ACBL v2 — Quick cool timers", "timer:"]
for suffix, name, *_ in units:
    lines.append(f"  ac_quick_cool_{suffix}:")
    lines.append(f'    name: "Quick Cool Timer — {name}"')
    lines.append(f"    duration: '01:00:00'")
    lines.append(f"    restore: true")
    lines.append(f'    icon: mdi:snowflake-alert')
    lines.append("")

with open(f"{OUT}/helpers_timer.yaml", "w") as f:
    f.write("\n".join(lines))


# ══════════════════════════════════════════════════════════
# Automation instances from blueprint
# ══════════════════════════════════════════════════════════
lines = ["# ACBL v2 — Blueprint automation instances for all 17 units", "automation:"]
for suffix, name, temp, humidity, start, end, target, high, min_off in units:
    alias = f"ACBL-{name.replace(' ', '-')}"
    lines.append(f'  - alias: "{alias}"')
    lines.append(f'    description: "ACBL v2 automation for {name}"')
    lines.append(f"    use_blueprint:")
    lines.append(f"      path: AC/acbl-v2.yaml")
    lines.append(f"      input:")
    lines.append(f"        ac_switch: switch.ac_{suffix}")
    lines.append(f"        power_sensor: sensor.ac_{suffix}_power")
    lines.append(f"        ac_mode: input_select.ac_mode_{suffix}")
    lines.append(f'        temperature_sensor: "{temp}"')
    lines.append(f'        humidity_sensor: "{humidity}"')
    lines.append(f"        power_source_sensor: sensor.villa_1_power_source")
    lines.append(f"        grid_stable_boolean: input_boolean.grid_power_stable")
    lines.append(f"        pre_outage_state: input_boolean.ac_pre_outage_{suffix}")
    lines.append(f"        target_temp_helper: input_number.ac_target_temp_{suffix}")
    lines.append(f"        high_temp_helper: input_number.ac_high_temp_{suffix}")
    lines.append(f"        start_time_helper: input_datetime.ac_start_time_{suffix}")
    lines.append(f"        end_time_helper: input_datetime.ac_end_time_{suffix}")
    lines.append(f"        last_off_helper: input_datetime.ac_last_off_{suffix}")
    lines.append(f"        min_off_helper: input_number.ac_min_off_{suffix}")
    lines.append(f"        quick_cool_timer: timer.ac_quick_cool_{suffix}")
    lines.append(f"        quick_cool_baseline_temp: input_number.ac_qc_baseline_temp_{suffix}")
    lines.append(f"        quick_cool_baseline_humidity: input_number.ac_qc_baseline_humidity_{suffix}")
    lines.append("")

with open(f"{OUT}/automations_from_blueprint.yaml", "w") as f:
    f.write("\n".join(lines))


# ══════════════════════════════════════════════════════════
# Summary
# ══════════════════════════════════════════════════════════
total_input_select = len(units)
total_input_number = len(units) * 5  # target, high, min_off, qc_baseline_temp, qc_baseline_humidity
total_input_datetime = len(units) * 3  # start, end, last_off
total_input_boolean = len(units)
total_timer = len(units)
total = total_input_select + total_input_number + total_input_datetime + total_input_boolean + total_timer

print(f"Generated ACBL v2 helpers for {len(units)} AC units:")
print(f"  input_select:   {total_input_select}")
print(f"  input_number:   {total_input_number}")
print(f"  input_datetime: {total_input_datetime}")
print(f"  input_boolean:  {total_input_boolean}")
print(f"  timer:          {total_timer}")
print(f"  TOTAL helpers:  {total}")
print(f"  automations:    {len(units)}")
print(f"\nFiles written to {OUT}/")
