from pydantic import BaseModel


# Shared properties
class BankBase(BaseModel):
    bank_name: str
    bank_holder_name: str
    bank_amount: float
    bank_bank_number: str
    bank_card_number: str
    bank_card_expiration: str
    bank_card_type: str
    bank_key: str
    
# Properties to receive on Bank creation
class BankCreate(BankBase):
    pass

# Properties to receive on Bank update
class BankUpdate(BankBase):
    pass


# Properties shared by models stored in DB
class BankInDBBase(BankBase):
    id: int
    bank_name: str
    bank_holder_name: str
    bank_amount: float
    bank_bank_number: str
    bank_card_number: str
    bank_card_expiration: str
    bank_card_type: str
    bank_key: str

    class Config:
        orm_mode = True

# Properties to return to client        
class Bank(BankInDBBase):
    pass

# Properties properties stored in DB
class BankInDB(BankInDBBase):
    pass
