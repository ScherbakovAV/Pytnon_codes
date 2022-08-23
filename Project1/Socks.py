num_red_socks = int(input('Введите количество красных носков (от 1 до 100)...................................'))
num_blue_socks = int(input('Введите количество синих носков (от 1 до 100).....................................'))
count_diff = 0
count_one = 0
if 1 <= num_red_socks <= 100 and 1 <= num_blue_socks <= 100:
    if num_red_socks > num_blue_socks:
        count_diff = num_blue_socks
        count_one = (num_red_socks - num_blue_socks) // 2
    if num_red_socks < num_blue_socks:
        count_diff = num_red_socks
        count_one = (num_blue_socks - num_red_socks) // 2
    if num_red_socks == num_blue_socks:
        count_diff = num_red_socks
        count_one = 0
    print('Максимальное количество дней, в которые можно носить разноцветные носки:.........', count_diff)
    print('Количество дней, в которое можно носить одноцветные носки после разноцветных:....', count_one)
else:
    print('Введено неверное количество носков, работа программы завершена.')
