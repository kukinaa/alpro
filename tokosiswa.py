transaksi = 'y'
while transaksi == 'y':
    no_transaksi = input('no transasksi: ')
    nama = input('nama pelanggan: ')
    tipe_member = input('tipe member: ')
    tanggal_transaksi = input('tanggal transaksi: ')

    if tipe_member == 'platinum':
        diskon = 0.15
    elif tipe_member == 'gold':
        diskon = 0.10
    elif tipe_member == 'silver':
        diskon = 0.05
    else: 
        diskon = 0

    lagi = 'y'
    sub_total = 0
    total = 0

    while lagi == 'y':
        kode = input('masukan kode barang: ')
        if kode == 'b001':
            nama_barang = 'buku tulis'
            harga = 15000
        elif kode == 'b002':
            nama_barang = 'buku gambar'
            harga = 12000
        elif kode == 'b003':
            nama_barang = 'pulpen gel'
            harga = 8000
        elif kode == 'a001':
            nama_barang = 'pensil 2b'
            harga = 5000
        else:
            nama_barang = 'penggaris'
            harga = 7000

        print(f'nama barang: {nama_barang}')
        print(f'harga barang: {harga}')
        jumlah = int(input('banyaknya: '))
        sub_total = harga * jumlah
        total = total + sub_total
        lagi = input('apakah anda ingin menambah item lagi? (y/t): ')

    print('-------------------------------------------------------------')
    print(f'total transaksi: {total}')
    potdis = diskon * total
    print(f'potongan diskon: {potdis}')
    admin = 5000
    print(f'biaya admin: {admin}')
    total_bayar = total - potdis + admin
    print(f'total bayar: {total_bayar}')
    transaksi = input('apakah anda ingin menambah transasksi lagi? (y/t): ')
    print('---------------------------------------------------------------')
    