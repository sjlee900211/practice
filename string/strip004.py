coffee_menu = " 에스프레소, 아메리카노, 카페라떼    , 카푸치노  "
coffee_menu_list = coffee_menu.split(',')
coffee_menu_list


coffee_list = []
for coffee in coffee_menu_list:
    temp = coffee.strip()
    coffee_list.append(temp)
print(coffee_list)