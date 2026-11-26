#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2026 Alexander Bartek <dev.alexander3892@proton.me>
# SPDX-License-Identifier: GPL-3.0-or-later

"""
    Fibonacci Sequence Generator – Iterative Approach: The program validates user input and uses a loop to generate and display the requested number of Fibonacci numbers.

    Copyright (C) 2026 Alexander Bartek <dev.alexander3892@proton.me>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

def main():
    while True:
        try:
            n = int(input("Type in a number "))

            if n <= 0:
                print("Type in a number that is greater than zero.")
                continue

            break

        except ValueError:
            print("This number is incorrect. Try again.")


    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()




main()
