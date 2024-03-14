# glyph_correction 🏁

Built to correct s550 glyphs into Bengali Unicode characters.

## Status

🏁 This repository is fully developed!

## Quickstart

1. Clone this repository along with submodules.

   ```sh
   git clone --recurse-submodules https://github.com/hoomexsun/glyph_correction.git
   ```

2. Install python requirements. Please refer [requirements.txt](requirements.txt)
3. Now, run `main.py`.

### Usage

After Step 1 & 2 from Quickstart.

1. Add your file.
2. Extract the string from the file and call either `gc.correct()` or `gc.correct_words()`.

   ```python
   from pathlib import Path
   from gc_ import GlyphCorrection

   content = Path("<YOUR_FILE_PATH>").read_text(encoding=utf-8)
   gc = GlyphCorrection()

   output_1 = gc.correct_words(content) # For huge text
   # or
   output_2 = gc.correct(content) # Simpler
   ```

3. Now, run `main.py`.

## GUI

Run `gui.py`. (Still under construction 🚧)

## Algorithm

**Input:** Unicode used as Bengali Glyph, {a₀, a₁, …, aₘ₋₁}  
**Output:** Correct Bengali Unicode {b₀, b₁, …, bₙ₋₁}

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

### FAQ

- If you forgot to add submodule, init and install submodules afterwards.

  ```sh
  git submodule init
  git submodule update
  ```

## See also

- [Glyph Correction](https://github.com/hoomexsun/glyph_correction).
- [Meetei/Meitei Mayek Transliteration](https://github.com/hoomexsun/mm_transliteration).
- [Meetei/Meitei Mayek Keyboard for Windows](https://github.com/hoomexsun/mm_keyboard).
- [Wahei Tool](https://https://github.com/hoomexsun/wahei)
