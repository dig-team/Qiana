import argparse
import sys

from pipeline import Pipeline
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Example CLI for Qiana project.')

    parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity')

    # Main arguments
    parser.add_argument('-o', '--outputFile', type=str, help='Target output file. If not set, output goes to stdout', required=False)
    parser.add_argument('-t', '--timeout', type=int, help='Maximum time before timeout when calling solver.', required=False)
    parser.add_argument('-c', '--closure', action='store_true', help='Only compute the qiana closure of the input. If false, contradictions will be sought and a solver called.', required=False)
    parser.add_argument('-s', '--sat', action='store_true', help='Only return FOUND CONTRADICTION or FOUND NO CONTRADICTION, only used if the -c option is ommited.', required=False)
    parser.add_argument('-n', '--numberVars', type=int, help='Pick the number of quoted variables. Default value is 5.', required=False)

    
    # Positional arguments
    parser.add_argument('input_file', nargs='?', help='Input file to process. If not provided, reads from stdin.')

    # Parsing arguments
    args = parser.parse_args()

    # Read input from file or stdin
    if args.input_file:
        try:
            with open(args.input_file, 'r') as f:
                input_content = f.read()
        except IOError as e:
            print(f"Error reading file {args.input_file}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Check if there's input from stdin
        if not sys.stdin.isatty():
            input_content = sys.stdin.read()
        else:
            print("No input file provided and no data piped to stdin.", file=sys.stderr)
            print("Please either specify an input file or pipe data to stdin.", file=sys.stderr)
            sys.exit(1)
    
    
    # Process input content here...
    # For demonstration purposes, just print the first 100 characters
    if args.verbose:
        print("Input preview:", input_content[:100] + ("..." if len(input_content) > 100 else ""))
    
    varNum = args.numberVars if args.numberVars else 5
    timeout = args.timeout if args.timeout else 5

    pipeline = Pipeline()
    pipeline.computeQianaClosure(input_content, varNum)
    if args.closure:
        output = pipeline.getQianaClosure()
    else:
        pipeline.computeProofTree(timeout)
        output = pipeline.getHtmlTree()
        if args.sat: output = "FOUND CONTRADICTION" if pipeline.foundContradiction else "FOUND NO CONTRADICTION"
    if args.outputFile:
        try:
            with open(args.outputFile, 'w') as f:
                f.write(output)
        except IOError as e:
            print(f"Error writing to file {args.outputFile}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(output)