import click
import numpy as np
import matplotlib.pyplot as plt

from agent import Robot


@click.command()
@click.option('--n', default=100)
@click.option('--speed', default=1)
@click.argument('tau_p')
def main(n, speed, tau_p):
    robot = Robot()
    robot.set(0, 1, 0)

    x_trajectory, y_trajectory = [], []
    
    for _ in range(n):
        cte = robot.y
        steer = -float(tau_p) * cte
        robot.move(steer, speed)
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)

    fig, ax = plt.subplots(1, 1, figsize=(8,8))
    ax.plot(x_trajectory, y_trajectory, 'g', label='PID controller')
    ax.plot(x_trajectory, np.zeros(n), 'r', label='reference')
    plt.show()


if __name__ == "__main__":
    main()