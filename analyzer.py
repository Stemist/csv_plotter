#!/user/bin/env python3

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import make_data


def main():
    # Generate data using imported module
    make_data.main()

    # path = os.path.relpath('./data_generator/')
    # print('Path: ', path)
    file = '2D_dataset.csv'
    
    # Open data file
    try:
        data = pd.read_csv(file)

    except Exception:
        print('Cannot import file.')
     

    # Display imported data
    print("Data imported from file: ")
    print(data)
    
    # Display analysis of data -- Needs fix. data.

    # Generate plots   
    data.plot(kind='scatter', x='Height',y='Weight',color='red')     
    plt.show()



if __name__ == '__main__':
    main()