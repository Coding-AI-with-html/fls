from pydantic import BaseModel, Field, field_validator

class Checker(BaseModel):
    stringer: str
    integer: int

    @field_validator('integer')
    @classmethod
    def validate_integer(cls, value):
        if value <= 0:
            raise ValueError(f"Integer is not valid: {value}")
        return value

userChecker = Checker(stringer="jackDaniels", integer=2)

def main():
    try:
        user = Checker(stringer="jack", integer=1)
        print(user)
    except ValueError as e:
        print(f"Error: {e}")



