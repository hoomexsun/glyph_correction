# glyph_correction 🏁

Built to correct s550 glyphs into Bengali Unicode characters.

## Status

🏁 This repository is fully developed!

## Quickstart

1. Clone this repository.

   ```sh
   git clone https://github.com/hoomexsun/glyph_correction.git
   ```

2. Install python requirements. Please refer [requirements.txt](requirements.txt)
3. Now, run `main.py`.

## Custom Usage

After Step 1 & 2 from Quickstart.

1. Add your file.
2. Extract the string from the file and call either `gc.correct()` or `gc.correct_words()`.

   ```python
   # main.py
   from pathlib import Path
   from src.gc_ import GlyphCorrection

   content = Path("<YOUR_FILE_PATH>").read_text(encoding="utf-8")
   gc = GlyphCorrection()

   output_1 = gc.correct_words(content) # For huge text
   # or
   output_2 = gc.correct(content) # Simpler
   ```

3. Now, run `main.py`.

## Use in your repository (as submodule)

1. Add this repository as submodule

   ```bash
   git submodule add https://github.com/hoomexsun/glyph_correction.git
   ```

2. Create a `GlyphCorrection` object after importing and then use its functions.

   ```python
   from glyph_correction import GlyphCorrection
   gc = GlyphCorrection()
   ...
   ```

## GUI

Check out gui built using tkinter on [XLIT](https://github.com/hoomexsun/xlit).

## Algorithm 1 (Glyph Correction)

**Input:** Unicode used as Bengali Glyph, A or {a₀, a₁, …, aₘ₋₁}  
**Output:** Correct Bengali Unicode, B or {b₀, b₁, …, bₙ₋₁}

1. Pre-adjust glyphs in **A**
2. **B** ← map_unicode[**A**]  
   **B** ← (**B** ∪ `r_glyph`) - **A**
3. for bᵢ in **B**:
   - if bᵢ is `r glyph` written on right:
     - bᵢ is removed and inserted using Jump (Reverse)
     - bᵢ ← map_unicode[bᵢ]
4. for bᵢ in **B**:
   - if bᵢ is `vowel` written on left:
     - bᵢ is removed and inserted using Jump
   - if bᵢ and bᵢ₊₁ are actually vowel written by enclosing:
     - bᵢ and bᵢ₊₁ are replaced with correct unicode
5. Return the resulting string **B**

## See also

- [Glyph Correction](https://github.com/hoomexsun/glyph_correction).
- [Meetei/Meitei Mayek Transliteration](https://github.com/hoomexsun/mm_transliteration).
- [Meetei/Meitei Mayek Keyboard for Windows](https://github.com/hoomexsun/mm_keyboard).
- [Wahei Tool](https://https://github.com/hoomexsun/wahei).
