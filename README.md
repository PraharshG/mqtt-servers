# MQTT Temperature Monitoring

## Overview
This repository contains two Python scripts demonstrating the use of MQTT (Message Queuing Telemetry Transport) for temperature monitoring. The setup includes a publisher that sends random temperature values to an MQTT broker and a subscriber that receives and displays these values in real-time.

### Files
1. **`mqtt_publisher.py`**: Publishes random temperature values to the MQTT broker.
2. **`mqtt_subscriber.py`**: Subscribes to the temperature topic to receive and print the published values.

## Installation

### Requirements
- Python 3.7+
- `paho-mqtt` package

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/PraharshG/mqtt-servers.git
   cd mqtt-temperature-monitoring
   ```
2. Install the required Python package:
   ```bash
   pip install paho-mqtt
   ```
3. Ensure both scripts are in the same directory and update the `mqttBroker` IP address to match your MQTT broker's address.

## Usage

### 1. Running the Publisher
The `mqtt_publisher.py` script generates random temperature values between 20.0 and 21.0 and publishes them to the MQTT topic `TEMPERATURE` every 5 seconds.

Run the publisher script:
```bash
python mqtt_publisher.py
```

### 2. Running the Subscriber
The `mqtt_subscriber.py` script subscribes to the `TEMPERATURE` topic and prints the received temperature values.

Run the subscriber script:
```bash
python mqtt_subscriber.py
```

### Example Output
#### Publisher:
```text
Just published 20.56 to Topic TEMPERATURE
Just published 20.89 to Topic TEMPERATURE
```

#### Subscriber:
```text
Received message: 20.56
Received message: 20.89
```

## Customization

### MQTT Broker
Update the `mqttBroker` variable in both scripts to match your broker's IP address or hostname:
```python
mqttBroker = "your-broker-ip"
```

### Temperature Range
Modify the range of random temperature values in `mqtt_publisher.py`:
```python
randNumber = uniform(20.0, 21.0)  # Change the range as needed
```

### Topic
Change the MQTT topic by updating the `client.publish` and `client.subscribe` methods in the respective scripts:
```python
client.publish("YOUR_TOPIC", randNumber)  # Publisher
client.subscribe("YOUR_TOPIC")  # Subscriber
```

## Notes
- Ensure your MQTT broker is running and accessible.
- The default broker port is set to 1883.
- The subscriber script runs for 30 seconds and then stops. Adjust the `time.sleep(30)` value in `mqtt_subscriber.py` to change the runtime.
