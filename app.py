import gradio as gr
from agentsb import process_question  # 假設這是用來處理問題的代理程式
from utils import record_conversation  # 假設用來記錄會話的工具函數
from plot import plot_ideal_gas  # 假設這是用來繪製 P-V 曲線的函數

# 問題處理函數
def run_simulation(question, plot_checkbox):
    if not question.strip():  # 確保問題不為空
        return "請輸入一個問題。", None

    # 進行計算，這裡使用 process_question 函數進行問題處理
    result_a, result_b = process_question(question)

    # 檢查 result_a 和 result_b 是否為字符串或字典
    if isinstance(result_a, str):
        response_a = result_a  # 如果是字符串，直接使用
    else:
        response_a = result_a['messages'][0]['content'] if isinstance(result_a, dict) and 'messages' in result_a else "來自 agent A 的回應無效。"

    if isinstance(result_b, str):
        response_b = result_b  # 如果是字符串，直接使用
    else:
        response_b = result_b['messages'][0]['content'] if isinstance(result_b, dict) and 'messages' in result_b else "來自 agent B 的回應無效。"

    # 提取 V、n 和 T （假設回應中包含這些信息）
    V = 22.4  # 假設體積為 22.4 L
    n = 1  # 假設摩爾數為 1 mol
    T = 272.84  # 假設溫度為 272.84 K

    # 計算壓力 P
    P = (n * 0.0821 * T) / V  # 假設 R=0.0821 atm·L/(mol·K)

    # 處理繪圖
    plot = None
    if plot_checkbox:
        plot = plot_ideal_gas(P, V, n, T)  # 現在傳遞正確的所有參數

    # 構建最終回應
    response = f"**🧑‍🏫 助教回答**：\n\n{response_a}\n\n**👩‍🏫 物理老師解釋**：\n\n{response_b}"

    return response, plot

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 🧪 理想氣體方程式 AI 模擬器")
    gr.Markdown("輸入與 PV=nRT 有關的問題，AI 將幫你計算並可視化 P-V 曲線。")

    # 用戶輸入問題
    question = gr.Textbox(label="請輸入問題（例如：P=1 atm, V=22.4 L, n=1 mol，請問 T？）", lines=3)
    
    # 繪製對應圖表的勾選框
    plot_checkbox = gr.Checkbox(label="繪製對應的 P-V 曲線", value=True)

    # 按鈕觸發模擬
    submit_btn = gr.Button("開始模擬")

    # 顯示計算結果和圖表
    output_text = gr.Markdown()
    output_plot = gr.Plot()

    # 當按鈕被按下時，觸發模擬邏輯
    submit_btn.click(run_simulation, inputs=[question, plot_checkbox], outputs=[output_text, output_plot])

# 啟動 Gradio 介面
demo.launch()


