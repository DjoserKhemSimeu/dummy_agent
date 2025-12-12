import subprocess

# Run the test script
result = subprocess.run(['python', 'test_addition.py'], capture_output=True, text=True)

print("Test Output:")
print(result.stdout)
if result.stderr:
    print("Test Errors:")
    print(result.stderr)