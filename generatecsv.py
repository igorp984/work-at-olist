import csv
from faker import Faker
import sys


def generateCSV(records, fileName):
    fake = Faker()
    with open(fileName, 'wt') as csvAuthors:
        writer = csv.DictWriter(csvAuthors, fieldnames=["Name"])
        for _ in range(records):
            name = fake.name()
            writer.writerow({"Name": name})


if __name__ == "__main__":
    fileName = sys.argv[1]
    records = int(sys.argv[2])
    generateCSV(records, fileName)
