def save_data(data, file_name='output.csv'):
    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False)
    print(f"Data saved to {file_name}")
    
    
    def process_data(data):
    df = pd.DataFrame(data)
    # Remove duplicates
    df = df.drop_duplicates()
    # Additional cleaning steps can be added here
    return df