from app.config import initialize_llm
from langchain_core.prompts import ChatPromptTemplate
from prompt import PLANNER_SYSTEM_PROMPT, PLANNER_USER_PROMPT, plan_data
from typing import Dict

def create_prompt_template(system_prompt: str, user_prompt: str, user_message: str) -> ChatPromptTemplate:
    """Creates a ChatPromptTemplate from the given system and user prompts."""
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", user_prompt)
    ])
    return prompt.invoke({"user_message": user_message})

def generate_travel_plan(user_message: str) -> Dict:
    """Generates a travel plan using the LLM model."""

    llm = initialize_llm()
    prompt = create_prompt_template(PLANNER_SYSTEM_PROMPT, PLANNER_USER_PROMPT, user_message)
    try:
        llm_response = llm.invoke(prompt).content
        llm_response = plan_data
        return llm_response
    except Exception as e:
        raise ValueError(f"Error generating travel plan: {e}")