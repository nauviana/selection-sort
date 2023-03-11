def seleksi(data):
    iterasi = 0
    for i in range (len(data)-1):
        minimal = i
        for j in range (i+1, len(data)):
            if data [j] < data [minimal]:
                minimal = j
        iterasi +=1
        data[minimal], data[i]=data[i], data [minimal]
        print(iterasi, data)

data = [60,4,26,11,52,33,88,44,29,76,17,94]

print('Angka yang akan di sort :\n', data )
print('Selection Sort :\n')
seleksi(data)