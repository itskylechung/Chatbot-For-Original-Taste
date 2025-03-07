from typing import List, Optional

from pydantic import BaseModel, Field


class BentoConfig(BaseModel):
    """Entity of each bento (Meal box)"""

    # 1. Each field is an `optional` -- this allows the model to decline to extract it!
    # 2. Each field has a `description` -- this description is used by the LLM.

    bento_name: str | None = Field(
        default=None, description="The name of the bento being ordered."
    )
    modify: str | None = Field(
        default=None,
        description="Custom modifications requested by the customer, such as less rice or more vegetables.",
    )
    # For best performance, document the schema well and make sure the model isn't force to return results if there's no information to be extracted in the text.


class Data(BaseModel):
    """Extracted all data from each bento (Meal box)."""

    # Creates a model so that we can extract multiple entities.
    bentos: List[BentoConfig]
