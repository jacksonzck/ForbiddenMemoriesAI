import json
import pandas as pd

# THE CARDS SAY MOOPS!
moops: pd.DataFrame = None

with open("Cards.json") as f:
    moops = pd.DataFrame.from_dict(json.load(f))
    moops.convert_dtypes()
    moops.set_index('Id', inplace=True)
    #print(moops.dtypes)

def cardNameToId(name: str) -> int:
    pass

def idToCardName(id: int) -> str:
    return "" + moops[moops.index == id].Name

def main():
    print(idToCardName(1))
    pass

if __name__ == "__main__":
    main()