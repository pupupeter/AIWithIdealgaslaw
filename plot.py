import plotly.graph_objs as go

def plot_ideal_gas(P, V, n, T):
    R = 0.0821
    # 模擬 P-V 曲線（保持 T, n 不變）
    volumes = [v for v in range(1, 50)]
    pressures = [(n * R * T) / v for v in volumes]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=volumes, y=pressures, mode='lines', name='P-V 曲線'))
    fig.update_layout(
        title="理想氣體壓力-體積關係圖",
        xaxis_title="體積 (L)",
        yaxis_title="壓力 (atm)",
        template="plotly_dark"
    )
    return fig

