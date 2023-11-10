def mean_vs_median(seq):
    #перевірка чи масив взагалі непарної довжини
    if len(seq) % 2 == 0:
        print("Послідовність має бути непарної довжини.")
        return
    seq_sum = 0
    #рахую суму
    for i in seq:
        seq_sum += i
    #бабль гум
    for i in range(len(seq)):
        for j in range(len(seq)-i-1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    #шукаю середнє значення та медіану
    mean_value = seq_sum / len(seq)
    median_value = seq[len(seq) // 2]
    #ну і виводжу
    if mean_value > median_value:
        print("mean")
    elif median_value > mean_value:
        print("median")
    else:
        print("same")
#викликаю функцію
mean_vs_median([1, 2, 3, 4])
mean_vs_median([1, 2, 3, 4, 5])
mean_vs_median([2, 4, 5, 7, 8])
mean_vs_median([2, 2, 5, 7, 8])
