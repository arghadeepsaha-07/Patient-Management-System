from pydantic import BaseModel,Field,EmailStr,field_validator,ConfigDict

class Patient_Response(BaseModel):
    id : int
    name : str = Field(description="Please enter your name",examples={"Arghadeep Saha","Masha"})
    age : int = Field(description="Please enter your age",examples={12,67})
    gender : str = Field(description="Please enter your gender",examples={"Male","Female","Transgender"})
    height : int = Field(description="Please enter your height in cm",examples={178,167})
    weight : int = Field(description="Please enter your weight",examples={67,77})
    problem : str = Field(description="Please enter your problem/diseases",examples={"Skin disease","Lung Problem"})
    email : EmailStr | None = Field(default=None,description="Please enter your Email",examples={"abc@gmail.com"})
    phone_no : str = Field(description="Please enter your phone number",examples={"8876197789"})
    emergency_phone_no : str = Field(description="Please enter your emergency phone number",examples={"9791767999"})

    model_config  = ConfigDict(from_attributes=True)

class Patient_Create(BaseModel):
    name : str = Field(description="Please enter your name",examples={"Arghadeep Saha","Masha"})
    age : int = Field(description="Please enter your age",examples={12,67})
    gender : str = Field(description="Please enter your gender",examples={"Male","Female","Transgender"})
    height : int = Field(description="Please enter your height in cm",examples={178,167})
    weight : int = Field(description="Please enter your weight",examples={67,77})
    problem : str = Field(description="Please enter your problem/diseases",examples={"Skin disease","Lung Problem"})
    email : EmailStr | None = Field(default=None,description="Please enter your Email",examples={"abc@gmail.com"})
    phone_no : str = Field(description="Please enter your phone number",examples={"8876197789"})
    emergency_phone_no : str = Field(description="Please enter your emergency phone number",examples={"9791767999"})


    @field_validator("email")
    @classmethod
    def email_validator(cls,value):
        value_domain = ["gmail.com","yahoo.com"]


        if value is None:
                return value
        domain_name = value.split("@")[-1]

        if domain_name not in value_domain:
                raise ValueError("Email not valid !")

        return value


class Update_Response(BaseModel):
    name : str  = Field(description="Please enter your name",examples={"Arghadeep Saha","Masha"})
    age : int = Field(description="Please enter your age",examples={12,67})
    gender : str  = Field(description="Please enter your gender",examples={"Male","Female","Transgender"})
    height : int  = Field(description="Please enter your height in cm",examples={178,167})
    weight : int  = Field(description="Please enter your weight",examples={67,77})
    problem : str = Field(description="Please enter your problem/diseases",examples={"Skin disease","Lung Problem"})
    email : EmailStr | None = Field(default=None,description="Please enter your Email",examples={"abc@gmail.com"})
    phone_no : str  = Field(description="Please enter your phone number",examples={"8876197789"})
    emergency_phone_no : str | None = Field(default=None,description="Please enter your emergency phone number",examples={"9791767999"})

    model_config  = ConfigDict(from_attributes=True)

    @field_validator("email")
    @classmethod
    def email_validator(cls,value):
        value_domain = ["gmail.com","yahoo.com"]


        if value is None:
                return value
        domain_name = value.split("@")[-1]

        if domain_name not in value_domain:
                raise ValueError("Email not valid !")

        return value

    

class Update_Patient(BaseModel):
    name : str | None = Field(default=None,description="Please enter your name",examples={"Arghadeep Saha","Masha"})
    age : int | None = Field(default=None,description="Please enter your age",examples={12,67})
    gender : str |None = Field(default=None,description="Please enter your gender",examples={"Male","Female","Transgender"})
    height : int | None = Field(default=None,description="Please enter your height in cm",examples={178,167})
    weight : int | None = Field(default=None,description="Please enter your weight",examples={67,77})
    problem : str | None = Field(default=None,description="Please enter your problem/diseases",examples={"Skin disease","Lung Problem"})
    email : EmailStr | None = Field(default=None,description="Please enter your Email",examples={"abc@gmail.com"})
    phone_no : str | None = Field(default=None,description="Please enter your phone number",examples={"8876197789"})
    emergency_phone_no : str | None = Field(default=None,description="Please enter your emergency phone number",examples={"9791767999"})

    @field_validator("email")
    @classmethod
    def email_validator(cls,value):
        value_domain = ["gmail.com","yahoo.com"]


        if value is None:
                return value
        domain_name = value.split("@")[-1]

        if domain_name not in value_domain:
                raise ValueError("Email not valid !")

        return value
