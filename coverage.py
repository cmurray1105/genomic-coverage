import csv
# skip first line i.e. read header first and then iterate over each row od csv as a list


def write_coverage():
    counts = {}
    with open('reads.csv', 'r') as read_obj:
      csv_reader = csv.reader(read_obj)
      header = next(csv_reader)
      # Check file as empty
      if header != None:
      # Iterate over each row after the header in the csv
        for row in csv_reader:
        # row variable is a list that represents a row in csv
          coverage = [*range(int(row[0]), (int(row[0]) + int(row[1])), 1)]
       # iterate through the coverage list and create a value key pair for each unique value and increment the count for each existing value
          for element in coverage:
            if element in counts:
              counts[element] += 1
            else:
              # print(type(element))
              counts[element] = 1
    new_output = []
    with open('loci.csv', 'r') as read_obj:
      csv_reader = csv.reader(read_obj)
      header = next(csv_reader)
    # Check file as empty
      if header != None:
        for row in csv_reader:
          if int(row[0]) in counts:
            idx = int(row[0])
            new_row = [row[0], counts[idx]]
            new_output.append(new_row)
          else:
            new_output.append([row[0], 0])
    with open('loci.csv', 'w') as csvfile:
      csvwriter = csv.writer(csvfile)
      csvwriter.writerow(['position', 'coverage'])
      # writer.writeheader()
      for element in new_output:
        csvwriter.writerow(element)
