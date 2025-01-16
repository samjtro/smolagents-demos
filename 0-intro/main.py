import os
from dotenv import load_dotenv
from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool, ManagedAgent


def main():
    model_id = "meta-llama/Llama-3.3-70B-Instruct"
    model = HfApiModel(model_id=model_id, token=os.environ["HUGGINGFACE_API_KEY"])
    web_agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

    managed_web_agent = ManagedAgent(
        agent=web_agent,
        name="web_search",
        description="Runs web searches for you. Give it your query as an argument.",
    )

    manager_agent = CodeAgent(tools=[], model=model, managed_agents=[managed_web_agent])

    manager_agent.run("Who is the CEO of Hugging Face?")


if __name__ == "__main__":
    load_dotenv()
    main()
