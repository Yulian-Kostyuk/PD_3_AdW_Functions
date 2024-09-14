list_true = []
def calculate_structure_sum(list_):
  new_list = []
  only_items = []
  for i in list_:
    if isinstance(i, list) or isinstance(i, tuple):
      for j in i:
        new_list.append(j)
        only_items.append(False)
    elif isinstance(i, dict):
      for key, value_ in i.items():
        new_list.append(key)
        new_list.append(value_)
        only_items.append(False)
    elif isinstance(i, set):
      i_list = list(i)
      for j in i_list:
        new_list.append(j)
        only_items.append(False)
    else:
      new_list.append(i)
      only_items.append(True)
  global list_true
  if False in only_items:
    false_pos = only_items.index(False)
    list_true.extend(new_list[0:false_pos])
    return calculate_structure_sum(new_list[false_pos:])
  else:
    list_true.extend(new_list)
    sum_ = 0
    for j in list_true:
      if isinstance(j, int):
        sum_ += j
      elif isinstance(j, str):
        sum_ += len(j)
      else:
        print('Неверный тип элемента списка! Должен быть либо числом, либо строкой')
    return sum_


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)