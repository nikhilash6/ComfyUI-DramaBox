"""
ComfyUI-DramaBox — Expressive TTS inside ComfyUI using the DramaBox LTX diffusion pipeline.

Two nodes (under the DramaBox category):
  DramaBox TTS      — select Gemma, generate audio from a prompt + optional voice reference
  DramaBox Options  — advanced controls: CFG, duration, VRAM management

DramaBox weights (~8.5 GB) download automatically from HuggingFace on first use.
Gemma: place a full HF directory in ComfyUI/models/text_encoders/ — it appears in the dropdown.
Install extra dependencies first:
    pip install -r ComfyUI/custom_nodes/ComfyUI-DramaBox/requirements.txt
"""

import logging

logger = logging.getLogger(__name__)

try:
    from .nodes.dramabox_tts import (
        NODE_CLASS_MAPPINGS as _TTS_CLS,
        NODE_DISPLAY_NAME_MAPPINGS as _TTS_DISP,
    )
    from .nodes.dramabox_options import (
        NODE_CLASS_MAPPINGS as _OPT_CLS,
        NODE_DISPLAY_NAME_MAPPINGS as _OPT_DISP,
    )

    NODE_CLASS_MAPPINGS = {**_TTS_CLS, **_OPT_CLS}
    NODE_DISPLAY_NAME_MAPPINGS = {**_TTS_DISP, **_OPT_DISP}

    logger.info("[ComfyUI-DramaBox] Nodes registered: %s", list(NODE_CLASS_MAPPINGS.keys()))

except Exception as exc:
    logger.error("[ComfyUI-DramaBox] Failed to register nodes: %s", exc)
    NODE_CLASS_MAPPINGS = {}
    NODE_DISPLAY_NAME_MAPPINGS = {}

WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
