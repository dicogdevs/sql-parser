

import pandas as pd

def create_excel_output(data, output_file):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)