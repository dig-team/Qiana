import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Example CLI for Qiana project.')

    # Adding arguments
    parser.add_argument('-n', '--name', type=str, help='Name of the user', required=True)
    parser.add_argument('-a', '--age', type=int, help='Age of the user', required=True)
    parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity')

    # Main arguments
    parser.add_argument('-o', '--outputFile', type=str, help='Target output file. If this is not set, result will be output to the standard output', required=False)
    parser.add_argument('-t', '--timeout', type=int, help='Maximum time before timeout when calling solver.', required=False)
    parser.add_argument('-c', '--closure', action='store_true', help='Only compute the qiana closure of the input. If this is false then contradictions will be sought. ', required=False)


    
    # Positional arguments
    parser.add_argument('input_file', nargs='?', help='Input file to process')

    # Parsing arguments
    args = parser.parse_args()

    # Using the arguments
    if args.verbose:
        print(f"Verbose mode is on.")
    print(f"Hello, {args.name}! You are {args.age} years old.")
    
    # Check if output file is set
    if args.outputFile:
        print(f"Output will be written to {args.outputFile}")
    else:
        print("No output file specified, results displayed on console only.")
        
    # Check if input file is provided
    if args.input_file:
        print(f"Processing input file: {args.input_file}")
    else:
        print("No input file specified.")
