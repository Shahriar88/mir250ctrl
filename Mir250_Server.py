# Run from an Administrator terminal
# Run from Command Prompt or PowerShell as Administrator

from __future__ import annotations

import argparse

from mir250ctrl import (
    INTERFACE,
    MIR_IP,
    SERVER_HOST,
    SERVER_PORT,
    TOPIC,
    run_server,
)


# -----------------------------------------------------------------------------
# Usage examples
# -----------------------------------------------------------------------------
# Run with all default values:
#   python Mir250_Server.py
#
# Equivalent command with every default written explicitly:
#   python Mir250_Server.py --host 127.0.0.1 --port 5000 \
#       --mir-ip 192.168.20.20 --interface "Wi-Fi" \
#       --topic "/mirwebapp/laser_map_pointcloud"
#
# Change only the capture interface:
#   python Mir250_Server.py --interface "Ethernet"
#
# Change only the MiR250 IP address:
#   python Mir250_Server.py --mir-ip 192.168.20.30
#
# Change both the MiR250 IP and capture interface:
#   python Mir250_Server.py --mir-ip 192.168.20.30 --interface "Ethernet"
#
# Use a different server TCP port:
#   python Mir250_Server.py --port 6000
#
# Allow clients on other computers to connect to this server:
#   python Mir250_Server.py --host 0.0.0.0
#
# Change the ROSBridge point-cloud topic:
#   python Mir250_Server.py --topic "/some/other/pointcloud_topic"
#
# Show all available command-line arguments:
#   python Mir250_Server.py --help
# -----------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="MiR250 point-cloud request/response server."
    )
    parser.add_argument(
        "--host",
        default=SERVER_HOST,
        help=f"Server bind host (default: {SERVER_HOST})",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=SERVER_PORT,
        help=f"Server TCP port (default: {SERVER_PORT})",
    )
    parser.add_argument(
        "--mir-ip",
        default=MIR_IP,
        help=f"MiR250 IP address (default: {MIR_IP})",
    )
    parser.add_argument(
        "--interface",
        default=INTERFACE,
        help=f"Capture interface (default: {INTERFACE})",
    )
    parser.add_argument(
        "--topic",
        default=TOPIC,
        help=f"ROSBridge point-cloud topic (default: {TOPIC})",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run_server(
        host=args.host,
        port=args.port,
        mir_ip=args.mir_ip,
        interface=args.interface,
        topic=args.topic,
    )


if __name__ == "__main__":
    main()
