import argparse
import os

import pandas as pd

os.makedirs("submissions1", exist_ok=True)

def generate_dummy_csv(output_file):
    transposed_data = [
        {"Turning Patterns": "Car", "BC": 1, "BE": 1, "DE": 1, "DA": 1, "FA": 9, "FC": 1},
        {"Turning Patterns": "Bus", "BC": 2, "BE": 2, "DE": 2, "DA": 2, "FA": 10, "FC": 2},
        {"Turning Patterns": "Truck", "BC": 3, "BE": 3, "DE": 3, "DA": 3, "FA": 10, "FC": 3},
        {"Turning Patterns": "Three-Wheeler", "BC": 4, "BE": 4, "DE": 4, "DA": 4, "FA": 0, "FC": 4},
        {"Turning Patterns": "Two-Wheeler", "BC": 5, "BE": 5, "DE": 5, "DA": 5, "FA": 0, "FC": 5},
        {"Turning Patterns": "LCV", "BC": 6, "BE": 6, "DE": 6, "DA": 6, "FA": 0, "FC": 6},
        {"Turning Patterns": "Bicycle", "BC": 7, "BE": 7, "DE": 7, "DA": 7, "FA": 0, "FC": 7},
    ]
    dummy_df = pd.DataFrame(transposed_data)
    dummy_df.to_csv(f"submissions1/{output_file}", index=False)


def main():
	parser = argparse.ArgumentParser(description="Process a video file and generate a dummy CSV output.")
	parser.add_argument('--input', type=str, help="Path to the input video file")
	parser.add_argument('--output', type=str, help="Path to the output CSV file")
	
	args = parser.parse_args()
	generate_dummy_csv(args.output)

if __name__ == "__main__":
	main()
