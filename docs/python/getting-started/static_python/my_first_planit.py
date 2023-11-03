from planit import *

# main class
planit = Planit()
# access assignment project
planit_project = planit.create_project()

# COMPONENTS
planit_project.set(TrafficAssignment.TRADITIONAL_STATIC)         
planit_project.assignment.set(PhysicalCost.BPR)
planit_project.assignment.set(VirtualCost.FIXED)
planit_project.assignment.set(Smoothing.MSA)

# CONFIGURE COST COMPONENT
# 	BPR Travel time function
alpha = 0.9
beta = 4.5
planit_project.assignment.physical_cost.set_default_parameters(alpha, beta)

# CONFIGURE OUTPUT
planit_project.assignment.output_configuration.set_persist_only_final_Iteration(True)

# RUN ASSIGNMENT
planit_project.run()