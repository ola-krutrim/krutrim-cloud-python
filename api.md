# Text to Image Generation
Examples:

---
- **Stable Diffusion Model**: [StableDiffusion1XL.py](./examples/models/StableDiffusion1XL.py) - This script contains the implementation of the Stable Diffusion model.


#### Methods:

---

:arrow_right: <code title="post /v1/images/generations/diffusion">client.images.generations.<a href="./src/krutrim_cloud/resources/images/generations.py">diffusion</a>(\*\*<a href="src/krutrim_cloud/types/images/generation_diffusion_params.py">params</a>) -> <a href="./src/krutrim_cloud/types/images/stable_diffusion_response.py">StableDiffusionResponse</a></code>

```python
from krutrim_cloud.types.images import StableDiffusionResponse
```


### Request Parameter List:

`model_name`: str: "diffusion1XL", # DO NOT CHANGE THIS VALUE

    Specifies the model to be used for generating the image.

`prompt`': Union[str, List[str]]: Specify the prompt

    Defines the main text or texts that describe what you want the image to depict. It could be a single string or a list of strings.

`prompt2`: Union[str, List[str]]: Optional -  Specify any additional prompt details if required

    Provides additional details or context to refine the image generation. It can be a single string or a list of strings.

`image_height`: int: 1024 gives the best output. Although, modify this based on your requirement. Range: 8 to 1024. Although, anything below 512 pixels won't work well 

    Specifies the height of the generated image in pixels.

`image_width`: int: 1024 gives the best output. Although, modify this based on your requirement. Range: 8 to 1024. Although, anything below 512 pixels won't work well 

    Specifies the width of the generated image in pixels.

`negative_prompt`: Union[str, List[str]]: Optional, mention aspects (if any) to be ignored in the output image

    Lists aspects or features to avoid in the generated image. It helps exclude unwanted elements.

`negative_prompt2`: Union[str, List[str]]: Optional, mention aspects (if any) to be ignored in the output image

    Provides additional aspects to be avoided in the output image, similar to negative_prompt

`num_output_images`: int: Optional , Defaults to 1. Max value is 5. 

    Determines the number of images to generate in response to the request.

`guidance_scale`: float: Optional, Defaults to 5. Optimal values are < 15.

    Controls how strongly the model adheres to the prompt. Higher values make the model stick more closely to the prompt.

`num_inference_steps`: int: Optional, Defaults to 50. Max value is 100.

    Defines the number of steps for the inference process. More steps can lead to higher quality images but also longer processing time.

`seed`: int: Optional, Leave it empty to generate a random value. Use the same value if you wish to get the same image. Modify the remaining parameters to get variants of the image

    Sets a seed for the random number generator, allowing you to reproduce the same image generation. If left empty, a random seed will be used.

`output_img_type`: str: Optional, Defaults to pil. Supported: pil only. 

    Specifies the format of the output image.

`timeout`: float: Optional,Override the client-level default timeout for this request, in seconds

    Overrides the default client timeout for this request, setting the maximum time (in seconds) the request should wait before timing out.

### Response Parameter List:

`created`: int

`data`: List[Dict[str, str]]

`error`: Optional[str] = None

---

# Image to Text Generation

Examples:

---
- **Idefics Model**: [Idefics.py](./examples/models/Idefics.py) - This script contains the implementation of the Idefics model.


#### Methods:

---

:arrow_right: <code title="post /v1/multimodal/generations/idefics">client.multimodal.generations.<a href="./src/krutrim_cloud/resources/multimodal/generations.py">idefics</a>(\*\*<a href="src/krutrim_cloud/types/multimodal/generation_idefics_params.py">params</a>) -> <a href="./src/krutrim_cloud/types/multimodal/idefics_response.py">IdeficsResponse</a></code>

```python
from krutrim_cloud.types.multimodal import IdeficsResponse
```


### Request Parameter List:

`model_name`: str: "idefics" # DO NOT CHANGE THIS VALUE

`prompts`:  list: Example
```
[
    "<image>  ", # normal string "<image>"
    "what is the city??",  # Add the prompt/question to be sent to the model related to the image here
    "<image>  ", # normal string "<image>"
    "what is the name of this bridge??"  # Add the prompt/question to be sent to the model related to the image here
]
```
`images`: list: Example
```
[
    [<base64 encoded image bytes of image 1>], # base64 encoded image byte data of image 1
    [], # This value is empty since there is no image reference at this index in the prompts list
    [<base64 encoded image bytes of image 2>], # base64 encoded image byte data of image 2
    [] # This value is empty since there is no image reference at this index in the prompts list
]
```
`max_tokens`: int: 50 - Max tokens can be generated [8 - 1024]

### Response Parameter List:

`generated_texts`: List[str]

---

# Audio Transcriptions

Examples:

---
- **Whisper Model**: [WhisperLargeV3.py](./examples/models/WhisperLargeV3.py)  [WhisperLargeV3_with_audio_manipulation.py](./examples/models/WhisperLargeV3.py) - This script contains the implementation of the Whisper model.


#### Methods:

---

:arrow_right: <code title="post /v1/audio/transcriptions">client.audio.transcriptions.<a href="./src/krutrim_cloud/resources/audio/transcriptions.py">create</a>(\*\*<a href="src/krutrim_cloud/types/audio/transcription_create_params.py">params</a>) -> <a href="./src/krutrim_cloud/types/shared/whisper_response.py">WhisperResponse</a></code>

```python
from krutrim_cloud.types import WhisperResponse
```

### Request Parameter List:

`file`: str | Path | AudioSegment: "your base64 encoded audio byte data here" OR "Path object of pathlib for the audio filepath" OR "PyDub AudioSegment object of Audio/Video"

    Specifies the audio file or audio data to be processed.

`model_name`: str : "openai/whisper-large-v3", # DO NOT CHANGE THIS

    Specifies the model to be used for transcription. This parameter is fixed and should not be changed.

`task`: str : "transcribe", # DO NOT CHANGE THIS

    Defines the task to be performed on the audio. This parameter is fixed and should not be changed.

`language`: str : "hindi", # Source language of the audio

    Specifies the source language of the audio. This helps the model understand which language to expect in the audio for better transcription accuracy.

`temperature`:  float : 0.0, # Optional, defaults to 0.0. Range - 0.0 to 2.0

    Controls the randomness of the transcription output. A lower value makes the output more deterministic, while a higher value introduces more randomness.

`response_format`: str : "json", # Optional, defaults to json. Values - verbose_json (or) json

    Specifies the format of the response from the transcription service.

`chunk_type`: str : "word" # Optional, defaults to sentence. Values - sentence (or) word
    Defines how the transcription output should be segmented. This parameter controls whether the transcription results are segmented by sentences or words.

### Response Parameter List:

`predictions`: Dict[str, Any]

---

# Audio Translations
Examples:

---
- **Whisper Model**: [WhisperLargeV3.py](./examples/models/WhisperLargeV3.py)  [WhisperLargeV3_with_audio_manipulation.py](./examples/models/WhisperLargeV3.py) - This script contains the implementation of the Whisper model.

#### Methods:

---

:arrow_right: <code title="post /v1/audio/translations">client.audio.translations.<a href="./src/krutrim_cloud/resources/audio/translations.py">create</a>(\*\*<a href="src/krutrim_cloud/types/audio/translation_create_params.py">params</a>) -> <a href="./src/krutrim_cloud/types/shared/whisper_response.py">WhisperResponse</a></code>

```python
from krutrim_cloud.types import WhisperResponse
```

### Request Parameter List:

`file`: str | Path | AudioSegment: "your base64 encoded audio byte data here" OR "Path object of pathlib for the audio filepath" OR "PyDub AudioSegment object of Audio/Video"

    Specifies the audio file or audio data to be processed for translation.

`model_name`: str: "openai/whisper-large-v3", # DO NOT CHANGE THIS

    Indicates the specific model to be used for translation. This parameter is fixed and should not be changed.

`task`: str: "translate" # DO NOT CHANGE THIS

    Defines the task to be performed on the audio file. In this case, it specifies that the task is translation.

`temperature`: float : 0.0, # Optional, defaults to 0.0. Range - 0.0 to 2.0
    Controls the creativity and randomness of the translation output. A lower value makes the translation more predictable and consistent, while a higher value allows for more variation.


### Response Parameter List:

`predictions`: Dict[str, Any]

---

# Text-to-Text Chat Completions
Examples:

---
- **Chat Completions Model**: [TextModels_ChatCompletion.py](./examples/models/TextModels_ChatCompletion.py) - This script contains the implementation of the Chat Completion model.

#### Methods:

---

:arrow_right: <code title="post /v1/chat/completions">client.chat.completions.<a href="./src/demo_project/resources/chat/completions.py">create</a>(\*\*<a href="src/demo_project/types/chat/completion_create_params.py">params</a>) -> <a href="./src/demo_project/types/chat/completion_create_response.py">CompletionCreateResponse</a></code>

```python
from krutrim_cloud.types.chat import CompletionCreateResponse
```


### Request Parameter List:

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

    Controls how much to penalize the model for generating tokens that have appeared frequently in the context. This helps reduce repetition in the generated text.

`logit_bias`: dict: {2435: -100, 640: -100}

    A dictionary to apply biases to specific token probabilities. The keys are token IDs and the values are the bias scores. Positive values increase the likelihood of the token being generated, while negative values decrease it.

`logprobs`: bool: true, # Optional, Defaults to false

    Indicates whether to return the log probabilities of the tokens generated. This is useful for understanding the model’s confidence in its predictions.

`top_logprobs`: int: 2, # Optional. Range: 0 to 50

    Specifies the number of top log probabilities to return for each token in the generated text. Helps in analyzing the distribution of token choices.

`max_tokens`: int: 256, # Optional

    Sets the maximum number of tokens to generate in the response. Controls the length of the output.

`n`: int: 1, # Optional, Defaults to 1

    Specifies the number of completions to generate for the given prompt. Useful for generating multiple variations.

`presence_penalty`: float: 0, # Optional, Defaults to 0. Range: -2.0 to 2.0

    Controls how much to penalize new tokens based on whether they appear in the text already. This helps reduce the likelihood of generating tokens that are already present in the context.

`response_format`: dict: { "type": "text" }, # Optional, Defaults to text

    Specifies the format of the response. Defines the type of output that will be returned by the API.

`stop`: str: null, # Optional, Defaults to null. Can take up to 4 sequences where the API will stop generating further tokens.

    Defines sequences where the model should stop generating further tokens. Can be used to control where the output should end.

`stream`: bool: false, # Optional, Defaults to false

    Indicates whether to stream the response as it is generated. Useful for real-time applications where you want to process the output incrementally.

`temperature`: float: 0, # Optional, Defaults to 1. Range: 0 to 2

    Controls the creativity of the output. A higher temperature makes the output more random, while a lower temperature makes it more deterministic.

`top_p`: float: 1 # Optional, Defaults to 1. We generally recommend altering this or temperature but not both.

    Also known as nucleus sampling, this parameter sets a cumulative probability threshold. Tokens are chosen from the smallest possible set whose cumulative probability exceeds top_p

### Response Parameter List:

`id`: str

`choices`: List[Choice]

        Choice:
        
        `finish_reason`: Optional[str] = None

        `index`: Optional[int] = None

        `message`: Optional[ChoiceMessage] = None
            
            ChoiceMessage:

            `content`: str

            `role`: str

`created`: int

`model`: str

`object`: str

---
# Bring Your Own Model

## Upload model to Krutrim S3 Storage

Examples:

---
- **Upload your model to S3 Storage**: [upload_model_to_model_registry_s3.py](examples/model-registry/upload_model_to_model_registry_s3.py) - This script contains the example of uploading model to S3 Storage.

#### Methods:

---

:arrow_right: Upload your model to Krutrim S3 Storage

<code title="post /api/v1/deploy/tasks">client.registry.model_registry.upload_files_to_s3</a>(\*\*params</a>) -> None </code>

### Request Parameter List:

`local_dir_path`: str: The local directory path containing the files to be uploaded to the S3 bucket. It must point to a valid directory containing model files.

`bucket_name`: str: The name of the S3 bucket where the files will be uploaded.

`model_id` : str : A unique identifier for the model being uploaded. This ID is used to organize the uploaded files in the S3 bucket and to register the model in the system.

`version` :str: The version of the model being uploaded. This helps manage multiple versions of the same model and allows for versioning in the model registry.

`base_model` :Optional[str], default = ""): An optional parameter specifying the base model on which the current model is built. This field can be left empty if the model is standalone and does not derive from any other model.

---

## Deploy Tasks for Bring Your Own Model

Examples:

---
- **Deploy Your Model from S3 Storage**: [byom_deploy.py](./examples/deploy/byom_deploy.py) - This script contains the example of deploying model from S3.

#### Methods:

---

:arrow_right: Deploy your own model from S3 storage path

<code title="post /api/v1/deploy/tasks">client.deploy.tasks.<a href="./src/krutrim_cloud/resources/deploy/tasks.py">create</a>(\*\*<a href="src/krutrim_cloud/types/deploy/task_create_params.py">params</a>) -> <a href="./src/krutrim_cloud/types/deploy/task_create_response.py">TaskCreateResponse</a></code>


```python
from krutrim_cloud.types.deploy import TaskCreateResponse
```

### Request Parameter List:
`model`: str : Model name.

`path`: str : S3's model directory path.

`s3_access_key`: str : S3 access key

`s3_endpoint`: str : S3 endpoint

`s3_region`: str : S3 region

`s3_secret`: str : S3 secret

`argument`: Optional[str] : additional argument to parse to inference engine

`environ`: Optional[str] : additional environment variables as "key_1=value1,key_2=value2" to pass to inference engine

`max_batch_size`: Optional[int] : max batch size , default: 256

`max_replicas`: Optional[int] : Max number of replicas, default: 1

`min_replicas`: Optional[int] : Min number of replicas, default: 1

### Response Parameter List:

`id`: str : Deployment Task ID

`name`: str : Model Deployment Name

---

:arrow_right: List deployment task based on provided deploy id

<code title="get /api/v1/deploy/tasks/{id}">client.deploy.tasks.<a href="./src/krutrim_cloud/resources/deploy/tasks.py">retrieve</a>(id) -> <a href="./src/krutrim_cloud/types/deploy/task_retrieve_response.py">TaskRetrieveResponse</a></code>

```python
from krutrim_cloud.types.deploy import TaskRetrieveResponse
```

### Request Parameter List:

`id`: str : Deployment Task ID

### Response Parameter List:
`id`: Optional[str] : Task ID

`checkpoint`: Optional[str] : Checkpoints

`inference_svc_name`: Optional[str] : Inference service name

`name`: Optional[str] : Task name

`namespace`: Optional[str] : Task namespace

`priority`: Optional[int] : Task priority

`status`: Optional[str] : Task status

---

:arrow_right: List all the deployment tasks

<code title="get /api/v1/deploy/tasks">client.deploy.tasks.<a href="./src/krutrim_cloud/resources/deploy/tasks.py">list</a>(\*\*<a href="src/krutrim_cloud/types/deploy/task_list_params.py">params</a>) -> <a href="./src/krutrim_cloud/types/deploy/task_list_response.py">TaskListResponse</a></code>

```python
from krutrim_cloud.types.deploy import TaskListResponse
```

### Request Parameter List:

`limit`: int : Limit the max number of item to be return.

`offset`: int : Offset index.

### Response Parameter List:

`count`: Optional[int] = None

`offset`: Optional[int] : List start offset

`task_list`: Optional[List[object]] : Task List

---

:arrow_right: Cancel/Undeploy the deployed task

<code title="get /api/v1/deploy/tasks/{id}/cancel">client.deploy.tasks.<a href="./src/krutrim_cloud/resources/deploy/tasks.py">cancel</a>(id) -> None</code>

### Request Parameter List:

`id`: str : Deployment Task ID

---
