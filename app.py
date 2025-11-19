import argparse


def greet(name: str) -> None:
    """Print a friendly greeting for the provided name."""
    print(f"Hello, {name}! Welcome to your Python app.")


def main() -> None:
    """Parse CLI arguments and run the greeting."""
    parser = argparse.ArgumentParser(description="Basic greeting app")
    parser.add_argument(
        "--name",
        default="Developer",
        help="Name to greet",
    )
    args = parser.parse_args()
    greet(args.name)


if __name__ == "__main__":
    main()


