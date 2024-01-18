class L:
    def __init__(self, line: int, column: int):
        self.line = line
        self.column = column

    def __str__(self) -> str:
        return f"L(line={self.line}, column={self.column})"

    def __eq__(self, object: object) -> bool:
        if (type(object).__name__ == "L" and hasattr(object, "line") and hasattr(object, "column")):
            return self.line == object.line and self.column == object.column
        return False

class Token:
    def __init__(self, loc: L, type: str | None, value: str):
        self.loc = loc
        self.type = type
        self.text = value

    def __str__(self) -> str:
        return f'Token(loc={self.loc}, type="{self.type}", text="{self.text}")'
