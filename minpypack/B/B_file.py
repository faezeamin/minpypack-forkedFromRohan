from pathlib import Path


def main():
    print("=====================================")
    print(f"__name__: {__name__}")
    print("Executing B_file")
    print(f'B_file path: {Path(__file__).parent.absolute()}')
    print(f'working directory absolute: {Path(__file__).absolute()}')
    print(f'working directory cwd: {Path.cwd()}')
    print("=====================================")


if __name__ == "__main__":
    main()
