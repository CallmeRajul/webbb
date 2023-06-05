print('silahkan masukan modal')
modal = int(input())
print('silahkan masukan harga beli dari produk')
produk = int(input())
print('silahkan masukan target keuntungan')
target = int(input())

keuntungan = target - modal 

print('silahkan masukan harga jual untuk setiap produk')
jual = int(input())
keuntunganJual = jual - produk
targetpenjualan = target / keuntunganJual
print('anda harus menjual setidaknya ',targetpenjualan, 'untuk mendapat uang ',target)
bisajual = modal/produk
keuntunganlangsung = bisajual * targetpenjualan
print('tapi anda hanya bisa menjual ', bisajual , 'dan mendapat keuntungan ',keuntunganlangsung)