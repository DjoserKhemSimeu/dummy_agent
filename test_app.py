#!/usr/bin/env python3
import subprocess

# Run the app.py script and capture the output
result = subprocess.run(['python', 'app.py'], capture_output=True, text=True)

# Print the output
print("Output of app.py:")
print(result.stdout)

# Check if the output is as expected (should print 'Résultat : 5')
if "Résultat : 5" in result.stdout:
    print("\nTest passed! The fix works correctly.")
else:
    print("\nTest failed! The output is not as expected.")