class controller:
    """ Implements a floating controller that only compensates for
    the effects of gravity on the arm.
    """

    def __init__(self, robot_config):

        self.robot_config = robot_config

    def control(self, q, dq):
        """ Generates the control signal

        q np.array: the current joint angles
        dq np.array: the current joint velocities
        """

        # calculate the effect of gravity in joint space
        g = self.robot_config.g(q)
        u = -g

        return u
