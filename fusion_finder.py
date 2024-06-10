import json
import pandas as pd
from typing import List

# THE CARDS SAY MOOPS!
moops: pd.DataFrame = None

with open("Cards.json") as f:
    moops = pd.DataFrame.from_dict(json.load(f))
    moops.convert_dtypes()
    moops["card_id"] = moops.Id
    moops.set_index('Id', inplace=True)
    #print(moops.head())
    #print(moops.dtypes)Series

# One deep fusion search for the cards we have.
def possible_fusions(card_ids: List[int]):
    cards = moops[moops.index.isin(card_ids)].sort_index()
    fusion_results = []
    fusion_results.extend([(card_id, 0, card_id) for card_id in card_ids])
    for fusion_list in cards.Fusions:
        for fusion in fusion_list:
            if fusion["_card2"] in cards.index:
                fusion_results.append((fusion["_card1"], fusion["_card2"], fusion["_result"]))
    return fusion_results

def best_attack(card_ids: List[int]):
    cards = moops[moops.index.isin(card_ids)].sort_index()
    return cards[cards.Attack == cards.Attack.max()].index[0]

def find_best_attack_fusion(card_ids):
    fusions = possible_fusions(card_ids)
    best_id = best_attack([result for _, _, result in fusions])
    for fusion in fusions:
        if fusion[2] == best_id:
            return fusion

def card_id_to_name(card_id):
    return moops[moops.index == card_id].iloc[0].Name

def card_name_to_id(card_name):
    matching_cards = moops[moops.Name == card_name]
    if len(matching_cards) == 0:
        return False
    return moops[moops.Name == card_name].iloc[0].card_id

def main():
    #print(best_attack(possible_fusions(pd.Series([2, 8], name="Id"))))
    print(f"What cards do you have in hand, Yugi? I'm your grandpoppy!")
    card_ids = []
    entry = input()
    while entry != "":
        card = card_name_to_id(entry)
        if card is False: 
            print(f"I couldn't recognize that card, yugi!")
        else: 
            print(f"Ah, the {entry}, card id {card}. What a classic!")
            card_ids.append(card)
        entry = input()
    card1, card2, card3 = find_best_attack_fusion(card_ids)
    print(f"Fuse {card_id_to_name(card1)} and {card_id_to_name(card2)}, Yugi!")
    print(f"It will get you {card_id_to_name(card3)}!!")
    pass

if __name__ == "__main__":
    main()