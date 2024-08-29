# Images

## Generations

Types:

```python
from krutrim_cloud.types.images import StableDiffusionResponse
```

Methods:

- <code title="post /v1/images/generations/diffusion">client.images.generations.<a href="./src/krutrim_cloud/resources/images/generations.py">diffusion</a>(\*\*<a href="src/krutrim_cloud/types/images/generation_diffusion_params.py">params</a>) -> <a href="./src/krutrim_cloud/types/images/stable_diffusion_response.py">StableDiffusionResponse</a></code>


    Parameter List:

    `model_name`: str: "diffusion1XL", # DO NOT CHANGE THIS VALUE

    `prompt`': Union[str, List[str]]: Specify the prompt

    `prompt2`: Union[str, List[str]]: Optional -  Specify any additional prompt details if required

    `image_height`: int: 1024 gives the best output. Although, modify this based on your requirement. Range: 8 to 1024. Although, anything below 512 pixels won't work well 

    `image_width`: int: 1024 gives the best output. Although, modify this based on your requirement. Range: 8 to 1024. Although, anything below 512 pixels won't work well 

    `negative_prompt`: Union[str, List[str]]: Optional, mention aspects (if any) to be ignored in the output image

    `negative_prompt2`: Union[str, List[str]]: Optional, mention aspects (if any) to be ignored in the output image

    `num_output_images`: int: Optional , Defaults to 1. Max value is 5. 

    `guidance_scale`: float: Optional, Defaults to 5. Optimal values are < 15.

    `num_inference_steps`: int: Optional, Defaults to 50. Max value is 100.

    `seed`: int: Optional, Leave it empty to generate a random value. Use the same value if you wish to get the same image. Modify the remaining parameters to get variants of the image

    `output_img_type`: str: Optional, Defaults to pil. Supported: pil, latent. 

    `timeout`: float: Optional,Override the client-level default timeout for this request, in seconds

# Multimodal

## Generations

Types:

```python
from krutrim_cloud.types.multimodal import IdeficsResponse
```

Methods:

- <code title="post /v1/multimodal/generations/idefics">client.multimodal.generations.<a href="./src/krutrim_cloud/resources/multimodal/generations.py">idefics</a>(\*\*<a href="src/krutrim_cloud/types/multimodal/generation_idefics_params.py">params</a>) -> <a href="./src/krutrim_cloud/types/multimodal/idefics_response.py">IdeficsResponse</a></code>

    Parameter List:
    
    `model_name`: str: "idefics" # DO NOT CHANGE THIS VALUE

    `prompts`:  list: Example
    ```
    [
        "<image bytes>  ", # encoded image byte data
        "what is the city??"  # Add the prompt/question to be sent to the model related to the image here
    ]
    ```
    `images`: list: Example
    ```
    [
        [<encoded image bytes here>], # encoded image byte data
        [] # This value is empty since there is no image reference at this index in the prompts list
    ]
    ```
    `max_tokens`: int: 50 - Max tokens can be generated [8 - 1024]

# Audio

## Transcriptions

Types:

```python
from krutrim_cloud.types import WhisperResponse
```

Methods:

- <code title="post /v1/audio/transcriptions">client.audio.transcriptions.<a href="./src/krutrim_cloud/resources/audio/transcriptions.py">create</a>(\*\*<a href="src/krutrim_cloud/types/audio/transcription_create_params.py">params</a>) -> <a href="./src/krutrim_cloud/types/shared/whisper_response.py">WhisperResponse</a></code>

    Parameter List:
    
    `file`: str | Path | AudioSegment: "your base64 encoded audio byte data here" OR "Path object of pathlib for the audio filepath" OR "PyDub AudioSegment object of Audio/Video"
    
    `model_name`: str : "openai/whisper-large-v3", # DO NOT CHANGE THIS
    
    `task`: str : "transcribe", # DO NOT CHANGE THIS
    
    `language`: str : "hindi", # Source language of the audio
    
    `temperature`:  float : 0.0, # Optional, defaults to 0.0. Range - 0.0 to 2.0
    
    `response_format`: str : "json", # Optional, defaults to json. Values - verbose_json (or) json
    
    `chunk_type`: str : "word" # Optional, defaults to sentence. Values - sentence (or) word

## Translations

Types:

```python
from krutrim_cloud.types import WhisperResponse
```

Methods:

- <code title="post /v1/audio/translations">client.audio.translations.<a href="./src/krutrim_cloud/resources/audio/translations.py">create</a>(\*\*<a href="src/krutrim_cloud/types/audio/translation_create_params.py">params</a>) -> <a href="./src/krutrim_cloud/types/shared/whisper_response.py">WhisperResponse</a></code>

    Parameters List:

    `file`: str | Path | AudioSegment: "your base64 encoded audio byte data here" OR "Path object of pathlib for the audio filepath" OR "PyDub AudioSegment object of Audio/Video"

    `model_name`: str: "openai/whisper-large-v3", # DO NOT CHANGE THIS

    `task`: str: "translate" # DO NOT CHANGE THIS

    `temperature`: float : 0.0, # Optional, defaults to 0.0. Range - 0.0 to 2.0

# Chat

## Completions

Types:

```python
from krutrim_cloud.types.chat import CompletionCreateResponse
```

Methods:

- <code title="post /v1/chat/completions">client.chat.completions.<a href="./src/demo_project/resources/chat/completions.py">create</a>(\*\*<a href="src/demo_project/types/chat/completion_create_params.py">params</a>) -> <a href="./src/demo_project/types/chat/completion_create_response.py">CompletionCreateResponse</a></code>

    Parameter List:

    `model`: str: "Krutrim-spectre-v2", Supported Values are: "Krutrim-spectre-v2", "Mistral-7B-Instruct", "Meta-Llama-3-8B-Instruct"

    `messages`: list[dict] : Example
    ```
    [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Hello!"
        }
    ]
    ```

    `frequency_penalty`: float: 0, # Optional, Defaults to 0. Range: -2.0 to 2.0

    `logit_bias`: dict: {2435: -100, 640: -100}
    
    `logprobs`: bool: true, # Optional, Defaults to false

    `top_logprobs`: int: 2, # Optional. Range: 0 to 50

    `max_tokens`: int: 256, # Optional

    `n`: int: 1, # Optional, Defaults to 1

    `presence_penalty`: float: 0, # Optional, Defaults to 0. Range: -2.0 to 2.0

    `response_format`: dict: { "type": "text" }, # Optional, Defaults to text

    `stop`: str: null, # Optional, Defaults to null. Can take up to 4 sequences where the API will stop generating further tokens.

    `stream`: bool: false, # Optional, Defaults to false

    `temperature`: float: 0, # Optional, Defaults to 1. Range: 0 to 2

    `top_p`: float: 1 # Optional, Defaults to 1. We generally recommend altering this or temperature but not both.

