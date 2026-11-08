from datetime import datetime
from rqrisk import Risk
from dateutil.relativedelta import relativedelta
from rqdatac.validators import ensure_date_range
import rqdatac
from pandas import DataFrame


def calc_max_drawback(
    order_book_id: str,
    start_date: None | datetime | str | int = None,
    end_date: None | datetime | str | int = None,
    benchmark_id: None | str = None,
) -> float:
    benchmark_id = benchmark_id or "000300.XSHG"
    start_date, end_date = ensure_date_range(start_date, end_date, delta=relativedelta(years=10))
    prices = rqdatac.get_price([order_book_id, benchmark_id], start_date, end_date, fields=["close"])["close"]
    daily_returns = prices.groupby("order_book_id").pct_change().dropna()
    risk = Risk(daily_returns[order_book_id], daily_returns[benchmark_id], 0)
    return risk.max_drawdown
