import openai

openai.api_key = "<YOUR_API_KEY>"  # replace with your OpenAI key

prompt_template = """
Given this network state:
{state_info}
Explain what is happening, why, and suggest an intervention.
"""

def get_reasoning(state_info):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt_template.format(state_info=state_info)}],
        max_tokens=250
    )
    return response.choices[0].message["content"]

if __name__ == "__main__":
    sample_state = "Example: latency=120ms, packet_loss=3%, state=degraded"
    print(get_reasoning(sample_state))