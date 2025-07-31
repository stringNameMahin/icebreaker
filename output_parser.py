from typing import List, Dict, Any
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class Summary(BaseModel):
    Summary: str = Field(description="summary")
    facts: List[str] = Field(description="Interesting facts about them")

    def to_dict(self) -> Dict[str, Any]:
        return {"summary": self.Summary, "facts": self.facts}
    

Summary_parser = PydanticOutputParser(pydantic_object=Summary)