from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    user_input = ""
    output_result = None

    if request.method == "POST":
        user_input = request.form.get("text_data", "")
        # Xử lý dữ liệu nhập: đảo ngược chuỗi, tính độ dài và số từ
        output_result = {
            "char_count": len(user_input),
            "word_count": len(user_input.split()),
            "reversed_text": user_input[::-1]
        }

    return render_template("index.html", user_input=user_input, result=output_result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
