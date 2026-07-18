import pandas as pd
import numpy as np

def calculate_ap(y_score: np.ndarray, y_true: np.ndarray):
    """
    Расчет классической метрики Average Precision (AP) для бинарной классификации.
    """

    n_positive = np.sum(y_true)

    if n_positive == 0:
        return 0.0
    if n_positive == len(y_true):
        return 1.0
    
    #Сортировка по убыванию скора
    idx = np.argsort(y_score)[::-1]
    y_true_sorted = y_true[idx]

    k = np.arange(1, len(y_true_sorted) + 1)

    #Precision@k
    cumsum_y = np.cumsum(y_true_sorted)
    precision_k = cumsum_y / k

    # AP
    ap = np.sum(y_true_sorted * precision_k) / n_positive

    return ap

def daily_ap(df: pd.DataFrame, y_score_col: str, y_true_col: str, date_col) -> float:
    """
    Расчет целевой посуточной метрики ранжирования Daily Average Precision.
    """
    
    #Считаем ap для каждого дня отдельно
    daily_aps = []

    for date, group in df.groupby(date_col):
        y_true = group[y_true_col].to_numpy()
        y_score = group[y_score_col].to_numpy()

        ap_d = calculate_ap(y_score, y_true)

        daily_aps.append(ap_d)

    return float(np.mean(daily_aps))



