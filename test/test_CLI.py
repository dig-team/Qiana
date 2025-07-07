import subprocess
import sys
import tempfile
import os
from pathlib import Path

def test_CLI_closure_only():
    """Test CLI with closure-only option using subprocess"""
    # Get the path to the CLI script
    cli_script = Path(__file__).parent.parent / "src" / "script" / "qianaCLI.py"
    
    # Sample TPTP input
    test_input = """
    fof(test1, axiom, p(a)).
    fof(test2, axiom, q(b)).
    """
    
    # Create temporary input file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.tptp', delete=False) as tmp_file:
        tmp_file.write(test_input)
        tmp_file_path = tmp_file.name
    
    try:
        # Run CLI with closure option
        result = subprocess.run([
            sys.executable, str(cli_script),
            '--closure',
            '--verbose',
            tmp_file_path
        ], capture_output=True, text=True, timeout=30)
        
        # Check that CLI executed successfully
        assert result.returncode == 0, f"CLI failed with stderr: {result.stderr}"
        assert len(result.stdout) > 0, "CLI produced no output"
        
    finally:
        # Clean up temp file
        os.unlink(tmp_file_path)

def test_CLI_stdin_input():
    """Test CLI reading from stdin"""
    cli_script = Path(__file__).parent.parent / "src" / "script" / "qianaCLI.py"
    
    test_input = """
    !believes(alice, p(c)).
    ![X] : p(X).
    """
    
    # Run CLI with stdin input
    result = subprocess.run([
        sys.executable, str(cli_script),
        '--closure',
        '--simplifiedInput',
        '--expandMacros'
    ], input=test_input, capture_output=True, text=True, timeout=30)
    
    assert result.returncode == 0, f"CLI failed with stderr: {result.stderr}"
    assert len(result.stdout) > 0, "CLI produced no output"

def test_CLI_output_file():
    """Test CLI writing to output file"""
    cli_script = Path(__file__).parent.parent / "src" / "script" / "qianaCLI.py"
    
    test_input = "fof(test, axiom, p(a))."
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.tptp', delete=False) as input_file:
        input_file.write(test_input)
        input_file_path = input_file.name
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.out', delete=False) as output_file:
        output_file_path = output_file.name
    
    try:
        # Run CLI with output file
        result = subprocess.run([
            sys.executable, str(cli_script),
            '--closure',
            '--outputFile', output_file_path,
            input_file_path
        ], capture_output=True, text=True, timeout=30)
        
        assert result.returncode == 0, f"CLI failed with stderr: {result.stderr}"
        
        # Check output file was created and has content
        assert os.path.exists(output_file_path), "Output file was not created"
        with open(output_file_path, 'r') as f:
            output_content = f.read()
        assert len(output_content) > 0, "Output file is empty"
        
    finally:
        # Clean up temp files
        os.unlink(input_file_path)
        if os.path.exists(output_file_path):
            os.unlink(output_file_path)

def test_CLI_help():
    """Test CLI help option"""
    cli_script = Path(__file__).parent.parent / "src" / "script" / "qianaCLI.py"
    
    result = subprocess.run([
        sys.executable, str(cli_script),
        '--help'
    ], capture_output=True, text=True, timeout=10)
    
    assert result.returncode == 0, f"CLI help failed with stderr: {result.stderr}"
    assert "Simple CLI to obtain the Qiana closure" in result.stdout, "Help text not found"

