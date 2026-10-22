from flask import Flask, render_template, request

app = Flask(__name__)

styles = ["Минимализм", "Скандинавский", "Лофт"]
rooms = [("Гостиная", 25, 2), ("Спальня", 16, 1), ("Кухня", 12, 1)]

total_area = sum(r[1] for r in rooms)
average_area = round(total_area / len(rooms), 1)

rating = 5
if rating >= 5:
    rating_text = "Отлично"
elif rating >= 3:
    rating_text = "Хорошо"
else:
    rating_text = "Нужно улучшить"

for style in styles:
    if style == "Лофт":
        continue
    if style == "Скандинавский":
        break

i = 0
while i < 3:
    i += 1

@app.route("/")
def index():
    return render_template("index.html", styles=styles, rooms=rooms,
                           total_area=total_area,
                           average_area=average_area,
                           rating_text=rating_text)

@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    area = None
    message = ""

    if request.method == "POST":
        try:
            a = float(request.form["length"])
            b = float(request.form["width"])
            if a > 0 and b > 0:
                area = round(a * b, 2)
            else:
                message = "Введите числа больше нуля"
        except ValueError:
            message = "Введите правильные числа"

    return render_template("calculator.html", area=area, message=message)

if __name__ == "__main__":
    app.run(debug=True)