def poisk():
    if find_item in items_list:
        return items_list.index(find_item)
    else:
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
for find_item in ['банан', 'груша', 'персик']:
    index_item = poisk()
    if index_item is None:
        print(f"Товар '{find_item}' не найден в списке.")
    else:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")