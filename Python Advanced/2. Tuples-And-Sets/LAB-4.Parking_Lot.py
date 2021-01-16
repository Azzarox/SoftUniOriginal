def input_lines(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def main_logic(data):
    parking_lot = set()
    for car in data:
        command, car_number = car.split(', ')
        if command == "IN":
            parking_lot.add(car_number)
        else:
            parking_lot.remove(car_number)

    return parking_lot


def print_result(parking_lot):
    if parking_lot:
        for car in parking_lot:
            print(car)
    else:
        print('Parking Lot is Empty')


n = int(input())

lines_data = input_lines(n)
result = main_logic(lines_data)
print_result(result)


# TODO: от презентацията:
# def input_to_list(count):
#     lines = []
#     for _ in range(count):
#         lines.append(input())
#
#     return lines
#
#
# def print_result(parking_lot):
#     if parking_lot:
#         for car in parking_lot:
#             print(car)
#     else:
#         print('Parking Lot is Empty')
#
#
# #
# # lines = [
# #     'IN, CA2844AA',
# #     'IN, CA1234TA',
# #     'OUT, CA2844AA',
# #     'IN, CA9999TT',
# #     'IN, CA2866HI',
# #     'OUT, CA1234TA',
# #     'IN, CA2844AA',
# #     'OUT, CA2866HI',
# #     'IN, CA9876HH',
# #     'IN, CA2822UU',
# # ]
# # lines = [
# #     'IN, CA2844AA',
# #     'IN, CA1234TA',
# #     'OUT, CA2844AA',
# #     'OUT, CA1234TA',
# # ]
#
# n = int(input())
# lines = input_to_list(n)
#
# parking_lot = set()
#
# for line in lines:
#     command, car = line.split(', ')
#     if command == 'IN':
#         parking_lot.add(car)
#     else:
#         parking_lot.remove(car)
#
# print_result(parking_lot)