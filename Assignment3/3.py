def filter_id(a):
    l1 = [{'id': 1, 'name': 'ernakulam'}, {'id': 2, 'name': 'Thrissur'}, {'id': 3, 'name': 'Kollam'},
          {'id': 4, 'name': 'Kozhikode'}, {'id': 5, 'name': 'Kottayam'}]
    filtered = list(filter(lambda x: x['id'] == int(a), l1))
    return filtered[0]['name'] if filtered else None

x = input("Enter the ID to search: ")
name = filter_id(x)
if name:
    print("Name corresponding to the ID:", name)
else:
    print("ID not found.")
