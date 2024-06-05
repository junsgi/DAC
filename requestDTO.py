from typing import Any
from pydantic import BaseModel 
class DACRequest(BaseModel):
    table1 : Any
    table2 : Any
    table3 : Any