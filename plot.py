df = pd.read_csv("trans.csv")

columns = list(df.columns)

for i in range(1,len(columns)):
    plt.figure()
    plt.bar(df['dist'], df[columns[i]],width = 0.4,color="Orange")
    plt.title(columns[i]+" GDP contribution")
    plt.ylabel("GDP in crores")
    plt.xlabel("Sector of economy")
    for x,y in zip(df['dist'],df[columns[i]]):
        label = "{:.0f}".format(y)
        plt.annotate(label,(x,y),textcoords="offset points", xytext=(0,10),  ha='center')
    plt.savefig(columns[i])
