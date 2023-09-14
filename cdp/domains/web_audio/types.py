from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

AutomationRate = Literal[
    "a-rate",
    "k-rate"
]

ChannelCountMode = Literal[
    "clamped-max",
    "explicit",
    "max"
]

ChannelInterpretation = Literal[
    "discrete",
    "speakers"
]

ContextState = Literal[
    "suspended",
    "running",
    "closed"
]

ContextType = Literal[
    "realtime",
    "offline"
]


@dataclass
class AudioListener:
    listenerId: GraphObjectId
    contextId: GraphObjectId


@dataclass
class AudioNode:
    nodeId: GraphObjectId
    contextId: GraphObjectId
    nodeType: NodeType
    numberOfInputs: float
    numberOfOutputs: float
    channelCount: float
    channelCountMode: ChannelCountMode
    channelInterpretation: ChannelInterpretation


@dataclass
class AudioParam:
    paramId: GraphObjectId
    nodeId: GraphObjectId
    contextId: GraphObjectId
    paramType: ParamType
    rate: AutomationRate
    defaultValue: float
    minValue: float
    maxValue: float


@dataclass
class BaseAudioContext:
    contextId: GraphObjectId
    contextType: ContextType
    contextState: ContextState
    realtimeData: ContextRealtimeData
    callbackBufferSize: float
    maxOutputChannelCount: float
    sampleRate: float


@dataclass
class ContextRealtimeData:
    currentTime: float
    renderCapacity: float
    callbackIntervalMean: float
    callbackIntervalVariance: float
