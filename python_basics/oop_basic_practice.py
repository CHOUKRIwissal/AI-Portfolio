# Parent class
class Device:

    # Initialize 
    def __init__(self, name, status, power_usage):
        self.name = name
        self.status = status
        self.power_usage = power_usage

    # Turn on
    def turn_on(self):
        self.status = "on"
        return self.status

    # Turn off
    def turn_off(self):
        self.status = "off"
        return self.status

    # Get power usage
    def get_power_usage(self):
        return self.power_usage

    # Display 
    def __str__(self):
        return f"{self.name} - {self.status}"


# Child class
class SmartLight(Device):

    def __init__(self, name, status, power_usage, brightness):
        super().__init__(name, status, power_usage)
        self.brightness = brightness

    # Set brightness
    def set_brightness(self, level):
        self.brightness = level
        return self.brightness

    # Decrease brightness
    def dim(self):
        self.brightness = max(0, self.brightness - 10)
        return self.brightness

    # Display 
    def __str__(self):
        return f"{self.name} - {self.status} - Brightness: {self.brightness}"


# Child class
class SmartSpeaker(Device):

    # Initialize 
    def __init__(self, name, status, power_usage, volume):
        super().__init__(name, status, power_usage)
        self.volume = volume

    # Set volume
    def set_volume(self, level):
        self.volume = level
        return self.volume

    # Play music
    def play_music(self):
        return "Playing music"

    # Display 
    def __str__(self):
        return f"{self.name} - {self.status} - Volume: {self.volume}"


# Test Device
device = Device("TV", "off", 100)

print(device)
print(device.turn_on())
print(device.turn_off())
print(device.get_power_usage())


# Test SmartLight
light = SmartLight("Bedroom Light", "off", 20, 80)

print(light)
print(light.set_brightness(60))
print(light.turn_on())
print(light)
print(light.dim())


# Test SmartSpeaker
speaker = SmartSpeaker("Speaker", "off", 50, 5)

print(speaker)
print(speaker.set_volume(8))
print(speaker.turn_on())
print(speaker.play_music())
print(speaker)
