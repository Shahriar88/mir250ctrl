from __future__ import annotations

"""Example use of Mir250MapFusion from the master mir250ctrl.py module.

Start Mir250_Server.py first from an Administrator terminal.
Then run this file from another terminal.

The file reads the MiR map, robot pose, and live point cloud.
Motion examples are included below but are disabled by default.
"""

from mir250ctrl import Mir250MapFusion


# ----------------------------------------------------------------------
# Motion test switch
# ----------------------------------------------------------------------
# Keep this False for normal map/point-cloud testing.
# Change to True only when you are physically ready to move the robot.
ENABLE_MOTION_TEST = False


def main() -> None:
    fusion = Mir250MapFusion(
        # Point-cloud TCP server
        server_host="127.0.0.1",
        server_port=5000,

        # MiR250 REST API
        base_url="http://192.168.20.20/api/v2.0.0",
        username="user1",
        password="12345678",

        # Map selection
        # Leave both as None to let the fusion class try to detect
        # the current map automatically from the MiR250 status.
        map_sn=None,
        map_guid=None,

        # Coordinate interpretation
        pointcloud_frame="map",

        # MiR orientation values are expected in degrees for
        # heading/map visualization.
        orientation_unit="deg",

        # Runtime settings
        debug=True,
        socket_timeout=15.0,
    )

    try:
        # --------------------------------------------------------------
        # 1. Load and inspect the current map
        # --------------------------------------------------------------
        fusion.load_current_map()
        fusion.print_map_metadata()

        # --------------------------------------------------------------
        # 2. Get one fresh combined snapshot
        # --------------------------------------------------------------
        # Includes:
        #   - cached map
        #   - fresh obstacle/laser XY data
        #   - fresh MiR x, y, orientation
        data = fusion.get_data()

        robot = data["robot"]
        obstacles = data["obstacles_map"]

        print()
        print("=" * 60)
        print("CURRENT ROBOT DATA")
        print("=" * 60)
        print("Robot X:", robot["x"])
        print("Robot Y:", robot["y"])
        print("Robot orientation:", robot["orientation"])
        print("Obstacle points:", len(obstacles))
        print("=" * 60)

        # --------------------------------------------------------------
        # 3. Optional robot movement
        # --------------------------------------------------------------
        if ENABLE_MOTION_TEST:          
            
            print()
            print("MOTION TEST ENABLED")
            
            # Clear any old/pending missions before starting this test
            print("Clearing existing mission queue...")
            fusion.stop()
            

            # First physical test:
            # Move backward 0.10 m at low speed.
            fusion.move_relative(
                x=-1.00,
                y=-0.00,
                orientation=0.0,
                vel_lin=1.00,
                vel_ang=0.05,
            )
            
            # Move forward 0.10 m at low speed.
            fusion.move_relative(
                x=1.00,
                y=-0.00,
                orientation=0.0,
                vel_lin=1.00,
                vel_ang=0.05,
            )

            # Other examples:
            #
            # Relative sideways / rotational move:
            #
            # fusion.move_relative(
            #     x=0.0,
            #     y=0.10,
            #     orientation=0.0,
            #     vel_lin=0.05,
            #     vel_ang=0.05,
            # )
            #
            # Rotate in place:
            #
            # fusion.move_relative(
            #     x=0.0,
            #     y=0.0,
            #     orientation=30.0,
            #     vel_lin=0.05,
            #     vel_ang=0.05,
            # )
            #
            # Absolute map-coordinate move:
            #
            # fusion.move_to(
            #     x=10.5,
            #     y=6.2,
            #     orientation=90.0,
            # )
            #
            # Repeated relative movement:
            #
            # fusion.move_relative_repeat(
            #     x=0.10,
            #     y=0.0,
            #     orientation=0.0,
            #     n_loop=2,
            #     vel_lin=0.05,
            #     vel_ang=0.05,
            # )
            #
            # Send robot to charger:
            #
            # fusion.go_to_charger(charge_min=50.0)
            #
            # Abort/clear queued movement:
            #
            # fusion.stop()

        else:
            print()
            print("Motion test disabled.")
            print("Set ENABLE_MOTION_TEST = True only when ready for a physical test.")

        # --------------------------------------------------------------
        # 4. Display map + robot pose + live obstacle points
        # --------------------------------------------------------------
        # refresh=False prevents another server/API acquisition because
        # get_data() was already called above.
        fusion.show(refresh=False)

    finally:
        fusion.close()


if __name__ == "__main__":
    main()
