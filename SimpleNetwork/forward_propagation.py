import numpy as np


def relu(input):
    '''Define your relu activation function here'''
    # Calculate the value for the output of the relu function: output
    output = max(0, input)
    
    # Return the value just calculated
    return(output)


weights = {
           'node_0': np.array([2, 4]), 
           'node_1': np.array([ 4, -5]), 
           'output': np.array([2, 7])
          }

if __name__ == '__main__':

    input_data = np.array([3, 5])

    # Calculate node 0 value: node_0_output
    node_0_input = (input_data * weights['node_0']).sum()
    node_0_output = relu(node_0_input)

    # Calculate node 1 value: node_1_output
    node_1_input = (input_data * weights['node_1']).sum()
    node_1_output = relu(node_1_input)

    # Put node values into array: hidden_layer_outputs
    hidden_layer_outputs = np.array([node_0_output, node_1_output])

    # Calculate model output (do not apply relu)
    model_output = (hidden_layer_outputs * weights['output']).sum()

    # Print model output
    print(model_output)