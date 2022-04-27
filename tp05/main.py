#!/usr/bin/env python


def read_lines(file):
    with open(file) as f:
        for line in f:
            yield line.strip()

def read_cols(line_generator):
    yield line_generator.split(',')[-1]
    

def filter(col_generator):
    if col_generator == "true":
        yield True


def main():
    file_name = "data.csv"
    lines = (line for line in open(file_name))
    list_lines = (line.strip().split(",") for line in lines)
    # all_dones = (data[-1] for data in list_lines)
    # dones = (True for d in all_dones if d == "true")

    # cpt = sum(dones)
    # print(cpt)
    maliste = list(list_lines)
    print(len(maliste))


def main02():
    file_name = "data.csv"
    
    g1 = read_lines(file_name)
    next(g1)
    

    cpt = 0
    for line in g1:
        g2 = read_cols(line)
        for col in g2:
            g3 = filter(col)
            for done in g3:
                cpt+=1
                print(done)
    
    print(cpt)


def main01():
    f = None
    # try:
    #     f = open("data.csv")

    # finally:
    #     print("close")
    #     f.close()


    cpt = 0
    with open("data.csv") as f:

        for line in f:
            print(line)
        # lines = f.readlines()
        # for line in lines:
        #     line = line.strip()
        #     cols = line.split(',')
            
        #     cpt+=1 if cols[-1] == 'true' else 0
            
            # cpt = cols[-1] == 'true' ? cpt+1:cpt
            # if cols[-1] == 'true':
            #     cpt+=1
            # else:
            #     cpt+=0


    
    print(cpt)
    print(f.closed)
if __name__ == '__main__':
    main()