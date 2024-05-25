import numpy as np
from scipy.stats import ks_2samp

chat_id = 886180056  # Ваш chat ID, не меняйте название переменной


def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    statistic, p_value = ks_2samp(x, y)
    alpha = 0.07
    return p_value < alpha
