# Pylance
# https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance

import pathlib

# importの自動修正
# Path


def func(i: int, s: str) -> str:
    return s * i


# 型ヒントの表示とチェック
func("1", "a")