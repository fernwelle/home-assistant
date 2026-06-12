type: vertical-stack
cards:
  - type: vertical-stack
    cards:
      - type: custom:mushroom-template-card
        entity: sensor.esp8266_mains_vs_grid_voltage_state
        primary: MAINS GRID STATE
        secondary: >
          {% set s = states('sensor.esp8266_mains_vs_grid_voltage_state') |
          upper %} {% if s == 'ON' %}
            ⚡ ON
          {% elif s == 'OFF' %}
            🔴 OFF
          {% else %}
            ⚠️ UNKNOWN
          {% endif %}
        icon: >
          {% set s = states('sensor.esp8266_mains_vs_grid_voltage_state') |
          upper %} {% if s == 'ON' %}
            mdi:flash
          {% elif s == 'OFF' %}
            mdi:power-plug-off
          {% else %}
            mdi:alert-circle-outline
          {% endif %}
        icon_color: >
          {% set s = states('sensor.esp8266_mains_vs_grid_voltage_state') |
          upper %} {% if s == 'ON' %} green {% elif s == 'OFF' %} red {% else %}
          grey {% endif %}
        tap_action:
          action: more-info
        card_mod:
          style: |
            @keyframes pulse {
              0% { opacity: 1; }
              50% { opacity: 0.4; }
              100% { opacity: 1; }
            }
            ha-card {
              border-radius: 12px;
              {% set s = states('sensor.esp8266_mains_vs_grid_voltage_state') | upper %}
              {% if s == 'OFF' %}
                background: rgba(255, 0, 0, 0.15);
                animation: pulse 1.2s infinite;
              {% elif s == 'ON' %}
                background: rgba(0, 200, 0, 0.12);
              {% elif s == 'UNKNOWN' %}
                background: rgba(150,150,150,0.15);
              {% endif %}
            }
            :host {
              {% set s = states('sensor.esp8266_mains_vs_grid_voltage_state') | upper %}
              {% if s == 'OFF' %}
                --ha-card-border-width: 2px;
                --ha-card-border-color: red;
              {% elif s == 'ON' %}
                --ha-card-border-width: 2px;
                --ha-card-border-color: green;
              {% elif s == 'UNKNOWN' %}
                --ha-card-border-width: 2px;
                --ha-card-border-color: grey;
              {% endif %}
            }
      - type: custom:mushroom-template-card
        entity: sensor.villa_1_power_source
        primary: SUPPLY SOURCE
        secondary: >
          {% set s = states('sensor.villa_1_power_source') | trim %} {% if s ==
          'grid' %}
            ⚡ GRID SUPPLY
          {% elif s == 'genset' %}
            🔌 GENSET SUPPLY
          {% elif s == 'panel_fault' %}
            🚨 PANEL FAULT
          {% elif s == 'no_power' %}
            🔴 NO SUPPLY
          {% else %}
            ⚠️ UNKNOWN
          {% endif %}
        icon: >
          {% set s = states('sensor.villa_1_power_source') | trim %} {% if s ==
          'grid' %}
            mdi:transmission-tower
          {% elif s == 'genset' %}
            mdi:engine
          {% elif s == 'panel_fault' %}
            mdi:alert-octagon
          {% elif s == 'no_power' %}
            mdi:power-plug-off
          {% else %}
            mdi:alert-circle-outline
          {% endif %}
        icon_color: >
          {% set s = states('sensor.villa_1_power_source') | trim %} {% if s ==
          'grid' %} green {% elif s == 'genset' %} orange {% elif s ==
          'panel_fault' %} amber {% elif s == 'no_power' %} red {% else %} grey
          {% endif %}
        tap_action:
          action: more-info
        card_mod:
          style: |
            @keyframes pulse {
              0% { opacity: 1; }
              50% { opacity: 0.4; }
              100% { opacity: 1; }
            }
            @keyframes fast-pulse {
              0% { opacity: 1; }
              25% { opacity: 0.3; }
              50% { opacity: 1; }
              75% { opacity: 0.3; }
              100% { opacity: 1; }
            }
            ha-card {
              border-radius: 12px;
              {% set s = states('sensor.villa_1_power_source') | trim %}
              {% if s == 'grid' %}
                background: rgba(0, 200, 0, 0.12);
              {% elif s == 'genset' %}
                background: rgba(255, 165, 0, 0.15);
              {% elif s == 'panel_fault' %}
                background: rgba(255, 191, 0, 0.2);
                animation: fast-pulse 0.8s infinite;
              {% elif s == 'no_power' %}
                background: rgba(255, 0, 0, 0.15);
                animation: pulse 1.2s infinite;
              {% else %}
                background: rgba(150,150,150,0.15);
              {% endif %}
            }
            :host {
              {% set s = states('sensor.villa_1_power_source') | trim %}
              {% if s == 'grid' %}
                --ha-card-border-width: 2px;
                --ha-card-border-color: green;
              {% elif s == 'genset' %}
                --ha-card-border-width: 2px;
                --ha-card-border-color: orange;
              {% elif s == 'panel_fault' %}
                --ha-card-border-width: 4px;
                --ha-card-border-color: #FFB300;
              {% elif s == 'no_power' %}
                --ha-card-border-width: 2px;
                --ha-card-border-color: red;
              {% else %}
                --ha-card-border-width: 2px;
                --ha-card-border-color: grey;
              {% endif %}
            }
      - type: markdown
        content: >
          **Current State Duration:** {{
          (states('sensor.grid_sense_previous_state_duration') | int) |
          timestamp_custom('%H:%M:%S', false) }}
        card_mod:
          style: |
            ha-card {
              background: transparent;
              border: none;
              box-shadow: none;
              padding: 2px 8px;
              font-size: 12px;
              color: #a0a3b1;
            }
  - type: markdown
    content: "**FLOOD LIGHTS**"
    card_mod:
      style: |
        ha-card {
          background: transparent;
          border: none;
          box-shadow: none;
          padding: 8px 4px 2px;
          font-size: 11px;
          font-weight: 600;
          letter-spacing: 0.9px;
          color: #facc15;
        }
  - type: custom:button-card
    name: All Floodlights
    icon: mdi:lightbulb-group
    show_state: false
    show_label: true
    triggers_update:
      - switch.v1_floodlight_switch
      - switch.v2_floodlight_switch
      - switch.v3_floodlight_switch
      - switch.mandir_floodlight
      - switch.v4_guest_floodlight
    label: |
      [[[
        const entities = ['switch.v1_floodlight_switch', 'switch.v2_floodlight_switch', 'switch.v3_floodlight_switch', 'switch.mandir_floodlight', 'switch.v4_guest_floodlight'];
        const onCount = entities.filter(e => states[e] && states[e].state === 'on').length;
        if (onCount === 0) return 'ALL OFF';
        if (onCount === entities.length) return 'ALL ON';
        return onCount + '/' + entities.length + ' ON';
      ]]]
    tap_action:
      action: call-service
      service: switch.toggle
      service_data:
        entity_id:
          - switch.v1_floodlight_switch
          - switch.v2_floodlight_switch
          - switch.v3_floodlight_switch
          - switch.mandir_floodlight
          - switch.v4_guest_floodlight
    styles:
      card:
        - border-radius: 10px
        - padding: 10px 16px
        - height: 50px
        - background: |
            [[[
              const entities = ['switch.v1_floodlight_switch', 'switch.v2_floodlight_switch', 'switch.v3_floodlight_switch', 'switch.mandir_floodlight', 'switch.v4_guest_floodlight'];
              const onCount = entities.filter(e => states[e] && states[e].state === 'on').length;
              if (onCount === entities.length) return 'rgba(250, 204, 21, 0.12)';
              if (onCount > 0) return 'rgba(250, 204, 21, 0.06)';
              return 'rgba(255, 255, 255, 0.03)';
            ]]]
        - border: |
            [[[
              const entities = ['switch.v1_floodlight_switch', 'switch.v2_floodlight_switch', 'switch.v3_floodlight_switch', 'switch.mandir_floodlight', 'switch.v4_guest_floodlight'];
              const onCount = entities.filter(e => states[e] && states[e].state === 'on').length;
              if (onCount === entities.length) return '1px solid rgba(250,204,21,0.4)';
              if (onCount > 0) return '1px solid rgba(250,204,21,0.2)';
              return '1px solid rgba(255,255,255,0.06)';
            ]]]
        - transition: all 0.2s ease
      grid:
        - grid-template-areas: "\"i n l\""
        - grid-template-columns: min-content 1fr min-content
        - align-items: center
      img_cell:
        - width: 28px
        - height: 28px
      icon:
        - width: 22px
        - color: |
            [[[
              const entities = ['switch.v1_floodlight_switch', 'switch.v2_floodlight_switch', 'switch.v3_floodlight_switch', 'switch.mandir_floodlight', 'switch.v4_guest_floodlight'];
              const onCount = entities.filter(e => states[e] && states[e].state === 'on').length;
              return onCount > 0 ? '#facc15' : '#6b6e7d';
            ]]]
      name:
        - justify-self: start
        - font-size: 13px
        - font-weight: 600
        - padding-left: 8px
        - color: |
            [[[
              const entities = ['switch.v1_floodlight_switch', 'switch.v2_floodlight_switch', 'switch.v3_floodlight_switch', 'switch.mandir_floodlight', 'switch.v4_guest_floodlight'];
              const onCount = entities.filter(e => states[e] && states[e].state === 'on').length;
              return onCount > 0 ? '#f0f0f3' : '#a0a3b1';
            ]]]
      label:
        - justify-self: end
        - font-size: 10px
        - font-weight: 600
        - padding: 2px 8px
        - border-radius: 4px
        - background: |
            [[[
              const entities = ['switch.v1_floodlight_switch', 'switch.v2_floodlight_switch', 'switch.v3_floodlight_switch', 'switch.mandir_floodlight', 'switch.v4_guest_floodlight'];
              const onCount = entities.filter(e => states[e] && states[e].state === 'on').length;
              return onCount > 0 ? 'rgba(250,204,21,0.15)' : 'rgba(255,255,255,0.05)';
            ]]]
        - color: |
            [[[
              const entities = ['switch.v1_floodlight_switch', 'switch.v2_floodlight_switch', 'switch.v3_floodlight_switch', 'switch.mandir_floodlight', 'switch.v4_guest_floodlight'];
              const onCount = entities.filter(e => states[e] && states[e].state === 'on').length;
              return onCount > 0 ? '#facc15' : '#6b6e7d';
            ]]]
  - type: grid
    columns: 3
    square: false
    cards:
      - type: custom:mushroom-entity-card
        entity: switch.v1_floodlight_switch
        name: V1
        icon: mdi:spotlight-beam
        tap_action:
          action: toggle
        hold_action:
          action: more-info
        card_mod:
          style: |
            ha-card {
              border-radius: 12px;
              {% if is_state('switch.v1_floodlight_switch', 'on') %}
                background: rgba(250, 204, 21, 0.12);
              {% else %}
                background: rgba(255, 255, 255, 0.04);
              {% endif %}
            }
            :host {
              {% if is_state('switch.v1_floodlight_switch', 'on') %}
                --ha-card-border-width: 1px;
                --ha-card-border-color: rgba(250, 204, 21, 0.4);
              {% else %}
                --ha-card-border-width: 1px;
                --ha-card-border-color: rgba(255, 255, 255, 0.06);
              {% endif %}
            }
      - type: custom:mushroom-entity-card
        entity: switch.v2_floodlight_switch
        name: V2
        icon: mdi:spotlight-beam
        tap_action:
          action: toggle
        hold_action:
          action: more-info
        card_mod:
          style: |
            ha-card {
              border-radius: 12px;
              {% if is_state('switch.v2_floodlight_switch', 'on') %}
                background: rgba(250, 204, 21, 0.12);
              {% else %}
                background: rgba(255, 255, 255, 0.04);
              {% endif %}
            }
            :host {
              {% if is_state('switch.v2_floodlight_switch', 'on') %}
                --ha-card-border-width: 1px;
                --ha-card-border-color: rgba(250, 204, 21, 0.4);
              {% else %}
                --ha-card-border-width: 1px;
                --ha-card-border-color: rgba(255, 255, 255, 0.06);
              {% endif %}
            }
      - type: custom:mushroom-entity-card
        entity: switch.v3_floodlight_switch
        name: V3
        icon: mdi:spotlight-beam
        tap_action:
          action: toggle
        hold_action:
          action: more-info
        card_mod:
          style: |
            ha-card {
              border-radius: 12px;
              {% if is_state('switch.v3_floodlight_switch', 'on') %}
                background: rgba(250, 204, 21, 0.12);
              {% else %}
                background: rgba(255, 255, 255, 0.04);
              {% endif %}
            }
            :host {
              {% if is_state('switch.v3_floodlight_switch', 'on') %}
                --ha-card-border-width: 1px;
                --ha-card-border-color: rgba(250, 204, 21, 0.4);
              {% else %}
                --ha-card-border-width: 1px;
                --ha-card-border-color: rgba(255, 255, 255, 0.06);
              {% endif %}
            }
      - type: custom:mushroom-entity-card
        entity: switch.mandir_floodlight
        name: Mandir
        icon: mdi:spotlight-beam
        tap_action:
          action: toggle
        hold_action:
          action: more-info
        card_mod:
          style: |
            ha-card {
              border-radius: 12px;
              {% if is_state('switch.mandir_floodlight', 'on') %}
                background: rgba(250, 204, 21, 0.12);
              {% else %}
                background: rgba(255, 255, 255, 0.04);
              {% endif %}
            }
            :host {
              {% if is_state('switch.mandir_floodlight', 'on') %}
                --ha-card-border-width: 1px;
                --ha-card-border-color: rgba(250, 204, 21, 0.4);
              {% else %}
                --ha-card-border-width: 1px;
                --ha-card-border-color: rgba(255, 255, 255, 0.06);
              {% endif %}
            }
      - type: custom:mushroom-entity-card
        entity: switch.v4_guest_floodlight
        name: V4
        icon: mdi:spotlight-beam
        tap_action:
          action: toggle
        hold_action:
          action: more-info
        card_mod:
          style: |
            ha-card {
              border-radius: 12px;
              {% if is_state('switch.v4_guest_floodlight', 'on') %}
                background: rgba(250, 204, 21, 0.12);
              {% else %}
                background: rgba(255, 255, 255, 0.04);
              {% endif %}
            }
            :host {
              {% if is_state('switch.v4_guest_floodlight', 'on') %}
                --ha-card-border-width: 1px;
                --ha-card-border-color: rgba(250, 204, 21, 0.4);
              {% else %}
                --ha-card-border-width: 1px;
                --ha-card-border-color: rgba(255, 255, 255, 0.06);
              {% endif %}
            }
  - type: markdown
    content: "**AIR CONDITIONING**"
    card_mod:
      style: |
        ha-card {
          background: transparent;
          border: none;
          box-shadow: none;
          padding: 8px 4px 2px;
          font-size: 11px;
          font-weight: 600;
          letter-spacing: 0.9px;
          color: #818cf8;
        }
  - type: grid
    columns: 2
    square: false
    cards:
      - type: custom:button-card
        entity: switch.ac_v1_master
        triggers_update:
          - input_boolean.grid_power_stable
          - sensor.esp8266_mains_vs_grid_voltage_state
          - sensor.ac_v1_master_on_time_today
          - sensor.ac_v1_master_cooling_time_today
          - sensor.homenode_sense_temp_v1_master_bme280_temperature
          - sensor.homenode_sense_temp_v1_master_bme280_humidity
        variables:
          temp_sensor: sensor.homenode_sense_temp_v1_master_bme280_temperature
          humidity_sensor: sensor.homenode_sense_temp_v1_master_bme280_humidity
        name: Master
        label: 2T O General
        show_state: false
        show_label: true
        show_icon: true
        icon: mdi:snowflake
        tap_action:
          action: toggle
        hold_action:
          action: more-info
        custom_fields:
          grid_alert: |
            [[[
              const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
              const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
              const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
              if (stable) return '';
              if (gridOn && !stable) return 'STABILIZING';
              return 'GRID OFF';
            ]]]
          climate: |
            [[[
              const tempId = variables && variables.temp_sensor ? variables.temp_sensor : '';
              const humidityId = variables && variables.humidity_sensor ? variables.humidity_sensor : '';
              const tempRaw = tempId && states[tempId] ? states[tempId].state : '';
              const humidityRaw = humidityId && states[humidityId] ? states[humidityId].state : '';
              const tempOk = tempRaw && !['unknown', 'unavailable', 'none'].includes(String(tempRaw).toLowerCase());
              const humidityOk = humidityRaw && !['unknown', 'unavailable', 'none'].includes(String(humidityRaw).toLowerCase());
              const temp = tempOk ? parseFloat(tempRaw).toFixed(1) : '';
              const humidity = humidityOk ? parseFloat(humidityRaw).toFixed(0) : '';
              if (tempOk && humidityOk) return `🌡 ${temp}°C • ${humidity}%`;
              if (tempOk) return `🌡 ${temp}°C`;
              if (humidityOk) return `💧 ${humidity}%`;
              return '';
            ]]]
          runtime: |
            [[[
              const onTimeEntity = states['sensor.ac_v1_master_on_time_today'];
              const coolTimeEntity = states['sensor.ac_v1_master_cooling_time_today'];
              const onRaw = onTimeEntity ? parseFloat(onTimeEntity.state) : 0;
              const coolRaw = coolTimeEntity ? parseFloat(coolTimeEntity.state) : 0;
              const onValid = onTimeEntity && !['unknown', 'unavailable'].includes(onTimeEntity.state);
              const coolValid = coolTimeEntity && !['unknown', 'unavailable'].includes(coolTimeEntity.state);
              if (!onValid && !coolValid) return '';
              const fmt = (h) => {
                const hrs = Math.floor(h);
                const mins = Math.round((h - hrs) * 60);
                if (hrs > 0 && mins > 0) return `${hrs}h ${mins}m`;
                if (hrs > 0) return `${hrs}h`;
                return `${mins}m`;
              };
              const parts = [];
              if (onValid && onRaw > 0.01) parts.push(`⏱ ${fmt(onRaw)}`);
              if (coolValid && coolRaw > 0.01) parts.push(`❄ ${fmt(coolRaw)}`);
              return parts.join(' · ');
            ]]]
        styles:
          card:
            - position: relative
            - border-radius: 10px
            - padding: 14px 16px
            - height: 140px
            - background: |
                [[[
                  const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                  const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                  const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                  const acOn = entity && entity.state === 'on';
                  if (!gridOn) return '#24181d';
                  if (gridOn && !stable) return '#231f18';
                  if (acOn) return '#162019';
                  return '#181a22';
                ]]]
            - border: |
                [[[
                  const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                  const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                  const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                  const acOn = entity && entity.state === 'on';
                  if (!gridOn) return '2px solid #f87171';
                  if (gridOn && !stable) return '2px solid #fbbf24';
                  if (acOn) return '1px solid rgba(74,222,128,0.34)';
                  return '1px solid rgba(255,255,255,0.06)';
                ]]]
            - box-shadow: |
                [[[
                  const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                  const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                  const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                  if (!gridOn) return '0 0 0 1px rgba(248,113,113,0.10)';
                  if (gridOn && !stable) return '0 0 0 1px rgba(251,191,36,0.10)';
                  return 'none';
                ]]]
            - transition: all 0.2s ease
          grid:
            - grid-template-areas: "\"i grid_alert\" \"n n\" \"l l\" \"climate climate\" \"runtime runtime\""
            - grid-template-columns: 1fr min-content
            - grid-template-rows: min-content min-content min-content min-content min-content
            - row-gap: 3px
          img_cell:
            - justify-content: start
            - align-items: start
            - width: 28px
            - height: 28px
          icon:
            - width: 22px
            - justify-self: start
            - color: |
                [[[
                  const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                  const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                  const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                  const acOn = entity && entity.state === 'on';
                  if (!gridOn) return '#f87171';
                  if (gridOn && !stable) return '#fbbf24';
                  if (acOn) return '#4ade80';
                  return '#6b6e7d';
                ]]]
            - opacity: |
                [[[
                  const acOn = entity && entity.state === 'on';
                  return acOn ? '1' : '0.75';
                ]]]
          name:
            - justify-self: start
            - font-size: 13px
            - font-weight: 600
            - color: |
                [[[
                  const acOn = entity && entity.state === 'on';
                  return acOn ? '#f0f0f3' : '#a0a3b1';
                ]]]
          label:
            - justify-self: start
            - font-size: 10px
            - color: |
                [[[
                  const acOn = entity && entity.state === 'on';
                  return acOn ? '#4ade80' : '#6b6e7d';
                ]]]
          custom_fields:
            grid_alert:
              - justify-self: end
              - align-self: start
              - display: |
                  [[[
                    const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                    const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                    const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                    return stable ? 'none' : 'block';
                  ]]]
              - padding: 2px 7px
              - border-radius: 20px
              - background: |
                  [[[
                    const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                    const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                    if (!gridOn) return 'rgba(248,113,113,0.14)';
                    return 'rgba(251,191,36,0.14)';
                  ]]]
              - border: |
                  [[[
                    const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                    const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                    if (!gridOn) return '1px solid rgba(248,113,113,0.45)';
                    return '1px solid rgba(251,191,36,0.45)';
                  ]]]
              - color: |
                  [[[
                    const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                    const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                    if (!gridOn) return '#f87171';
                    return '#fbbf24';
                  ]]]
              - font-size: 9px
              - font-weight: 700
              - letter-spacing: 0.5px
              - white-space: nowrap
            climate:
              - justify-self: start
              - align-self: end
              - display: |
                  [[[
                    const tempId = variables && variables.temp_sensor ? variables.temp_sensor : '';
                    const humidityId = variables && variables.humidity_sensor ? variables.humidity_sensor : '';
                    const tempRaw = tempId && states[tempId] ? states[tempId].state : '';
                    const humidityRaw = humidityId && states[humidityId] ? states[humidityId].state : '';
                    const tempOk = tempRaw && !['unknown', 'unavailable', 'none'].includes(String(tempRaw).toLowerCase());
                    const humidityOk = humidityRaw && !['unknown', 'unavailable', 'none'].includes(String(humidityRaw).toLowerCase());
                    return tempOk || humidityOk ? 'block' : 'none';
                  ]]]
              - margin-top: 2px
              - padding: 3px 8px
              - border-radius: 6px
              - background: "#1e2029"
              - border: 1px solid rgba(255,255,255,0.06)
              - color: "#a0a3b1"
              - font-size: 10px
              - font-weight: 500
            runtime:
              - justify-self: start
              - align-self: end
              - display: |
                  [[[
                    const onTimeEntity = states['sensor.ac_v1_master_on_time_today'];
                    const coolTimeEntity = states['sensor.ac_v1_master_cooling_time_today'];
                    const onRaw = onTimeEntity ? parseFloat(onTimeEntity.state) : 0;
                    const coolRaw = coolTimeEntity ? parseFloat(coolTimeEntity.state) : 0;
                    const onValid = onTimeEntity && !['unknown', 'unavailable'].includes(onTimeEntity.state);
                    const coolValid = coolTimeEntity && !['unknown', 'unavailable'].includes(coolTimeEntity.state);
                    return (onValid && onRaw > 0.01) || (coolValid && coolRaw > 0.01) ? 'block' : 'none';
                  ]]]
              - margin-top: 1px
              - padding: 3px 8px
              - border-radius: 6px
              - background: "#1a1c25"
              - border: 1px solid rgba(255,255,255,0.04)
              - color: "#7c7f8e"
              - font-size: 9.5px
              - font-weight: 500
      - type: custom:button-card
        entity: switch.ac_v1_raam
        triggers_update:
          - input_boolean.grid_power_stable
          - sensor.esp8266_mains_vs_grid_voltage_state
          - sensor.ac_v1_raam_on_time_today
          - sensor.ac_v1_raam_cooling_time_today
          - sensor.temp_v1_raam_temperature
          - sensor.temp_v1_raam_humidity
        variables:
          temp_sensor: sensor.temp_v1_raam_temperature
          humidity_sensor: sensor.temp_v1_raam_humidity
        name: Raam
        label: 1.5T GTKC50
        show_state: false
        show_label: true
        show_icon: true
        icon: mdi:snowflake
        tap_action:
          action: toggle
        hold_action:
          action: more-info
        custom_fields:
          grid_alert: |
            [[[
              const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
              const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
              const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
              if (stable) return '';
              if (gridOn && !stable) return 'STABILIZING';
              return 'GRID OFF';
            ]]]
          climate: |
            [[[
              const tempId = variables && variables.temp_sensor ? variables.temp_sensor : '';
              const humidityId = variables && variables.humidity_sensor ? variables.humidity_sensor : '';
              const tempRaw = tempId && states[tempId] ? states[tempId].state : '';
              const humidityRaw = humidityId && states[humidityId] ? states[humidityId].state : '';
              const tempOk = tempRaw && !['unknown', 'unavailable', 'none'].includes(String(tempRaw).toLowerCase());
              const humidityOk = humidityRaw && !['unknown', 'unavailable', 'none'].includes(String(humidityRaw).toLowerCase());
              const temp = tempOk ? parseFloat(tempRaw).toFixed(1) : '';
              const humidity = humidityOk ? parseFloat(humidityRaw).toFixed(0) : '';
              if (tempOk && humidityOk) return `🌡 ${temp}°C • ${humidity}%`;
              if (tempOk) return `🌡 ${temp}°C`;
              if (humidityOk) return `💧 ${humidity}%`;
              return '';
            ]]]
          runtime: |
            [[[
              const onTimeEntity = states['sensor.ac_v1_raam_on_time_today'];
              const coolTimeEntity = states['sensor.ac_v1_raam_cooling_time_today'];
              const onRaw = onTimeEntity ? parseFloat(onTimeEntity.state) : 0;
              const coolRaw = coolTimeEntity ? parseFloat(coolTimeEntity.state) : 0;
              const onValid = onTimeEntity && !['unknown', 'unavailable'].includes(onTimeEntity.state);
              const coolValid = coolTimeEntity && !['unknown', 'unavailable'].includes(coolTimeEntity.state);
              if (!onValid && !coolValid) return '';
              const fmt = (h) => {
                const hrs = Math.floor(h);
                const mins = Math.round((h - hrs) * 60);
                if (hrs > 0 && mins > 0) return `${hrs}h ${mins}m`;
                if (hrs > 0) return `${hrs}h`;
                return `${mins}m`;
              };
              const parts = [];
              if (onValid && onRaw > 0.01) parts.push(`⏱ ${fmt(onRaw)}`);
              if (coolValid && coolRaw > 0.01) parts.push(`❄ ${fmt(coolRaw)}`);
              return parts.join(' · ');
            ]]]
        styles:
          card:
            - position: relative
            - border-radius: 10px
            - padding: 14px 16px
            - height: 140px
            - background: |
                [[[
                  const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                  const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                  const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                  const acOn = entity && entity.state === 'on';
                  if (!gridOn) return '#24181d';
                  if (gridOn && !stable) return '#231f18';
                  if (acOn) return '#162019';
                  return '#181a22';
                ]]]
            - border: |
                [[[
                  const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                  const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                  const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                  const acOn = entity && entity.state === 'on';
                  if (!gridOn) return '2px solid #f87171';
                  if (gridOn && !stable) return '2px solid #fbbf24';
                  if (acOn) return '1px solid rgba(74,222,128,0.34)';
                  return '1px solid rgba(255,255,255,0.06)';
                ]]]
            - box-shadow: |
                [[[
                  const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                  const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                  const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                  if (!gridOn) return '0 0 0 1px rgba(248,113,113,0.10)';
                  if (gridOn && !stable) return '0 0 0 1px rgba(251,191,36,0.10)';
                  return 'none';
                ]]]
            - transition: all 0.2s ease
          grid:
            - grid-template-areas: "\"i grid_alert\" \"n n\" \"l l\" \"climate climate\" \"runtime runtime\""
            - grid-template-columns: 1fr min-content
            - grid-template-rows: min-content min-content min-content min-content min-content
            - row-gap: 3px
          img_cell:
            - justify-content: start
            - align-items: start
            - width: 28px
            - height: 28px
          icon:
            - width: 22px
            - justify-self: start
            - color: |
                [[[
                  const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                  const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                  const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                  const acOn = entity && entity.state === 'on';
                  if (!gridOn) return '#f87171';
                  if (gridOn && !stable) return '#fbbf24';
                  if (acOn) return '#4ade80';
                  return '#6b6e7d';
                ]]]
            - opacity: |
                [[[
                  const acOn = entity && entity.state === 'on';
                  return acOn ? '1' : '0.75';
                ]]]
          name:
            - justify-self: start
            - font-size: 13px
            - font-weight: 600
            - color: |
                [[[
                  const acOn = entity && entity.state === 'on';
                  return acOn ? '#f0f0f3' : '#a0a3b1';
                ]]]
          label:
            - justify-self: start
            - font-size: 10px
            - color: |
                [[[
                  const acOn = entity && entity.state === 'on';
                  return acOn ? '#4ade80' : '#6b6e7d';
                ]]]
          custom_fields:
            grid_alert:
              - justify-self: end
              - align-self: start
              - display: |
                  [[[
                    const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                    const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                    const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                    return stable ? 'none' : 'block';
                  ]]]
              - padding: 2px 7px
              - border-radius: 20px
              - background: |
                  [[[
                    const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                    const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                    if (!gridOn) return 'rgba(248,113,113,0.14)';
                    return 'rgba(251,191,36,0.14)';
                  ]]]
              - border: |
                  [[[
                    const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                    const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                    if (!gridOn) return '1px solid rgba(248,113,113,0.45)';
                    return '1px solid rgba(251,191,36,0.45)';
                  ]]]
              - color: |
                  [[[
                    const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                    const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                    if (!gridOn) return '#f87171';
                    return '#fbbf24';
                  ]]]
              - font-size: 9px
              - font-weight: 700
              - letter-spacing: 0.5px
              - white-space: nowrap
            climate:
              - justify-self: start
              - align-self: end
              - display: |
                  [[[
                    const tempId = variables && variables.temp_sensor ? variables.temp_sensor : '';
                    const humidityId = variables && variables.humidity_sensor ? variables.humidity_sensor : '';
                    const tempRaw = tempId && states[tempId] ? states[tempId].state : '';
                    const humidityRaw = humidityId && states[humidityId] ? states[humidityId].state : '';
                    const tempOk = tempRaw && !['unknown', 'unavailable', 'none'].includes(String(tempRaw).toLowerCase());
                    const humidityOk = humidityRaw && !['unknown', 'unavailable', 'none'].includes(String(humidityRaw).toLowerCase());
                    return tempOk || humidityOk ? 'block' : 'none';
                  ]]]
              - margin-top: 2px
              - padding: 3px 8px
              - border-radius: 6px
              - background: "#1e2029"
              - border: 1px solid rgba(255,255,255,0.06)
              - color: "#a0a3b1"
              - font-size: 10px
              - font-weight: 500
            runtime:
              - justify-self: start
              - align-self: end
              - display: |
                  [[[
                    const onTimeEntity = states['sensor.ac_v1_raam_on_time_today'];
                    const coolTimeEntity = states['sensor.ac_v1_raam_cooling_time_today'];
                    const onRaw = onTimeEntity ? parseFloat(onTimeEntity.state) : 0;
                    const coolRaw = coolTimeEntity ? parseFloat(coolTimeEntity.state) : 0;
                    const onValid = onTimeEntity && !['unknown', 'unavailable'].includes(onTimeEntity.state);
                    const coolValid = coolTimeEntity && !['unknown', 'unavailable'].includes(coolTimeEntity.state);
                    return (onValid && onRaw > 0.01) || (coolValid && coolRaw > 0.01) ? 'block' : 'none';
                  ]]]
              - margin-top: 1px
              - padding: 3px 8px
              - border-radius: 6px
              - background: "#1a1c25"
              - border: 1px solid rgba(255,255,255,0.04)
              - color: "#7c7f8e"
              - font-size: 9.5px
              - font-weight: 500
      - type: custom:button-card
        entity: switch.ac_v1_radhha
        triggers_update:
          - input_boolean.grid_power_stable
          - sensor.esp8266_mains_vs_grid_voltage_state
          - sensor.ac_v1_radhha_on_time_today
          - sensor.ac_v1_radhha_cooling_time_today
          - sensor.temp_v1_radhha_zb_temperature
          - sensor.temp_v1_radhha_zb_humidity
        variables:
          temp_sensor: sensor.temp_v1_radhha_zb_temperature
          humidity_sensor: sensor.temp_v1_radhha_zb_humidity
        name: Radhha
        label: 1.5T GTKC50
        show_state: false
        show_label: true
        show_icon: true
        icon: mdi:snowflake
        tap_action:
          action: toggle
        hold_action:
          action: more-info
        custom_fields:
          grid_alert: |
            [[[
              const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
              const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
              const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
              if (stable) return '';
              if (gridOn && !stable) return 'STABILIZING';
              return 'GRID OFF';
            ]]]
          climate: |
            [[[
              const tempId = variables && variables.temp_sensor ? variables.temp_sensor : '';
              const humidityId = variables && variables.humidity_sensor ? variables.humidity_sensor : '';
              const tempRaw = tempId && states[tempId] ? states[tempId].state : '';
              const humidityRaw = humidityId && states[humidityId] ? states[humidityId].state : '';
              const tempOk = tempRaw && !['unknown', 'unavailable', 'none'].includes(String(tempRaw).toLowerCase());
              const humidityOk = humidityRaw && !['unknown', 'unavailable', 'none'].includes(String(humidityRaw).toLowerCase());
              const temp = tempOk ? parseFloat(tempRaw).toFixed(1) : '';
              const humidity = humidityOk ? parseFloat(humidityRaw).toFixed(0) : '';
              if (tempOk && humidityOk) return `🌡 ${temp}°C • ${humidity}%`;
              if (tempOk) return `🌡 ${temp}°C`;
              if (humidityOk) return `💧 ${humidity}%`;
              return '';
            ]]]
          runtime: |
            [[[
              const onTimeEntity = states['sensor.ac_v1_radhha_on_time_today'];
              const coolTimeEntity = states['sensor.ac_v1_radhha_cooling_time_today'];
              const onRaw = onTimeEntity ? parseFloat(onTimeEntity.state) : 0;
              const coolRaw = coolTimeEntity ? parseFloat(coolTimeEntity.state) : 0;
              const onValid = onTimeEntity && !['unknown', 'unavailable'].includes(onTimeEntity.state);
              const coolValid = coolTimeEntity && !['unknown', 'unavailable'].includes(coolTimeEntity.state);
              if (!onValid && !coolValid) return '';
              const fmt = (h) => {
                const hrs = Math.floor(h);
                const mins = Math.round((h - hrs) * 60);
                if (hrs > 0 && mins > 0) return `${hrs}h ${mins}m`;
                if (hrs > 0) return `${hrs}h`;
                return `${mins}m`;
              };
              const parts = [];
              if (onValid && onRaw > 0.01) parts.push(`⏱ ${fmt(onRaw)}`);
              if (coolValid && coolRaw > 0.01) parts.push(`❄ ${fmt(coolRaw)}`);
              return parts.join(' · ');
            ]]]
        styles:
          card:
            - position: relative
            - border-radius: 10px
            - padding: 14px 16px
            - height: 140px
            - background: |
                [[[
                  const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                  const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                  const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                  const acOn = entity && entity.state === 'on';
                  if (!gridOn) return '#24181d';
                  if (gridOn && !stable) return '#231f18';
                  if (acOn) return '#162019';
                  return '#181a22';
                ]]]
            - border: |
                [[[
                  const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                  const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                  const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                  const acOn = entity && entity.state === 'on';
                  if (!gridOn) return '2px solid #f87171';
                  if (gridOn && !stable) return '2px solid #fbbf24';
                  if (acOn) return '1px solid rgba(74,222,128,0.34)';
                  return '1px solid rgba(255,255,255,0.06)';
                ]]]
            - box-shadow: |
                [[[
                  const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                  const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                  const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                  if (!gridOn) return '0 0 0 1px rgba(248,113,113,0.10)';
                  if (gridOn && !stable) return '0 0 0 1px rgba(251,191,36,0.10)';
                  return 'none';
                ]]]
            - transition: all 0.2s ease
          grid:
            - grid-template-areas: "\"i grid_alert\" \"n n\" \"l l\" \"climate climate\" \"runtime runtime\""
            - grid-template-columns: 1fr min-content
            - grid-template-rows: min-content min-content min-content min-content min-content
            - row-gap: 3px
          img_cell:
            - justify-content: start
            - align-items: start
            - width: 28px
            - height: 28px
          icon:
            - width: 22px
            - justify-self: start
            - color: |
                [[[
                  const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                  const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                  const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                  const acOn = entity && entity.state === 'on';
                  if (!gridOn) return '#f87171';
                  if (gridOn && !stable) return '#fbbf24';
                  if (acOn) return '#4ade80';
                  return '#6b6e7d';
                ]]]
            - opacity: |
                [[[
                  const acOn = entity && entity.state === 'on';
                  return acOn ? '1' : '0.75';
                ]]]
          name:
            - justify-self: start
            - font-size: 13px
            - font-weight: 600
            - color: |
                [[[
                  const acOn = entity && entity.state === 'on';
                  return acOn ? '#f0f0f3' : '#a0a3b1';
                ]]]
          label:
            - justify-self: start
            - font-size: 10px
            - color: |
                [[[
                  const acOn = entity && entity.state === 'on';
                  return acOn ? '#4ade80' : '#6b6e7d';
                ]]]
          custom_fields:
            grid_alert:
              - justify-self: end
              - align-self: start
              - display: |
                  [[[
                    const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                    const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                    const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                    return stable ? 'none' : 'block';
                  ]]]
              - padding: 2px 7px
              - border-radius: 20px
              - background: |
                  [[[
                    const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                    const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                    if (!gridOn) return 'rgba(248,113,113,0.14)';
                    return 'rgba(251,191,36,0.14)';
                  ]]]
              - border: |
                  [[[
                    const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                    const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                    if (!gridOn) return '1px solid rgba(248,113,113,0.45)';
                    return '1px solid rgba(251,191,36,0.45)';
                  ]]]
              - color: |
                  [[[
                    const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                    const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                    if (!gridOn) return '#f87171';
                    return '#fbbf24';
                  ]]]
              - font-size: 9px
              - font-weight: 700
              - letter-spacing: 0.5px
              - white-space: nowrap
            climate:
              - justify-self: start
              - align-self: end
              - display: |
                  [[[
                    const tempId = variables && variables.temp_sensor ? variables.temp_sensor : '';
                    const humidityId = variables && variables.humidity_sensor ? variables.humidity_sensor : '';
                    const tempRaw = tempId && states[tempId] ? states[tempId].state : '';
                    const humidityRaw = humidityId && states[humidityId] ? states[humidityId].state : '';
                    const tempOk = tempRaw && !['unknown', 'unavailable', 'none'].includes(String(tempRaw).toLowerCase());
                    const humidityOk = humidityRaw && !['unknown', 'unavailable', 'none'].includes(String(humidityRaw).toLowerCase());
                    return tempOk || humidityOk ? 'block' : 'none';
                  ]]]
              - margin-top: 2px
              - padding: 3px 8px
              - border-radius: 6px
              - background: "#1e2029"
              - border: 1px solid rgba(255,255,255,0.06)
              - color: "#a0a3b1"
              - font-size: 10px
              - font-weight: 500
            runtime:
              - justify-self: start
              - align-self: end
              - display: |
                  [[[
                    const onTimeEntity = states['sensor.ac_v1_radhha_on_time_today'];
                    const coolTimeEntity = states['sensor.ac_v1_radhha_cooling_time_today'];
                    const onRaw = onTimeEntity ? parseFloat(onTimeEntity.state) : 0;
                    const coolRaw = coolTimeEntity ? parseFloat(coolTimeEntity.state) : 0;
                    const onValid = onTimeEntity && !['unknown', 'unavailable'].includes(onTimeEntity.state);
                    const coolValid = coolTimeEntity && !['unknown', 'unavailable'].includes(coolTimeEntity.state);
                    return (onValid && onRaw > 0.01) || (coolValid && coolRaw > 0.01) ? 'block' : 'none';
                  ]]]
              - margin-top: 1px
              - padding: 3px 8px
              - border-radius: 6px
              - background: "#1a1c25"
              - border: 1px solid rgba(255,255,255,0.04)
              - color: "#7c7f8e"
              - font-size: 9.5px
              - font-weight: 500
      - type: custom:button-card
        entity: switch.ac_v1_yoga
        triggers_update:
          - input_boolean.grid_power_stable
          - sensor.esp8266_mains_vs_grid_voltage_state
          - sensor.ac_v1_yoga_on_time_today
          - sensor.ac_v1_yoga_cooling_time_today
        variables:
          temp_sensor: ""
          humidity_sensor: ""
        name: Yoga
        label: 1T Daikin GTQ35
        show_state: false
        show_label: true
        show_icon: true
        icon: mdi:snowflake
        tap_action:
          action: toggle
        hold_action:
          action: more-info
        custom_fields:
          grid_alert: |
            [[[
              const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
              const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
              const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
              if (stable) return '';
              if (gridOn && !stable) return 'STABILIZING';
              return 'GRID OFF';
            ]]]
          climate: |
            [[[
              const tempId = variables && variables.temp_sensor ? variables.temp_sensor : '';
              const humidityId = variables && variables.humidity_sensor ? variables.humidity_sensor : '';
              const tempRaw = tempId && states[tempId] ? states[tempId].state : '';
              const humidityRaw = humidityId && states[humidityId] ? states[humidityId].state : '';
              const tempOk = tempRaw && !['unknown', 'unavailable', 'none'].includes(String(tempRaw).toLowerCase());
              const humidityOk = humidityRaw && !['unknown', 'unavailable', 'none'].includes(String(humidityRaw).toLowerCase());
              const temp = tempOk ? parseFloat(tempRaw).toFixed(1) : '';
              const humidity = humidityOk ? parseFloat(humidityRaw).toFixed(0) : '';
              if (tempOk && humidityOk) return `🌡 ${temp}°C • ${humidity}%`;
              if (tempOk) return `🌡 ${temp}°C`;
              if (humidityOk) return `💧 ${humidity}%`;
              return '';
            ]]]
          runtime: |
            [[[
              const onTimeEntity = states['sensor.ac_v1_yoga_on_time_today'];
              const coolTimeEntity = states['sensor.ac_v1_yoga_cooling_time_today'];
              const onRaw = onTimeEntity ? parseFloat(onTimeEntity.state) : 0;
              const coolRaw = coolTimeEntity ? parseFloat(coolTimeEntity.state) : 0;
              const onValid = onTimeEntity && !['unknown', 'unavailable'].includes(onTimeEntity.state);
              const coolValid = coolTimeEntity && !['unknown', 'unavailable'].includes(coolTimeEntity.state);
              if (!onValid && !coolValid) return '';
              const fmt = (h) => {
                const hrs = Math.floor(h);
                const mins = Math.round((h - hrs) * 60);
                if (hrs > 0 && mins > 0) return `${hrs}h ${mins}m`;
                if (hrs > 0) return `${hrs}h`;
                return `${mins}m`;
              };
              const parts = [];
              if (onValid && onRaw > 0.01) parts.push(`⏱ ${fmt(onRaw)}`);
              if (coolValid && coolRaw > 0.01) parts.push(`❄ ${fmt(coolRaw)}`);
              return parts.join(' · ');
            ]]]
        styles:
          card:
            - position: relative
            - border-radius: 10px
            - padding: 14px 16px
            - height: 140px
            - background: |
                [[[
                  const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                  const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                  const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                  const acOn = entity && entity.state === 'on';
                  if (!gridOn) return '#24181d';
                  if (gridOn && !stable) return '#231f18';
                  if (acOn) return '#162019';
                  return '#181a22';
                ]]]
            - border: |
                [[[
                  const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                  const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                  const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                  const acOn = entity && entity.state === 'on';
                  if (!gridOn) return '2px solid #f87171';
                  if (gridOn && !stable) return '2px solid #fbbf24';
                  if (acOn) return '1px solid rgba(74,222,128,0.34)';
                  return '1px solid rgba(255,255,255,0.06)';
                ]]]
            - box-shadow: |
                [[[
                  const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                  const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                  const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                  if (!gridOn) return '0 0 0 1px rgba(248,113,113,0.10)';
                  if (gridOn && !stable) return '0 0 0 1px rgba(251,191,36,0.10)';
                  return 'none';
                ]]]
            - transition: all 0.2s ease
          grid:
            - grid-template-areas: "\"i grid_alert\" \"n n\" \"l l\" \"climate climate\" \"runtime runtime\""
            - grid-template-columns: 1fr min-content
            - grid-template-rows: min-content min-content min-content min-content min-content
            - row-gap: 3px
          img_cell:
            - justify-content: start
            - align-items: start
            - width: 28px
            - height: 28px
          icon:
            - width: 22px
            - justify-self: start
            - color: |
                [[[
                  const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                  const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                  const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                  const acOn = entity && entity.state === 'on';
                  if (!gridOn) return '#f87171';
                  if (gridOn && !stable) return '#fbbf24';
                  if (acOn) return '#4ade80';
                  return '#6b6e7d';
                ]]]
            - opacity: |
                [[[
                  const acOn = entity && entity.state === 'on';
                  return acOn ? '1' : '0.75';
                ]]]
          name:
            - justify-self: start
            - font-size: 13px
            - font-weight: 600
            - color: |
                [[[
                  const acOn = entity && entity.state === 'on';
                  return acOn ? '#f0f0f3' : '#a0a3b1';
                ]]]
          label:
            - justify-self: start
            - font-size: 10px
            - color: |
                [[[
                  const acOn = entity && entity.state === 'on';
                  return acOn ? '#4ade80' : '#6b6e7d';
                ]]]
          custom_fields:
            grid_alert:
              - justify-self: end
              - align-self: start
              - display: |
                  [[[
                    const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                    const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                    const stable = states['input_boolean.grid_power_stable'] && states['input_boolean.grid_power_stable'].state === 'on';
                    return stable ? 'none' : 'block';
                  ]]]
              - padding: 2px 7px
              - border-radius: 20px
              - background: |
                  [[[
                    const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                    const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                    if (!gridOn) return 'rgba(248,113,113,0.14)';
                    return 'rgba(251,191,36,0.14)';
                  ]]]
              - border: |
                  [[[
                    const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                    const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                    if (!gridOn) return '1px solid rgba(248,113,113,0.45)';
                    return '1px solid rgba(251,191,36,0.45)';
                  ]]]
              - color: |
                  [[[
                    const gridSensor = states['sensor.esp8266_mains_vs_grid_voltage_state'];
                    const gridOn = gridSensor && gridSensor.state.toLowerCase() === 'on';
                    if (!gridOn) return '#f87171';
                    return '#fbbf24';
                  ]]]
              - font-size: 9px
              - font-weight: 700
              - letter-spacing: 0.5px
              - white-space: nowrap
            climate:
              - justify-self: start
              - align-self: end
              - display: |
                  [[[
                    const tempId = variables && variables.temp_sensor ? variables.temp_sensor : '';
                    const humidityId = variables && variables.humidity_sensor ? variables.humidity_sensor : '';
                    const tempRaw = tempId && states[tempId] ? states[tempId].state : '';
                    const humidityRaw = humidityId && states[humidityId] ? states[humidityId].state : '';
                    const tempOk = tempRaw && !['unknown', 'unavailable', 'none'].includes(String(tempRaw).toLowerCase());
                    const humidityOk = humidityRaw && !['unknown', 'unavailable', 'none'].includes(String(humidityRaw).toLowerCase());
                    return tempOk || humidityOk ? 'block' : 'none';
                  ]]]
              - margin-top: 2px
              - padding: 3px 8px
              - border-radius: 6px
              - background: "#1e2029"
              - border: 1px solid rgba(255,255,255,0.06)
              - color: "#a0a3b1"
              - font-size: 10px
              - font-weight: 500
            runtime:
              - justify-self: start
              - align-self: end
              - display: |
                  [[[
                    const onTimeEntity = states['sensor.ac_v1_yoga_on_time_today'];
                    const coolTimeEntity = states['sensor.ac_v1_yoga_cooling_time_today'];
                    const onRaw = onTimeEntity ? parseFloat(onTimeEntity.state) : 0;
                    const coolRaw = coolTimeEntity ? parseFloat(coolTimeEntity.state) : 0;
                    const onValid = onTimeEntity && !['unknown', 'unavailable'].includes(onTimeEntity.state);
                    const coolValid = coolTimeEntity && !['unknown', 'unavailable'].includes(coolTimeEntity.state);
                    return (onValid && onRaw > 0.01) || (coolValid && coolRaw > 0.01) ? 'block' : 'none';
                  ]]]
              - margin-top: 1px
              - padding: 3px 8px
              - border-radius: 6px
              - background: "#1a1c25"
              - border: 1px solid rgba(255,255,255,0.04)
              - color: "#7c7f8e"
              - font-size: 9.5px
              - font-weight: 500
