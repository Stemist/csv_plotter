
def main():

    import csv
    import random
    import os

    with open('2D_dataset.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', 
        quotechar='|', quoting=csv.QUOTE_MINIMAL)

        filewriter.writerow(['Height', 'Weight'])

        for i in range(101):
            filewriter.writerow([i, i+random.randint(1,100)])


if __name__ == '__main__':
    main()