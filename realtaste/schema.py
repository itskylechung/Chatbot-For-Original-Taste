from typing import List, Optional

from pydantic import BaseModel, Field


class ChooseBento(BaseModel):
    """Entity of that bento"""

    # 1. Each field is an `optional` -- this allows the model to decline to extract it!
    # 2. Each field has a `description` -- this description is used by the LLM.
    bento_name: Optional[str] = Field(
        description="The name of the bento being ordered."
    )
    modify: Optional[str] = Field(
        description="Custom modifications requested by the customer, such as less rice or more vegetables."
    )


class Data(BaseModel):
    """Extracted data about bentos."""

    # Creates a model so that we can extract multiple entities.
    bentos: List[ChooseBento]
