import pandas

if __name__ == '__main__':
    # pandas.set_option('display.max_rows', None)
    # pandas.set_option('display.max_columns', None)

    df = pandas.read_csv("test_data.csv")
    print(df)
    print("\nDescribe dataframe")
    print(df.describe())

    df["Total"] = df["Quantity"] * df["PurchasePrice"]
    print("\n Dataframe with extra column")
    print(df)

    df.drop('Total', axis=1, inplace=True)

    print("\n Convert column to list")
    column = df["LastName"]
    print("Values of column ",  column.tolist())

    print("\n Group by")
    # print(df.groupby('City').median(True))
    print(df[["FirstName", "City"]].groupby('FirstName').count())

    print("\n Sort and filter")
    print(df.sort_values(by='PurchasePrice', ascending=False), "\n")

    print(df[df['Quantity'] < 15])
