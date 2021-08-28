#-*- coding:utf-8 -*-
"""
プレイゾーン
"""


class Area:
    def __init__(self, player):
        self.deck = player.deck  # 山札
        self.player_name = player.name  # プレイヤー名
        self.hands = []  # 手札
        self.fight = []  # バトル場
        self.bench = []  # ベンチ
        self.trash = []  # トラッシュ
        self.max_sides = player.deck.remain() // 10  # サイドにおける枚数
        self.sides = []  # サイド
        # self.studium = []  # スタジアムカード置き場
