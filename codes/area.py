#-*- coding:utf-8 -*-
"""
プレイゾーン
"""


class Area:
    def __init__(self, deck):
        self.deck = deck  # 山札
        self.hands = []  # 手札
        self.fight = []  # バトル場
        self.bench = []  # ベンチ
        self.trash = []  # トラッシュ
        self.sides = []  # サイド
        self.max_sides = deck.remain() // 10  # サイドにおける枚数
        self.studium = []  # スタジアムカード置き場
