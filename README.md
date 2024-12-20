# Document Analysis Tool

This Python script processes a text document to generate a report on the frequency of characters and the number of words. It is designed to analyze the content of a text file and display insights about its composition.

---

## Features

- **Count Character Frequencies**: Counts how often each alphabetical character appears in the document (case insensitive).
- **Count Words**: Counts the total number of words in the document.
- **Readable Report**: Displays a summary of the analysis directly in the console.

---

## How It Works

1. **`countChars(words)`**:

   - Converts the input text to lowercase for case-insensitive analysis.
   - Iterates through each character in the input text.
   - Records the frequency of each alphabetical character using a dictionary.
   - Ignores non-alphabetical characters.
   - Outputs the frequency of each character.

2. **`countWords(words)`**:

   - Splits the input text into words.
   - Counts the total number of words in the text.
   - Outputs the total word count.

3. **`main()`**:
   - Reads the contents of a text file (`books/frankenstein.txt`).
   - Calls `countWords()` to count the words in the document.
   - Calls `countChars()` to count the frequency of each character.
   - Prints the analyzed text and the results.

---

## Requirements

- Python 3.x

---

## Usage

1. Place the text file you want to analyze in a `books` folder in the same directory as the script.
   - Example file: `books/frankenstein.txt`
2. Run the script:
   ```bash
   python script_name.py
   ```
