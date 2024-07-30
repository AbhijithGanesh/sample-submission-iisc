import argparse
import os

import pandas as pd

os.makedirs("submissions", exist_ok=True)

def generate_dummy_csv(output_file):
    dummy_df = pd.DataFrame(
		{
			"Turning Patterns": [
				"Car", "Bus", "Truck", "Three-Wheeler", "Two-Wheeler", "LCV", "Bicycle",
			],
			"BC": [1, 2, 3, 4, 5, 6, 7],
			"BE": [1, 2, 3, 4, 5, 6, 7],
			"DE": [1, 2, 3, 4, 5, 6, 7],
			"DA":[1, 2, 3, 4, 5, 6, 7],
			"FA":[9, 10, 10, 0, 0, 0, 0],
			"FC":[1, 2, 3, 4, 5, 6, 7],
		}
    )
    dummy_df.to_csv(f"/app/submissions/{output_file}", index=False)

def main():
	parser = argparse.ArgumentParser(description="Process a video file and generate a dummy CSV output.")
	parser.add_argument('--input', type=str, help="Path to the input video file")
	parser.add_argument('--output', type=str, help="Path to the output CSV file")
	
	args = parser.parse_args()
	generate_dummy_csv(args.output)

if __name__ == "__main__":
	main()
