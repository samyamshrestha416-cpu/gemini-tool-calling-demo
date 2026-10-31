# Gemini Tool Calling Demo

A small product assistant for a fictional coffee company, **GlobalJava Roasters**,
built with the **Google Gemini API** and **tool calling**.

Instead of guessing prices or product details, the model asks the program to run
Python functions that read the real product data, then answers using the result.

This is a learning project. The idea comes from the Dataquest tutorial
"How to Connect an LLM to Python Functions (Tool Calling Tutorial)". I adapted it
from the OpenAI style to Google's `google-genai` library.

## How tool calling works

1. I give the model a list of Python functions (the "tools").
2. The user asks a question, for example "How much is the house blend?"
3. The model does not answer from memory. It asks for a tool call, such as
   `get_product_info(product_id="house-blend")`.
4. My code runs the real function and gets the data.
5. The result goes back to the model, which writes the final answer.

The model never runs any code itself. It only chooses which function to call and
with which inputs. It learns what each tool does from the function's **name**,
**type hints**, and **docstring**.

## Tools

| Tool | What it does |
|------|--------------|
| `get_product_info(product_id)` | Returns the name, origin, flavor profile, price, and certifications of a product |
| `calculate_total_price(product_ids)` | Adds up the prices of the products a customer wants to buy |

Both live in `products.py`. If a product id does not exist, the tool returns a
clear error message, so the model can tell the user instead of inventing a product.

## Project structure

```
Tool_calling/
├── products.py            # Product data and the tool functions
├── product_assistant.py   # Sends one question to Gemini with the tools attached
├── requirements.txt       # Python packages
└── .gitignore             # Keeps .env and venv out of Git
```

## Setup

1. **Create a virtual environment and install the packages:**

   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Mac/Linux
   pip install -r requirements.txt
   ```

2. **Get a Gemini API key** from Google AI Studio (it has a free tier).

3. **Create a `.env` file** in the project folder (never upload this file):

   ```
   GEMINI_API_KEY=your_key_here
   ```

4. **Run it:**

   ```bash
   python product_assistant.py
   ```

Model names change often. If you get a "model not found" error, check Google's
documentation for a current Flash model and update the name in the code.

## Example

Question:

```
What can you tell me about Yirgacheffe coffee?
```

Terminal output while it runs:

```
TOOL CALLED with: ethiopian-yirgacheffe
```

The assistant then answers with the origin, flavor notes, certifications, and
price taken from the product data.

Another example:

```
How much would 2 house blends and 1 geisha reserve cost?
```

The model calls `calculate_total_price` with
`["house-blend", "house-blend", "geisha-reserve"]`, and the total is calculated by
Python, not by the model.

## What I learned

- Gemini builds the tool description from a Python function, so a clear docstring
  and type hints matter
- The model can only use the product ids the docstring tells it about, so the docstring
  must list the real ids
- Why arithmetic is better done by a tool than by the model
- The difference between OpenAI's tool format (JSON) and Gemini's (Python functions)
- Printing inside a tool proves that my own code runs, not the model's

## Ideas for improvement

- A `list_products` tool so the model can discover available products
- A chat loop that remembers the conversation
- Read products from a database instead of a dictionary
- Handle several tool calls in one question and print each one
