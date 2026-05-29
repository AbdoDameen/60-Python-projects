from textblob import TextBlob


def main():
    """Correct a list of misspelled words and show before/after mapping."""
    words = ["Data Scence", "Machine Learnin"]
    corrected_words = []

    for word in words:
        corrected_words.append(TextBlob(word))

    print("Spelling corrections:")
    print("-" * 40)

    # Show the wrong -> correct mapping
    for original, corrected in zip(words, corrected_words):
        print(f"  {original:20} -> {corrected.correct()}")

    print("-" * 40)
    print("Wrong words: ", words)
    print("Correct words:", [str(w.correct()) for w in corrected_words])


if __name__ == '__main__':
    main()
