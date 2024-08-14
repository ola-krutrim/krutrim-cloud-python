import base64
from PIL import Image
import io
import os
from datetime import datetime
from krutrim_cloud._exceptions import TimeRetrievalError


def convert_base64_to_PIL_img(base64_data: str) -> Image.Image:
    """
    Convert a base64 encoded string to a PIL Image.

    Args:
        base64_data (str): A base64 encoded string representing image data.

    Returns:
        PIL.Image.Image: A PIL Image object created from the base64 encoded data.

    Raises:
        ValueError: If the base64_data is not a valid base64 string.
        IOError: If the base64 data cannot be decoded into an image.

    Example:
        >>> base64_data = "iVBORw0KGgoAAAANSUhEUgAAAAUA..."
        >>> image = convert_base64_to_PIL_img(base64_data)
        >>> image.show()
    """
    try:
        img_bytes = base64.b64decode(base64_data)
    except (base64.binascii.Error, TypeError) as e:
        raise ValueError("Invalid base64 string") from e

    try:
        image = Image.open(io.BytesIO(img_bytes))
    except (IOError, ValueError) as e:
        raise IOError("Cannot convert base64 data to an image") from e

    return image


def save_PIL_img(PIL_image_obj: Image.Image, output_dirpath: str, filename: str) -> None:
    """
    Save a PIL Image object to the specified directory with the given filename.

    Args:
        PIL_image_obj (PIL.Image.Image): The PIL Image object to be saved.
        output_dirpath (str): The directory path where the image will be saved.
        filename (str): The name of the file to save the image as.

    Returns:
        None

    Raises:
        ValueError: If the PIL_image_obj is not a valid PIL Image object.
        OSError: If the image cannot be saved due to an OS-related error.

    Example:
        >>> from PIL import Image
        >>> image = Image.new('RGB', (100, 100), color = 'red')
        >>> save_PIL_img(image, '/path/to/save', 'image.png')
    """
    if not isinstance(PIL_image_obj, Image.Image):
        raise ValueError("The provided object is not a valid PIL Image object.")

    try:
        os.makedirs(output_dirpath, exist_ok=True)
    except OSError as e:
        raise OSError(f"Failed to create directory '{output_dirpath}': {e}")

    try:
        save_path = os.path.join(output_dirpath, filename)
        PIL_image_obj.save(save_path)
    except OSError as e:
        raise OSError(f"Failed to save the image to '{save_path}': {e}")


def save_text_array_content(text_data_array: list, output_dirpath: str, filename: str) -> None:
    """
    Save the content of a list of text data to a file in the specified directory.

    Args:
        text_data_array (list): A list of strings where each string represents a line of text.
        output_dirpath (str): The directory path where the file will be saved.
        filename (str): The name of the file to save the text data as.

    Returns:
        None

    Raises:
        ValueError: If text_data_array is not a list of strings.
        OSError: If the directory cannot be created or the file cannot be written due to an OS-related error.

    Example:
        >>> text_data = ["Line 1", "Line 2", "Line 3"]
        >>> save_text_array_content(text_data, '/path/to/save', 'output.txt')
    """
    if not isinstance(text_data_array, list) or not all(isinstance(line, str) for line in text_data_array):
        raise ValueError("text_data_array must be a list of strings.")

    try:
        os.makedirs(output_dirpath, exist_ok=True)
    except OSError as e:
        raise OSError(f"Failed to create directory '{output_dirpath}': {e}")

    try:
        file_path = os.path.join(output_dirpath, filename)
        with open(file_path, "w") as file:
            for line in text_data_array:
                file.write(line + "\n")
    except OSError as e:
        raise OSError(f"Failed to write to file '{file_path}': {e}")


def save_text_content(text_data: str, output_dirpath: str, filename: str) -> None:
    """
    Save a string of text data to a file in the specified directory.

    Args:
        text_data (str): The text data to be saved to the file.
        output_dirpath (str): The directory path where the file will be saved.
        filename (str): The name of the file to save the text data as.

    Returns:
        None

    Raises:
        ValueError: If text_data is not a string.
        OSError: If the directory cannot be created or the file cannot be written due to an OS-related error.

    Example:
        >>> text_data = "This is a sample text."
        >>> save_text_content(text_data, '/path/to/save', 'output.txt')
    """
    if not isinstance(text_data, str):
        raise ValueError("text_data must be a string.")

    try:
        os.makedirs(output_dirpath, exist_ok=True)
    except OSError as e:
        raise OSError(f"Failed to create directory '{output_dirpath}': {e}")

    try:
        file_path = os.path.join(output_dirpath, filename)
        with open(file_path, "w") as file:
            file.write(text_data + "\n")
    except OSError as e:
        raise OSError(f"Failed to write to file '{file_path}': {e}")


def convert_PIL_image_to_base64(PIL_image_obj: Image.Image, format: str = "JPEG") -> str:
    """
    Convert a PIL Image object to a base64 encoded string.

    Args:
        PIL_image_obj (PIL.Image.Image): The PIL Image object to be converted.
        format (str): The format to use for encoding the image. Defaults to "JPEG".

    Returns:
        str: The base64 encoded string of the image.

    Raises:
        ValueError: If PIL_image_obj is not a valid PIL Image object.
        OSError: If there is an error during the image saving or encoding process.

    Example:
        >>> from PIL import Image
        >>> image = Image.new('RGB', (100, 100), color = 'red')
        >>> base64_string = convert_PIL_image_to_base64(image, format="PNG")
        >>> print(base64_string)
    """
    if not isinstance(PIL_image_obj, Image.Image):
        raise ValueError("The provided object is not a valid PIL Image object.")

    try:
        # Convert the PIL Image to a BytesIO object
        buffered = io.BytesIO()
        PIL_image_obj.save(buffered, format=format)
    except (OSError, ValueError) as e:
        raise OSError(f"Failed to save the image to a BytesIO object: {e}")

    try:
        # Encode the BytesIO object to base64
        return base64.b64encode(buffered.getvalue()).decode("utf-8")
    except (base64.binascii.Error, TypeError) as e:
        raise OSError(f"Failed to encode the image to base64: {e}")


def convert_audio_file_to_base64(audio_filepath: str) -> str:
    """
    Convert an audio file to a base64 encoded string.

    Args:
        audio_filepath (str): The file path to the audio file to be converted.

    Returns:
        str: The base64 encoded string of the audio file.

    Raises:
        FileNotFoundError: If the audio file does not exist.
        OSError: If there is an error reading the audio file.
        ValueError: If audio_filepath is not a valid string.

    Example:
        >>> base64_string = convert_audio_file_to_base64('/path/to/audio.mp3')
        >>> print(base64_string)
    """
    if not isinstance(audio_filepath, str):
        raise ValueError("audio_filepath must be a valid string.")

    try:
        with open(audio_filepath, "rb") as audio_file:
            audio_data = audio_file.read()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Audio file '{audio_filepath}' not found: {e}")
    except OSError as e:
        raise OSError(f"Error reading the audio file '{audio_filepath}': {e}")

    try:
        # Encode the audio data to base64
        return base64.b64encode(audio_data).decode("utf-8")
    except (base64.binascii.Error, TypeError) as e:
        raise ValueError(f"Failed to encode the audio file to base64: {e}")


def get_current_time_string(format: str = "%Y%m%d_%H%M%S") -> str:
    """
    Retrieve the current time as a string in the specified format.

    Args:
        format (str): The format in which to return the current time string. Defaults to "%Y%m%d_%H%M%S".

    Returns:
        str: The current time formatted as a string.

    Raises:
        TimeRetrievalError: If there's an issue retrieving or formatting the current time.

    Example:
        >>> current_time = get_current_time_string()
        >>> print(current_time)  # Output: 20240801_130501
    """
    try:
        current_time = datetime.now()
        time_string = current_time.strftime(format)
        return time_string
    except Exception as exc:
        raise TimeRetrievalError(f"Failed to retrieve or format the current time: {exc}")
