from pydantic import BaseModel, Field, EmailStr


class UserPasswordSchema(BaseModel):
    password: str = Field(examples=['lkjhg+hgf5h'], min_length=8)


class UserBaseSchema(BaseModel):
    email: EmailStr = Field(description="email to login", examples=['user@gmail.com'])
    name: str = Field(min_length=1, max_length=50, examples=['casper'])


class IdSchema(BaseModel):
    id: int = Field(gt=0, examples=[123, 5, 9])


class CreateUserSchema(UserPasswordSchema, UserBaseSchema):
    pass
