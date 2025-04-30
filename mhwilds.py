import random

"""
ランダムで1体のモンスターを返す
"""
class MonsterHunterWildsBot:
    def __init__(self, monster_list="monsters.txt"):
        self.monster_list = self.load_monsters(monster_list)

    def load_monsters(self, file_path):
        monsters = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        if ',' in line:
                            number, name =line.split(',', 1)
                            monsters[int(number.strip())] = name.strip()
                        # else:
                        #     # 番号がない場合にリスト順に番号を振る
                        #     monsters[len(monsters) + 1] = line
        except FileNotFoundError:
            print(f"MonsterHunterWilds -> MonsterList is NotFound[error:002]")
            return {}
        return monsters
    
    def seggest_monster(self):
        """
        MonsterHunterWildsに実装されているモンスターの狩猟可能なリストからランダムに1体提案する
        """
        if not self.monster_list:
            return "好きなモンスターを狩るッピ！"
        monster_numbers = list(self.monster_list.keys())
        random_number = random.choice(monster_numbers)
        suggested_monster = self.monster_list[random_number]
        return f"【{suggested_monster}】を狩るッピ！"
    
if __name__ == "__main__":
    # 単独実行時テスト
    bot = MonsterHunterWildsBot()
    suggestion = bot.seggest_monster()
    print(suggestion)