def update_order():
    chai_type = "Elaichi"
    
    print(f" before kitchen update", chai_type)
    def kintchen():
        nonlocal chai_type
        chai_type = "kesar"
    kintchen()
    print(f" After kitchen update", chai_type)
    
update_order()