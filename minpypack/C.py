from pathlib import Path


def main():
    print("=====================================")
    print(f"__name__: {__name__}")
    print("Executing module C")
    print(f'module C path: {Path(__file__).parent.absolute()}')
    print(f'working directory absolute: {Path(__file__).absolute()}')
    print(f'working directory cwd: {Path.cwd()}')
    print("=====================================")


def BfromC():
    import minpypack.B.B_file as B
    B.main()


if __name__ == "__main__":
    main()
