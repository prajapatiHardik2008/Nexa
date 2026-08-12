import datetime
import os
import dotenv
import requests

dotenv.load_dotenv()


def apiprocess(command):
  # Command length check
  if len(command) > 25:
    return "Error: Command too long! Please keep it under 25 characters."

  invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
  stream = False

  headers = {
      "Authorization": f"Bearer {os.getenv('AI_API')}",
      "Accept": "text/event-stream" if stream else "application/json",
      "Content-Type": "application/json",
  }

  payload = {
      "messages": [{"role": "user", "content": command}],
      "model": "google/gemma-4-31b-it",
      "chat_template_kwargs": {"enable_thinking": True},
      "max_tokens": 512,
      "stream": stream,
      "temperature": 1,
      "top_p": 0.95,
  }

  current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  try:
    response = requests.post(
        invoke_url, headers=headers, json=payload, stream=stream
    )

    
    if response.status_code != 200:
      error_msg = f"[{current_time}] API ERROR {response.status_code}: {response.text}\n"
      with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(error_msg)
      return f"API Error {response.status_code}"

    data = response.json()

    
    usage = data.get("usage", {})
    prompt_tokens = usage.get("prompt_tokens", 0)
    completion_tokens = usage.get("completion_tokens", 0)
    total_tokens = usage.get("total_tokens", 0)
    reasoning_tokens = usage.get("reasoning_tokens", 0)
    cached_tokens = (
        usage.get("prompt_tokens_details", {}).get("cached_tokens", 0)
    )

    
    log_entry = (
        f"[{current_time}] SUCCESS | Command: '{command}'\n"
        f"   - Prompt Tokens: {prompt_tokens} (Cached: {cached_tokens})\n"
        f"   - Completion Tokens: {completion_tokens}\n"
        f"   - Reasoning Tokens: {reasoning_tokens}\n"
        f"   - Total Tokens Used: {total_tokens}\n"
        "--------------------------------------------------\n"
    )

    with open("logs.txt", "a", encoding="utf-8") as f:
      f.write(log_entry)


    assistant_content = (
        data.get("choices", [{}])[0].get("message", {}).get("content", "")
    )
    return assistant_content

  except Exception as e:
    error_log = f"[{current_time}] EXCEPTION: {str(e)}\n"
    with open("logs.txt", "a", encoding="utf-8") as f:
      f.write(error_log)
    return f"Error: {e}"



