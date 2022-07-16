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
class Material:
    f: float
    sf: float = 1.5

    def __post_init__(self):
        self.fd = self.f / self.sf


@dataclass
class Square:
    w: float
    material: Material

    def __post_init__(self):
        self.area = self.w * self.w
        self.force_max = self.material.fd * self.area


@dataclass
class Triangle:
    w: float
    h: float
    material: Material

    def __post_init__(self):
        self.area = self.w * self.h * 0.5
        self.force_max = self.material.fd * self.area


"""
FASTAPI
- Declare again the dataclasses as `pydantic.dataclass`
to store only the initialization attributes.
- Initialize the `library` dataclasses using the 
pydantic.dataclasses inside the functions.
--> PROBLEMS in `python_dataclasses.py` SOLVED!
--> Code more redundant.
"""


@pydantic_dataclass
class MaterialBM:
    f: float
    sf: float = 1.5


@pydantic_dataclass
class SquareBM:
    w: float
    material: MaterialBM


@pydantic_dataclass
class TriangleBM:
    w: float
    h: float
    material: MaterialBM


@app.post("/square/")
async def root(square: SquareBM):
    square = Square(
        w=square.w,
        material=Material(
            f=square.material.f,
            sf=square.material.sf,
        ),
    )
    return {
        "msg": "square",
        "res": {
            "area": square.area,
            "force_max": square.force_max,
        },
    }


@app.post("/triangle/")
async def root(triangle: TriangleBM):
    triangle = Triangle(
        w=triangle.w,
        h=triangle.h,
        material=Material(
            f=triangle.material.f,
            sf=triangle.material.sf,
        ),
    )
    return {
        "msg": "square",
        "res": {
            "area": triangle.area,
            "force_max": triangle.force_max,
        },
    }
