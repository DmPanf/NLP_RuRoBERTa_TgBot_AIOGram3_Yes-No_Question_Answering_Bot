import re
import torch

# Список стоп-слов
stop_words = """или, но, дабы, затем, потом, лишь только, он, мы, его, вы, вам, вас, ее, что,
который, их, все, они, я, весь, мне, меня, таким, для, на, по, со, из, от, до, без, над, под, за, при, после, во,
же, то, бы, всего, итого, даже, да, нет, ой, ого, эх, браво, здравствуйте, спасибо, извините,
скажем, может, допустим, честно говоря, например, на самом деле, однако, вообще, в, общем, вероятно, очень,
минимально, максимально, абсолютно, огромный, предельно, сильно, слабо, самый, сайт, давать, всегда, однако, и, а, но, да, если, что, когда, потому, что, так, как, как, будто,
вследствие, того, что, с, тех, пор, как, в, то, время, как, для, того, чтобы, ни, то, ли, но, зато, от, и, к, кто, что,
такой, такое, такая, почему"""

stop_words_set = set(stop_words.replace('\n', '').split(', '))

def clean_text(text):
    # Удаление ссылок
    text = re.sub(r'http\S+', '', text)
    # Удаление специальных символов
    text = re.sub(r'[^A-Za-zА-Яа-я0-9\s]', '', text)
    # Удаление лишних пробелов
    text = re.sub(r'\s+', ' ', text).strip()

    # Удаление стоп-слов
    words = text.split()
    cleaned_words = [word for word in words if word.lower() not in stop_words_set]
    return ' '.join(cleaned_words)

def predict_answer(question, passage, model, tokenizer, device):
    # Очистка текста
    question = clean_text(question)
    passage = clean_text(passage)

    inputs = tokenizer.encode_plus(
        question, passage,
        add_special_tokens=True,
        max_length=512,
        padding='max_length',
        truncation=True,
        return_tensors='pt'
    )

    input_ids = inputs['input_ids'].to(device)
    attention_mask = inputs['attention_mask'].to(device)

    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()

    return "Yes" if predicted_class == 1 else "No"
