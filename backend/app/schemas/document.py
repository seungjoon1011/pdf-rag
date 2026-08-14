from pydantic import BaseModel, ConfigDict

class DocumentCreate(BaseModel):
    title: str
    filename: str

class DocumentResponse(BaseModel):
    id: int
    title: str
    filename: str

    model_config = ConfigDict(from_attribute=True)