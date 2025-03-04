# PythonProjesi
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):  # Eğer öğe bir liste ise
            result.extend(flatten(item))  # Özyinelemeli olarak aç
        else:
            result.append(item)  # Değilse doğrudan ekle
    return result

# Örnek kullanım:
input_list = [[1, 'a', ['cat', 2], 2], [[[3]], 'dog'], 4, 5]
output_list = flatten(input_list)
print(output_list)
------
def reverse_list(lst):
    reversed_lst = []
    for item in reversed(lst):  # Ana listeyi ters çevir
        if isinstance(item, list):  # Eğer öğe bir liste ise
            reversed_lst.append(reverse_list(item))  # İçeriği de ters çevirerek ekle
        else:
            reversed_lst.append(item)
    return reversed_lst

# Örnek kullanım:
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_list(input_list)
print(output_list)
