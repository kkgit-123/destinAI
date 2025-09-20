from pydantic import BaseModel

class DummyItem(BaseModel):
    name: str
    value: str

class PromptRequest(BaseModel):
    prompt: str
