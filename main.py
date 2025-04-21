import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, title="3択クイズゲーム")
        self.question = "宅建は何の略？"
        self.choices = ["宅地建物取引士", "宅急便検定", "宅飲み検定"]
        self.answer_index = 0
        self.selected_index = 0
        self.message = ""
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_UP):
            self.selected_index = (self.selected_index - 1) % len(self.choices)
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.selected_index = (self.selected_index + 1) % len(self.choices)
        if pyxel.btnp(pyxel.KEY_RETURN):
            if self.selected_index == self.answer_index:
                self.message = "正解！"
            else:
                self.message = "不正解…"

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, self.question, 7)
        for i, choice in enumerate(self.choices):
            prefix = ">" if i == self.selected_index else " "
            pyxel.text(10, 30 + i * 10, f"{prefix} {choice}", 6 if i == self.selected_index else 7)
        pyxel.text(10, 70, self.message, 8)

App()
