import ollama
import requests
# ----------------- BEGIN OF TOOL: Get Current Weather ----------------- 
def get_current_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"Weather of {city} today: {data['current_condition']}"
        else:
            return ""
    except Exception as e:
        return str(e)
    

weather_tool = {
      'type': 'function',
      'function': {
        'name': 'get_current_weather',
        'description': 'Get the current weather for a city.',
        'parameters': {
          'type': 'object',
          'properties': {
            'city': {
              'type': 'string',
              'description': 'The name of the city',
            },
          },
          'required': ['city'],
        },
      }
    }
# ----------------- END OF TOOL: Get Current Weather ----------------- 

messages = [{'role': 'user', 'content': "What is the weather in Tokyo right now?"}]

response = ollama.chat(
    model='llama3.1',
    messages=messages,
    tools=[weather_tool]
)


print("Parsing tools: ", response['message'])

# if tool calling is needed
if len(response['message']['tool_calls']) > 0:
    # add message into the context
    messages.append(response['message'])
    # Parse the tool & argugments
    tool = response['message']['tool_calls'][0]
    function_name = tool['function']['name']
    args = tool['function']['arguments'].values()

    if function_name == 'get_current_weather':
        # call weather api
        function_response = get_current_weather(*args)
        # add api resonse into the context
        messages.append({'role': 'tool', 'content': function_response})

# Send the message context to llama3.1, get the final response
final_response = ollama.chat(model='llama3.1', messages=messages)

# Print the result
print("\033[1;31m",final_response['message']['content'],"\033[0m",)

