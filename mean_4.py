from pathlib import Path

data = [float(i.replace(",", ".")) for i in Path("C:\\Users\\DIANA\\Downloads\\CdSe_CdZnS Core_Shell.txt").read_text().split()]
data_x = [i for i in data if data.index(i) % 2 == 0]
data_y = [i for i in data if data.index(i) % 2 != 0]


def mean_dev(s):
    len_s = len(s)
    mean_data = sum(s) / len_s
    delta_mean_dev = [abs(x - mean_data) for x in s]
    mean_d = sum(delta_mean_dev) / len_s
    return mean_d


def mean_sqr(s):
    len_s = len(s)
    mean_data = sum(s) / len(s)
    delta_mean_sqr = [(x - mean_data) ** 2 for x in s]
    mean_sq = (sum(delta_mean_sqr) / len_s) ** 0.5
    return mean_sq


# 1 способ
print('1 способ:')
print(f'Среднее отклонение первой величины {mean_dev(data_x)}')
print(f'Среднеквадратичное отклонение первой величины {mean_sqr(data_x)}')
print()
print(f'Среднее отклонение второй величины = {mean_dev(data_y)}')
print(f'Среднеквадратичное второй величины = {mean_sqr(data_y)}')

# 2 способ
print()
print('2 способ:')
print(f'Среднее отклонение величины {mean_dev(data_x)}')
print(f'Среднеквадратичное отклонение величины {mean_sqr(data_x)}')

# 3 способ
print()
print('3 способ:')
print(f'Среднее отклонение величины = {mean_dev(data_y)}')
print(f'Среднеквадратичное величины = {mean_sqr(data_y)}')
