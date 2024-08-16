import click
import matplotlib.pyplot as plt

from simulation.dynamics import DynamicsSimulation
from simulation.motor import Motor
from simulation.vehicle import Vehicle


@click.command(context_settings={"show_default": True})
@click.option("--vehicle", default="drjoe", help="The vehicle to simulate.")
@click.option("--motor",
              default="aerotech_l1940x",
              help="The motor that provides thrust to the vehicle.")
@click.option("--hertz",
              default=100,
              help="The speed at which to run the software loop.")
def simulate(vehicle: str, motor: str, hertz: int):
    """Run a complete software-in-the-loop rocket flight simulation."""
    vehicle_file_path = f"data/vehicles/{vehicle}.json"
    vehicle = Vehicle.from_json(vehicle_file_path)

    motor_file_path = f"data/motors/{motor}.json"
    motor = Motor.from_json(motor_file_path)

    dynamics = DynamicsSimulation(vehicle, motor)

    # TODO: Run the simulation.
    time_delta = 1 / hertz

    times = []
    positions = []

    state = dynamics.state
    while state.time < 50:
        times.append(state.time)
        positions.append(state.position)
        dynamics.step(time_delta)
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    # Create a 3D plot
    import numpy as np
    positions = np.array(positions)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the position data
    ax.plot(positions[:, 0],
            positions[:, 1],
            positions[:, 2],
            label='Rocket Position')

    # Add labels and title
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_zlabel('Z Position')
    ax.set_title('Rocket Position vs Time')

    # Show the legend
    ax.legend()

    # Show the plot
    plt.show()


# plt.xlabel("Time (seconds)")
# plt.ylabel("Altitude (meters)")
# plt.title("ACS Simulation")
# plt.plot(times, positions)
# plt.show()

if __name__ == "__main__":
    simulate()
