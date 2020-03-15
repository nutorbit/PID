import click
import numpy as np
import matplotlib.pyplot as plt

from agent import Robot


@click.command()
@click.option('--n', default=100)
@click.option('--speed', default=1)
@click.argument('tau_p')
@click.argument('tau_d')
def main(n, speed, tau_p, tau_d):
    robot = Robot()
    robot.set(0, 1, 0)

    x_trajectory, y_trajectory = [], []
    prev_cte = robot.y

    for _ in range(n):
        cte = robot.y
        diff_cte = cte - prev_cte
        prev_cte = cte

        steer = -float(tau_p) * cte -float(tau_d) * diff_cte
        robot.move(steer, speed)
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)

    fig, ax = plt.subplots(1, 1, figsize=(8,8))
    ax.plot(x_trajectory, y_trajectory, 'g', label='PID controller')
    ax.plot(x_trajectory, np.zeros(n), 'r', label='reference')
    plt.show()


if __name__ == "__main__":
    main()