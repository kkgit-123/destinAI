from app.utils.config_reader import ConfigReader
from langchain.chat_models import init_chat_model

# Initialize the ConfigReader
config = ConfigReader()

def get_config():
    """
    Returns the initialized ConfigReader instance.
    """
    return config

def initialize_llm():
    """Initializes the LLM model."""
    try:
        config = ConfigReader()
        
        model_name = config.get('LLM', 'MODEL_NAME')
        api_key = config.get('LLM', 'API_KEY')
        provider = config.get('LLM', 'PROVIDER')

        if not model_name or not api_key:
            raise ValueError("MODEL_NAME and/or API_KEY is missing in the LLM config section.")

        llm = init_chat_model(
            model_name,
            model_provider=provider,
            api_key=api_key,
            temperature=0
        )

        return llm
    except Exception as e:
        raise RuntimeError(f"Failed to initialize LLM model: {e}")