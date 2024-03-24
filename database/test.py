import os
from dotenv import load_dotenv

def main(): 
    load_dotenv()
    db = os.environ.get('myuser')
    print(db)

if __name__ == "__main__":
    main()