Imaging Intern Coding Exercise for Flatiron Internship

This program implements the coding excerise in Python. It accomplishes the following objectives:

1. Display the values for the shape [NLAYERS, NROWS, NCOLUMNS].
2. Display the minimum and maximum values for the entries in the volume V.
3. Create a PNG image of the maximum value projection for V.

The maximum value projection for V is an image I of size NROWS by NCOLUMNS where each pixel I[row, column] represents the maximum value of V[layer, row, column] for all NLAYERS layers.

## Prerequisites

Before running the program, make sure you have the following installed:

- Python 3.x
- NumPy
- Pillow

You can install NumPy and Pillow using pip:

pip install numpy pillow

## How to Run

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the source code.

3. Create a virtual environment:
   ```bash
   python -m venv myenv
   ```
4. Activate the virtual enviroment
   On windows:-myenv\Scripts\activate
   on mac:-source myenv/bin/activate

5. Run the python script -python source.py

After running the script, you will find the following output files:

output_values.png: Contains the values displayed for the shape and minimum/maximum values.
maxvalue_projection.png: Contains the PNG image of the maximum value projection.
