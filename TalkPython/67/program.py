import pyperclip


def paste_from_clipboard() -> str:
    return pyperclip.paste()


def copy_to_clipboard(text: str) -> None:
    pyperclip.copy(text)


def main():
    print(paste_from_clipboard())

    text = input('Your text: ')
    copy_to_clipboard(text)

    print(paste_from_clipboard())


if __name__ == '__main__':
    main()
