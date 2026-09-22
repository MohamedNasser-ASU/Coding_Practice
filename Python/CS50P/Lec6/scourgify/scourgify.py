import sys
import csv
def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    try:
        # write
        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames= ["first","last","house"])
            writer.writeheader()
            # read
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                # kol ma y read row mn el input.csv yktebo bel shakl el gdeed fi el output.csv
                for row in reader:
                    name = row["name"]
                    last, first= name.split(',')
                    writer.writerow({"first": first.strip(), "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
main()
