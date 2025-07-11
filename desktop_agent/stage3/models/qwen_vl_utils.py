import torch
from transformers import BitsAndBytesConfig
from config import MODEL_PATH, QUANTIZATION_CONFIG

from modelscope import Qwen2_5_VLForConditionalGeneration, AutoProcessor

def load_model_and_processor():
    """加载模型和处理器"""
    model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
        MODEL_PATH,
        quantization_config=QUANTIZATION_CONFIG,
        torch_dtype="auto",
        device_map="auto",
        local_files_only=True
    )

    processor = AutoProcessor.from_pretrained(MODEL_PATH, local_files_only=True)

    return model, processor

