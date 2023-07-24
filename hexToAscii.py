class HexToAsciiConverter:
    def __init__(self, hex_string):
        self.hex_string = hex_string

    def convert(self):
        try:
            # lets remove the leading '0x' if present
            if self.hex_string.startswith('0x'):
                self.hex_string = self.hex_string[2:]

            # the actuall conversion
            ascii_string = bytes.fromhex(self.hex_string).decode('ascii')
            return ascii_string
        
        except ValueError:
            return "invalid Hexadecimal Input"
        
if __name__ == "__main__":
    hex_input = input("Enter hex string")
    converter = HexToAsciiConverter(hex_input)
    result = converter.convert()
    print("ASCII representation: ", result)
