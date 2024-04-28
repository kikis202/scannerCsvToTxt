import csv
import argparse

output_text_file = './output.txt'

def parse_csv(input_csv_file):
  # Open the CSV file and create a new text file for output
  with open(input_csv_file, mode='r', encoding='utf-8', newline='') as csvfile, \
    open(output_text_file, mode='w', encoding='utf-8') as txtfile:
      csvfile.readline()  # Skip the first line which contains "sep=,"
      reader = csv.DictReader(csvfile)
      
      for row in reader:
        quantity = row['Quantity'].strip()
        card_name = row['Card Name'].strip()

        txtfile.write(f"{quantity}x {card_name}\n")

  print("Data has been successfully extracted and saved.")

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--path", help="Path to the input CSV file. Default: `./input.csv`", default="./input.csv")
  args = parser.parse_args()
  input_csv_file = args.path

  parse_csv(input_csv_file)

if __name__ == "__main__":
  main()