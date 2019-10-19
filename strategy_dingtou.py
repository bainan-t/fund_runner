#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# File   : strategy_dingtou
# Date   : 2019/9/1 0001
# Author : Chen Ji
# Email  : fzls.zju@gmail.com
# -------------------------------
import datetime

from strategy_inteface import StrategyInterface


class DingtouStrategy(StrategyInterface):
    def name(self) -> str:
        return "定投-%d天" % self.days

    def __init__(self, days):
        self.days = days
        self.period = datetime.timedelta(days=days)
        self.last_time = datetime.datetime(1970, 1, 1)

    def run(self, time: str, net_values: list, profits: list, decision_shares: list, current_share: float,
            current_invest_money: float, sell_money: float) -> float:
        # 最简单的每周定投
        t = datetime.datetime.strptime(time, "%Y-%m-%d")
        if t - self.last_time >= self.period:  # 每周期定投400/30*周期天数（每个基金一个月400元）
            self.last_time = t
            return 400.0/30*self.days

        return 0.0
