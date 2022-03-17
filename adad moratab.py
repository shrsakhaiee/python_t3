
array = []
tedad_daryaft_adad = int (input("tedad adad ra vared konid:"))

for i in range (0,tedad_daryaft_adad):
    adad = int (input("adad ra vared konid:"))
    array.append(adad)
arraye_sort = sorted(array)
if arraye_sort == array:
    print("moratab shode")
else:
    print("moratab nashode", arraye_sort)