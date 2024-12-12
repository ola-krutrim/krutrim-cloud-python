from __future__ import annotations
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

# Import all related classes for different APIs
from .transcribe import (
    TranscribeResource,
    AsyncTranscribeResource,
    TranscribeResourceWithRawResponse,
    AsyncTranscribeResourceWithRawResponse,
    TranscribeResourceWithStreamingResponse,
    AsyncTranscribeResourceWithStreamingResponse,
)

from .tts import (
    TtsResource,
    AsyncTtsResource,
    TtsResourceWithRawResponse,
    AsyncTtsResourceWithRawResponse,
    TtsResourceWithStreamingResponse,
    AsyncTtsResourceWithStreamingResponse,
)

from .tts_trans import (
    TtsTransResource,
    AsyncTtsTransResource,
    TtsTransResourceWithRawResponse,
    AsyncTtsTransResourceWithRawResponse,
    TtsTransResourceWithStreamingResponse,
    AsyncTtsTransResourceWithStreamingResponse,
)

from .stt_trans import (
    SttTransResource,
    AsyncSttTransResource,
    SttTransResourceWithRawResponse,
    AsyncSttTransResourceWithRawResponse,
    SttTransResourceWithStreamingResponse,
    AsyncSttTransResourceWithStreamingResponse,
)

from .sts_trans import (
    StsTransResource,
    AsyncStsTransResource,
    StsTransResourceWithRawResponse,
    AsyncStsTransResourceWithRawResponse,
    StsTransResourceWithStreamingResponse,
    AsyncStsTransResourceWithStreamingResponse,
)

from .transcribe_lf import (
    TranscribeLfResource,
    AsyncTranscribeLfResource,
    TranscribeLfResourceWithRawResponse,
    AsyncTranscribeLfResourceWithRawResponse,
    TranscribeLfResourceWithStreamingResponse,
    AsyncTranscribeLfResourceWithStreamingResponse,
)

from .stt_trans_lf import (
    SttTransLfResource,
    AsyncSttTransLfResource,
    SttTransLfResourceWithRawResponse,
    AsyncSttTransLfResourceWithRawResponse,
    SttTransLfResourceWithStreamingResponse,
    AsyncSttTransLfResourceWithStreamingResponse,
)

from .language_detection import (
    LanguageDetectionResource,
    AsyncLanguageDetectionResource,
    LanguageDetectionResourceWithRawResponse,
    AsyncLanguageDetectionResourceWithRawResponse,
    LanguageDetectionResourceWithStreamingResponse,
    AsyncLanguageDetectionResourceWithStreamingResponse,
)

from .entity_extraction import (
    EntityExtractionResource,
    AsyncEntityExtractionResource,
    EntityExtractionResourceWithRawResponse,
    AsyncEntityExtractionResourceWithRawResponse,
    EntityExtractionResourceWithStreamingResponse,
    AsyncEntityExtractionResourceWithStreamingResponse,
)

from .summarization import (
    SummarizationResource,
    AsyncSummarizationResource,
    SummarizationResourceWithRawResponse,
    AsyncSummarizationResourceWithRawResponse,
    SummarizationResourceWithStreamingResponse,
    AsyncSummarizationResourceWithStreamingResponse,
)

from .translation import (
    TranslationResource,
    AsyncTranslationResource,
    TranslationResourceWithRawResponse,
    AsyncTranslationResourceWithRawResponse,
    TranslationResourceWithStreamingResponse,
    AsyncTranslationResourceWithStreamingResponse,
)

from .sentiment_analysis import (
    SentimentAnalysisResource,
    AsyncSentimentAnalysisResource,
    SentimentAnalysisResourceWithRawResponse,
    AsyncSentimentAnalysisResourceWithRawResponse,
    SentimentAnalysisResourceWithStreamingResponse,
    AsyncSentimentAnalysisResourceWithStreamingResponse,
)

from .job_status import (
   JobStatusResource,
   AsyncJobStatusResource,
   JobStatusResourceWithRawResponse,
   AsyncJobStatusResourceWithRawResponse,
   JobStatusResourceWithStreamingResponse,
   AsyncJobStatusResourceWithStreamingResponse,
)

__all__ = [
    "LanguageLabsResource",
    "AsyncLanguageLabsResource"
]

# Synchronous Resources for Language Labs

class LanguageLabsResource(SyncAPIResource):
    @cached_property
    def transcribe(self) -> TranscribeResource:
        return TranscribeResource(self._client)

    @cached_property
    def tts(self) -> TtsResource:
        return TtsResource(self._client)

    @cached_property
    def tts_trans(self) -> TtsTransResource:
        return TtsTransResource(self._client)

    @cached_property
    def language_detection(self) -> LanguageDetectionResource:
        return LanguageDetectionResource(self._client)

    @cached_property
    def entity_extraction(self) -> EntityExtractionResource:
        return EntityExtractionResource(self._client)

    @cached_property
    def summarization(self) -> SummarizationResource:
        return SummarizationResource(self._client)

    @cached_property
    def translation(self) -> TranslationResource:
        return TranslationResource(self._client)

    @cached_property
    def sentiment_analysis(self) -> SentimentAnalysisResource:
        return SentimentAnalysisResource(self._client)

    @cached_property
    def stt_trans(self) -> SttTransResource:
        return SttTransResource(self._client)

    @cached_property
    def sts_trans(self) -> StsTransResource:
        return StsTransResource(self._client)

    @cached_property
    def transcribe_lf(self) -> TranscribeLfResource:
        return TranscribeLfResource(self._client)

    @cached_property
    def stt_trans_lf(self) -> SttTransLfResource:
        return SttTransLfResource(self._client)

    @cached_property
    def job_status(self) -> JobStatusResource:
        return JobStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> LanguageLabsResourceWithRawResponse:
        return LanguageLabsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LanguageLabsResourceWithStreamingResponse:
        return LanguageLabsResourceWithStreamingResponse(self)

# Asynchronous Resources for Language Labs

class AsyncLanguageLabsResource(AsyncAPIResource):
    @cached_property
    def transcribe(self) -> AsyncTranscribeResource:
        return AsyncTranscribeResource(self._client)

    @cached_property
    def tts(self) -> AsyncTtsResource:
        return AsyncTtsResource(self._client)

    @cached_property
    def tts_trans(self) -> AsyncTtsTransResource:
        return AsyncTtsTransResource(self._client)

    @cached_property
    def language_detection(self) -> AsyncLanguageDetectionResource:
        return AsyncLanguageDetectionResource(self._client)

    @cached_property
    def entity_extraction(self) -> AsyncEntityExtractionResource:
        return AsyncEntityExtractionResource(self._client)

    @cached_property
    def summarization(self) -> AsyncSummarizationResource:
        return AsyncSummarizationResource(self._client)

    @cached_property
    def translation(self) -> AsyncTranslationResource:
        return AsyncTranslationResource(self._client)

    @cached_property
    def sentiment_analysis(self) -> AsyncSentimentAnalysisResource:
        return AsyncSentimentAnalysisResource(self._client)

    @cached_property
    def stt_trans(self) -> AsyncSttTransResource:
        return AsyncSttTransResource(self._client)

    @cached_property
    def sts_trans(self) -> AsyncStsTransResource:
        return AsyncStsTransResource(self._client)

    @cached_property
    def transcribe_lf(self) -> AsyncTranscribeLfResource:
        return AsyncTranscribeLfResource(self._client)

    @cached_property
    def stt_trans_lf(self) -> AsyncSttTransLfResource:
        return AsyncSttTransLfResource(self._client)

    @cached_property
    def job_status(self) -> AsyncJobStatusResource:
        return AsyncJobStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLanguageLabsResourceWithRawResponse:
        return AsyncLanguageLabsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLanguageLabsResourceWithStreamingResponse:
        return AsyncLanguageLabsResourceWithStreamingResponse(self)


# Sync Resource Classes with Raw and Streaming Responses
class LanguageLabsResourceWithRawResponse:
    def __init__(self, languagelabs: LanguageLabsResource) -> None:
        self._languagelabs = languagelabs

    @cached_property
    def transcribe(self) -> TranscribeResourceWithRawResponse:
        return TranscribeResourceWithRawResponse(self._languagelabs.transcribe)

    @cached_property
    def tts(self) -> TtsResourceWithRawResponse:
        return TtsResourceWithRawResponse(self._languagelabs.tts)

    @cached_property
    def tts_trans(self) -> TtsTransResourceWithRawResponse:
        return TtsTransResourceWithRawResponse(self._languagelabs.tts_trans)

    @cached_property
    def language_detection(self) -> LanguageDetectionResourceWithRawResponse:
        return LanguageDetectionResourceWithRawResponse(self._languagelabs.language_detection)

    @cached_property
    def entity_extraction(self) -> EntityExtractionResourceWithRawResponse:
        return EntityExtractionResourceWithRawResponse(self._languagelabs.entity_extraction)

    @cached_property
    def summarization(self) -> SummarizationResourceWithRawResponse:
        return SummarizationResourceWithRawResponse(self._languagelabs.summarization)

    @cached_property
    def translation(self) -> TranslationResourceWithRawResponse:
        return TranslationResourceWithRawResponse(self._languagelabs.translation)

    @cached_property
    def sentiment_analysis(self) -> SentimentAnalysisResourceWithRawResponse:
        return SentimentAnalysisResourceWithRawResponse(self._languagelabs.sentiment_analysis)

    @cached_property
    def stt_trans(self) -> SttTransResourceWithRawResponse:
        return SttTransResourceWithRawResponse(self._languagelabs.stt_trans)

    @cached_property
    def sts_trans(self) -> StsTransResourceWithRawResponse:
        return StsTransResourceWithRawResponse(self._languagelabs.sts_trans)

    @cached_property
    def transcribe_lf(self) -> TranscribeLfResourceWithRawResponse:
        return TranscribeLfResourceWithRawResponse(self._languagelabs.transcribe_lf)

    @cached_property
    def stt_trans_lf(self) -> SttTransLfResourceWithRawResponse:
        return SttTransLfResourceWithRawResponse(self._languagelabs.stt_trans_lf)

    @cached_property
    def job_status(self) -> JobStatusResourceWithRawResponse:
        return JobStatusResourceWithRawResponse(self._languagelabs.job_status)


class AsyncLanguageLabsResourceWithRawResponse:
    def __init__(self, languagelabs: AsyncLanguageLabsResource) -> None:
        self._languagelabs = languagelabs

    @cached_property
    def transcribe(self) -> AsyncTranscribeResourceWithRawResponse:
        return AsyncTranscribeResourceWithRawResponse(self._languagelabs.transcribe)

    @cached_property
    def tts(self) -> AsyncTtsResourceWithRawResponse:
        return AsyncTtsResourceWithRawResponse(self._languagelabs.tts)

    @cached_property
    def tts_trans(self) -> AsyncTtsTransResourceWithRawResponse:
        return AsyncTtsTransResourceWithRawResponse(self._languagelabs.tts_trans)

    @cached_property
    def language_detection(self) -> AsyncLanguageDetectionResourceWithRawResponse:
        return AsyncLanguageDetectionResourceWithRawResponse(self._languagelabs.language_detection)

    @cached_property
    def entity_extraction(self) -> AsyncEntityExtractionResourceWithRawResponse:
        return AsyncEntityExtractionResourceWithRawResponse(self._languagelabs.entity_extraction)

    @cached_property
    def summarization(self) -> AsyncSummarizationResourceWithRawResponse:
        return AsyncSummarizationResourceWithRawResponse(self._languagelabs.summarization)

    @cached_property
    def translation(self) -> AsyncTranslationResourceWithRawResponse:
        return AsyncTranslationResourceWithRawResponse(self._languagelabs.translation)

    @cached_property
    def sentiment_analysis(self) -> AsyncSentimentAnalysisResourceWithRawResponse:
        return AsyncSentimentAnalysisResourceWithRawResponse(self._languagelabs.sentiment_analysis)

    @cached_property
    def stt_trans(self) -> AsyncSttTransResourceWithRawResponse:
        return AsyncSttTransResourceWithRawResponse(self._languagelabs.stt_trans)

    @cached_property
    def sts_trans(self) -> AsyncStsTransResourceWithRawResponse:
        return AsyncStsTransResourceWithRawResponse(self._languagelabs.sts_trans)

    @cached_property
    def transcribe_lf(self) -> AsyncTranscribeLfResourceWithRawResponse:
        return AsyncTranscribeLfResourceWithRawResponse(self._languagelabs.transcribe_lf)

    @cached_property
    def stt_trans_lf(self) -> AsyncSttTransLfResourceWithRawResponse:
        return AsyncSttTransLfResourceWithRawResponse(self._languagelabs.stt_trans_lf)

    @cached_property
    def job_status(self) -> AsyncJobStatusResourceWithRawResponse:
        return AsyncJobStatusResourceWithRawResponse(self._languagelabs.job_status)


# Sync Resource Classes with Streaming Responses
class LanguageLabsResourceWithStreamingResponse:
    def __init__(self, languagelabs: LanguageLabsResource) -> None:
        self._languagelabs = languagelabs

    @cached_property
    def transcribe(self) -> TranscribeResourceWithStreamingResponse:
        return TranscribeResourceWithStreamingResponse(self._languagelabs.transcribe)

    @cached_property
    def tts(self) -> TtsResourceWithStreamingResponse:
        return TtsResourceWithStreamingResponse(self._languagelabs.tts)

    @cached_property
    def tts_trans(self) -> TtsTransResourceWithStreamingResponse:
        return TtsTransResourceWithStreamingResponse(self._languagelabs.tts_trans)

    @cached_property
    def language_detection(self) -> LanguageDetectionResourceWithStreamingResponse:
        return LanguageDetectionResourceWithStreamingResponse(self._languagelabs.language_detection)

    @cached_property
    def entity_extraction(self) -> EntityExtractionResourceWithStreamingResponse:
        return EntityExtractionResourceWithStreamingResponse(self._languagelabs.entity_extraction)

    def summarization(self) -> SummarizationResourceWithStreamingResponse:
        return SummarizationResourceWithStreamingResponse(self._languagelabs.summarization)

    @cached_property
    def translation(self) -> TranslationResourceWithStreamingResponse:
        return TranslationResourceWithStreamingResponse(self._languagelabs.translation)

    @cached_property
    def sentiment_analysis(self) -> SentimentAnalysisResourceWithStreamingResponse:
        return SentimentAnalysisResourceWithStreamingResponse(self._languagelabs.sentiment_analysis)

    @cached_property
    def stt_trans(self) -> SttTransResourceWithStreamingResponse:
        return SttTransResourceWithStreamingResponse(self._languagelabs.stt_trans)

    @cached_property
    def job_status(self) -> JobStatusResourceWithStreamingResponse:
        return JobStatusResourceWithStreamingResponse(self._languagelabs.job_status)

    @cached_property
    def sts_trans(self) -> StsTransResourceWithStreamingResponse:
        return StsTransResourceWithStreamingResponse(self._languagelabs.sts_trans)

    @cached_property
    def transcribe_lf(self) -> TranscribeLfResourceWithStreamingResponse:
        return TranscribeLfResourceWithStreamingResponse(self._languagelabs.transcribe_lf)

    @cached_property
    def stt_trans_lf(self) -> SttTransLfResourceWithStreamingResponse:
        return SttTransLfResourceWithStreamingResponse(self._languagelabs.stt_trans_lf)


class AsyncLanguageLabsResourceWithStreamingResponse:
    def __init__(self, languagelabs: AsyncLanguageLabsResource) -> None:
        self._languagelabs = languagelabs

    @cached_property
    def transcribe(self) -> AsyncTranscribeResourceWithStreamingResponse:
        return AsyncTranscribeResourceWithStreamingResponse(self._languagelabs.transcribe)

    @cached_property
    def tts(self) -> AsyncTtsResourceWithStreamingResponse:
        return AsyncTtsResourceWithStreamingResponse(self._languagelabs.tts)

    @cached_property
    def tts_trans(self) -> AsyncTtsTransResourceWithStreamingResponse:
        return AsyncTtsTransResourceWithStreamingResponse(self._languagelabs.tts_trans)

    @cached_property
    def language_detection(self) -> AsyncLanguageDetectionResourceWithStreamingResponse:
        return AsyncLanguageDetectionResourceWithStreamingResponse(self._languagelabs.language_detection)

    @cached_property
    def entity_extraction(self) -> AsyncEntityExtractionResourceWithStreamingResponse:
        return AsyncEntityExtractionResourceWithStreamingResponse(self._languagelabs.entity_extraction)

    @cached_property
    def summarization(self) -> AsyncSummarizationResourceWithStreamingResponse:
        return AsyncSummarizationResourceWithStreamingResponse(self._languagelabs.summarization)

    @cached_property
    def translation(self) -> AsyncTranslationResourceWithStreamingResponse:
        return AsyncTranslationResourceWithStreamingResponse(self._languagelabs.translation)

    @cached_property
    def sentiment_analysis(self) -> AsyncSentimentAnalysisResourceWithStreamingResponse:
        return AsyncSentimentAnalysisResourceWithStreamingResponse(self._languagelabs.sentiment_analysis)

    @cached_property
    def stt_trans(self) -> AsyncSttTransResourceWithStreamingResponse:
        return AsyncSttTransResourceWithStreamingResponse(self._languagelabs.stt_trans)

    @cached_property
    def sts_trans(self) -> AsyncStsTransResourceWithStreamingResponse:
        return AsyncStsTransResourceWithStreamingResponse(self._languagelabs.sts_trans)

    @cached_property
    def transcribe_lf(self) -> AsyncTranscribeLfResourceWithStreamingResponse:
        return AsyncTranscribeLfResourceWithStreamingResponse(self._languagelabs.transcribe_lf)

    @cached_property
    def stt_trans_lf(self) -> AsyncSttTransLfResourceWithStreamingResponse:
        return AsyncSttTransLfResourceWithStreamingResponse(self._languagelabs.stt_trans_lf)

    @cached_property
    def job_status(self) -> AsyncJobStatusResourceWithStreamingResponse:
        return AsyncJobStatusResourceWithStreamingResponse(self._languagelabs.job_status)