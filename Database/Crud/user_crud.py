from typing import Any, Dict, Optional, Union
from Routes.Security import get_password_hash, verify_password
from Database.Crud.base_crud import CRUDBase
from Models.Base_Models import User
from Schema.User_Schema import UserCreate, UserUpdate
from typing import Type
from sqlalchemy.orm import Session

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def __init__(self, model: Type[User]):    
        super().__init__(model)
        
        
    def authenticate(self, db: Session, *, username: str, password: str) -> Optional[User]:
        user_found = self.read_by_username(db, username=username)
        # print("New Password:", get_password_hash(password))
        if not user_found:
            return None
        if not verify_password(password, user_found.password_sha512):
            return None
        return user_found

    # def is_active(self, user_found: User) -> bool:
    #     return user_found.is_active

    def is_superuser(self, user_found: User) -> bool:
        return user_found.userRole == "Admin"
    
    def get_username(self, user_found: User) -> bool:
        return user.username;
        
        
user = CRUDUser(User)