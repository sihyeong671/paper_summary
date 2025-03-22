from smolagents import CodeAgent,LiteLLMModel

model_id = "ollama_chat/gemma3:1b"

model = LiteLLMModel(
    model_id=model_id,
    api_base="http://localhost:11434",
    num_ctx=8192    
)
agent = CodeAgent(tools=[],
                  model=model,
                  add_base_tools=True)

agent.run(
    "Colu you give me the 118th number in the Fibonacci sequence?",
)