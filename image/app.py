import argparse
import pandas as pd

def generate_dummy_csv(output_file):
    dummy_df = pd.DataFrame(
		{
			'sample': [1, 2, 3, 4, 5],
			'feature1': [0.1, 0.2, 0.3, 0.4, 0.5],
			'feature2': [0.5, 0.4, 0.3, 0.2, 0.1],
        }
    )
    dummy_df.to_csv(output_file, index=False)

def main():
	parser = argparse.ArgumentParser(description="Process a video file and generate a dummy CSV output.")
	parser.add_argument('--input', type=str, help="Path to the input video file")
	parser.add_argument('--output', type=str, help="Path to the output CSV file")
	
	args = parser.parse_args()
	generate_dummy_csv(args.output)

if __name__ == "__main__":
	main()
