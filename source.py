import struct
import numpy as np
from PIL import Image

def read_binary_file(filename):
    """Reads binary data from file and returns the data as a numpy array."""
    with open(filename, 'rb') as f:
        # Read the first 12 bytes to get the shape information
        shape_data = f.read(12)

        # Unpack the shape data
        shape = struct.unpack('3f', shape_data)

        # Read the rest of the data
        data = np.fromfile(f, dtype=np.float32)
        
    return shape, data

def display_shape(shape):
    """Displays the values for the shape [NLAYERS, NROWS, NCOLUMNS]."""
    print("Number of Layers (NLAYERS):", int(shape[0]))
    print("Number of Rows (NROWS):", int(shape[1]))
    print("Number of Columns (NCOLUMNS):", int(shape[2]))


def display_min_max(data):
    """Displays the minimum and maximum values in the data."""
    print("Minimum value:", np.min(data))
    print("Maximum value:", np.max(data))


def max_value_projection(shape, data):
    """Creates a maximum value projection image from the data."""
    # Convert shape to integers
    shape = tuple(map(int, shape))
    # Reshape the data into a 3D volume
    volume = data.reshape(shape)
    # Calculate the maximum value projection
    max_projection = np.max(volume, axis=0)
    # Normalize the values to the range 0..255
    max_projection = (max_projection - np.min(max_projection)) / (np.max(max_projection) - np.min(max_projection)) * 255
    # Convert to uint8 for PIL
    max_projection = max_projection.astype(np.uint8)
    # Create PIL image
    img = Image.fromarray(max_projection)
    return img



def main():
    # Read binary file
    filename = 'mri.bin'
    shape, data = read_binary_file(filename)
    #Displays the values for the Shape 
    display_shape(shape)
    #displays the minimum and maximum values of entries in volume V.
    display_min_max(data)
    #creates a PNG image of the maximum value projection of V.
    img = max_value_projection(shape, data)
    img.save('max_projection.png')
    print("Maximum value projection image of V saved as max_projection.png")
   


if __name__ == "__main__":
    main()
