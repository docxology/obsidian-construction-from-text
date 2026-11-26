# Reproduction and limitations {#sec:limits}

Use the repository's documented Python installation, select the synthetic garden folder with `--texts_dir`, and write the output to a fresh directory with `--obsidian_dir`. Pass `--skip_topics` and run `docs/examples/verify_vault.py` over that directory. This scope covers source structure and generated artifacts without needing a personal vault, a live service, or a plugin.

The graph count includes candidate expressions that can overlap or reflect incidental capitalization and document labels. The fixture is too small to evaluate extraction precision, topic quality, or note navigation at corpus scale. Markdown dialects beyond the documented structured format and filename collisions also require independent checks. The retained vault is a prior generated example with its own source inputs.
