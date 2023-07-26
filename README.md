# JSON Fixer

JSON Fixer is a versatile Python package designed to efficiently handle and correct JSON data. With its user-friendly interface, the package offers seamless JSON data manipulation and restoration capabilities, making it an essential tool for developers working with JSON files and APIs.

## Key Features

- Efficiently handle and correct JSON data.
- User-friendly interface for easy manipulation.
- Seamless restoration of JSON data.
- Simplifies the process of rectifying JSON errors.
- Ensures data consistency and accuracy.

## Installation

### From PyPI

You can install JSON Fixer using pip from the Python Package Index (PyPI):

```bash
pip install jsonfixer
```

### From GitHub

Alternatively, you can clone the repository from GitHub and install it manually:

```bash
git clone https://github.com/cool425589/jsonfixer.git
cd jsonfixer
pip install .
```

## Usage

```python
import jsonfixer

repaired_str = jsonfixer.JsonRepair("{the json str you wanna fix}").repair()

```

## Example

```python
import jsonfixer

# Your JSON manipulation and correction code here
json_str = """ {"school":"台灣大學","department":"資訊工程",} """
repaired_str = jsonfixer.JsonRepair(json_str).repair()

```

```
>>> repaired_str
' {"school":"台灣大學","department":"資訊工程"} '
```

## Contributions

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/cool425589/jsonfixer/blob/main/LICENSE.txt) file for details.

## Contact

For any inquiries or questions, please contact us at cool425589@gmail.com
