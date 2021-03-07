# Python Docstring Generator
# https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring


def func(i: int, s: str) -> str:
    # Generate Docstring (Ctrl+Shift+2) でDocstringが自動生成される
    return s * i


func(3, "a")