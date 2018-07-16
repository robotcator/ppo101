import os

dir = "./train_part/"

filenames = sorted(os.listdir(dir))

cnt = 0
for idx in range(len(filenames))[::-1]:
    print (filenames[idx])
    cnt += 1
    if cnt > 10:
        break
    os.popen(r'hdfs dfs -put train_part/{0} hdfs://10.150.14.110:9000/v-xiaoji/v5-stable/train_part'.format( filenames[idx] ))