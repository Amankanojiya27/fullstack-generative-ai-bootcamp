def brew_chai(flavor):
    if flavor not in ["ginger", "lemon", "elaichi"]:
        raise ValueError("Unsupported chai flavor")
    print(f"Brewing {flavor} chai")


brew_chai("lemon")
print()
brew_chai("mint")
