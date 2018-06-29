import csv

def main(): 
  with open('SampleHousingData.csv', 'rU') as csvfile:
    spamreader = csv.reader(csvfile, dialect=csv.excel_tab)
    for row in spamreader:
      print ', '.join(row)


if __name__ == "__main__":
    main()

