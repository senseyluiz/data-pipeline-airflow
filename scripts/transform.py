import json
import pandas as pd

def transform_actions():
    with open('../database/actions.json', 'r') as infile:
        actions = json.load(infile)

    df = pd.DataFrame(actions)

    # Convertendo os tipos
    df['date'] = pd.to_datetime(df['date'])
    df['open'] = df['open'].astype(float)
    df['high'] = df['high'].astype(float)
    df['low'] = df['low'].astype(float)
    df['close'] = df['close'].astype(float)
    df['volume'] = df['volume'].astype(int)

    # Ordena por data mais recente
    df = df.sort_values(by=['date'], ascending=False)

    # Metrica de variação de preço
    df["price_change_percent"] = ((df["close"] - df["open"]) / df["open"]) * 100

    # Reset no índice
    df.reset_index(drop=True, inplace=True)

    return df

if __name__ == '__main__':
    df = transform_actions()
    df.to_csv('../database/actions.csv', index=False)

    print("\033[32mDados transformados com sucesso!\033[m")