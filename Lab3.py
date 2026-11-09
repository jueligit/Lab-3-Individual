# CIS-117 Lab 3
# This program will read the country_full.csv and divide
# the countries according to their regions, then place them 
# into seperate CSV files with just the country name and region.
# Authors : Julia Ueligitone

import csv

try: 

    with open('country_full.csv', "r") as rf:
        csv_reader = csv.reader(rf)
        next(csv_reader)  # Skip the header row
        regions = {}
        for cells in csv_reader:
            country_name = cells[0]
            region = cells[5]
            if region != "":
                if region not in regions:
                    regions[region] = []
                regions[region].append([country_name, region])

        for region_name in regions:
            filename = region_name + ".csv"
            with open(filename, "w", newline="") as wf:
                csv_writer = csv.writer(wf)
                csv_writer.writerow(["name", "region"])
                csv_writer.writerows(regions[region_name])

    print("files created successfully!")
except FileNotFoundError:
    print("Error: country_full.csv not found.")
except PermissionError:
    print("Error: Permission denied for access to file.")
except IOError:
    print("Error: An input/output error occurred while reading or writing the file.")
except Exception as e:
    print("An unexpected error occurred:", e)