def manipulate_data(df):
    """
    Manipulate the CRM data for analysis.

    Parameters:
    df (DataFrame): Input DataFrame.

    Returns:
    DataFrame: A manipulated DataFrame.
    """
    # Example manipulation: removing duplicates
    df = df.drop_duplicates()
    return df
