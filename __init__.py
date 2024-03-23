DOMAIN = "blauberg_smart_wifi"

def setup(hass, config):
    hass.states.set("blauberg_smart_wifi.world", "what")

    return True
