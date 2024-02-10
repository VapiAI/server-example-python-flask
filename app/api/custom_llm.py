import os
import json
import time  # Used for simulating a delay in streaming
from flask import Blueprint, request, Response, jsonify
from openai import OpenAI

custom_llm = Blueprint('custom_llm', __name__)

client = OpenAI(
  # This is the default and can be omitted
  api_key=os.environ.get("OPENAI_API_KEY"),
)



def generate_streaming_response(data):
  """
  Generator function to simulate streaming data.
  """
  for message in data:
    json_data = message.model_dump_json()
    yield f"data: {json_data}\n\n"




@custom_llm.route('/basic/chat/completions', methods=['POST'])
def basic_custom_llm_route():
  request_data = request.get_json()
  response = {
    "id": "chatcmpl-8mcLf78g0quztp4BMtwd3hEj58Uof",
    "object": "chat.completion",
    "created": int(time.time()),
    "model": "gpt-3.5-turbo-0613",
    "system_fingerprint": None,
    "choices": [
      {
        "index": 0,
        "delta": {"content": request_data['messages'][-1]['content'] if len(request_data['messages']) > 0 else ""},
        "logprobs": None,
        "finish_reason": "stop"
      }
    ]
  }
  return jsonify(response), 200




@custom_llm.route('/openai-sse/chat/completions', methods=['POST'])
def custom_llm_openai_sse_handler():
  request_data = request.get_json()
  streaming = request_data.get('stream', False)

  if streaming:
    # Simulate a stream of responses

    chat_completion_stream = client.chat.completions.create(**request_data)


    return Response(generate_streaming_response(chat_completion_stream), content_type='text/event-stream')
  else:
    # Simulate a non-streaming response
    chat_completion = client.chat.completions.create(**request_data)
    return Response(chat_completion.model_dump_json(), content_type='application/json')


@custom_llm.route('/openai-advanced/chat/completions', methods=['POST'])
def openai_advanced_custom_llm_route():
  request_data = request.get_json()
  streaming = request_data.get('stream', False)


  last_message = request_data['messages'][-1]
  prompt = f"""
    Create a prompt which can act as a prompt template where I put the original prompt and it can modify it according to my intentions so that the final modified prompt is more detailed. You can expand certain terms or keywords.
    ----------
    PROMPT: {last_message['content']}.
    MODIFIED PROMPT: """
  completion = client.completions.create(
    model= "gpt-3.5-turbo-instruct",
    prompt=prompt,
    max_tokens=500,
    temperature=0.7
  )
  modified_message = request_data['messages'][:-1] + [{'content': completion.choices[0].text, 'role': last_message['role']}]

  request_data['messages'] = modified_message
  if streaming:
    chat_completion_stream = client.chat.completions.create(**request_data)


    return Response(generate_streaming_response(chat_completion_stream), content_type='text/event-stream')
  else:
    # Simulate a non-streaming response
    chat_completion = client.chat.completions.create(**request_data)
    return Response(chat_completion.model_dump_json(), content_type='application/json')
