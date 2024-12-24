import pandas as pd
parquet_file = "C:/Users/jamal/Desktop/page_26.parquet"
df = pd.read_parquet(parquet_file, engine='auto')  # Use 'pyarrow'
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
if 'raw_text' in df.columns:
    print(df['raw_text'].iloc[0])  # Display the raw text from the first row
else:
    print("\nThe 'raw_text' column is not found in the Parquet file.")
