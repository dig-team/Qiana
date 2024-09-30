import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Example CLI for Qiana project.')

    # Adding arguments
    parser.add_argument('-n', '--name', type=str, help='Name of the user', required=True)
    parser.add_argument('-a', '--age', type=int, help='Age of the user', required=True)
    parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity')

    # Parsing arguments
    args = parser.parse_args()

    # Using the arguments
    if args.verbose:
        print(f"Verbose mode is on.")
    print(f"Hello, {args.name}! You are {args.age} years old.")
