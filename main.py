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


def prepare_eval():
    wordmap_content = Path("data/wordmap.txt").read_text(encoding="utf-8").strip()
    new_content = ""
    for word_pair in wordmap_content.split("\n"):
        word_bn, word_mm = word_pair.split("\t")
        new_content += f"{word_pair}\t{len(word_mm)}\t0\t{word_mm}\n"
    Path("exp/eval.txt").write_text(new_content.strip(), encoding="utf-8")


def evaluate():
    eval_content = Path("exp/eval_completed.txt").read_text(encoding="utf-8").strip()
    distribution = {
        "1": 0,  # Indigenous
        "2": 0,  # Loan word
        "3": 0,  # Named Entity
        "4": 0,  # Mixed (Loan+ind or named+ind)
    }
    err = 0
    M = 0  # number of words
    N = 0  # Number of characters
    num_not_ok = 0  # Number of words without error
    for line in eval_content.split("\n"):
        words = line.split("\t")
        M += 1
        N += int(words[2])
        if words[3] != "0":
            num_not_ok += 1
            err += int(words[3])
        if len(words) == 6:
            distribution[words[5]] += 1

    print(f"Word Level Accuracy={1-num_not_ok/M=:.02f} | {num_not_ok=} | {M=}")
    print(f"Character Level Accuracy={1-err/N=:.02f} | {err=} | {N=}")
    print(f"{distribution=} | Total={sum(distribution.values())}")


if __name__ == "__main__":
    # run()
    # prepare_eval()
    evaluate()
