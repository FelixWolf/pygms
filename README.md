GameMaker: Studio data parser and writer
========================================

Wewlad. For now, it reads stuff, it *might* write data later.
Expect full support. May be even usable to write a GMS player/debugger in pygame? Idk.

Support
-------

Currently supports GMS 2 data(Tested with data.win).

Chunk status!

Chunk | Support | Notes
----- | ------- | -----
FORM  | Part    | Cannot be finished until all chunks supported.
GEN8  | Full    |
GEN7  | Full (?)| Partually tested, no data to test on. Implemented in `GEN8.py`.
STRG  | Full    |
AUDO  | Full    | Does not decode files, only stores them in memory.
PATH  | Impl    | Base exists as well as format, but no data to test on.
BGRN  | Full    |
CODE  | Full    | Does not parse code, see `bytecode.py`.
OPTN  | Full    |
LANG  | Part (?)| Untested, boiler plate exists.
EXTN  | None    | To be added.
SOND  | Full    |
AGRP  | None    | To be added.
SPRT  | Full    |
SCPT  | None    | To be added.
GLOB  | None    | To be added.
SHDR  | None    | To be added.
FONT  | None    | To be added.
TMLN  | None    | To be added.
OBJT  | Full    |
ROOM  | None    | To be added.
DAFL  | None    | To be added.
EMBI  | None    | To be added.
TPAG  | Full    |

Disclaimer
----------

What you do with this library is *your* responsibility. Please be respectful of creator's rights.
This is intended as a educational, debugging, experimentation, and *SCIENCING* tool. This is **NOT** a way to circumvent game DRM or other similar stuff. Doing so will result in me and many others frowning upon your actions.

This is not a YoYo Games product. It is not sponsored, endorced, or otherwise supported by YoYo Games.
GameMaker: Studio and YoYo Games are registered trademarks of YoYo Games.
