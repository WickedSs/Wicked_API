from typing import Optional, List
from pydantic import BaseModel


# Shared properties
class MaterialBase(BaseModel):
    materialName: str
    materialType: str
    materialPrice: float
    materialQte: int
    materialKey: str
    
# Properties to receive on Material creation
class MaterialCreate(MaterialBase):
    pass

# Properties to receive on Material update
class MaterialUpdate(MaterialBase):
    pass


# Properties shared by models stored in DB
class MaterialInDBBase(MaterialBase):
    id: int
    materialName: str
    materialType: str
    materialPrice: float
    materialQte: int
    materialKey: str

    class Config:
        orm_mode = True

# Properties to return to client        
class Material(MaterialInDBBase):
    pass

# Properties properties stored in DB
class MaterialInDB(MaterialInDBBase):
    pass
