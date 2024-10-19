import matplotlib.pyplot as plt

def visualize_data(df):
    """
    Visualize CRM data.

    Parameters:
    df (DataFrame): DataFrame containing the CRM data.
    """
    df['Sales'].plot(kind='bar')
    plt.title('Sales Data')
    plt.xlabel('Customers')
    plt.ylabel('Sales Amount')
    plt.savefig('image/example_visualization.png')
    plt.show()
