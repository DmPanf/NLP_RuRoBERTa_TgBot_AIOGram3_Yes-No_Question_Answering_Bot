import os
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from safetensors.torch import load_file
from dotenv import load_dotenv

load_dotenv()  # Загрузка переменных окружения из .env
model_directory = os.getenv('MODEL_DIRECTORY')

# +++++++++ Более безопасный вариант работы с загружаемыми моделями ++++++
def load_model_and_tokenizer():
    # Загрузка токенизатора и модели с указанием имени файла весов model.safetensors
    tokenizer = AutoTokenizer.from_pretrained(model_directory)  # Загрузка токенизатора
    # Загрузка конфигурации модели
    config = AutoModelForSequenceClassification.from_pretrained(model_directory).config
    # Инициализация пустой модели с той же конфигурацией
    model = AutoModelForSequenceClassification.from_config(config)
    # Загрузка весов модели из файла .safetensors
    weights_path = os.path.join(model_directory, "model.safetensors")
    state_dict = load_file(weights_path)  # Используем load_file для загрузки весов (возвращает их как state_dict)
    model.load_state_dict(state_dict)

    # Определение устройства (GPU или CPU)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    model.eval()

    return model, tokenizer, device


#from transformers import AutoTokenizer, AutoModelForSequenceClassification
#def load_model_and_tokenizer():    # Загрузка модели и токенизатора вида model.bin
#    tokenizer = AutoTokenizer.from_pretrained(model_directory)
#    model = AutoModelForSequenceClassification.from_pretrained(model_directory)
#    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#    model.to(device)
#    model.eval()
#    return model, tokenizer, device
