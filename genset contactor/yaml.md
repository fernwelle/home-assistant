##OLD and working
- sensor:
      - name: "Villa 1 Power Source"
        unique_id: v1_power_source
        state: >-
          {% set grid_stable = is_state('input_boolean.grid_power_stable', 'on') %}
          {% set grid_contactor = is_state('switch.grid_contactor', 'on') %}
          {% if grid_stable and grid_contactor %}
            grid
          {% elif grid_stable and not grid_contactor %}
            genset
          {% elif not grid_stable and grid_contactor %}
            panel_fault
          {% else %}
            no_power
          {% endif %}
        icon: >-
          {% set state = this.state %}
          {% if state == 'grid' %}
            mdi:transmission-tower
          {% elif state == 'genset' %}
            mdi:engine
          {% elif state == 'panel_fault' %}
            mdi:alert-circle
          {% else %}
            mdi:power-plug-off
          {% endif %}


  ###new update with 5 states