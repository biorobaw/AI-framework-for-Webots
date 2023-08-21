import numpy as np
from scipy.special import softmax

def add_motion_bias(available_actions, previous_action_index):
    if previous_action_index == -1:
        return available_actions
    else:
        action_distribution = [i for i in available_actions]
        # Previous action bias
        action_distribution[previous_action_index] += 1
        # Adjacent action bias
        action_distribution[(previous_action_index - 1) % 8] += .5
        action_distribution[(previous_action_index + 1) % 8] += .5
        # Orthogonal action bias
        action_distribution[(previous_action_index - 2) % 8] += .25
        action_distribution[(previous_action_index + 2) % 8] += .25
        # Eliminate not available actions
        action_distribution = np.multiply(action_distribution, available_actions)
    return action_distribution

def apply_softmax(action_distrabution):
    return softmax(action_distrabution)