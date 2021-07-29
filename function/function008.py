list_data = ['abc', 1, 2, 'def']
tuple_data = ('abc', 1, 2, 'def')
set_data = {'abc', 1, 2, 'def'}

[type(list_data), type(tuple_data), type(set_data)]

print("리스트로 변환 : ", list(tuple_data), list(set_data))

print("튜플로 변환 : ", tuple(list_data), tuple(set_data))

print("세트로 변환 : ", set(list_data), set(tuple_data))