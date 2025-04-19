from flask import Flask, render_template, request
from agentsb import process_question
from utils import record_conversation
from plot import plot_ideal_gas

import plotly.io as pio

# 建立 Flask 應用程式
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    plot_html = None

    if request.method == "POST":
        question = request.form["question"]
        plot_checkbox = "plot_checkbox" in request.form

        if not question.strip():
            response = "請輸入一個問題。"
        else:
            result_a, result_b = process_question(question)

            response_a = result_a if isinstance(result_a, str) else result_a.get("messages", [{}])[0].get("content", "來自 agent A 的回應無效。")
            response_b = result_b if isinstance(result_b, str) else result_b.get("messages", [{}])[0].get("content", "來自 agent B 的回應無效。")

            V, n, T = 22.4, 1, 272.84
            P = (n * 0.0821 * T) / V

            if plot_checkbox:
                fig = plot_ideal_gas(P, V, n, T)
                plot_html = pio.to_html(fig, full_html=False)

            response = f"<strong>🧑‍🏫 助教回答</strong>：<br>{response_a}<br><br><strong>👩‍🏫 物理老師解釋</strong>：<br>{response_b}"

    return render_template("index.html", response=response, plot_html=plot_html)

# 執行 Flask 應用
if __name__ == "__main__":
    app.run(debug=True)
