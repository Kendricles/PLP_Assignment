def process_file(input_path="input.txt", output_path="output.txt"):
    """Read text from input_path, convert to uppercase, count words, and write to output_path."""
    try:
        with open(input_path, "r") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Input file '{input_path}' not found.")
        return

    num_words = len(text.split())
    uppercase = text.upper()

    with open(output_path, "w") as output_file:
        output_file.write(uppercase)
        output_file.write(f" text is {text}\n\nNumber of words: {num_words}\n")

    print(f"Successfully created '{output_path}' with {num_words} words and content as\n {text}")


process_file()