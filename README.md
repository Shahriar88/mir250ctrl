# mir250ctrl

A Python toolkit for controlling, monitoring, and interfacing with MiR250 mobile robots.

`mir250ctrl` provides tools for MiR REST API communication, robot mission control, map access, live point-cloud capture, TCP communication, and map/robot/obstacle visualization.

## Installation

Install from PyPI:

```bash
pip install mir250ctrl
```

The main dependencies are installed automatically with the package.

Live point-cloud capture using PyShark may require additional system setup, including TShark/Wireshark.

## Repository Examples

The repository includes standalone Python examples demonstrating the point-cloud and map-fusion features of `mir250ctrl`.

### `Mir250_Server.py`

Runs the MiR250 point-cloud TCP server.

The server captures live MiR250 laser point-cloud data and makes it available to local or remote Python clients.

The server supports command-line configuration for:

- MiR250 IP address
- Network interface
- TCP host and port
- ROSBridge point-cloud topic

Example:

```bash
python Mir250_Server.py
```

Run this script before using the point-cloud client or map-fusion example.

### `Mir250_Client.py`

A minimal TCP client example for requesting one point cloud from `Mir250_Server.py`.

It demonstrates how to:

- Connect to the point-cloud server
- Request a fresh point cloud
- Access the returned `x` and `y` coordinates
- Read the number of decoded points

Example:

```bash
python Mir250_Client.py
```

### `Mir250_Map_Usage.py`

Example application using `Mir250MapFusion`.

It combines:

- MiR map data
- Current robot position and orientation
- Live laser / obstacle point-cloud data
- Point-cloud transformation and visualization

The example can display the MiR map together with the robot pose and live obstacle points.

Robot motion examples are also included, but motion testing is disabled by default:

```python
ENABLE_MOTION_TEST = False
```

Only enable motion testing when the robot and operating area are physically ready and all required safety precautions are in place.

## Typical Point-Cloud Workflow

Start the point-cloud server:

```bash
python Mir250_Server.py
```

Then, in another terminal, run either:

```bash
python Mir250_Client.py
```

to retrieve point-cloud coordinates, or:

```bash
python Mir250_Map_Usage.py
```

to combine the MiR map, robot pose, and live obstacle data.

## License

MIT License

Copyright (c) 2026 Md Shahriar Forhad