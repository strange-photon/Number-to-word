# Number-to-Word Converter

The **Number-to-Word Converter** is a Python program that allows you to convert numerical values into their word representations. It supports numbers up to 16 digits in length, providing a versatile solution for transforming numeric data into human-readable formats.

## Features

- Accurate and reliable conversion of numbers to their word equivalents.
- Handles zeros, odd and even-length numbers, and crore unit for numbers exceeding 9 digits.
- Easy integration into projects for improved readability and interpretability of numeric data.

## Usage

To use the program, simply call the `NumToWord` function, passing the desired number as an argument. The function will return the word representation of the number. For example, running `NumToWord(9000)` will output "nine thousand."

## How it Works

The program utilizes three dictionaries, `D1`, `D2`, and `D3`, which map numbers to their corresponding word equivalents. These dictionaries ensure accurate and reliable conversion from numeric values to their textual counterparts. The program incorporates helper functions, such as `upto3` and `main`, to handle different digit counts and ensure accurate conversion.

## Examples

Here are some examples of number-to-word conversions:

- `NumToWord(123456789)` will output "twelve crore, thirty-four lakh, fifty-six thousand, seven hundred eighty-nine."
- `NumToWord(9000)` will output "nine thousand."
- `NumToWord(42)` will output "forty two."

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you find any issues or would like to suggest enhancements, please create an issue or submit a pull request.

