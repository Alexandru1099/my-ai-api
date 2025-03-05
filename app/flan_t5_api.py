from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = FastAPI()

# Încarcă modelul Flan-T5
model_name = "google/flan-t5-small"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Structura cererii
class ChatRequest(BaseModel):
    question: str
    max_tokens: int = 50

@app.post("/chat/")
def chat(request: ChatRequest):
    """ Endpoint pentru generare de răspunsuri """
    input_text = f"Answer the following question: {request.question}"
    inputs = tokenizer(input_text, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=request.max_tokens,
        pad_token_id=tokenizer.eos_token_id
    )

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"question": request.question, "response": result}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
