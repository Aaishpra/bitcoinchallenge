import csv

file = open("block.txt", "w")

with open('mempool.csv') as csvFile:
    
    # Algorithm for maximising the transaction fees
    # 1.Sort the tx_id list in decreasing order so that we can maximize the fees(better to use quicksort for this)
    # 2.Let total_sum[i] = fees[i]* weight[i] and total_fees+= total_sum[i] and total_weight+=weight[i].
    # 3.Using this function iterate over the whole list of tx_id while total_weight < 4000000(max weight of a block).
    # 4.Now print and write the tx_id in reverse order in txt_file.csv.

    readCsv = csv.reader(csvFile)
    for row in readCsv:
        my_tx_id = row[0]
        my_fees = row[1]
        my_weight = row[2]
        my_parents = row[3]
        line = "{}\n".format(my_tx_id)
        file.write(line)

file.close()
