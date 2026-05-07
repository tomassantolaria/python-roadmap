from pathlib import Path
#import os

def clean_text(text):
    cleaned_words = []
    
    for word in text:
        word = word.strip(".,!?:;\"'()[]{}")
        
        if word and not word.isdecimal() :
            cleaned_words.append(word)
            
    return cleaned_words

def main():
    try:
        #print(os.getcwd())
        file_path = Path("automation/python-basics/sample_data/archivo.txt")
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        words = content.split()
        clean_text = clean_text(words)


        print(f"Cantidad de palabras limpias: {len(clean_text)}")

    except FileNotFoundError:
        print("Error: archivo no encontrado")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()