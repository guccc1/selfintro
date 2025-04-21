import pyxel

class QuizGame:
    def __init__(self):
        pyxel.init(160, 120, title="クイズゲーム", fps=30)
        self.questions = [
            {"question": "富士山は日本で一番高い山？", "answer": "A"},
            {"question": "ピカチュウは水タイプ？", "answer": "B"},
            {"question": "東京は日本の首都？", "answer": "A"}
        ]
        self.current = 0
        self.score = 0
        self.message = "Z: はい（A）  X: いいえ（B）"
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Z):
            self.check_answer("A")
        elif pyxel.btnp(pyxel.KEY_X):
            self.check_answer("B")

    def check_answer(self, user_answer):
        correct_answer = self.questions[self.current]["answer"]
        if user_answer == correct_answer:
            self.score += 1
            self.message = "正解！"
        else:
            self.message = "不正解！"
        
        pyxel.play(0, 0)
        pyxel.delay(300)  # 少し待つ
        self.current += 1
        if self.current >= len(self.questions):
            self.current = -1  # ゲーム終了

    def draw(self):
        pyxel.cls(0)
        if self.current == -1:
            pyxel.text(10, 40, f"ゲーム終了！スコア: {self.score}", pyxel.frame_count % 16)
            pyxel.text(10, 60, "F5で再読み込みしてリスタート", 7)
        else:
            q = self.questions[self.current]["question"]
            pyxel.text(10, 30, f"Q{self.current+1}: {q}", 7)
            pyxel.text(10, 60, self.message, 11)
