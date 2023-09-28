# -*- coding: utf-8 -*-
from pyth.plugins.python.reader import P, PythonReader, ITALIC, BOLD, T, L, LE


def buildDoc():
    return PythonReader.read((
        P[
            T(ITALIC, BOLD)["Hello World"],
            ", hee hee hee! ", T(url='http://www.google.com')["This seems to work"]
        ],
        L[
            [str(word) for word in ("One", "Two", "Three", "Four")]
        ],
        L[
            "Introduction",
            LE[
                "First sentence in the\nsub-section",
                "Also some other stuff",
                L[
                    "Alpha",
                    L[
                        "Beta\nWhomble",
                        LE["Beta", "Whoop\nWhoa"],
                        "Beta",
                    ],
                    "Gamma",
                    "Gamma",
                ],
                "Final sentence in the sub-section",
            ],
            T(BOLD)["Conclusion"],
        ],
        "That's all, folks! 再見!"
    ))
