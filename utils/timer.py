"""
timer.py: Modul pro měření času hraní her

author: Štefan Barát
email: barat70671@mot.sps-dopravni.cz
discord: hatsukooo
"""

import time


def start_timer():
    """
    Spustí časovač.

    Returns:
        float: Čas začátku (timestamp)
    """
    return time.time()


def stop_timer(start_time):
    """
    Zastaví časovač a vypočítá uplynulý čas.

    Args:
        start_time (float): Čas začátku z start_timer()

    Returns:
        float: Uplynulý čas v sekundách
    """
    return time.time() - start_time


def format_time(seconds):
    """
    Naformátuje čas do čitelného formátu.

    Args:
        seconds (float): Čas v sekundách

    Returns:
        str: Formátovaný čas (např. "2m 34s" nebo "45s")
    """
    if seconds < 60:
        return f"{int(seconds)}s"
    else:
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        return f"{minutes}m {secs}s"
