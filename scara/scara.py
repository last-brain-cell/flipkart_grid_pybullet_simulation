import pybullet as p

# Initialize PyBullet simulation
physicsClient = p.connect(p.GUI)
p.setGravity(0, 0, -9.81)

# Load the URDF file
robot = p.loadURDF("scara.urdf", [0, 0, 0], useFixedBase=True)

# Simulation loop
while True:
    p.stepSimulation()


# Disconnect from the simulation
# p.disconnect()
