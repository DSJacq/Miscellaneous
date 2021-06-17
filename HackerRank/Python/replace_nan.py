    fill = {**dict.fromkeys(df.select_dtypes(np.number).columns, 0), 
            **dict.fromkeys(df.select_dtypes(exclude=np.number).columns, '')}
    df = df.fillna(fill)
