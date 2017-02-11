# Cole Hocking
# Hashing Algorithm

from sys import exit

file1 = 'hw3a.txt'
file2 = 'hw3b.txt'
file3 = 'hw3c.txt'
# pick a prime number of buckets + 1 overflow bucket
num_buckets = 18
max_size = 4500

################################################################################


def new():
    hset = []
    for i in range(0, num_buckets):
        hset.append([])
    return hset
bucketlist = new()

################################################################################


def add_to_list(item, blist):
    # decide which bucket to place integer
    bucket = hash(item) % (num_buckets-1)
    # send to overflow if bucket full
    if len(blist[bucket]) >= max_size:
        blist[num_buckets - 1].append(item)
    else:
        blist[bucket].append(item)

################################################################################


def add_files():
    file_list = [file1, file2, file3]
    for filei in file_list:
        with open(filei) as f:
            ctr = 0
            err_ctr = 0
            for line in f:
                ctr += 1
                while True:
                    try:
                        item = int(line)
                        add_to_list(item, bucketlist)
                        break
                    except ValueError:
                        err_ctr += 1
                        # limiting number of errors code will skip w/o terminate
                        if err_ctr > 3:
                            exit("Too many non-integers. Use valid data files.")
                        else:
                            print("Data on line %d in %r not an integer:"
                                  "\nExcluded from list." % (ctr, filei))
                    break
            print("Size of the set of integers in %r: %d" % (filei, ctr))
add_files()

################################################################################


def output_info():
    print("Spots in each bucket: %d" % max_size)
    print("buckets created: %d" % len(bucketlist))
    print("Number of integers in buckets 0 - 17: ")
    print([len(x) for (x) in bucketlist])
    print("Size of overflow bucket:")
    print(len(bucketlist[17]))
output_info()


################################################################################
