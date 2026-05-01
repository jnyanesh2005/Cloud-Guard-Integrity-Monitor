from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserConfirm(BaseModel):
    email: str
    code: str

class FileMetadata(BaseModel):
    file_id: str
    filename: str
    hash_sha256: str
    timestamp: str
    user_id: str
    s3_key: str

class IntegrityCheckResponse(BaseModel):
    filename: str
    stored_hash: str
    calculated_hash: str
    is_valid: bool
    message: str
    algorithm: str = "BLAKE3"
