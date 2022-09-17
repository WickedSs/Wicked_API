from Routes.Config import get_password_hash, verify_password
from Database.Crud.base_crud import CRUDBase
from Models.Base_Models import User
from Schema.User_Schema import UserCreate, UserUpdate
from typing import Type

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def __init__(self, model: Type[User]):    
        super().__init__(model)
        
        
user = CRUDUser(User)