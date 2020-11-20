import requests
from typing import Tuple


class color:

    __HEX_CHARS = ('0', '1', '2', '3', '4', '5', '6', '7',
                   '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')

    # - - - I N I T - M E T H O D S - - - #

    def __init__(self,
                 hex: str = None,
                 rgb: Tuple[int, int, int] = None,
                 hsl: Tuple[int, float, float] = None,
                 cmyk: Tuple[int, int, int, int] = None,
                 ) -> None:

        inputs = [hex, rgb, hsl, cmyk]
        if sum(x is not None for x in inputs) != 1:
            # If color specified more then once,
            # or not specified at all
            raise ValueError("Specify one color (single format) at a time")

        if hex:
            self._request_by_hex(hex)

        if rgb:
            self._request_by_rgb(rgb)

        if hsl:
            self._request_by_hsl(hsl)

        if cmyk:
            self._request_by_cmyk(cmyk)

    def _request_by_hex(self,
                        value: str,
                        ) -> None:
        """ Make a request to thecolorapi.com, with the given hex value.
        value should be a 6 char string.
        """

        if not isinstance(value, str):
            # If not a string
            raise TypeError("Hex color must be represented as string")

        # Remove '#' and '0x' from the string, convert to lowercase
        value = value.replace('#', '').replace('0x', '').lower()

        # Remove invalid chars from string
        value = [char
                 for char in value
                 if char in self.__HEX_CHARS]
        value = ''.join(value)  # convert back to string from list

        if len(value) != 6:
            # If string length is not 6
            raise ValueError("Invalid hex string")

        # Make an api request and save the json output.
        self._request({"hex": value})

    def _request_by_rgb(self,
                        value: Tuple[int, int, int],
                        ) -> None:
        """ Make a request to thecolorapi.com, with the given rgb value.
        value should be a tuple, containing 3 integers between 0 and 255. """

        if not isinstance(value, tuple):
            # If not tuple
            raise TypeError("RGB color must be represented as a tuple")

        if len(value) != 3 or not all(isinstance(v, int) for v in value):
            # If tuple length is not 3
            # If values inside tuple are not integers
            raise ValueError("RGB tuple must contain 3 integers")

        # force only numbers between 0 and 255
        value = (self.minmax(v, 0, 255) for v in value)

        # convert from tuple to string
        value = (str(color) for color in value)
        param = ','.join(value)

        # Make an api request and save the json output
        self._request({"rgb": param})

    def _request_by_hsl(self,
                        value: Tuple[int, int, int]):
        """ Make a request to thecolorapi.com, with the given hsl value.
        value should be a tuple. The tuple should contain three values:

        -   value[0] (int)
            Represents the hue, in degrees (between 0 and 359)

        -   value[1] (int)
            Represents the saturation, as a nubmer between 0 and 100.

        -   value[2] (int)
            Represents the lightness, as a number between 0 and 100.
        """

        if not isinstance(value, tuple):
            # If not tuple
            raise TypeError("HSL color must be represented as a tuple")

        if len(value) != 3 or not all(isinstance(v, int) for v in value):
            # If tuple length is not 3
            # If values inside tuple are not integers
            raise ValueError("HSL tuple must contain 3 integers")

        value = list(value)

        # Mod 360 on hue degrees
        value[0] = value[0] % 360

        # force saturation and lightness to be between 0 and 100
        value[1:] = [minmax(v, 0, 100) for v in value[1:]]

        # Convert to string
        value = (str(color) for color in value)
        value = ','.join(value)

        # Make an api request and save the json output
        self._request({"hsl": value})

    def _request_by_cmyk(self,
                         value: Tuple[int, int, int, int]
                         ) -> None:
        """ Make a request to thecolorapi.com, with the given cmyk value.
        value should be a tuple, containing 4 integers between 0 and 100. """

        if not isinstance(value, tuple):
            # If not tuple
            raise TypeError("CMYK color must be represented as a tuple")

        if len(value) != 4 or not all(isinstance(v, int) for v in value):
            # If tuple length is not 4
            # If values inside tuple are not integers
            raise ValueError("CMYK tuple must contain 4 integers")

        # force only numbers between 0 and 100
        value = (self.minmax(v, 0, 100) for v in value)

        # convert from tuple to string
        value = (str(color) for color in value)
        param = ','.join(value)

        self._request({"cmyk": param})

    def _request(self,
                 params: dict):

        response = requests.get(
            "https://www.thecolorapi.com/id",
            params=params)

        if response.status_code != 200:
            raise ValueError(response.json["message"])

        self.__json = response.json()

    # - - - G E T - P R O P E R T I E S - - - #

    @property
    def hex(self,
            ) -> str:
        """ The color, represented as a hex string.
        For instance, `#0047AB`.
        """

        return self.__json["hex"]["value"]

    @property
    def hex_clean(self,) -> str:
        """ The color, represented as a clear hex string (without `#`).
        For instance, `0047AB`.
        """

        return self.__json["hex"]["clean"]

    @property
    def rgb(self,) -> Tuple[int, int, int]:
        """ The color, represented as tuple in the rgb format.
        Values will range between 0 and 255.
        For instance, `(0, 71, 171)`.
        """

        rgb = self.__json["rgb"]
        return (rgb["r"], rgb["g"], rgb["b"])

    @property
    def rgb_fraction(self) -> Tuple[float, float, float]:
        """ The color, represented as a tuple in the rgb format.
        values will range between 0 and 1 (floating).
        For instance, `(0, 0.278, 0.670)`.
        """

        rgb = self.__json["rgb"]["fraction"]
        return (rgb["r"], rgb["g"], rgb["b"])

    @property
    def hsl(self,) -> Tuple[int, int, int]:
        """ The color, represented as a tuple in the hsl format.
        For the first cell (representing the hue), values will range between
        0 and 359 (degrees).
        For the 2nd and 3rd cells, values will range between 0 and 100.
        For instance, `(215, 100, 34)`.
        """

        hsl = self.__json["hsl"]
        return (hsl["h"], hsl["s"], hsl["l"])

    @property
    def hsl_fraction(self,) -> Tuple[float, float, float]:
        """ The color, represented as a tuple in the hsl format.
        Values will range between 0 and 1 (floating).
        For instance, `(0.597, 1, 0.335)`.
        """

        hsl = self.__json["hsl"]["fraction"]
        return (hsl["h"], hsl["s"], hsl["l"])

    @property
    def hsv(self,) -> Tuple[int, int, int]:
        """ The color, represented as a tuple in the hsv format.
        For the first cell (representing the hue), values will range between
        0 and 359 (degrees).
        For the 2nd and the 3rd cells, values will range between 0 and 100.
        For instance, `(215, 100, 34)`.
        """

        hsv = self.__json["hsv"]
        return (hsv["h"], hsv["s"], hsv["v"])

    @property
    def hsv_fraction(self,) -> Tuple[float, float, float]:
        """ The color, represented as a tuple in the hsv format.
        Values will range between 0 and 1 (floating).
        For instance, `(0.597, 1, 0.670)`.
        """

        hsv = self.__json["hsv"]["fraction"]
        return (hsv["h"], hsv["s"], hsv["v"])

    @property
    def cmyk(self,) -> Tuple[int, int, int, int]:
        """ The color, represented as a tuple in the cmyk format.
        Values will range between 0 and 100.
        For instace, `(100, 58, ,0, 33)`.
        """

        cmyk = self.__json["cmyk"]
        return (cmyk["c"], cmyk["m"], cmyk["y"], cmyk["k"])

    @property
    def cmyk_fraction(self,) -> Tuple[float, float, float, float]:
        """ The color, represented as a tuple in the cmyk format.
        Values will range between 0 and 1 (floating).
        For instance, `(1, 0.584, 0, 0.329)`.
        """

        cmyk = self.__json["cmyk"]["fraction"]
        return (cmyk["c"], cmyk["m"], cmyk["y"], cmyk["k"])

    @property
    def contrast_hex(self,) -> str:
        """ A hex representation of black (`#000000`) or white (`#ffffff`) as a
        string. Returns the opposite color of this one. Useful for text color
        when this color is the background color, for example.
        """

        return self.__json["contrast"]["value"]

    @property
    def name(self,) -> str:
        """ A string representing (naming) the color. """

        return self.__json["name"]["value"]

    # - - - P R I V A T E - M E T H O D S - - - #

    @staticmethod
    def minmax(value1, value2, value3):
        """ Recives 3 values, and returns the one that is in between the two. """

        list = [value1, value2, value3]
        list.sort()
        return list[1]
