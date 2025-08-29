from litellm import completion

def llm_tool(prompt, model="gemini-pro", max_tokens=800, temperature=0.2):
    response = completion(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=temperature,
        api_base="http://localhost:4000"  # local litellm
    )
    return response["choices"][0]["message"]["content"]