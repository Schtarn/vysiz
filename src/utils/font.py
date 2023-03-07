"""
The MIT License (MIT)

Copyright (c) 2023-present shiüo

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from PySide6.QtGui import QFontDatabase

from utils import global_path


def load(path):
    return QFontDatabase.applicationFontFamilies(
        QFontDatabase.addApplicationFont(global_path.get_proj_abs_path(path))
    )[0]


def load_font(w):
    w.Pretendard_Black = load("assets/fonts/Pretendard-Black.otf")
    w.Pretendard_Bold = load("assets/fonts/Pretendard-Bold.otf")
    w.Pretendard_ExtraBold = load("assets/fonts/Pretendard-ExtraBold.otf")
    w.Pretendard_ExtraLight = load("assets/fonts/Pretendard-ExtraLight.otf")
    w.Pretendard_Light = load("assets/fonts/Pretendard-Light.otf")
    w.Pretendard_Medium = load("assets/fonts/Pretendard-Medium.otf")
    w.Pretendard_Regular = load("assets/fonts/Pretendard-Regular.otf")
    w.Pretendard_SemiBold = load("assets/fonts/Pretendard-SemiBold.otf")
    w.Pretendard_Thin = load("assets/fonts/Pretendard-Thin.otf")
