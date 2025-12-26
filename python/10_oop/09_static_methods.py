class Utils:
    
    # def chat_cleaner(text):        # Error: missing 'self'
    # def chat_cleaner(self, text):  # Works even without @staticmethod, but requires an instance(self)
    
    @staticmethod  # Decorator
    def chat_cleaner(text):  # With @staticmethod, 'self' is not needed
        return [item.strip() for item in text.split(",")]


raw = "apple,   orange,   banana"

# Method 1 (using an instance)
# obj = Utils()
# print(obj.chat_cleaner(raw))

# Method 2 (calling directly from the class)
obj2 = Utils.chat_cleaner(raw)
print(obj2)
