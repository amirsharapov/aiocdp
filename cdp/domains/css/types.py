from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

CSSRuleType = Literal[
    "MediaRule",
    "SupportsRule",
    "ContainerRule",
    "LayerRule",
    "ScopeRule",
    "StyleRule"
]

StyleSheetOrigin = Literal[
    "injected",
    "user-agent",
    "inspector",
    "regular"
]


@dataclass
class CSSComputedStyleProperty:
    name: str
    value: str


@dataclass
class CSSContainerQuery:
    text: str
    range: SourceRange
    styleSheetId: StyleSheetId
    name: str
    physicalAxes: PhysicalAxes
    logicalAxes: LogicalAxes


@dataclass
class CSSKeyframeRule:
    styleSheetId: StyleSheetId
    origin: StyleSheetOrigin
    keyText: Value
    style: CSSStyle


@dataclass
class CSSKeyframesRule:
    animationName: Value
    keyframes: list


@dataclass
class CSSLayer:
    text: str
    range: SourceRange
    styleSheetId: StyleSheetId


@dataclass
class CSSLayerData:
    name: str
    subLayers: list
    order: float


@dataclass
class CSSMedia:
    text: str
    source: str
    sourceURL: str
    range: SourceRange
    styleSheetId: StyleSheetId
    mediaList: list


@dataclass
class CSSPositionFallbackRule:
    name: Value
    tryRules: list


@dataclass
class CSSProperty:
    name: str
    value: str
    important: bool
    implicit: bool
    text: str
    parsedOk: bool
    disabled: bool
    range: SourceRange
    longhandProperties: list


@dataclass
class CSSPropertyRegistration:
    propertyName: str
    initialValue: Value
    inherits: bool
    syntax: str


@dataclass
class CSSPropertyRule:
    styleSheetId: StyleSheetId
    origin: StyleSheetOrigin
    propertyName: Value
    style: CSSStyle


@dataclass
class CSSRule:
    styleSheetId: StyleSheetId
    selectorList: SelectorList
    nestingSelectors: list
    origin: StyleSheetOrigin
    style: CSSStyle
    media: list
    containerQueries: list
    supports: list
    layers: list
    scopes: list
    ruleTypes: list


@dataclass
class CSSScope:
    text: str
    range: SourceRange
    styleSheetId: StyleSheetId


@dataclass
class CSSStyle:
    styleSheetId: StyleSheetId
    cssProperties: list
    shorthandEntries: list
    cssText: str
    range: SourceRange


@dataclass
class CSSStyleSheetHeader:
    styleSheetId: StyleSheetId
    frameId: FrameId
    sourceURL: str
    sourceMapURL: str
    origin: StyleSheetOrigin
    title: str
    ownerNode: BackendNodeId
    disabled: bool
    hasSourceURL: bool
    isInline: bool
    isMutable: bool
    isConstructed: bool
    startLine: float
    startColumn: float
    length: float
    endLine: float
    endColumn: float
    loadingFailed: bool


@dataclass
class CSSSupports:
    text: str
    active: bool
    range: SourceRange
    styleSheetId: StyleSheetId


@dataclass
class CSSTryRule:
    styleSheetId: StyleSheetId
    origin: StyleSheetOrigin
    style: CSSStyle


@dataclass
class FontFace:
    fontFamily: str
    fontStyle: str
    fontVariant: str
    fontWeight: str
    fontStretch: str
    fontDisplay: str
    unicodeRange: str
    src: str
    platformFontFamily: str
    fontVariationAxes: list


@dataclass
class FontVariationAxis:
    tag: str
    name: str
    minValue: float
    maxValue: float
    defaultValue: float


@dataclass
class InheritedPseudoElementMatches:
    pseudoElements: list


@dataclass
class InheritedStyleEntry:
    inlineStyle: CSSStyle
    matchedCSSRules: list


@dataclass
class MediaQuery:
    expressions: list
    active: bool


@dataclass
class MediaQueryExpression:
    value: float
    unit: str
    feature: str
    valueRange: SourceRange
    computedLength: float


@dataclass
class PlatformFontUsage:
    familyName: str
    isCustomFont: bool
    glyphCount: float


@dataclass
class PseudoElementMatches:
    pseudoType: PseudoType
    pseudoIdentifier: str
    matches: list


@dataclass
class RuleMatch:
    rule: CSSRule
    matchingSelectors: list


@dataclass
class RuleUsage:
    styleSheetId: StyleSheetId
    startOffset: float
    endOffset: float
    used: bool


@dataclass
class SelectorList:
    selectors: list
    text: str


@dataclass
class ShorthandEntry:
    name: str
    value: str
    important: bool


@dataclass
class SourceRange:
    startLine: int
    startColumn: int
    endLine: int
    endColumn: int


@dataclass
class Specificity:
    a: int
    b: int
    c: int


@dataclass
class StyleDeclarationEdit:
    styleSheetId: StyleSheetId
    range: SourceRange
    text: str


@dataclass
class Value:
    text: str
    range: SourceRange
    specificity: Specificity
