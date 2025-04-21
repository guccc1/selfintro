import pyxel

# クイズの質問と回答を定義
questions = [
    {"question": "フランスの首都はどこですか？", "options": ["パリ", "ロンドン", "ベルリン", "マドリード"], "answer": 0},
    {"question": "2 + 2 はいくつですか？", "options": ["3", "4", "5", "6"], "answer": 1},
    {"question": "太陽系で最大の惑星はどれですか？", "options": ["地球", "火星", "木星", "土星"], "answer": 2},
]

current_question = 0
selected_option = -1
score = 0

def update():
    global current_question, selected_option, score
    
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    
    if pyxel.btnp(pyxel.KEY_UP):
        selected_option = (selected_option - 1) % len(questions[current_question]["options"])
    
    if pyxel.btnp(pyxel.KEY_DOWN):
        selected_option = (selected_option + 1) % len(questions[current_question]["options"])
    
    if pyxel.btnp(pyxel.KEY_RETURN):
        if selected_option == questions[current_question]["answer"]:
            score += 1
        current_question += 1
        selected_option = -1
        if current_question >= len(questions):
            current_question = 0

def draw():
    pyxel.cls(0)
    
    if current_question < len(questions):
        pyxel.text(10, 10, questions[current_question]["question"], pyxel.COLOR_WHITE)
        
        for i, option in enumerate(questions[current_question]["options"]):
            color = pyxel.COLOR_YELLOW if i == selected_option else pyxel.COLOR_WHITE
            pyxel.text(10, 30 + i * 10, option, color)
        
        pyxel.text(10, 70, f"Score: {score}", pyxel.COLOR_WHITE)
    else:
        pyxel.text(10, 10, f"Quiz Finished! Your score: {score}", pyxel.COLOR_WHITE)

pyxel.init(160, 120)
pyxel.run(update, draw)
