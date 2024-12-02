from flask import Flask, render_template, request

app = Flask(__name__)

# MBTI问题列表
questions = [
    {
        "id": 1,
        "text": "在社交场合中，你通常会：",
        "choices": [
            {"value": "E", "text": "和很多人交谈，感到能量充沛"},
            {"value": "I", "text": "倾向于和少数人深入交谈，或独处"}
        ]
    },
    {
        "id": 2,
        "text": "你更倾向于：",
        "choices": [
            {"value": "S", "text": "关注具体的事实和细节"},
            {"value": "N", "text": "关注概念和可能性"}
        ]
    },
    {
        "id": 3,
        "text": "做决定时，你通常：",
        "choices": [
            {"value": "T", "text": "依据逻辑和客观分析"},
            {"value": "F", "text": "考虑人的感受和价值观"}
        ]
    },
    {
        "id": 4,
        "text": "你更喜欢：",
        "choices": [
            {"value": "J", "text": "按计划行事，提前做决定"},
            {"value": "P", "text": "保持灵活，随机应变"}
        ]
    }
]

def calculate_mbti(answers):
    mbti = ""
    mbti += "E" if answers[0] == "E" else "I"
    mbti += "S" if answers[1] == "S" else "N"
    mbti += "T" if answers[2] == "T" else "F"
    mbti += "J" if answers[3] == "J" else "P"
    return mbti

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/result', methods=['POST'])
def result():
    answers = []
    for i in range(1, 5):
        answers.append(request.form.get(f'q{i}'))
    
    mbti_result = calculate_mbti(answers)
    return render_template('result.html', mbti=mbti_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)