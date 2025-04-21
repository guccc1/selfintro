import pyxel
import random

class QuizGame:
    def __init__(self):
        # 3択問題のリスト
        self.questions = [
            {
                "question": "宅地建物取引業法において、宅地建物取引業者は、契約書面を交付しなければならない期間は？",
                "options": ["契約成立後3日以内", "契約成立後5日以内", "契約成立後7日以内"],
                "answer": 1  # 2番目の選択肢が正解
            },
            {
                "question": "不動産の売買契約において、売主が買主に対して保証するべき義務は？",
                "options": ["瑕疵担保責任", "引き渡し責任", "所有権移転責任"],
                "answer": 0  # 1番目の選択肢が正解
            },
            {
                "question": "不動産の表示において、地積の単位は何ですか？",
                "options": ["平方メートル", "平方フィート", "平方ヤード"],
                "answer": 0  # 1番目の選択肢が正解
            }
        ]
        self.current_question = None
        self.is_correct = None
        self.score = 0
        self.start_game()

    def start_game(self):
        self.next_question()
        pyxel.init(160, 120, title="3宅クイズゲーム")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # ユーザーの入力を受け付け
        if pyxel.btnp(pyxel.KEY_1):
            self.check_answer(0)  # 1番目の選択肢
        elif pyxel.btnp(pyxel.KEY_2):
            self.check_answer(1)  # 2番目の選択肢
        elif pyxel.btnp(pyxel.KEY_3):
            self.check_answer(2)  # 3番目の選択肢

    def check_answer(self, selected_option):
        if selected_option == self.current_question['answer']:
            self.is_correct = True
            self.score += 1
        else:
            self.is_correct = False

        pyxel.timer(30, self.next_question)  # 次の問題に進む

    def next_question(self):
        if len(self.questions) == 0:
            pyxel.quit()  # 問題がなくなったら終了
            return
        
        self.current_question = random.choice(self.questions)  # ランダムに問題を選ぶ
        self.questions.remove(self.current_question)  # 使用した問題を削除

    def draw(self):
        pyxel.cls(0)

        if self.is_correct is None:
            # 問題がまだ表示されていない場合
            pyxel.text(10, 10, self.current_question["question"], pyxel.COLOR_WHITE)
            for i, option in enumerate(self.current_question["options"]):
                pyxel.text(10, 30 + i * 10, f"{i+1}. {option}", pyxel.COLOR_WHITE)
        else:
            if self.is_correct:
                pyxel.text(10, 10, "正解！", pyxel.COLOR_GREEN)
            else:
                pyxel.text(10, 10, "不正解...", pyxel.COLOR_RED)

            # 得点表示
            pyxel.text(10, 50, f"あなたの得点: {self.score}", pyxel.COLOR_WHITE)

        pyxel.text(10, 90, "1, 2, 3で選択してください", pyxel.COLOR_WHITE)

QuizGame()
