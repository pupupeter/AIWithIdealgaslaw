from smolagents import CodeAgent, LiteLLMModel

# Function to process the question and return results
def process_question(question):
    # Initialize the LiteLLMModel with the provided model ID and API key
    model_id = "gemini/gemini-2.0-flash"
    model = LiteLLMModel(model_id=model_id, GEMINI_API_KEY="AIzaSyBJj-7Am6kkBj-HGjex-d22j78HzNTRLK8")
    
    # Initialize the CodeAgent for both agents A and B
    agent_a = CodeAgent(tools=[], model=model, add_base_tools=True)
    agent_b = CodeAgent(tools=[], model=model, add_base_tools=True)

    # Run agent A (calculation agent) with the user question
    result_a = agent_a.run(
        f"你是化學或物理助教，擅長使用理想氣體方程式 PV=nRT 幫忙計算。請根據題目算出答案，並標註單位，回傳時請不要額外講解。問題：{question}"
    )
    
    # Run agent B (explaining agent) with the user question
    result_b = agent_b.run(
        f"你是熱心的物理老師，擅長解釋理想氣體方程式 PV=nRT 解題過程，並可解釋圖表或額外說明。問題：{question}"
    )
    
    # Ensure both results are returned as strings (in case there are unexpected results or objects)
    return str(result_a), str(result_b)

# Function to process plot based on question
