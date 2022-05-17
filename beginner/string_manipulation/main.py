a = "Temukan "
b = "dengan potongan 55%! Hanya Rp"
c = ". Dapatkan sekarang juga di Shopee! "
t = "Temukan Sipolos Celana Pendek Chino Pants Regular Fit dengan potongan 55%! Hanya Rp149.000. Dapatkan sekarang juga di Shopee! https:linkrandom"

step1 = t.replace(a, '')
step2 = step1.replace(b, '+')
step3 = step2.replace(c, '+')
print(step3)

arrstring = step3.split('+')
print(arrstring)

nama = arrstring[0]
harga = arrstring[1]
link = arrstring[2]

print(nama)
print(harga)
print(link)
