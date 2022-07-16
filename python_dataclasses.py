from typing import Type
from dataclasses import dataclass
from pydantic import BaseModel
from pydantic.dataclasses import dataclass as pydantic_dataclass

from fastapi import FastAPI, Request


app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "API working!"}


"""
INDEPENDENT LIBRARY
- Contains nested native python dataclasses.
- Each dataclass performs internal computations.
"""


@dataclass
# @pydantic_dataclass
class Material:
    f: float
    sf: float = 1.5

    def __post_init__(self):
        self.fd = self.f / self.sf


@dataclass
# @pydantic_dataclass
class Square:
    w: float
    material: Material

    def __post_init__(self):
        self.area = self.w * self.w
        self.force_max = self.material.fd * self.area


@dataclass
# @pydantic_dataclass
class Triangle:
    w: float
    h: float
    material: Material

    def __post_init__(self):
        self.area = self.w * self.h * 0.5
        self.force_max = self.material.fd * self.area


"""
FASTAPI
- Attributes defined inside `__post_init__` don't exist.
- Can't perform computations depending on those attributes:
ERROR: AttributeError: 'dict' object has no attribute 'fd'
"""


@app.post("/square/")
async def root(square: Square):
    # square = Square(
    #     w=square.w,
    #     material=Material(
    #         f=square.material.f,
    #         # sf=square.material.sf,
    #     ),
    # )
    return {
        "msg": "square",
        "res": {
            "area": square.area,
            "force_max": square.force_max,
        },
    }


@app.post("/triangle/")
async def root(triangle: Triangle):
    return {
        "msg": "square",
        "res": {
            "area": triangle.area,
            "force_max": triangle.force_max,
        },
    }
