import pandas
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pandas.read_csv("plot_data.csv")
    print(df)

    # Plot a line graph
    df.plot(x='Day', y='Temperature', kind='line', marker='o', linestyle='-')

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.title('Line Graph from DataFrame')

    # Display the plot
    plt.show()

    # Create a bar plot
    df.plot(x='Day', y='Temperature', kind='bar', legend=False)
    plt.xlabel('Day')
    plt.ylabel('Temperature')
    plt.title('Bar Plot from DataFrame')
    plt.show()

