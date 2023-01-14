from typing import Any, Dict, Optional, Union, List
from Routes.Security import get_password_hash, verify_password
from Database.Crud.base_crud import CRUDBase
from Models.Base_Models import Persistant
from Schema.Persistant_Schema import PersistantCreate, PersistantUpdate
from typing import Type
from sqlalchemy.orm import Session

class CRUDPersistant(CRUDBase[Persistant, PersistantCreate, PersistantUpdate]):
    def __init__(self, model: Type[Persistant]):    
        super().__init__(model)
        

persistant = CRUDPersistant(Persistant)