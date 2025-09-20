from pydantic import BaseModel

class DummyItem(BaseModel):
    name: str
    value: str
