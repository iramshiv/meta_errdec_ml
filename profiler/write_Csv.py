import csv


def write_csv(fname, df, cname, cname1):
    with open(fname, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(cname)
        for x in df[cname1[0]]:
            writer.writerow([x])


def write_csv1(fname, cname):
    with open(fname, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(cname)


def write_csv_r(fname, cname, x):
    with open(fname, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(cname)
        writer.writerows([x])

def write_csv_ro(fname, cname, x):
    with open(fname, 'w', newline='') as file:
        writer = csv.writer(file)
        for c in cname:
            writer.writerow(c)
        for x1 in x:
            writer.writerows([x1])