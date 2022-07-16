# fastapi-playground
Small FastAPI apps to explore ideas.
- `python_dataclasses.py`: use python native nested dataclasses instead of pydantic. Multiple problems:
  - When a dataclass is used twice, the admin ui fails.
  - When a dataclass has attributes declared in a nested dataclass inside `__post_init__`, they're not available (does pydantic convert the dataclass and doesn't execute the initialization method?)
- `python_dataclasses.py`: use pydantic dataclasses.
  - Define pydantic dataclasses to store the initialization attributes of the needed python dataclasses.
  - Pass pydantic dataclasses as arguments in the requests.
  - Initialize the library dataclasses (python dataclasses) with the attributes from the pydantic dataclasses.
  - Use the original functionality of the library dataclasses.


## Start app
```
uvicorn python_dataclasses:app --reload
uvicorn pydantic_dataclasses:app --reload
```

## Testing
```
pytest test_python_dataclasses.py
pytest test_pydantic_dataclasses.py
```
