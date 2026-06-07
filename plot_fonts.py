"""matplotlib 한글 폰트 설정 (Python 3.12+ / Streamlit Cloud 호환)."""

from __future__ import annotations

from pathlib import Path

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

_FONT_CANDIDATES = (
    Path(__file__).resolve().parent / "fonts" / "NanumGothic.ttf",
    Path("/usr/share/fonts/truetype/nanum/NanumGothic.ttf"),
    Path("/usr/share/fonts/nanum/NanumGothic.ttf"),
)


def setup_korean_font() -> None:
    for path in _FONT_CANDIDATES:
        if not path.is_file():
            continue
        fm.fontManager.addfont(str(path))
        family = fm.FontProperties(fname=str(path)).get_name()
        plt.rcParams["font.family"] = family
        plt.rcParams["axes.unicode_minus"] = False
        return

    plt.rcParams["axes.unicode_minus"] = False
