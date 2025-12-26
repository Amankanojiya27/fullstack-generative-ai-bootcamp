# Function to serve chai based on flavor
def serve_chai(flavor):
    try:
        # Try block: code that might cause an error
        print(f"Preparing {flavor} chai...")
        
        # Raise an error if the flavor is unknown
        if flavor == "unknown":
            raise ValueError("We do not know this flavor")
            
    except ValueError as e:
        # Except block: runs if an error occurs in try
        print("Error:", e)
        
    else:
        # Else block: runs only if no error occurred
        print(f"{flavor} chai is served")
        
    finally:
        # Finally block: always runs, no matter what
        print("Next Customer Please")

# Test with a known flavor
serve_chai("masala")

print("\n")  # Just to separate outputs

# Test with an unknown flavor
serve_chai("unknown")
