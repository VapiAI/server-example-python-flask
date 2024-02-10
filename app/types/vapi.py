from typing import Optional, List, Dict, Union, Literal, TypedDict, Any
from enum import Enum

# Assuming ChatCompletionCreateParams and ChatCompletionMessageParam are defined elsewhere
# and have their Python equivalent, they should be imported here.

class FunctionDefinition:
    # Define the structure of FunctionDefinition based on its usage in TypeScript
    pass

class Model(TypedDict, total=False):
    model: str
    systemPrompt: Optional[str]
    temperature: Optional[float]
    functions: List[Dict[str, Union[FunctionDefinition, Any]]]
    provider: str
    url: Optional[str]

PLAY_HT_EMOTIONS = [
    "female_happy",
    "female_sad",
    "female_angry",
    "female_fearful",
    "female_disgust",
    "female_surprised",
]
PlayHTEmotion = Literal[
    "female_happy",
    "female_sad",
    "female_angry",
    "female_fearful",
    "female_disgust",
    "female_surprised",
]

class Voice(TypedDict, total=False):
    provider: str
    voiceId: str
    speed: Optional[float]
    stability: Optional[float]
    similarityBoost: Optional[float]
    style: Optional[float]
    useSpeakerBoost: Optional[bool]
    temperature: Optional[float]
    emotion: Optional[PlayHTEmotion]
    voiceGuidance: Optional[float]
    styleGuidance: Optional[float]
    textGuidance: Optional[float]

class Assistant(TypedDict, total=False):
    name: Optional[str]
    transcriber: Optional[Dict[str, Union[str, List[str]]]]
    model: Optional[Model]
    voice: Optional[Voice]
    language: Optional[str]
    forwardingPhoneNumber: Optional[str]
    firstMessage: Optional[str]
    voicemailMessage: Optional[str]
    endCallMessage: Optional[str]
    endCallPhrases: Optional[List[str]]
    interruptionsEnabled: Optional[bool]
    recordingEnabled: Optional[bool]
    endCallFunctionEnabled: Optional[bool]
    dialKeypadFunctionEnabled: Optional[bool]
    fillersEnabled: Optional[bool]
    clientMessages: Optional[List[Any]]
    serverMessages: Optional[List[Any]]
    silenceTimeoutSeconds: Optional[int]
    responseDelaySeconds: Optional[int]
    liveTranscriptsEnabled: Optional[bool]
    keywords: Optional[List[str]]
    parentId: Optional[str]
    serverUrl: Optional[str]
    serverUrlSecret: Optional[str]
    id: Optional[str]
    orgId: Optional[str]
    createdAt: Optional[Any]  # Replace Any with the appropriate type for dates
    updatedAt: Optional[Any]  # Replace Any with the appropriate type for dates

VAPI_CALL_STATUSES = [
    "queued",
    "ringing",
    "in-progress",
    "forwarding",
    "ended",
]
VapiCallStatus = Literal[
    "queued",
    "ringing",
    "in-progress",
    "forwarding",
    "ended",
]

class VapiWebhookEnum(Enum):
    ASSISTANT_REQUEST = "assistant-request"
    FUNCTION_CALL = "function-call"
    STATUS_UPDATE = "status-update"
    END_OF_CALL_REPORT = "end-of-call-report"
    HANG = "hang"
    SPEECH_UPDATE = "speech-update"
    TRANSCRIPT = "transcript"

class ConversationMessage(TypedDict):
    role: Literal["user", "system", "bot", "function_call", "function_result"]
    message: Optional[str]
    name: Optional[str]
    args: Optional[str]
    result: Optional[str]
    time: int
    endTime: Optional[int]
    secondsFromStart: int

class BaseVapiPayload(TypedDict):
    call: Any  # Replace Any with the appropriate type for VapiCall

class AssistantRequestPayload(BaseVapiPayload):
    type: Literal[VapiWebhookEnum.ASSISTANT_REQUEST]

class StatusUpdatePayload(BaseVapiPayload):
    type: Literal[VapiWebhookEnum.STATUS_UPDATE]
    status: VapiCallStatus
    messages: Optional[List[Any]]  # Replace Any with the appropriate type

class FunctionCallPayload(BaseVapiPayload):
    type: Literal[VapiWebhookEnum.FUNCTION_CALL]
    functionCall: Any  # Replace Any with the appropriate type

class EndOfCallReportPayload(BaseVapiPayload):
    type: Literal[VapiWebhookEnum.END_OF_CALL_REPORT]
    endedReason: str
    transcript: str
    messages: List[ConversationMessage]
    summary: str
    recordingUrl: Optional[str]

class HangPayload(BaseVapiPayload):
    type: Literal[VapiWebhookEnum.HANG]

class SpeechUpdatePayload(BaseVapiPayload):
    type: Literal[VapiWebhookEnum.SPEECH_UPDATE]
    status: Literal["started", "stopped"]
    role: Literal["assistant", "user"]

class TranscriptPayload(TypedDict):
    type: Literal[VapiWebhookEnum.TRANSCRIPT]
    role: Literal["assistant", "user"]
    transcriptType: Literal["partial", "final"]
    transcript: str

class VapiCall(TypedDict):
    # Define the structure of VapiCall based on its usage in TypeScript
    pass

VapiPayload = Union[
    AssistantRequestPayload,
    StatusUpdatePayload,
    FunctionCallPayload,
    EndOfCallReportPayload,
    SpeechUpdatePayload,
    TranscriptPayload,
    HangPayload,
]

class FunctionCallMessageResponse(TypedDict, total=False):
    result: str

class AssistantRequestMessageResponse(TypedDict, total=False):
    assistant: Optional[Assistant]
    error: Optional[str]

class StatusUpdateMessageResponse(TypedDict):
    pass

class SpeechUpdateMessageResponse(TypedDict):
    pass

class TranscriptMessageResponse(TypedDict):
    pass

class HangMessageResponse(TypedDict):
    pass

class EndOfCallReportMessageResponse(TypedDict):
    pass

VapiResponse = Union[
    AssistantRequestMessageResponse,
    FunctionCallMessageResponse,
    EndOfCallReportMessageResponse,
    HangMessageResponse,
    StatusUpdateMessageResponse,
    SpeechUpdateMessageResponse,
    TranscriptMessageResponse,
]