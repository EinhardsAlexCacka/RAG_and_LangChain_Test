import os
from dotenv import load_dotenv
from importlib.metadata import version
load_dotenv()

core_version = version("langchain-core")
lg_version = version("langgraph")
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

print(f"langchain-core version: {core_version}")
print(f"langgraph version: {lg_version}")

def main():
    # Test OpenAI
    llm = ChatOpenAI(model_name="gpt-5.4-mini", temperature=0)
    response = llm.invoke("Say 'setup complete!' in one word")
    print(response)
    
    model_ollama = ChatOllama(
        model='gemma4:31b-cloud',
        base_url='https://ollama.com',
        client_kwargs={
            'headers': {
                'Authorization': f"Bearer {os.environ['OLLAMA_API_KEY']}"
            }
        }
    )
    
    # Test Ollama Cloud
    llm_ollama = model_ollama
    response_ollama = llm_ollama.invoke("Say 'setup complete!' in one word")
    print(f"Response from ChatOllama: {response_ollama}")

    print("Setup complete!")

if __name__ == "__main__":
    main()
