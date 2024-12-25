from dataclasses import dataclass,field
from typing import Any


#
# @dataclass
# class PersonData:
#     name:str
#     lastname:str
#     age:int = field(default=18,compare=False)
#     interests:list=field(default_factory=list)
#     info : str = field(init=False,compare=False)
#
#     def __post_init__(self):
#         self.info:str = f"Person: {self.name} {self.lastname} {self.age}"
#
# pd1 = PersonData("Toxir",'Sobir',12)
# pd2 = PersonData("Toxir",'Sobir',12)
# print(pd1 == pd2)


class Days:
    @staticmethod
    def may_days():
        return ['Du','Se','Chor','Pay','Ju']

@dataclass
class PersonData:
    current_id = 0
    id:int = field(init=False)
    name:str
    lastname:str
    age:Any

@dataclass
class Employee(PersonData):
    age:int
    salary:int
    passport:str
    Work_days:list = field(default_factory=Days.may_days)

    def __post_init__(self):
        super().__post__init()
        print("employee ichida")


em = Employee('Jalil','Jalilov',13,1111,'aa123')

