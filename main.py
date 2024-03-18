from pathlib import Path

from src.gc_ import GlyphCorrection
from utils import create_wordmap


def run(
    mk_wmap: bool = True,
):
    root_dir = "data"
    data_path = f"{root_dir}/words.txt"
    output_path = f"{root_dir}/output.txt"
    wordmap_path = f"{root_dir}/wordmap"

    content: str = Path(data_path).read_text(encoding="utf-8")
    gc = GlyphCorrection()
    output: str = gc.correct_words(content)
    Path(output_path).write_text(output, encoding="utf-8")
    Path(output_path).with_suffix(".min").write_text(
        "\n".join(
            sorted({word.strip() for word in output.split("\n") if word.strip()})
        ),
        encoding="utf-8",
    )
    if mk_wmap:
        create_wordmap(content, output, wordmap_path)


if __name__ == "__main__":
    run()
