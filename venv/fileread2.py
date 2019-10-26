# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
x = 0
number = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x = x + 1
    pos = line.find(':')
    number = number + float(line[pos+1:].rstrip())
print(number/x)
print("Done")
