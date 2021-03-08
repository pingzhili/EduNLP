__all__ = ['watex']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
@Js
def PyJs_anonymous_0_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    @Js
    def PyJs_anonymous_1_(module, exports, __webpack_require__, this, arguments, var=var):
        var = Scope({'module':module, 'exports':exports, '__webpack_require__':__webpack_require__, 'this':this, 'arguments':arguments}, var)
        var.registers(['exports', 'module', '__webpack_require__'])
        pass
    PyJs_anonymous_1_._set_name('anonymous')
    @Js
    def PyJs_anonymous_2_(module, __webpack_exports__, __webpack_require__, this, arguments, var=var):
        var = Scope({'module':module, '__webpack_exports__':__webpack_exports__, '__webpack_require__':__webpack_require__, 'this':this, 'arguments':arguments}, var)
        var.registers(['ligatures', 'Token_Token', 'mathchoice_chooseMathStyle', 'textSymbols', 'buildCommon_makeSvgSpan', '_text', 'stretchy_svgSpan', 'textFontFamilies', 'delimiter_makeCustomSizedDelim', 'op', 'punct', 'stylArray', 'textFontShapes', 'buildCommon', 'delimiter_getMetrics', 'buildCommon_mathnormal', 'main', 'symbols_i4', 'src_symbols', 'supsub_htmlBuilderDelegate', 'macros', 'buildHTMLUnbreakable', 'dCellStyle', 'katex_renderToHTMLTree', 'binRightCanceller', 'spaceAfterDots', 'mathitLetters', 'utils_escape', 'sizing_htmlBuilder', 'buildCommon_makeVList', '_sup', 'stretchy_mathMLnode', 'ams', 'tree_DocumentFragment', '_toMarkup', 'iCombinations', 'ESCAPE_REGEX', 'mathMLTree', 'hLinePad', 'katex', 'array_mathmlBuilder', 'op_mathmlBuilder', 'assertParsed', 'src_Style', 'letters', 'binLeftCanceller', '_environments', '_cramp', 'alignMap', 'src_functions', 'Parser_Parser', 'units_calculateSize', 'boldsymbol', 'fontMap', 'symbols_math', 'noSuccessor', 'buildHTML', 'assertSpan', 'buildCommon_makeGlue', 'src_buildTree', 'domTree_Img', 'assertSymbolNodeType', 'sizingGroup', 'defineFunctionBuilders', 'tokenRegexString', 'fontMetricsData', 'delimiter_makeSizedDelim', 'extraCharacterMap', 'setFontMetrics', 'symbols_close', 'thickspace', 'parseArray', 'assertNodeType', 'delimiter_styleWrap', 'Style_styles', 'buildTree_displayWrap', 'buildHTML_checkPartialGroup', 'symbols_i3', 'checkAtomFamily', 'domTree_SymbolNode', 'buildMathML_getVariant', 'font_htmlBuilder', 'wideLatinLetterData', 'SvgNode', '_ch2', 'stackAlwaysDelimiters', 'checkDelimiter', 'centerSpan', 'dotsByToken', 'contains', 'ParseError', 'svgGeometry', 'controlWordRegexString', 'getBaseElem', '_htmlGroupBuilders', 'makeSqrtImage', 'delimiter_makeInner', '_sub', 'getCharacterMetrics', 'stackLargeDelimiters', 'katex_0', 'buildCommon_makeOrd', 'SourceLocation', 'sizeStyleMap', 'buildHTML_buildGroup', 'op_htmlBuilder', 'renderToString', 'bin', 'regularSpace', 'src_ParseError', 'symbols_textord', 'mathord', 'symbols_ch', 'utils', 'symbols_spacing', 'buildCommon_lookupSymbol', 'extraLatin', 'symbols', '_mathmlGroupBuilders', 'makeNullDelimiter', 'accent_htmlBuilder', 'sizeFuncs', 'buildCommon_mathsym', 'DomEnum', 'domTree_PathNode', 'groupLength', 'emPad', 'sizeElementFromChildren', 'buildTree_buildTree', 'src_symbols_i', '_functions', 'defaultVariant', 'wide_character_wideCharacterFont', 'Sc', '_ch', 'accent_mathmlBuilder', 'makeVerb', 'Dc', 'delimTypeToFont', 'buildMathML_makeText', 'wideNumeralData', 'SSc', 'domTree_Anchor', 'buildCommon_makeFragment', 'delimiter_mathrmSize', 'array_htmlBuilder', 'symbols_inner', 'environments', 'utils_isCharacterBox', 'buildCommon_canCombine', 'src_parseTree', 'singleCharIntegrals', 'defineEnvironment', 'delimiter_makeStackedDelim', 'builtinMacros', '__webpack_exports__', 'sigmasAndXis', 'symbols_accent', 'Settings_Settings', 'Tc', 'stackLargeDelimiterSequence', 'horizBrace_htmlBuilder', 'hyphenate', 'color_htmlBuilder', 'singleCharBigOps', 'src_Settings', 'tightSpacings', '_i5', 'validUnit', 'getTypeOfDomTree', 'buildMathML', 'mathTextSymbols', 'buildMathML_makeRow', 'enclose_htmlBuilder', 'horizBrace_mathmlBuilder', 'relativeUnit', 'delimiters', 'defineMacro', 'NON_STRETCHY_ACCENT_REGEX', 'controlWordWhitespaceRegex', 'retrieveTextFontName', 'traverseNonSpaceNodes', 'defineFunction_ordargument', 'genfrac_adjustStyle', 'font_mathmlBuilder', 'NON_ATOMS', 'controlWordWhitespaceRegexString', 'getHLines', 'tag_pad', 'stretchyCodePoint', 'ESCAPE_LOOKUP', 'getOutermostNode', 'latexRaiseA', '_fracNum', 'sizeToMaxHeight', 'functions', 'stackNeverDelimiterSequence', 'styling_styleMap', 'controlSymbolRegexString', 'SpaceNode', 'macros_def', 'S', 'stackNeverDelimiters', 'delimiter', 'buildTree_buildHTMLTree', 'katexImagesData', 'getVListChildrenAndDepth', 'color_mathmlBuilder', 'delimiter_makeLargeDelim', 'buildCommon_wrapFragment', 'scriptFromCodepoint', 'T', 'sizeMultipliers', 'buildCommon_staticSvg', 'mclass_mathmlBuilder', 'cssSpace', 'svgData', 'Style', 'D', 'domTree_Span', 'unicodeAccents', 'svgGeometry_path', 'Options_Options', 'assertAtomFamily', 'newDocumentFragment', 'textFontWeights', 'mclass_htmlBuilder', 'katex_renderError', 'checkNodeType', 'katex_renderToDomTree', 'binrelClass', 'spacings', 'ptPerUnit', 'thinspace', 'scriptData', 'buildCommon_mathdefault', 'src_Options', 'src_environments', 'genfrac_htmlBuilder', 'stackAlwaysDelimiterSequence', 'genfrac_mathmlBuilder', 'stretchy', '_ch5', 'assertSymbolDomNode', 'defineFunction', 'sizeAtStyle', 'module', 'buildHTML_styleMap', 'checkSymbolNodeType', 'mclass_makeSpan', 'Lexer_Lexer', 'parseTree_parseTree', 'katex_render', 'defineSymbol', '__webpack_require__', 'makeLeftRightDelim', 'SS', 'katex_webpack', 'supportedCodepoint', 'fontMetricsBySizeIndex', 'makeLineSpan', 'buildCommon_makeAnchor', 'mediumspace', 'buildHTML_buildExpression', 'mathMLTree_TextNode', 'fontAliases', 'spaceRegexString', 'digitToNumber', 'delimFromValue', '_ch3', '_fracDen', 'Namespace_Namespace', 'MacroExpander_MacroExpander', '_toNode', 'LineNode', 'vbPad', 'allBlocks', 'symbols_wideChar', 'deflt', 'buildCommon_tryCombineChars', 'macros_newcommand', 'unicodeSymbols', 'implicitCommands', 'delimiter_makeSmallDelim', 'createClass', 'symbols_open', 'rel', 'buildExpressionRow', 'traverseSequence', 'optionsWithFont', 'combiningDiacriticalMarkString', 'katex_generateParseTree', 'symbols_i2', 'mathMLTree_MathNode', '_ch4', 'combiningDiacriticalMarksEndRegex', 'buildCommon_makeSpan', 'buildHTML_makeSpan', 'delimiter_sqrtSvg', 'getGlobalMetrics', 'buildCommon_makeSymbol', 'delimiterSizes', 'ATOMS', 'uppercase', 'stretchy_encloseSpan', 'symbols_text', 'enclose_mathmlBuilder', 'buildTree_optionsFromSettings', 'initNode', 'arrow_paddedNode', 'buildMathML_buildGroup', 'buildMathML_buildExpression', 'symbols_i', 'assert', 'array_alignedHandler'])
        @Js
        def PyJsHoisted_utils_escape_(text, this, arguments, var=var):
            var = Scope({'text':text, 'this':this, 'arguments':arguments}, var)
            var.registers(['text'])
            @Js
            def PyJs_anonymous_11_(match, this, arguments, var=var):
                var = Scope({'match':match, 'this':this, 'arguments':arguments}, var)
                var.registers(['match'])
                return var.get('ESCAPE_LOOKUP').get(var.get('match'))
            PyJs_anonymous_11_._set_name('anonymous')
            return var.get('String')(var.get('text')).callprop('replace', var.get('ESCAPE_REGEX'), PyJs_anonymous_11_)
        PyJsHoisted_utils_escape_.func_name = 'utils_escape'
        var.put('utils_escape', PyJsHoisted_utils_escape_)
        @Js
        def PyJsHoisted_scriptFromCodepoint_(codepoint, this, arguments, var=var):
            var = Scope({'codepoint':codepoint, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'codepoint', '_i', 'block', 'script'])
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('scriptData').get('length')):
                try:
                    var.put('script', var.get('scriptData').get(var.get('i')))
                    #for JS loop
                    var.put('_i', Js(0.0))
                    while (var.get('_i')<var.get('script').get('blocks').get('length')):
                        try:
                            var.put('block', var.get('script').get('blocks').get(var.get('_i')))
                            if ((var.get('codepoint')>=var.get('block').get('0')) and (var.get('codepoint')<=var.get('block').get('1'))):
                                return var.get('script').get('name')
                        finally:
                                (var.put('_i',Js(var.get('_i').to_number())+Js(1))-Js(1))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            return var.get(u"null")
        PyJsHoisted_scriptFromCodepoint_.func_name = 'scriptFromCodepoint'
        var.put('scriptFromCodepoint', PyJsHoisted_scriptFromCodepoint_)
        @Js
        def PyJsHoisted_supportedCodepoint_(codepoint, this, arguments, var=var):
            var = Scope({'codepoint':codepoint, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'codepoint'])
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('allBlocks').get('length')):
                try:
                    if ((var.get('codepoint')>=var.get('allBlocks').get(var.get('i'))) and (var.get('codepoint')<=var.get('allBlocks').get((var.get('i')+Js(1.0))))):
                        return Js(True)
                finally:
                        var.put('i', Js(2.0), '+')
            return Js(False)
        PyJsHoisted_supportedCodepoint_.func_name = 'supportedCodepoint'
        var.put('supportedCodepoint', PyJsHoisted_supportedCodepoint_)
        @Js
        def PyJsHoisted_assertSymbolDomNode_(group, this, arguments, var=var):
            var = Scope({'group':group, 'this':this, 'arguments':arguments}, var)
            var.registers(['group'])
            if var.get('group').instanceof(var.get('domTree_SymbolNode')):
                return var.get('group')
            else:
                PyJsTempException = JsToPyException(var.get('Error').create(((Js('Expected symbolNode but got ')+var.get('String')(var.get('group')))+Js('.'))))
                raise PyJsTempException
        PyJsHoisted_assertSymbolDomNode_.func_name = 'assertSymbolDomNode'
        var.put('assertSymbolDomNode', PyJsHoisted_assertSymbolDomNode_)
        @Js
        def PyJsHoisted_assertSpan_(group, this, arguments, var=var):
            var = Scope({'group':group, 'this':this, 'arguments':arguments}, var)
            var.registers(['group'])
            if var.get('group').instanceof(var.get('domTree_Span')):
                return var.get('group')
            else:
                PyJsTempException = JsToPyException(var.get('Error').create(((Js('Expected span<HtmlDomNode> but got ')+var.get('String')(var.get('group')))+Js('.'))))
                raise PyJsTempException
        PyJsHoisted_assertSpan_.func_name = 'assertSpan'
        var.put('assertSpan', PyJsHoisted_assertSpan_)
        @Js
        def PyJsHoisted_setFontMetrics_(fontName, metrics, this, arguments, var=var):
            var = Scope({'fontName':fontName, 'metrics':metrics, 'this':this, 'arguments':arguments}, var)
            var.registers(['fontName', 'metrics'])
            var.get('fontMetricsData').put(var.get('fontName'), var.get('metrics'))
        PyJsHoisted_setFontMetrics_.func_name = 'setFontMetrics'
        var.put('setFontMetrics', PyJsHoisted_setFontMetrics_)
        @Js
        def PyJsHoisted_getCharacterMetrics_(character, font, mode, this, arguments, var=var):
            var = Scope({'character':character, 'font':font, 'mode':mode, 'this':this, 'arguments':arguments}, var)
            var.registers(['mode', 'font', 'ch', 'metrics', 'character'])
            if var.get('fontMetricsData').get(var.get('font')).neg():
                PyJsTempException = JsToPyException(var.get('Error').create(((Js('Font metrics not found for font: ')+var.get('font'))+Js('.'))))
                raise PyJsTempException
            var.put('ch', var.get('character').callprop('charCodeAt', Js(0.0)))
            var.put('metrics', var.get('fontMetricsData').get(var.get('font')).get(var.get('ch')))
            if (var.get('metrics').neg() and var.get('extraCharacterMap').contains(var.get('character').get('0'))):
                var.put('ch', var.get('extraCharacterMap').get(var.get('character').get('0')).callprop('charCodeAt', Js(0.0)))
                var.put('metrics', var.get('fontMetricsData').get(var.get('font')).get(var.get('ch')))
            if (var.get('metrics').neg() and PyJsStrictEq(var.get('mode'),Js('text'))):
                if var.get('supportedCodepoint')(var.get('ch')):
                    var.put('metrics', var.get('fontMetricsData').get(var.get('font')).get('77'))
            if var.get('metrics'):
                return Js({'depth':var.get('metrics').get('0'),'height':var.get('metrics').get('1'),'italic':var.get('metrics').get('2'),'skew':var.get('metrics').get('3'),'width':var.get('metrics').get('4')})
        PyJsHoisted_getCharacterMetrics_.func_name = 'getCharacterMetrics'
        var.put('getCharacterMetrics', PyJsHoisted_getCharacterMetrics_)
        @Js
        def PyJsHoisted_getGlobalMetrics_(size, this, arguments, var=var):
            var = Scope({'size':size, 'this':this, 'arguments':arguments}, var)
            var.registers(['sizeIndex', 'key', 'metrics', 'size'])
            pass
            if (var.get('size')>=Js(5.0)):
                var.put('sizeIndex', Js(0.0))
            else:
                if (var.get('size')>=Js(3.0)):
                    var.put('sizeIndex', Js(1.0))
                else:
                    var.put('sizeIndex', Js(2.0))
            if var.get('fontMetricsBySizeIndex').get(var.get('sizeIndex')).neg():
                var.put('metrics', var.get('fontMetricsBySizeIndex').put(var.get('sizeIndex'), Js({'cssEmPerMu':(var.get('sigmasAndXis').get('quad').get(var.get('sizeIndex'))/Js(18.0))})))
                for PyJsTemp in var.get('sigmasAndXis'):
                    var.put('key', PyJsTemp)
                    if var.get('sigmasAndXis').callprop('hasOwnProperty', var.get('key')):
                        var.get('metrics').put(var.get('key'), var.get('sigmasAndXis').get(var.get('key')).get(var.get('sizeIndex')))
            return var.get('fontMetricsBySizeIndex').get(var.get('sizeIndex'))
        PyJsHoisted_getGlobalMetrics_.func_name = 'getGlobalMetrics'
        var.put('getGlobalMetrics', PyJsHoisted_getGlobalMetrics_)
        @Js
        def PyJsHoisted_defineSymbol_(mode, font, group, replace, name, acceptUnicodeChar, this, arguments, var=var):
            var = Scope({'mode':mode, 'font':font, 'group':group, 'replace':replace, 'name':name, 'acceptUnicodeChar':acceptUnicodeChar, 'this':this, 'arguments':arguments}, var)
            var.registers(['mode', 'font', 'group', 'name', 'acceptUnicodeChar', 'replace'])
            var.get('symbols').get(var.get('mode')).put(var.get('name'), Js({'font':var.get('font'),'group':var.get('group'),'replace':var.get('replace')}))
            if (var.get('acceptUnicodeChar') and var.get('replace')):
                var.get('symbols').get(var.get('mode')).put(var.get('replace'), var.get('symbols').get(var.get('mode')).get(var.get('name')))
        PyJsHoisted_defineSymbol_.func_name = 'defineSymbol'
        var.put('defineSymbol', PyJsHoisted_defineSymbol_)
        @Js
        def PyJsHoisted_assertNodeType_(node, type, this, arguments, var=var):
            var = Scope({'node':node, 'type':type, 'this':this, 'arguments':arguments}, var)
            var.registers(['node', 'type', 'typedNode'])
            var.put('typedNode', var.get('checkNodeType')(var.get('node'), var.get('type')))
            if var.get('typedNode').neg():
                PyJsTempException = JsToPyException(var.get('Error').create((((Js('Expected node of type ')+var.get('type'))+Js(', but got '))+((Js('node of type ')+var.get('node').get('type')) if var.get('node') else var.get('String')(var.get('node'))))))
                raise PyJsTempException
            return var.get('typedNode')
        PyJsHoisted_assertNodeType_.func_name = 'assertNodeType'
        var.put('assertNodeType', PyJsHoisted_assertNodeType_)
        @Js
        def PyJsHoisted_checkNodeType_(node, type, this, arguments, var=var):
            var = Scope({'node':node, 'type':type, 'this':this, 'arguments':arguments}, var)
            var.registers(['node', 'type'])
            if (var.get('node') and PyJsStrictEq(var.get('node').get('type'),var.get('type'))):
                return var.get('node')
            return var.get(u"null")
        PyJsHoisted_checkNodeType_.func_name = 'checkNodeType'
        var.put('checkNodeType', PyJsHoisted_checkNodeType_)
        @Js
        def PyJsHoisted_assertAtomFamily_(node, family, this, arguments, var=var):
            var = Scope({'node':node, 'family':family, 'this':this, 'arguments':arguments}, var)
            var.registers(['node', 'family', 'typedNode'])
            var.put('typedNode', var.get('checkAtomFamily')(var.get('node'), var.get('family')))
            if var.get('typedNode').neg():
                PyJsTempException = JsToPyException(var.get('Error').create((((Js('Expected node of type "atom" and family "')+var.get('family'))+Js('", but got '))+(((Js('atom of family ')+var.get('node').get('family')) if PyJsStrictEq(var.get('node').get('type'),Js('atom')) else (Js('node of type ')+var.get('node').get('type'))) if var.get('node') else var.get('String')(var.get('node'))))))
                raise PyJsTempException
            return var.get('typedNode')
        PyJsHoisted_assertAtomFamily_.func_name = 'assertAtomFamily'
        var.put('assertAtomFamily', PyJsHoisted_assertAtomFamily_)
        @Js
        def PyJsHoisted_checkAtomFamily_(node, family, this, arguments, var=var):
            var = Scope({'node':node, 'family':family, 'this':this, 'arguments':arguments}, var)
            var.registers(['node', 'family'])
            return (var.get('node') if ((var.get('node') and PyJsStrictEq(var.get('node').get('type'),Js('atom'))) and PyJsStrictEq(var.get('node').get('family'),var.get('family'))) else var.get(u"null"))
        PyJsHoisted_checkAtomFamily_.func_name = 'checkAtomFamily'
        var.put('checkAtomFamily', PyJsHoisted_checkAtomFamily_)
        @Js
        def PyJsHoisted_assertSymbolNodeType_(node, this, arguments, var=var):
            var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
            var.registers(['node', 'typedNode'])
            var.put('typedNode', var.get('checkSymbolNodeType')(var.get('node')))
            if var.get('typedNode').neg():
                PyJsTempException = JsToPyException(var.get('Error').create((Js('Expected node of symbol group type, but got ')+((Js('node of type ')+var.get('node').get('type')) if var.get('node') else var.get('String')(var.get('node'))))))
                raise PyJsTempException
            return var.get('typedNode')
        PyJsHoisted_assertSymbolNodeType_.func_name = 'assertSymbolNodeType'
        var.put('assertSymbolNodeType', PyJsHoisted_assertSymbolNodeType_)
        @Js
        def PyJsHoisted_checkSymbolNodeType_(node, this, arguments, var=var):
            var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
            var.registers(['node'])
            if (var.get('node') and (PyJsStrictEq(var.get('node').get('type'),Js('atom')) or var.get('NON_ATOMS').callprop('hasOwnProperty', var.get('node').get('type')))):
                return var.get('node')
            return var.get(u"null")
        PyJsHoisted_checkSymbolNodeType_.func_name = 'checkSymbolNodeType'
        var.put('checkSymbolNodeType', PyJsHoisted_checkSymbolNodeType_)
        @Js
        def PyJsHoisted_defineFunction_(_ref, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'nodeType', 'type', 'handler', 'mathmlBuilder', 'data', 'props', 'names', '_ref', 'htmlBuilder'])
            var.put('type', var.get('_ref').get('type'))
            var.put('nodeType', var.get('_ref').get('nodeType'))
            var.put('names', var.get('_ref').get('names'))
            var.put('props', var.get('_ref').get('props'))
            var.put('handler', var.get('_ref').get('handler'))
            var.put('htmlBuilder', var.get('_ref').get('htmlBuilder'))
            var.put('mathmlBuilder', var.get('_ref').get('mathmlBuilder'))
            var.put('data', Js({'type':var.get('type'),'numArgs':var.get('props').get('numArgs'),'argTypes':var.get('props').get('argTypes'),'greediness':(Js(1.0) if PyJsStrictEq(var.get('props').get('greediness'),var.get('undefined')) else var.get('props').get('greediness')),'allowedInText':var.get('props').get('allowedInText').neg().neg(),'allowedInMath':(Js(True) if PyJsStrictEq(var.get('props').get('allowedInMath'),var.get('undefined')) else var.get('props').get('allowedInMath')),'numOptionalArgs':(var.get('props').get('numOptionalArgs') or Js(0.0)),'infix':var.get('props').get('infix').neg().neg(),'consumeMode':var.get('props').get('consumeMode'),'handler':var.get('handler')}))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('names').get('length')):
                try:
                    var.get('_functions').put(var.get('names').get(var.get('i')), var.get('data'))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            if var.get('type'):
                if var.get('htmlBuilder'):
                    var.get('_htmlGroupBuilders').put(var.get('type'), var.get('htmlBuilder'))
                if var.get('mathmlBuilder'):
                    var.get('_mathmlGroupBuilders').put(var.get('type'), var.get('mathmlBuilder'))
        PyJsHoisted_defineFunction_.func_name = 'defineFunction'
        var.put('defineFunction', PyJsHoisted_defineFunction_)
        @Js
        def PyJsHoisted_defineFunctionBuilders_(_ref2, this, arguments, var=var):
            var = Scope({'_ref2':_ref2, 'this':this, 'arguments':arguments}, var)
            var.registers(['mathmlBuilder', 'type', 'htmlBuilder', '_ref2'])
            var.put('type', var.get('_ref2').get('type'))
            var.put('htmlBuilder', var.get('_ref2').get('htmlBuilder'))
            var.put('mathmlBuilder', var.get('_ref2').get('mathmlBuilder'))
            @Js
            def PyJs_handler_113_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'handler':PyJs_handler_113_}, var)
                var.registers([])
                PyJsTempException = JsToPyException(var.get('Error').create(Js('Should never be called.')))
                raise PyJsTempException
            PyJs_handler_113_._set_name('handler')
            var.get('defineFunction')(Js({'type':var.get('type'),'names':Js([]),'props':Js({'numArgs':Js(0.0)}),'handler':PyJs_handler_113_,'htmlBuilder':var.get('htmlBuilder'),'mathmlBuilder':var.get('mathmlBuilder')}))
        PyJsHoisted_defineFunctionBuilders_.func_name = 'defineFunctionBuilders'
        var.put('defineFunctionBuilders', PyJsHoisted_defineFunctionBuilders_)
        @Js
        def PyJsHoisted_buildHTMLUnbreakable_(children, options, this, arguments, var=var):
            var = Scope({'children':children, 'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['body', 'options', 'children', 'strut'])
            var.put('body', var.get('buildHTML_makeSpan')(Js([Js('base')]), var.get('children'), var.get('options')))
            var.put('strut', var.get('buildHTML_makeSpan')(Js([Js('strut')])))
            var.get('strut').get('style').put('height', ((var.get('body').get('height')+var.get('body').get('depth'))+Js('em')))
            var.get('strut').get('style').put('verticalAlign', ((-var.get('body').get('depth'))+Js('em')))
            var.get('body').get('children').callprop('unshift', var.get('strut'))
            return var.get('body')
        PyJsHoisted_buildHTMLUnbreakable_.func_name = 'buildHTMLUnbreakable'
        var.put('buildHTMLUnbreakable', PyJsHoisted_buildHTMLUnbreakable_)
        @Js
        def PyJsHoisted_buildHTML_(tree, options, this, arguments, var=var):
            var = Scope({'tree':tree, 'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['parts', 'children', 'i', 'expression', 'htmlNode', 'tagChild', 'options', 'tag', 'nobreak', 'tree', 'strut'])
            var.put('tag', var.get(u"null"))
            if (PyJsStrictEq(var.get('tree').get('length'),Js(1.0)) and PyJsStrictEq(var.get('tree').get('0').get('type'),Js('tag'))):
                var.put('tag', var.get('tree').get('0').get('tag'))
                var.put('tree', var.get('tree').get('0').get('body'))
            var.put('expression', var.get('buildHTML_buildExpression')(var.get('tree'), var.get('options'), Js(True)))
            var.put('children', Js([]))
            var.put('parts', Js([]))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('expression').get('length')):
                try:
                    var.get('parts').callprop('push', var.get('expression').get(var.get('i')))
                    if ((var.get('expression').get(var.get('i')).callprop('hasClass', Js('mbin')) or var.get('expression').get(var.get('i')).callprop('hasClass', Js('mrel'))) or var.get('expression').get(var.get('i')).callprop('hasClass', Js('allowbreak'))):
                        var.put('nobreak', Js(False))
                        while (((var.get('i')<(var.get('expression').get('length')-Js(1.0))) and var.get('expression').get((var.get('i')+Js(1.0))).callprop('hasClass', Js('mspace'))) and var.get('expression').get((var.get('i')+Js(1.0))).callprop('hasClass', Js('newline')).neg()):
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                            var.get('parts').callprop('push', var.get('expression').get(var.get('i')))
                            if var.get('expression').get(var.get('i')).callprop('hasClass', Js('nobreak')):
                                var.put('nobreak', Js(True))
                        if var.get('nobreak').neg():
                            var.get('children').callprop('push', var.get('buildHTMLUnbreakable')(var.get('parts'), var.get('options')))
                            var.put('parts', Js([]))
                    else:
                        if var.get('expression').get(var.get('i')).callprop('hasClass', Js('newline')):
                            var.get('parts').callprop('pop')
                            if (var.get('parts').get('length')>Js(0.0)):
                                var.get('children').callprop('push', var.get('buildHTMLUnbreakable')(var.get('parts'), var.get('options')))
                                var.put('parts', Js([]))
                            var.get('children').callprop('push', var.get('expression').get(var.get('i')))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            if (var.get('parts').get('length')>Js(0.0)):
                var.get('children').callprop('push', var.get('buildHTMLUnbreakable')(var.get('parts'), var.get('options')))
            pass
            if var.get('tag'):
                var.put('tagChild', var.get('buildHTMLUnbreakable')(var.get('buildHTML_buildExpression')(var.get('tag'), var.get('options'), Js(True))))
                var.get('tagChild').put('classes', Js([Js('tag')]))
                var.get('children').callprop('push', var.get('tagChild'))
            var.put('htmlNode', var.get('buildHTML_makeSpan')(Js([Js('katex-html')]), var.get('children')))
            var.get('htmlNode').callprop('setAttribute', Js('aria-hidden'), Js('true'))
            if var.get('tagChild'):
                var.put('strut', var.get('tagChild').get('children').get('0'))
                var.get('strut').get('style').put('height', ((var.get('htmlNode').get('height')+var.get('htmlNode').get('depth'))+Js('em')))
                var.get('strut').get('style').put('verticalAlign', ((-var.get('htmlNode').get('depth'))+Js('em')))
            return var.get('htmlNode')
        PyJsHoisted_buildHTML_.func_name = 'buildHTML'
        var.put('buildHTML', PyJsHoisted_buildHTML_)
        @Js
        def PyJsHoisted_newDocumentFragment_(children, this, arguments, var=var):
            var = Scope({'children':children, 'this':this, 'arguments':arguments}, var)
            var.registers(['children'])
            return var.get('tree_DocumentFragment').create(var.get('children'))
        PyJsHoisted_newDocumentFragment_.func_name = 'newDocumentFragment'
        var.put('newDocumentFragment', PyJsHoisted_newDocumentFragment_)
        @Js
        def PyJsHoisted_buildMathML_(tree, texExpression, options, this, arguments, var=var):
            var = Scope({'tree':tree, 'texExpression':texExpression, 'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['expression', 'options', 'annotation', 'texExpression', 'wrapper', 'semantics', 'tree', 'math'])
            var.put('expression', var.get('buildMathML_buildExpression')(var.get('tree'), var.get('options')))
            pass
            if ((PyJsStrictEq(var.get('expression').get('length'),Js(1.0)) and var.get('expression').get('0').instanceof(var.get('mathMLTree_MathNode'))) and var.get('utils').callprop('contains', Js([Js('mrow'), Js('mtable')]), var.get('expression').get('0').get('type'))):
                var.put('wrapper', var.get('expression').get('0'))
            else:
                var.put('wrapper', var.get('mathMLTree').get('MathNode').create(Js('mrow'), var.get('expression')))
            var.put('annotation', var.get('mathMLTree').get('MathNode').create(Js('annotation'), Js([var.get('mathMLTree').get('TextNode').create(var.get('texExpression'))])))
            var.get('annotation').callprop('setAttribute', Js('encoding'), Js('application/x-tex'))
            var.put('semantics', var.get('mathMLTree').get('MathNode').create(Js('semantics'), Js([var.get('wrapper'), var.get('annotation')])))
            var.put('math', var.get('mathMLTree').get('MathNode').create(Js('math'), Js([var.get('semantics')])))
            return var.get('buildCommon').callprop('makeSpan', Js([Js('katex-mathml')]), Js([var.get('math')]))
        PyJsHoisted_buildMathML_.func_name = 'buildMathML'
        var.put('buildMathML', PyJsHoisted_buildMathML_)
        @Js
        def PyJsHoisted_checkDelimiter_(delim, context, this, arguments, var=var):
            var = Scope({'delim':delim, 'context':context, 'this':this, 'arguments':arguments}, var)
            var.registers(['symDelim', 'context', 'delim'])
            var.put('symDelim', var.get('checkSymbolNodeType')(var.get('delim')))
            if (var.get('symDelim') and var.get('utils').callprop('contains', var.get('delimiters'), var.get('symDelim').get('text'))):
                return var.get('symDelim')
            else:
                PyJsTempException = JsToPyException(var.get('src_ParseError').create(((((Js("Invalid delimiter: '")+(var.get('symDelim').get('text') if var.get('symDelim') else var.get('JSON').callprop('stringify', var.get('delim'))))+Js("' after '"))+var.get('context').get('funcName'))+Js("'")), var.get('delim')))
                raise PyJsTempException
        PyJsHoisted_checkDelimiter_.func_name = 'checkDelimiter'
        var.put('checkDelimiter', PyJsHoisted_checkDelimiter_)
        @Js
        def PyJsHoisted_assertParsed_(group, this, arguments, var=var):
            var = Scope({'group':group, 'this':this, 'arguments':arguments}, var)
            var.registers(['group'])
            if var.get('group').get('body').neg():
                PyJsTempException = JsToPyException(var.get('Error').create(Js("Bug: The leftright ParseNode wasn't fully parsed.")))
                raise PyJsTempException
        PyJsHoisted_assertParsed_.func_name = 'assertParsed'
        var.put('assertParsed', PyJsHoisted_assertParsed_)
        @Js
        def PyJsHoisted_defineEnvironment_(_ref, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'handler', 'type', 'mathmlBuilder', 'data', 'props', 'names', '_ref', 'htmlBuilder'])
            var.put('type', var.get('_ref').get('type'))
            var.put('names', var.get('_ref').get('names'))
            var.put('props', var.get('_ref').get('props'))
            var.put('handler', var.get('_ref').get('handler'))
            var.put('htmlBuilder', var.get('_ref').get('htmlBuilder'))
            var.put('mathmlBuilder', var.get('_ref').get('mathmlBuilder'))
            var.put('data', Js({'type':var.get('type'),'numArgs':(var.get('props').get('numArgs') or Js(0.0)),'greediness':Js(1.0),'allowedInText':Js(False),'numOptionalArgs':Js(0.0),'handler':var.get('handler')}))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('names').get('length')):
                try:
                    var.get('_environments').put(var.get('names').get(var.get('i')), var.get('data'))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            if var.get('htmlBuilder'):
                var.get('_htmlGroupBuilders').put(var.get('type'), var.get('htmlBuilder'))
            if var.get('mathmlBuilder'):
                var.get('_mathmlGroupBuilders').put(var.get('type'), var.get('mathmlBuilder'))
        PyJsHoisted_defineEnvironment_.func_name = 'defineEnvironment'
        var.put('defineEnvironment', PyJsHoisted_defineEnvironment_)
        @Js
        def PyJsHoisted_getHLines_(parser, this, arguments, var=var):
            var = Scope({'parser':parser, 'this':this, 'arguments':arguments}, var)
            var.registers(['parser', 'nxt', 'hlineInfo'])
            var.put('hlineInfo', Js([]))
            var.get('parser').callprop('consumeSpaces')
            var.put('nxt', var.get('parser').get('nextToken').get('text'))
            while (PyJsStrictEq(var.get('nxt'),Js('\\hline')) or PyJsStrictEq(var.get('nxt'),Js('\\hdashline'))):
                var.get('parser').callprop('consume')
                var.get('hlineInfo').callprop('push', PyJsStrictEq(var.get('nxt'),Js('\\hdashline')))
                var.get('parser').callprop('consumeSpaces')
                var.put('nxt', var.get('parser').get('nextToken').get('text'))
            return var.get('hlineInfo')
        PyJsHoisted_getHLines_.func_name = 'getHLines'
        var.put('getHLines', PyJsHoisted_getHLines_)
        @Js
        def PyJsHoisted_parseArray_(parser, _ref, style, this, arguments, var=var):
            var = Scope({'parser':parser, '_ref':_ref, 'style':style, 'this':this, 'arguments':arguments}, var)
            var.registers(['addJot', 'hskipBeforeAndAfter', 'body', 'rowGaps', 'style', 'colSeparationType', 'arraystretch', 'cols', 'next', 'row', 'cell', 'cr', 'stretch', 'hLinesBeforeRow', '_ref', 'parser'])
            var.put('hskipBeforeAndAfter', var.get('_ref').get('hskipBeforeAndAfter'))
            var.put('addJot', var.get('_ref').get('addJot'))
            var.put('cols', var.get('_ref').get('cols'))
            var.put('arraystretch', var.get('_ref').get('arraystretch'))
            var.put('colSeparationType', var.get('_ref').get('colSeparationType'))
            var.get('parser').get('gullet').callprop('beginGroup')
            var.get('parser').get('gullet').get('macros').callprop('set', Js('\\\\'), Js('\\cr'))
            if var.get('arraystretch').neg():
                var.put('stretch', var.get('parser').get('gullet').callprop('expandMacroAsText', Js('\\arraystretch')))
                if (var.get('stretch')==var.get(u"null")):
                    var.put('arraystretch', Js(1.0))
                else:
                    var.put('arraystretch', var.get('parseFloat')(var.get('stretch')))
                    if (var.get('arraystretch').neg() or (var.get('arraystretch')<Js(0.0))):
                        PyJsTempException = JsToPyException(var.get('src_ParseError').create((Js('Invalid \\arraystretch: ')+var.get('stretch'))))
                        raise PyJsTempException
            var.put('row', Js([]))
            var.put('body', Js([var.get('row')]))
            var.put('rowGaps', Js([]))
            var.put('hLinesBeforeRow', Js([]))
            var.get('hLinesBeforeRow').callprop('push', var.get('getHLines')(var.get('parser')))
            while Js(True):
                var.put('cell', var.get('parser').callprop('parseExpression', Js(False), Js('\\cr')))
                var.put('cell', Js({'type':Js('ordgroup'),'mode':var.get('parser').get('mode'),'body':var.get('cell')}))
                if var.get('style'):
                    var.put('cell', Js({'type':Js('styling'),'mode':var.get('parser').get('mode'),'style':var.get('style'),'body':Js([var.get('cell')])}))
                var.get('row').callprop('push', var.get('cell'))
                var.put('next', var.get('parser').get('nextToken').get('text'))
                if PyJsStrictEq(var.get('next'),Js('&')):
                    var.get('parser').callprop('consume')
                else:
                    if PyJsStrictEq(var.get('next'),Js('\\end')):
                        if ((PyJsStrictEq(var.get('row').get('length'),Js(1.0)) and PyJsStrictEq(var.get('cell').get('type'),Js('styling'))) and PyJsStrictEq(var.get('cell').get('body').get('0').get('body').get('length'),Js(0.0))):
                            var.get('body').callprop('pop')
                        if (var.get('hLinesBeforeRow').get('length')<(var.get('body').get('length')+Js(1.0))):
                            var.get('hLinesBeforeRow').callprop('push', Js([]))
                        break
                    else:
                        if PyJsStrictEq(var.get('next'),Js('\\cr')):
                            var.put('cr', var.get('assertNodeType')(var.get('parser').callprop('parseFunction'), Js('cr')))
                            var.get('rowGaps').callprop('push', var.get('cr').get('size'))
                            var.get('hLinesBeforeRow').callprop('push', var.get('getHLines')(var.get('parser')))
                            var.put('row', Js([]))
                            var.get('body').callprop('push', var.get('row'))
                        else:
                            PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('Expected & or \\\\ or \\cr or \\end'), var.get('parser').get('nextToken')))
                            raise PyJsTempException
            var.get('parser').get('gullet').callprop('endGroup')
            return Js({'type':Js('array'),'mode':var.get('parser').get('mode'),'addJot':var.get('addJot'),'arraystretch':var.get('arraystretch'),'body':var.get('body'),'cols':var.get('cols'),'rowGaps':var.get('rowGaps'),'hskipBeforeAndAfter':var.get('hskipBeforeAndAfter'),'hLinesBeforeRow':var.get('hLinesBeforeRow'),'colSeparationType':var.get('colSeparationType')})
        PyJsHoisted_parseArray_.func_name = 'parseArray'
        var.put('parseArray', PyJsHoisted_parseArray_)
        @Js
        def PyJsHoisted_dCellStyle_(envName, this, arguments, var=var):
            var = Scope({'envName':envName, 'this':this, 'arguments':arguments}, var)
            var.registers(['envName'])
            if PyJsStrictEq(var.get('envName').callprop('substr', Js(0.0), Js(1.0)),Js('d')):
                return Js('display')
            else:
                return Js('text')
        PyJsHoisted_dCellStyle_.func_name = 'dCellStyle'
        var.put('dCellStyle', PyJsHoisted_dCellStyle_)
        @Js
        def PyJsHoisted_mclass_htmlBuilder_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['group', 'options', 'elements'])
            var.put('elements', var.get('buildHTML_buildExpression')(var.get('group').get('body'), var.get('options'), Js(True)))
            return var.get('mclass_makeSpan')(Js([var.get('group').get('mclass')]), var.get('elements'), var.get('options'))
        PyJsHoisted_mclass_htmlBuilder_.func_name = 'mclass_htmlBuilder'
        var.put('mclass_htmlBuilder', PyJsHoisted_mclass_htmlBuilder_)
        @Js
        def PyJsHoisted_mclass_mathmlBuilder_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['group', 'inner', 'options'])
            var.put('inner', var.get('buildMathML_buildExpression')(var.get('group').get('body'), var.get('options')))
            return var.get('mathMLTree').callprop('newDocumentFragment', var.get('inner'))
        PyJsHoisted_mclass_mathmlBuilder_.func_name = 'mclass_mathmlBuilder'
        var.put('mclass_mathmlBuilder', PyJsHoisted_mclass_mathmlBuilder_)
        @Js
        def PyJsHoisted_sizingGroup_(value, options, baseOptions, this, arguments, var=var):
            var = Scope({'value':value, 'options':options, 'baseOptions':baseOptions, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'options', 'baseOptions', 'pos', 'inner', 'multiplier', 'value'])
            var.put('inner', var.get('buildHTML_buildExpression')(var.get('value'), var.get('options'), Js(False)))
            var.put('multiplier', (var.get('options').get('sizeMultiplier')/var.get('baseOptions').get('sizeMultiplier')))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('inner').get('length')):
                try:
                    var.put('pos', var.get('inner').get(var.get('i')).get('classes').callprop('indexOf', Js('sizing')))
                    if (var.get('pos')<Js(0.0)):
                        var.get('Array').get('prototype').get('push').callprop('apply', var.get('inner').get(var.get('i')).get('classes'), var.get('options').callprop('sizingClasses', var.get('baseOptions')))
                    else:
                        if PyJsStrictEq(var.get('inner').get(var.get('i')).get('classes').get((var.get('pos')+Js(1.0))),(Js('reset-size')+var.get('options').get('size'))):
                            var.get('inner').get(var.get('i')).get('classes').put((var.get('pos')+Js(1.0)), (Js('reset-size')+var.get('baseOptions').get('size')))
                    var.get('inner').get(var.get('i')).put('height', var.get('multiplier'), '*')
                    var.get('inner').get(var.get('i')).put('depth', var.get('multiplier'), '*')
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            return var.get('buildCommon').callprop('makeFragment', var.get('inner'))
        PyJsHoisted_sizingGroup_.func_name = 'sizingGroup'
        var.put('sizingGroup', PyJsHoisted_sizingGroup_)
        @Js
        def PyJsHoisted_defineMacro_(name, body, this, arguments, var=var):
            var = Scope({'name':name, 'body':body, 'this':this, 'arguments':arguments}, var)
            var.registers(['body', 'name'])
            var.get('builtinMacros').put(var.get('name'), var.get('body'))
        PyJsHoisted_defineMacro_.func_name = 'defineMacro'
        var.put('defineMacro', PyJsHoisted_defineMacro_)
        Js('use strict')
        var.get('__webpack_require__').callprop('r', var.get('__webpack_exports__'))
        var.put('katex', var.get('__webpack_require__')(Js(0.0)))
        @Js
        def PyJs_anonymous_3_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['SourceLocation'])
            @Js
            def PyJsHoisted_SourceLocation_(lexer, start, end, this, arguments, var=var):
                var = Scope({'lexer':lexer, 'start':start, 'end':end, 'this':this, 'arguments':arguments}, var)
                var.registers(['start', 'lexer', 'end'])
                var.get(u"this").put('lexer', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('start', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('end', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('lexer', var.get('lexer'))
                var.get(u"this").put('start', var.get('start'))
                var.get(u"this").put('end', var.get('end'))
            PyJsHoisted_SourceLocation_.func_name = 'SourceLocation'
            var.put('SourceLocation', PyJsHoisted_SourceLocation_)
            pass
            @Js
            def PyJs_range_4_(first, second, this, arguments, var=var):
                var = Scope({'first':first, 'second':second, 'this':this, 'arguments':arguments, 'range':PyJs_range_4_}, var)
                var.registers(['second', 'first'])
                if var.get('second').neg():
                    return (var.get('first') and var.get('first').get('loc'))
                else:
                    if (((var.get('first').neg() or var.get('first').get('loc').neg()) or var.get('second').get('loc').neg()) or PyJsStrictNeq(var.get('first').get('loc').get('lexer'),var.get('second').get('loc').get('lexer'))):
                        return var.get(u"null")
                    else:
                        return var.get('SourceLocation').create(var.get('first').get('loc').get('lexer'), var.get('first').get('loc').get('start'), var.get('second').get('loc').get('end'))
            PyJs_range_4_._set_name('range')
            var.get('SourceLocation').put('range', PyJs_range_4_)
            return var.get('SourceLocation')
        PyJs_anonymous_3_._set_name('anonymous')
        var.put('SourceLocation', PyJs_anonymous_3_())
        @Js
        def PyJs_anonymous_5_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['_proto', 'Token'])
            @Js
            def PyJsHoisted_Token_(text, loc, this, arguments, var=var):
                var = Scope({'text':text, 'loc':loc, 'this':this, 'arguments':arguments}, var)
                var.registers(['loc', 'text'])
                var.get(u"this").put('text', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('loc', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('text', var.get('text'))
                var.get(u"this").put('loc', var.get('loc'))
            PyJsHoisted_Token_.func_name = 'Token'
            var.put('Token', PyJsHoisted_Token_)
            pass
            var.put('_proto', var.get('Token').get('prototype'))
            @Js
            def PyJs_range_6_(endToken, text, this, arguments, var=var):
                var = Scope({'endToken':endToken, 'text':text, 'this':this, 'arguments':arguments, 'range':PyJs_range_6_}, var)
                var.registers(['text', 'endToken'])
                return var.get('Token').create(var.get('text'), var.get('SourceLocation').callprop('range', var.get(u"this"), var.get('endToken')))
            PyJs_range_6_._set_name('range')
            var.get('_proto').put('range', PyJs_range_6_)
            return var.get('Token')
        PyJs_anonymous_5_._set_name('anonymous')
        var.put('Token_Token', PyJs_anonymous_5_())
        @Js
        def PyJs_ParseError_7_(message, token, this, arguments, var=var):
            var = Scope({'message':message, 'token':token, 'this':this, 'arguments':arguments, 'ParseError':PyJs_ParseError_7_}, var)
            var.registers(['loc', 'input', 'left', 'end', 'underlined', 'error', 'start', 'message', 'right', 'self', 'token'])
            var.get(u"this").put('position', PyJsComma(Js(0.0), Js(None)))
            var.put('error', (Js('KaTeX parse error: ')+var.get('message')))
            pass
            var.put('loc', (var.get('token') and var.get('token').get('loc')))
            if (var.get('loc') and (var.get('loc').get('start')<=var.get('loc').get('end'))):
                var.put('input', var.get('loc').get('lexer').get('input'))
                var.put('start', var.get('loc').get('start'))
                var.put('end', var.get('loc').get('end'))
                if PyJsStrictEq(var.get('start'),var.get('input').get('length')):
                    var.put('error', Js(' at end of input: '), '+')
                else:
                    var.put('error', ((Js(' at position ')+(var.get('start')+Js(1.0)))+Js(': ')), '+')
                var.put('underlined', var.get('input').callprop('slice', var.get('start'), var.get('end')).callprop('replace', JsRegExp('/[^]/g'), Js('$&̲')))
                pass
                if (var.get('start')>Js(15.0)):
                    var.put('left', (Js('…')+var.get('input').callprop('slice', (var.get('start')-Js(15.0)), var.get('start'))))
                else:
                    var.put('left', var.get('input').callprop('slice', Js(0.0), var.get('start')))
                pass
                if ((var.get('end')+Js(15.0))<var.get('input').get('length')):
                    var.put('right', (var.get('input').callprop('slice', var.get('end'), (var.get('end')+Js(15.0)))+Js('…')))
                else:
                    var.put('right', var.get('input').callprop('slice', var.get('end')))
                var.put('error', ((var.get('left')+var.get('underlined'))+var.get('right')), '+')
            var.put('self', var.get('Error').create(var.get('error')))
            var.get('self').put('name', Js('ParseError'))
            var.get('self').put('__proto__', var.get('ParseError').get('prototype'))
            var.get('self').put('position', var.get('start'))
            return var.get('self')
        PyJs_ParseError_7_._set_name('ParseError')
        var.put('ParseError', PyJs_ParseError_7_)
        var.get('ParseError').get('prototype').put('__proto__', var.get('Error').get('prototype'))
        var.put('src_ParseError', var.get('ParseError'))
        @Js
        def PyJs_contains_8_(list, elem, this, arguments, var=var):
            var = Scope({'list':list, 'elem':elem, 'this':this, 'arguments':arguments, 'contains':PyJs_contains_8_}, var)
            var.registers(['elem', 'list'])
            return PyJsStrictNeq(var.get('list').callprop('indexOf', var.get('elem')),(-Js(1.0)))
        PyJs_contains_8_._set_name('contains')
        var.put('contains', PyJs_contains_8_)
        @Js
        def PyJs_deflt_9_(setting, defaultIfUndefined, this, arguments, var=var):
            var = Scope({'setting':setting, 'defaultIfUndefined':defaultIfUndefined, 'this':this, 'arguments':arguments, 'deflt':PyJs_deflt_9_}, var)
            var.registers(['defaultIfUndefined', 'setting'])
            return (var.get('defaultIfUndefined') if PyJsStrictEq(var.get('setting'),var.get('undefined')) else var.get('setting'))
        PyJs_deflt_9_._set_name('deflt')
        var.put('deflt', PyJs_deflt_9_)
        var.put('uppercase', JsRegExp('/([A-Z])/g'))
        @Js
        def PyJs_hyphenate_10_(str, this, arguments, var=var):
            var = Scope({'str':str, 'this':this, 'arguments':arguments, 'hyphenate':PyJs_hyphenate_10_}, var)
            var.registers(['str'])
            return var.get('str').callprop('replace', var.get('uppercase'), Js('-$1')).callprop('toLowerCase')
        PyJs_hyphenate_10_._set_name('hyphenate')
        var.put('hyphenate', PyJs_hyphenate_10_)
        var.put('ESCAPE_LOOKUP', Js({'&':Js('&amp;'),'>':Js('&gt;'),'<':Js('&lt;'),'"':Js('&quot;'),"'":Js('&#x27;')}))
        var.put('ESCAPE_REGEX', JsRegExp('/[&><"\']/g'))
        pass
        @Js
        def PyJs_getBaseElem_12_(group, this, arguments, var=var):
            var = Scope({'group':group, 'this':this, 'arguments':arguments, 'getBaseElem':PyJs_getBaseElem_12_}, var)
            var.registers(['group'])
            if PyJsStrictEq(var.get('group').get('type'),Js('ordgroup')):
                if PyJsStrictEq(var.get('group').get('body').get('length'),Js(1.0)):
                    return var.get('getBaseElem')(var.get('group').get('body').get('0'))
                else:
                    return var.get('group')
            else:
                if PyJsStrictEq(var.get('group').get('type'),Js('color')):
                    if PyJsStrictEq(var.get('group').get('body').get('length'),Js(1.0)):
                        return var.get('getBaseElem')(var.get('group').get('body').get('0'))
                    else:
                        return var.get('group')
                else:
                    if PyJsStrictEq(var.get('group').get('type'),Js('font')):
                        return var.get('getBaseElem')(var.get('group').get('body'))
                    else:
                        return var.get('group')
        PyJs_getBaseElem_12_._set_name('getBaseElem')
        var.put('getBaseElem', PyJs_getBaseElem_12_)
        @Js
        def PyJs_isCharacterBox_13_(group, this, arguments, var=var):
            var = Scope({'group':group, 'this':this, 'arguments':arguments, 'isCharacterBox':PyJs_isCharacterBox_13_}, var)
            var.registers(['group', 'baseElem'])
            var.put('baseElem', var.get('getBaseElem')(var.get('group')))
            return ((PyJsStrictEq(var.get('baseElem').get('type'),Js('mathord')) or PyJsStrictEq(var.get('baseElem').get('type'),Js('textord'))) or PyJsStrictEq(var.get('baseElem').get('type'),Js('atom')))
        PyJs_isCharacterBox_13_._set_name('isCharacterBox')
        var.put('utils_isCharacterBox', PyJs_isCharacterBox_13_)
        @Js
        def PyJs_InlineNonPyName_14_(value, this, arguments, var=var):
            var = Scope({'value':value, 'this':this, 'arguments':arguments, 'assert':PyJs_InlineNonPyName_14_}, var)
            var.registers(['value'])
            if var.get('value').neg():
                PyJsTempException = JsToPyException(var.get('Error').create((Js('Expected non-null, but got ')+var.get('String')(var.get('value')))))
                raise PyJsTempException
            return var.get('value')
        PyJs_InlineNonPyName_14_._set_name('assert')
        var.put('assert', PyJs_InlineNonPyName_14_)
        var.put('utils', Js({'contains':var.get('contains'),'deflt':var.get('deflt'),'escape':var.get('utils_escape'),'hyphenate':var.get('hyphenate'),'getBaseElem':var.get('getBaseElem'),'isCharacterBox':var.get('utils_isCharacterBox')}))
        @Js
        def PyJs_anonymous_15_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['_proto', 'Settings'])
            @Js
            def PyJsHoisted_Settings_(options, this, arguments, var=var):
                var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
                var.registers(['options'])
                var.get(u"this").put('displayMode', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('leqno', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('fleqn', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('throwOnError', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('errorColor', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('macros', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('colorIsTextColor', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('strict', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('maxSize', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('maxExpand', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('allowedProtocols', PyJsComma(Js(0.0), Js(None)))
                var.put('options', (var.get('options') or Js({})))
                var.get(u"this").put('displayMode', var.get('utils').callprop('deflt', var.get('options').get('displayMode'), Js(False)))
                var.get(u"this").put('leqno', var.get('utils').callprop('deflt', var.get('options').get('leqno'), Js(False)))
                var.get(u"this").put('fleqn', var.get('utils').callprop('deflt', var.get('options').get('fleqn'), Js(False)))
                var.get(u"this").put('throwOnError', var.get('utils').callprop('deflt', var.get('options').get('throwOnError'), Js(True)))
                var.get(u"this").put('errorColor', var.get('utils').callprop('deflt', var.get('options').get('errorColor'), Js('#cc0000')))
                var.get(u"this").put('macros', (var.get('options').get('macros') or Js({})))
                var.get(u"this").put('colorIsTextColor', var.get('utils').callprop('deflt', var.get('options').get('colorIsTextColor'), Js(False)))
                var.get(u"this").put('strict', var.get('utils').callprop('deflt', var.get('options').get('strict'), Js('warn')))
                var.get(u"this").put('maxSize', var.get('Math').callprop('max', Js(0.0), var.get('utils').callprop('deflt', var.get('options').get('maxSize'), var.get('Infinity'))))
                var.get(u"this").put('maxExpand', var.get('Math').callprop('max', Js(0.0), var.get('utils').callprop('deflt', var.get('options').get('maxExpand'), Js(1000.0))))
                var.get(u"this").put('allowedProtocols', var.get('utils').callprop('deflt', var.get('options').get('allowedProtocols'), Js([Js('http'), Js('https'), Js('mailto'), Js('_relative')])))
            PyJsHoisted_Settings_.func_name = 'Settings'
            var.put('Settings', PyJsHoisted_Settings_)
            pass
            var.put('_proto', var.get('Settings').get('prototype'))
            @Js
            def PyJs_reportNonstrict_16_(errorCode, errorMsg, token, this, arguments, var=var):
                var = Scope({'errorCode':errorCode, 'errorMsg':errorMsg, 'token':token, 'this':this, 'arguments':arguments, 'reportNonstrict':PyJs_reportNonstrict_16_}, var)
                var.registers(['errorCode', 'strict', 'errorMsg', 'token'])
                var.put('strict', var.get(u"this").get('strict'))
                if PyJsStrictEq(var.get('strict',throw=False).typeof(),Js('function')):
                    var.put('strict', var.get('strict')(var.get('errorCode'), var.get('errorMsg'), var.get('token')))
                if (var.get('strict').neg() or PyJsStrictEq(var.get('strict'),Js('ignore'))):
                    return var.get('undefined')
                else:
                    if (PyJsStrictEq(var.get('strict'),Js(True)) or PyJsStrictEq(var.get('strict'),Js('error'))):
                        PyJsTempException = JsToPyException(var.get('src_ParseError').create((Js("LaTeX-incompatible input and strict mode is set to 'error': ")+(((var.get('errorMsg')+Js(' ['))+var.get('errorCode'))+Js(']'))), var.get('token')))
                        raise PyJsTempException
                    else:
                        if PyJsStrictEq(var.get('strict'),Js('warn')):
                            (PyJsStrictNeq(var.get('console',throw=False).typeof(),Js('undefined')) and var.get('console').callprop('warn', (Js("LaTeX-incompatible input and strict mode is set to 'warn': ")+(((var.get('errorMsg')+Js(' ['))+var.get('errorCode'))+Js(']')))))
                        else:
                            (PyJsStrictNeq(var.get('console',throw=False).typeof(),Js('undefined')) and var.get('console').callprop('warn', (Js('LaTeX-incompatible input and strict mode is set to ')+((((((Js("unrecognized '")+var.get('strict'))+Js("': "))+var.get('errorMsg'))+Js(' ['))+var.get('errorCode'))+Js(']')))))
            PyJs_reportNonstrict_16_._set_name('reportNonstrict')
            var.get('_proto').put('reportNonstrict', PyJs_reportNonstrict_16_)
            @Js
            def PyJs_useStrictBehavior_17_(errorCode, errorMsg, token, this, arguments, var=var):
                var = Scope({'errorCode':errorCode, 'errorMsg':errorMsg, 'token':token, 'this':this, 'arguments':arguments, 'useStrictBehavior':PyJs_useStrictBehavior_17_}, var)
                var.registers(['errorCode', 'strict', 'errorMsg', 'token'])
                var.put('strict', var.get(u"this").get('strict'))
                if PyJsStrictEq(var.get('strict',throw=False).typeof(),Js('function')):
                    try:
                        var.put('strict', var.get('strict')(var.get('errorCode'), var.get('errorMsg'), var.get('token')))
                    except PyJsException as PyJsTempException:
                        PyJsHolder_6572726f72_2351029 = var.own.get('error')
                        var.force_own_put('error', PyExceptionToJs(PyJsTempException))
                        try:
                            var.put('strict', Js('error'))
                        finally:
                            if PyJsHolder_6572726f72_2351029 is not None:
                                var.own['error'] = PyJsHolder_6572726f72_2351029
                            else:
                                del var.own['error']
                            del PyJsHolder_6572726f72_2351029
                if (var.get('strict').neg() or PyJsStrictEq(var.get('strict'),Js('ignore'))):
                    return Js(False)
                else:
                    if (PyJsStrictEq(var.get('strict'),Js(True)) or PyJsStrictEq(var.get('strict'),Js('error'))):
                        return Js(True)
                    else:
                        if PyJsStrictEq(var.get('strict'),Js('warn')):
                            (PyJsStrictNeq(var.get('console',throw=False).typeof(),Js('undefined')) and var.get('console').callprop('warn', (Js("LaTeX-incompatible input and strict mode is set to 'warn': ")+(((var.get('errorMsg')+Js(' ['))+var.get('errorCode'))+Js(']')))))
                            return Js(False)
                        else:
                            (PyJsStrictNeq(var.get('console',throw=False).typeof(),Js('undefined')) and var.get('console').callprop('warn', (Js('LaTeX-incompatible input and strict mode is set to ')+((((((Js("unrecognized '")+var.get('strict'))+Js("': "))+var.get('errorMsg'))+Js(' ['))+var.get('errorCode'))+Js(']')))))
                            return Js(False)
            PyJs_useStrictBehavior_17_._set_name('useStrictBehavior')
            var.get('_proto').put('useStrictBehavior', PyJs_useStrictBehavior_17_)
            return var.get('Settings')
        PyJs_anonymous_15_._set_name('anonymous')
        var.put('Settings_Settings', PyJs_anonymous_15_())
        var.put('src_Settings', var.get('Settings_Settings'))
        @Js
        def PyJs_anonymous_18_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['_proto', 'Style'])
            @Js
            def PyJsHoisted_Style_(id, size, cramped, this, arguments, var=var):
                var = Scope({'id':id, 'size':size, 'cramped':cramped, 'this':this, 'arguments':arguments}, var)
                var.registers(['cramped', 'size', 'id'])
                var.get(u"this").put('id', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('size', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('cramped', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('id', var.get('id'))
                var.get(u"this").put('size', var.get('size'))
                var.get(u"this").put('cramped', var.get('cramped'))
            PyJsHoisted_Style_.func_name = 'Style'
            var.put('Style', PyJsHoisted_Style_)
            pass
            var.put('_proto', var.get('Style').get('prototype'))
            @Js
            def PyJs_sup_19_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'sup':PyJs_sup_19_}, var)
                var.registers([])
                return var.get('Style_styles').get(var.get('_sup').get(var.get(u"this").get('id')))
            PyJs_sup_19_._set_name('sup')
            var.get('_proto').put('sup', PyJs_sup_19_)
            @Js
            def PyJs_sub_20_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'sub':PyJs_sub_20_}, var)
                var.registers([])
                return var.get('Style_styles').get(var.get('_sub').get(var.get(u"this").get('id')))
            PyJs_sub_20_._set_name('sub')
            var.get('_proto').put('sub', PyJs_sub_20_)
            @Js
            def PyJs_fracNum_21_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'fracNum':PyJs_fracNum_21_}, var)
                var.registers([])
                return var.get('Style_styles').get(var.get('_fracNum').get(var.get(u"this").get('id')))
            PyJs_fracNum_21_._set_name('fracNum')
            var.get('_proto').put('fracNum', PyJs_fracNum_21_)
            @Js
            def PyJs_fracDen_22_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'fracDen':PyJs_fracDen_22_}, var)
                var.registers([])
                return var.get('Style_styles').get(var.get('_fracDen').get(var.get(u"this").get('id')))
            PyJs_fracDen_22_._set_name('fracDen')
            var.get('_proto').put('fracDen', PyJs_fracDen_22_)
            @Js
            def PyJs_cramp_23_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'cramp':PyJs_cramp_23_}, var)
                var.registers([])
                return var.get('Style_styles').get(var.get('_cramp').get(var.get(u"this").get('id')))
            PyJs_cramp_23_._set_name('cramp')
            var.get('_proto').put('cramp', PyJs_cramp_23_)
            @Js
            def PyJs_text_24_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'text':PyJs_text_24_}, var)
                var.registers([])
                return var.get('Style_styles').get(var.get('_text').get(var.get(u"this").get('id')))
            PyJs_text_24_._set_name('text')
            var.get('_proto').put('text', PyJs_text_24_)
            @Js
            def PyJs_isTight_25_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'isTight':PyJs_isTight_25_}, var)
                var.registers([])
                return (var.get(u"this").get('size')>=Js(2.0))
            PyJs_isTight_25_._set_name('isTight')
            var.get('_proto').put('isTight', PyJs_isTight_25_)
            return var.get('Style')
        PyJs_anonymous_18_._set_name('anonymous')
        var.put('Style', PyJs_anonymous_18_())
        var.put('D', Js(0.0))
        var.put('Dc', Js(1.0))
        var.put('T', Js(2.0))
        var.put('Tc', Js(3.0))
        var.put('S', Js(4.0))
        var.put('Sc', Js(5.0))
        var.put('SS', Js(6.0))
        var.put('SSc', Js(7.0))
        var.put('Style_styles', Js([var.get('Style').create(var.get('D'), Js(0.0), Js(False)), var.get('Style').create(var.get('Dc'), Js(0.0), Js(True)), var.get('Style').create(var.get('T'), Js(1.0), Js(False)), var.get('Style').create(var.get('Tc'), Js(1.0), Js(True)), var.get('Style').create(var.get('S'), Js(2.0), Js(False)), var.get('Style').create(var.get('Sc'), Js(2.0), Js(True)), var.get('Style').create(var.get('SS'), Js(3.0), Js(False)), var.get('Style').create(var.get('SSc'), Js(3.0), Js(True))]))
        var.put('_sup', Js([var.get('S'), var.get('Sc'), var.get('S'), var.get('Sc'), var.get('SS'), var.get('SSc'), var.get('SS'), var.get('SSc')]))
        var.put('_sub', Js([var.get('Sc'), var.get('Sc'), var.get('Sc'), var.get('Sc'), var.get('SSc'), var.get('SSc'), var.get('SSc'), var.get('SSc')]))
        var.put('_fracNum', Js([var.get('T'), var.get('Tc'), var.get('S'), var.get('Sc'), var.get('SS'), var.get('SSc'), var.get('SS'), var.get('SSc')]))
        var.put('_fracDen', Js([var.get('Tc'), var.get('Tc'), var.get('Sc'), var.get('Sc'), var.get('SSc'), var.get('SSc'), var.get('SSc'), var.get('SSc')]))
        var.put('_cramp', Js([var.get('Dc'), var.get('Dc'), var.get('Tc'), var.get('Tc'), var.get('Sc'), var.get('Sc'), var.get('SSc'), var.get('SSc')]))
        var.put('_text', Js([var.get('D'), var.get('Dc'), var.get('T'), var.get('Tc'), var.get('T'), var.get('Tc'), var.get('T'), var.get('Tc')]))
        var.put('src_Style', Js({'DISPLAY':var.get('Style_styles').get(var.get('D')),'TEXT':var.get('Style_styles').get(var.get('T')),'SCRIPT':var.get('Style_styles').get(var.get('S')),'SCRIPTSCRIPT':var.get('Style_styles').get(var.get('SS'))}))
        var.put('scriptData', Js([Js({'name':Js('latin'),'blocks':Js([Js([Js(256), Js(591)]), Js([Js(768), Js(879)])])}), Js({'name':Js('cyrillic'),'blocks':Js([Js([Js(1024), Js(1279)])])}), Js({'name':Js('brahmic'),'blocks':Js([Js([Js(2304), Js(4255)])])}), Js({'name':Js('georgian'),'blocks':Js([Js([Js(4256), Js(4351)])])}), Js({'name':Js('cjk'),'blocks':Js([Js([Js(12288), Js(12543)]), Js([Js(19968), Js(40879)]), Js([Js(65280), Js(65376)])])}), Js({'name':Js('hangul'),'blocks':Js([Js([Js(44032), Js(55215)])])})]))
        pass
        var.put('allBlocks', Js([]))
        @Js
        def PyJs_anonymous_26_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            @Js
            def PyJs_anonymous_27_(b, this, arguments, var=var):
                var = Scope({'b':b, 'this':this, 'arguments':arguments}, var)
                var.registers(['b'])
                return var.get('allBlocks').get('push').callprop('apply', var.get('allBlocks'), var.get('b'))
            PyJs_anonymous_27_._set_name('anonymous')
            return var.get('s').get('blocks').callprop('forEach', PyJs_anonymous_27_)
        PyJs_anonymous_26_._set_name('anonymous')
        var.get('scriptData').callprop('forEach', PyJs_anonymous_26_)
        pass
        var.put('hLinePad', Js(80.0))
        def PyJs_LONG_28_(var=var):
            return ((Js('M95,')+(Js(622.0)+var.get('hLinePad')))+Js('c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,\n-10,-9.5,-14c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54c44.2,-33.3,65.8,\n-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10s173,378,173,378c0.7,0,\n35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429c69,-144,104.5,-217.7,106.5,\n-221c5.3,-9.3,12,-14,20,-14H400000v40H845.2724s-225.272,467,-225.272,467\ns-235,486,-235,486c-2.7,4.7,-9,7,-19,7c-6,0,-10,-1,-12,-3s-194,-422,-194,-422\ns-65,47,-65,47z M834 '))
        def PyJs_LONG_29_(var=var):
            return ((Js('M263,')+(Js(601.0)+var.get('hLinePad')))+Js('c0.7,0,18,39.7,52,119c34,79.3,68.167,\n158.7,102.5,238c34.3,79.3,51.8,119.3,52.5,120c340,-704.7,510.7,-1060.3,512,-1067\nc4.7,-7.3,11,-11,19,-11H40000v40H1012.3s-271.3,567,-271.3,567c-38.7,80.7,-84,\n175,-136,283c-52,108,-89.167,185.3,-111.5,232c-22.3,46.7,-33.8,70.3,-34.5,71\nc-4.7,4.7,-12.3,7,-23,7s-12,-1,-12,-1s-109,-253,-109,-253c-72.7,-168,-109.3,\n-252,-110,-252c-10.7,8,-22,16.7,-34,26c-22,17.3,-33.3,26,-34,26s-26,-26,-26,-26\ns76,-59,76,-59s76,-60,76,-60z M1001 '))
        def PyJs_LONG_30_(var=var):
            return ((Js('M1001,')+var.get('hLinePad'))+Js('H400000v40H1013.1s-83.4,268,-264.1,840c-180.7,\n572,-277,876.3,-289,913c-4.7,4.7,-12.7,7,-24,7s-12,0,-12,0c-1.3,-3.3,-3.7,-11.7,\n-7,-25c-35.3,-125.3,-106.7,-373.3,-214,-744c-10,12,-21,25,-33,39s-32,39,-32,39\nc-6,-5.3,-15,-14,-27,-26s25,-30,25,-30c26.7,-32.7,52,-63,76,-91s52,-60,52,-60\ns208,722,208,722c56,-175.3,126.3,-397.3,211,-666c84.7,-268.7,153.8,-488.2,207.5,\n-658.5c53.7,-170.3,84.5,-266.8,92.5,-289.5c4,-6.7,10,-10,18,-10z\nM1001 '))
        def PyJs_LONG_31_(var=var):
            return ((Js('M424,')+(Js(2398.0)+var.get('hLinePad')))+Js('c-1.3,-0.7,-38.5,-172,-111.5,-514c-73,\n-342,-109.8,-513.3,-110.5,-514c0,-2,-10.7,14.3,-32,49c-4.7,7.3,-9.8,15.7,-15.5,\n25c-5.7,9.3,-9.8,16,-12.5,20s-5,7,-5,7c-4,-3.3,-8.3,-7.7,-13,-13s-13,-13,-13,\n-13s76,-122,76,-122s77,-121,77,-121s209,968,209,968c0,-2,84.7,-361.7,254,-1079\nc169.3,-717.3,254.7,-1077.7,256,-1081c4,-6.7,10,-10,18,-10H400000v40H1014.6\ns-87.3,378.7,-272.6,1166c-185.3,787.3,-279.3,1182.3,-282,1185c-2,6,-10,9,-24,9\nc-8,0,-12,-0.7,-12,-2z M1001 '))
        def PyJs_LONG_32_(var=var):
            return ((Js('M473,')+(Js(2713.0)+var.get('hLinePad')))+Js('c339.3,-1799.3,509.3,-2700,510,-2702\nc3.3,-7.3,9.3,-11,18,-11H400000v40H1017.7s-90.5,478,-276.2,1466c-185.7,988,\n-279.5,1483,-281.5,1485c-2,6,-10,9,-24,9c-8,0,-12,-0.7,-12,-2c0,-1.3,-5.3,-32,\n-16,-92c-50.7,-293.3,-119.7,-693.3,-207,-1200c0,-1.3,-5.3,8.7,-16,30c-10.7,\n21.3,-21.3,42.7,-32,64s-16,33,-16,33s-26,-26,-26,-26s76,-153,76,-153s77,-151,\n77,-151c0.7,0.7,35.7,202,105,604c67.3,400.7,102,602.7,104,606z\nM1001 '))
        var.put('svgGeometry_path', Js({'sqrtMain':((PyJs_LONG_28_()+var.get('hLinePad'))+Js('H400000v40H845z')),'sqrtSize1':((PyJs_LONG_29_()+var.get('hLinePad'))+Js('H40000v40H1012z')),'sqrtSize2':((PyJs_LONG_30_()+var.get('hLinePad'))+Js('H400000v40H1013z')),'sqrtSize3':((PyJs_LONG_31_()+var.get('hLinePad'))+Js('H400000v40H1014z')),'sqrtSize4':((PyJs_LONG_32_()+var.get('hLinePad'))+Js('H400000v40H1017z')),'doubleleftarrow':Js('M262 157\nl10-10c34-36 62.7-77 86-123 3.3-8 5-13.3 5-16 0-5.3-6.7-8-20-8-7.3\n 0-12.2.5-14.5 1.5-2.3 1-4.8 4.5-7.5 10.5-49.3 97.3-121.7 169.3-217 216-28\n 14-57.3 25-88 33-6.7 2-11 3.8-13 5.5-2 1.7-3 4.2-3 7.5s1 5.8 3 7.5\nc2 1.7 6.3 3.5 13 5.5 68 17.3 128.2 47.8 180.5 91.5 52.3 43.7 93.8 96.2 124.5\n 157.5 9.3 8 15.3 12.3 18 13h6c12-.7 18-4 18-10 0-2-1.7-7-5-15-23.3-46-52-87\n-86-123l-10-10h399738v-40H218c328 0 0 0 0 0l-10-8c-26.7-20-65.7-43-117-69 2.7\n-2 6-3.7 10-5 36.7-16 72.3-37.3 107-64l10-8h399782v-40z\nm8 0v40h399730v-40zm0 194v40h399730v-40z'),'doublerightarrow':Js('M399738 392l\n-10 10c-34 36-62.7 77-86 123-3.3 8-5 13.3-5 16 0 5.3 6.7 8 20 8 7.3 0 12.2-.5\n 14.5-1.5 2.3-1 4.8-4.5 7.5-10.5 49.3-97.3 121.7-169.3 217-216 28-14 57.3-25 88\n-33 6.7-2 11-3.8 13-5.5 2-1.7 3-4.2 3-7.5s-1-5.8-3-7.5c-2-1.7-6.3-3.5-13-5.5-68\n-17.3-128.2-47.8-180.5-91.5-52.3-43.7-93.8-96.2-124.5-157.5-9.3-8-15.3-12.3-18\n-13h-6c-12 .7-18 4-18 10 0 2 1.7 7 5 15 23.3 46 52 87 86 123l10 10H0v40h399782\nc-328 0 0 0 0 0l10 8c26.7 20 65.7 43 117 69-2.7 2-6 3.7-10 5-36.7 16-72.3 37.3\n-107 64l-10 8H0v40zM0 157v40h399730v-40zm0 194v40h399730v-40z'),'leftarrow':Js('M400000 241H110l3-3c68.7-52.7 113.7-120\n 135-202 4-14.7 6-23 6-25 0-7.3-7-11-21-11-8 0-13.2.8-15.5 2.5-2.3 1.7-4.2 5.8\n-5.5 12.5-1.3 4.7-2.7 10.3-4 17-12 48.7-34.8 92-68.5 130S65.3 228.3 18 247\nc-10 4-16 7.7-18 11 0 8.7 6 14.3 18 17 47.3 18.7 87.8 47 121.5 85S196 441.3 208\n 490c.7 2 1.3 5 2 9s1.2 6.7 1.5 8c.3 1.3 1 3.3 2 6s2.2 4.5 3.5 5.5c1.3 1 3.3\n 1.8 6 2.5s6 1 10 1c14 0 21-3.7 21-11 0-2-2-10.3-6-25-20-79.3-65-146.7-135-202\n l-3-3h399890zM100 241v40h399900v-40z'),'leftbrace':Js('M6 548l-6-6v-35l6-11c56-104 135.3-181.3 238-232 57.3-28.7 117\n-45 179-50h399577v120H403c-43.3 7-81 15-113 26-100.7 33-179.7 91-237 174-2.7\n 5-6 9-10 13-.7 1-7.3 1-20 1H6z'),'leftbraceunder':Js('M0 6l6-6h17c12.688 0 19.313.3 20 1 4 4 7.313 8.3 10 13\n 35.313 51.3 80.813 93.8 136.5 127.5 55.688 33.7 117.188 55.8 184.5 66.5.688\n 0 2 .3 4 1 18.688 2.7 76 4.3 172 5h399450v120H429l-6-1c-124.688-8-235-61.7\n-331-161C60.687 138.7 32.312 99.3 7 54L0 41V6z'),'leftgroup':Js('M400000 80\nH435C64 80 168.3 229.4 21 260c-5.9 1.2-18 0-18 0-2 0-3-1-3-3v-38C76 61 257 0\n 435 0h399565z'),'leftgroupunder':Js('M400000 262\nH435C64 262 168.3 112.6 21 82c-5.9-1.2-18 0-18 0-2 0-3 1-3 3v38c76 158 257 219\n 435 219h399565z'),'leftharpoon':Js('M0 267c.7 5.3 3 10 7 14h399993v-40H93c3.3\n-3.3 10.2-9.5 20.5-18.5s17.8-15.8 22.5-20.5c50.7-52 88-110.3 112-175 4-11.3 5\n-18.3 3-21-1.3-4-7.3-6-18-6-8 0-13 .7-15 2s-4.7 6.7-8 16c-42 98.7-107.3 174.7\n-196 228-6.7 4.7-10.7 8-12 10-1.3 2-2 5.7-2 11zm100-26v40h399900v-40z'),'leftharpoonplus':Js('M0 267c.7 5.3 3 10 7 14h399993v-40H93c3.3-3.3 10.2-9.5\n 20.5-18.5s17.8-15.8 22.5-20.5c50.7-52 88-110.3 112-175 4-11.3 5-18.3 3-21-1.3\n-4-7.3-6-18-6-8 0-13 .7-15 2s-4.7 6.7-8 16c-42 98.7-107.3 174.7-196 228-6.7 4.7\n-10.7 8-12 10-1.3 2-2 5.7-2 11zm100-26v40h399900v-40zM0 435v40h400000v-40z\nm0 0v40h400000v-40z'),'leftharpoondown':Js('M7 241c-4 4-6.333 8.667-7 14 0 5.333.667 9 2 11s5.333\n 5.333 12 10c90.667 54 156 130 196 228 3.333 10.667 6.333 16.333 9 17 2 .667 5\n 1 9 1h5c10.667 0 16.667-2 18-6 2-2.667 1-9.667-3-21-32-87.333-82.667-157.667\n-152-211l-3-3h399907v-40zM93 281 H400000 v-40L7 241z'),'leftharpoondownplus':Js('M7 435c-4 4-6.3 8.7-7 14 0 5.3.7 9 2 11s5.3 5.3 12\n 10c90.7 54 156 130 196 228 3.3 10.7 6.3 16.3 9 17 2 .7 5 1 9 1h5c10.7 0 16.7\n-2 18-6 2-2.7 1-9.7-3-21-32-87.3-82.7-157.7-152-211l-3-3h399907v-40H7zm93 0\nv40h399900v-40zM0 241v40h399900v-40zm0 0v40h399900v-40z'),'lefthook':Js('M400000 281 H103s-33-11.2-61-33.5S0 197.3 0 164s14.2-61.2 42.5\n-83.5C70.8 58.2 104 47 142 47 c16.7 0 25 6.7 25 20 0 12-8.7 18.7-26 20-40 3.3\n-68.7 15.7-86 37-10 12-15 25.3-15 40 0 22.7 9.8 40.7 29.5 54 19.7 13.3 43.5 21\n 71.5 23h399859zM103 281v-40h399897v40z'),'leftlinesegment':Js('M40 281 V428 H0 V94 H40 V241 H400000 v40z\nM40 281 V428 H0 V94 H40 V241 H400000 v40z'),'leftmapsto':Js('M40 281 V448H0V74H40V241H400000v40z\nM40 281 V448H0V74H40V241H400000v40z'),'leftToFrom':Js('M0 147h400000v40H0zm0 214c68 40 115.7 95.7 143 167h22c15.3 0 23\n-.3 23-1 0-1.3-5.3-13.7-16-37-18-35.3-41.3-69-70-101l-7-8h399905v-40H95l7-8\nc28.7-32 52-65.7 70-101 10.7-23.3 16-35.7 16-37 0-.7-7.7-1-23-1h-22C115.7 265.3\n 68 321 0 361zm0-174v-40h399900v40zm100 154v40h399900v-40z'),'longequal':Js('M0 50 h400000 v40H0z m0 194h40000v40H0z\nM0 50 h400000 v40H0z m0 194h40000v40H0z'),'midbrace':Js('M200428 334\nc-100.7-8.3-195.3-44-280-108-55.3-42-101.7-93-139-153l-9-14c-2.7 4-5.7 8.7-9 14\n-53.3 86.7-123.7 153-211 199-66.7 36-137.3 56.3-212 62H0V214h199568c178.3-11.7\n 311.7-78.3 403-201 6-8 9.7-12 11-12 .7-.7 6.7-1 18-1s17.3.3 18 1c1.3 0 5 4 11\n 12 44.7 59.3 101.3 106.3 170 141s145.3 54.3 229 60h199572v120z'),'midbraceunder':Js('M199572 214\nc100.7 8.3 195.3 44 280 108 55.3 42 101.7 93 139 153l9 14c2.7-4 5.7-8.7 9-14\n 53.3-86.7 123.7-153 211-199 66.7-36 137.3-56.3 212-62h199568v120H200432c-178.3\n 11.7-311.7 78.3-403 201-6 8-9.7 12-11 12-.7.7-6.7 1-18 1s-17.3-.3-18-1c-1.3 0\n-5-4-11-12-44.7-59.3-101.3-106.3-170-141s-145.3-54.3-229-60H0V214z'),'oiintSize1':Js('M512.6 71.6c272.6 0 320.3 106.8 320.3 178.2 0 70.8-47.7 177.6\n-320.3 177.6S193.1 320.6 193.1 249.8c0-71.4 46.9-178.2 319.5-178.2z\nm368.1 178.2c0-86.4-60.9-215.4-368.1-215.4-306.4 0-367.3 129-367.3 215.4 0 85.8\n60.9 214.8 367.3 214.8 307.2 0 368.1-129 368.1-214.8z'),'oiintSize2':Js('M757.8 100.1c384.7 0 451.1 137.6 451.1 230 0 91.3-66.4 228.8\n-451.1 228.8-386.3 0-452.7-137.5-452.7-228.8 0-92.4 66.4-230 452.7-230z\nm502.4 230c0-111.2-82.4-277.2-502.4-277.2s-504 166-504 277.2\nc0 110 84 276 504 276s502.4-166 502.4-276z'),'oiiintSize1':Js('M681.4 71.6c408.9 0 480.5 106.8 480.5 178.2 0 70.8-71.6 177.6\n-480.5 177.6S202.1 320.6 202.1 249.8c0-71.4 70.5-178.2 479.3-178.2z\nm525.8 178.2c0-86.4-86.8-215.4-525.7-215.4-437.9 0-524.7 129-524.7 215.4 0\n85.8 86.8 214.8 524.7 214.8 438.9 0 525.7-129 525.7-214.8z'),'oiiintSize2':Js('M1021.2 53c603.6 0 707.8 165.8 707.8 277.2 0 110-104.2 275.8\n-707.8 275.8-606 0-710.2-165.8-710.2-275.8C311 218.8 415.2 53 1021.2 53z\nm770.4 277.1c0-131.2-126.4-327.6-770.5-327.6S248.4 198.9 248.4 330.1\nc0 130 128.8 326.4 772.7 326.4s770.5-196.4 770.5-326.4z'),'rightarrow':Js('M0 241v40h399891c-47.3 35.3-84 78-110 128\n-16.7 32-27.7 63.7-33 95 0 1.3-.2 2.7-.5 4-.3 1.3-.5 2.3-.5 3 0 7.3 6.7 11 20\n 11 8 0 13.2-.8 15.5-2.5 2.3-1.7 4.2-5.5 5.5-11.5 2-13.3 5.7-27 11-41 14.7-44.7\n 39-84.5 73-119.5s73.7-60.2 119-75.5c6-2 9-5.7 9-11s-3-9-9-11c-45.3-15.3-85\n-40.5-119-75.5s-58.3-74.8-73-119.5c-4.7-14-8.3-27.3-11-40-1.3-6.7-3.2-10.8-5.5\n-12.5-2.3-1.7-7.5-2.5-15.5-2.5-14 0-21 3.7-21 11 0 2 2 10.3 6 25 20.7 83.3 67\n 151.7 139 205zm0 0v40h399900v-40z'),'rightbrace':Js('M400000 542l\n-6 6h-17c-12.7 0-19.3-.3-20-1-4-4-7.3-8.3-10-13-35.3-51.3-80.8-93.8-136.5-127.5\ns-117.2-55.8-184.5-66.5c-.7 0-2-.3-4-1-18.7-2.7-76-4.3-172-5H0V214h399571l6 1\nc124.7 8 235 61.7 331 161 31.3 33.3 59.7 72.7 85 118l7 13v35z'),'rightbraceunder':Js('M399994 0l6 6v35l-6 11c-56 104-135.3 181.3-238 232-57.3\n 28.7-117 45-179 50H-300V214h399897c43.3-7 81-15 113-26 100.7-33 179.7-91 237\n-174 2.7-5 6-9 10-13 .7-1 7.3-1 20-1h17z'),'rightgroup':Js('M0 80h399565c371 0 266.7 149.4 414 180 5.9 1.2 18 0 18 0 2 0\n 3-1 3-3v-38c-76-158-257-219-435-219H0z'),'rightgroupunder':Js('M0 262h399565c371 0 266.7-149.4 414-180 5.9-1.2 18 0 18\n 0 2 0 3 1 3 3v38c-76 158-257 219-435 219H0z'),'rightharpoon':Js('M0 241v40h399993c4.7-4.7 7-9.3 7-14 0-9.3\n-3.7-15.3-11-18-92.7-56.7-159-133.7-199-231-3.3-9.3-6-14.7-8-16-2-1.3-7-2-15-2\n-10.7 0-16.7 2-18 6-2 2.7-1 9.7 3 21 15.3 42 36.7 81.8 64 119.5 27.3 37.7 58\n 69.2 92 94.5zm0 0v40h399900v-40z'),'rightharpoonplus':Js('M0 241v40h399993c4.7-4.7 7-9.3 7-14 0-9.3-3.7-15.3-11\n-18-92.7-56.7-159-133.7-199-231-3.3-9.3-6-14.7-8-16-2-1.3-7-2-15-2-10.7 0-16.7\n 2-18 6-2 2.7-1 9.7 3 21 15.3 42 36.7 81.8 64 119.5 27.3 37.7 58 69.2 92 94.5z\nm0 0v40h399900v-40z m100 194v40h399900v-40zm0 0v40h399900v-40z'),'rightharpoondown':Js('M399747 511c0 7.3 6.7 11 20 11 8 0 13-.8 15-2.5s4.7-6.8\n 8-15.5c40-94 99.3-166.3 178-217 13.3-8 20.3-12.3 21-13 5.3-3.3 8.5-5.8 9.5\n-7.5 1-1.7 1.5-5.2 1.5-10.5s-2.3-10.3-7-15H0v40h399908c-34 25.3-64.7 57-92 95\n-27.3 38-48.7 77.7-64 119-3.3 8.7-5 14-5 16zM0 241v40h399900v-40z'),'rightharpoondownplus':Js('M399747 705c0 7.3 6.7 11 20 11 8 0 13-.8\n 15-2.5s4.7-6.8 8-15.5c40-94 99.3-166.3 178-217 13.3-8 20.3-12.3 21-13 5.3-3.3\n 8.5-5.8 9.5-7.5 1-1.7 1.5-5.2 1.5-10.5s-2.3-10.3-7-15H0v40h399908c-34 25.3\n-64.7 57-92 95-27.3 38-48.7 77.7-64 119-3.3 8.7-5 14-5 16zM0 435v40h399900v-40z\nm0-194v40h400000v-40zm0 0v40h400000v-40z'),'righthook':Js('M399859 241c-764 0 0 0 0 0 40-3.3 68.7-15.7 86-37 10-12 15-25.3\n 15-40 0-22.7-9.8-40.7-29.5-54-19.7-13.3-43.5-21-71.5-23-17.3-1.3-26-8-26-20 0\n-13.3 8.7-20 26-20 38 0 71 11.2 99 33.5 0 0 7 5.6 21 16.7 14 11.2 21 33.5 21\n 66.8s-14 61.2-42 83.5c-28 22.3-61 33.5-99 33.5L0 241z M0 281v-40h399859v40z'),'rightlinesegment':Js('M399960 241 V94 h40 V428 h-40 V281 H0 v-40z\nM399960 241 V94 h40 V428 h-40 V281 H0 v-40z'),'rightToFrom':Js('M400000 167c-70.7-42-118-97.7-142-167h-23c-15.3 0-23 .3-23\n 1 0 1.3 5.3 13.7 16 37 18 35.3 41.3 69 70 101l7 8H0v40h399905l-7 8c-28.7 32\n-52 65.7-70 101-10.7 23.3-16 35.7-16 37 0 .7 7.7 1 23 1h23c24-69.3 71.3-125 142\n-167z M100 147v40h399900v-40zM0 341v40h399900v-40z'),'twoheadleftarrow':Js('M0 167c68 40\n 115.7 95.7 143 167h22c15.3 0 23-.3 23-1 0-1.3-5.3-13.7-16-37-18-35.3-41.3-69\n-70-101l-7-8h125l9 7c50.7 39.3 85 86 103 140h46c0-4.7-6.3-18.7-19-42-18-35.3\n-40-67.3-66-96l-9-9h399716v-40H284l9-9c26-28.7 48-60.7 66-96 12.7-23.333 19\n-37.333 19-42h-46c-18 54-52.3 100.7-103 140l-9 7H95l7-8c28.7-32 52-65.7 70-101\n 10.7-23.333 16-35.7 16-37 0-.7-7.7-1-23-1h-22C115.7 71.3 68 127 0 167z'),'twoheadrightarrow':Js('M400000 167\nc-68-40-115.7-95.7-143-167h-22c-15.3 0-23 .3-23 1 0 1.3 5.3 13.7 16 37 18 35.3\n 41.3 69 70 101l7 8h-125l-9-7c-50.7-39.3-85-86-103-140h-46c0 4.7 6.3 18.7 19 42\n 18 35.3 40 67.3 66 96l9 9H0v40h399716l-9 9c-26 28.7-48 60.7-66 96-12.7 23.333\n-19 37.333-19 42h46c18-54 52.3-100.7 103-140l9-7h125l-7 8c-28.7 32-52 65.7-70\n 101-10.7 23.333-16 35.7-16 37 0 .7 7.7 1 23 1h22c27.3-71.3 75-127 143-167z'),'tilde1':Js('M200 55.538c-77 0-168 73.953-177 73.953-3 0-7\n-2.175-9-5.437L2 97c-1-2-2-4-2-6 0-4 2-7 5-9l20-12C116 12 171 0 207 0c86 0\n 114 68 191 68 78 0 168-68 177-68 4 0 7 2 9 5l12 19c1 2.175 2 4.35 2 6.525 0\n 4.35-2 7.613-5 9.788l-19 13.05c-92 63.077-116.937 75.308-183 76.128\n-68.267.847-113-73.952-191-73.952z'),'tilde2':Js('M344 55.266c-142 0-300.638 81.316-311.5 86.418\n-8.01 3.762-22.5 10.91-23.5 5.562L1 120c-1-2-1-3-1-4 0-5 3-9 8-10l18.4-9C160.9\n 31.9 283 0 358 0c148 0 188 122 331 122s314-97 326-97c4 0 8 2 10 7l7 21.114\nc1 2.14 1 3.21 1 4.28 0 5.347-3 9.626-7 10.696l-22.3 12.622C852.6 158.372 751\n 181.476 676 181.476c-149 0-189-126.21-332-126.21z'),'tilde3':Js('M786 59C457 59 32 175.242 13 175.242c-6 0-10-3.457\n-11-10.37L.15 138c-1-7 3-12 10-13l19.2-6.4C378.4 40.7 634.3 0 804.3 0c337 0\n 411.8 157 746.8 157 328 0 754-112 773-112 5 0 10 3 11 9l1 14.075c1 8.066-.697\n 16.595-6.697 17.492l-21.052 7.31c-367.9 98.146-609.15 122.696-778.15 122.696\n -338 0-409-156.573-744-156.573z'),'tilde4':Js('M786 58C457 58 32 177.487 13 177.487c-6 0-10-3.345\n-11-10.035L.15 143c-1-7 3-12 10-13l22-6.7C381.2 35 637.15 0 807.15 0c337 0 409\n 177 744 177 328 0 754-127 773-127 5 0 10 3 11 9l1 14.794c1 7.805-3 13.38-9\n 14.495l-20.7 5.574c-366.85 99.79-607.3 139.372-776.3 139.372-338 0-409\n -175.236-744-175.236z'),'vec':Js('M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5\n3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11\n10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63\n-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1\n-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59\nH213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359\nc-16-25.333-24-45-24-59z'),'widehat1':Js('M529 0h5l519 115c5 1 9 5 9 10 0 1-1 2-1 3l-4 22\nc-1 5-5 9-11 9h-2L532 67 19 159h-2c-5 0-9-4-11-9l-5-22c-1-6 2-12 8-13z'),'widehat2':Js('M1181 0h2l1171 176c6 0 10 5 10 11l-2 23c-1 6-5 10\n-11 10h-1L1182 67 15 220h-1c-6 0-10-4-11-10l-2-23c-1-6 4-11 10-11z'),'widehat3':Js('M1181 0h2l1171 236c6 0 10 5 10 11l-2 23c-1 6-5 10\n-11 10h-1L1182 67 15 280h-1c-6 0-10-4-11-10l-2-23c-1-6 4-11 10-11z'),'widehat4':Js('M1181 0h2l1171 296c6 0 10 5 10 11l-2 23c-1 6-5 10\n-11 10h-1L1182 67 15 340h-1c-6 0-10-4-11-10l-2-23c-1-6 4-11 10-11z'),'widecheck1':Js('M529,159h5l519,-115c5,-1,9,-5,9,-10c0,-1,-1,-2,-1,-3l-4,-22c-1,\n-5,-5,-9,-11,-9h-2l-512,92l-513,-92h-2c-5,0,-9,4,-11,9l-5,22c-1,6,2,12,8,13z'),'widecheck2':Js('M1181,220h2l1171,-176c6,0,10,-5,10,-11l-2,-23c-1,-6,-5,-10,\n-11,-10h-1l-1168,153l-1167,-153h-1c-6,0,-10,4,-11,10l-2,23c-1,6,4,11,10,11z'),'widecheck3':Js('M1181,280h2l1171,-236c6,0,10,-5,10,-11l-2,-23c-1,-6,-5,-10,\n-11,-10h-1l-1168,213l-1167,-213h-1c-6,0,-10,4,-11,10l-2,23c-1,6,4,11,10,11z'),'widecheck4':Js('M1181,340h2l1171,-296c6,0,10,-5,10,-11l-2,-23c-1,-6,-5,-10,\n-11,-10h-1l-1168,273l-1167,-273h-1c-6,0,-10,4,-11,10l-2,23c-1,6,4,11,10,11z'),'baraboveleftarrow':Js('M400000 620h-399890l3 -3c68.7 -52.7 113.7 -120 135 -202\nc4 -14.7 6 -23 6 -25c0 -7.3 -7 -11 -21 -11c-8 0 -13.2 0.8 -15.5 2.5\nc-2.3 1.7 -4.2 5.8 -5.5 12.5c-1.3 4.7 -2.7 10.3 -4 17c-12 48.7 -34.8 92 -68.5 130\ns-74.2 66.3 -121.5 85c-10 4 -16 7.7 -18 11c0 8.7 6 14.3 18 17c47.3 18.7 87.8 47\n121.5 85s56.5 81.3 68.5 130c0.7 2 1.3 5 2 9s1.2 6.7 1.5 8c0.3 1.3 1 3.3 2 6\ns2.2 4.5 3.5 5.5c1.3 1 3.3 1.8 6 2.5s6 1 10 1c14 0 21 -3.7 21 -11\nc0 -2 -2 -10.3 -6 -25c-20 -79.3 -65 -146.7 -135 -202l-3 -3h399890z\nM100 620v40h399900v-40z M0 241v40h399900v-40zM0 241v40h399900v-40z'),'rightarrowabovebar':Js('M0 241v40h399891c-47.3 35.3-84 78-110 128-16.7 32\n-27.7 63.7-33 95 0 1.3-.2 2.7-.5 4-.3 1.3-.5 2.3-.5 3 0 7.3 6.7 11 20 11 8 0\n13.2-.8 15.5-2.5 2.3-1.7 4.2-5.5 5.5-11.5 2-13.3 5.7-27 11-41 14.7-44.7 39\n-84.5 73-119.5s73.7-60.2 119-75.5c6-2 9-5.7 9-11s-3-9-9-11c-45.3-15.3-85-40.5\n-119-75.5s-58.3-74.8-73-119.5c-4.7-14-8.3-27.3-11-40-1.3-6.7-3.2-10.8-5.5\n-12.5-2.3-1.7-7.5-2.5-15.5-2.5-14 0-21 3.7-21 11 0 2 2 10.3 6 25 20.7 83.3 67\n151.7 139 205zm96 379h399894v40H0zm0 0h399904v40H0z'),'baraboveshortleftharpoon':Js('M507,435c-4,4,-6.3,8.7,-7,14c0,5.3,0.7,9,2,11\nc1.3,2,5.3,5.3,12,10c90.7,54,156,130,196,228c3.3,10.7,6.3,16.3,9,17\nc2,0.7,5,1,9,1c0,0,5,0,5,0c10.7,0,16.7,-2,18,-6c2,-2.7,1,-9.7,-3,-21\nc-32,-87.3,-82.7,-157.7,-152,-211c0,0,-3,-3,-3,-3l399351,0l0,-40\nc-398570,0,-399437,0,-399437,0z M593 435 v40 H399500 v-40z\nM0 281 v-40 H399908 v40z M0 281 v-40 H399908 v40z'),'rightharpoonaboveshortbar':Js('M0,241 l0,40c399126,0,399993,0,399993,0\nc4.7,-4.7,7,-9.3,7,-14c0,-9.3,-3.7,-15.3,-11,-18c-92.7,-56.7,-159,-133.7,-199,\n-231c-3.3,-9.3,-6,-14.7,-8,-16c-2,-1.3,-7,-2,-15,-2c-10.7,0,-16.7,2,-18,6\nc-2,2.7,-1,9.7,3,21c15.3,42,36.7,81.8,64,119.5c27.3,37.7,58,69.2,92,94.5z\nM0 241 v40 H399908 v-40z M0 475 v-40 H399500 v40z M0 475 v-40 H399500 v40z'),'shortbaraboveleftharpoon':Js('M7,435c-4,4,-6.3,8.7,-7,14c0,5.3,0.7,9,2,11\nc1.3,2,5.3,5.3,12,10c90.7,54,156,130,196,228c3.3,10.7,6.3,16.3,9,17c2,0.7,5,1,9,\n1c0,0,5,0,5,0c10.7,0,16.7,-2,18,-6c2,-2.7,1,-9.7,-3,-21c-32,-87.3,-82.7,-157.7,\n-152,-211c0,0,-3,-3,-3,-3l399907,0l0,-40c-399126,0,-399993,0,-399993,0z\nM93 435 v40 H400000 v-40z M500 241 v40 H400000 v-40z M500 241 v40 H400000 v-40z'),'shortrightharpoonabovebar':Js('M53,241l0,40c398570,0,399437,0,399437,0\nc4.7,-4.7,7,-9.3,7,-14c0,-9.3,-3.7,-15.3,-11,-18c-92.7,-56.7,-159,-133.7,-199,\n-231c-3.3,-9.3,-6,-14.7,-8,-16c-2,-1.3,-7,-2,-15,-2c-10.7,0,-16.7,2,-18,6\nc-2,2.7,-1,9.7,3,21c15.3,42,36.7,81.8,64,119.5c27.3,37.7,58,69.2,92,94.5z\nM500 241 v40 H399408 v-40z M500 435 v40 H400000 v-40z')}))
        var.put('svgGeometry', Js({'path':var.get('svgGeometry_path')}))
        @Js
        def PyJs_anonymous_33_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['_proto', 'DocumentFragment'])
            @Js
            def PyJsHoisted_DocumentFragment_(children, this, arguments, var=var):
                var = Scope({'children':children, 'this':this, 'arguments':arguments}, var)
                var.registers(['children'])
                var.get(u"this").put('children', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('classes', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('height', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('depth', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('maxFontSize', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('style', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('children', var.get('children'))
                var.get(u"this").put('classes', Js([]))
                var.get(u"this").put('height', Js(0.0))
                var.get(u"this").put('depth', Js(0.0))
                var.get(u"this").put('maxFontSize', Js(0.0))
                var.get(u"this").put('style', Js({}))
            PyJsHoisted_DocumentFragment_.func_name = 'DocumentFragment'
            var.put('DocumentFragment', PyJsHoisted_DocumentFragment_)
            pass
            var.put('_proto', var.get('DocumentFragment').get('prototype'))
            @Js
            def PyJs_hasClass_34_(className, this, arguments, var=var):
                var = Scope({'className':className, 'this':this, 'arguments':arguments, 'hasClass':PyJs_hasClass_34_}, var)
                var.registers(['className'])
                return var.get('utils').callprop('contains', var.get(u"this").get('classes'), var.get('className'))
            PyJs_hasClass_34_._set_name('hasClass')
            var.get('_proto').put('hasClass', PyJs_hasClass_34_)
            @Js
            def PyJs_toNode_35_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toNode':PyJs_toNode_35_}, var)
                var.registers(['frag', 'i'])
                var.put('frag', var.get('document').callprop('createDocumentFragment'))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get(u"this").get('children').get('length')):
                    try:
                        var.get('frag').callprop('appendChild', var.get(u"this").get('children').get(var.get('i')).callprop('toNode'))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                return var.get('frag')
            PyJs_toNode_35_._set_name('toNode')
            var.get('_proto').put('toNode', PyJs_toNode_35_)
            @Js
            def PyJs_toMarkup_36_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toMarkup':PyJs_toMarkup_36_}, var)
                var.registers(['i', 'markup'])
                var.put('markup', Js(''))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get(u"this").get('children').get('length')):
                    try:
                        var.put('markup', var.get(u"this").get('children').get(var.get('i')).callprop('toMarkup'), '+')
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                return var.get('markup')
            PyJs_toMarkup_36_._set_name('toMarkup')
            var.get('_proto').put('toMarkup', PyJs_toMarkup_36_)
            @Js
            def PyJs_toText_37_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toText':PyJs_toText_37_}, var)
                var.registers(['toText'])
                @Js
                def PyJs_toText_38_(child, this, arguments, var=var):
                    var = Scope({'child':child, 'this':this, 'arguments':arguments, 'toText':PyJs_toText_38_}, var)
                    var.registers(['child'])
                    return var.get('child').callprop('toText')
                PyJs_toText_38_._set_name('toText')
                var.put('toText', PyJs_toText_38_)
                return var.get(u"this").get('children').callprop('map', var.get('toText')).callprop('join', Js(''))
            PyJs_toText_37_._set_name('toText')
            var.get('_proto').put('toText', PyJs_toText_37_)
            return var.get('DocumentFragment')
        PyJs_anonymous_33_._set_name('anonymous')
        var.put('tree_DocumentFragment', PyJs_anonymous_33_())
        @Js
        def PyJs_createClass_39_(classes, this, arguments, var=var):
            var = Scope({'classes':classes, 'this':this, 'arguments':arguments, 'createClass':PyJs_createClass_39_}, var)
            var.registers(['classes'])
            @Js
            def PyJs_anonymous_40_(cls, this, arguments, var=var):
                var = Scope({'cls':cls, 'this':this, 'arguments':arguments}, var)
                var.registers(['cls'])
                return var.get('cls')
            PyJs_anonymous_40_._set_name('anonymous')
            return var.get('classes').callprop('filter', PyJs_anonymous_40_).callprop('join', Js(' '))
        PyJs_createClass_39_._set_name('createClass')
        var.put('createClass', PyJs_createClass_39_)
        @Js
        def PyJs_initNode_41_(classes, options, style, this, arguments, var=var):
            var = Scope({'classes':classes, 'options':options, 'style':style, 'this':this, 'arguments':arguments, 'initNode':PyJs_initNode_41_}, var)
            var.registers(['color', 'options', 'style', 'classes'])
            var.get(u"this").put('classes', (var.get('classes') or Js([])))
            var.get(u"this").put('attributes', Js({}))
            var.get(u"this").put('height', Js(0.0))
            var.get(u"this").put('depth', Js(0.0))
            var.get(u"this").put('maxFontSize', Js(0.0))
            var.get(u"this").put('style', (var.get('style') or Js({})))
            if var.get('options'):
                if var.get('options').get('style').callprop('isTight'):
                    var.get(u"this").get('classes').callprop('push', Js('mtight'))
                var.put('color', var.get('options').callprop('getColor'))
                if var.get('color'):
                    var.get(u"this").get('style').put('color', var.get('color'))
        PyJs_initNode_41_._set_name('initNode')
        var.put('initNode', PyJs_initNode_41_)
        @Js
        def PyJs_toNode_42_(tagName, this, arguments, var=var):
            var = Scope({'tagName':tagName, 'this':this, 'arguments':arguments, 'toNode':PyJs_toNode_42_}, var)
            var.registers(['i', 'node', 'tagName', 'style', 'attr'])
            var.put('node', var.get('document').callprop('createElement', var.get('tagName')))
            var.get('node').put('className', var.get('createClass')(var.get(u"this").get('classes')))
            for PyJsTemp in var.get(u"this").get('style'):
                var.put('style', PyJsTemp)
                if var.get(u"this").get('style').callprop('hasOwnProperty', var.get('style')):
                    var.get('node').get('style').put(var.get('style'), var.get(u"this").get('style').get(var.get('style')))
            for PyJsTemp in var.get(u"this").get('attributes'):
                var.put('attr', PyJsTemp)
                if var.get(u"this").get('attributes').callprop('hasOwnProperty', var.get('attr')):
                    var.get('node').callprop('setAttribute', var.get('attr'), var.get(u"this").get('attributes').get(var.get('attr')))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get(u"this").get('children').get('length')):
                try:
                    var.get('node').callprop('appendChild', var.get(u"this").get('children').get(var.get('i')).callprop('toNode'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            return var.get('node')
        PyJs_toNode_42_._set_name('toNode')
        var.put('_toNode', PyJs_toNode_42_)
        @Js
        def PyJs_toMarkup_43_(tagName, this, arguments, var=var):
            var = Scope({'tagName':tagName, 'this':this, 'arguments':arguments, 'toMarkup':PyJs_toMarkup_43_}, var)
            var.registers(['i', 'tagName', 'style', 'markup', 'attr', 'styles'])
            var.put('markup', (Js('<')+var.get('tagName')))
            if var.get(u"this").get('classes').get('length'):
                var.put('markup', ((Js(' class="')+var.get('utils').callprop('escape', var.get('createClass')(var.get(u"this").get('classes'))))+Js('"')), '+')
            var.put('styles', Js(''))
            for PyJsTemp in var.get(u"this").get('style'):
                var.put('style', PyJsTemp)
                if var.get(u"this").get('style').callprop('hasOwnProperty', var.get('style')):
                    var.put('styles', (((var.get('utils').callprop('hyphenate', var.get('style'))+Js(':'))+var.get(u"this").get('style').get(var.get('style')))+Js(';')), '+')
            if var.get('styles'):
                var.put('markup', ((Js(' style="')+var.get('utils').callprop('escape', var.get('styles')))+Js('"')), '+')
            for PyJsTemp in var.get(u"this").get('attributes'):
                var.put('attr', PyJsTemp)
                if var.get(u"this").get('attributes').callprop('hasOwnProperty', var.get('attr')):
                    var.put('markup', ((((Js(' ')+var.get('attr'))+Js('="'))+var.get('utils').callprop('escape', var.get(u"this").get('attributes').get(var.get('attr'))))+Js('"')), '+')
            var.put('markup', Js('>'), '+')
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get(u"this").get('children').get('length')):
                try:
                    var.put('markup', var.get(u"this").get('children').get(var.get('i')).callprop('toMarkup'), '+')
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('markup', ((Js('</')+var.get('tagName'))+Js('>')), '+')
            return var.get('markup')
        PyJs_toMarkup_43_._set_name('toMarkup')
        var.put('_toMarkup', PyJs_toMarkup_43_)
        @Js
        def PyJs_anonymous_44_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['_proto', 'Span'])
            @Js
            def PyJsHoisted_Span_(classes, children, options, style, this, arguments, var=var):
                var = Scope({'classes':classes, 'children':children, 'options':options, 'style':style, 'this':this, 'arguments':arguments}, var)
                var.registers(['options', 'style', 'classes', 'children'])
                var.get(u"this").put('children', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('attributes', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('classes', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('height', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('depth', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('width', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('maxFontSize', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('style', PyJsComma(Js(0.0), Js(None)))
                var.get('initNode').callprop('call', var.get(u"this"), var.get('classes'), var.get('options'), var.get('style'))
                var.get(u"this").put('children', (var.get('children') or Js([])))
            PyJsHoisted_Span_.func_name = 'Span'
            var.put('Span', PyJsHoisted_Span_)
            pass
            var.put('_proto', var.get('Span').get('prototype'))
            @Js
            def PyJs_setAttribute_45_(attribute, value, this, arguments, var=var):
                var = Scope({'attribute':attribute, 'value':value, 'this':this, 'arguments':arguments, 'setAttribute':PyJs_setAttribute_45_}, var)
                var.registers(['attribute', 'value'])
                var.get(u"this").get('attributes').put(var.get('attribute'), var.get('value'))
            PyJs_setAttribute_45_._set_name('setAttribute')
            var.get('_proto').put('setAttribute', PyJs_setAttribute_45_)
            @Js
            def PyJs_hasClass_46_(className, this, arguments, var=var):
                var = Scope({'className':className, 'this':this, 'arguments':arguments, 'hasClass':PyJs_hasClass_46_}, var)
                var.registers(['className'])
                return var.get('utils').callprop('contains', var.get(u"this").get('classes'), var.get('className'))
            PyJs_hasClass_46_._set_name('hasClass')
            var.get('_proto').put('hasClass', PyJs_hasClass_46_)
            @Js
            def PyJs_toNode_47_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toNode':PyJs_toNode_47_}, var)
                var.registers([])
                return var.get('_toNode').callprop('call', var.get(u"this"), Js('span'))
            PyJs_toNode_47_._set_name('toNode')
            var.get('_proto').put('toNode', PyJs_toNode_47_)
            @Js
            def PyJs_toMarkup_48_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toMarkup':PyJs_toMarkup_48_}, var)
                var.registers([])
                return var.get('_toMarkup').callprop('call', var.get(u"this"), Js('span'))
            PyJs_toMarkup_48_._set_name('toMarkup')
            var.get('_proto').put('toMarkup', PyJs_toMarkup_48_)
            return var.get('Span')
        PyJs_anonymous_44_._set_name('anonymous')
        var.put('domTree_Span', PyJs_anonymous_44_())
        @Js
        def PyJs_anonymous_49_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['Anchor', '_proto2'])
            @Js
            def PyJsHoisted_Anchor_(href, classes, children, options, this, arguments, var=var):
                var = Scope({'href':href, 'classes':classes, 'children':children, 'options':options, 'this':this, 'arguments':arguments}, var)
                var.registers(['options', 'classes', 'href', 'children'])
                var.get(u"this").put('children', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('attributes', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('classes', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('height', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('depth', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('maxFontSize', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('style', PyJsComma(Js(0.0), Js(None)))
                var.get('initNode').callprop('call', var.get(u"this"), var.get('classes'), var.get('options'))
                var.get(u"this").put('children', (var.get('children') or Js([])))
                var.get(u"this").callprop('setAttribute', Js('href'), var.get('href'))
            PyJsHoisted_Anchor_.func_name = 'Anchor'
            var.put('Anchor', PyJsHoisted_Anchor_)
            pass
            var.put('_proto2', var.get('Anchor').get('prototype'))
            @Js
            def PyJs_setAttribute_50_(attribute, value, this, arguments, var=var):
                var = Scope({'attribute':attribute, 'value':value, 'this':this, 'arguments':arguments, 'setAttribute':PyJs_setAttribute_50_}, var)
                var.registers(['attribute', 'value'])
                var.get(u"this").get('attributes').put(var.get('attribute'), var.get('value'))
            PyJs_setAttribute_50_._set_name('setAttribute')
            var.get('_proto2').put('setAttribute', PyJs_setAttribute_50_)
            @Js
            def PyJs_hasClass_51_(className, this, arguments, var=var):
                var = Scope({'className':className, 'this':this, 'arguments':arguments, 'hasClass':PyJs_hasClass_51_}, var)
                var.registers(['className'])
                return var.get('utils').callprop('contains', var.get(u"this").get('classes'), var.get('className'))
            PyJs_hasClass_51_._set_name('hasClass')
            var.get('_proto2').put('hasClass', PyJs_hasClass_51_)
            @Js
            def PyJs_toNode_52_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toNode':PyJs_toNode_52_}, var)
                var.registers([])
                return var.get('_toNode').callprop('call', var.get(u"this"), Js('a'))
            PyJs_toNode_52_._set_name('toNode')
            var.get('_proto2').put('toNode', PyJs_toNode_52_)
            @Js
            def PyJs_toMarkup_53_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toMarkup':PyJs_toMarkup_53_}, var)
                var.registers([])
                return var.get('_toMarkup').callprop('call', var.get(u"this"), Js('a'))
            PyJs_toMarkup_53_._set_name('toMarkup')
            var.get('_proto2').put('toMarkup', PyJs_toMarkup_53_)
            return var.get('Anchor')
        PyJs_anonymous_49_._set_name('anonymous')
        var.put('domTree_Anchor', PyJs_anonymous_49_())
        @Js
        def PyJs_anonymous_54_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['Img', '_proto3'])
            @Js
            def PyJsHoisted_Img_(src, alt, style, this, arguments, var=var):
                var = Scope({'src':src, 'alt':alt, 'style':style, 'this':this, 'arguments':arguments}, var)
                var.registers(['style', 'alt', 'src'])
                var.get(u"this").put('src', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('alt', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('classes', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('height', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('depth', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('maxFontSize', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('style', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('alt', var.get('alt'))
                var.get(u"this").put('src', var.get('src'))
                var.get(u"this").put('classes', Js([Js('mord')]))
                var.get(u"this").put('style', var.get('style'))
            PyJsHoisted_Img_.func_name = 'Img'
            var.put('Img', PyJsHoisted_Img_)
            pass
            var.put('_proto3', var.get('Img').get('prototype'))
            @Js
            def PyJs_hasClass_55_(className, this, arguments, var=var):
                var = Scope({'className':className, 'this':this, 'arguments':arguments, 'hasClass':PyJs_hasClass_55_}, var)
                var.registers(['className'])
                return var.get('utils').callprop('contains', var.get(u"this").get('classes'), var.get('className'))
            PyJs_hasClass_55_._set_name('hasClass')
            var.get('_proto3').put('hasClass', PyJs_hasClass_55_)
            @Js
            def PyJs_toNode_56_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toNode':PyJs_toNode_56_}, var)
                var.registers(['node', 'style'])
                var.put('node', var.get('document').callprop('createElement', Js('img')))
                var.get('node').put('src', var.get(u"this").get('src'))
                var.get('node').put('alt', var.get(u"this").get('alt'))
                var.get('node').put('className', Js('mord'))
                for PyJsTemp in var.get(u"this").get('style'):
                    var.put('style', PyJsTemp)
                    if var.get(u"this").get('style').callprop('hasOwnProperty', var.get('style')):
                        var.get('node').get('style').put(var.get('style'), var.get(u"this").get('style').get(var.get('style')))
                return var.get('node')
            PyJs_toNode_56_._set_name('toNode')
            var.get('_proto3').put('toNode', PyJs_toNode_56_)
            @Js
            def PyJs_toMarkup_57_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toMarkup':PyJs_toMarkup_57_}, var)
                var.registers(['style', 'markup', 'styles'])
                var.put('markup', ((((Js("<img  src='")+var.get(u"this").get('src'))+Js(" 'alt='"))+var.get(u"this").get('alt'))+Js("' ")))
                var.put('styles', Js(''))
                for PyJsTemp in var.get(u"this").get('style'):
                    var.put('style', PyJsTemp)
                    if var.get(u"this").get('style').callprop('hasOwnProperty', var.get('style')):
                        var.put('styles', (((var.get('utils').callprop('hyphenate', var.get('style'))+Js(':'))+var.get(u"this").get('style').get(var.get('style')))+Js(';')), '+')
                if var.get('styles'):
                    var.put('markup', ((Js(' style="')+var.get('utils').callprop('escape', var.get('styles')))+Js('"')), '+')
                var.put('markup', Js("'/>"), '+')
                return var.get('markup')
            PyJs_toMarkup_57_._set_name('toMarkup')
            var.get('_proto3').put('toMarkup', PyJs_toMarkup_57_)
            return var.get('Img')
        PyJs_anonymous_54_._set_name('anonymous')
        var.put('domTree_Img', PyJs_anonymous_54_())
        var.put('iCombinations', Js({'î':Js('ı̂'),'ï':Js('ı̈'),'í':Js('ı́'),'ì':Js('ı̀')}))
        @Js
        def PyJs_anonymous_58_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['_proto4', 'SymbolNode'])
            @Js
            def PyJsHoisted_SymbolNode_(text, height, depth, italic, skew, width, classes, style, this, arguments, var=var):
                var = Scope({'text':text, 'height':height, 'depth':depth, 'italic':italic, 'skew':skew, 'width':width, 'classes':classes, 'style':style, 'this':this, 'arguments':arguments}, var)
                var.registers(['depth', 'italic', 'text', 'classes', 'width', 'style', 'height', 'skew', 'script'])
                var.get(u"this").put('text', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('height', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('depth', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('italic', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('skew', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('width', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('maxFontSize', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('classes', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('style', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('text', var.get('text'))
                var.get(u"this").put('height', (var.get('height') or Js(0.0)))
                var.get(u"this").put('depth', (var.get('depth') or Js(0.0)))
                var.get(u"this").put('italic', (var.get('italic') or Js(0.0)))
                var.get(u"this").put('skew', (var.get('skew') or Js(0.0)))
                var.get(u"this").put('width', (var.get('width') or Js(0.0)))
                var.get(u"this").put('classes', (var.get('classes') or Js([])))
                var.get(u"this").put('style', (var.get('style') or Js({})))
                var.get(u"this").put('maxFontSize', Js(0.0))
                var.put('script', var.get('scriptFromCodepoint')(var.get(u"this").get('text').callprop('charCodeAt', Js(0.0))))
                if var.get('script'):
                    var.get(u"this").get('classes').callprop('push', (var.get('script')+Js('_fallback')))
                if JsRegExp('/[îïíì]/').callprop('test', var.get(u"this").get('text')):
                    var.get(u"this").put('text', var.get('iCombinations').get(var.get(u"this").get('text')))
            PyJsHoisted_SymbolNode_.func_name = 'SymbolNode'
            var.put('SymbolNode', PyJsHoisted_SymbolNode_)
            pass
            var.put('_proto4', var.get('SymbolNode').get('prototype'))
            @Js
            def PyJs_hasClass_59_(className, this, arguments, var=var):
                var = Scope({'className':className, 'this':this, 'arguments':arguments, 'hasClass':PyJs_hasClass_59_}, var)
                var.registers(['className'])
                return var.get('utils').callprop('contains', var.get(u"this").get('classes'), var.get('className'))
            PyJs_hasClass_59_._set_name('hasClass')
            var.get('_proto4').put('hasClass', PyJs_hasClass_59_)
            @Js
            def PyJs_toNode_60_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toNode':PyJs_toNode_60_}, var)
                var.registers(['node', 'style', 'span'])
                var.put('node', var.get('document').callprop('createTextNode', var.get(u"this").get('text')))
                var.put('span', var.get(u"null"))
                if (var.get(u"this").get('italic')>Js(0.0)):
                    var.put('span', var.get('document').callprop('createElement', Js('span')))
                    var.get('span').get('style').put('marginRight', (var.get(u"this").get('italic')+Js('em')))
                if (var.get(u"this").get('classes').get('length')>Js(0.0)):
                    var.put('span', (var.get('span') or var.get('document').callprop('createElement', Js('span'))))
                    var.get('span').put('className', var.get('createClass')(var.get(u"this").get('classes')))
                for PyJsTemp in var.get(u"this").get('style'):
                    var.put('style', PyJsTemp)
                    if var.get(u"this").get('style').callprop('hasOwnProperty', var.get('style')):
                        var.put('span', (var.get('span') or var.get('document').callprop('createElement', Js('span'))))
                        var.get('span').get('style').put(var.get('style'), var.get(u"this").get('style').get(var.get('style')))
                if var.get('span'):
                    var.get('span').callprop('appendChild', var.get('node'))
                    return var.get('span')
                else:
                    return var.get('node')
            PyJs_toNode_60_._set_name('toNode')
            var.get('_proto4').put('toNode', PyJs_toNode_60_)
            @Js
            def PyJs_toMarkup_61_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toMarkup':PyJs_toMarkup_61_}, var)
                var.registers(['escaped', 'needsSpan', 'style', 'markup', 'styles'])
                var.put('needsSpan', Js(False))
                var.put('markup', Js('<span'))
                if var.get(u"this").get('classes').get('length'):
                    var.put('needsSpan', Js(True))
                    var.put('markup', Js(' class="'), '+')
                    var.put('markup', var.get('utils').callprop('escape', var.get('createClass')(var.get(u"this").get('classes'))), '+')
                    var.put('markup', Js('"'), '+')
                var.put('styles', Js(''))
                if (var.get(u"this").get('italic')>Js(0.0)):
                    var.put('styles', ((Js('margin-right:')+var.get(u"this").get('italic'))+Js('em;')), '+')
                for PyJsTemp in var.get(u"this").get('style'):
                    var.put('style', PyJsTemp)
                    if var.get(u"this").get('style').callprop('hasOwnProperty', var.get('style')):
                        var.put('styles', (((var.get('utils').callprop('hyphenate', var.get('style'))+Js(':'))+var.get(u"this").get('style').get(var.get('style')))+Js(';')), '+')
                if var.get('styles'):
                    var.put('needsSpan', Js(True))
                    var.put('markup', ((Js(' style="')+var.get('utils').callprop('escape', var.get('styles')))+Js('"')), '+')
                var.put('escaped', var.get('utils').callprop('escape', var.get(u"this").get('text')))
                if var.get('needsSpan'):
                    var.put('markup', Js('>'), '+')
                    var.put('markup', var.get('escaped'), '+')
                    var.put('markup', Js('</span>'), '+')
                    return var.get('markup')
                else:
                    return var.get('escaped')
            PyJs_toMarkup_61_._set_name('toMarkup')
            var.get('_proto4').put('toMarkup', PyJs_toMarkup_61_)
            return var.get('SymbolNode')
        PyJs_anonymous_58_._set_name('anonymous')
        var.put('domTree_SymbolNode', PyJs_anonymous_58_())
        @Js
        def PyJs_anonymous_62_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['_proto5', 'SvgNode'])
            @Js
            def PyJsHoisted_SvgNode_(children, attributes, this, arguments, var=var):
                var = Scope({'children':children, 'attributes':attributes, 'this':this, 'arguments':arguments}, var)
                var.registers(['children', 'attributes'])
                var.get(u"this").put('children', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('attributes', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('children', (var.get('children') or Js([])))
                var.get(u"this").put('attributes', (var.get('attributes') or Js({})))
            PyJsHoisted_SvgNode_.func_name = 'SvgNode'
            var.put('SvgNode', PyJsHoisted_SvgNode_)
            pass
            var.put('_proto5', var.get('SvgNode').get('prototype'))
            @Js
            def PyJs_toNode_63_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toNode':PyJs_toNode_63_}, var)
                var.registers(['node', 'svgNS', 'attr', 'i'])
                var.put('svgNS', Js('http://www.w3.org/2000/svg'))
                var.put('node', var.get('document').callprop('createElementNS', var.get('svgNS'), Js('svg')))
                for PyJsTemp in var.get(u"this").get('attributes'):
                    var.put('attr', PyJsTemp)
                    if var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get(u"this").get('attributes'), var.get('attr')):
                        var.get('node').callprop('setAttribute', var.get('attr'), var.get(u"this").get('attributes').get(var.get('attr')))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get(u"this").get('children').get('length')):
                    try:
                        var.get('node').callprop('appendChild', var.get(u"this").get('children').get(var.get('i')).callprop('toNode'))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                return var.get('node')
            PyJs_toNode_63_._set_name('toNode')
            var.get('_proto5').put('toNode', PyJs_toNode_63_)
            @Js
            def PyJs_toMarkup_64_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toMarkup':PyJs_toMarkup_64_}, var)
                var.registers(['attr', 'i', 'markup'])
                var.put('markup', Js('<svg'))
                for PyJsTemp in var.get(u"this").get('attributes'):
                    var.put('attr', PyJsTemp)
                    if var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get(u"this").get('attributes'), var.get('attr')):
                        var.put('markup', ((((Js(' ')+var.get('attr'))+Js("='"))+var.get(u"this").get('attributes').get(var.get('attr')))+Js("'")), '+')
                var.put('markup', Js('>'), '+')
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get(u"this").get('children').get('length')):
                    try:
                        var.put('markup', var.get(u"this").get('children').get(var.get('i')).callprop('toMarkup'), '+')
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                var.put('markup', Js('</svg>'), '+')
                return var.get('markup')
            PyJs_toMarkup_64_._set_name('toMarkup')
            var.get('_proto5').put('toMarkup', PyJs_toMarkup_64_)
            return var.get('SvgNode')
        PyJs_anonymous_62_._set_name('anonymous')
        var.put('SvgNode', PyJs_anonymous_62_())
        @Js
        def PyJs_anonymous_65_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['_proto6', 'PathNode'])
            @Js
            def PyJsHoisted_PathNode_(pathName, alternate, this, arguments, var=var):
                var = Scope({'pathName':pathName, 'alternate':alternate, 'this':this, 'arguments':arguments}, var)
                var.registers(['pathName', 'alternate'])
                var.get(u"this").put('pathName', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('alternate', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('pathName', var.get('pathName'))
                var.get(u"this").put('alternate', var.get('alternate'))
            PyJsHoisted_PathNode_.func_name = 'PathNode'
            var.put('PathNode', PyJsHoisted_PathNode_)
            pass
            var.put('_proto6', var.get('PathNode').get('prototype'))
            @Js
            def PyJs_toNode_66_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toNode':PyJs_toNode_66_}, var)
                var.registers(['node', 'svgNS'])
                var.put('svgNS', Js('http://www.w3.org/2000/svg'))
                var.put('node', var.get('document').callprop('createElementNS', var.get('svgNS'), Js('path')))
                if var.get(u"this").get('alternate'):
                    var.get('node').callprop('setAttribute', Js('d'), var.get(u"this").get('alternate'))
                else:
                    var.get('node').callprop('setAttribute', Js('d'), var.get('svgGeometry').get('path').get(var.get(u"this").get('pathName')))
                return var.get('node')
            PyJs_toNode_66_._set_name('toNode')
            var.get('_proto6').put('toNode', PyJs_toNode_66_)
            @Js
            def PyJs_toMarkup_67_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toMarkup':PyJs_toMarkup_67_}, var)
                var.registers([])
                if var.get(u"this").get('alternate'):
                    return ((Js("<path d='")+var.get(u"this").get('alternate'))+Js("'/>"))
                else:
                    return ((Js("<path d='")+var.get('svgGeometry').get('path').get(var.get(u"this").get('pathName')))+Js("'/>"))
            PyJs_toMarkup_67_._set_name('toMarkup')
            var.get('_proto6').put('toMarkup', PyJs_toMarkup_67_)
            return var.get('PathNode')
        PyJs_anonymous_65_._set_name('anonymous')
        var.put('domTree_PathNode', PyJs_anonymous_65_())
        @Js
        def PyJs_anonymous_68_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['_proto7', 'LineNode'])
            @Js
            def PyJsHoisted_LineNode_(attributes, this, arguments, var=var):
                var = Scope({'attributes':attributes, 'this':this, 'arguments':arguments}, var)
                var.registers(['attributes'])
                var.get(u"this").put('attributes', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('attributes', (var.get('attributes') or Js({})))
            PyJsHoisted_LineNode_.func_name = 'LineNode'
            var.put('LineNode', PyJsHoisted_LineNode_)
            pass
            var.put('_proto7', var.get('LineNode').get('prototype'))
            @Js
            def PyJs_toNode_69_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toNode':PyJs_toNode_69_}, var)
                var.registers(['node', 'svgNS', 'attr'])
                var.put('svgNS', Js('http://www.w3.org/2000/svg'))
                var.put('node', var.get('document').callprop('createElementNS', var.get('svgNS'), Js('line')))
                for PyJsTemp in var.get(u"this").get('attributes'):
                    var.put('attr', PyJsTemp)
                    if var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get(u"this").get('attributes'), var.get('attr')):
                        var.get('node').callprop('setAttribute', var.get('attr'), var.get(u"this").get('attributes').get(var.get('attr')))
                return var.get('node')
            PyJs_toNode_69_._set_name('toNode')
            var.get('_proto7').put('toNode', PyJs_toNode_69_)
            @Js
            def PyJs_toMarkup_70_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toMarkup':PyJs_toMarkup_70_}, var)
                var.registers(['attr', 'markup'])
                var.put('markup', Js('<line'))
                for PyJsTemp in var.get(u"this").get('attributes'):
                    var.put('attr', PyJsTemp)
                    if var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get(u"this").get('attributes'), var.get('attr')):
                        var.put('markup', ((((Js(' ')+var.get('attr'))+Js("='"))+var.get(u"this").get('attributes').get(var.get('attr')))+Js("'")), '+')
                var.put('markup', Js('/>'), '+')
                return var.get('markup')
            PyJs_toMarkup_70_._set_name('toMarkup')
            var.get('_proto7').put('toMarkup', PyJs_toMarkup_70_)
            return var.get('LineNode')
        PyJs_anonymous_68_._set_name('anonymous')
        var.put('LineNode', PyJs_anonymous_68_())
        pass
        pass
        var.put('fontMetricsData', Js({'AMS-Regular':Js({'65':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.72222)]),'66':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.66667)]),'67':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.72222)]),'68':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.72222)]),'69':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.66667)]),'70':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.61111)]),'71':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.77778)]),'72':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.77778)]),'73':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.38889)]),'74':Js([Js(0.16667), Js(0.68889), Js(0.0), Js(0.0), Js(0.5)]),'75':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.77778)]),'76':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.66667)]),'77':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.94445)]),'78':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.72222)]),'79':Js([Js(0.16667), Js(0.68889), Js(0.0), Js(0.0), Js(0.77778)]),'80':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.61111)]),'81':Js([Js(0.16667), Js(0.68889), Js(0.0), Js(0.0), Js(0.77778)]),'82':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.72222)]),'83':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.55556)]),'84':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.66667)]),'85':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.72222)]),'86':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.72222)]),'87':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(1.0)]),'88':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.72222)]),'89':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.72222)]),'90':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.66667)]),'107':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.55556)]),'165':Js([Js(0.0), Js(0.675), Js(0.025), Js(0.0), Js(0.75)]),'174':Js([Js(0.15559), Js(0.69224), Js(0.0), Js(0.0), Js(0.94666)]),'240':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.55556)]),'295':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.54028)]),'710':Js([Js(0.0), Js(0.825), Js(0.0), Js(0.0), Js(2.33334)]),'732':Js([Js(0.0), Js(0.9), Js(0.0), Js(0.0), Js(2.33334)]),'770':Js([Js(0.0), Js(0.825), Js(0.0), Js(0.0), Js(2.33334)]),'771':Js([Js(0.0), Js(0.9), Js(0.0), Js(0.0), Js(2.33334)]),'989':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0), Js(0.77778)]),'1008':Js([Js(0.0), Js(0.43056), Js(0.04028), Js(0.0), Js(0.66667)]),'8245':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0), Js(0.275)]),'8463':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.54028)]),'8487':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.72222)]),'8498':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.55556)]),'8502':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.66667)]),'8503':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.44445)]),'8504':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.66667)]),'8513':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.63889)]),'8592':Js([(-Js(0.03598)), Js(0.46402), Js(0.0), Js(0.0), Js(0.5)]),'8594':Js([(-Js(0.03598)), Js(0.46402), Js(0.0), Js(0.0), Js(0.5)]),'8602':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(1.0)]),'8603':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(1.0)]),'8606':Js([Js(0.01354), Js(0.52239), Js(0.0), Js(0.0), Js(1.0)]),'8608':Js([Js(0.01354), Js(0.52239), Js(0.0), Js(0.0), Js(1.0)]),'8610':Js([Js(0.01354), Js(0.52239), Js(0.0), Js(0.0), Js(1.11111)]),'8611':Js([Js(0.01354), Js(0.52239), Js(0.0), Js(0.0), Js(1.11111)]),'8619':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0), Js(1.0)]),'8620':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0), Js(1.0)]),'8621':Js([(-Js(0.13313)), Js(0.37788), Js(0.0), Js(0.0), Js(1.38889)]),'8622':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(1.0)]),'8624':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.5)]),'8625':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.5)]),'8630':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(1.0)]),'8631':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(1.0)]),'8634':Js([Js(0.08198), Js(0.58198), Js(0.0), Js(0.0), Js(0.77778)]),'8635':Js([Js(0.08198), Js(0.58198), Js(0.0), Js(0.0), Js(0.77778)]),'8638':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0), Js(0.41667)]),'8639':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0), Js(0.41667)]),'8642':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0), Js(0.41667)]),'8643':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0), Js(0.41667)]),'8644':Js([Js(0.1808), Js(0.675), Js(0.0), Js(0.0), Js(1.0)]),'8646':Js([Js(0.1808), Js(0.675), Js(0.0), Js(0.0), Js(1.0)]),'8647':Js([Js(0.1808), Js(0.675), Js(0.0), Js(0.0), Js(1.0)]),'8648':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0), Js(0.83334)]),'8649':Js([Js(0.1808), Js(0.675), Js(0.0), Js(0.0), Js(1.0)]),'8650':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0), Js(0.83334)]),'8651':Js([Js(0.01354), Js(0.52239), Js(0.0), Js(0.0), Js(1.0)]),'8652':Js([Js(0.01354), Js(0.52239), Js(0.0), Js(0.0), Js(1.0)]),'8653':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(1.0)]),'8654':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(1.0)]),'8655':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(1.0)]),'8666':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0), Js(1.0)]),'8667':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0), Js(1.0)]),'8669':Js([(-Js(0.13313)), Js(0.37788), Js(0.0), Js(0.0), Js(1.0)]),'8672':Js([(-Js(0.064)), Js(0.437), Js(0.0), Js(0.0), Js(1.334)]),'8674':Js([(-Js(0.064)), Js(0.437), Js(0.0), Js(0.0), Js(1.334)]),'8705':Js([Js(0.0), Js(0.825), Js(0.0), Js(0.0), Js(0.5)]),'8708':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.55556)]),'8709':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0), Js(0.77778)]),'8717':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.42917)]),'8722':Js([(-Js(0.03598)), Js(0.46402), Js(0.0), Js(0.0), Js(0.5)]),'8724':Js([Js(0.08198), Js(0.69224), Js(0.0), Js(0.0), Js(0.77778)]),'8726':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0), Js(0.77778)]),'8733':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.77778)]),'8736':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.72222)]),'8737':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.72222)]),'8738':Js([Js(0.03517), Js(0.52239), Js(0.0), Js(0.0), Js(0.72222)]),'8739':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0), Js(0.22222)]),'8740':Js([Js(0.25142), Js(0.74111), Js(0.0), Js(0.0), Js(0.27778)]),'8741':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0), Js(0.38889)]),'8742':Js([Js(0.25142), Js(0.74111), Js(0.0), Js(0.0), Js(0.5)]),'8756':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.66667)]),'8757':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.66667)]),'8764':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(0.77778)]),'8765':Js([(-Js(0.13313)), Js(0.37788), Js(0.0), Js(0.0), Js(0.77778)]),'8769':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(0.77778)]),'8770':Js([(-Js(0.03625)), Js(0.46375), Js(0.0), Js(0.0), Js(0.77778)]),'8774':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0), Js(0.77778)]),'8776':Js([(-Js(0.01688)), Js(0.48312), Js(0.0), Js(0.0), Js(0.77778)]),'8778':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0), Js(0.77778)]),'8782':Js([Js(0.06062), Js(0.54986), Js(0.0), Js(0.0), Js(0.77778)]),'8783':Js([Js(0.06062), Js(0.54986), Js(0.0), Js(0.0), Js(0.77778)]),'8785':Js([Js(0.08198), Js(0.58198), Js(0.0), Js(0.0), Js(0.77778)]),'8786':Js([Js(0.08198), Js(0.58198), Js(0.0), Js(0.0), Js(0.77778)]),'8787':Js([Js(0.08198), Js(0.58198), Js(0.0), Js(0.0), Js(0.77778)]),'8790':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.77778)]),'8791':Js([Js(0.22958), Js(0.72958), Js(0.0), Js(0.0), Js(0.77778)]),'8796':Js([Js(0.08198), Js(0.91667), Js(0.0), Js(0.0), Js(0.77778)]),'8806':Js([Js(0.25583), Js(0.75583), Js(0.0), Js(0.0), Js(0.77778)]),'8807':Js([Js(0.25583), Js(0.75583), Js(0.0), Js(0.0), Js(0.77778)]),'8808':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0), Js(0.77778)]),'8809':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0), Js(0.77778)]),'8812':Js([Js(0.25583), Js(0.75583), Js(0.0), Js(0.0), Js(0.5)]),'8814':Js([Js(0.20576), Js(0.70576), Js(0.0), Js(0.0), Js(0.77778)]),'8815':Js([Js(0.20576), Js(0.70576), Js(0.0), Js(0.0), Js(0.77778)]),'8816':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0), Js(0.77778)]),'8817':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0), Js(0.77778)]),'8818':Js([Js(0.22958), Js(0.72958), Js(0.0), Js(0.0), Js(0.77778)]),'8819':Js([Js(0.22958), Js(0.72958), Js(0.0), Js(0.0), Js(0.77778)]),'8822':Js([Js(0.1808), Js(0.675), Js(0.0), Js(0.0), Js(0.77778)]),'8823':Js([Js(0.1808), Js(0.675), Js(0.0), Js(0.0), Js(0.77778)]),'8828':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0), Js(0.77778)]),'8829':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0), Js(0.77778)]),'8830':Js([Js(0.22958), Js(0.72958), Js(0.0), Js(0.0), Js(0.77778)]),'8831':Js([Js(0.22958), Js(0.72958), Js(0.0), Js(0.0), Js(0.77778)]),'8832':Js([Js(0.20576), Js(0.70576), Js(0.0), Js(0.0), Js(0.77778)]),'8833':Js([Js(0.20576), Js(0.70576), Js(0.0), Js(0.0), Js(0.77778)]),'8840':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0), Js(0.77778)]),'8841':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0), Js(0.77778)]),'8842':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0), Js(0.77778)]),'8843':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0), Js(0.77778)]),'8847':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0), Js(0.77778)]),'8848':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0), Js(0.77778)]),'8858':Js([Js(0.08198), Js(0.58198), Js(0.0), Js(0.0), Js(0.77778)]),'8859':Js([Js(0.08198), Js(0.58198), Js(0.0), Js(0.0), Js(0.77778)]),'8861':Js([Js(0.08198), Js(0.58198), Js(0.0), Js(0.0), Js(0.77778)]),'8862':Js([Js(0.0), Js(0.675), Js(0.0), Js(0.0), Js(0.77778)]),'8863':Js([Js(0.0), Js(0.675), Js(0.0), Js(0.0), Js(0.77778)]),'8864':Js([Js(0.0), Js(0.675), Js(0.0), Js(0.0), Js(0.77778)]),'8865':Js([Js(0.0), Js(0.675), Js(0.0), Js(0.0), Js(0.77778)]),'8872':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.61111)]),'8873':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.72222)]),'8874':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.88889)]),'8876':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.61111)]),'8877':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.61111)]),'8878':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.72222)]),'8879':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.72222)]),'8882':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0), Js(0.77778)]),'8883':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0), Js(0.77778)]),'8884':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0), Js(0.77778)]),'8885':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0), Js(0.77778)]),'8888':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0), Js(1.11111)]),'8890':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0), Js(0.55556)]),'8891':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0), Js(0.61111)]),'8892':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0), Js(0.61111)]),'8901':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0), Js(0.27778)]),'8903':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0), Js(0.77778)]),'8905':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0), Js(0.77778)]),'8906':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0), Js(0.77778)]),'8907':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.77778)]),'8908':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.77778)]),'8909':Js([(-Js(0.03598)), Js(0.46402), Js(0.0), Js(0.0), Js(0.77778)]),'8910':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0), Js(0.76042)]),'8911':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0), Js(0.76042)]),'8912':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0), Js(0.77778)]),'8913':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0), Js(0.77778)]),'8914':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0), Js(0.66667)]),'8915':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0), Js(0.66667)]),'8916':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.66667)]),'8918':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0), Js(0.77778)]),'8919':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0), Js(0.77778)]),'8920':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0), Js(1.33334)]),'8921':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0), Js(1.33334)]),'8922':Js([Js(0.38569), Js(0.88569), Js(0.0), Js(0.0), Js(0.77778)]),'8923':Js([Js(0.38569), Js(0.88569), Js(0.0), Js(0.0), Js(0.77778)]),'8926':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0), Js(0.77778)]),'8927':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0), Js(0.77778)]),'8928':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0), Js(0.77778)]),'8929':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0), Js(0.77778)]),'8934':Js([Js(0.23222), Js(0.74111), Js(0.0), Js(0.0), Js(0.77778)]),'8935':Js([Js(0.23222), Js(0.74111), Js(0.0), Js(0.0), Js(0.77778)]),'8936':Js([Js(0.23222), Js(0.74111), Js(0.0), Js(0.0), Js(0.77778)]),'8937':Js([Js(0.23222), Js(0.74111), Js(0.0), Js(0.0), Js(0.77778)]),'8938':Js([Js(0.20576), Js(0.70576), Js(0.0), Js(0.0), Js(0.77778)]),'8939':Js([Js(0.20576), Js(0.70576), Js(0.0), Js(0.0), Js(0.77778)]),'8940':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0), Js(0.77778)]),'8941':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0), Js(0.77778)]),'8994':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0), Js(0.77778)]),'8995':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0), Js(0.77778)]),'9416':Js([Js(0.15559), Js(0.69224), Js(0.0), Js(0.0), Js(0.90222)]),'9484':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.5)]),'9488':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.5)]),'9492':Js([Js(0.0), Js(0.37788), Js(0.0), Js(0.0), Js(0.5)]),'9496':Js([Js(0.0), Js(0.37788), Js(0.0), Js(0.0), Js(0.5)]),'9585':Js([Js(0.19444), Js(0.68889), Js(0.0), Js(0.0), Js(0.88889)]),'9586':Js([Js(0.19444), Js(0.74111), Js(0.0), Js(0.0), Js(0.88889)]),'9632':Js([Js(0.0), Js(0.675), Js(0.0), Js(0.0), Js(0.77778)]),'9633':Js([Js(0.0), Js(0.675), Js(0.0), Js(0.0), Js(0.77778)]),'9650':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0), Js(0.72222)]),'9651':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0), Js(0.72222)]),'9654':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0), Js(0.77778)]),'9660':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0), Js(0.72222)]),'9661':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0), Js(0.72222)]),'9664':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0), Js(0.77778)]),'9674':Js([Js(0.11111), Js(0.69224), Js(0.0), Js(0.0), Js(0.66667)]),'9733':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0), Js(0.94445)]),'10003':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.83334)]),'10016':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.83334)]),'10731':Js([Js(0.11111), Js(0.69224), Js(0.0), Js(0.0), Js(0.66667)]),'10846':Js([Js(0.19444), Js(0.75583), Js(0.0), Js(0.0), Js(0.61111)]),'10877':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0), Js(0.77778)]),'10878':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0), Js(0.77778)]),'10885':Js([Js(0.25583), Js(0.75583), Js(0.0), Js(0.0), Js(0.77778)]),'10886':Js([Js(0.25583), Js(0.75583), Js(0.0), Js(0.0), Js(0.77778)]),'10887':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0), Js(0.77778)]),'10888':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0), Js(0.77778)]),'10889':Js([Js(0.26167), Js(0.75726), Js(0.0), Js(0.0), Js(0.77778)]),'10890':Js([Js(0.26167), Js(0.75726), Js(0.0), Js(0.0), Js(0.77778)]),'10891':Js([Js(0.48256), Js(0.98256), Js(0.0), Js(0.0), Js(0.77778)]),'10892':Js([Js(0.48256), Js(0.98256), Js(0.0), Js(0.0), Js(0.77778)]),'10901':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0), Js(0.77778)]),'10902':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0), Js(0.77778)]),'10933':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0), Js(0.77778)]),'10934':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0), Js(0.77778)]),'10935':Js([Js(0.26167), Js(0.75726), Js(0.0), Js(0.0), Js(0.77778)]),'10936':Js([Js(0.26167), Js(0.75726), Js(0.0), Js(0.0), Js(0.77778)]),'10937':Js([Js(0.26167), Js(0.75726), Js(0.0), Js(0.0), Js(0.77778)]),'10938':Js([Js(0.26167), Js(0.75726), Js(0.0), Js(0.0), Js(0.77778)]),'10949':Js([Js(0.25583), Js(0.75583), Js(0.0), Js(0.0), Js(0.77778)]),'10950':Js([Js(0.25583), Js(0.75583), Js(0.0), Js(0.0), Js(0.77778)]),'10955':Js([Js(0.28481), Js(0.79383), Js(0.0), Js(0.0), Js(0.77778)]),'10956':Js([Js(0.28481), Js(0.79383), Js(0.0), Js(0.0), Js(0.77778)]),'57350':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0), Js(0.22222)]),'57351':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0), Js(0.38889)]),'57352':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0), Js(0.77778)]),'57353':Js([Js(0.0), Js(0.43056), Js(0.04028), Js(0.0), Js(0.66667)]),'57356':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0), Js(0.77778)]),'57357':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0), Js(0.77778)]),'57358':Js([Js(0.41951), Js(0.91951), Js(0.0), Js(0.0), Js(0.77778)]),'57359':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0), Js(0.77778)]),'57360':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0), Js(0.77778)]),'57361':Js([Js(0.41951), Js(0.91951), Js(0.0), Js(0.0), Js(0.77778)]),'57366':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0), Js(0.77778)]),'57367':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0), Js(0.77778)]),'57368':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0), Js(0.77778)]),'57369':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0), Js(0.77778)]),'57370':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0), Js(0.77778)]),'57371':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0), Js(0.77778)])}),'Caligraphic-Regular':Js({'48':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.5)]),'49':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.5)]),'50':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.5)]),'51':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0), Js(0.5)]),'52':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0), Js(0.5)]),'53':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0), Js(0.5)]),'54':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.5)]),'55':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0), Js(0.5)]),'56':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.5)]),'57':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0), Js(0.5)]),'65':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.19445), Js(0.79847)]),'66':Js([Js(0.0), Js(0.68333), Js(0.03041), Js(0.13889), Js(0.65681)]),'67':Js([Js(0.0), Js(0.68333), Js(0.05834), Js(0.13889), Js(0.52653)]),'68':Js([Js(0.0), Js(0.68333), Js(0.02778), Js(0.08334), Js(0.77139)]),'69':Js([Js(0.0), Js(0.68333), Js(0.08944), Js(0.11111), Js(0.52778)]),'70':Js([Js(0.0), Js(0.68333), Js(0.09931), Js(0.11111), Js(0.71875)]),'71':Js([Js(0.09722), Js(0.68333), Js(0.0593), Js(0.11111), Js(0.59487)]),'72':Js([Js(0.0), Js(0.68333), Js(0.00965), Js(0.11111), Js(0.84452)]),'73':Js([Js(0.0), Js(0.68333), Js(0.07382), Js(0.0), Js(0.54452)]),'74':Js([Js(0.09722), Js(0.68333), Js(0.18472), Js(0.16667), Js(0.67778)]),'75':Js([Js(0.0), Js(0.68333), Js(0.01445), Js(0.05556), Js(0.76195)]),'76':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.13889), Js(0.68972)]),'77':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.13889), Js(1.2009)]),'78':Js([Js(0.0), Js(0.68333), Js(0.14736), Js(0.08334), Js(0.82049)]),'79':Js([Js(0.0), Js(0.68333), Js(0.02778), Js(0.11111), Js(0.79611)]),'80':Js([Js(0.0), Js(0.68333), Js(0.08222), Js(0.08334), Js(0.69556)]),'81':Js([Js(0.09722), Js(0.68333), Js(0.0), Js(0.11111), Js(0.81667)]),'82':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.08334), Js(0.8475)]),'83':Js([Js(0.0), Js(0.68333), Js(0.075), Js(0.13889), Js(0.60556)]),'84':Js([Js(0.0), Js(0.68333), Js(0.25417), Js(0.0), Js(0.54464)]),'85':Js([Js(0.0), Js(0.68333), Js(0.09931), Js(0.08334), Js(0.62583)]),'86':Js([Js(0.0), Js(0.68333), Js(0.08222), Js(0.0), Js(0.61278)]),'87':Js([Js(0.0), Js(0.68333), Js(0.08222), Js(0.08334), Js(0.98778)]),'88':Js([Js(0.0), Js(0.68333), Js(0.14643), Js(0.13889), Js(0.7133)]),'89':Js([Js(0.09722), Js(0.68333), Js(0.08222), Js(0.08334), Js(0.66834)]),'90':Js([Js(0.0), Js(0.68333), Js(0.07944), Js(0.13889), Js(0.72473)])}),'Fraktur-Regular':Js({'33':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.29574)]),'34':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.21471)]),'38':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.73786)]),'39':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.21201)]),'40':Js([Js(0.24982), Js(0.74947), Js(0.0), Js(0.0), Js(0.38865)]),'41':Js([Js(0.24982), Js(0.74947), Js(0.0), Js(0.0), Js(0.38865)]),'42':Js([Js(0.0), Js(0.62119), Js(0.0), Js(0.0), Js(0.27764)]),'43':Js([Js(0.08319), Js(0.58283), Js(0.0), Js(0.0), Js(0.75623)]),'44':Js([Js(0.0), Js(0.10803), Js(0.0), Js(0.0), Js(0.27764)]),'45':Js([Js(0.08319), Js(0.58283), Js(0.0), Js(0.0), Js(0.75623)]),'46':Js([Js(0.0), Js(0.10803), Js(0.0), Js(0.0), Js(0.27764)]),'47':Js([Js(0.24982), Js(0.74947), Js(0.0), Js(0.0), Js(0.50181)]),'48':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0), Js(0.50181)]),'49':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0), Js(0.50181)]),'50':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0), Js(0.50181)]),'51':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0), Js(0.50181)]),'52':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0), Js(0.50181)]),'53':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0), Js(0.50181)]),'54':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.50181)]),'55':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0), Js(0.50181)]),'56':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.50181)]),'57':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0), Js(0.50181)]),'58':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0), Js(0.21606)]),'59':Js([Js(0.12604), Js(0.47534), Js(0.0), Js(0.0), Js(0.21606)]),'61':Js([(-Js(0.13099)), Js(0.36866), Js(0.0), Js(0.0), Js(0.75623)]),'63':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.36245)]),'65':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.7176)]),'66':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.88397)]),'67':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.61254)]),'68':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.83158)]),'69':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.66278)]),'70':Js([Js(0.12604), Js(0.69141), Js(0.0), Js(0.0), Js(0.61119)]),'71':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.78539)]),'72':Js([Js(0.06302), Js(0.69141), Js(0.0), Js(0.0), Js(0.7203)]),'73':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.55448)]),'74':Js([Js(0.12604), Js(0.69141), Js(0.0), Js(0.0), Js(0.55231)]),'75':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.66845)]),'76':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.66602)]),'77':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(1.04953)]),'78':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.83212)]),'79':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.82699)]),'80':Js([Js(0.18906), Js(0.69141), Js(0.0), Js(0.0), Js(0.82753)]),'81':Js([Js(0.03781), Js(0.69141), Js(0.0), Js(0.0), Js(0.82699)]),'82':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.82807)]),'83':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.82861)]),'84':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.66899)]),'85':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.64576)]),'86':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.83131)]),'87':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(1.04602)]),'88':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.71922)]),'89':Js([Js(0.18906), Js(0.69141), Js(0.0), Js(0.0), Js(0.83293)]),'90':Js([Js(0.12604), Js(0.69141), Js(0.0), Js(0.0), Js(0.60201)]),'91':Js([Js(0.24982), Js(0.74947), Js(0.0), Js(0.0), Js(0.27764)]),'93':Js([Js(0.24982), Js(0.74947), Js(0.0), Js(0.0), Js(0.27764)]),'94':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.49965)]),'97':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0), Js(0.50046)]),'98':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.51315)]),'99':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0), Js(0.38946)]),'100':Js([Js(0.0), Js(0.62119), Js(0.0), Js(0.0), Js(0.49857)]),'101':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0), Js(0.40053)]),'102':Js([Js(0.18906), Js(0.69141), Js(0.0), Js(0.0), Js(0.32626)]),'103':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0), Js(0.5037)]),'104':Js([Js(0.18906), Js(0.69141), Js(0.0), Js(0.0), Js(0.52126)]),'105':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.27899)]),'106':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.28088)]),'107':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.38946)]),'108':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.27953)]),'109':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0), Js(0.76676)]),'110':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0), Js(0.52666)]),'111':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0), Js(0.48885)]),'112':Js([Js(0.18906), Js(0.52396), Js(0.0), Js(0.0), Js(0.50046)]),'113':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0), Js(0.48912)]),'114':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0), Js(0.38919)]),'115':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0), Js(0.44266)]),'116':Js([Js(0.0), Js(0.62119), Js(0.0), Js(0.0), Js(0.33301)]),'117':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0), Js(0.5172)]),'118':Js([Js(0.0), Js(0.52396), Js(0.0), Js(0.0), Js(0.5118)]),'119':Js([Js(0.0), Js(0.52396), Js(0.0), Js(0.0), Js(0.77351)]),'120':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0), Js(0.38865)]),'121':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0), Js(0.49884)]),'122':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0), Js(0.39054)]),'8216':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.21471)]),'8217':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.21471)]),'58112':Js([Js(0.0), Js(0.62119), Js(0.0), Js(0.0), Js(0.49749)]),'58113':Js([Js(0.0), Js(0.62119), Js(0.0), Js(0.0), Js(0.4983)]),'58114':Js([Js(0.18906), Js(0.69141), Js(0.0), Js(0.0), Js(0.33328)]),'58115':Js([Js(0.18906), Js(0.69141), Js(0.0), Js(0.0), Js(0.32923)]),'58116':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0), Js(0.50343)]),'58117':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0), Js(0.33301)]),'58118':Js([Js(0.0), Js(0.62119), Js(0.0), Js(0.0), Js(0.33409)]),'58119':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0), Js(0.50073)])}),'Main-Bold':Js({'33':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.35)]),'34':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.60278)]),'35':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.95833)]),'36':Js([Js(0.05556), Js(0.75), Js(0.0), Js(0.0), Js(0.575)]),'37':Js([Js(0.05556), Js(0.75), Js(0.0), Js(0.0), Js(0.95833)]),'38':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.89444)]),'39':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.31944)]),'40':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.44722)]),'41':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.44722)]),'42':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0), Js(0.575)]),'43':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0), Js(0.89444)]),'44':Js([Js(0.19444), Js(0.15556), Js(0.0), Js(0.0), Js(0.31944)]),'45':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.38333)]),'46':Js([Js(0.0), Js(0.15556), Js(0.0), Js(0.0), Js(0.31944)]),'47':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.575)]),'48':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.575)]),'49':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.575)]),'50':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.575)]),'51':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.575)]),'52':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.575)]),'53':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.575)]),'54':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.575)]),'55':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.575)]),'56':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.575)]),'57':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.575)]),'58':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.31944)]),'59':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0), Js(0.31944)]),'60':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0), Js(0.89444)]),'61':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0), Js(0.89444)]),'62':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0), Js(0.89444)]),'63':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.54305)]),'64':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.89444)]),'65':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.86944)]),'66':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.81805)]),'67':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.83055)]),'68':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.88194)]),'69':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.75555)]),'70':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.72361)]),'71':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.90416)]),'72':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.9)]),'73':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.43611)]),'74':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.59444)]),'75':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.90138)]),'76':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.69166)]),'77':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(1.09166)]),'78':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.9)]),'79':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.86388)]),'80':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.78611)]),'81':Js([Js(0.19444), Js(0.68611), Js(0.0), Js(0.0), Js(0.86388)]),'82':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.8625)]),'83':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.63889)]),'84':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.8)]),'85':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.88472)]),'86':Js([Js(0.0), Js(0.68611), Js(0.01597), Js(0.0), Js(0.86944)]),'87':Js([Js(0.0), Js(0.68611), Js(0.01597), Js(0.0), Js(1.18888)]),'88':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.86944)]),'89':Js([Js(0.0), Js(0.68611), Js(0.02875), Js(0.0), Js(0.86944)]),'90':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.70277)]),'91':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.31944)]),'92':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.575)]),'93':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.31944)]),'94':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.575)]),'95':Js([Js(0.31), Js(0.13444), Js(0.03194), Js(0.0), Js(0.575)]),'97':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.55902)]),'98':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.63889)]),'99':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.51111)]),'100':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.63889)]),'101':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.52708)]),'102':Js([Js(0.0), Js(0.69444), Js(0.10903), Js(0.0), Js(0.35139)]),'103':Js([Js(0.19444), Js(0.44444), Js(0.01597), Js(0.0), Js(0.575)]),'104':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.63889)]),'105':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.31944)]),'106':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.35139)]),'107':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.60694)]),'108':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.31944)]),'109':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.95833)]),'110':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.63889)]),'111':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.575)]),'112':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0), Js(0.63889)]),'113':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0), Js(0.60694)]),'114':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.47361)]),'115':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.45361)]),'116':Js([Js(0.0), Js(0.63492), Js(0.0), Js(0.0), Js(0.44722)]),'117':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.63889)]),'118':Js([Js(0.0), Js(0.44444), Js(0.01597), Js(0.0), Js(0.60694)]),'119':Js([Js(0.0), Js(0.44444), Js(0.01597), Js(0.0), Js(0.83055)]),'120':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.60694)]),'121':Js([Js(0.19444), Js(0.44444), Js(0.01597), Js(0.0), Js(0.60694)]),'122':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.51111)]),'123':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.575)]),'124':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.31944)]),'125':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.575)]),'126':Js([Js(0.35), Js(0.34444), Js(0.0), Js(0.0), Js(0.575)]),'168':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.575)]),'172':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.76666)]),'176':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.86944)]),'177':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0), Js(0.89444)]),'184':Js([Js(0.17014), Js(0.0), Js(0.0), Js(0.0), Js(0.51111)]),'198':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(1.04166)]),'215':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0), Js(0.89444)]),'216':Js([Js(0.04861), Js(0.73472), Js(0.0), Js(0.0), Js(0.89444)]),'223':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.59722)]),'230':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.83055)]),'247':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0), Js(0.89444)]),'248':Js([Js(0.09722), Js(0.54167), Js(0.0), Js(0.0), Js(0.575)]),'305':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.31944)]),'338':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(1.16944)]),'339':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.89444)]),'567':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0), Js(0.35139)]),'710':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.575)]),'711':Js([Js(0.0), Js(0.63194), Js(0.0), Js(0.0), Js(0.575)]),'713':Js([Js(0.0), Js(0.59611), Js(0.0), Js(0.0), Js(0.575)]),'714':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.575)]),'715':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.575)]),'728':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.575)]),'729':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.31944)]),'730':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.86944)]),'732':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.575)]),'733':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.575)]),'915':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.69166)]),'916':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.95833)]),'920':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.89444)]),'923':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.80555)]),'926':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.76666)]),'928':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.9)]),'931':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.83055)]),'933':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.89444)]),'934':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.83055)]),'936':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.89444)]),'937':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.83055)]),'8211':Js([Js(0.0), Js(0.44444), Js(0.03194), Js(0.0), Js(0.575)]),'8212':Js([Js(0.0), Js(0.44444), Js(0.03194), Js(0.0), Js(1.14999)]),'8216':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.31944)]),'8217':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.31944)]),'8220':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.60278)]),'8221':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.60278)]),'8224':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.51111)]),'8225':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.51111)]),'8242':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0), Js(0.34444)]),'8407':Js([Js(0.0), Js(0.72444), Js(0.15486), Js(0.0), Js(0.575)]),'8463':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.66759)]),'8465':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.83055)]),'8467':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.47361)]),'8472':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0), Js(0.74027)]),'8476':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.83055)]),'8501':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.70277)]),'8592':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0), Js(1.14999)]),'8593':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.575)]),'8594':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0), Js(1.14999)]),'8595':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.575)]),'8596':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0), Js(1.14999)]),'8597':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.575)]),'8598':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(1.14999)]),'8599':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(1.14999)]),'8600':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(1.14999)]),'8601':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(1.14999)]),'8636':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0), Js(1.14999)]),'8637':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0), Js(1.14999)]),'8640':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0), Js(1.14999)]),'8641':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0), Js(1.14999)]),'8656':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0), Js(1.14999)]),'8657':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.70277)]),'8658':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0), Js(1.14999)]),'8659':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.70277)]),'8660':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0), Js(1.14999)]),'8661':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.70277)]),'8704':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.63889)]),'8706':Js([Js(0.0), Js(0.69444), Js(0.06389), Js(0.0), Js(0.62847)]),'8707':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.63889)]),'8709':Js([Js(0.05556), Js(0.75), Js(0.0), Js(0.0), Js(0.575)]),'8711':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.95833)]),'8712':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0), Js(0.76666)]),'8715':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0), Js(0.76666)]),'8722':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0), Js(0.89444)]),'8723':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0), Js(0.89444)]),'8725':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.575)]),'8726':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.575)]),'8727':Js([(-Js(0.02778)), Js(0.47222), Js(0.0), Js(0.0), Js(0.575)]),'8728':Js([(-Js(0.02639)), Js(0.47361), Js(0.0), Js(0.0), Js(0.575)]),'8729':Js([(-Js(0.02639)), Js(0.47361), Js(0.0), Js(0.0), Js(0.575)]),'8730':Js([Js(0.18), Js(0.82), Js(0.0), Js(0.0), Js(0.95833)]),'8733':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.89444)]),'8734':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(1.14999)]),'8736':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.72222)]),'8739':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.31944)]),'8741':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.575)]),'8743':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0), Js(0.76666)]),'8744':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0), Js(0.76666)]),'8745':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0), Js(0.76666)]),'8746':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0), Js(0.76666)]),'8747':Js([Js(0.19444), Js(0.69444), Js(0.12778), Js(0.0), Js(0.56875)]),'8764':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0), Js(0.89444)]),'8768':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.31944)]),'8771':Js([Js(0.00222), Js(0.50222), Js(0.0), Js(0.0), Js(0.89444)]),'8776':Js([Js(0.02444), Js(0.52444), Js(0.0), Js(0.0), Js(0.89444)]),'8781':Js([Js(0.00222), Js(0.50222), Js(0.0), Js(0.0), Js(0.89444)]),'8801':Js([Js(0.00222), Js(0.50222), Js(0.0), Js(0.0), Js(0.89444)]),'8804':Js([Js(0.19667), Js(0.69667), Js(0.0), Js(0.0), Js(0.89444)]),'8805':Js([Js(0.19667), Js(0.69667), Js(0.0), Js(0.0), Js(0.89444)]),'8810':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0), Js(1.14999)]),'8811':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0), Js(1.14999)]),'8826':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0), Js(0.89444)]),'8827':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0), Js(0.89444)]),'8834':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0), Js(0.89444)]),'8835':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0), Js(0.89444)]),'8838':Js([Js(0.19667), Js(0.69667), Js(0.0), Js(0.0), Js(0.89444)]),'8839':Js([Js(0.19667), Js(0.69667), Js(0.0), Js(0.0), Js(0.89444)]),'8846':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0), Js(0.76666)]),'8849':Js([Js(0.19667), Js(0.69667), Js(0.0), Js(0.0), Js(0.89444)]),'8850':Js([Js(0.19667), Js(0.69667), Js(0.0), Js(0.0), Js(0.89444)]),'8851':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0), Js(0.76666)]),'8852':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0), Js(0.76666)]),'8853':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0), Js(0.89444)]),'8854':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0), Js(0.89444)]),'8855':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0), Js(0.89444)]),'8856':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0), Js(0.89444)]),'8857':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0), Js(0.89444)]),'8866':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.70277)]),'8867':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.70277)]),'8868':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.89444)]),'8869':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.89444)]),'8900':Js([(-Js(0.02639)), Js(0.47361), Js(0.0), Js(0.0), Js(0.575)]),'8901':Js([(-Js(0.02639)), Js(0.47361), Js(0.0), Js(0.0), Js(0.31944)]),'8902':Js([(-Js(0.02778)), Js(0.47222), Js(0.0), Js(0.0), Js(0.575)]),'8968':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.51111)]),'8969':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.51111)]),'8970':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.51111)]),'8971':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.51111)]),'8994':Js([(-Js(0.13889)), Js(0.36111), Js(0.0), Js(0.0), Js(1.14999)]),'8995':Js([(-Js(0.13889)), Js(0.36111), Js(0.0), Js(0.0), Js(1.14999)]),'9651':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(1.02222)]),'9657':Js([(-Js(0.02778)), Js(0.47222), Js(0.0), Js(0.0), Js(0.575)]),'9661':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(1.02222)]),'9667':Js([(-Js(0.02778)), Js(0.47222), Js(0.0), Js(0.0), Js(0.575)]),'9711':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(1.14999)]),'9824':Js([Js(0.12963), Js(0.69444), Js(0.0), Js(0.0), Js(0.89444)]),'9825':Js([Js(0.12963), Js(0.69444), Js(0.0), Js(0.0), Js(0.89444)]),'9826':Js([Js(0.12963), Js(0.69444), Js(0.0), Js(0.0), Js(0.89444)]),'9827':Js([Js(0.12963), Js(0.69444), Js(0.0), Js(0.0), Js(0.89444)]),'9837':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0), Js(0.44722)]),'9838':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.44722)]),'9839':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.44722)]),'10216':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.44722)]),'10217':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.44722)]),'10815':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.9)]),'10927':Js([Js(0.19667), Js(0.69667), Js(0.0), Js(0.0), Js(0.89444)]),'10928':Js([Js(0.19667), Js(0.69667), Js(0.0), Js(0.0), Js(0.89444)]),'57376':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.0)])}),'Main-BoldItalic':Js({'33':Js([Js(0.0), Js(0.69444), Js(0.11417), Js(0.0), Js(0.38611)]),'34':Js([Js(0.0), Js(0.69444), Js(0.07939), Js(0.0), Js(0.62055)]),'35':Js([Js(0.19444), Js(0.69444), Js(0.06833), Js(0.0), Js(0.94444)]),'37':Js([Js(0.05556), Js(0.75), Js(0.12861), Js(0.0), Js(0.94444)]),'38':Js([Js(0.0), Js(0.69444), Js(0.08528), Js(0.0), Js(0.88555)]),'39':Js([Js(0.0), Js(0.69444), Js(0.12945), Js(0.0), Js(0.35555)]),'40':Js([Js(0.25), Js(0.75), Js(0.15806), Js(0.0), Js(0.47333)]),'41':Js([Js(0.25), Js(0.75), Js(0.03306), Js(0.0), Js(0.47333)]),'42':Js([Js(0.0), Js(0.75), Js(0.14333), Js(0.0), Js(0.59111)]),'43':Js([Js(0.10333), Js(0.60333), Js(0.03306), Js(0.0), Js(0.88555)]),'44':Js([Js(0.19444), Js(0.14722), Js(0.0), Js(0.0), Js(0.35555)]),'45':Js([Js(0.0), Js(0.44444), Js(0.02611), Js(0.0), Js(0.41444)]),'46':Js([Js(0.0), Js(0.14722), Js(0.0), Js(0.0), Js(0.35555)]),'47':Js([Js(0.25), Js(0.75), Js(0.15806), Js(0.0), Js(0.59111)]),'48':Js([Js(0.0), Js(0.64444), Js(0.13167), Js(0.0), Js(0.59111)]),'49':Js([Js(0.0), Js(0.64444), Js(0.13167), Js(0.0), Js(0.59111)]),'50':Js([Js(0.0), Js(0.64444), Js(0.13167), Js(0.0), Js(0.59111)]),'51':Js([Js(0.0), Js(0.64444), Js(0.13167), Js(0.0), Js(0.59111)]),'52':Js([Js(0.19444), Js(0.64444), Js(0.13167), Js(0.0), Js(0.59111)]),'53':Js([Js(0.0), Js(0.64444), Js(0.13167), Js(0.0), Js(0.59111)]),'54':Js([Js(0.0), Js(0.64444), Js(0.13167), Js(0.0), Js(0.59111)]),'55':Js([Js(0.19444), Js(0.64444), Js(0.13167), Js(0.0), Js(0.59111)]),'56':Js([Js(0.0), Js(0.64444), Js(0.13167), Js(0.0), Js(0.59111)]),'57':Js([Js(0.0), Js(0.64444), Js(0.13167), Js(0.0), Js(0.59111)]),'58':Js([Js(0.0), Js(0.44444), Js(0.06695), Js(0.0), Js(0.35555)]),'59':Js([Js(0.19444), Js(0.44444), Js(0.06695), Js(0.0), Js(0.35555)]),'61':Js([(-Js(0.10889)), Js(0.39111), Js(0.06833), Js(0.0), Js(0.88555)]),'63':Js([Js(0.0), Js(0.69444), Js(0.11472), Js(0.0), Js(0.59111)]),'64':Js([Js(0.0), Js(0.69444), Js(0.09208), Js(0.0), Js(0.88555)]),'65':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.86555)]),'66':Js([Js(0.0), Js(0.68611), Js(0.0992), Js(0.0), Js(0.81666)]),'67':Js([Js(0.0), Js(0.68611), Js(0.14208), Js(0.0), Js(0.82666)]),'68':Js([Js(0.0), Js(0.68611), Js(0.09062), Js(0.0), Js(0.87555)]),'69':Js([Js(0.0), Js(0.68611), Js(0.11431), Js(0.0), Js(0.75666)]),'70':Js([Js(0.0), Js(0.68611), Js(0.12903), Js(0.0), Js(0.72722)]),'71':Js([Js(0.0), Js(0.68611), Js(0.07347), Js(0.0), Js(0.89527)]),'72':Js([Js(0.0), Js(0.68611), Js(0.17208), Js(0.0), Js(0.8961)]),'73':Js([Js(0.0), Js(0.68611), Js(0.15681), Js(0.0), Js(0.47166)]),'74':Js([Js(0.0), Js(0.68611), Js(0.145), Js(0.0), Js(0.61055)]),'75':Js([Js(0.0), Js(0.68611), Js(0.14208), Js(0.0), Js(0.89499)]),'76':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.69777)]),'77':Js([Js(0.0), Js(0.68611), Js(0.17208), Js(0.0), Js(1.07277)]),'78':Js([Js(0.0), Js(0.68611), Js(0.17208), Js(0.0), Js(0.8961)]),'79':Js([Js(0.0), Js(0.68611), Js(0.09062), Js(0.0), Js(0.85499)]),'80':Js([Js(0.0), Js(0.68611), Js(0.0992), Js(0.0), Js(0.78721)]),'81':Js([Js(0.19444), Js(0.68611), Js(0.09062), Js(0.0), Js(0.85499)]),'82':Js([Js(0.0), Js(0.68611), Js(0.02559), Js(0.0), Js(0.85944)]),'83':Js([Js(0.0), Js(0.68611), Js(0.11264), Js(0.0), Js(0.64999)]),'84':Js([Js(0.0), Js(0.68611), Js(0.12903), Js(0.0), Js(0.7961)]),'85':Js([Js(0.0), Js(0.68611), Js(0.17208), Js(0.0), Js(0.88083)]),'86':Js([Js(0.0), Js(0.68611), Js(0.18625), Js(0.0), Js(0.86555)]),'87':Js([Js(0.0), Js(0.68611), Js(0.18625), Js(0.0), Js(1.15999)]),'88':Js([Js(0.0), Js(0.68611), Js(0.15681), Js(0.0), Js(0.86555)]),'89':Js([Js(0.0), Js(0.68611), Js(0.19803), Js(0.0), Js(0.86555)]),'90':Js([Js(0.0), Js(0.68611), Js(0.14208), Js(0.0), Js(0.70888)]),'91':Js([Js(0.25), Js(0.75), Js(0.1875), Js(0.0), Js(0.35611)]),'93':Js([Js(0.25), Js(0.75), Js(0.09972), Js(0.0), Js(0.35611)]),'94':Js([Js(0.0), Js(0.69444), Js(0.06709), Js(0.0), Js(0.59111)]),'95':Js([Js(0.31), Js(0.13444), Js(0.09811), Js(0.0), Js(0.59111)]),'97':Js([Js(0.0), Js(0.44444), Js(0.09426), Js(0.0), Js(0.59111)]),'98':Js([Js(0.0), Js(0.69444), Js(0.07861), Js(0.0), Js(0.53222)]),'99':Js([Js(0.0), Js(0.44444), Js(0.05222), Js(0.0), Js(0.53222)]),'100':Js([Js(0.0), Js(0.69444), Js(0.10861), Js(0.0), Js(0.59111)]),'101':Js([Js(0.0), Js(0.44444), Js(0.085), Js(0.0), Js(0.53222)]),'102':Js([Js(0.19444), Js(0.69444), Js(0.21778), Js(0.0), Js(0.4)]),'103':Js([Js(0.19444), Js(0.44444), Js(0.105), Js(0.0), Js(0.53222)]),'104':Js([Js(0.0), Js(0.69444), Js(0.09426), Js(0.0), Js(0.59111)]),'105':Js([Js(0.0), Js(0.69326), Js(0.11387), Js(0.0), Js(0.35555)]),'106':Js([Js(0.19444), Js(0.69326), Js(0.1672), Js(0.0), Js(0.35555)]),'107':Js([Js(0.0), Js(0.69444), Js(0.11111), Js(0.0), Js(0.53222)]),'108':Js([Js(0.0), Js(0.69444), Js(0.10861), Js(0.0), Js(0.29666)]),'109':Js([Js(0.0), Js(0.44444), Js(0.09426), Js(0.0), Js(0.94444)]),'110':Js([Js(0.0), Js(0.44444), Js(0.09426), Js(0.0), Js(0.64999)]),'111':Js([Js(0.0), Js(0.44444), Js(0.07861), Js(0.0), Js(0.59111)]),'112':Js([Js(0.19444), Js(0.44444), Js(0.07861), Js(0.0), Js(0.59111)]),'113':Js([Js(0.19444), Js(0.44444), Js(0.105), Js(0.0), Js(0.53222)]),'114':Js([Js(0.0), Js(0.44444), Js(0.11111), Js(0.0), Js(0.50167)]),'115':Js([Js(0.0), Js(0.44444), Js(0.08167), Js(0.0), Js(0.48694)]),'116':Js([Js(0.0), Js(0.63492), Js(0.09639), Js(0.0), Js(0.385)]),'117':Js([Js(0.0), Js(0.44444), Js(0.09426), Js(0.0), Js(0.62055)]),'118':Js([Js(0.0), Js(0.44444), Js(0.11111), Js(0.0), Js(0.53222)]),'119':Js([Js(0.0), Js(0.44444), Js(0.11111), Js(0.0), Js(0.76777)]),'120':Js([Js(0.0), Js(0.44444), Js(0.12583), Js(0.0), Js(0.56055)]),'121':Js([Js(0.19444), Js(0.44444), Js(0.105), Js(0.0), Js(0.56166)]),'122':Js([Js(0.0), Js(0.44444), Js(0.13889), Js(0.0), Js(0.49055)]),'126':Js([Js(0.35), Js(0.34444), Js(0.11472), Js(0.0), Js(0.59111)]),'163':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.86853)]),'168':Js([Js(0.0), Js(0.69444), Js(0.11473), Js(0.0), Js(0.59111)]),'176':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.94888)]),'184':Js([Js(0.17014), Js(0.0), Js(0.0), Js(0.0), Js(0.53222)]),'198':Js([Js(0.0), Js(0.68611), Js(0.11431), Js(0.0), Js(1.02277)]),'216':Js([Js(0.04861), Js(0.73472), Js(0.09062), Js(0.0), Js(0.88555)]),'223':Js([Js(0.19444), Js(0.69444), Js(0.09736), Js(0.0), Js(0.665)]),'230':Js([Js(0.0), Js(0.44444), Js(0.085), Js(0.0), Js(0.82666)]),'248':Js([Js(0.09722), Js(0.54167), Js(0.09458), Js(0.0), Js(0.59111)]),'305':Js([Js(0.0), Js(0.44444), Js(0.09426), Js(0.0), Js(0.35555)]),'338':Js([Js(0.0), Js(0.68611), Js(0.11431), Js(0.0), Js(1.14054)]),'339':Js([Js(0.0), Js(0.44444), Js(0.085), Js(0.0), Js(0.82666)]),'567':Js([Js(0.19444), Js(0.44444), Js(0.04611), Js(0.0), Js(0.385)]),'710':Js([Js(0.0), Js(0.69444), Js(0.06709), Js(0.0), Js(0.59111)]),'711':Js([Js(0.0), Js(0.63194), Js(0.08271), Js(0.0), Js(0.59111)]),'713':Js([Js(0.0), Js(0.59444), Js(0.10444), Js(0.0), Js(0.59111)]),'714':Js([Js(0.0), Js(0.69444), Js(0.08528), Js(0.0), Js(0.59111)]),'715':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.59111)]),'728':Js([Js(0.0), Js(0.69444), Js(0.10333), Js(0.0), Js(0.59111)]),'729':Js([Js(0.0), Js(0.69444), Js(0.12945), Js(0.0), Js(0.35555)]),'730':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.94888)]),'732':Js([Js(0.0), Js(0.69444), Js(0.11472), Js(0.0), Js(0.59111)]),'733':Js([Js(0.0), Js(0.69444), Js(0.11472), Js(0.0), Js(0.59111)]),'915':Js([Js(0.0), Js(0.68611), Js(0.12903), Js(0.0), Js(0.69777)]),'916':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.94444)]),'920':Js([Js(0.0), Js(0.68611), Js(0.09062), Js(0.0), Js(0.88555)]),'923':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.80666)]),'926':Js([Js(0.0), Js(0.68611), Js(0.15092), Js(0.0), Js(0.76777)]),'928':Js([Js(0.0), Js(0.68611), Js(0.17208), Js(0.0), Js(0.8961)]),'931':Js([Js(0.0), Js(0.68611), Js(0.11431), Js(0.0), Js(0.82666)]),'933':Js([Js(0.0), Js(0.68611), Js(0.10778), Js(0.0), Js(0.88555)]),'934':Js([Js(0.0), Js(0.68611), Js(0.05632), Js(0.0), Js(0.82666)]),'936':Js([Js(0.0), Js(0.68611), Js(0.10778), Js(0.0), Js(0.88555)]),'937':Js([Js(0.0), Js(0.68611), Js(0.0992), Js(0.0), Js(0.82666)]),'8211':Js([Js(0.0), Js(0.44444), Js(0.09811), Js(0.0), Js(0.59111)]),'8212':Js([Js(0.0), Js(0.44444), Js(0.09811), Js(0.0), Js(1.18221)]),'8216':Js([Js(0.0), Js(0.69444), Js(0.12945), Js(0.0), Js(0.35555)]),'8217':Js([Js(0.0), Js(0.69444), Js(0.12945), Js(0.0), Js(0.35555)]),'8220':Js([Js(0.0), Js(0.69444), Js(0.16772), Js(0.0), Js(0.62055)]),'8221':Js([Js(0.0), Js(0.69444), Js(0.07939), Js(0.0), Js(0.62055)])}),'Main-Italic':Js({'33':Js([Js(0.0), Js(0.69444), Js(0.12417), Js(0.0), Js(0.30667)]),'34':Js([Js(0.0), Js(0.69444), Js(0.06961), Js(0.0), Js(0.51444)]),'35':Js([Js(0.19444), Js(0.69444), Js(0.06616), Js(0.0), Js(0.81777)]),'37':Js([Js(0.05556), Js(0.75), Js(0.13639), Js(0.0), Js(0.81777)]),'38':Js([Js(0.0), Js(0.69444), Js(0.09694), Js(0.0), Js(0.76666)]),'39':Js([Js(0.0), Js(0.69444), Js(0.12417), Js(0.0), Js(0.30667)]),'40':Js([Js(0.25), Js(0.75), Js(0.16194), Js(0.0), Js(0.40889)]),'41':Js([Js(0.25), Js(0.75), Js(0.03694), Js(0.0), Js(0.40889)]),'42':Js([Js(0.0), Js(0.75), Js(0.14917), Js(0.0), Js(0.51111)]),'43':Js([Js(0.05667), Js(0.56167), Js(0.03694), Js(0.0), Js(0.76666)]),'44':Js([Js(0.19444), Js(0.10556), Js(0.0), Js(0.0), Js(0.30667)]),'45':Js([Js(0.0), Js(0.43056), Js(0.02826), Js(0.0), Js(0.35778)]),'46':Js([Js(0.0), Js(0.10556), Js(0.0), Js(0.0), Js(0.30667)]),'47':Js([Js(0.25), Js(0.75), Js(0.16194), Js(0.0), Js(0.51111)]),'48':Js([Js(0.0), Js(0.64444), Js(0.13556), Js(0.0), Js(0.51111)]),'49':Js([Js(0.0), Js(0.64444), Js(0.13556), Js(0.0), Js(0.51111)]),'50':Js([Js(0.0), Js(0.64444), Js(0.13556), Js(0.0), Js(0.51111)]),'51':Js([Js(0.0), Js(0.64444), Js(0.13556), Js(0.0), Js(0.51111)]),'52':Js([Js(0.19444), Js(0.64444), Js(0.13556), Js(0.0), Js(0.51111)]),'53':Js([Js(0.0), Js(0.64444), Js(0.13556), Js(0.0), Js(0.51111)]),'54':Js([Js(0.0), Js(0.64444), Js(0.13556), Js(0.0), Js(0.51111)]),'55':Js([Js(0.19444), Js(0.64444), Js(0.13556), Js(0.0), Js(0.51111)]),'56':Js([Js(0.0), Js(0.64444), Js(0.13556), Js(0.0), Js(0.51111)]),'57':Js([Js(0.0), Js(0.64444), Js(0.13556), Js(0.0), Js(0.51111)]),'58':Js([Js(0.0), Js(0.43056), Js(0.0582), Js(0.0), Js(0.30667)]),'59':Js([Js(0.19444), Js(0.43056), Js(0.0582), Js(0.0), Js(0.30667)]),'61':Js([(-Js(0.13313)), Js(0.36687), Js(0.06616), Js(0.0), Js(0.76666)]),'63':Js([Js(0.0), Js(0.69444), Js(0.1225), Js(0.0), Js(0.51111)]),'64':Js([Js(0.0), Js(0.69444), Js(0.09597), Js(0.0), Js(0.76666)]),'65':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.74333)]),'66':Js([Js(0.0), Js(0.68333), Js(0.10257), Js(0.0), Js(0.70389)]),'67':Js([Js(0.0), Js(0.68333), Js(0.14528), Js(0.0), Js(0.71555)]),'68':Js([Js(0.0), Js(0.68333), Js(0.09403), Js(0.0), Js(0.755)]),'69':Js([Js(0.0), Js(0.68333), Js(0.12028), Js(0.0), Js(0.67833)]),'70':Js([Js(0.0), Js(0.68333), Js(0.13305), Js(0.0), Js(0.65277)]),'71':Js([Js(0.0), Js(0.68333), Js(0.08722), Js(0.0), Js(0.77361)]),'72':Js([Js(0.0), Js(0.68333), Js(0.16389), Js(0.0), Js(0.74333)]),'73':Js([Js(0.0), Js(0.68333), Js(0.15806), Js(0.0), Js(0.38555)]),'74':Js([Js(0.0), Js(0.68333), Js(0.14028), Js(0.0), Js(0.525)]),'75':Js([Js(0.0), Js(0.68333), Js(0.14528), Js(0.0), Js(0.76888)]),'76':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.62722)]),'77':Js([Js(0.0), Js(0.68333), Js(0.16389), Js(0.0), Js(0.89666)]),'78':Js([Js(0.0), Js(0.68333), Js(0.16389), Js(0.0), Js(0.74333)]),'79':Js([Js(0.0), Js(0.68333), Js(0.09403), Js(0.0), Js(0.76666)]),'80':Js([Js(0.0), Js(0.68333), Js(0.10257), Js(0.0), Js(0.67833)]),'81':Js([Js(0.19444), Js(0.68333), Js(0.09403), Js(0.0), Js(0.76666)]),'82':Js([Js(0.0), Js(0.68333), Js(0.03868), Js(0.0), Js(0.72944)]),'83':Js([Js(0.0), Js(0.68333), Js(0.11972), Js(0.0), Js(0.56222)]),'84':Js([Js(0.0), Js(0.68333), Js(0.13305), Js(0.0), Js(0.71555)]),'85':Js([Js(0.0), Js(0.68333), Js(0.16389), Js(0.0), Js(0.74333)]),'86':Js([Js(0.0), Js(0.68333), Js(0.18361), Js(0.0), Js(0.74333)]),'87':Js([Js(0.0), Js(0.68333), Js(0.18361), Js(0.0), Js(0.99888)]),'88':Js([Js(0.0), Js(0.68333), Js(0.15806), Js(0.0), Js(0.74333)]),'89':Js([Js(0.0), Js(0.68333), Js(0.19383), Js(0.0), Js(0.74333)]),'90':Js([Js(0.0), Js(0.68333), Js(0.14528), Js(0.0), Js(0.61333)]),'91':Js([Js(0.25), Js(0.75), Js(0.1875), Js(0.0), Js(0.30667)]),'93':Js([Js(0.25), Js(0.75), Js(0.10528), Js(0.0), Js(0.30667)]),'94':Js([Js(0.0), Js(0.69444), Js(0.06646), Js(0.0), Js(0.51111)]),'95':Js([Js(0.31), Js(0.12056), Js(0.09208), Js(0.0), Js(0.51111)]),'97':Js([Js(0.0), Js(0.43056), Js(0.07671), Js(0.0), Js(0.51111)]),'98':Js([Js(0.0), Js(0.69444), Js(0.06312), Js(0.0), Js(0.46)]),'99':Js([Js(0.0), Js(0.43056), Js(0.05653), Js(0.0), Js(0.46)]),'100':Js([Js(0.0), Js(0.69444), Js(0.10333), Js(0.0), Js(0.51111)]),'101':Js([Js(0.0), Js(0.43056), Js(0.07514), Js(0.0), Js(0.46)]),'102':Js([Js(0.19444), Js(0.69444), Js(0.21194), Js(0.0), Js(0.30667)]),'103':Js([Js(0.19444), Js(0.43056), Js(0.08847), Js(0.0), Js(0.46)]),'104':Js([Js(0.0), Js(0.69444), Js(0.07671), Js(0.0), Js(0.51111)]),'105':Js([Js(0.0), Js(0.65536), Js(0.1019), Js(0.0), Js(0.30667)]),'106':Js([Js(0.19444), Js(0.65536), Js(0.14467), Js(0.0), Js(0.30667)]),'107':Js([Js(0.0), Js(0.69444), Js(0.10764), Js(0.0), Js(0.46)]),'108':Js([Js(0.0), Js(0.69444), Js(0.10333), Js(0.0), Js(0.25555)]),'109':Js([Js(0.0), Js(0.43056), Js(0.07671), Js(0.0), Js(0.81777)]),'110':Js([Js(0.0), Js(0.43056), Js(0.07671), Js(0.0), Js(0.56222)]),'111':Js([Js(0.0), Js(0.43056), Js(0.06312), Js(0.0), Js(0.51111)]),'112':Js([Js(0.19444), Js(0.43056), Js(0.06312), Js(0.0), Js(0.51111)]),'113':Js([Js(0.19444), Js(0.43056), Js(0.08847), Js(0.0), Js(0.46)]),'114':Js([Js(0.0), Js(0.43056), Js(0.10764), Js(0.0), Js(0.42166)]),'115':Js([Js(0.0), Js(0.43056), Js(0.08208), Js(0.0), Js(0.40889)]),'116':Js([Js(0.0), Js(0.61508), Js(0.09486), Js(0.0), Js(0.33222)]),'117':Js([Js(0.0), Js(0.43056), Js(0.07671), Js(0.0), Js(0.53666)]),'118':Js([Js(0.0), Js(0.43056), Js(0.10764), Js(0.0), Js(0.46)]),'119':Js([Js(0.0), Js(0.43056), Js(0.10764), Js(0.0), Js(0.66444)]),'120':Js([Js(0.0), Js(0.43056), Js(0.12042), Js(0.0), Js(0.46389)]),'121':Js([Js(0.19444), Js(0.43056), Js(0.08847), Js(0.0), Js(0.48555)]),'122':Js([Js(0.0), Js(0.43056), Js(0.12292), Js(0.0), Js(0.40889)]),'126':Js([Js(0.35), Js(0.31786), Js(0.11585), Js(0.0), Js(0.51111)]),'163':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.76909)]),'168':Js([Js(0.0), Js(0.66786), Js(0.10474), Js(0.0), Js(0.51111)]),'176':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.83129)]),'184':Js([Js(0.17014), Js(0.0), Js(0.0), Js(0.0), Js(0.46)]),'198':Js([Js(0.0), Js(0.68333), Js(0.12028), Js(0.0), Js(0.88277)]),'216':Js([Js(0.04861), Js(0.73194), Js(0.09403), Js(0.0), Js(0.76666)]),'223':Js([Js(0.19444), Js(0.69444), Js(0.10514), Js(0.0), Js(0.53666)]),'230':Js([Js(0.0), Js(0.43056), Js(0.07514), Js(0.0), Js(0.71555)]),'248':Js([Js(0.09722), Js(0.52778), Js(0.09194), Js(0.0), Js(0.51111)]),'305':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.02778), Js(0.32246)]),'338':Js([Js(0.0), Js(0.68333), Js(0.12028), Js(0.0), Js(0.98499)]),'339':Js([Js(0.0), Js(0.43056), Js(0.07514), Js(0.0), Js(0.71555)]),'567':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.08334), Js(0.38403)]),'710':Js([Js(0.0), Js(0.69444), Js(0.06646), Js(0.0), Js(0.51111)]),'711':Js([Js(0.0), Js(0.62847), Js(0.08295), Js(0.0), Js(0.51111)]),'713':Js([Js(0.0), Js(0.56167), Js(0.10333), Js(0.0), Js(0.51111)]),'714':Js([Js(0.0), Js(0.69444), Js(0.09694), Js(0.0), Js(0.51111)]),'715':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.51111)]),'728':Js([Js(0.0), Js(0.69444), Js(0.10806), Js(0.0), Js(0.51111)]),'729':Js([Js(0.0), Js(0.66786), Js(0.11752), Js(0.0), Js(0.30667)]),'730':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.83129)]),'732':Js([Js(0.0), Js(0.66786), Js(0.11585), Js(0.0), Js(0.51111)]),'733':Js([Js(0.0), Js(0.69444), Js(0.1225), Js(0.0), Js(0.51111)]),'915':Js([Js(0.0), Js(0.68333), Js(0.13305), Js(0.0), Js(0.62722)]),'916':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.81777)]),'920':Js([Js(0.0), Js(0.68333), Js(0.09403), Js(0.0), Js(0.76666)]),'923':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.69222)]),'926':Js([Js(0.0), Js(0.68333), Js(0.15294), Js(0.0), Js(0.66444)]),'928':Js([Js(0.0), Js(0.68333), Js(0.16389), Js(0.0), Js(0.74333)]),'931':Js([Js(0.0), Js(0.68333), Js(0.12028), Js(0.0), Js(0.71555)]),'933':Js([Js(0.0), Js(0.68333), Js(0.11111), Js(0.0), Js(0.76666)]),'934':Js([Js(0.0), Js(0.68333), Js(0.05986), Js(0.0), Js(0.71555)]),'936':Js([Js(0.0), Js(0.68333), Js(0.11111), Js(0.0), Js(0.76666)]),'937':Js([Js(0.0), Js(0.68333), Js(0.10257), Js(0.0), Js(0.71555)]),'8211':Js([Js(0.0), Js(0.43056), Js(0.09208), Js(0.0), Js(0.51111)]),'8212':Js([Js(0.0), Js(0.43056), Js(0.09208), Js(0.0), Js(1.02222)]),'8216':Js([Js(0.0), Js(0.69444), Js(0.12417), Js(0.0), Js(0.30667)]),'8217':Js([Js(0.0), Js(0.69444), Js(0.12417), Js(0.0), Js(0.30667)]),'8220':Js([Js(0.0), Js(0.69444), Js(0.1685), Js(0.0), Js(0.51444)]),'8221':Js([Js(0.0), Js(0.69444), Js(0.06961), Js(0.0), Js(0.51444)]),'8463':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.54028)])}),'Main-Regular':Js({'32':Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.25)]),'33':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.27778)]),'34':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'35':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.83334)]),'36':Js([Js(0.05556), Js(0.75), Js(0.0), Js(0.0), Js(0.5)]),'37':Js([Js(0.05556), Js(0.75), Js(0.0), Js(0.0), Js(0.83334)]),'38':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.77778)]),'39':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.27778)]),'40':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.38889)]),'41':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.38889)]),'42':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0), Js(0.5)]),'43':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0), Js(0.77778)]),'44':Js([Js(0.19444), Js(0.10556), Js(0.0), Js(0.0), Js(0.27778)]),'45':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.33333)]),'46':Js([Js(0.0), Js(0.10556), Js(0.0), Js(0.0), Js(0.27778)]),'47':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.5)]),'48':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.5)]),'49':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.5)]),'50':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.5)]),'51':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.5)]),'52':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.5)]),'53':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.5)]),'54':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.5)]),'55':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.5)]),'56':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.5)]),'57':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0), Js(0.5)]),'58':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.27778)]),'59':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0), Js(0.27778)]),'60':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0), Js(0.77778)]),'61':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(0.77778)]),'62':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0), Js(0.77778)]),'63':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.47222)]),'64':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.77778)]),'65':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.75)]),'66':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.70834)]),'67':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.72222)]),'68':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.76389)]),'69':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.68056)]),'70':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.65278)]),'71':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.78472)]),'72':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.75)]),'73':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.36111)]),'74':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.51389)]),'75':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.77778)]),'76':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.625)]),'77':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.91667)]),'78':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.75)]),'79':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.77778)]),'80':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.68056)]),'81':Js([Js(0.19444), Js(0.68333), Js(0.0), Js(0.0), Js(0.77778)]),'82':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.73611)]),'83':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.55556)]),'84':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.72222)]),'85':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.75)]),'86':Js([Js(0.0), Js(0.68333), Js(0.01389), Js(0.0), Js(0.75)]),'87':Js([Js(0.0), Js(0.68333), Js(0.01389), Js(0.0), Js(1.02778)]),'88':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.75)]),'89':Js([Js(0.0), Js(0.68333), Js(0.025), Js(0.0), Js(0.75)]),'90':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.61111)]),'91':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.27778)]),'92':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.5)]),'93':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.27778)]),'94':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'95':Js([Js(0.31), Js(0.12056), Js(0.02778), Js(0.0), Js(0.5)]),'97':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.5)]),'98':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55556)]),'99':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.44445)]),'100':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55556)]),'101':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.44445)]),'102':Js([Js(0.0), Js(0.69444), Js(0.07778), Js(0.0), Js(0.30556)]),'103':Js([Js(0.19444), Js(0.43056), Js(0.01389), Js(0.0), Js(0.5)]),'104':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55556)]),'105':Js([Js(0.0), Js(0.66786), Js(0.0), Js(0.0), Js(0.27778)]),'106':Js([Js(0.19444), Js(0.66786), Js(0.0), Js(0.0), Js(0.30556)]),'107':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.52778)]),'108':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.27778)]),'109':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.83334)]),'110':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.55556)]),'111':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.5)]),'112':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0), Js(0.55556)]),'113':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0), Js(0.52778)]),'114':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.39167)]),'115':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.39445)]),'116':Js([Js(0.0), Js(0.61508), Js(0.0), Js(0.0), Js(0.38889)]),'117':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.55556)]),'118':Js([Js(0.0), Js(0.43056), Js(0.01389), Js(0.0), Js(0.52778)]),'119':Js([Js(0.0), Js(0.43056), Js(0.01389), Js(0.0), Js(0.72222)]),'120':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.52778)]),'121':Js([Js(0.19444), Js(0.43056), Js(0.01389), Js(0.0), Js(0.52778)]),'122':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.44445)]),'123':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.5)]),'124':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.27778)]),'125':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.5)]),'126':Js([Js(0.35), Js(0.31786), Js(0.0), Js(0.0), Js(0.5)]),'160':Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.25)]),'167':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.44445)]),'168':Js([Js(0.0), Js(0.66786), Js(0.0), Js(0.0), Js(0.5)]),'172':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.66667)]),'176':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.75)]),'177':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0), Js(0.77778)]),'182':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.61111)]),'184':Js([Js(0.17014), Js(0.0), Js(0.0), Js(0.0), Js(0.44445)]),'198':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.90278)]),'215':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0), Js(0.77778)]),'216':Js([Js(0.04861), Js(0.73194), Js(0.0), Js(0.0), Js(0.77778)]),'223':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'230':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.72222)]),'247':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0), Js(0.77778)]),'248':Js([Js(0.09722), Js(0.52778), Js(0.0), Js(0.0), Js(0.5)]),'305':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.27778)]),'338':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(1.01389)]),'339':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.77778)]),'567':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0), Js(0.30556)]),'710':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'711':Js([Js(0.0), Js(0.62847), Js(0.0), Js(0.0), Js(0.5)]),'713':Js([Js(0.0), Js(0.56778), Js(0.0), Js(0.0), Js(0.5)]),'714':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'715':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'728':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'729':Js([Js(0.0), Js(0.66786), Js(0.0), Js(0.0), Js(0.27778)]),'730':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.75)]),'732':Js([Js(0.0), Js(0.66786), Js(0.0), Js(0.0), Js(0.5)]),'733':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'915':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.625)]),'916':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.83334)]),'920':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.77778)]),'923':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.69445)]),'926':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.66667)]),'928':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.75)]),'931':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.72222)]),'933':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.77778)]),'934':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.72222)]),'936':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.77778)]),'937':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.72222)]),'8211':Js([Js(0.0), Js(0.43056), Js(0.02778), Js(0.0), Js(0.5)]),'8212':Js([Js(0.0), Js(0.43056), Js(0.02778), Js(0.0), Js(1.0)]),'8216':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.27778)]),'8217':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.27778)]),'8220':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'8221':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'8224':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.44445)]),'8225':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.44445)]),'8230':Js([Js(0.0), Js(0.12), Js(0.0), Js(0.0), Js(1.172)]),'8242':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0), Js(0.275)]),'8407':Js([Js(0.0), Js(0.71444), Js(0.15382), Js(0.0), Js(0.5)]),'8463':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0), Js(0.54028)]),'8465':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.72222)]),'8467':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.11111), Js(0.41667)]),'8472':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.11111), Js(0.63646)]),'8476':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.72222)]),'8501':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.61111)]),'8592':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(1.0)]),'8593':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'8594':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(1.0)]),'8595':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'8596':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(1.0)]),'8597':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.5)]),'8598':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(1.0)]),'8599':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(1.0)]),'8600':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(1.0)]),'8601':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(1.0)]),'8614':Js([Js(0.011), Js(0.511), Js(0.0), Js(0.0), Js(1.0)]),'8617':Js([Js(0.011), Js(0.511), Js(0.0), Js(0.0), Js(1.126)]),'8618':Js([Js(0.011), Js(0.511), Js(0.0), Js(0.0), Js(1.126)]),'8636':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(1.0)]),'8637':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(1.0)]),'8640':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(1.0)]),'8641':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(1.0)]),'8652':Js([Js(0.011), Js(0.671), Js(0.0), Js(0.0), Js(1.0)]),'8656':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(1.0)]),'8657':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.61111)]),'8658':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(1.0)]),'8659':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.61111)]),'8660':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(1.0)]),'8661':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.61111)]),'8704':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55556)]),'8706':Js([Js(0.0), Js(0.69444), Js(0.05556), Js(0.08334), Js(0.5309)]),'8707':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55556)]),'8709':Js([Js(0.05556), Js(0.75), Js(0.0), Js(0.0), Js(0.5)]),'8711':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.83334)]),'8712':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0), Js(0.66667)]),'8715':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0), Js(0.66667)]),'8722':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0), Js(0.77778)]),'8723':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0), Js(0.77778)]),'8725':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.5)]),'8726':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.5)]),'8727':Js([(-Js(0.03472)), Js(0.46528), Js(0.0), Js(0.0), Js(0.5)]),'8728':Js([(-Js(0.05555)), Js(0.44445), Js(0.0), Js(0.0), Js(0.5)]),'8729':Js([(-Js(0.05555)), Js(0.44445), Js(0.0), Js(0.0), Js(0.5)]),'8730':Js([Js(0.2), Js(0.8), Js(0.0), Js(0.0), Js(0.83334)]),'8733':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.77778)]),'8734':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(1.0)]),'8736':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0), Js(0.72222)]),'8739':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.27778)]),'8741':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.5)]),'8743':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0), Js(0.66667)]),'8744':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0), Js(0.66667)]),'8745':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0), Js(0.66667)]),'8746':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0), Js(0.66667)]),'8747':Js([Js(0.19444), Js(0.69444), Js(0.11111), Js(0.0), Js(0.41667)]),'8764':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0), Js(0.77778)]),'8768':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.27778)]),'8771':Js([(-Js(0.03625)), Js(0.46375), Js(0.0), Js(0.0), Js(0.77778)]),'8773':Js([(-Js(0.022)), Js(0.589), Js(0.0), Js(0.0), Js(1.0)]),'8776':Js([(-Js(0.01688)), Js(0.48312), Js(0.0), Js(0.0), Js(0.77778)]),'8781':Js([(-Js(0.03625)), Js(0.46375), Js(0.0), Js(0.0), Js(0.77778)]),'8784':Js([(-Js(0.133)), Js(0.67), Js(0.0), Js(0.0), Js(0.778)]),'8801':Js([(-Js(0.03625)), Js(0.46375), Js(0.0), Js(0.0), Js(0.77778)]),'8804':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0), Js(0.77778)]),'8805':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0), Js(0.77778)]),'8810':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0), Js(1.0)]),'8811':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0), Js(1.0)]),'8826':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0), Js(0.77778)]),'8827':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0), Js(0.77778)]),'8834':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0), Js(0.77778)]),'8835':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0), Js(0.77778)]),'8838':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0), Js(0.77778)]),'8839':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0), Js(0.77778)]),'8846':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0), Js(0.66667)]),'8849':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0), Js(0.77778)]),'8850':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0), Js(0.77778)]),'8851':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0), Js(0.66667)]),'8852':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0), Js(0.66667)]),'8853':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0), Js(0.77778)]),'8854':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0), Js(0.77778)]),'8855':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0), Js(0.77778)]),'8856':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0), Js(0.77778)]),'8857':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0), Js(0.77778)]),'8866':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.61111)]),'8867':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.61111)]),'8868':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.77778)]),'8869':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.77778)]),'8872':Js([Js(0.249), Js(0.75), Js(0.0), Js(0.0), Js(0.867)]),'8900':Js([(-Js(0.05555)), Js(0.44445), Js(0.0), Js(0.0), Js(0.5)]),'8901':Js([(-Js(0.05555)), Js(0.44445), Js(0.0), Js(0.0), Js(0.27778)]),'8902':Js([(-Js(0.03472)), Js(0.46528), Js(0.0), Js(0.0), Js(0.5)]),'8904':Js([Js(0.005), Js(0.505), Js(0.0), Js(0.0), Js(0.9)]),'8942':Js([Js(0.03), Js(0.9), Js(0.0), Js(0.0), Js(0.278)]),'8943':Js([(-Js(0.19)), Js(0.31), Js(0.0), Js(0.0), Js(1.172)]),'8945':Js([(-Js(0.1)), Js(0.82), Js(0.0), Js(0.0), Js(1.282)]),'8968':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.44445)]),'8969':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.44445)]),'8970':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.44445)]),'8971':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.44445)]),'8994':Js([(-Js(0.14236)), Js(0.35764), Js(0.0), Js(0.0), Js(1.0)]),'8995':Js([(-Js(0.14236)), Js(0.35764), Js(0.0), Js(0.0), Js(1.0)]),'9136':Js([Js(0.244), Js(0.744), Js(0.0), Js(0.0), Js(0.412)]),'9137':Js([Js(0.244), Js(0.744), Js(0.0), Js(0.0), Js(0.412)]),'9651':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.88889)]),'9657':Js([(-Js(0.03472)), Js(0.46528), Js(0.0), Js(0.0), Js(0.5)]),'9661':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.88889)]),'9667':Js([(-Js(0.03472)), Js(0.46528), Js(0.0), Js(0.0), Js(0.5)]),'9711':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(1.0)]),'9824':Js([Js(0.12963), Js(0.69444), Js(0.0), Js(0.0), Js(0.77778)]),'9825':Js([Js(0.12963), Js(0.69444), Js(0.0), Js(0.0), Js(0.77778)]),'9826':Js([Js(0.12963), Js(0.69444), Js(0.0), Js(0.0), Js(0.77778)]),'9827':Js([Js(0.12963), Js(0.69444), Js(0.0), Js(0.0), Js(0.77778)]),'9837':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0), Js(0.38889)]),'9838':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.38889)]),'9839':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.38889)]),'10216':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.38889)]),'10217':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.38889)]),'10222':Js([Js(0.244), Js(0.744), Js(0.0), Js(0.0), Js(0.412)]),'10223':Js([Js(0.244), Js(0.744), Js(0.0), Js(0.0), Js(0.412)]),'10229':Js([Js(0.011), Js(0.511), Js(0.0), Js(0.0), Js(1.609)]),'10230':Js([Js(0.011), Js(0.511), Js(0.0), Js(0.0), Js(1.638)]),'10231':Js([Js(0.011), Js(0.511), Js(0.0), Js(0.0), Js(1.859)]),'10232':Js([Js(0.024), Js(0.525), Js(0.0), Js(0.0), Js(1.609)]),'10233':Js([Js(0.024), Js(0.525), Js(0.0), Js(0.0), Js(1.638)]),'10234':Js([Js(0.024), Js(0.525), Js(0.0), Js(0.0), Js(1.858)]),'10236':Js([Js(0.011), Js(0.511), Js(0.0), Js(0.0), Js(1.638)]),'10815':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0), Js(0.75)]),'10927':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0), Js(0.77778)]),'10928':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0), Js(0.77778)]),'57376':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.0)])}),'Math-BoldItalic':Js({'65':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.86944)]),'66':Js([Js(0.0), Js(0.68611), Js(0.04835), Js(0.0), Js(0.8664)]),'67':Js([Js(0.0), Js(0.68611), Js(0.06979), Js(0.0), Js(0.81694)]),'68':Js([Js(0.0), Js(0.68611), Js(0.03194), Js(0.0), Js(0.93812)]),'69':Js([Js(0.0), Js(0.68611), Js(0.05451), Js(0.0), Js(0.81007)]),'70':Js([Js(0.0), Js(0.68611), Js(0.15972), Js(0.0), Js(0.68889)]),'71':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.88673)]),'72':Js([Js(0.0), Js(0.68611), Js(0.08229), Js(0.0), Js(0.98229)]),'73':Js([Js(0.0), Js(0.68611), Js(0.07778), Js(0.0), Js(0.51111)]),'74':Js([Js(0.0), Js(0.68611), Js(0.10069), Js(0.0), Js(0.63125)]),'75':Js([Js(0.0), Js(0.68611), Js(0.06979), Js(0.0), Js(0.97118)]),'76':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.75555)]),'77':Js([Js(0.0), Js(0.68611), Js(0.11424), Js(0.0), Js(1.14201)]),'78':Js([Js(0.0), Js(0.68611), Js(0.11424), Js(0.0), Js(0.95034)]),'79':Js([Js(0.0), Js(0.68611), Js(0.03194), Js(0.0), Js(0.83666)]),'80':Js([Js(0.0), Js(0.68611), Js(0.15972), Js(0.0), Js(0.72309)]),'81':Js([Js(0.19444), Js(0.68611), Js(0.0), Js(0.0), Js(0.86861)]),'82':Js([Js(0.0), Js(0.68611), Js(0.00421), Js(0.0), Js(0.87235)]),'83':Js([Js(0.0), Js(0.68611), Js(0.05382), Js(0.0), Js(0.69271)]),'84':Js([Js(0.0), Js(0.68611), Js(0.15972), Js(0.0), Js(0.63663)]),'85':Js([Js(0.0), Js(0.68611), Js(0.11424), Js(0.0), Js(0.80027)]),'86':Js([Js(0.0), Js(0.68611), Js(0.25555), Js(0.0), Js(0.67778)]),'87':Js([Js(0.0), Js(0.68611), Js(0.15972), Js(0.0), Js(1.09305)]),'88':Js([Js(0.0), Js(0.68611), Js(0.07778), Js(0.0), Js(0.94722)]),'89':Js([Js(0.0), Js(0.68611), Js(0.25555), Js(0.0), Js(0.67458)]),'90':Js([Js(0.0), Js(0.68611), Js(0.06979), Js(0.0), Js(0.77257)]),'97':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.63287)]),'98':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.52083)]),'99':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.51342)]),'100':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.60972)]),'101':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.55361)]),'102':Js([Js(0.19444), Js(0.69444), Js(0.11042), Js(0.0), Js(0.56806)]),'103':Js([Js(0.19444), Js(0.44444), Js(0.03704), Js(0.0), Js(0.5449)]),'104':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.66759)]),'105':Js([Js(0.0), Js(0.69326), Js(0.0), Js(0.0), Js(0.4048)]),'106':Js([Js(0.19444), Js(0.69326), Js(0.0622), Js(0.0), Js(0.47083)]),'107':Js([Js(0.0), Js(0.69444), Js(0.01852), Js(0.0), Js(0.6037)]),'108':Js([Js(0.0), Js(0.69444), Js(0.0088), Js(0.0), Js(0.34815)]),'109':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(1.0324)]),'110':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.71296)]),'111':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.58472)]),'112':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0), Js(0.60092)]),'113':Js([Js(0.19444), Js(0.44444), Js(0.03704), Js(0.0), Js(0.54213)]),'114':Js([Js(0.0), Js(0.44444), Js(0.03194), Js(0.0), Js(0.5287)]),'115':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.53125)]),'116':Js([Js(0.0), Js(0.63492), Js(0.0), Js(0.0), Js(0.41528)]),'117':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.68102)]),'118':Js([Js(0.0), Js(0.44444), Js(0.03704), Js(0.0), Js(0.56666)]),'119':Js([Js(0.0), Js(0.44444), Js(0.02778), Js(0.0), Js(0.83148)]),'120':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.65903)]),'121':Js([Js(0.19444), Js(0.44444), Js(0.03704), Js(0.0), Js(0.59028)]),'122':Js([Js(0.0), Js(0.44444), Js(0.04213), Js(0.0), Js(0.55509)]),'915':Js([Js(0.0), Js(0.68611), Js(0.15972), Js(0.0), Js(0.65694)]),'916':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.95833)]),'920':Js([Js(0.0), Js(0.68611), Js(0.03194), Js(0.0), Js(0.86722)]),'923':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.80555)]),'926':Js([Js(0.0), Js(0.68611), Js(0.07458), Js(0.0), Js(0.84125)]),'928':Js([Js(0.0), Js(0.68611), Js(0.08229), Js(0.0), Js(0.98229)]),'931':Js([Js(0.0), Js(0.68611), Js(0.05451), Js(0.0), Js(0.88507)]),'933':Js([Js(0.0), Js(0.68611), Js(0.15972), Js(0.0), Js(0.67083)]),'934':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0), Js(0.76666)]),'936':Js([Js(0.0), Js(0.68611), Js(0.11653), Js(0.0), Js(0.71402)]),'937':Js([Js(0.0), Js(0.68611), Js(0.04835), Js(0.0), Js(0.8789)]),'945':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.76064)]),'946':Js([Js(0.19444), Js(0.69444), Js(0.03403), Js(0.0), Js(0.65972)]),'947':Js([Js(0.19444), Js(0.44444), Js(0.06389), Js(0.0), Js(0.59003)]),'948':Js([Js(0.0), Js(0.69444), Js(0.03819), Js(0.0), Js(0.52222)]),'949':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.52882)]),'950':Js([Js(0.19444), Js(0.69444), Js(0.06215), Js(0.0), Js(0.50833)]),'951':Js([Js(0.19444), Js(0.44444), Js(0.03704), Js(0.0), Js(0.6)]),'952':Js([Js(0.0), Js(0.69444), Js(0.03194), Js(0.0), Js(0.5618)]),'953':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.41204)]),'954':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.66759)]),'955':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.67083)]),'956':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0), Js(0.70787)]),'957':Js([Js(0.0), Js(0.44444), Js(0.06898), Js(0.0), Js(0.57685)]),'958':Js([Js(0.19444), Js(0.69444), Js(0.03021), Js(0.0), Js(0.50833)]),'959':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.58472)]),'960':Js([Js(0.0), Js(0.44444), Js(0.03704), Js(0.0), Js(0.68241)]),'961':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0), Js(0.6118)]),'962':Js([Js(0.09722), Js(0.44444), Js(0.07917), Js(0.0), Js(0.42361)]),'963':Js([Js(0.0), Js(0.44444), Js(0.03704), Js(0.0), Js(0.68588)]),'964':Js([Js(0.0), Js(0.44444), Js(0.13472), Js(0.0), Js(0.52083)]),'965':Js([Js(0.0), Js(0.44444), Js(0.03704), Js(0.0), Js(0.63055)]),'966':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0), Js(0.74722)]),'967':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0), Js(0.71805)]),'968':Js([Js(0.19444), Js(0.69444), Js(0.03704), Js(0.0), Js(0.75833)]),'969':Js([Js(0.0), Js(0.44444), Js(0.03704), Js(0.0), Js(0.71782)]),'977':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.69155)]),'981':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.7125)]),'982':Js([Js(0.0), Js(0.44444), Js(0.03194), Js(0.0), Js(0.975)]),'1009':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0), Js(0.6118)]),'1013':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.48333)])}),'Math-Italic':Js({'65':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.13889), Js(0.75)]),'66':Js([Js(0.0), Js(0.68333), Js(0.05017), Js(0.08334), Js(0.75851)]),'67':Js([Js(0.0), Js(0.68333), Js(0.07153), Js(0.08334), Js(0.71472)]),'68':Js([Js(0.0), Js(0.68333), Js(0.02778), Js(0.05556), Js(0.82792)]),'69':Js([Js(0.0), Js(0.68333), Js(0.05764), Js(0.08334), Js(0.7382)]),'70':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.08334), Js(0.64306)]),'71':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.08334), Js(0.78625)]),'72':Js([Js(0.0), Js(0.68333), Js(0.08125), Js(0.05556), Js(0.83125)]),'73':Js([Js(0.0), Js(0.68333), Js(0.07847), Js(0.11111), Js(0.43958)]),'74':Js([Js(0.0), Js(0.68333), Js(0.09618), Js(0.16667), Js(0.55451)]),'75':Js([Js(0.0), Js(0.68333), Js(0.07153), Js(0.05556), Js(0.84931)]),'76':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.02778), Js(0.68056)]),'77':Js([Js(0.0), Js(0.68333), Js(0.10903), Js(0.08334), Js(0.97014)]),'78':Js([Js(0.0), Js(0.68333), Js(0.10903), Js(0.08334), Js(0.80347)]),'79':Js([Js(0.0), Js(0.68333), Js(0.02778), Js(0.08334), Js(0.76278)]),'80':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.08334), Js(0.64201)]),'81':Js([Js(0.19444), Js(0.68333), Js(0.0), Js(0.08334), Js(0.79056)]),'82':Js([Js(0.0), Js(0.68333), Js(0.00773), Js(0.08334), Js(0.75929)]),'83':Js([Js(0.0), Js(0.68333), Js(0.05764), Js(0.08334), Js(0.6132)]),'84':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.08334), Js(0.58438)]),'85':Js([Js(0.0), Js(0.68333), Js(0.10903), Js(0.02778), Js(0.68278)]),'86':Js([Js(0.0), Js(0.68333), Js(0.22222), Js(0.0), Js(0.58333)]),'87':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.0), Js(0.94445)]),'88':Js([Js(0.0), Js(0.68333), Js(0.07847), Js(0.08334), Js(0.82847)]),'89':Js([Js(0.0), Js(0.68333), Js(0.22222), Js(0.0), Js(0.58056)]),'90':Js([Js(0.0), Js(0.68333), Js(0.07153), Js(0.08334), Js(0.68264)]),'97':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.52859)]),'98':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.42917)]),'99':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556), Js(0.43276)]),'100':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.16667), Js(0.52049)]),'101':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556), Js(0.46563)]),'102':Js([Js(0.19444), Js(0.69444), Js(0.10764), Js(0.16667), Js(0.48959)]),'103':Js([Js(0.19444), Js(0.43056), Js(0.03588), Js(0.02778), Js(0.47697)]),'104':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.57616)]),'105':Js([Js(0.0), Js(0.65952), Js(0.0), Js(0.0), Js(0.34451)]),'106':Js([Js(0.19444), Js(0.65952), Js(0.05724), Js(0.0), Js(0.41181)]),'107':Js([Js(0.0), Js(0.69444), Js(0.03148), Js(0.0), Js(0.5206)]),'108':Js([Js(0.0), Js(0.69444), Js(0.01968), Js(0.08334), Js(0.29838)]),'109':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.87801)]),'110':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.60023)]),'111':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556), Js(0.48472)]),'112':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.08334), Js(0.50313)]),'113':Js([Js(0.19444), Js(0.43056), Js(0.03588), Js(0.08334), Js(0.44641)]),'114':Js([Js(0.0), Js(0.43056), Js(0.02778), Js(0.05556), Js(0.45116)]),'115':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556), Js(0.46875)]),'116':Js([Js(0.0), Js(0.61508), Js(0.0), Js(0.08334), Js(0.36111)]),'117':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.02778), Js(0.57246)]),'118':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.02778), Js(0.48472)]),'119':Js([Js(0.0), Js(0.43056), Js(0.02691), Js(0.08334), Js(0.71592)]),'120':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.02778), Js(0.57153)]),'121':Js([Js(0.19444), Js(0.43056), Js(0.03588), Js(0.05556), Js(0.49028)]),'122':Js([Js(0.0), Js(0.43056), Js(0.04398), Js(0.05556), Js(0.46505)]),'915':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.08334), Js(0.61528)]),'916':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.16667), Js(0.83334)]),'920':Js([Js(0.0), Js(0.68333), Js(0.02778), Js(0.08334), Js(0.76278)]),'923':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.16667), Js(0.69445)]),'926':Js([Js(0.0), Js(0.68333), Js(0.07569), Js(0.08334), Js(0.74236)]),'928':Js([Js(0.0), Js(0.68333), Js(0.08125), Js(0.05556), Js(0.83125)]),'931':Js([Js(0.0), Js(0.68333), Js(0.05764), Js(0.08334), Js(0.77986)]),'933':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.05556), Js(0.58333)]),'934':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.08334), Js(0.66667)]),'936':Js([Js(0.0), Js(0.68333), Js(0.11), Js(0.05556), Js(0.61222)]),'937':Js([Js(0.0), Js(0.68333), Js(0.05017), Js(0.08334), Js(0.7724)]),'945':Js([Js(0.0), Js(0.43056), Js(0.0037), Js(0.02778), Js(0.6397)]),'946':Js([Js(0.19444), Js(0.69444), Js(0.05278), Js(0.08334), Js(0.56563)]),'947':Js([Js(0.19444), Js(0.43056), Js(0.05556), Js(0.0), Js(0.51773)]),'948':Js([Js(0.0), Js(0.69444), Js(0.03785), Js(0.05556), Js(0.44444)]),'949':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.08334), Js(0.46632)]),'950':Js([Js(0.19444), Js(0.69444), Js(0.07378), Js(0.08334), Js(0.4375)]),'951':Js([Js(0.19444), Js(0.43056), Js(0.03588), Js(0.05556), Js(0.49653)]),'952':Js([Js(0.0), Js(0.69444), Js(0.02778), Js(0.08334), Js(0.46944)]),'953':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556), Js(0.35394)]),'954':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.57616)]),'955':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.58334)]),'956':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.02778), Js(0.60255)]),'957':Js([Js(0.0), Js(0.43056), Js(0.06366), Js(0.02778), Js(0.49398)]),'958':Js([Js(0.19444), Js(0.69444), Js(0.04601), Js(0.11111), Js(0.4375)]),'959':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556), Js(0.48472)]),'960':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.0), Js(0.57003)]),'961':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.08334), Js(0.51702)]),'962':Js([Js(0.09722), Js(0.43056), Js(0.07986), Js(0.08334), Js(0.36285)]),'963':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.0), Js(0.57141)]),'964':Js([Js(0.0), Js(0.43056), Js(0.1132), Js(0.02778), Js(0.43715)]),'965':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.02778), Js(0.54028)]),'966':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.08334), Js(0.65417)]),'967':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.05556), Js(0.62569)]),'968':Js([Js(0.19444), Js(0.69444), Js(0.03588), Js(0.11111), Js(0.65139)]),'969':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.0), Js(0.62245)]),'977':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.08334), Js(0.59144)]),'981':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.08334), Js(0.59583)]),'982':Js([Js(0.0), Js(0.43056), Js(0.02778), Js(0.0), Js(0.82813)]),'1009':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.08334), Js(0.51702)]),'1013':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556), Js(0.4059)])}),'Math-Regular':Js({'65':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.13889), Js(0.75)]),'66':Js([Js(0.0), Js(0.68333), Js(0.05017), Js(0.08334), Js(0.75851)]),'67':Js([Js(0.0), Js(0.68333), Js(0.07153), Js(0.08334), Js(0.71472)]),'68':Js([Js(0.0), Js(0.68333), Js(0.02778), Js(0.05556), Js(0.82792)]),'69':Js([Js(0.0), Js(0.68333), Js(0.05764), Js(0.08334), Js(0.7382)]),'70':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.08334), Js(0.64306)]),'71':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.08334), Js(0.78625)]),'72':Js([Js(0.0), Js(0.68333), Js(0.08125), Js(0.05556), Js(0.83125)]),'73':Js([Js(0.0), Js(0.68333), Js(0.07847), Js(0.11111), Js(0.43958)]),'74':Js([Js(0.0), Js(0.68333), Js(0.09618), Js(0.16667), Js(0.55451)]),'75':Js([Js(0.0), Js(0.68333), Js(0.07153), Js(0.05556), Js(0.84931)]),'76':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.02778), Js(0.68056)]),'77':Js([Js(0.0), Js(0.68333), Js(0.10903), Js(0.08334), Js(0.97014)]),'78':Js([Js(0.0), Js(0.68333), Js(0.10903), Js(0.08334), Js(0.80347)]),'79':Js([Js(0.0), Js(0.68333), Js(0.02778), Js(0.08334), Js(0.76278)]),'80':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.08334), Js(0.64201)]),'81':Js([Js(0.19444), Js(0.68333), Js(0.0), Js(0.08334), Js(0.79056)]),'82':Js([Js(0.0), Js(0.68333), Js(0.00773), Js(0.08334), Js(0.75929)]),'83':Js([Js(0.0), Js(0.68333), Js(0.05764), Js(0.08334), Js(0.6132)]),'84':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.08334), Js(0.58438)]),'85':Js([Js(0.0), Js(0.68333), Js(0.10903), Js(0.02778), Js(0.68278)]),'86':Js([Js(0.0), Js(0.68333), Js(0.22222), Js(0.0), Js(0.58333)]),'87':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.0), Js(0.94445)]),'88':Js([Js(0.0), Js(0.68333), Js(0.07847), Js(0.08334), Js(0.82847)]),'89':Js([Js(0.0), Js(0.68333), Js(0.22222), Js(0.0), Js(0.58056)]),'90':Js([Js(0.0), Js(0.68333), Js(0.07153), Js(0.08334), Js(0.68264)]),'97':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.52859)]),'98':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.42917)]),'99':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556), Js(0.43276)]),'100':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.16667), Js(0.52049)]),'101':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556), Js(0.46563)]),'102':Js([Js(0.19444), Js(0.69444), Js(0.10764), Js(0.16667), Js(0.48959)]),'103':Js([Js(0.19444), Js(0.43056), Js(0.03588), Js(0.02778), Js(0.47697)]),'104':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.57616)]),'105':Js([Js(0.0), Js(0.65952), Js(0.0), Js(0.0), Js(0.34451)]),'106':Js([Js(0.19444), Js(0.65952), Js(0.05724), Js(0.0), Js(0.41181)]),'107':Js([Js(0.0), Js(0.69444), Js(0.03148), Js(0.0), Js(0.5206)]),'108':Js([Js(0.0), Js(0.69444), Js(0.01968), Js(0.08334), Js(0.29838)]),'109':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.87801)]),'110':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.60023)]),'111':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556), Js(0.48472)]),'112':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.08334), Js(0.50313)]),'113':Js([Js(0.19444), Js(0.43056), Js(0.03588), Js(0.08334), Js(0.44641)]),'114':Js([Js(0.0), Js(0.43056), Js(0.02778), Js(0.05556), Js(0.45116)]),'115':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556), Js(0.46875)]),'116':Js([Js(0.0), Js(0.61508), Js(0.0), Js(0.08334), Js(0.36111)]),'117':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.02778), Js(0.57246)]),'118':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.02778), Js(0.48472)]),'119':Js([Js(0.0), Js(0.43056), Js(0.02691), Js(0.08334), Js(0.71592)]),'120':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.02778), Js(0.57153)]),'121':Js([Js(0.19444), Js(0.43056), Js(0.03588), Js(0.05556), Js(0.49028)]),'122':Js([Js(0.0), Js(0.43056), Js(0.04398), Js(0.05556), Js(0.46505)]),'915':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.08334), Js(0.61528)]),'916':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.16667), Js(0.83334)]),'920':Js([Js(0.0), Js(0.68333), Js(0.02778), Js(0.08334), Js(0.76278)]),'923':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.16667), Js(0.69445)]),'926':Js([Js(0.0), Js(0.68333), Js(0.07569), Js(0.08334), Js(0.74236)]),'928':Js([Js(0.0), Js(0.68333), Js(0.08125), Js(0.05556), Js(0.83125)]),'931':Js([Js(0.0), Js(0.68333), Js(0.05764), Js(0.08334), Js(0.77986)]),'933':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.05556), Js(0.58333)]),'934':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.08334), Js(0.66667)]),'936':Js([Js(0.0), Js(0.68333), Js(0.11), Js(0.05556), Js(0.61222)]),'937':Js([Js(0.0), Js(0.68333), Js(0.05017), Js(0.08334), Js(0.7724)]),'945':Js([Js(0.0), Js(0.43056), Js(0.0037), Js(0.02778), Js(0.6397)]),'946':Js([Js(0.19444), Js(0.69444), Js(0.05278), Js(0.08334), Js(0.56563)]),'947':Js([Js(0.19444), Js(0.43056), Js(0.05556), Js(0.0), Js(0.51773)]),'948':Js([Js(0.0), Js(0.69444), Js(0.03785), Js(0.05556), Js(0.44444)]),'949':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.08334), Js(0.46632)]),'950':Js([Js(0.19444), Js(0.69444), Js(0.07378), Js(0.08334), Js(0.4375)]),'951':Js([Js(0.19444), Js(0.43056), Js(0.03588), Js(0.05556), Js(0.49653)]),'952':Js([Js(0.0), Js(0.69444), Js(0.02778), Js(0.08334), Js(0.46944)]),'953':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556), Js(0.35394)]),'954':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.57616)]),'955':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.58334)]),'956':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.02778), Js(0.60255)]),'957':Js([Js(0.0), Js(0.43056), Js(0.06366), Js(0.02778), Js(0.49398)]),'958':Js([Js(0.19444), Js(0.69444), Js(0.04601), Js(0.11111), Js(0.4375)]),'959':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556), Js(0.48472)]),'960':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.0), Js(0.57003)]),'961':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.08334), Js(0.51702)]),'962':Js([Js(0.09722), Js(0.43056), Js(0.07986), Js(0.08334), Js(0.36285)]),'963':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.0), Js(0.57141)]),'964':Js([Js(0.0), Js(0.43056), Js(0.1132), Js(0.02778), Js(0.43715)]),'965':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.02778), Js(0.54028)]),'966':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.08334), Js(0.65417)]),'967':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.05556), Js(0.62569)]),'968':Js([Js(0.19444), Js(0.69444), Js(0.03588), Js(0.11111), Js(0.65139)]),'969':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.0), Js(0.62245)]),'977':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.08334), Js(0.59144)]),'981':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.08334), Js(0.59583)]),'982':Js([Js(0.0), Js(0.43056), Js(0.02778), Js(0.0), Js(0.82813)]),'1009':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.08334), Js(0.51702)]),'1013':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556), Js(0.4059)])}),'SansSerif-Bold':Js({'33':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.36667)]),'34':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55834)]),'35':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.91667)]),'36':Js([Js(0.05556), Js(0.75), Js(0.0), Js(0.0), Js(0.55)]),'37':Js([Js(0.05556), Js(0.75), Js(0.0), Js(0.0), Js(1.02912)]),'38':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.83056)]),'39':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.30556)]),'40':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.42778)]),'41':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.42778)]),'42':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0), Js(0.55)]),'43':Js([Js(0.11667), Js(0.61667), Js(0.0), Js(0.0), Js(0.85556)]),'44':Js([Js(0.10556), Js(0.13056), Js(0.0), Js(0.0), Js(0.30556)]),'45':Js([Js(0.0), Js(0.45833), Js(0.0), Js(0.0), Js(0.36667)]),'46':Js([Js(0.0), Js(0.13056), Js(0.0), Js(0.0), Js(0.30556)]),'47':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.55)]),'48':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55)]),'49':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55)]),'50':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55)]),'51':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55)]),'52':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55)]),'53':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55)]),'54':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55)]),'55':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55)]),'56':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55)]),'57':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55)]),'58':Js([Js(0.0), Js(0.45833), Js(0.0), Js(0.0), Js(0.30556)]),'59':Js([Js(0.10556), Js(0.45833), Js(0.0), Js(0.0), Js(0.30556)]),'61':Js([(-Js(0.09375)), Js(0.40625), Js(0.0), Js(0.0), Js(0.85556)]),'63':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.51945)]),'64':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.73334)]),'65':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.73334)]),'66':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.73334)]),'67':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.70278)]),'68':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.79445)]),'69':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.64167)]),'70':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.61111)]),'71':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.73334)]),'72':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.79445)]),'73':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.33056)]),'74':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.51945)]),'75':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.76389)]),'76':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.58056)]),'77':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.97778)]),'78':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.79445)]),'79':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.79445)]),'80':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.70278)]),'81':Js([Js(0.10556), Js(0.69444), Js(0.0), Js(0.0), Js(0.79445)]),'82':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.70278)]),'83':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.61111)]),'84':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.73334)]),'85':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.76389)]),'86':Js([Js(0.0), Js(0.69444), Js(0.01528), Js(0.0), Js(0.73334)]),'87':Js([Js(0.0), Js(0.69444), Js(0.01528), Js(0.0), Js(1.03889)]),'88':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.73334)]),'89':Js([Js(0.0), Js(0.69444), Js(0.0275), Js(0.0), Js(0.73334)]),'90':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.67223)]),'91':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.34306)]),'93':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.34306)]),'94':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55)]),'95':Js([Js(0.35), Js(0.10833), Js(0.03056), Js(0.0), Js(0.55)]),'97':Js([Js(0.0), Js(0.45833), Js(0.0), Js(0.0), Js(0.525)]),'98':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.56111)]),'99':Js([Js(0.0), Js(0.45833), Js(0.0), Js(0.0), Js(0.48889)]),'100':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.56111)]),'101':Js([Js(0.0), Js(0.45833), Js(0.0), Js(0.0), Js(0.51111)]),'102':Js([Js(0.0), Js(0.69444), Js(0.07639), Js(0.0), Js(0.33611)]),'103':Js([Js(0.19444), Js(0.45833), Js(0.01528), Js(0.0), Js(0.55)]),'104':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.56111)]),'105':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.25556)]),'106':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.28611)]),'107':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.53056)]),'108':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.25556)]),'109':Js([Js(0.0), Js(0.45833), Js(0.0), Js(0.0), Js(0.86667)]),'110':Js([Js(0.0), Js(0.45833), Js(0.0), Js(0.0), Js(0.56111)]),'111':Js([Js(0.0), Js(0.45833), Js(0.0), Js(0.0), Js(0.55)]),'112':Js([Js(0.19444), Js(0.45833), Js(0.0), Js(0.0), Js(0.56111)]),'113':Js([Js(0.19444), Js(0.45833), Js(0.0), Js(0.0), Js(0.56111)]),'114':Js([Js(0.0), Js(0.45833), Js(0.01528), Js(0.0), Js(0.37222)]),'115':Js([Js(0.0), Js(0.45833), Js(0.0), Js(0.0), Js(0.42167)]),'116':Js([Js(0.0), Js(0.58929), Js(0.0), Js(0.0), Js(0.40417)]),'117':Js([Js(0.0), Js(0.45833), Js(0.0), Js(0.0), Js(0.56111)]),'118':Js([Js(0.0), Js(0.45833), Js(0.01528), Js(0.0), Js(0.5)]),'119':Js([Js(0.0), Js(0.45833), Js(0.01528), Js(0.0), Js(0.74445)]),'120':Js([Js(0.0), Js(0.45833), Js(0.0), Js(0.0), Js(0.5)]),'121':Js([Js(0.19444), Js(0.45833), Js(0.01528), Js(0.0), Js(0.5)]),'122':Js([Js(0.0), Js(0.45833), Js(0.0), Js(0.0), Js(0.47639)]),'126':Js([Js(0.35), Js(0.34444), Js(0.0), Js(0.0), Js(0.55)]),'168':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55)]),'176':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.73334)]),'180':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55)]),'184':Js([Js(0.17014), Js(0.0), Js(0.0), Js(0.0), Js(0.48889)]),'305':Js([Js(0.0), Js(0.45833), Js(0.0), Js(0.0), Js(0.25556)]),'567':Js([Js(0.19444), Js(0.45833), Js(0.0), Js(0.0), Js(0.28611)]),'710':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55)]),'711':Js([Js(0.0), Js(0.63542), Js(0.0), Js(0.0), Js(0.55)]),'713':Js([Js(0.0), Js(0.63778), Js(0.0), Js(0.0), Js(0.55)]),'728':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55)]),'729':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.30556)]),'730':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.73334)]),'732':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55)]),'733':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55)]),'915':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.58056)]),'916':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.91667)]),'920':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.85556)]),'923':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.67223)]),'926':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.73334)]),'928':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.79445)]),'931':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.79445)]),'933':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.85556)]),'934':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.79445)]),'936':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.85556)]),'937':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.79445)]),'8211':Js([Js(0.0), Js(0.45833), Js(0.03056), Js(0.0), Js(0.55)]),'8212':Js([Js(0.0), Js(0.45833), Js(0.03056), Js(0.0), Js(1.10001)]),'8216':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.30556)]),'8217':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.30556)]),'8220':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55834)]),'8221':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55834)])}),'SansSerif-Italic':Js({'33':Js([Js(0.0), Js(0.69444), Js(0.05733), Js(0.0), Js(0.31945)]),'34':Js([Js(0.0), Js(0.69444), Js(0.00316), Js(0.0), Js(0.5)]),'35':Js([Js(0.19444), Js(0.69444), Js(0.05087), Js(0.0), Js(0.83334)]),'36':Js([Js(0.05556), Js(0.75), Js(0.11156), Js(0.0), Js(0.5)]),'37':Js([Js(0.05556), Js(0.75), Js(0.03126), Js(0.0), Js(0.83334)]),'38':Js([Js(0.0), Js(0.69444), Js(0.03058), Js(0.0), Js(0.75834)]),'39':Js([Js(0.0), Js(0.69444), Js(0.07816), Js(0.0), Js(0.27778)]),'40':Js([Js(0.25), Js(0.75), Js(0.13164), Js(0.0), Js(0.38889)]),'41':Js([Js(0.25), Js(0.75), Js(0.02536), Js(0.0), Js(0.38889)]),'42':Js([Js(0.0), Js(0.75), Js(0.11775), Js(0.0), Js(0.5)]),'43':Js([Js(0.08333), Js(0.58333), Js(0.02536), Js(0.0), Js(0.77778)]),'44':Js([Js(0.125), Js(0.08333), Js(0.0), Js(0.0), Js(0.27778)]),'45':Js([Js(0.0), Js(0.44444), Js(0.01946), Js(0.0), Js(0.33333)]),'46':Js([Js(0.0), Js(0.08333), Js(0.0), Js(0.0), Js(0.27778)]),'47':Js([Js(0.25), Js(0.75), Js(0.13164), Js(0.0), Js(0.5)]),'48':Js([Js(0.0), Js(0.65556), Js(0.11156), Js(0.0), Js(0.5)]),'49':Js([Js(0.0), Js(0.65556), Js(0.11156), Js(0.0), Js(0.5)]),'50':Js([Js(0.0), Js(0.65556), Js(0.11156), Js(0.0), Js(0.5)]),'51':Js([Js(0.0), Js(0.65556), Js(0.11156), Js(0.0), Js(0.5)]),'52':Js([Js(0.0), Js(0.65556), Js(0.11156), Js(0.0), Js(0.5)]),'53':Js([Js(0.0), Js(0.65556), Js(0.11156), Js(0.0), Js(0.5)]),'54':Js([Js(0.0), Js(0.65556), Js(0.11156), Js(0.0), Js(0.5)]),'55':Js([Js(0.0), Js(0.65556), Js(0.11156), Js(0.0), Js(0.5)]),'56':Js([Js(0.0), Js(0.65556), Js(0.11156), Js(0.0), Js(0.5)]),'57':Js([Js(0.0), Js(0.65556), Js(0.11156), Js(0.0), Js(0.5)]),'58':Js([Js(0.0), Js(0.44444), Js(0.02502), Js(0.0), Js(0.27778)]),'59':Js([Js(0.125), Js(0.44444), Js(0.02502), Js(0.0), Js(0.27778)]),'61':Js([(-Js(0.13)), Js(0.37), Js(0.05087), Js(0.0), Js(0.77778)]),'63':Js([Js(0.0), Js(0.69444), Js(0.11809), Js(0.0), Js(0.47222)]),'64':Js([Js(0.0), Js(0.69444), Js(0.07555), Js(0.0), Js(0.66667)]),'65':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.66667)]),'66':Js([Js(0.0), Js(0.69444), Js(0.08293), Js(0.0), Js(0.66667)]),'67':Js([Js(0.0), Js(0.69444), Js(0.11983), Js(0.0), Js(0.63889)]),'68':Js([Js(0.0), Js(0.69444), Js(0.07555), Js(0.0), Js(0.72223)]),'69':Js([Js(0.0), Js(0.69444), Js(0.11983), Js(0.0), Js(0.59722)]),'70':Js([Js(0.0), Js(0.69444), Js(0.13372), Js(0.0), Js(0.56945)]),'71':Js([Js(0.0), Js(0.69444), Js(0.11983), Js(0.0), Js(0.66667)]),'72':Js([Js(0.0), Js(0.69444), Js(0.08094), Js(0.0), Js(0.70834)]),'73':Js([Js(0.0), Js(0.69444), Js(0.13372), Js(0.0), Js(0.27778)]),'74':Js([Js(0.0), Js(0.69444), Js(0.08094), Js(0.0), Js(0.47222)]),'75':Js([Js(0.0), Js(0.69444), Js(0.11983), Js(0.0), Js(0.69445)]),'76':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.54167)]),'77':Js([Js(0.0), Js(0.69444), Js(0.08094), Js(0.0), Js(0.875)]),'78':Js([Js(0.0), Js(0.69444), Js(0.08094), Js(0.0), Js(0.70834)]),'79':Js([Js(0.0), Js(0.69444), Js(0.07555), Js(0.0), Js(0.73611)]),'80':Js([Js(0.0), Js(0.69444), Js(0.08293), Js(0.0), Js(0.63889)]),'81':Js([Js(0.125), Js(0.69444), Js(0.07555), Js(0.0), Js(0.73611)]),'82':Js([Js(0.0), Js(0.69444), Js(0.08293), Js(0.0), Js(0.64584)]),'83':Js([Js(0.0), Js(0.69444), Js(0.09205), Js(0.0), Js(0.55556)]),'84':Js([Js(0.0), Js(0.69444), Js(0.13372), Js(0.0), Js(0.68056)]),'85':Js([Js(0.0), Js(0.69444), Js(0.08094), Js(0.0), Js(0.6875)]),'86':Js([Js(0.0), Js(0.69444), Js(0.1615), Js(0.0), Js(0.66667)]),'87':Js([Js(0.0), Js(0.69444), Js(0.1615), Js(0.0), Js(0.94445)]),'88':Js([Js(0.0), Js(0.69444), Js(0.13372), Js(0.0), Js(0.66667)]),'89':Js([Js(0.0), Js(0.69444), Js(0.17261), Js(0.0), Js(0.66667)]),'90':Js([Js(0.0), Js(0.69444), Js(0.11983), Js(0.0), Js(0.61111)]),'91':Js([Js(0.25), Js(0.75), Js(0.15942), Js(0.0), Js(0.28889)]),'93':Js([Js(0.25), Js(0.75), Js(0.08719), Js(0.0), Js(0.28889)]),'94':Js([Js(0.0), Js(0.69444), Js(0.0799), Js(0.0), Js(0.5)]),'95':Js([Js(0.35), Js(0.09444), Js(0.08616), Js(0.0), Js(0.5)]),'97':Js([Js(0.0), Js(0.44444), Js(0.00981), Js(0.0), Js(0.48056)]),'98':Js([Js(0.0), Js(0.69444), Js(0.03057), Js(0.0), Js(0.51667)]),'99':Js([Js(0.0), Js(0.44444), Js(0.08336), Js(0.0), Js(0.44445)]),'100':Js([Js(0.0), Js(0.69444), Js(0.09483), Js(0.0), Js(0.51667)]),'101':Js([Js(0.0), Js(0.44444), Js(0.06778), Js(0.0), Js(0.44445)]),'102':Js([Js(0.0), Js(0.69444), Js(0.21705), Js(0.0), Js(0.30556)]),'103':Js([Js(0.19444), Js(0.44444), Js(0.10836), Js(0.0), Js(0.5)]),'104':Js([Js(0.0), Js(0.69444), Js(0.01778), Js(0.0), Js(0.51667)]),'105':Js([Js(0.0), Js(0.67937), Js(0.09718), Js(0.0), Js(0.23889)]),'106':Js([Js(0.19444), Js(0.67937), Js(0.09162), Js(0.0), Js(0.26667)]),'107':Js([Js(0.0), Js(0.69444), Js(0.08336), Js(0.0), Js(0.48889)]),'108':Js([Js(0.0), Js(0.69444), Js(0.09483), Js(0.0), Js(0.23889)]),'109':Js([Js(0.0), Js(0.44444), Js(0.01778), Js(0.0), Js(0.79445)]),'110':Js([Js(0.0), Js(0.44444), Js(0.01778), Js(0.0), Js(0.51667)]),'111':Js([Js(0.0), Js(0.44444), Js(0.06613), Js(0.0), Js(0.5)]),'112':Js([Js(0.19444), Js(0.44444), Js(0.0389), Js(0.0), Js(0.51667)]),'113':Js([Js(0.19444), Js(0.44444), Js(0.04169), Js(0.0), Js(0.51667)]),'114':Js([Js(0.0), Js(0.44444), Js(0.10836), Js(0.0), Js(0.34167)]),'115':Js([Js(0.0), Js(0.44444), Js(0.0778), Js(0.0), Js(0.38333)]),'116':Js([Js(0.0), Js(0.57143), Js(0.07225), Js(0.0), Js(0.36111)]),'117':Js([Js(0.0), Js(0.44444), Js(0.04169), Js(0.0), Js(0.51667)]),'118':Js([Js(0.0), Js(0.44444), Js(0.10836), Js(0.0), Js(0.46111)]),'119':Js([Js(0.0), Js(0.44444), Js(0.10836), Js(0.0), Js(0.68334)]),'120':Js([Js(0.0), Js(0.44444), Js(0.09169), Js(0.0), Js(0.46111)]),'121':Js([Js(0.19444), Js(0.44444), Js(0.10836), Js(0.0), Js(0.46111)]),'122':Js([Js(0.0), Js(0.44444), Js(0.08752), Js(0.0), Js(0.43472)]),'126':Js([Js(0.35), Js(0.32659), Js(0.08826), Js(0.0), Js(0.5)]),'168':Js([Js(0.0), Js(0.67937), Js(0.06385), Js(0.0), Js(0.5)]),'176':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.73752)]),'184':Js([Js(0.17014), Js(0.0), Js(0.0), Js(0.0), Js(0.44445)]),'305':Js([Js(0.0), Js(0.44444), Js(0.04169), Js(0.0), Js(0.23889)]),'567':Js([Js(0.19444), Js(0.44444), Js(0.04169), Js(0.0), Js(0.26667)]),'710':Js([Js(0.0), Js(0.69444), Js(0.0799), Js(0.0), Js(0.5)]),'711':Js([Js(0.0), Js(0.63194), Js(0.08432), Js(0.0), Js(0.5)]),'713':Js([Js(0.0), Js(0.60889), Js(0.08776), Js(0.0), Js(0.5)]),'714':Js([Js(0.0), Js(0.69444), Js(0.09205), Js(0.0), Js(0.5)]),'715':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'728':Js([Js(0.0), Js(0.69444), Js(0.09483), Js(0.0), Js(0.5)]),'729':Js([Js(0.0), Js(0.67937), Js(0.07774), Js(0.0), Js(0.27778)]),'730':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.73752)]),'732':Js([Js(0.0), Js(0.67659), Js(0.08826), Js(0.0), Js(0.5)]),'733':Js([Js(0.0), Js(0.69444), Js(0.09205), Js(0.0), Js(0.5)]),'915':Js([Js(0.0), Js(0.69444), Js(0.13372), Js(0.0), Js(0.54167)]),'916':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.83334)]),'920':Js([Js(0.0), Js(0.69444), Js(0.07555), Js(0.0), Js(0.77778)]),'923':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.61111)]),'926':Js([Js(0.0), Js(0.69444), Js(0.12816), Js(0.0), Js(0.66667)]),'928':Js([Js(0.0), Js(0.69444), Js(0.08094), Js(0.0), Js(0.70834)]),'931':Js([Js(0.0), Js(0.69444), Js(0.11983), Js(0.0), Js(0.72222)]),'933':Js([Js(0.0), Js(0.69444), Js(0.09031), Js(0.0), Js(0.77778)]),'934':Js([Js(0.0), Js(0.69444), Js(0.04603), Js(0.0), Js(0.72222)]),'936':Js([Js(0.0), Js(0.69444), Js(0.09031), Js(0.0), Js(0.77778)]),'937':Js([Js(0.0), Js(0.69444), Js(0.08293), Js(0.0), Js(0.72222)]),'8211':Js([Js(0.0), Js(0.44444), Js(0.08616), Js(0.0), Js(0.5)]),'8212':Js([Js(0.0), Js(0.44444), Js(0.08616), Js(0.0), Js(1.0)]),'8216':Js([Js(0.0), Js(0.69444), Js(0.07816), Js(0.0), Js(0.27778)]),'8217':Js([Js(0.0), Js(0.69444), Js(0.07816), Js(0.0), Js(0.27778)]),'8220':Js([Js(0.0), Js(0.69444), Js(0.14205), Js(0.0), Js(0.5)]),'8221':Js([Js(0.0), Js(0.69444), Js(0.00316), Js(0.0), Js(0.5)])}),'SansSerif-Regular':Js({'33':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.31945)]),'34':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'35':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0), Js(0.83334)]),'36':Js([Js(0.05556), Js(0.75), Js(0.0), Js(0.0), Js(0.5)]),'37':Js([Js(0.05556), Js(0.75), Js(0.0), Js(0.0), Js(0.83334)]),'38':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.75834)]),'39':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.27778)]),'40':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.38889)]),'41':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.38889)]),'42':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0), Js(0.5)]),'43':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0), Js(0.77778)]),'44':Js([Js(0.125), Js(0.08333), Js(0.0), Js(0.0), Js(0.27778)]),'45':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.33333)]),'46':Js([Js(0.0), Js(0.08333), Js(0.0), Js(0.0), Js(0.27778)]),'47':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.5)]),'48':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0), Js(0.5)]),'49':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0), Js(0.5)]),'50':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0), Js(0.5)]),'51':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0), Js(0.5)]),'52':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0), Js(0.5)]),'53':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0), Js(0.5)]),'54':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0), Js(0.5)]),'55':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0), Js(0.5)]),'56':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0), Js(0.5)]),'57':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0), Js(0.5)]),'58':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.27778)]),'59':Js([Js(0.125), Js(0.44444), Js(0.0), Js(0.0), Js(0.27778)]),'61':Js([(-Js(0.13)), Js(0.37), Js(0.0), Js(0.0), Js(0.77778)]),'63':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.47222)]),'64':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.66667)]),'65':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.66667)]),'66':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.66667)]),'67':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.63889)]),'68':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.72223)]),'69':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.59722)]),'70':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.56945)]),'71':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.66667)]),'72':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.70834)]),'73':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.27778)]),'74':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.47222)]),'75':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.69445)]),'76':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.54167)]),'77':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.875)]),'78':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.70834)]),'79':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.73611)]),'80':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.63889)]),'81':Js([Js(0.125), Js(0.69444), Js(0.0), Js(0.0), Js(0.73611)]),'82':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.64584)]),'83':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.55556)]),'84':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.68056)]),'85':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.6875)]),'86':Js([Js(0.0), Js(0.69444), Js(0.01389), Js(0.0), Js(0.66667)]),'87':Js([Js(0.0), Js(0.69444), Js(0.01389), Js(0.0), Js(0.94445)]),'88':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.66667)]),'89':Js([Js(0.0), Js(0.69444), Js(0.025), Js(0.0), Js(0.66667)]),'90':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.61111)]),'91':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.28889)]),'93':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0), Js(0.28889)]),'94':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'95':Js([Js(0.35), Js(0.09444), Js(0.02778), Js(0.0), Js(0.5)]),'97':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.48056)]),'98':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.51667)]),'99':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.44445)]),'100':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.51667)]),'101':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.44445)]),'102':Js([Js(0.0), Js(0.69444), Js(0.06944), Js(0.0), Js(0.30556)]),'103':Js([Js(0.19444), Js(0.44444), Js(0.01389), Js(0.0), Js(0.5)]),'104':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.51667)]),'105':Js([Js(0.0), Js(0.67937), Js(0.0), Js(0.0), Js(0.23889)]),'106':Js([Js(0.19444), Js(0.67937), Js(0.0), Js(0.0), Js(0.26667)]),'107':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.48889)]),'108':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.23889)]),'109':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.79445)]),'110':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.51667)]),'111':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.5)]),'112':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0), Js(0.51667)]),'113':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0), Js(0.51667)]),'114':Js([Js(0.0), Js(0.44444), Js(0.01389), Js(0.0), Js(0.34167)]),'115':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.38333)]),'116':Js([Js(0.0), Js(0.57143), Js(0.0), Js(0.0), Js(0.36111)]),'117':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.51667)]),'118':Js([Js(0.0), Js(0.44444), Js(0.01389), Js(0.0), Js(0.46111)]),'119':Js([Js(0.0), Js(0.44444), Js(0.01389), Js(0.0), Js(0.68334)]),'120':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.46111)]),'121':Js([Js(0.19444), Js(0.44444), Js(0.01389), Js(0.0), Js(0.46111)]),'122':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.43472)]),'126':Js([Js(0.35), Js(0.32659), Js(0.0), Js(0.0), Js(0.5)]),'168':Js([Js(0.0), Js(0.67937), Js(0.0), Js(0.0), Js(0.5)]),'176':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.66667)]),'184':Js([Js(0.17014), Js(0.0), Js(0.0), Js(0.0), Js(0.44445)]),'305':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0), Js(0.23889)]),'567':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0), Js(0.26667)]),'710':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'711':Js([Js(0.0), Js(0.63194), Js(0.0), Js(0.0), Js(0.5)]),'713':Js([Js(0.0), Js(0.60889), Js(0.0), Js(0.0), Js(0.5)]),'714':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'715':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'728':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'729':Js([Js(0.0), Js(0.67937), Js(0.0), Js(0.0), Js(0.27778)]),'730':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.66667)]),'732':Js([Js(0.0), Js(0.67659), Js(0.0), Js(0.0), Js(0.5)]),'733':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'915':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.54167)]),'916':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.83334)]),'920':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.77778)]),'923':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.61111)]),'926':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.66667)]),'928':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.70834)]),'931':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.72222)]),'933':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.77778)]),'934':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.72222)]),'936':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.77778)]),'937':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.72222)]),'8211':Js([Js(0.0), Js(0.44444), Js(0.02778), Js(0.0), Js(0.5)]),'8212':Js([Js(0.0), Js(0.44444), Js(0.02778), Js(0.0), Js(1.0)]),'8216':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.27778)]),'8217':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.27778)]),'8220':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)]),'8221':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0), Js(0.5)])}),'Script-Regular':Js({'65':Js([Js(0.0), Js(0.7), Js(0.22925), Js(0.0), Js(0.80253)]),'66':Js([Js(0.0), Js(0.7), Js(0.04087), Js(0.0), Js(0.90757)]),'67':Js([Js(0.0), Js(0.7), Js(0.1689), Js(0.0), Js(0.66619)]),'68':Js([Js(0.0), Js(0.7), Js(0.09371), Js(0.0), Js(0.77443)]),'69':Js([Js(0.0), Js(0.7), Js(0.18583), Js(0.0), Js(0.56162)]),'70':Js([Js(0.0), Js(0.7), Js(0.13634), Js(0.0), Js(0.89544)]),'71':Js([Js(0.0), Js(0.7), Js(0.17322), Js(0.0), Js(0.60961)]),'72':Js([Js(0.0), Js(0.7), Js(0.29694), Js(0.0), Js(0.96919)]),'73':Js([Js(0.0), Js(0.7), Js(0.19189), Js(0.0), Js(0.80907)]),'74':Js([Js(0.27778), Js(0.7), Js(0.19189), Js(0.0), Js(1.05159)]),'75':Js([Js(0.0), Js(0.7), Js(0.31259), Js(0.0), Js(0.91364)]),'76':Js([Js(0.0), Js(0.7), Js(0.19189), Js(0.0), Js(0.87373)]),'77':Js([Js(0.0), Js(0.7), Js(0.15981), Js(0.0), Js(1.08031)]),'78':Js([Js(0.0), Js(0.7), Js(0.3525), Js(0.0), Js(0.9015)]),'79':Js([Js(0.0), Js(0.7), Js(0.08078), Js(0.0), Js(0.73787)]),'80':Js([Js(0.0), Js(0.7), Js(0.08078), Js(0.0), Js(1.01262)]),'81':Js([Js(0.0), Js(0.7), Js(0.03305), Js(0.0), Js(0.88282)]),'82':Js([Js(0.0), Js(0.7), Js(0.06259), Js(0.0), Js(0.85)]),'83':Js([Js(0.0), Js(0.7), Js(0.19189), Js(0.0), Js(0.86767)]),'84':Js([Js(0.0), Js(0.7), Js(0.29087), Js(0.0), Js(0.74697)]),'85':Js([Js(0.0), Js(0.7), Js(0.25815), Js(0.0), Js(0.79996)]),'86':Js([Js(0.0), Js(0.7), Js(0.27523), Js(0.0), Js(0.62204)]),'87':Js([Js(0.0), Js(0.7), Js(0.27523), Js(0.0), Js(0.80532)]),'88':Js([Js(0.0), Js(0.7), Js(0.26006), Js(0.0), Js(0.94445)]),'89':Js([Js(0.0), Js(0.7), Js(0.2939), Js(0.0), Js(0.70961)]),'90':Js([Js(0.0), Js(0.7), Js(0.24037), Js(0.0), Js(0.8212)])}),'Size1-Regular':Js({'40':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0), Js(0.45834)]),'41':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0), Js(0.45834)]),'47':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0), Js(0.57778)]),'91':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0), Js(0.41667)]),'92':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0), Js(0.57778)]),'93':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0), Js(0.41667)]),'123':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0), Js(0.58334)]),'125':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0), Js(0.58334)]),'710':Js([Js(0.0), Js(0.72222), Js(0.0), Js(0.0), Js(0.55556)]),'732':Js([Js(0.0), Js(0.72222), Js(0.0), Js(0.0), Js(0.55556)]),'770':Js([Js(0.0), Js(0.72222), Js(0.0), Js(0.0), Js(0.55556)]),'771':Js([Js(0.0), Js(0.72222), Js(0.0), Js(0.0), Js(0.55556)]),'8214':Js([(-Js(0.00099)), Js(0.601), Js(0.0), Js(0.0), Js(0.77778)]),'8593':Js([Js(1e-05), Js(0.6), Js(0.0), Js(0.0), Js(0.66667)]),'8595':Js([Js(1e-05), Js(0.6), Js(0.0), Js(0.0), Js(0.66667)]),'8657':Js([Js(1e-05), Js(0.6), Js(0.0), Js(0.0), Js(0.77778)]),'8659':Js([Js(1e-05), Js(0.6), Js(0.0), Js(0.0), Js(0.77778)]),'8719':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0), Js(0.94445)]),'8720':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0), Js(0.94445)]),'8721':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0), Js(1.05556)]),'8730':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0), Js(1.0)]),'8739':Js([(-Js(0.00599)), Js(0.606), Js(0.0), Js(0.0), Js(0.33333)]),'8741':Js([(-Js(0.00599)), Js(0.606), Js(0.0), Js(0.0), Js(0.55556)]),'8747':Js([Js(0.30612), Js(0.805), Js(0.19445), Js(0.0), Js(0.47222)]),'8748':Js([Js(0.306), Js(0.805), Js(0.19445), Js(0.0), Js(0.47222)]),'8749':Js([Js(0.306), Js(0.805), Js(0.19445), Js(0.0), Js(0.47222)]),'8750':Js([Js(0.30612), Js(0.805), Js(0.19445), Js(0.0), Js(0.47222)]),'8896':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0), Js(0.83334)]),'8897':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0), Js(0.83334)]),'8898':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0), Js(0.83334)]),'8899':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0), Js(0.83334)]),'8968':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0), Js(0.47222)]),'8969':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0), Js(0.47222)]),'8970':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0), Js(0.47222)]),'8971':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0), Js(0.47222)]),'9168':Js([(-Js(0.00099)), Js(0.601), Js(0.0), Js(0.0), Js(0.66667)]),'10216':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0), Js(0.47222)]),'10217':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0), Js(0.47222)]),'10752':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0), Js(1.11111)]),'10753':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0), Js(1.11111)]),'10754':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0), Js(1.11111)]),'10756':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0), Js(0.83334)]),'10758':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0), Js(0.83334)])}),'Size2-Regular':Js({'40':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0), Js(0.59722)]),'41':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0), Js(0.59722)]),'47':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0), Js(0.81111)]),'91':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0), Js(0.47222)]),'92':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0), Js(0.81111)]),'93':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0), Js(0.47222)]),'123':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0), Js(0.66667)]),'125':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0), Js(0.66667)]),'710':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0), Js(1.0)]),'732':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0), Js(1.0)]),'770':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0), Js(1.0)]),'771':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0), Js(1.0)]),'8719':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0), Js(1.27778)]),'8720':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0), Js(1.27778)]),'8721':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0), Js(1.44445)]),'8730':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0), Js(1.0)]),'8747':Js([Js(0.86225), Js(1.36), Js(0.44445), Js(0.0), Js(0.55556)]),'8748':Js([Js(0.862), Js(1.36), Js(0.44445), Js(0.0), Js(0.55556)]),'8749':Js([Js(0.862), Js(1.36), Js(0.44445), Js(0.0), Js(0.55556)]),'8750':Js([Js(0.86225), Js(1.36), Js(0.44445), Js(0.0), Js(0.55556)]),'8896':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0), Js(1.11111)]),'8897':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0), Js(1.11111)]),'8898':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0), Js(1.11111)]),'8899':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0), Js(1.11111)]),'8968':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0), Js(0.52778)]),'8969':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0), Js(0.52778)]),'8970':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0), Js(0.52778)]),'8971':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0), Js(0.52778)]),'10216':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0), Js(0.61111)]),'10217':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0), Js(0.61111)]),'10752':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0), Js(1.51112)]),'10753':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0), Js(1.51112)]),'10754':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0), Js(1.51112)]),'10756':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0), Js(1.11111)]),'10758':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0), Js(1.11111)])}),'Size3-Regular':Js({'40':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0), Js(0.73611)]),'41':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0), Js(0.73611)]),'47':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0), Js(1.04445)]),'91':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0), Js(0.52778)]),'92':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0), Js(1.04445)]),'93':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0), Js(0.52778)]),'123':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0), Js(0.75)]),'125':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0), Js(0.75)]),'710':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0), Js(1.44445)]),'732':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0), Js(1.44445)]),'770':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0), Js(1.44445)]),'771':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0), Js(1.44445)]),'8730':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0), Js(1.0)]),'8968':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0), Js(0.58334)]),'8969':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0), Js(0.58334)]),'8970':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0), Js(0.58334)]),'8971':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0), Js(0.58334)]),'10216':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0), Js(0.75)]),'10217':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0), Js(0.75)])}),'Size4-Regular':Js({'40':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0), Js(0.79167)]),'41':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0), Js(0.79167)]),'47':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0), Js(1.27778)]),'91':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0), Js(0.58334)]),'92':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0), Js(1.27778)]),'93':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0), Js(0.58334)]),'123':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0), Js(0.80556)]),'125':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0), Js(0.80556)]),'710':Js([Js(0.0), Js(0.825), Js(0.0), Js(0.0), Js(1.8889)]),'732':Js([Js(0.0), Js(0.825), Js(0.0), Js(0.0), Js(1.8889)]),'770':Js([Js(0.0), Js(0.825), Js(0.0), Js(0.0), Js(1.8889)]),'771':Js([Js(0.0), Js(0.825), Js(0.0), Js(0.0), Js(1.8889)]),'8730':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0), Js(1.0)]),'8968':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0), Js(0.63889)]),'8969':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0), Js(0.63889)]),'8970':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0), Js(0.63889)]),'8971':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0), Js(0.63889)]),'9115':Js([Js(0.64502), Js(1.155), Js(0.0), Js(0.0), Js(0.875)]),'9116':Js([Js(1e-05), Js(0.6), Js(0.0), Js(0.0), Js(0.875)]),'9117':Js([Js(0.64502), Js(1.155), Js(0.0), Js(0.0), Js(0.875)]),'9118':Js([Js(0.64502), Js(1.155), Js(0.0), Js(0.0), Js(0.875)]),'9119':Js([Js(1e-05), Js(0.6), Js(0.0), Js(0.0), Js(0.875)]),'9120':Js([Js(0.64502), Js(1.155), Js(0.0), Js(0.0), Js(0.875)]),'9121':Js([Js(0.64502), Js(1.155), Js(0.0), Js(0.0), Js(0.66667)]),'9122':Js([(-Js(0.00099)), Js(0.601), Js(0.0), Js(0.0), Js(0.66667)]),'9123':Js([Js(0.64502), Js(1.155), Js(0.0), Js(0.0), Js(0.66667)]),'9124':Js([Js(0.64502), Js(1.155), Js(0.0), Js(0.0), Js(0.66667)]),'9125':Js([(-Js(0.00099)), Js(0.601), Js(0.0), Js(0.0), Js(0.66667)]),'9126':Js([Js(0.64502), Js(1.155), Js(0.0), Js(0.0), Js(0.66667)]),'9127':Js([Js(1e-05), Js(0.9), Js(0.0), Js(0.0), Js(0.88889)]),'9128':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0), Js(0.88889)]),'9129':Js([Js(0.90001), Js(0.0), Js(0.0), Js(0.0), Js(0.88889)]),'9130':Js([Js(0.0), Js(0.3), Js(0.0), Js(0.0), Js(0.88889)]),'9131':Js([Js(1e-05), Js(0.9), Js(0.0), Js(0.0), Js(0.88889)]),'9132':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0), Js(0.88889)]),'9133':Js([Js(0.90001), Js(0.0), Js(0.0), Js(0.0), Js(0.88889)]),'9143':Js([Js(0.88502), Js(0.915), Js(0.0), Js(0.0), Js(1.05556)]),'10216':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0), Js(0.80556)]),'10217':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0), Js(0.80556)]),'57344':Js([(-Js(0.00499)), Js(0.605), Js(0.0), Js(0.0), Js(1.05556)]),'57345':Js([(-Js(0.00499)), Js(0.605), Js(0.0), Js(0.0), Js(1.05556)]),'57680':Js([Js(0.0), Js(0.12), Js(0.0), Js(0.0), Js(0.45)]),'57681':Js([Js(0.0), Js(0.12), Js(0.0), Js(0.0), Js(0.45)]),'57682':Js([Js(0.0), Js(0.12), Js(0.0), Js(0.0), Js(0.45)]),'57683':Js([Js(0.0), Js(0.12), Js(0.0), Js(0.0), Js(0.45)])}),'Typewriter-Regular':Js({'32':Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.525)]),'33':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'34':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'35':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'36':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0), Js(0.525)]),'37':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0), Js(0.525)]),'38':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'39':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'40':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0), Js(0.525)]),'41':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0), Js(0.525)]),'42':Js([Js(0.0), Js(0.52083), Js(0.0), Js(0.0), Js(0.525)]),'43':Js([(-Js(0.08056)), Js(0.53055), Js(0.0), Js(0.0), Js(0.525)]),'44':Js([Js(0.13889), Js(0.125), Js(0.0), Js(0.0), Js(0.525)]),'45':Js([(-Js(0.08056)), Js(0.53055), Js(0.0), Js(0.0), Js(0.525)]),'46':Js([Js(0.0), Js(0.125), Js(0.0), Js(0.0), Js(0.525)]),'47':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0), Js(0.525)]),'48':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'49':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'50':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'51':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'52':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'53':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'54':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'55':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'56':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'57':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'58':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'59':Js([Js(0.13889), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'60':Js([(-Js(0.05556)), Js(0.55556), Js(0.0), Js(0.0), Js(0.525)]),'61':Js([(-Js(0.19549)), Js(0.41562), Js(0.0), Js(0.0), Js(0.525)]),'62':Js([(-Js(0.05556)), Js(0.55556), Js(0.0), Js(0.0), Js(0.525)]),'63':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'64':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'65':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'66':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'67':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'68':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'69':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'70':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'71':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'72':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'73':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'74':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'75':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'76':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'77':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'78':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'79':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'80':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'81':Js([Js(0.13889), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'82':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'83':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'84':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'85':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'86':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'87':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'88':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'89':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'90':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'91':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0), Js(0.525)]),'92':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0), Js(0.525)]),'93':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0), Js(0.525)]),'94':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'95':Js([Js(0.09514), Js(0.0), Js(0.0), Js(0.0), Js(0.525)]),'96':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'97':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'98':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'99':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'100':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'101':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'102':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'103':Js([Js(0.22222), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'104':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'105':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'106':Js([Js(0.22222), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'107':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'108':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'109':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'110':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'111':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'112':Js([Js(0.22222), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'113':Js([Js(0.22222), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'114':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'115':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'116':Js([Js(0.0), Js(0.55358), Js(0.0), Js(0.0), Js(0.525)]),'117':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'118':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'119':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'120':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'121':Js([Js(0.22222), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'122':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'123':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0), Js(0.525)]),'124':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0), Js(0.525)]),'125':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0), Js(0.525)]),'126':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'127':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'160':Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.525)]),'176':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'184':Js([Js(0.19445), Js(0.0), Js(0.0), Js(0.0), Js(0.525)]),'305':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'567':Js([Js(0.22222), Js(0.43056), Js(0.0), Js(0.0), Js(0.525)]),'711':Js([Js(0.0), Js(0.56597), Js(0.0), Js(0.0), Js(0.525)]),'713':Js([Js(0.0), Js(0.56555), Js(0.0), Js(0.0), Js(0.525)]),'714':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'715':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'728':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'730':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'770':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'771':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'776':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'915':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'916':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'920':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'923':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'926':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'928':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'931':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'933':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'934':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'936':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'937':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'8216':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'8217':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'8242':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0), Js(0.525)]),'9251':Js([Js(0.11111), Js(0.21944), Js(0.0), Js(0.0), Js(0.525)])})}))
        var.put('sigmasAndXis', Js({'slant':Js([Js(0.25), Js(0.25), Js(0.25)]),'space':Js([Js(0.0), Js(0.0), Js(0.0)]),'stretch':Js([Js(0.0), Js(0.0), Js(0.0)]),'shrink':Js([Js(0.0), Js(0.0), Js(0.0)]),'xHeight':Js([Js(0.431), Js(0.431), Js(0.431)]),'quad':Js([Js(1.0), Js(1.171), Js(1.472)]),'extraSpace':Js([Js(0.0), Js(0.0), Js(0.0)]),'num1':Js([Js(0.677), Js(0.732), Js(0.925)]),'num2':Js([Js(0.394), Js(0.384), Js(0.387)]),'num3':Js([Js(0.444), Js(0.471), Js(0.504)]),'denom1':Js([Js(0.686), Js(0.752), Js(1.025)]),'denom2':Js([Js(0.345), Js(0.344), Js(0.532)]),'sup1':Js([Js(0.413), Js(0.503), Js(0.504)]),'sup2':Js([Js(0.363), Js(0.431), Js(0.404)]),'sup3':Js([Js(0.289), Js(0.286), Js(0.294)]),'sub1':Js([Js(0.15), Js(0.143), Js(0.2)]),'sub2':Js([Js(0.247), Js(0.286), Js(0.4)]),'supDrop':Js([Js(0.386), Js(0.353), Js(0.494)]),'subDrop':Js([Js(0.05), Js(0.071), Js(0.1)]),'delim1':Js([Js(2.39), Js(1.7), Js(1.98)]),'delim2':Js([Js(1.01), Js(1.157), Js(1.42)]),'axisHeight':Js([Js(0.25), Js(0.25), Js(0.25)]),'defaultRuleThickness':Js([Js(0.04), Js(0.049), Js(0.049)]),'bigOpSpacing1':Js([Js(0.111), Js(0.111), Js(0.111)]),'bigOpSpacing2':Js([Js(0.166), Js(0.166), Js(0.166)]),'bigOpSpacing3':Js([Js(0.2), Js(0.2), Js(0.2)]),'bigOpSpacing4':Js([Js(0.6), Js(0.611), Js(0.611)]),'bigOpSpacing5':Js([Js(0.1), Js(0.143), Js(0.143)]),'sqrtRuleThickness':Js([Js(0.04), Js(0.04), Js(0.04)]),'ptPerEm':Js([Js(10.0), Js(10.0), Js(10.0)]),'doubleRuleSep':Js([Js(0.2), Js(0.2), Js(0.2)])}))
        var.put('extraCharacterMap', Js({'Å':Js('A'),'Ç':Js('C'),'Ð':Js('D'),'Þ':Js('o'),'å':Js('a'),'ç':Js('c'),'ð':Js('d'),'þ':Js('o'),'А':Js('A'),'Б':Js('B'),'В':Js('B'),'Г':Js('F'),'Д':Js('A'),'Е':Js('E'),'Ж':Js('K'),'З':Js('3'),'И':Js('N'),'Й':Js('N'),'К':Js('K'),'Л':Js('N'),'М':Js('M'),'Н':Js('H'),'О':Js('O'),'П':Js('N'),'Р':Js('P'),'С':Js('C'),'Т':Js('T'),'У':Js('y'),'Ф':Js('O'),'Х':Js('X'),'Ц':Js('U'),'Ч':Js('h'),'Ш':Js('W'),'Щ':Js('W'),'Ъ':Js('B'),'Ы':Js('X'),'Ь':Js('B'),'Э':Js('3'),'Ю':Js('X'),'Я':Js('R'),'а':Js('a'),'б':Js('b'),'в':Js('a'),'г':Js('r'),'д':Js('y'),'е':Js('e'),'ж':Js('m'),'з':Js('e'),'и':Js('n'),'й':Js('n'),'к':Js('n'),'л':Js('n'),'м':Js('m'),'н':Js('n'),'о':Js('o'),'п':Js('n'),'р':Js('p'),'с':Js('c'),'т':Js('o'),'у':Js('y'),'ф':Js('b'),'х':Js('x'),'ц':Js('n'),'ч':Js('n'),'ш':Js('w'),'щ':Js('w'),'ъ':Js('a'),'ы':Js('m'),'ь':Js('a'),'э':Js('e'),'ю':Js('m'),'я':Js('r')}))
        pass
        pass
        var.put('fontMetricsBySizeIndex', Js({}))
        pass
        var.put('ATOMS', Js({'bin':Js(1.0),'close':Js(1.0),'inner':Js(1.0),'open':Js(1.0),'punct':Js(1.0),'rel':Js(1.0)}))
        var.put('NON_ATOMS', Js({'accent-token':Js(1.0),'mathord':Js(1.0),'op-token':Js(1.0),'spacing':Js(1.0),'textord':Js(1.0)}))
        var.put('symbols', Js({'math':Js({}),'text':Js({})}))
        var.put('src_symbols', var.get('symbols'))
        pass
        var.put('symbols_math', Js('math'))
        var.put('symbols_text', Js('text'))
        var.put('main', Js('main'))
        var.put('ams', Js('ams'))
        var.put('symbols_accent', Js('accent-token'))
        var.put('bin', Js('bin'))
        var.put('symbols_close', Js('close'))
        var.put('symbols_inner', Js('inner'))
        var.put('mathord', Js('mathord'))
        var.put('op', Js('op-token'))
        var.put('symbols_open', Js('open'))
        var.put('punct', Js('punct'))
        var.put('rel', Js('rel'))
        var.put('symbols_spacing', Js('spacing'))
        var.put('symbols_textord', Js('textord'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('≡'), Js('\\equiv'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('≺'), Js('\\prec'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('≻'), Js('\\succ'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('∼'), Js('\\sim'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⊥'), Js('\\perp'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⪯'), Js('\\preceq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⪰'), Js('\\succeq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('≃'), Js('\\simeq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('∣'), Js('\\mid'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('≪'), Js('\\ll'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('≫'), Js('\\gg'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('≍'), Js('\\asymp'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('∥'), Js('\\parallel'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⋈'), Js('\\bowtie'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⌣'), Js('\\smile'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⊑'), Js('\\sqsubseteq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⊒'), Js('\\sqsupseteq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('≐'), Js('\\doteq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⌢'), Js('\\frown'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('∋'), Js('\\ni'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('∝'), Js('\\propto'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⊢'), Js('\\vdash'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⊣'), Js('\\dashv'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('∋'), Js('\\owns'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('punct'), Js('.'), Js('\\ldotp'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('punct'), Js('⋅'), Js('\\cdotp'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('#'), Js('\\#'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('#'), Js('\\#'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('&'), Js('\\&'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('&'), Js('\\&'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('ℵ'), Js('\\aleph'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('∀'), Js('\\forall'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('ℏ'), Js('\\hbar'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('∃'), Js('\\exists'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('∇'), Js('\\nabla'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('♭'), Js('\\flat'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('ℓ'), Js('\\ell'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('♮'), Js('\\natural'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('♣'), Js('\\clubsuit'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('℘'), Js('\\wp'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('♯'), Js('\\sharp'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('♢'), Js('\\diamondsuit'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('ℜ'), Js('\\Re'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('♡'), Js('\\heartsuit'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('ℑ'), Js('\\Im'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('♠'), Js('\\spadesuit'), Js(True))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('§'), Js('\\S'), Js(True))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('¶'), Js('\\P'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('†'), Js('\\dag'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('†'), Js('\\dag'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('†'), Js('\\textdagger'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('‡'), Js('\\ddag'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('‡'), Js('\\ddag'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('‡'), Js('\\textdaggerdbl'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_close'), Js('⎱'), Js('\\rmoustache'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_open'), Js('⎰'), Js('\\lmoustache'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_close'), Js('⟯'), Js('\\rgroup'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_open'), Js('⟮'), Js('\\lgroup'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('∓'), Js('\\mp'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('⊖'), Js('\\ominus'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('⊎'), Js('\\uplus'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('⊓'), Js('\\sqcap'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('∗'), Js('\\ast'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('⊔'), Js('\\sqcup'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('◯'), Js('\\bigcirc'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('∙'), Js('\\bullet'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('‡'), Js('\\ddagger'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('≀'), Js('\\wr'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('⨿'), Js('\\amalg'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('&'), Js('\\And'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⟵'), Js('\\longleftarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⇐'), Js('\\Leftarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⟸'), Js('\\Longleftarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⟶'), Js('\\longrightarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⇒'), Js('\\Rightarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⟹'), Js('\\Longrightarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('↔'), Js('\\leftrightarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⟷'), Js('\\longleftrightarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⇔'), Js('\\Leftrightarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⟺'), Js('\\Longleftrightarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('↦'), Js('\\mapsto'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⟼'), Js('\\longmapsto'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('↗'), Js('\\nearrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('↩'), Js('\\hookleftarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('↪'), Js('\\hookrightarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('↘'), Js('\\searrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('↼'), Js('\\leftharpoonup'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⇀'), Js('\\rightharpoonup'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('↙'), Js('\\swarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('↽'), Js('\\leftharpoondown'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⇁'), Js('\\rightharpoondown'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('↖'), Js('\\nwarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⇌'), Js('\\rightleftharpoons'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≮'), Js('\\nless'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('\ue010'), Js('\\@nleqslant'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('\ue011'), Js('\\@nleqq'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⪇'), Js('\\lneq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≨'), Js('\\lneqq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('\ue00c'), Js('\\@lvertneqq'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋦'), Js('\\lnsim'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⪉'), Js('\\lnapprox'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊀'), Js('\\nprec'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋠'), Js('\\npreceq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋨'), Js('\\precnsim'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⪹'), Js('\\precnapprox'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≁'), Js('\\nsim'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('\ue006'), Js('\\@nshortmid'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('∤'), Js('\\nmid'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊬'), Js('\\nvdash'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊭'), Js('\\nvDash'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋪'), Js('\\ntriangleleft'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋬'), Js('\\ntrianglelefteq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊊'), Js('\\subsetneq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('\ue01a'), Js('\\@varsubsetneq'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⫋'), Js('\\subsetneqq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('\ue017'), Js('\\@varsubsetneqq'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≯'), Js('\\ngtr'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('\ue00f'), Js('\\@ngeqslant'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('\ue00e'), Js('\\@ngeqq'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⪈'), Js('\\gneq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≩'), Js('\\gneqq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('\ue00d'), Js('\\@gvertneqq'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋧'), Js('\\gnsim'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⪊'), Js('\\gnapprox'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊁'), Js('\\nsucc'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋡'), Js('\\nsucceq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋩'), Js('\\succnsim'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⪺'), Js('\\succnapprox'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≆'), Js('\\ncong'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('\ue007'), Js('\\@nshortparallel'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('∦'), Js('\\nparallel'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊯'), Js('\\nVDash'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋫'), Js('\\ntriangleright'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋭'), Js('\\ntrianglerighteq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('\ue018'), Js('\\@nsupseteqq'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊋'), Js('\\supsetneq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('\ue01b'), Js('\\@varsupsetneq'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⫌'), Js('\\supsetneqq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('\ue019'), Js('\\@varsupsetneqq'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊮'), Js('\\nVdash'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⪵'), Js('\\precneqq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⪶'), Js('\\succneqq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('\ue016'), Js('\\@nsubseteqq'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⊴'), Js('\\unlhd'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⊵'), Js('\\unrhd'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↚'), Js('\\nleftarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↛'), Js('\\nrightarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⇍'), Js('\\nLeftarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⇏'), Js('\\nRightarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↮'), Js('\\nleftrightarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⇎'), Js('\\nLeftrightarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('△'), Js('\\vartriangle'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('ℏ'), Js('\\hslash'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('▽'), Js('\\triangledown'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('◊'), Js('\\lozenge'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('Ⓢ'), Js('\\circledS'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('®'), Js('\\circledR'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('ams'), var.get('symbols_textord'), Js('®'), Js('\\circledR'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('∡'), Js('\\measuredangle'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('∄'), Js('\\nexists'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('℧'), Js('\\mho'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('Ⅎ'), Js('\\Finv'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('⅁'), Js('\\Game'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('‵'), Js('\\backprime'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('▲'), Js('\\blacktriangle'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('▼'), Js('\\blacktriangledown'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('■'), Js('\\blacksquare'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('⧫'), Js('\\blacklozenge'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('★'), Js('\\bigstar'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('∢'), Js('\\sphericalangle'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('∁'), Js('\\complement'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('ð'), Js('\\eth'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('╱'), Js('\\diagup'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('╲'), Js('\\diagdown'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('□'), Js('\\square'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('□'), Js('\\Box'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('◊'), Js('\\Diamond'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('¥'), Js('\\yen'), Js(True))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('ams'), var.get('symbols_textord'), Js('¥'), Js('\\yen'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('✓'), Js('\\checkmark'), Js(True))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('ams'), var.get('symbols_textord'), Js('✓'), Js('\\checkmark'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('ℶ'), Js('\\beth'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('ℸ'), Js('\\daleth'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('ℷ'), Js('\\gimel'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('ϝ'), Js('\\digamma'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('ϰ'), Js('\\varkappa'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_open'), Js('┌'), Js('\\ulcorner'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_close'), Js('┐'), Js('\\urcorner'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_open'), Js('└'), Js('\\llcorner'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_close'), Js('┘'), Js('\\lrcorner'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≦'), Js('\\leqq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⩽'), Js('\\leqslant'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⪕'), Js('\\eqslantless'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≲'), Js('\\lesssim'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⪅'), Js('\\lessapprox'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≊'), Js('\\approxeq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⋖'), Js('\\lessdot'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋘'), Js('\\lll'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≶'), Js('\\lessgtr'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋚'), Js('\\lesseqgtr'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⪋'), Js('\\lesseqqgtr'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≑'), Js('\\doteqdot'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≓'), Js('\\risingdotseq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≒'), Js('\\fallingdotseq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('∽'), Js('\\backsim'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋍'), Js('\\backsimeq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⫅'), Js('\\subseteqq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋐'), Js('\\Subset'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊏'), Js('\\sqsubset'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≼'), Js('\\preccurlyeq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋞'), Js('\\curlyeqprec'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≾'), Js('\\precsim'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⪷'), Js('\\precapprox'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊲'), Js('\\vartriangleleft'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊴'), Js('\\trianglelefteq'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊨'), Js('\\vDash'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊪'), Js('\\Vvdash'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⌣'), Js('\\smallsmile'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⌢'), Js('\\smallfrown'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≏'), Js('\\bumpeq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≎'), Js('\\Bumpeq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≧'), Js('\\geqq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⩾'), Js('\\geqslant'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⪖'), Js('\\eqslantgtr'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≳'), Js('\\gtrsim'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⪆'), Js('\\gtrapprox'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⋗'), Js('\\gtrdot'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋙'), Js('\\ggg'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≷'), Js('\\gtrless'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋛'), Js('\\gtreqless'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⪌'), Js('\\gtreqqless'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≖'), Js('\\eqcirc'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≗'), Js('\\circeq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≜'), Js('\\triangleq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('∼'), Js('\\thicksim'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≈'), Js('\\thickapprox'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⫆'), Js('\\supseteqq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋑'), Js('\\Supset'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊐'), Js('\\sqsupset'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≽'), Js('\\succcurlyeq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋟'), Js('\\curlyeqsucc'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≿'), Js('\\succsim'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⪸'), Js('\\succapprox'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊳'), Js('\\vartriangleright'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊵'), Js('\\trianglerighteq'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊩'), Js('\\Vdash'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('∣'), Js('\\shortmid'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('∥'), Js('\\shortparallel'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≬'), Js('\\between'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋔'), Js('\\pitchfork'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('∝'), Js('\\varpropto'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('◀'), Js('\\blacktriangleleft'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('∴'), Js('\\therefore'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('∍'), Js('\\backepsilon'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('▶'), Js('\\blacktriangleright'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('∵'), Js('\\because'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋘'), Js('\\llless'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⋙'), Js('\\gggtr'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⊲'), Js('\\lhd'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⊳'), Js('\\rhd'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≂'), Js('\\eqsim'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⋈'), Js('\\Join'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≑'), Js('\\Doteq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('∔'), Js('\\dotplus'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('∖'), Js('\\smallsetminus'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⋒'), Js('\\Cap'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⋓'), Js('\\Cup'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⩞'), Js('\\doublebarwedge'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⊟'), Js('\\boxminus'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⊞'), Js('\\boxplus'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⋇'), Js('\\divideontimes'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⋉'), Js('\\ltimes'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⋊'), Js('\\rtimes'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⋋'), Js('\\leftthreetimes'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⋌'), Js('\\rightthreetimes'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⋏'), Js('\\curlywedge'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⋎'), Js('\\curlyvee'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⊝'), Js('\\circleddash'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⊛'), Js('\\circledast'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⋅'), Js('\\centerdot'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⊺'), Js('\\intercal'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⋒'), Js('\\doublecap'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⋓'), Js('\\doublecup'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⊠'), Js('\\boxtimes'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⇢'), Js('\\dashrightarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⇠'), Js('\\dashleftarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⇇'), Js('\\leftleftarrows'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⇆'), Js('\\leftrightarrows'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⇚'), Js('\\Lleftarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↞'), Js('\\twoheadleftarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↢'), Js('\\leftarrowtail'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↫'), Js('\\looparrowleft'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⇋'), Js('\\leftrightharpoons'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↶'), Js('\\curvearrowleft'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↺'), Js('\\circlearrowleft'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↰'), Js('\\Lsh'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⇈'), Js('\\upuparrows'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↿'), Js('\\upharpoonleft'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⇃'), Js('\\downharpoonleft'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊸'), Js('\\multimap'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↭'), Js('\\leftrightsquigarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⇉'), Js('\\rightrightarrows'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⇄'), Js('\\rightleftarrows'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↠'), Js('\\twoheadrightarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↣'), Js('\\rightarrowtail'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↬'), Js('\\looparrowright'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↷'), Js('\\curvearrowright'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↻'), Js('\\circlearrowright'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↱'), Js('\\Rsh'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⇊'), Js('\\downdownarrows'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↾'), Js('\\upharpoonright'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⇂'), Js('\\downharpoonright'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⇝'), Js('\\rightsquigarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⇝'), Js('\\leadsto'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⇛'), Js('\\Rrightarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('↾'), Js('\\restriction'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('‘'), Js('`'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('$'), Js('\\$'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('$'), Js('\\$'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('$'), Js('\\textdollar'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('%'), Js('\\%'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('%'), Js('\\%'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('_'), Js('\\_'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('_'), Js('\\_'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('_'), Js('\\textunderscore'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('∠'), Js('\\angle'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('∞'), Js('\\infty'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('′'), Js('\\prime'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('△'), Js('\\triangle'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('Γ'), Js('\\Gamma'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('Δ'), Js('\\Delta'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('Θ'), Js('\\Theta'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('Λ'), Js('\\Lambda'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('Ξ'), Js('\\Xi'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('Π'), Js('\\Pi'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('Σ'), Js('\\Sigma'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('Υ'), Js('\\Upsilon'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('Φ'), Js('\\Phi'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('Ψ'), Js('\\Psi'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('Ω'), Js('\\Omega'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('A'), Js('Α'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('B'), Js('Β'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('E'), Js('Ε'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('Z'), Js('Ζ'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('H'), Js('Η'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('I'), Js('Ι'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('K'), Js('Κ'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('M'), Js('Μ'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('N'), Js('Ν'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('O'), Js('Ο'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('P'), Js('Ρ'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('T'), Js('Τ'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('X'), Js('Χ'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('¬'), Js('\\neg'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('¬'), Js('\\lnot'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('⊤'), Js('\\top'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('⊥'), Js('\\bot'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('∅'), Js('\\emptyset'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('∅'), Js('\\varnothing'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('α'), Js('\\alpha'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('β'), Js('\\beta'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('γ'), Js('\\gamma'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('δ'), Js('\\delta'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('ϵ'), Js('\\epsilon'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('ζ'), Js('\\zeta'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('η'), Js('\\eta'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('θ'), Js('\\theta'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('ι'), Js('\\iota'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('κ'), Js('\\kappa'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('λ'), Js('\\lambda'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('μ'), Js('\\mu'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('ν'), Js('\\nu'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('ξ'), Js('\\xi'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('ο'), Js('\\omicron'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('π'), Js('\\pi'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('ρ'), Js('\\rho'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('σ'), Js('\\sigma'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('τ'), Js('\\tau'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('υ'), Js('\\upsilon'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('ϕ'), Js('\\phi'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('χ'), Js('\\chi'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('ψ'), Js('\\psi'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('ω'), Js('\\omega'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('ε'), Js('\\varepsilon'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('ϑ'), Js('\\vartheta'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('ϖ'), Js('\\varpi'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('ϱ'), Js('\\varrho'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('ς'), Js('\\varsigma'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('φ'), Js('\\varphi'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('∗'), Js('*'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('+'), Js('+'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('−'), Js('-'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('⋅'), Js('\\cdot'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('∘'), Js('\\circ'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('÷'), Js('\\div'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('±'), Js('\\pm'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('×'), Js('\\times'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('∩'), Js('\\cap'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('∪'), Js('\\cup'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('∖'), Js('\\setminus'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('∧'), Js('\\land'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('∨'), Js('\\lor'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('∧'), Js('\\wedge'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('∨'), Js('\\vee'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('√'), Js('\\surd'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_open'), Js('('), Js('('))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_open'), Js('['), Js('['))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_open'), Js('⟨'), Js('\\langle'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_open'), Js('∣'), Js('\\lvert'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_open'), Js('∥'), Js('\\lVert'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_close'), Js(')'), Js(')'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_close'), Js(']'), Js(']'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_close'), Js('?'), Js('?'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_close'), Js('!'), Js('!'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_close'), Js('⟩'), Js('\\rangle'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_close'), Js('∣'), Js('\\rvert'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_close'), Js('∥'), Js('\\rVert'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('='), Js('='))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('<'), Js('<'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('>'), Js('>'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js(':'), Js(':'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('∉'), Js('\\not\\in'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('∉'), Js('\\notin'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('≠'), Js('\\ne'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('≠'), Js('\\neq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('≈'), Js('\\approx'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('≅'), Js('\\cong'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('≥'), Js('\\ge'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('≥'), Js('\\geq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('←'), Js('\\gets'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('>'), Js('\\gt'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('∈'), Js('\\in'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('\ue020'), Js('\\@not'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⊂'), Js('\\subset'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⊃'), Js('\\supset'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⊆'), Js('\\subseteq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⊇'), Js('\\supseteq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊈'), Js('\\nsubseteq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('⊉'), Js('\\nsupseteq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⊨'), Js('\\models'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('←'), Js('\\leftarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('≤'), Js('\\le'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('≤'), Js('\\leq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('<'), Js('\\lt'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('→'), Js('\\rightarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('→'), Js('\\to'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≱'), Js('\\ngeq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('rel'), Js('≰'), Js('\\nleq'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_spacing'), Js('\xa0'), Js('\\ '))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_spacing'), Js('\xa0'), Js('~'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_spacing'), Js('\xa0'), Js('\\space'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_spacing'), Js('\xa0'), Js('\\nobreakspace'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_spacing'), Js('\xa0'), Js('\\ '))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_spacing'), Js('\xa0'), Js('~'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_spacing'), Js('\xa0'), Js('\\space'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_spacing'), Js('\xa0'), Js('\\nobreakspace'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_spacing'), var.get(u"null"), Js('\\nobreak'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_spacing'), var.get(u"null"), Js('\\allowbreak'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('punct'), Js(','), Js(','))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('punct'), Js(';'), Js(';'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⊼'), Js('\\barwedge'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⊻'), Js('\\veebar'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('⊙'), Js('\\odot'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('⊕'), Js('\\oplus'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('⊗'), Js('\\otimes'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('∂'), Js('\\partial'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('⊘'), Js('\\oslash'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⊚'), Js('\\circledcirc'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('bin'), Js('⊡'), Js('\\boxdot'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('△'), Js('\\bigtriangleup'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('▽'), Js('\\bigtriangledown'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('†'), Js('\\dagger'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('⋄'), Js('\\diamond'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('⋆'), Js('\\star'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('◃'), Js('\\triangleleft'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('bin'), Js('▹'), Js('\\triangleright'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_open'), Js('{'), Js('\\{'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('{'), Js('\\{'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('{'), Js('\\textbraceleft'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_close'), Js('}'), Js('\\}'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('}'), Js('\\}'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('}'), Js('\\textbraceright'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_open'), Js('{'), Js('\\lbrace'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_close'), Js('}'), Js('\\rbrace'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_open'), Js('['), Js('\\lbrack'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('['), Js('\\lbrack'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_close'), Js(']'), Js('\\rbrack'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js(']'), Js('\\rbrack'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_open'), Js('('), Js('\\lparen'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_close'), Js(')'), Js('\\rparen'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('<'), Js('\\textless'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('>'), Js('\\textgreater'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_open'), Js('⌊'), Js('\\lfloor'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_close'), Js('⌋'), Js('\\rfloor'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_open'), Js('⌈'), Js('\\lceil'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_close'), Js('⌉'), Js('\\rceil'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('\\'), Js('\\backslash'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('∣'), Js('|'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('∣'), Js('\\vert'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('|'), Js('\\textbar'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('∥'), Js('\\|'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('∥'), Js('\\Vert'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('∥'), Js('\\textbardbl'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('~'), Js('\\textasciitilde'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('\\'), Js('\\textbackslash'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('^'), Js('\\textasciicircum'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('↑'), Js('\\uparrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⇑'), Js('\\Uparrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('↓'), Js('\\downarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⇓'), Js('\\Downarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('↕'), Js('\\updownarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('rel'), Js('⇕'), Js('\\Updownarrow'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('∐'), Js('\\coprod'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('⋁'), Js('\\bigvee'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('⋀'), Js('\\bigwedge'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('⨄'), Js('\\biguplus'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('⋂'), Js('\\bigcap'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('⋃'), Js('\\bigcup'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('∫'), Js('\\int'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('∫'), Js('\\intop'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('∬'), Js('\\iint'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('∭'), Js('\\iiint'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('∏'), Js('\\prod'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('∑'), Js('\\sum'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('⨂'), Js('\\bigotimes'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('⨁'), Js('\\bigoplus'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('⨀'), Js('\\bigodot'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('∮'), Js('\\oint'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('∯'), Js('\\oiint'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('∰'), Js('\\oiiint'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('⨆'), Js('\\bigsqcup'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('op'), Js('∫'), Js('\\smallint'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_inner'), Js('…'), Js('\\textellipsis'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_inner'), Js('…'), Js('\\mathellipsis'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_inner'), Js('…'), Js('\\ldots'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_inner'), Js('…'), Js('\\ldots'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_inner'), Js('⋯'), Js('\\@cdots'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_inner'), Js('⋱'), Js('\\ddots'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('⋮'), Js('\\varvdots'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_accent'), Js('ˊ'), Js('\\acute'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_accent'), Js('ˋ'), Js('\\grave'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_accent'), Js('¨'), Js('\\ddot'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_accent'), Js('~'), Js('\\tilde'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_accent'), Js('ˉ'), Js('\\bar'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_accent'), Js('˘'), Js('\\breve'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_accent'), Js('ˇ'), Js('\\check'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_accent'), Js('^'), Js('\\hat'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_accent'), Js('⃗'), Js('\\vec'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_accent'), Js('˙'), Js('\\dot'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_accent'), Js('˚'), Js('\\mathring'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('ı'), Js('\\imath'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('ȷ'), Js('\\jmath'), Js(True))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('ı'), Js('\\i'), Js(True))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('ȷ'), Js('\\j'), Js(True))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('ß'), Js('\\ss'), Js(True))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('æ'), Js('\\ae'), Js(True))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('æ'), Js('\\ae'), Js(True))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('œ'), Js('\\oe'), Js(True))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('ø'), Js('\\o'), Js(True))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('Æ'), Js('\\AE'), Js(True))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('Œ'), Js('\\OE'), Js(True))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('Ø'), Js('\\O'), Js(True))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_accent'), Js('ˊ'), Js("\\'"))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_accent'), Js('ˋ'), Js('\\`'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_accent'), Js('ˆ'), Js('\\^'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_accent'), Js('˜'), Js('\\~'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_accent'), Js('ˉ'), Js('\\='))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_accent'), Js('˘'), Js('\\u'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_accent'), Js('˙'), Js('\\.'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_accent'), Js('˚'), Js('\\r'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_accent'), Js('ˇ'), Js('\\v'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_accent'), Js('¨'), Js('\\"'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_accent'), Js('˝'), Js('\\H'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_accent'), Js('◯'), Js('\\textcircled'))
        var.put('ligatures', Js({'--':Js(True),'---':Js(True),'``':Js(True),"''":Js(True)}))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('–'), Js('--'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('–'), Js('\\textendash'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('—'), Js('---'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('—'), Js('\\textemdash'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('‘'), Js('`'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('‘'), Js('\\textquoteleft'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('’'), Js("'"))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('’'), Js('\\textquoteright'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('“'), Js('``'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('“'), Js('\\textquotedblleft'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('”'), Js("''"))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('”'), Js('\\textquotedblright'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), Js('°'), Js('\\degree'), Js(True))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('°'), Js('\\degree'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('°'), Js('\\textdegree'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('£'), Js('\\pounds'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('£'), Js('\\mathsterling'), Js(True))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('mathord'), Js('£'), Js('\\pounds'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('mathord'), Js('£'), Js('\\textsterling'), Js(True))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('✠'), Js('\\maltese'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('ams'), var.get('symbols_textord'), Js('✠'), Js('\\maltese'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_spacing'), Js('\xa0'), Js('\\ '))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_spacing'), Js('\xa0'), Js(' '))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_spacing'), Js('\xa0'), Js('~'))
        var.put('mathTextSymbols', Js('0123456789/@."'))
        #for JS loop
        var.put('symbols_i', Js(0.0))
        while (var.get('symbols_i')<var.get('mathTextSymbols').get('length')):
            try:
                var.put('symbols_ch', var.get('mathTextSymbols').callprop('charAt', var.get('symbols_i')))
                var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('symbols_textord'), var.get('symbols_ch'), var.get('symbols_ch'))
            finally:
                    (var.put('symbols_i',Js(var.get('symbols_i').to_number())+Js(1))-Js(1))
        var.put('textSymbols', Js('0123456789!@*()-=+[]<>|";:?/.,'))
        #for JS loop
        var.put('src_symbols_i', Js(0.0))
        while (var.get('src_symbols_i')<var.get('textSymbols').get('length')):
            try:
                var.put('_ch', var.get('textSymbols').callprop('charAt', var.get('src_symbols_i')))
                var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), var.get('_ch'), var.get('_ch'))
            finally:
                    (var.put('src_symbols_i',Js(var.get('src_symbols_i').to_number())+Js(1))-Js(1))
        var.put('letters', Js('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'))
        #for JS loop
        var.put('symbols_i2', Js(0.0))
        while (var.get('symbols_i2')<var.get('letters').get('length')):
            try:
                var.put('_ch2', var.get('letters').callprop('charAt', var.get('symbols_i2')))
                var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), var.get('_ch2'), var.get('_ch2'))
                var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), var.get('_ch2'), var.get('_ch2'))
            finally:
                    (var.put('symbols_i2',Js(var.get('symbols_i2').to_number())+Js(1))-Js(1))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('C'), Js('ℂ'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('ams'), var.get('symbols_textord'), Js('C'), Js('ℂ'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('H'), Js('ℍ'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('ams'), var.get('symbols_textord'), Js('H'), Js('ℍ'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('N'), Js('ℕ'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('ams'), var.get('symbols_textord'), Js('N'), Js('ℕ'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('P'), Js('ℙ'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('ams'), var.get('symbols_textord'), Js('P'), Js('ℙ'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('Q'), Js('ℚ'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('ams'), var.get('symbols_textord'), Js('Q'), Js('ℚ'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('R'), Js('ℝ'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('ams'), var.get('symbols_textord'), Js('R'), Js('ℝ'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('ams'), var.get('symbols_textord'), Js('Z'), Js('ℤ'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('ams'), var.get('symbols_textord'), Js('Z'), Js('ℤ'))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('h'), Js('ℎ'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('mathord'), Js('h'), Js('ℎ'))
        var.put('symbols_wideChar', Js(''))
        #for JS loop
        var.put('symbols_i3', Js(0.0))
        while (var.get('symbols_i3')<var.get('letters').get('length')):
            try:
                var.put('_ch3', var.get('letters').callprop('charAt', var.get('symbols_i3')))
                var.put('symbols_wideChar', var.get('String').callprop('fromCharCode', Js(55349), (Js(56320)+var.get('symbols_i3'))))
                var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), var.get('_ch3'), var.get('symbols_wideChar'))
                var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), var.get('_ch3'), var.get('symbols_wideChar'))
                var.put('symbols_wideChar', var.get('String').callprop('fromCharCode', Js(55349), (Js(56372)+var.get('symbols_i3'))))
                var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), var.get('_ch3'), var.get('symbols_wideChar'))
                var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), var.get('_ch3'), var.get('symbols_wideChar'))
                var.put('symbols_wideChar', var.get('String').callprop('fromCharCode', Js(55349), (Js(56424)+var.get('symbols_i3'))))
                var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), var.get('_ch3'), var.get('symbols_wideChar'))
                var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), var.get('_ch3'), var.get('symbols_wideChar'))
                var.put('symbols_wideChar', var.get('String').callprop('fromCharCode', Js(55349), (Js(56580)+var.get('symbols_i3'))))
                var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), var.get('_ch3'), var.get('symbols_wideChar'))
                var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), var.get('_ch3'), var.get('symbols_wideChar'))
                var.put('symbols_wideChar', var.get('String').callprop('fromCharCode', Js(55349), (Js(56736)+var.get('symbols_i3'))))
                var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), var.get('_ch3'), var.get('symbols_wideChar'))
                var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), var.get('_ch3'), var.get('symbols_wideChar'))
                var.put('symbols_wideChar', var.get('String').callprop('fromCharCode', Js(55349), (Js(56788)+var.get('symbols_i3'))))
                var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), var.get('_ch3'), var.get('symbols_wideChar'))
                var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), var.get('_ch3'), var.get('symbols_wideChar'))
                var.put('symbols_wideChar', var.get('String').callprop('fromCharCode', Js(55349), (Js(56840)+var.get('symbols_i3'))))
                var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), var.get('_ch3'), var.get('symbols_wideChar'))
                var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), var.get('_ch3'), var.get('symbols_wideChar'))
                var.put('symbols_wideChar', var.get('String').callprop('fromCharCode', Js(55349), (Js(56944)+var.get('symbols_i3'))))
                var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), var.get('_ch3'), var.get('symbols_wideChar'))
                var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), var.get('_ch3'), var.get('symbols_wideChar'))
                if (var.get('symbols_i3')<Js(26.0)):
                    var.put('symbols_wideChar', var.get('String').callprop('fromCharCode', Js(55349), (Js(56632)+var.get('symbols_i3'))))
                    var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), var.get('_ch3'), var.get('symbols_wideChar'))
                    var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), var.get('_ch3'), var.get('symbols_wideChar'))
                    var.put('symbols_wideChar', var.get('String').callprop('fromCharCode', Js(55349), (Js(56476)+var.get('symbols_i3'))))
                    var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), var.get('_ch3'), var.get('symbols_wideChar'))
                    var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), var.get('_ch3'), var.get('symbols_wideChar'))
            finally:
                    (var.put('symbols_i3',Js(var.get('symbols_i3').to_number())+Js(1))-Js(1))
        var.put('symbols_wideChar', var.get('String').callprop('fromCharCode', Js(55349), Js(56668)))
        var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), Js('k'), var.get('symbols_wideChar'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('k'), var.get('symbols_wideChar'))
        #for JS loop
        var.put('symbols_i4', Js(0.0))
        while (var.get('symbols_i4')<Js(10.0)):
            try:
                var.put('_ch4', var.get('symbols_i4').callprop('toString'))
                var.put('symbols_wideChar', var.get('String').callprop('fromCharCode', Js(55349), (Js(57294)+var.get('symbols_i4'))))
                var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), var.get('_ch4'), var.get('symbols_wideChar'))
                var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), var.get('_ch4'), var.get('symbols_wideChar'))
                var.put('symbols_wideChar', var.get('String').callprop('fromCharCode', Js(55349), (Js(57314)+var.get('symbols_i4'))))
                var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), var.get('_ch4'), var.get('symbols_wideChar'))
                var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), var.get('_ch4'), var.get('symbols_wideChar'))
                var.put('symbols_wideChar', var.get('String').callprop('fromCharCode', Js(55349), (Js(57324)+var.get('symbols_i4'))))
                var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), var.get('_ch4'), var.get('symbols_wideChar'))
                var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), var.get('_ch4'), var.get('symbols_wideChar'))
                var.put('symbols_wideChar', var.get('String').callprop('fromCharCode', Js(55349), (Js(57334)+var.get('symbols_i4'))))
                var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), var.get('_ch4'), var.get('symbols_wideChar'))
                var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), var.get('_ch4'), var.get('symbols_wideChar'))
            finally:
                    (var.put('symbols_i4',Js(var.get('symbols_i4').to_number())+Js(1))-Js(1))
        var.put('extraLatin', Js('ÇÐÞçþ'))
        #for JS loop
        var.put('_i5', Js(0.0))
        while (var.get('_i5')<var.get('extraLatin').get('length')):
            try:
                var.put('_ch5', var.get('extraLatin').callprop('charAt', var.get('_i5')))
                var.get('defineSymbol')(var.get('symbols_math'), var.get('main'), var.get('mathord'), var.get('_ch5'), var.get('_ch5'))
                var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), var.get('_ch5'), var.get('_ch5'))
            finally:
                    (var.put('_i5',Js(var.get('_i5').to_number())+Js(1))-Js(1))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('ð'), Js('ð'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('–'), Js('–'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('—'), Js('—'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('‘'), Js('‘'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('’'), Js('’'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('“'), Js('“'))
        var.get('defineSymbol')(var.get('symbols_text'), var.get('main'), var.get('symbols_textord'), Js('”'), Js('”'))
        var.put('wideLatinLetterData', Js([Js([Js('mathbf'), Js('textbf'), Js('Main-Bold')]), Js([Js('mathbf'), Js('textbf'), Js('Main-Bold')]), Js([Js('mathdefault'), Js('textit'), Js('Math-Italic')]), Js([Js('mathdefault'), Js('textit'), Js('Math-Italic')]), Js([Js('boldsymbol'), Js('boldsymbol'), Js('Main-BoldItalic')]), Js([Js('boldsymbol'), Js('boldsymbol'), Js('Main-BoldItalic')]), Js([Js('mathscr'), Js('textscr'), Js('Script-Regular')]), Js([Js(''), Js(''), Js('')]), Js([Js(''), Js(''), Js('')]), Js([Js(''), Js(''), Js('')]), Js([Js('mathfrak'), Js('textfrak'), Js('Fraktur-Regular')]), Js([Js('mathfrak'), Js('textfrak'), Js('Fraktur-Regular')]), Js([Js('mathbb'), Js('textbb'), Js('AMS-Regular')]), Js([Js('mathbb'), Js('textbb'), Js('AMS-Regular')]), Js([Js(''), Js(''), Js('')]), Js([Js(''), Js(''), Js('')]), Js([Js('mathsf'), Js('textsf'), Js('SansSerif-Regular')]), Js([Js('mathsf'), Js('textsf'), Js('SansSerif-Regular')]), Js([Js('mathboldsf'), Js('textboldsf'), Js('SansSerif-Bold')]), Js([Js('mathboldsf'), Js('textboldsf'), Js('SansSerif-Bold')]), Js([Js('mathitsf'), Js('textitsf'), Js('SansSerif-Italic')]), Js([Js('mathitsf'), Js('textitsf'), Js('SansSerif-Italic')]), Js([Js(''), Js(''), Js('')]), Js([Js(''), Js(''), Js('')]), Js([Js('mathtt'), Js('texttt'), Js('Typewriter-Regular')]), Js([Js('mathtt'), Js('texttt'), Js('Typewriter-Regular')])]))
        var.put('wideNumeralData', Js([Js([Js('mathbf'), Js('textbf'), Js('Main-Bold')]), Js([Js(''), Js(''), Js('')]), Js([Js('mathsf'), Js('textsf'), Js('SansSerif-Regular')]), Js([Js('mathboldsf'), Js('textboldsf'), Js('SansSerif-Bold')]), Js([Js('mathtt'), Js('texttt'), Js('Typewriter-Regular')])]))
        @Js
        def PyJs_wideCharacterFont_71_(wideChar, mode, this, arguments, var=var):
            var = Scope({'wideChar':wideChar, 'mode':mode, 'this':this, 'arguments':arguments, 'wideCharacterFont':PyJs_wideCharacterFont_71_}, var)
            var.registers(['j', 'H', 'i', 'L', 'codePoint', 'wideChar', '_i', 'mode'])
            var.put('H', var.get('wideChar').callprop('charCodeAt', Js(0.0)))
            var.put('L', var.get('wideChar').callprop('charCodeAt', Js(1.0)))
            var.put('codePoint', ((((var.get('H')-Js(55296))*Js(1024))+(var.get('L')-Js(56320)))+Js(65536)))
            var.put('j', (Js(0.0) if PyJsStrictEq(var.get('mode'),Js('math')) else Js(1.0)))
            if ((Js(119808)<=var.get('codePoint')) and (var.get('codePoint')<Js(120484))):
                var.put('i', var.get('Math').callprop('floor', ((var.get('codePoint')-Js(119808))/Js(26.0))))
                return Js([var.get('wideLatinLetterData').get(var.get('i')).get('2'), var.get('wideLatinLetterData').get(var.get('i')).get(var.get('j'))])
            else:
                if ((Js(120782)<=var.get('codePoint')) and (var.get('codePoint')<=Js(120831))):
                    var.put('_i', var.get('Math').callprop('floor', ((var.get('codePoint')-Js(120782))/Js(10.0))))
                    return Js([var.get('wideNumeralData').get(var.get('_i')).get('2'), var.get('wideNumeralData').get(var.get('_i')).get(var.get('j'))])
                else:
                    if (PyJsStrictEq(var.get('codePoint'),Js(120485)) or PyJsStrictEq(var.get('codePoint'),Js(120486))):
                        return Js([var.get('wideLatinLetterData').get('0').get('2'), var.get('wideLatinLetterData').get('0').get(var.get('j'))])
                    else:
                        if ((Js(120486)<var.get('codePoint')) and (var.get('codePoint')<Js(120782))):
                            return Js([Js(''), Js('')])
                        else:
                            PyJsTempException = JsToPyException(var.get('src_ParseError').create((Js('Unsupported character: ')+var.get('wideChar'))))
                            raise PyJsTempException
        PyJs_wideCharacterFont_71_._set_name('wideCharacterFont')
        var.put('wide_character_wideCharacterFont', PyJs_wideCharacterFont_71_)
        var.put('sizeStyleMap', Js([Js([Js(1.0), Js(1.0), Js(1.0)]), Js([Js(2.0), Js(1.0), Js(1.0)]), Js([Js(3.0), Js(1.0), Js(1.0)]), Js([Js(4.0), Js(2.0), Js(1.0)]), Js([Js(5.0), Js(2.0), Js(1.0)]), Js([Js(6.0), Js(3.0), Js(1.0)]), Js([Js(7.0), Js(4.0), Js(2.0)]), Js([Js(8.0), Js(6.0), Js(3.0)]), Js([Js(9.0), Js(7.0), Js(6.0)]), Js([Js(10.0), Js(8.0), Js(7.0)]), Js([Js(11.0), Js(10.0), Js(9.0)])]))
        var.put('sizeMultipliers', Js([Js(0.5), Js(0.6), Js(0.7), Js(0.8), Js(0.9), Js(1.0), Js(1.2), Js(1.44), Js(1.728), Js(2.074), Js(2.488)]))
        @Js
        def PyJs_sizeAtStyle_72_(size, style, this, arguments, var=var):
            var = Scope({'size':size, 'style':style, 'this':this, 'arguments':arguments, 'sizeAtStyle':PyJs_sizeAtStyle_72_}, var)
            var.registers(['style', 'size'])
            return (var.get('size') if (var.get('style').get('size')<Js(2.0)) else var.get('sizeStyleMap').get((var.get('size')-Js(1.0))).get((var.get('style').get('size')-Js(1.0))))
        PyJs_sizeAtStyle_72_._set_name('sizeAtStyle')
        var.put('sizeAtStyle', PyJs_sizeAtStyle_72_)
        @Js
        def PyJs_anonymous_73_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['_proto', 'Options'])
            @Js
            def PyJsHoisted_Options_(data, this, arguments, var=var):
                var = Scope({'data':data, 'this':this, 'arguments':arguments}, var)
                var.registers(['data'])
                var.get(u"this").put('style', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('color', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('size', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('textSize', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('phantom', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('font', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('fontFamily', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('fontWeight', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('fontShape', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('sizeMultiplier', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('maxSize', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('_fontMetrics', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('style', var.get('data').get('style'))
                var.get(u"this").put('color', var.get('data').get('color'))
                var.get(u"this").put('size', (var.get('data').get('size') or var.get('Options').get('BASESIZE')))
                var.get(u"this").put('textSize', (var.get('data').get('textSize') or var.get(u"this").get('size')))
                var.get(u"this").put('phantom', var.get('data').get('phantom').neg().neg())
                var.get(u"this").put('font', (var.get('data').get('font') or Js('')))
                var.get(u"this").put('fontFamily', (var.get('data').get('fontFamily') or Js('')))
                var.get(u"this").put('fontWeight', (var.get('data').get('fontWeight') or Js('')))
                var.get(u"this").put('fontShape', (var.get('data').get('fontShape') or Js('')))
                var.get(u"this").put('sizeMultiplier', var.get('sizeMultipliers').get((var.get(u"this").get('size')-Js(1.0))))
                var.get(u"this").put('maxSize', var.get('data').get('maxSize'))
                var.get(u"this").put('_fontMetrics', var.get('undefined'))
            PyJsHoisted_Options_.func_name = 'Options'
            var.put('Options', PyJsHoisted_Options_)
            pass
            var.put('_proto', var.get('Options').get('prototype'))
            @Js
            def PyJs_extend_74_(extension, this, arguments, var=var):
                var = Scope({'extension':extension, 'this':this, 'arguments':arguments, 'extend':PyJs_extend_74_}, var)
                var.registers(['key', 'extension', 'data'])
                var.put('data', Js({'style':var.get(u"this").get('style'),'size':var.get(u"this").get('size'),'textSize':var.get(u"this").get('textSize'),'color':var.get(u"this").get('color'),'phantom':var.get(u"this").get('phantom'),'font':var.get(u"this").get('font'),'fontFamily':var.get(u"this").get('fontFamily'),'fontWeight':var.get(u"this").get('fontWeight'),'fontShape':var.get(u"this").get('fontShape'),'maxSize':var.get(u"this").get('maxSize')}))
                for PyJsTemp in var.get('extension'):
                    var.put('key', PyJsTemp)
                    if var.get('extension').callprop('hasOwnProperty', var.get('key')):
                        var.get('data').put(var.get('key'), var.get('extension').get(var.get('key')))
                return var.get('Options').create(var.get('data'))
            PyJs_extend_74_._set_name('extend')
            var.get('_proto').put('extend', PyJs_extend_74_)
            @Js
            def PyJs_havingStyle_75_(style, this, arguments, var=var):
                var = Scope({'style':style, 'this':this, 'arguments':arguments, 'havingStyle':PyJs_havingStyle_75_}, var)
                var.registers(['style'])
                if PyJsStrictEq(var.get(u"this").get('style'),var.get('style')):
                    return var.get(u"this")
                else:
                    return var.get(u"this").callprop('extend', Js({'style':var.get('style'),'size':var.get('sizeAtStyle')(var.get(u"this").get('textSize'), var.get('style'))}))
            PyJs_havingStyle_75_._set_name('havingStyle')
            var.get('_proto').put('havingStyle', PyJs_havingStyle_75_)
            @Js
            def PyJs_havingCrampedStyle_76_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'havingCrampedStyle':PyJs_havingCrampedStyle_76_}, var)
                var.registers([])
                return var.get(u"this").callprop('havingStyle', var.get(u"this").get('style').callprop('cramp'))
            PyJs_havingCrampedStyle_76_._set_name('havingCrampedStyle')
            var.get('_proto').put('havingCrampedStyle', PyJs_havingCrampedStyle_76_)
            @Js
            def PyJs_havingSize_77_(size, this, arguments, var=var):
                var = Scope({'size':size, 'this':this, 'arguments':arguments, 'havingSize':PyJs_havingSize_77_}, var)
                var.registers(['size'])
                if (PyJsStrictEq(var.get(u"this").get('size'),var.get('size')) and PyJsStrictEq(var.get(u"this").get('textSize'),var.get('size'))):
                    return var.get(u"this")
                else:
                    return var.get(u"this").callprop('extend', Js({'style':var.get(u"this").get('style').callprop('text'),'size':var.get('size'),'textSize':var.get('size'),'sizeMultiplier':var.get('sizeMultipliers').get((var.get('size')-Js(1.0)))}))
            PyJs_havingSize_77_._set_name('havingSize')
            var.get('_proto').put('havingSize', PyJs_havingSize_77_)
            @Js
            def PyJs_havingBaseStyle_78_(style, this, arguments, var=var):
                var = Scope({'style':style, 'this':this, 'arguments':arguments, 'havingBaseStyle':PyJs_havingBaseStyle_78_}, var)
                var.registers(['style', 'wantSize'])
                var.put('style', (var.get('style') or var.get(u"this").get('style').callprop('text')))
                var.put('wantSize', var.get('sizeAtStyle')(var.get('Options').get('BASESIZE'), var.get('style')))
                if ((PyJsStrictEq(var.get(u"this").get('size'),var.get('wantSize')) and PyJsStrictEq(var.get(u"this").get('textSize'),var.get('Options').get('BASESIZE'))) and PyJsStrictEq(var.get(u"this").get('style'),var.get('style'))):
                    return var.get(u"this")
                else:
                    return var.get(u"this").callprop('extend', Js({'style':var.get('style'),'size':var.get('wantSize')}))
            PyJs_havingBaseStyle_78_._set_name('havingBaseStyle')
            var.get('_proto').put('havingBaseStyle', PyJs_havingBaseStyle_78_)
            @Js
            def PyJs_havingBaseSizing_79_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'havingBaseSizing':PyJs_havingBaseSizing_79_}, var)
                var.registers(['size'])
                pass
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get(u"this").get('style').get('id'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                        SWITCHED = True
                        var.put('size', Js(3.0))
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                        SWITCHED = True
                        var.put('size', Js(1.0))
                        break
                    if True:
                        SWITCHED = True
                        var.put('size', Js(6.0))
                    SWITCHED = True
                    break
                return var.get(u"this").callprop('extend', Js({'style':var.get(u"this").get('style').callprop('text'),'size':var.get('size')}))
            PyJs_havingBaseSizing_79_._set_name('havingBaseSizing')
            var.get('_proto').put('havingBaseSizing', PyJs_havingBaseSizing_79_)
            @Js
            def PyJs_withColor_80_(color, this, arguments, var=var):
                var = Scope({'color':color, 'this':this, 'arguments':arguments, 'withColor':PyJs_withColor_80_}, var)
                var.registers(['color'])
                return var.get(u"this").callprop('extend', Js({'color':var.get('color')}))
            PyJs_withColor_80_._set_name('withColor')
            var.get('_proto').put('withColor', PyJs_withColor_80_)
            @Js
            def PyJs_withPhantom_81_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'withPhantom':PyJs_withPhantom_81_}, var)
                var.registers([])
                return var.get(u"this").callprop('extend', Js({'phantom':Js(True)}))
            PyJs_withPhantom_81_._set_name('withPhantom')
            var.get('_proto').put('withPhantom', PyJs_withPhantom_81_)
            @Js
            def PyJs_withFont_82_(font, this, arguments, var=var):
                var = Scope({'font':font, 'this':this, 'arguments':arguments, 'withFont':PyJs_withFont_82_}, var)
                var.registers(['font'])
                return var.get(u"this").callprop('extend', Js({'font':var.get('font')}))
            PyJs_withFont_82_._set_name('withFont')
            var.get('_proto').put('withFont', PyJs_withFont_82_)
            @Js
            def PyJs_withTextFontFamily_83_(fontFamily, this, arguments, var=var):
                var = Scope({'fontFamily':fontFamily, 'this':this, 'arguments':arguments, 'withTextFontFamily':PyJs_withTextFontFamily_83_}, var)
                var.registers(['fontFamily'])
                return var.get(u"this").callprop('extend', Js({'fontFamily':var.get('fontFamily'),'font':Js('')}))
            PyJs_withTextFontFamily_83_._set_name('withTextFontFamily')
            var.get('_proto').put('withTextFontFamily', PyJs_withTextFontFamily_83_)
            @Js
            def PyJs_withTextFontWeight_84_(fontWeight, this, arguments, var=var):
                var = Scope({'fontWeight':fontWeight, 'this':this, 'arguments':arguments, 'withTextFontWeight':PyJs_withTextFontWeight_84_}, var)
                var.registers(['fontWeight'])
                return var.get(u"this").callprop('extend', Js({'fontWeight':var.get('fontWeight'),'font':Js('')}))
            PyJs_withTextFontWeight_84_._set_name('withTextFontWeight')
            var.get('_proto').put('withTextFontWeight', PyJs_withTextFontWeight_84_)
            @Js
            def PyJs_withTextFontShape_85_(fontShape, this, arguments, var=var):
                var = Scope({'fontShape':fontShape, 'this':this, 'arguments':arguments, 'withTextFontShape':PyJs_withTextFontShape_85_}, var)
                var.registers(['fontShape'])
                return var.get(u"this").callprop('extend', Js({'fontShape':var.get('fontShape'),'font':Js('')}))
            PyJs_withTextFontShape_85_._set_name('withTextFontShape')
            var.get('_proto').put('withTextFontShape', PyJs_withTextFontShape_85_)
            @Js
            def PyJs_sizingClasses_86_(oldOptions, this, arguments, var=var):
                var = Scope({'oldOptions':oldOptions, 'this':this, 'arguments':arguments, 'sizingClasses':PyJs_sizingClasses_86_}, var)
                var.registers(['oldOptions'])
                if PyJsStrictNeq(var.get('oldOptions').get('size'),var.get(u"this").get('size')):
                    return Js([Js('sizing'), (Js('reset-size')+var.get('oldOptions').get('size')), (Js('size')+var.get(u"this").get('size'))])
                else:
                    return Js([])
            PyJs_sizingClasses_86_._set_name('sizingClasses')
            var.get('_proto').put('sizingClasses', PyJs_sizingClasses_86_)
            @Js
            def PyJs_baseSizingClasses_87_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'baseSizingClasses':PyJs_baseSizingClasses_87_}, var)
                var.registers([])
                if PyJsStrictNeq(var.get(u"this").get('size'),var.get('Options').get('BASESIZE')):
                    return Js([Js('sizing'), (Js('reset-size')+var.get(u"this").get('size')), (Js('size')+var.get('Options').get('BASESIZE'))])
                else:
                    return Js([])
            PyJs_baseSizingClasses_87_._set_name('baseSizingClasses')
            var.get('_proto').put('baseSizingClasses', PyJs_baseSizingClasses_87_)
            @Js
            def PyJs_fontMetrics_88_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'fontMetrics':PyJs_fontMetrics_88_}, var)
                var.registers([])
                if var.get(u"this").get('_fontMetrics').neg():
                    var.get(u"this").put('_fontMetrics', var.get('getGlobalMetrics')(var.get(u"this").get('size')))
                return var.get(u"this").get('_fontMetrics')
            PyJs_fontMetrics_88_._set_name('fontMetrics')
            var.get('_proto').put('fontMetrics', PyJs_fontMetrics_88_)
            @Js
            def PyJs_getColor_89_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'getColor':PyJs_getColor_89_}, var)
                var.registers([])
                if var.get(u"this").get('phantom'):
                    return Js('transparent')
                else:
                    return var.get(u"this").get('color')
            PyJs_getColor_89_._set_name('getColor')
            var.get('_proto').put('getColor', PyJs_getColor_89_)
            return var.get('Options')
        PyJs_anonymous_73_._set_name('anonymous')
        var.put('Options_Options', PyJs_anonymous_73_())
        var.get('Options_Options').put('BASESIZE', Js(6.0))
        var.put('src_Options', var.get('Options_Options'))
        var.put('ptPerUnit', Js({'pt':Js(1.0),'mm':(Js(7227.0)/Js(2540.0)),'cm':(Js(7227.0)/Js(254.0)),'in':Js(72.27),'bp':(Js(803.0)/Js(800.0)),'pc':Js(12.0),'dd':(Js(1238.0)/Js(1157.0)),'cc':(Js(14856.0)/Js(1157.0)),'nd':(Js(685.0)/Js(642.0)),'nc':(Js(1370.0)/Js(107.0)),'sp':(Js(1.0)/Js(65536.0)),'px':(Js(803.0)/Js(800.0))}))
        var.put('relativeUnit', Js({'ex':Js(True),'em':Js(True),'mu':Js(True)}))
        @Js
        def PyJs_validUnit_90_(unit, this, arguments, var=var):
            var = Scope({'unit':unit, 'this':this, 'arguments':arguments, 'validUnit':PyJs_validUnit_90_}, var)
            var.registers(['unit'])
            if PyJsStrictNeq(var.get('unit',throw=False).typeof(),Js('string')):
                var.put('unit', var.get('unit').get('unit'))
            return ((var.get('ptPerUnit').contains(var.get('unit')) or var.get('relativeUnit').contains(var.get('unit'))) or PyJsStrictEq(var.get('unit'),Js('ex')))
        PyJs_validUnit_90_._set_name('validUnit')
        var.put('validUnit', PyJs_validUnit_90_)
        @Js
        def PyJs_calculateSize_91_(sizeValue, options, this, arguments, var=var):
            var = Scope({'sizeValue':sizeValue, 'options':options, 'this':this, 'arguments':arguments, 'calculateSize':PyJs_calculateSize_91_}, var)
            var.registers(['scale', 'sizeValue', 'unitOptions', 'options'])
            pass
            if var.get('ptPerUnit').contains(var.get('sizeValue').get('unit')):
                var.put('scale', ((var.get('ptPerUnit').get(var.get('sizeValue').get('unit'))/var.get('options').callprop('fontMetrics').get('ptPerEm'))/var.get('options').get('sizeMultiplier')))
            else:
                if PyJsStrictEq(var.get('sizeValue').get('unit'),Js('mu')):
                    var.put('scale', var.get('options').callprop('fontMetrics').get('cssEmPerMu'))
                else:
                    pass
                    if var.get('options').get('style').callprop('isTight'):
                        var.put('unitOptions', var.get('options').callprop('havingStyle', var.get('options').get('style').callprop('text')))
                    else:
                        var.put('unitOptions', var.get('options'))
                    if PyJsStrictEq(var.get('sizeValue').get('unit'),Js('ex')):
                        var.put('scale', var.get('unitOptions').callprop('fontMetrics').get('xHeight'))
                    else:
                        if PyJsStrictEq(var.get('sizeValue').get('unit'),Js('em')):
                            var.put('scale', var.get('unitOptions').callprop('fontMetrics').get('quad'))
                        else:
                            PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js("Invalid unit: '")+var.get('sizeValue').get('unit'))+Js("'"))))
                            raise PyJsTempException
                    if PyJsStrictNeq(var.get('unitOptions'),var.get('options')):
                        var.put('scale', (var.get('unitOptions').get('sizeMultiplier')/var.get('options').get('sizeMultiplier')), '*')
            return var.get('Math').callprop('min', (var.get('sizeValue').get('number')*var.get('scale')), var.get('options').get('maxSize'))
        PyJs_calculateSize_91_._set_name('calculateSize')
        var.put('units_calculateSize', PyJs_calculateSize_91_)
        var.put('mathitLetters', Js([Js('\\imath'), Js('ı'), Js('\\jmath'), Js('ȷ'), Js('\\pounds'), Js('\\mathsterling'), Js('\\textsterling'), Js('£')]))
        @Js
        def PyJs_lookupSymbol_92_(value, fontName, mode, this, arguments, var=var):
            var = Scope({'value':value, 'fontName':fontName, 'mode':mode, 'this':this, 'arguments':arguments, 'lookupSymbol':PyJs_lookupSymbol_92_}, var)
            var.registers(['fontName', 'value', 'mode'])
            if (var.get('src_symbols').get(var.get('mode')).get(var.get('value')) and var.get('src_symbols').get(var.get('mode')).get(var.get('value')).get('replace')):
                var.put('value', var.get('src_symbols').get(var.get('mode')).get(var.get('value')).get('replace'))
            return Js({'value':var.get('value'),'metrics':var.get('getCharacterMetrics')(var.get('value'), var.get('fontName'), var.get('mode'))})
        PyJs_lookupSymbol_92_._set_name('lookupSymbol')
        var.put('buildCommon_lookupSymbol', PyJs_lookupSymbol_92_)
        @Js
        def PyJs_makeSymbol_93_(value, fontName, mode, options, classes, this, arguments, var=var):
            var = Scope({'value':value, 'fontName':fontName, 'mode':mode, 'options':options, 'classes':classes, 'this':this, 'arguments':arguments, 'makeSymbol':PyJs_makeSymbol_93_}, var)
            var.registers(['fontName', 'symbolNode', 'value', 'color', 'italic', 'mode', 'options', 'lookup', 'classes', 'metrics'])
            var.put('lookup', var.get('buildCommon_lookupSymbol')(var.get('value'), var.get('fontName'), var.get('mode')))
            var.put('metrics', var.get('lookup').get('metrics'))
            var.put('value', var.get('lookup').get('value'))
            pass
            if var.get('metrics'):
                var.put('italic', var.get('metrics').get('italic'))
                if (PyJsStrictEq(var.get('mode'),Js('text')) or (var.get('options') and PyJsStrictEq(var.get('options').get('font'),Js('mathit')))):
                    var.put('italic', Js(0.0))
                var.put('symbolNode', var.get('domTree_SymbolNode').create(var.get('value'), var.get('metrics').get('height'), var.get('metrics').get('depth'), var.get('italic'), var.get('metrics').get('skew'), var.get('metrics').get('width'), var.get('classes')))
            else:
                (PyJsStrictNeq(var.get('console',throw=False).typeof(),Js('undefined')) and var.get('console').callprop('warn', ((((Js("No character metrics for '")+var.get('value'))+Js("' in style '"))+var.get('fontName'))+Js("'"))))
                var.put('symbolNode', var.get('domTree_SymbolNode').create(var.get('value'), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), var.get('classes')))
            if var.get('options'):
                var.get('symbolNode').put('maxFontSize', var.get('options').get('sizeMultiplier'))
                if var.get('options').get('style').callprop('isTight'):
                    var.get('symbolNode').get('classes').callprop('push', Js('mtight'))
                var.put('color', var.get('options').callprop('getColor'))
                if var.get('color'):
                    var.get('symbolNode').get('style').put('color', var.get('color'))
            return var.get('symbolNode')
        PyJs_makeSymbol_93_._set_name('makeSymbol')
        var.put('buildCommon_makeSymbol', PyJs_makeSymbol_93_)
        @Js
        def PyJs_mathsym_94_(value, mode, options, classes, this, arguments, var=var):
            var = Scope({'value':value, 'mode':mode, 'options':options, 'classes':classes, 'this':this, 'arguments':arguments, 'mathsym':PyJs_mathsym_94_}, var)
            var.registers(['options', 'classes', 'value', 'mode'])
            if PyJsStrictEq(var.get('classes'),PyJsComma(Js(0.0), Js(None))):
                var.put('classes', Js([]))
            if (((var.get('options') and var.get('options').get('font')) and PyJsStrictEq(var.get('options').get('font'),Js('boldsymbol'))) and var.get('buildCommon_lookupSymbol')(var.get('value'), Js('Main-Bold'), var.get('mode')).get('metrics')):
                return var.get('buildCommon_makeSymbol')(var.get('value'), Js('Main-Bold'), var.get('mode'), var.get('options'), var.get('classes').callprop('concat', Js([Js('mathbf')])))
            else:
                if (PyJsStrictEq(var.get('value'),Js('\\')) or PyJsStrictEq(var.get('src_symbols').get(var.get('mode')).get(var.get('value')).get('font'),Js('main'))):
                    return var.get('buildCommon_makeSymbol')(var.get('value'), Js('Main-Regular'), var.get('mode'), var.get('options'), var.get('classes'))
                else:
                    return var.get('buildCommon_makeSymbol')(var.get('value'), Js('AMS-Regular'), var.get('mode'), var.get('options'), var.get('classes').callprop('concat', Js([Js('amsrm')])))
        PyJs_mathsym_94_._set_name('mathsym')
        var.put('buildCommon_mathsym', PyJs_mathsym_94_)
        @Js
        def PyJs_mathdefault_95_(value, mode, options, classes, this, arguments, var=var):
            var = Scope({'value':value, 'mode':mode, 'options':options, 'classes':classes, 'this':this, 'arguments':arguments, 'mathdefault':PyJs_mathdefault_95_}, var)
            var.registers(['options', 'classes', 'value', 'mode'])
            if (JsRegExp('/[0-9]/').callprop('test', var.get('value').callprop('charAt', Js(0.0))) or var.get('utils').callprop('contains', var.get('mathitLetters'), var.get('value'))):
                return Js({'fontName':Js('Main-Italic'),'fontClass':Js('mathit')})
            else:
                return Js({'fontName':Js('Math-Italic'),'fontClass':Js('mathdefault')})
        PyJs_mathdefault_95_._set_name('mathdefault')
        var.put('buildCommon_mathdefault', PyJs_mathdefault_95_)
        @Js
        def PyJs_mathnormal_96_(value, mode, options, classes, this, arguments, var=var):
            var = Scope({'value':value, 'mode':mode, 'options':options, 'classes':classes, 'this':this, 'arguments':arguments, 'mathnormal':PyJs_mathnormal_96_}, var)
            var.registers(['options', 'classes', 'value', 'mode'])
            if var.get('utils').callprop('contains', var.get('mathitLetters'), var.get('value')):
                return Js({'fontName':Js('Main-Italic'),'fontClass':Js('mathit')})
            else:
                if JsRegExp('/[0-9]/').callprop('test', var.get('value').callprop('charAt', Js(0.0))):
                    return Js({'fontName':Js('Caligraphic-Regular'),'fontClass':Js('mathcal')})
                else:
                    return Js({'fontName':Js('Math-Italic'),'fontClass':Js('mathdefault')})
        PyJs_mathnormal_96_._set_name('mathnormal')
        var.put('buildCommon_mathnormal', PyJs_mathnormal_96_)
        @Js
        def PyJs_boldsymbol_97_(value, mode, options, classes, this, arguments, var=var):
            var = Scope({'value':value, 'mode':mode, 'options':options, 'classes':classes, 'this':this, 'arguments':arguments, 'boldsymbol':PyJs_boldsymbol_97_}, var)
            var.registers(['options', 'classes', 'value', 'mode'])
            if var.get('buildCommon_lookupSymbol')(var.get('value'), Js('Math-BoldItalic'), var.get('mode')).get('metrics'):
                return Js({'fontName':Js('Math-BoldItalic'),'fontClass':Js('boldsymbol')})
            else:
                return Js({'fontName':Js('Main-Bold'),'fontClass':Js('mathbf')})
        PyJs_boldsymbol_97_._set_name('boldsymbol')
        var.put('boldsymbol', PyJs_boldsymbol_97_)
        @Js
        def PyJs_makeOrd_98_(group, options, type, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'type':type, 'this':this, 'arguments':arguments, 'makeOrd':PyJs_makeOrd_98_}, var)
            var.registers(['fontData', 'mode', 'parts', 'i', 'options', '_fontName2', 'fontClasses', 'classes', 'fontLookup', '_fontName', 'fontName', 'fontOrFamily', 'type', 'font', 'wideFontClass', 'group', 'text', 'wideFontName', '_fontName3', 'isFont', '_wideCharacterFont'])
            var.put('mode', var.get('group').get('mode'))
            var.put('text', var.get('group').get('text'))
            var.put('classes', Js([Js('mord')]))
            var.put('isFont', (PyJsStrictEq(var.get('mode'),Js('math')) or (PyJsStrictEq(var.get('mode'),Js('text')) and var.get('options').get('font'))))
            var.put('fontOrFamily', (var.get('options').get('font') if var.get('isFont') else var.get('options').get('fontFamily')))
            if PyJsStrictEq(var.get('text').callprop('charCodeAt', Js(0.0)),Js(55349)):
                var.put('_wideCharacterFont', var.get('wide_character_wideCharacterFont')(var.get('text'), var.get('mode')))
                var.put('wideFontName', var.get('_wideCharacterFont').get('0'))
                var.put('wideFontClass', var.get('_wideCharacterFont').get('1'))
                return var.get('buildCommon_makeSymbol')(var.get('text'), var.get('wideFontName'), var.get('mode'), var.get('options'), var.get('classes').callprop('concat', var.get('wideFontClass')))
            else:
                if var.get('fontOrFamily'):
                    pass
                    pass
                    if (PyJsStrictEq(var.get('fontOrFamily'),Js('boldsymbol')) or PyJsStrictEq(var.get('fontOrFamily'),Js('mathnormal'))):
                        var.put('fontData', (var.get('boldsymbol')(var.get('text'), var.get('mode'), var.get('options'), var.get('classes')) if PyJsStrictEq(var.get('fontOrFamily'),Js('boldsymbol')) else var.get('buildCommon_mathnormal')(var.get('text'), var.get('mode'), var.get('options'), var.get('classes'))))
                        var.put('fontName', var.get('fontData').get('fontName'))
                        var.put('fontClasses', Js([var.get('fontData').get('fontClass')]))
                    else:
                        if var.get('utils').callprop('contains', var.get('mathitLetters'), var.get('text')):
                            var.put('fontName', Js('Main-Italic'))
                            var.put('fontClasses', Js([Js('mathit')]))
                        else:
                            if var.get('isFont'):
                                var.put('fontName', var.get('fontMap').get(var.get('fontOrFamily')).get('fontName'))
                                var.put('fontClasses', Js([var.get('fontOrFamily')]))
                            else:
                                var.put('fontName', var.get('retrieveTextFontName')(var.get('fontOrFamily'), var.get('options').get('fontWeight'), var.get('options').get('fontShape')))
                                var.put('fontClasses', Js([var.get('fontOrFamily'), var.get('options').get('fontWeight'), var.get('options').get('fontShape')]))
                    if var.get('buildCommon_lookupSymbol')(var.get('text'), var.get('fontName'), var.get('mode')).get('metrics'):
                        return var.get('buildCommon_makeSymbol')(var.get('text'), var.get('fontName'), var.get('mode'), var.get('options'), var.get('classes').callprop('concat', var.get('fontClasses')))
                    else:
                        if (var.get('ligatures').callprop('hasOwnProperty', var.get('text')) and PyJsStrictEq(var.get('fontName').callprop('substr', Js(0.0), Js(10.0)),Js('Typewriter'))):
                            var.put('parts', Js([]))
                            #for JS loop
                            var.put('i', Js(0.0))
                            while (var.get('i')<var.get('text').get('length')):
                                try:
                                    var.get('parts').callprop('push', var.get('buildCommon_makeSymbol')(var.get('text').get(var.get('i')), var.get('fontName'), var.get('mode'), var.get('options'), var.get('classes').callprop('concat', var.get('fontClasses'))))
                                finally:
                                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                            return var.get('buildCommon_makeFragment')(var.get('parts'))
            if PyJsStrictEq(var.get('type'),Js('mathord')):
                var.put('fontLookup', var.get('buildCommon_mathdefault')(var.get('text'), var.get('mode'), var.get('options'), var.get('classes')))
                return var.get('buildCommon_makeSymbol')(var.get('text'), var.get('fontLookup').get('fontName'), var.get('mode'), var.get('options'), var.get('classes').callprop('concat', Js([var.get('fontLookup').get('fontClass')])))
            else:
                if PyJsStrictEq(var.get('type'),Js('textord')):
                    var.put('font', (var.get('src_symbols').get(var.get('mode')).get(var.get('text')) and var.get('src_symbols').get(var.get('mode')).get(var.get('text')).get('font')))
                    if PyJsStrictEq(var.get('font'),Js('ams')):
                        var.put('_fontName', var.get('retrieveTextFontName')(Js('amsrm'), var.get('options').get('fontWeight'), var.get('options').get('fontShape')))
                        return var.get('buildCommon_makeSymbol')(var.get('text'), var.get('_fontName'), var.get('mode'), var.get('options'), var.get('classes').callprop('concat', Js('amsrm'), var.get('options').get('fontWeight'), var.get('options').get('fontShape')))
                    else:
                        if (PyJsStrictEq(var.get('font'),Js('main')) or var.get('font').neg()):
                            var.put('_fontName2', var.get('retrieveTextFontName')(Js('textrm'), var.get('options').get('fontWeight'), var.get('options').get('fontShape')))
                            return var.get('buildCommon_makeSymbol')(var.get('text'), var.get('_fontName2'), var.get('mode'), var.get('options'), var.get('classes').callprop('concat', var.get('options').get('fontWeight'), var.get('options').get('fontShape')))
                        else:
                            var.put('_fontName3', var.get('retrieveTextFontName')(var.get('font'), var.get('options').get('fontWeight'), var.get('options').get('fontShape')))
                            return var.get('buildCommon_makeSymbol')(var.get('text'), var.get('_fontName3'), var.get('mode'), var.get('options'), var.get('classes').callprop('concat', var.get('_fontName3'), var.get('options').get('fontWeight'), var.get('options').get('fontShape')))
                else:
                    PyJsTempException = JsToPyException(var.get('Error').create(((Js('unexpected type: ')+var.get('type'))+Js(' in makeOrd'))))
                    raise PyJsTempException
        PyJs_makeOrd_98_._set_name('makeOrd')
        var.put('buildCommon_makeOrd', PyJs_makeOrd_98_)
        @Js
        def PyJs_canCombine_99_(prev, next, this, arguments, var=var):
            var = Scope({'prev':prev, 'next':next, 'this':this, 'arguments':arguments, 'canCombine':PyJs_canCombine_99_}, var)
            var.registers(['prev', 'style', '_style', 'next'])
            if ((PyJsStrictNeq(var.get('createClass')(var.get('prev').get('classes')),var.get('createClass')(var.get('next').get('classes'))) or PyJsStrictNeq(var.get('prev').get('skew'),var.get('next').get('skew'))) or PyJsStrictNeq(var.get('prev').get('maxFontSize'),var.get('next').get('maxFontSize'))):
                return Js(False)
            for PyJsTemp in var.get('prev').get('style'):
                var.put('style', PyJsTemp)
                if (var.get('prev').get('style').callprop('hasOwnProperty', var.get('style')) and PyJsStrictNeq(var.get('prev').get('style').get(var.get('style')),var.get('next').get('style').get(var.get('style')))):
                    return Js(False)
            for PyJsTemp in var.get('next').get('style'):
                var.put('_style', PyJsTemp)
                if (var.get('next').get('style').callprop('hasOwnProperty', var.get('_style')) and PyJsStrictNeq(var.get('prev').get('style').get(var.get('_style')),var.get('next').get('style').get(var.get('_style')))):
                    return Js(False)
            return Js(True)
        PyJs_canCombine_99_._set_name('canCombine')
        var.put('buildCommon_canCombine', PyJs_canCombine_99_)
        @Js
        def PyJs_tryCombineChars_100_(chars, this, arguments, var=var):
            var = Scope({'chars':chars, 'this':this, 'arguments':arguments, 'tryCombineChars':PyJs_tryCombineChars_100_}, var)
            var.registers(['prev', 'chars', 'i', 'next'])
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<(var.get('chars').get('length')-Js(1.0))):
                try:
                    var.put('prev', var.get('chars').get(var.get('i')))
                    var.put('next', var.get('chars').get((var.get('i')+Js(1.0))))
                    if ((var.get('prev').instanceof(var.get('domTree_SymbolNode')) and var.get('next').instanceof(var.get('domTree_SymbolNode'))) and var.get('buildCommon_canCombine')(var.get('prev'), var.get('next'))):
                        var.get('prev').put('text', var.get('next').get('text'), '+')
                        var.get('prev').put('height', var.get('Math').callprop('max', var.get('prev').get('height'), var.get('next').get('height')))
                        var.get('prev').put('depth', var.get('Math').callprop('max', var.get('prev').get('depth'), var.get('next').get('depth')))
                        var.get('prev').put('italic', var.get('next').get('italic'))
                        var.get('chars').callprop('splice', (var.get('i')+Js(1.0)), Js(1.0))
                        (var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            return var.get('chars')
        PyJs_tryCombineChars_100_._set_name('tryCombineChars')
        var.put('buildCommon_tryCombineChars', PyJs_tryCombineChars_100_)
        @Js
        def PyJs_sizeElementFromChildren_101_(elem, this, arguments, var=var):
            var = Scope({'elem':elem, 'this':this, 'arguments':arguments, 'sizeElementFromChildren':PyJs_sizeElementFromChildren_101_}, var)
            var.registers(['elem', 'i', 'depth', 'child', 'maxFontSize', 'height'])
            var.put('height', Js(0.0))
            var.put('depth', Js(0.0))
            var.put('maxFontSize', Js(0.0))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('elem').get('children').get('length')):
                try:
                    var.put('child', var.get('elem').get('children').get(var.get('i')))
                    if (var.get('child').get('height')>var.get('height')):
                        var.put('height', var.get('child').get('height'))
                    if (var.get('child').get('depth')>var.get('depth')):
                        var.put('depth', var.get('child').get('depth'))
                    if (var.get('child').get('maxFontSize')>var.get('maxFontSize')):
                        var.put('maxFontSize', var.get('child').get('maxFontSize'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.get('elem').put('height', var.get('height'))
            var.get('elem').put('depth', var.get('depth'))
            var.get('elem').put('maxFontSize', var.get('maxFontSize'))
        PyJs_sizeElementFromChildren_101_._set_name('sizeElementFromChildren')
        var.put('sizeElementFromChildren', PyJs_sizeElementFromChildren_101_)
        @Js
        def PyJs_makeSpan_102_(classes, children, options, style, this, arguments, var=var):
            var = Scope({'classes':classes, 'children':children, 'options':options, 'style':style, 'this':this, 'arguments':arguments, 'makeSpan':PyJs_makeSpan_102_}, var)
            var.registers(['children', 'options', 'span', 'style', 'classes'])
            var.put('span', var.get('domTree_Span').create(var.get('classes'), var.get('children'), var.get('options'), var.get('style')))
            var.get('sizeElementFromChildren')(var.get('span'))
            return var.get('span')
        PyJs_makeSpan_102_._set_name('makeSpan')
        var.put('buildCommon_makeSpan', PyJs_makeSpan_102_)
        @Js
        def PyJs_makeSvgSpan_103_(classes, children, options, style, this, arguments, var=var):
            var = Scope({'classes':classes, 'children':children, 'options':options, 'style':style, 'this':this, 'arguments':arguments, 'makeSvgSpan':PyJs_makeSvgSpan_103_}, var)
            var.registers(['options', 'style', 'classes', 'children'])
            return var.get('domTree_Span').create(var.get('classes'), var.get('children'), var.get('options'), var.get('style'))
        PyJs_makeSvgSpan_103_._set_name('makeSvgSpan')
        var.put('buildCommon_makeSvgSpan', PyJs_makeSvgSpan_103_)
        @Js
        def PyJs_makeLineSpan_104_(className, options, thickness, this, arguments, var=var):
            var = Scope({'className':className, 'options':options, 'thickness':thickness, 'this':this, 'arguments':arguments, 'makeLineSpan':PyJs_makeLineSpan_104_}, var)
            var.registers(['options', 'line', 'className', 'thickness'])
            var.put('line', var.get('buildCommon_makeSpan')(Js([var.get('className')]), Js([]), var.get('options')))
            var.get('line').put('height', (var.get('thickness') or var.get('options').callprop('fontMetrics').get('defaultRuleThickness')))
            var.get('line').get('style').put('borderBottomWidth', (var.get('line').get('height')+Js('em')))
            var.get('line').put('maxFontSize', Js(1.0))
            return var.get('line')
        PyJs_makeLineSpan_104_._set_name('makeLineSpan')
        var.put('makeLineSpan', PyJs_makeLineSpan_104_)
        @Js
        def PyJs_makeAnchor_105_(href, classes, children, options, this, arguments, var=var):
            var = Scope({'href':href, 'classes':classes, 'children':children, 'options':options, 'this':this, 'arguments':arguments, 'makeAnchor':PyJs_makeAnchor_105_}, var)
            var.registers(['children', 'options', 'anchor', 'classes', 'href'])
            var.put('anchor', var.get('domTree_Anchor').create(var.get('href'), var.get('classes'), var.get('children'), var.get('options')))
            var.get('sizeElementFromChildren')(var.get('anchor'))
            return var.get('anchor')
        PyJs_makeAnchor_105_._set_name('makeAnchor')
        var.put('buildCommon_makeAnchor', PyJs_makeAnchor_105_)
        @Js
        def PyJs_makeFragment_106_(children, this, arguments, var=var):
            var = Scope({'children':children, 'this':this, 'arguments':arguments, 'makeFragment':PyJs_makeFragment_106_}, var)
            var.registers(['fragment', 'children'])
            var.put('fragment', var.get('tree_DocumentFragment').create(var.get('children')))
            var.get('sizeElementFromChildren')(var.get('fragment'))
            return var.get('fragment')
        PyJs_makeFragment_106_._set_name('makeFragment')
        var.put('buildCommon_makeFragment', PyJs_makeFragment_106_)
        @Js
        def PyJs_wrapFragment_107_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'wrapFragment':PyJs_wrapFragment_107_}, var)
            var.registers(['group', 'options'])
            if var.get('group').instanceof(var.get('tree_DocumentFragment')):
                return var.get('buildCommon_makeSpan')(Js([]), Js([var.get('group')]), var.get('options'))
            return var.get('group')
        PyJs_wrapFragment_107_._set_name('wrapFragment')
        var.put('buildCommon_wrapFragment', PyJs_wrapFragment_107_)
        @Js
        def PyJs_getVListChildrenAndDepth_108_(params, this, arguments, var=var):
            var = Scope({'params':params, 'this':this, 'arguments':arguments, 'getVListChildrenAndDepth':PyJs_getVListChildrenAndDepth_108_}, var)
            var.registers(['_depth', 'diff', 'children', 'oldChildren', 'i', 'size', 'params', 'depth', '_i', 'child', 'currPos', 'bottom', 'firstChild'])
            if PyJsStrictEq(var.get('params').get('positionType'),Js('individualShift')):
                var.put('oldChildren', var.get('params').get('children'))
                var.put('children', Js([var.get('oldChildren').get('0')]))
                var.put('_depth', ((-var.get('oldChildren').get('0').get('shift'))-var.get('oldChildren').get('0').get('elem').get('depth')))
                var.put('currPos', var.get('_depth'))
                #for JS loop
                var.put('i', Js(1.0))
                while (var.get('i')<var.get('oldChildren').get('length')):
                    try:
                        var.put('diff', (((-var.get('oldChildren').get(var.get('i')).get('shift'))-var.get('currPos'))-var.get('oldChildren').get(var.get('i')).get('elem').get('depth')))
                        var.put('size', (var.get('diff')-(var.get('oldChildren').get((var.get('i')-Js(1.0))).get('elem').get('height')+var.get('oldChildren').get((var.get('i')-Js(1.0))).get('elem').get('depth'))))
                        var.put('currPos', (var.get('currPos')+var.get('diff')))
                        var.get('children').callprop('push', Js({'type':Js('kern'),'size':var.get('size')}))
                        var.get('children').callprop('push', var.get('oldChildren').get(var.get('i')))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                return Js({'children':var.get('children'),'depth':var.get('_depth')})
            pass
            if PyJsStrictEq(var.get('params').get('positionType'),Js('top')):
                var.put('bottom', var.get('params').get('positionData'))
                #for JS loop
                var.put('_i', Js(0.0))
                while (var.get('_i')<var.get('params').get('children').get('length')):
                    try:
                        var.put('child', var.get('params').get('children').get(var.get('_i')))
                        var.put('bottom', (var.get('child').get('size') if PyJsStrictEq(var.get('child').get('type'),Js('kern')) else (var.get('child').get('elem').get('height')+var.get('child').get('elem').get('depth'))), '-')
                    finally:
                            (var.put('_i',Js(var.get('_i').to_number())+Js(1))-Js(1))
                var.put('depth', var.get('bottom'))
            else:
                if PyJsStrictEq(var.get('params').get('positionType'),Js('bottom')):
                    var.put('depth', (-var.get('params').get('positionData')))
                else:
                    var.put('firstChild', var.get('params').get('children').get('0'))
                    if PyJsStrictNeq(var.get('firstChild').get('type'),Js('elem')):
                        PyJsTempException = JsToPyException(var.get('Error').create(Js('First child must have type "elem".')))
                        raise PyJsTempException
                    if PyJsStrictEq(var.get('params').get('positionType'),Js('shift')):
                        var.put('depth', ((-var.get('firstChild').get('elem').get('depth'))-var.get('params').get('positionData')))
                    else:
                        if PyJsStrictEq(var.get('params').get('positionType'),Js('firstBaseline')):
                            var.put('depth', (-var.get('firstChild').get('elem').get('depth')))
                        else:
                            PyJsTempException = JsToPyException(var.get('Error').create(((Js('Invalid positionType ')+var.get('params').get('positionType'))+Js('.'))))
                            raise PyJsTempException
            return Js({'children':var.get('params').get('children'),'depth':var.get('depth')})
        PyJs_getVListChildrenAndDepth_108_._set_name('getVListChildrenAndDepth')
        var.put('getVListChildrenAndDepth', PyJs_getVListChildrenAndDepth_108_)
        @Js
        def PyJs_makeVList_109_(params, options, this, arguments, var=var):
            var = Scope({'params':params, 'options':options, 'this':this, 'arguments':arguments, 'makeVList':PyJs_makeVList_109_}, var)
            var.registers(['elem', 'emptySpan', 'childWrap', 'rows', 'realChildren', '_getVListChildrenAndD', 'i', 'params', 'minPos', 'options', 'depthStrut', '_elem', 'vlist', 'classes', 'topStrut', '_i2', 'child', 'vtable', '_child', 'children', 'maxPos', 'depth', 'currPos', 'pstrutSize', 'style', 'pstrut'])
            var.put('_getVListChildrenAndD', var.get('getVListChildrenAndDepth')(var.get('params')))
            var.put('children', var.get('_getVListChildrenAndD').get('children'))
            var.put('depth', var.get('_getVListChildrenAndD').get('depth'))
            var.put('pstrutSize', Js(0.0))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('children').get('length')):
                try:
                    var.put('child', var.get('children').get(var.get('i')))
                    if PyJsStrictEq(var.get('child').get('type'),Js('elem')):
                        var.put('elem', var.get('child').get('elem'))
                        var.put('pstrutSize', var.get('Math').callprop('max', var.get('pstrutSize'), var.get('elem').get('maxFontSize'), var.get('elem').get('height')))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('pstrutSize', Js(2.0), '+')
            var.put('pstrut', var.get('buildCommon_makeSpan')(Js([Js('pstrut')]), Js([])))
            var.get('pstrut').get('style').put('height', (var.get('pstrutSize')+Js('em')))
            var.put('realChildren', Js([]))
            var.put('minPos', var.get('depth'))
            var.put('maxPos', var.get('depth'))
            var.put('currPos', var.get('depth'))
            #for JS loop
            var.put('_i2', Js(0.0))
            while (var.get('_i2')<var.get('children').get('length')):
                try:
                    var.put('_child', var.get('children').get(var.get('_i2')))
                    if PyJsStrictEq(var.get('_child').get('type'),Js('kern')):
                        var.put('currPos', var.get('_child').get('size'), '+')
                    else:
                        var.put('_elem', var.get('_child').get('elem'))
                        var.put('classes', (var.get('_child').get('wrapperClasses') or Js([])))
                        var.put('style', (var.get('_child').get('wrapperStyle') or Js({})))
                        var.put('childWrap', var.get('buildCommon_makeSpan')(var.get('classes'), Js([var.get('pstrut'), var.get('_elem')]), var.get('undefined'), var.get('style')))
                        var.get('childWrap').get('style').put('top', ((((-var.get('pstrutSize'))-var.get('currPos'))-var.get('_elem').get('depth'))+Js('em')))
                        if var.get('_child').get('marginLeft'):
                            var.get('childWrap').get('style').put('marginLeft', var.get('_child').get('marginLeft'))
                        if var.get('_child').get('marginRight'):
                            var.get('childWrap').get('style').put('marginRight', var.get('_child').get('marginRight'))
                        var.get('realChildren').callprop('push', var.get('childWrap'))
                        var.put('currPos', (var.get('_elem').get('height')+var.get('_elem').get('depth')), '+')
                    var.put('minPos', var.get('Math').callprop('min', var.get('minPos'), var.get('currPos')))
                    var.put('maxPos', var.get('Math').callprop('max', var.get('maxPos'), var.get('currPos')))
                finally:
                        (var.put('_i2',Js(var.get('_i2').to_number())+Js(1))-Js(1))
            var.put('vlist', var.get('buildCommon_makeSpan')(Js([Js('vlist')]), var.get('realChildren')))
            var.get('vlist').get('style').put('height', (var.get('maxPos')+Js('em')))
            pass
            if (var.get('minPos')<Js(0.0)):
                var.put('emptySpan', var.get('buildCommon_makeSpan')(Js([]), Js([])))
                var.put('depthStrut', var.get('buildCommon_makeSpan')(Js([Js('vlist')]), Js([var.get('emptySpan')])))
                var.get('depthStrut').get('style').put('height', ((-var.get('minPos'))+Js('em')))
                var.put('topStrut', var.get('buildCommon_makeSpan')(Js([Js('vlist-s')]), Js([var.get('domTree_SymbolNode').create(Js('\u200b'))])))
                var.put('rows', Js([var.get('buildCommon_makeSpan')(Js([Js('vlist-r')]), Js([var.get('vlist'), var.get('topStrut')])), var.get('buildCommon_makeSpan')(Js([Js('vlist-r')]), Js([var.get('depthStrut')]))]))
            else:
                var.put('rows', Js([var.get('buildCommon_makeSpan')(Js([Js('vlist-r')]), Js([var.get('vlist')]))]))
            var.put('vtable', var.get('buildCommon_makeSpan')(Js([Js('vlist-t')]), var.get('rows')))
            if PyJsStrictEq(var.get('rows').get('length'),Js(2.0)):
                var.get('vtable').get('classes').callprop('push', Js('vlist-t2'))
            var.get('vtable').put('height', var.get('maxPos'))
            var.get('vtable').put('depth', (-var.get('minPos')))
            return var.get('vtable')
        PyJs_makeVList_109_._set_name('makeVList')
        var.put('buildCommon_makeVList', PyJs_makeVList_109_)
        @Js
        def PyJs_makeGlue_110_(measurement, options, this, arguments, var=var):
            var = Scope({'measurement':measurement, 'options':options, 'this':this, 'arguments':arguments, 'makeGlue':PyJs_makeGlue_110_}, var)
            var.registers(['measurement', 'options', 'size', 'rule'])
            var.put('rule', var.get('buildCommon_makeSpan')(Js([Js('mspace')]), Js([]), var.get('options')))
            var.put('size', var.get('units_calculateSize')(var.get('measurement'), var.get('options')))
            var.get('rule').get('style').put('marginRight', (var.get('size')+Js('em')))
            return var.get('rule')
        PyJs_makeGlue_110_._set_name('makeGlue')
        var.put('buildCommon_makeGlue', PyJs_makeGlue_110_)
        @Js
        def PyJs_retrieveTextFontName_111_(fontFamily, fontWeight, fontShape, this, arguments, var=var):
            var = Scope({'fontFamily':fontFamily, 'fontWeight':fontWeight, 'fontShape':fontShape, 'this':this, 'arguments':arguments, 'retrieveTextFontName':PyJs_retrieveTextFontName_111_}, var)
            var.registers(['fontShape', 'fontFamily', 'baseFontName', 'fontStylesName', 'fontWeight'])
            var.put('baseFontName', Js(''))
            while 1:
                SWITCHED = False
                CONDITION = (var.get('fontFamily'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js('amsrm')):
                    SWITCHED = True
                    var.put('baseFontName', Js('AMS'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('textrm')):
                    SWITCHED = True
                    var.put('baseFontName', Js('Main'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('textsf')):
                    SWITCHED = True
                    var.put('baseFontName', Js('SansSerif'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('texttt')):
                    SWITCHED = True
                    var.put('baseFontName', Js('Typewriter'))
                    break
                if True:
                    SWITCHED = True
                    var.put('baseFontName', var.get('fontFamily'))
                SWITCHED = True
                break
            pass
            if (PyJsStrictEq(var.get('fontWeight'),Js('textbf')) and PyJsStrictEq(var.get('fontShape'),Js('textit'))):
                var.put('fontStylesName', Js('BoldItalic'))
            else:
                if PyJsStrictEq(var.get('fontWeight'),Js('textbf')):
                    var.put('fontStylesName', Js('Bold'))
                else:
                    if PyJsStrictEq(var.get('fontWeight'),Js('textit')):
                        var.put('fontStylesName', Js('Italic'))
                    else:
                        var.put('fontStylesName', Js('Regular'))
            return ((var.get('baseFontName')+Js('-'))+var.get('fontStylesName'))
        PyJs_retrieveTextFontName_111_._set_name('retrieveTextFontName')
        var.put('retrieveTextFontName', PyJs_retrieveTextFontName_111_)
        var.put('fontMap', Js({'mathbf':Js({'variant':Js('bold'),'fontName':Js('Main-Bold')}),'mathrm':Js({'variant':Js('normal'),'fontName':Js('Main-Regular')}),'textit':Js({'variant':Js('italic'),'fontName':Js('Main-Italic')}),'mathit':Js({'variant':Js('italic'),'fontName':Js('Main-Italic')}),'mathbb':Js({'variant':Js('double-struck'),'fontName':Js('AMS-Regular')}),'mathcal':Js({'variant':Js('script'),'fontName':Js('Caligraphic-Regular')}),'mathfrak':Js({'variant':Js('fraktur'),'fontName':Js('Fraktur-Regular')}),'mathscr':Js({'variant':Js('script'),'fontName':Js('Script-Regular')}),'mathsf':Js({'variant':Js('sans-serif'),'fontName':Js('SansSerif-Regular')}),'mathtt':Js({'variant':Js('monospace'),'fontName':Js('Typewriter-Regular')})}))
        var.put('svgData', Js({'vec':Js([Js('vec'), Js(0.471), Js(0.714)]),'oiintSize1':Js([Js('oiintSize1'), Js(0.957), Js(0.499)]),'oiintSize2':Js([Js('oiintSize2'), Js(1.472), Js(0.659)]),'oiiintSize1':Js([Js('oiiintSize1'), Js(1.304), Js(0.499)]),'oiiintSize2':Js([Js('oiiintSize2'), Js(1.98), Js(0.659)])}))
        @Js
        def PyJs_staticSvg_112_(value, options, this, arguments, var=var):
            var = Scope({'value':value, 'options':options, 'this':this, 'arguments':arguments, 'staticSvg':PyJs_staticSvg_112_}, var)
            var.registers(['pathName', '_svgData$value', 'options', 'path', 'svgNode', 'width', 'span', 'height', 'value'])
            var.put('_svgData$value', var.get('svgData').get(var.get('value')))
            var.put('pathName', var.get('_svgData$value').get('0'))
            var.put('width', var.get('_svgData$value').get('1'))
            var.put('height', var.get('_svgData$value').get('2'))
            var.put('path', var.get('domTree_PathNode').create(var.get('pathName')))
            var.put('svgNode', var.get('SvgNode').create(Js([var.get('path')]), Js({'width':(var.get('width')+Js('em')),'height':(var.get('height')+Js('em')),'style':((Js('width:')+var.get('width'))+Js('em')),'viewBox':(((Js('0 0 ')+(Js(1000.0)*var.get('width')))+Js(' '))+(Js(1000.0)*var.get('height'))),'preserveAspectRatio':Js('xMinYMin')})))
            var.put('span', var.get('buildCommon_makeSvgSpan')(Js([Js('overlay')]), Js([var.get('svgNode')]), var.get('options')))
            var.get('span').put('height', var.get('height'))
            var.get('span').get('style').put('height', (var.get('height')+Js('em')))
            var.get('span').get('style').put('width', (var.get('width')+Js('em')))
            return var.get('span')
        PyJs_staticSvg_112_._set_name('staticSvg')
        var.put('buildCommon_staticSvg', PyJs_staticSvg_112_)
        var.put('buildCommon', Js({'fontMap':var.get('fontMap'),'makeSymbol':var.get('buildCommon_makeSymbol'),'mathsym':var.get('buildCommon_mathsym'),'makeSpan':var.get('buildCommon_makeSpan'),'makeSvgSpan':var.get('buildCommon_makeSvgSpan'),'makeLineSpan':var.get('makeLineSpan'),'makeAnchor':var.get('buildCommon_makeAnchor'),'makeFragment':var.get('buildCommon_makeFragment'),'wrapFragment':var.get('buildCommon_wrapFragment'),'makeVList':var.get('buildCommon_makeVList'),'makeOrd':var.get('buildCommon_makeOrd'),'makeGlue':var.get('buildCommon_makeGlue'),'staticSvg':var.get('buildCommon_staticSvg'),'svgData':var.get('svgData'),'tryCombineChars':var.get('buildCommon_tryCombineChars')}))
        pass
        pass
        pass
        pass
        pass
        pass
        var.put('thinspace', Js({'number':Js(3.0),'unit':Js('mu')}))
        var.put('mediumspace', Js({'number':Js(4.0),'unit':Js('mu')}))
        var.put('thickspace', Js({'number':Js(5.0),'unit':Js('mu')}))
        var.put('spacings', Js({'mord':Js({'mop':var.get('thinspace'),'mbin':var.get('mediumspace'),'mrel':var.get('thickspace'),'minner':var.get('thinspace')}),'mop':Js({'mord':var.get('thinspace'),'mop':var.get('thinspace'),'mrel':var.get('thickspace'),'minner':var.get('thinspace')}),'mbin':Js({'mord':var.get('mediumspace'),'mop':var.get('mediumspace'),'mopen':var.get('mediumspace'),'minner':var.get('mediumspace')}),'mrel':Js({'mord':var.get('thickspace'),'mop':var.get('thickspace'),'mopen':var.get('thickspace'),'minner':var.get('thickspace')}),'mopen':Js({}),'mclose':Js({'mop':var.get('thinspace'),'mbin':var.get('mediumspace'),'mrel':var.get('thickspace'),'minner':var.get('thinspace')}),'mpunct':Js({'mord':var.get('thinspace'),'mop':var.get('thinspace'),'mrel':var.get('thickspace'),'mopen':var.get('thinspace'),'mclose':var.get('thinspace'),'mpunct':var.get('thinspace'),'minner':var.get('thinspace')}),'minner':Js({'mord':var.get('thinspace'),'mop':var.get('thinspace'),'mbin':var.get('mediumspace'),'mrel':var.get('thickspace'),'mopen':var.get('thinspace'),'mpunct':var.get('thinspace'),'minner':var.get('thinspace')})}))
        var.put('tightSpacings', Js({'mord':Js({'mop':var.get('thinspace')}),'mop':Js({'mord':var.get('thinspace'),'mop':var.get('thinspace')}),'mbin':Js({}),'mrel':Js({}),'mopen':Js({}),'mclose':Js({'mop':var.get('thinspace')}),'mpunct':Js({}),'minner':Js({'mop':var.get('thinspace')})}))
        var.put('_functions', Js({}))
        var.put('_htmlGroupBuilders', Js({}))
        var.put('_mathmlGroupBuilders', Js({}))
        pass
        pass
        @Js
        def PyJs_ordargument_114_(arg, this, arguments, var=var):
            var = Scope({'arg':arg, 'this':this, 'arguments':arguments, 'ordargument':PyJs_ordargument_114_}, var)
            var.registers(['node', 'arg'])
            var.put('node', var.get('checkNodeType')(var.get('arg'), Js('ordgroup')))
            return (var.get('node').get('body') if var.get('node') else Js([var.get('arg')]))
        PyJs_ordargument_114_._set_name('ordargument')
        var.put('defineFunction_ordargument', PyJs_ordargument_114_)
        var.put('buildHTML_makeSpan', var.get('buildCommon').get('makeSpan'))
        var.put('binLeftCanceller', Js([Js('leftmost'), Js('mbin'), Js('mopen'), Js('mrel'), Js('mop'), Js('mpunct')]))
        var.put('binRightCanceller', Js([Js('rightmost'), Js('mrel'), Js('mclose'), Js('mpunct')]))
        var.put('buildHTML_styleMap', Js({'display':var.get('src_Style').get('DISPLAY'),'text':var.get('src_Style').get('TEXT'),'script':var.get('src_Style').get('SCRIPT'),'scriptscript':var.get('src_Style').get('SCRIPTSCRIPT')}))
        var.put('DomEnum', Js({'mord':Js('mord'),'mop':Js('mop'),'mbin':Js('mbin'),'mrel':Js('mrel'),'mopen':Js('mopen'),'mclose':Js('mclose'),'mpunct':Js('mpunct'),'minner':Js('minner')}))
        @Js
        def PyJs_buildExpression_115_(expression, options, isRealGroup, surrounding, this, arguments, var=var):
            var = Scope({'expression':expression, 'options':options, 'isRealGroup':isRealGroup, 'surrounding':surrounding, 'this':this, 'arguments':arguments, 'buildExpression':PyJs_buildExpression_115_}, var)
            var.registers(['glueOptions', 'i', 'children', 'expression', 'surrounding', 'options', 'dummyPrev', 'node', 'groups', 'isRealGroup', 'dummyNext', 'output'])
            if PyJsStrictEq(var.get('surrounding'),PyJsComma(Js(0.0), Js(None))):
                var.put('surrounding', Js([var.get(u"null"), var.get(u"null")]))
            var.put('groups', Js([]))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('expression').get('length')):
                try:
                    var.put('output', var.get('buildHTML_buildGroup')(var.get('expression').get(var.get('i')), var.get('options')))
                    if var.get('output').instanceof(var.get('tree_DocumentFragment')):
                        var.put('children', var.get('output').get('children'))
                        var.get('groups').get('push').callprop('apply', var.get('groups'), var.get('children'))
                    else:
                        var.get('groups').callprop('push', var.get('output'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            if var.get('isRealGroup').neg():
                return var.get('groups')
            var.put('glueOptions', var.get('options'))
            if PyJsStrictEq(var.get('expression').get('length'),Js(1.0)):
                var.put('node', (var.get('checkNodeType')(var.get('expression').get('0'), Js('sizing')) or var.get('checkNodeType')(var.get('expression').get('0'), Js('styling'))))
                if var.get('node').neg():
                    pass
                else:
                    if PyJsStrictEq(var.get('node').get('type'),Js('sizing')):
                        var.put('glueOptions', var.get('options').callprop('havingSize', var.get('node').get('size')))
                    else:
                        if PyJsStrictEq(var.get('node').get('type'),Js('styling')):
                            var.put('glueOptions', var.get('options').callprop('havingStyle', var.get('buildHTML_styleMap').get(var.get('node').get('style'))))
            var.put('dummyPrev', var.get('buildHTML_makeSpan')(Js([(var.get('surrounding').get('0') or Js('leftmost'))]), Js([]), var.get('options')))
            var.put('dummyNext', var.get('buildHTML_makeSpan')(Js([(var.get('surrounding').get('1') or Js('rightmost'))]), Js([]), var.get('options')))
            @Js
            def PyJs_anonymous_116_(node, prev, this, arguments, var=var):
                var = Scope({'node':node, 'prev':prev, 'this':this, 'arguments':arguments}, var)
                var.registers(['node', 'prevType', 'type', 'prev'])
                var.put('prevType', var.get('prev').get('classes').get('0'))
                var.put('type', var.get('node').get('classes').get('0'))
                if (PyJsStrictEq(var.get('prevType'),Js('mbin')) and var.get('utils').callprop('contains', var.get('binRightCanceller'), var.get('type'))):
                    var.get('prev').get('classes').put('0', Js('mord'))
                else:
                    if (PyJsStrictEq(var.get('type'),Js('mbin')) and var.get('utils').callprop('contains', var.get('binLeftCanceller'), var.get('prevType'))):
                        var.get('node').get('classes').put('0', Js('mord'))
            PyJs_anonymous_116_._set_name('anonymous')
            var.get('traverseNonSpaceNodes')(var.get('groups'), PyJs_anonymous_116_, Js({'node':var.get('dummyPrev')}), var.get('dummyNext'))
            @Js
            def PyJs_anonymous_117_(node, prev, this, arguments, var=var):
                var = Scope({'node':node, 'prev':prev, 'this':this, 'arguments':arguments}, var)
                var.registers(['type', 'prev', 'node', 'prevType', 'space'])
                var.put('prevType', var.get('getTypeOfDomTree')(var.get('prev')))
                var.put('type', var.get('getTypeOfDomTree')(var.get('node')))
                var.put('space', ((var.get('tightSpacings').get(var.get('prevType')).get(var.get('type')) if var.get('node').callprop('hasClass', Js('mtight')) else var.get('spacings').get(var.get('prevType')).get(var.get('type'))) if (var.get('prevType') and var.get('type')) else var.get(u"null")))
                if var.get('space'):
                    return var.get('buildCommon').callprop('makeGlue', var.get('space'), var.get('glueOptions'))
            PyJs_anonymous_117_._set_name('anonymous')
            var.get('traverseNonSpaceNodes')(var.get('groups'), PyJs_anonymous_117_, Js({'node':var.get('dummyPrev')}), var.get('dummyNext'))
            return var.get('groups')
        PyJs_buildExpression_115_._set_name('buildExpression')
        var.put('buildHTML_buildExpression', PyJs_buildExpression_115_)
        @Js
        def PyJs_traverseNonSpaceNodes_118_(nodes, callback, prev, next, this, arguments, var=var):
            var = Scope({'nodes':nodes, 'callback':callback, 'prev':prev, 'next':next, 'this':this, 'arguments':arguments, 'traverseNonSpaceNodes':PyJs_traverseNonSpaceNodes_118_}, var)
            var.registers(['i', 'prev', 'callback', 'next', 'node', 'result', 'nodes', 'partialGroup'])
            if var.get('next'):
                var.get('nodes').callprop('push', var.get('next'))
            var.put('i', Js(0.0))
            #for JS loop
            
            while (var.get('i')<var.get('nodes').get('length')):
                try:
                    var.put('node', var.get('nodes').get(var.get('i')))
                    var.put('partialGroup', var.get('buildHTML_checkPartialGroup')(var.get('node')))
                    if var.get('partialGroup'):
                        var.get('traverseNonSpaceNodes')(var.get('partialGroup').get('children'), var.get('callback'), var.get('prev'))
                        continue
                    if PyJsStrictEq(var.get('node').get('classes').get('0'),Js('mspace')):
                        continue
                    var.put('result', var.get('callback')(var.get('node'), var.get('prev').get('node')))
                    if var.get('result'):
                        if var.get('prev').get('insertAfter'):
                            var.get('prev').callprop('insertAfter', var.get('result'))
                        else:
                            var.get('nodes').callprop('unshift', var.get('result'))
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                    var.get('prev').put('node', var.get('node'))
                    @Js
                    def PyJs_anonymous_119_(index, this, arguments, var=var):
                        var = Scope({'index':index, 'this':this, 'arguments':arguments}, var)
                        var.registers(['index'])
                        @Js
                        def PyJs_anonymous_120_(n, this, arguments, var=var):
                            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
                            var.registers(['n'])
                            var.get('nodes').callprop('splice', (var.get('index')+Js(1.0)), Js(0.0), var.get('n'))
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                        PyJs_anonymous_120_._set_name('anonymous')
                        return PyJs_anonymous_120_
                    PyJs_anonymous_119_._set_name('anonymous')
                    var.get('prev').put('insertAfter', PyJs_anonymous_119_(var.get('i')))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            if var.get('next'):
                var.get('nodes').callprop('pop')
        PyJs_traverseNonSpaceNodes_118_._set_name('traverseNonSpaceNodes')
        var.put('traverseNonSpaceNodes', PyJs_traverseNonSpaceNodes_118_)
        @Js
        def PyJs_checkPartialGroup_121_(node, this, arguments, var=var):
            var = Scope({'node':node, 'this':this, 'arguments':arguments, 'checkPartialGroup':PyJs_checkPartialGroup_121_}, var)
            var.registers(['node'])
            if (var.get('node').instanceof(var.get('tree_DocumentFragment')) or var.get('node').instanceof(var.get('domTree_Anchor'))):
                return var.get('node')
            return var.get(u"null")
        PyJs_checkPartialGroup_121_._set_name('checkPartialGroup')
        var.put('buildHTML_checkPartialGroup', PyJs_checkPartialGroup_121_)
        @Js
        def PyJs_getOutermostNode_122_(node, side, this, arguments, var=var):
            var = Scope({'node':node, 'side':side, 'this':this, 'arguments':arguments, 'getOutermostNode':PyJs_getOutermostNode_122_}, var)
            var.registers(['node', 'children', 'side', 'partialGroup'])
            var.put('partialGroup', var.get('buildHTML_checkPartialGroup')(var.get('node')))
            if var.get('partialGroup'):
                var.put('children', var.get('partialGroup').get('children'))
                if var.get('children').get('length'):
                    if PyJsStrictEq(var.get('side'),Js('right')):
                        return var.get('getOutermostNode')(var.get('children').get((var.get('children').get('length')-Js(1.0))), Js('right'))
                    else:
                        if PyJsStrictEq(var.get('side'),Js('left')):
                            return var.get('getOutermostNode')(var.get('children').get('0'), Js('left'))
            return var.get('node')
        PyJs_getOutermostNode_122_._set_name('getOutermostNode')
        var.put('getOutermostNode', PyJs_getOutermostNode_122_)
        @Js
        def PyJs_getTypeOfDomTree_123_(node, side, this, arguments, var=var):
            var = Scope({'node':node, 'side':side, 'this':this, 'arguments':arguments, 'getTypeOfDomTree':PyJs_getTypeOfDomTree_123_}, var)
            var.registers(['node', 'side'])
            if var.get('node').neg():
                return var.get(u"null")
            if var.get('side'):
                var.put('node', var.get('getOutermostNode')(var.get('node'), var.get('side')))
            return (var.get('DomEnum').get(var.get('node').get('classes').get('0')) or var.get(u"null"))
        PyJs_getTypeOfDomTree_123_._set_name('getTypeOfDomTree')
        var.put('getTypeOfDomTree', PyJs_getTypeOfDomTree_123_)
        @Js
        def PyJs_makeNullDelimiter_124_(options, classes, this, arguments, var=var):
            var = Scope({'options':options, 'classes':classes, 'this':this, 'arguments':arguments, 'makeNullDelimiter':PyJs_makeNullDelimiter_124_}, var)
            var.registers(['moreClasses', 'options', 'classes'])
            var.put('moreClasses', Js([Js('nulldelimiter')]).callprop('concat', var.get('options').callprop('baseSizingClasses')))
            return var.get('buildHTML_makeSpan')(var.get('classes').callprop('concat', var.get('moreClasses')))
        PyJs_makeNullDelimiter_124_._set_name('makeNullDelimiter')
        var.put('makeNullDelimiter', PyJs_makeNullDelimiter_124_)
        @Js
        def PyJs_buildGroup_125_(group, options, baseOptions, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'baseOptions':baseOptions, 'this':this, 'arguments':arguments, 'buildGroup':PyJs_buildGroup_125_}, var)
            var.registers(['group', 'options', 'baseOptions', 'groupNode', 'multiplier'])
            if var.get('group').neg():
                return var.get('buildHTML_makeSpan')()
            if var.get('_htmlGroupBuilders').get(var.get('group').get('type')):
                var.put('groupNode', var.get('_htmlGroupBuilders').callprop(var.get('group').get('type'), var.get('group'), var.get('options')))
                if (var.get('baseOptions') and PyJsStrictNeq(var.get('options').get('size'),var.get('baseOptions').get('size'))):
                    var.put('groupNode', var.get('buildHTML_makeSpan')(var.get('options').callprop('sizingClasses', var.get('baseOptions')), Js([var.get('groupNode')]), var.get('options')))
                    var.put('multiplier', (var.get('options').get('sizeMultiplier')/var.get('baseOptions').get('sizeMultiplier')))
                    var.get('groupNode').put('height', var.get('multiplier'), '*')
                    var.get('groupNode').put('depth', var.get('multiplier'), '*')
                return var.get('groupNode')
            else:
                PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js("Got group of unknown type: '")+var.get('group').get('type'))+Js("'"))))
                raise PyJsTempException
        PyJs_buildGroup_125_._set_name('buildGroup')
        var.put('buildHTML_buildGroup', PyJs_buildGroup_125_)
        pass
        pass
        pass
        @Js
        def PyJs_anonymous_126_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['_proto', 'MathNode'])
            @Js
            def PyJsHoisted_MathNode_(type, children, this, arguments, var=var):
                var = Scope({'type':type, 'children':children, 'this':this, 'arguments':arguments}, var)
                var.registers(['children', 'type'])
                var.get(u"this").put('type', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('attributes', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('children', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('type', var.get('type'))
                var.get(u"this").put('attributes', Js({}))
                var.get(u"this").put('children', (var.get('children') or Js([])))
            PyJsHoisted_MathNode_.func_name = 'MathNode'
            var.put('MathNode', PyJsHoisted_MathNode_)
            pass
            var.put('_proto', var.get('MathNode').get('prototype'))
            @Js
            def PyJs_setAttribute_127_(name, value, this, arguments, var=var):
                var = Scope({'name':name, 'value':value, 'this':this, 'arguments':arguments, 'setAttribute':PyJs_setAttribute_127_}, var)
                var.registers(['name', 'value'])
                var.get(u"this").get('attributes').put(var.get('name'), var.get('value'))
            PyJs_setAttribute_127_._set_name('setAttribute')
            var.get('_proto').put('setAttribute', PyJs_setAttribute_127_)
            @Js
            def PyJs_getAttribute_128_(name, this, arguments, var=var):
                var = Scope({'name':name, 'this':this, 'arguments':arguments, 'getAttribute':PyJs_getAttribute_128_}, var)
                var.registers(['name'])
                return var.get(u"this").get('attributes').get(var.get('name'))
            PyJs_getAttribute_128_._set_name('getAttribute')
            var.get('_proto').put('getAttribute', PyJs_getAttribute_128_)
            @Js
            def PyJs_toNode_129_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toNode':PyJs_toNode_129_}, var)
                var.registers(['node', 'i', 'attr'])
                var.put('node', var.get('document').callprop('createElementNS', Js('http://www.w3.org/1998/Math/MathML'), var.get(u"this").get('type')))
                for PyJsTemp in var.get(u"this").get('attributes'):
                    var.put('attr', PyJsTemp)
                    if var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get(u"this").get('attributes'), var.get('attr')):
                        var.get('node').callprop('setAttribute', var.get('attr'), var.get(u"this").get('attributes').get(var.get('attr')))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get(u"this").get('children').get('length')):
                    try:
                        var.get('node').callprop('appendChild', var.get(u"this").get('children').get(var.get('i')).callprop('toNode'))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                return var.get('node')
            PyJs_toNode_129_._set_name('toNode')
            var.get('_proto').put('toNode', PyJs_toNode_129_)
            @Js
            def PyJs_toMarkup_130_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toMarkup':PyJs_toMarkup_130_}, var)
                var.registers(['attr', 'i', 'markup'])
                var.put('markup', (Js('<')+var.get(u"this").get('type')))
                for PyJsTemp in var.get(u"this").get('attributes'):
                    var.put('attr', PyJsTemp)
                    if var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get(u"this").get('attributes'), var.get('attr')):
                        var.put('markup', ((Js(' ')+var.get('attr'))+Js('="')), '+')
                        var.put('markup', var.get('utils').callprop('escape', var.get(u"this").get('attributes').get(var.get('attr'))), '+')
                        var.put('markup', Js('"'), '+')
                var.put('markup', Js('>'), '+')
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get(u"this").get('children').get('length')):
                    try:
                        var.put('markup', var.get(u"this").get('children').get(var.get('i')).callprop('toMarkup'), '+')
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                var.put('markup', ((Js('</')+var.get(u"this").get('type'))+Js('>')), '+')
                return var.get('markup')
            PyJs_toMarkup_130_._set_name('toMarkup')
            var.get('_proto').put('toMarkup', PyJs_toMarkup_130_)
            @Js
            def PyJs_toText_131_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toText':PyJs_toText_131_}, var)
                var.registers([])
                @Js
                def PyJs_anonymous_132_(child, this, arguments, var=var):
                    var = Scope({'child':child, 'this':this, 'arguments':arguments}, var)
                    var.registers(['child'])
                    return var.get('child').callprop('toText')
                PyJs_anonymous_132_._set_name('anonymous')
                return var.get(u"this").get('children').callprop('map', PyJs_anonymous_132_).callprop('join', Js(''))
            PyJs_toText_131_._set_name('toText')
            var.get('_proto').put('toText', PyJs_toText_131_)
            return var.get('MathNode')
        PyJs_anonymous_126_._set_name('anonymous')
        var.put('mathMLTree_MathNode', PyJs_anonymous_126_())
        @Js
        def PyJs_anonymous_133_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['_proto2', 'TextNode'])
            @Js
            def PyJsHoisted_TextNode_(text, this, arguments, var=var):
                var = Scope({'text':text, 'this':this, 'arguments':arguments}, var)
                var.registers(['text'])
                var.get(u"this").put('text', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('text', var.get('text'))
            PyJsHoisted_TextNode_.func_name = 'TextNode'
            var.put('TextNode', PyJsHoisted_TextNode_)
            pass
            var.put('_proto2', var.get('TextNode').get('prototype'))
            @Js
            def PyJs_toNode_134_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toNode':PyJs_toNode_134_}, var)
                var.registers([])
                return var.get('document').callprop('createTextNode', var.get(u"this").get('text'))
            PyJs_toNode_134_._set_name('toNode')
            var.get('_proto2').put('toNode', PyJs_toNode_134_)
            @Js
            def PyJs_toMarkup_135_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toMarkup':PyJs_toMarkup_135_}, var)
                var.registers([])
                return var.get('utils').callprop('escape', var.get(u"this").callprop('toText'))
            PyJs_toMarkup_135_._set_name('toMarkup')
            var.get('_proto2').put('toMarkup', PyJs_toMarkup_135_)
            @Js
            def PyJs_toText_136_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toText':PyJs_toText_136_}, var)
                var.registers([])
                return var.get(u"this").get('text')
            PyJs_toText_136_._set_name('toText')
            var.get('_proto2').put('toText', PyJs_toText_136_)
            return var.get('TextNode')
        PyJs_anonymous_133_._set_name('anonymous')
        var.put('mathMLTree_TextNode', PyJs_anonymous_133_())
        @Js
        def PyJs_anonymous_137_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['SpaceNode', '_proto3'])
            @Js
            def PyJsHoisted_SpaceNode_(width, this, arguments, var=var):
                var = Scope({'width':width, 'this':this, 'arguments':arguments}, var)
                var.registers(['width'])
                var.get(u"this").put('width', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('character', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('width', var.get('width'))
                if ((var.get('width')>=Js(0.05555)) and (var.get('width')<=Js(0.05556))):
                    var.get(u"this").put('character', Js('\u200a'))
                else:
                    if ((var.get('width')>=Js(0.1666)) and (var.get('width')<=Js(0.1667))):
                        var.get(u"this").put('character', Js('\u2009'))
                    else:
                        if ((var.get('width')>=Js(0.2222)) and (var.get('width')<=Js(0.2223))):
                            var.get(u"this").put('character', Js('\u2005'))
                        else:
                            if ((var.get('width')>=Js(0.2777)) and (var.get('width')<=Js(0.2778))):
                                var.get(u"this").put('character', Js('\u2005\u200a'))
                            else:
                                if ((var.get('width')>=(-Js(0.05556))) and (var.get('width')<=(-Js(0.05555)))):
                                    var.get(u"this").put('character', Js('\u200a\u2063'))
                                else:
                                    if ((var.get('width')>=(-Js(0.1667))) and (var.get('width')<=(-Js(0.1666)))):
                                        var.get(u"this").put('character', Js('\u2009\u2063'))
                                    else:
                                        if ((var.get('width')>=(-Js(0.2223))) and (var.get('width')<=(-Js(0.2222)))):
                                            var.get(u"this").put('character', Js('\u205f\u2063'))
                                        else:
                                            if ((var.get('width')>=(-Js(0.2778))) and (var.get('width')<=(-Js(0.2777)))):
                                                var.get(u"this").put('character', Js('\u2005\u2063'))
                                            else:
                                                var.get(u"this").put('character', var.get(u"null"))
            PyJsHoisted_SpaceNode_.func_name = 'SpaceNode'
            var.put('SpaceNode', PyJsHoisted_SpaceNode_)
            pass
            var.put('_proto3', var.get('SpaceNode').get('prototype'))
            @Js
            def PyJs_toNode_138_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toNode':PyJs_toNode_138_}, var)
                var.registers(['node'])
                if var.get(u"this").get('character'):
                    return var.get('document').callprop('createTextNode', var.get(u"this").get('character'))
                else:
                    var.put('node', var.get('document').callprop('createElementNS', Js('http://www.w3.org/1998/Math/MathML'), Js('mspace')))
                    var.get('node').callprop('setAttribute', Js('width'), (var.get(u"this").get('width')+Js('em')))
                    return var.get('node')
            PyJs_toNode_138_._set_name('toNode')
            var.get('_proto3').put('toNode', PyJs_toNode_138_)
            @Js
            def PyJs_toMarkup_139_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toMarkup':PyJs_toMarkup_139_}, var)
                var.registers([])
                if var.get(u"this").get('character'):
                    return ((Js('<mtext>')+var.get(u"this").get('character'))+Js('</mtext>'))
                else:
                    return ((Js('<mspace width="')+var.get(u"this").get('width'))+Js('em"/>'))
            PyJs_toMarkup_139_._set_name('toMarkup')
            var.get('_proto3').put('toMarkup', PyJs_toMarkup_139_)
            @Js
            def PyJs_toText_140_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'toText':PyJs_toText_140_}, var)
                var.registers([])
                if var.get(u"this").get('character'):
                    return var.get(u"this").get('character')
                else:
                    return Js(' ')
            PyJs_toText_140_._set_name('toText')
            var.get('_proto3').put('toText', PyJs_toText_140_)
            return var.get('SpaceNode')
        PyJs_anonymous_137_._set_name('anonymous')
        var.put('SpaceNode', PyJs_anonymous_137_())
        var.put('mathMLTree', Js({'MathNode':var.get('mathMLTree_MathNode'),'TextNode':var.get('mathMLTree_TextNode'),'SpaceNode':var.get('SpaceNode'),'newDocumentFragment':var.get('newDocumentFragment')}))
        @Js
        def PyJs_makeText_141_(text, mode, options, this, arguments, var=var):
            var = Scope({'text':text, 'mode':mode, 'options':options, 'this':this, 'arguments':arguments, 'makeText':PyJs_makeText_141_}, var)
            var.registers(['options', 'text', 'mode'])
            def PyJs_LONG_142_(var=var):
                return (((var.get('src_symbols').get(var.get('mode')).get(var.get('text')) and var.get('src_symbols').get(var.get('mode')).get(var.get('text')).get('replace')) and PyJsStrictNeq(var.get('text').callprop('charCodeAt', Js(0.0)),Js(55349))) and ((var.get('ligatures').callprop('hasOwnProperty', var.get('text')) and var.get('options')) and ((var.get('options').get('fontFamily') and PyJsStrictEq(var.get('options').get('fontFamily').callprop('substr', Js(4.0), Js(2.0)),Js('tt'))) or (var.get('options').get('font') and PyJsStrictEq(var.get('options').get('font').callprop('substr', Js(4.0), Js(2.0)),Js('tt'))))).neg())
            if PyJs_LONG_142_():
                var.put('text', var.get('src_symbols').get(var.get('mode')).get(var.get('text')).get('replace'))
            return var.get('mathMLTree').get('TextNode').create(var.get('text'))
        PyJs_makeText_141_._set_name('makeText')
        var.put('buildMathML_makeText', PyJs_makeText_141_)
        @Js
        def PyJs_makeRow_143_(body, this, arguments, var=var):
            var = Scope({'body':body, 'this':this, 'arguments':arguments, 'makeRow':PyJs_makeRow_143_}, var)
            var.registers(['body'])
            if PyJsStrictEq(var.get('body').get('length'),Js(1.0)):
                return var.get('body').get('0')
            else:
                return var.get('mathMLTree').get('MathNode').create(Js('mrow'), var.get('body'))
        PyJs_makeRow_143_._set_name('makeRow')
        var.put('buildMathML_makeRow', PyJs_makeRow_143_)
        @Js
        def PyJs_getVariant_144_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'getVariant':PyJs_getVariant_144_}, var)
            var.registers(['fontName', 'mode', 'font', 'group', 'options', 'text'])
            if PyJsStrictEq(var.get('options').get('fontFamily'),Js('texttt')):
                return Js('monospace')
            else:
                if PyJsStrictEq(var.get('options').get('fontFamily'),Js('textsf')):
                    if (PyJsStrictEq(var.get('options').get('fontShape'),Js('textit')) and PyJsStrictEq(var.get('options').get('fontWeight'),Js('textbf'))):
                        return Js('sans-serif-bold-italic')
                    else:
                        if PyJsStrictEq(var.get('options').get('fontShape'),Js('textit')):
                            return Js('sans-serif-italic')
                        else:
                            if PyJsStrictEq(var.get('options').get('fontWeight'),Js('textbf')):
                                return Js('bold-sans-serif')
                            else:
                                return Js('sans-serif')
                else:
                    if (PyJsStrictEq(var.get('options').get('fontShape'),Js('textit')) and PyJsStrictEq(var.get('options').get('fontWeight'),Js('textbf'))):
                        return Js('bold-italic')
                    else:
                        if PyJsStrictEq(var.get('options').get('fontShape'),Js('textit')):
                            return Js('italic')
                        else:
                            if PyJsStrictEq(var.get('options').get('fontWeight'),Js('textbf')):
                                return Js('bold')
            var.put('font', var.get('options').get('font'))
            if (var.get('font').neg() or PyJsStrictEq(var.get('font'),Js('mathnormal'))):
                return var.get(u"null")
            var.put('mode', var.get('group').get('mode'))
            if PyJsStrictEq(var.get('font'),Js('mathit')):
                return Js('italic')
            else:
                if PyJsStrictEq(var.get('font'),Js('boldsymbol')):
                    return Js('bold-italic')
            var.put('text', var.get('group').get('text'))
            if var.get('utils').callprop('contains', Js([Js('\\imath'), Js('\\jmath')]), var.get('text')):
                return var.get(u"null")
            if (var.get('src_symbols').get(var.get('mode')).get(var.get('text')) and var.get('src_symbols').get(var.get('mode')).get(var.get('text')).get('replace')):
                var.put('text', var.get('src_symbols').get(var.get('mode')).get(var.get('text')).get('replace'))
            var.put('fontName', var.get('buildCommon').get('fontMap').get(var.get('font')).get('fontName'))
            if var.get('getCharacterMetrics')(var.get('text'), var.get('fontName'), var.get('mode')):
                return var.get('buildCommon').get('fontMap').get(var.get('font')).get('variant')
            return var.get(u"null")
        PyJs_getVariant_144_._set_name('getVariant')
        var.put('buildMathML_getVariant', PyJs_getVariant_144_)
        @Js
        def PyJs_buildExpression_145_(expression, options, this, arguments, var=var):
            var = Scope({'expression':expression, 'options':options, 'this':this, 'arguments':arguments, 'buildExpression':PyJs_buildExpression_145_}, var)
            var.registers(['_lastGroup$children', 'i', '_lastGroup$children2', '_child', 'expression', 'group', 'options', 'child', 'lastChild', 'lastGroup', '_lastGroup$children3', 'groups'])
            var.put('groups', Js([]))
            pass
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('expression').get('length')):
                try:
                    var.put('group', var.get('buildMathML_buildGroup')(var.get('expression').get(var.get('i')), var.get('options')))
                    if (var.get('group').instanceof(var.get('mathMLTree_MathNode')) and var.get('lastGroup').instanceof(var.get('mathMLTree_MathNode'))):
                        if ((PyJsStrictEq(var.get('group').get('type'),Js('mtext')) and PyJsStrictEq(var.get('lastGroup').get('type'),Js('mtext'))) and PyJsStrictEq(var.get('group').callprop('getAttribute', Js('mathvariant')),var.get('lastGroup').callprop('getAttribute', Js('mathvariant')))):
                            pass
                            var.put('_lastGroup$children', var.get('lastGroup').get('children')).get('push').callprop('apply', var.get('_lastGroup$children'), var.get('group').get('children'))
                            continue
                        else:
                            if (PyJsStrictEq(var.get('group').get('type'),Js('mn')) and PyJsStrictEq(var.get('lastGroup').get('type'),Js('mn'))):
                                pass
                                var.put('_lastGroup$children2', var.get('lastGroup').get('children')).get('push').callprop('apply', var.get('_lastGroup$children2'), var.get('group').get('children'))
                                continue
                            else:
                                if ((PyJsStrictEq(var.get('group').get('type'),Js('mi')) and PyJsStrictEq(var.get('group').get('children').get('length'),Js(1.0))) and PyJsStrictEq(var.get('lastGroup').get('type'),Js('mn'))):
                                    var.put('child', var.get('group').get('children').get('0'))
                                    if (var.get('child').instanceof(var.get('mathMLTree_TextNode')) and PyJsStrictEq(var.get('child').get('text'),Js('.'))):
                                        pass
                                        var.put('_lastGroup$children3', var.get('lastGroup').get('children')).get('push').callprop('apply', var.get('_lastGroup$children3'), var.get('group').get('children'))
                                        continue
                                else:
                                    if (PyJsStrictEq(var.get('lastGroup').get('type'),Js('mi')) and PyJsStrictEq(var.get('lastGroup').get('children').get('length'),Js(1.0))):
                                        var.put('lastChild', var.get('lastGroup').get('children').get('0'))
                                        if ((var.get('lastChild').instanceof(var.get('mathMLTree_TextNode')) and PyJsStrictEq(var.get('lastChild').get('text'),Js('̸'))) and ((PyJsStrictEq(var.get('group').get('type'),Js('mo')) or PyJsStrictEq(var.get('group').get('type'),Js('mi'))) or PyJsStrictEq(var.get('group').get('type'),Js('mn')))):
                                            var.put('_child', var.get('group').get('children').get('0'))
                                            if (var.get('_child').instanceof(var.get('mathMLTree_TextNode')) and (var.get('_child').get('text').get('length')>Js(0.0))):
                                                var.get('_child').put('text', ((var.get('_child').get('text').callprop('slice', Js(0.0), Js(1.0))+Js('̸'))+var.get('_child').get('text').callprop('slice', Js(1.0))))
                                                var.get('groups').callprop('pop')
                    var.get('groups').callprop('push', var.get('group'))
                    var.put('lastGroup', var.get('group'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            return var.get('groups')
        PyJs_buildExpression_145_._set_name('buildExpression')
        var.put('buildMathML_buildExpression', PyJs_buildExpression_145_)
        @Js
        def PyJs_buildExpressionRow_146_(expression, options, this, arguments, var=var):
            var = Scope({'expression':expression, 'options':options, 'this':this, 'arguments':arguments, 'buildExpressionRow':PyJs_buildExpressionRow_146_}, var)
            var.registers(['options', 'expression'])
            return var.get('buildMathML_makeRow')(var.get('buildMathML_buildExpression')(var.get('expression'), var.get('options')))
        PyJs_buildExpressionRow_146_._set_name('buildExpressionRow')
        var.put('buildExpressionRow', PyJs_buildExpressionRow_146_)
        @Js
        def PyJs_buildGroup_147_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'buildGroup':PyJs_buildGroup_147_}, var)
            var.registers(['group', 'options', 'result'])
            if var.get('group').neg():
                return var.get('mathMLTree').get('MathNode').create(Js('mrow'))
            if var.get('_mathmlGroupBuilders').get(var.get('group').get('type')):
                var.put('result', var.get('_mathmlGroupBuilders').callprop(var.get('group').get('type'), var.get('group'), var.get('options')))
                return var.get('result')
            else:
                PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js("Got group of unknown type: '")+var.get('group').get('type'))+Js("'"))))
                raise PyJsTempException
        PyJs_buildGroup_147_._set_name('buildGroup')
        var.put('buildMathML_buildGroup', PyJs_buildGroup_147_)
        pass
        @Js
        def PyJs_optionsFromSettings_148_(settings, this, arguments, var=var):
            var = Scope({'settings':settings, 'this':this, 'arguments':arguments, 'optionsFromSettings':PyJs_optionsFromSettings_148_}, var)
            var.registers(['settings'])
            return var.get('src_Options').create(Js({'style':(var.get('src_Style').get('DISPLAY') if var.get('settings').get('displayMode') else var.get('src_Style').get('TEXT')),'maxSize':var.get('settings').get('maxSize')}))
        PyJs_optionsFromSettings_148_._set_name('optionsFromSettings')
        var.put('buildTree_optionsFromSettings', PyJs_optionsFromSettings_148_)
        @Js
        def PyJs_displayWrap_149_(node, settings, this, arguments, var=var):
            var = Scope({'node':node, 'settings':settings, 'this':this, 'arguments':arguments, 'displayWrap':PyJs_displayWrap_149_}, var)
            var.registers(['node', 'classes', 'settings'])
            if var.get('settings').get('displayMode'):
                var.put('classes', Js([Js('katex-display')]))
                if var.get('settings').get('leqno'):
                    var.get('classes').callprop('push', Js('leqno'))
                if var.get('settings').get('fleqn'):
                    var.get('classes').callprop('push', Js('fleqn'))
                var.put('node', var.get('buildCommon').callprop('makeSpan', var.get('classes'), Js([var.get('node')])))
            return var.get('node')
        PyJs_displayWrap_149_._set_name('displayWrap')
        var.put('buildTree_displayWrap', PyJs_displayWrap_149_)
        @Js
        def PyJs_buildTree_150_(tree, expression, settings, this, arguments, var=var):
            var = Scope({'tree':tree, 'expression':expression, 'settings':settings, 'this':this, 'arguments':arguments, 'buildTree':PyJs_buildTree_150_}, var)
            var.registers(['mathMLNode', 'expression', 'htmlNode', 'options', 'katexNode', 'settings', 'tree'])
            var.put('options', var.get('buildTree_optionsFromSettings')(var.get('settings')))
            var.put('mathMLNode', var.get('buildMathML')(var.get('tree'), var.get('expression'), var.get('options')))
            var.put('htmlNode', var.get('buildHTML')(var.get('tree'), var.get('options')))
            var.put('katexNode', var.get('buildCommon').callprop('makeSpan', Js([Js('katex')]), Js([var.get('mathMLNode'), var.get('htmlNode')])))
            return var.get('buildTree_displayWrap')(var.get('katexNode'), var.get('settings'))
        PyJs_buildTree_150_._set_name('buildTree')
        var.put('buildTree_buildTree', PyJs_buildTree_150_)
        @Js
        def PyJs_buildHTMLTree_151_(tree, expression, settings, this, arguments, var=var):
            var = Scope({'tree':tree, 'expression':expression, 'settings':settings, 'this':this, 'arguments':arguments, 'buildHTMLTree':PyJs_buildHTMLTree_151_}, var)
            var.registers(['expression', 'htmlNode', 'options', 'katexNode', 'settings', 'tree'])
            var.put('options', var.get('buildTree_optionsFromSettings')(var.get('settings')))
            var.put('htmlNode', var.get('buildHTML')(var.get('tree'), var.get('options')))
            var.put('katexNode', var.get('buildCommon').callprop('makeSpan', Js([Js('katex')]), Js([var.get('htmlNode')])))
            return var.get('buildTree_displayWrap')(var.get('katexNode'), var.get('settings'))
        PyJs_buildHTMLTree_151_._set_name('buildHTMLTree')
        var.put('buildTree_buildHTMLTree', PyJs_buildHTMLTree_151_)
        var.put('src_buildTree', var.get('buildTree_buildTree'))
        var.put('stretchyCodePoint', Js({'widehat':Js('^'),'widecheck':Js('ˇ'),'widetilde':Js('~'),'utilde':Js('~'),'overleftarrow':Js('←'),'underleftarrow':Js('←'),'xleftarrow':Js('←'),'overrightarrow':Js('→'),'underrightarrow':Js('→'),'xrightarrow':Js('→'),'underbrace':Js('⏟'),'overbrace':Js('⏞'),'overgroup':Js('⏠'),'undergroup':Js('⏡'),'overleftrightarrow':Js('↔'),'underleftrightarrow':Js('↔'),'xleftrightarrow':Js('↔'),'Overrightarrow':Js('⇒'),'xRightarrow':Js('⇒'),'overleftharpoon':Js('↼'),'xleftharpoonup':Js('↼'),'overrightharpoon':Js('⇀'),'xrightharpoonup':Js('⇀'),'xLeftarrow':Js('⇐'),'xLeftrightarrow':Js('⇔'),'xhookleftarrow':Js('↩'),'xhookrightarrow':Js('↪'),'xmapsto':Js('↦'),'xrightharpoondown':Js('⇁'),'xleftharpoondown':Js('↽'),'xrightleftharpoons':Js('⇌'),'xleftrightharpoons':Js('⇋'),'xtwoheadleftarrow':Js('↞'),'xtwoheadrightarrow':Js('↠'),'xlongequal':Js('='),'xtofrom':Js('⇄'),'xrightleftarrows':Js('⇄'),'xrightequilibrium':Js('⇌'),'xleftequilibrium':Js('⇋')}))
        @Js
        def PyJs_mathMLnode_152_(label, this, arguments, var=var):
            var = Scope({'label':label, 'this':this, 'arguments':arguments, 'mathMLnode':PyJs_mathMLnode_152_}, var)
            var.registers(['node', 'label'])
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mo'), Js([var.get('mathMLTree').get('TextNode').create(var.get('stretchyCodePoint').get(var.get('label').callprop('substr', Js(1.0))))])))
            var.get('node').callprop('setAttribute', Js('stretchy'), Js('true'))
            return var.get('node')
        PyJs_mathMLnode_152_._set_name('mathMLnode')
        var.put('stretchy_mathMLnode', PyJs_mathMLnode_152_)
        var.put('katexImagesData', Js({'overrightarrow':Js([Js([Js('rightarrow')]), Js(0.888), Js(522.0), Js('xMaxYMin')]),'overleftarrow':Js([Js([Js('leftarrow')]), Js(0.888), Js(522.0), Js('xMinYMin')]),'underrightarrow':Js([Js([Js('rightarrow')]), Js(0.888), Js(522.0), Js('xMaxYMin')]),'underleftarrow':Js([Js([Js('leftarrow')]), Js(0.888), Js(522.0), Js('xMinYMin')]),'xrightarrow':Js([Js([Js('rightarrow')]), Js(1.469), Js(522.0), Js('xMaxYMin')]),'xleftarrow':Js([Js([Js('leftarrow')]), Js(1.469), Js(522.0), Js('xMinYMin')]),'Overrightarrow':Js([Js([Js('doublerightarrow')]), Js(0.888), Js(560.0), Js('xMaxYMin')]),'xRightarrow':Js([Js([Js('doublerightarrow')]), Js(1.526), Js(560.0), Js('xMaxYMin')]),'xLeftarrow':Js([Js([Js('doubleleftarrow')]), Js(1.526), Js(560.0), Js('xMinYMin')]),'overleftharpoon':Js([Js([Js('leftharpoon')]), Js(0.888), Js(522.0), Js('xMinYMin')]),'xleftharpoonup':Js([Js([Js('leftharpoon')]), Js(0.888), Js(522.0), Js('xMinYMin')]),'xleftharpoondown':Js([Js([Js('leftharpoondown')]), Js(0.888), Js(522.0), Js('xMinYMin')]),'overrightharpoon':Js([Js([Js('rightharpoon')]), Js(0.888), Js(522.0), Js('xMaxYMin')]),'xrightharpoonup':Js([Js([Js('rightharpoon')]), Js(0.888), Js(522.0), Js('xMaxYMin')]),'xrightharpoondown':Js([Js([Js('rightharpoondown')]), Js(0.888), Js(522.0), Js('xMaxYMin')]),'xlongequal':Js([Js([Js('longequal')]), Js(0.888), Js(334.0), Js('xMinYMin')]),'xtwoheadleftarrow':Js([Js([Js('twoheadleftarrow')]), Js(0.888), Js(334.0), Js('xMinYMin')]),'xtwoheadrightarrow':Js([Js([Js('twoheadrightarrow')]), Js(0.888), Js(334.0), Js('xMaxYMin')]),'overleftrightarrow':Js([Js([Js('leftarrow'), Js('rightarrow')]), Js(0.888), Js(522.0)]),'overbrace':Js([Js([Js('leftbrace'), Js('midbrace'), Js('rightbrace')]), Js(1.6), Js(548.0)]),'underbrace':Js([Js([Js('leftbraceunder'), Js('midbraceunder'), Js('rightbraceunder')]), Js(1.6), Js(548.0)]),'underleftrightarrow':Js([Js([Js('leftarrow'), Js('rightarrow')]), Js(0.888), Js(522.0)]),'xleftrightarrow':Js([Js([Js('leftarrow'), Js('rightarrow')]), Js(1.75), Js(522.0)]),'xLeftrightarrow':Js([Js([Js('doubleleftarrow'), Js('doublerightarrow')]), Js(1.75), Js(560.0)]),'xrightleftharpoons':Js([Js([Js('leftharpoondownplus'), Js('rightharpoonplus')]), Js(1.75), Js(716.0)]),'xleftrightharpoons':Js([Js([Js('leftharpoonplus'), Js('rightharpoondownplus')]), Js(1.75), Js(716.0)]),'xhookleftarrow':Js([Js([Js('leftarrow'), Js('righthook')]), Js(1.08), Js(522.0)]),'xhookrightarrow':Js([Js([Js('lefthook'), Js('rightarrow')]), Js(1.08), Js(522.0)]),'overlinesegment':Js([Js([Js('leftlinesegment'), Js('rightlinesegment')]), Js(0.888), Js(522.0)]),'underlinesegment':Js([Js([Js('leftlinesegment'), Js('rightlinesegment')]), Js(0.888), Js(522.0)]),'overgroup':Js([Js([Js('leftgroup'), Js('rightgroup')]), Js(0.888), Js(342.0)]),'undergroup':Js([Js([Js('leftgroupunder'), Js('rightgroupunder')]), Js(0.888), Js(342.0)]),'xmapsto':Js([Js([Js('leftmapsto'), Js('rightarrow')]), Js(1.5), Js(522.0)]),'xtofrom':Js([Js([Js('leftToFrom'), Js('rightToFrom')]), Js(1.75), Js(528.0)]),'xrightleftarrows':Js([Js([Js('baraboveleftarrow'), Js('rightarrowabovebar')]), Js(1.75), Js(901.0)]),'xrightequilibrium':Js([Js([Js('baraboveshortleftharpoon'), Js('rightharpoonaboveshortbar')]), Js(1.75), Js(716.0)]),'xleftequilibrium':Js([Js([Js('shortbaraboveleftharpoon'), Js('shortrightharpoonabovebar')]), Js(1.75), Js(716.0)])}))
        @Js
        def PyJs_groupLength_153_(arg, this, arguments, var=var):
            var = Scope({'arg':arg, 'this':this, 'arguments':arguments, 'groupLength':PyJs_groupLength_153_}, var)
            var.registers(['arg'])
            if PyJsStrictEq(var.get('arg').get('type'),Js('ordgroup')):
                return var.get('arg').get('body').get('length')
            else:
                return Js(1.0)
        PyJs_groupLength_153_._set_name('groupLength')
        var.put('groupLength', PyJs_groupLength_153_)
        @Js
        def PyJs_svgSpan_154_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'svgSpan':PyJs_svgSpan_154_}, var)
            var.registers(['_buildSvgSpan_', 'group', 'options', 'buildSvgSpan_', 'span', 'height', 'minWidth'])
            @Js
            def PyJsHoisted_buildSvgSpan__(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers(['aligns', 'label', 'numChars', 'data', '_path', 'svgNode', '_svgNode', '_viewBoxHeight', 'align1', 'pathName', 'i', '_minWidth', 'spans', 'imgIndex', '_span', 'numSvgChildren', '_height2', 'widthClasses', 'viewBoxHeight', 'grp', 'viewBoxWidth', 'path', '_height', 'paths'])
                var.put('viewBoxWidth', Js(400000.0))
                var.put('label', var.get('group').get('label').callprop('substr', Js(1.0)))
                if var.get('utils').callprop('contains', Js([Js('widehat'), Js('widecheck'), Js('widetilde'), Js('utilde')]), var.get('label')):
                    var.put('grp', var.get('group'))
                    var.put('numChars', var.get('groupLength')(var.get('grp').get('base')))
                    pass
                    pass
                    pass
                    if (var.get('numChars')>Js(5.0)):
                        if (PyJsStrictEq(var.get('label'),Js('widehat')) or PyJsStrictEq(var.get('label'),Js('widecheck'))):
                            var.put('viewBoxHeight', Js(420.0))
                            var.put('viewBoxWidth', Js(2364.0))
                            var.put('_height', Js(0.42))
                            var.put('pathName', (var.get('label')+Js('4')))
                        else:
                            var.put('viewBoxHeight', Js(312.0))
                            var.put('viewBoxWidth', Js(2340.0))
                            var.put('_height', Js(0.34))
                            var.put('pathName', Js('tilde4'))
                    else:
                        var.put('imgIndex', Js([Js(1.0), Js(1.0), Js(2.0), Js(2.0), Js(3.0), Js(3.0)]).get(var.get('numChars')))
                        if (PyJsStrictEq(var.get('label'),Js('widehat')) or PyJsStrictEq(var.get('label'),Js('widecheck'))):
                            var.put('viewBoxWidth', Js([Js(0.0), Js(1062.0), Js(2364.0), Js(2364.0), Js(2364.0)]).get(var.get('imgIndex')))
                            var.put('viewBoxHeight', Js([Js(0.0), Js(239.0), Js(300.0), Js(360.0), Js(420.0)]).get(var.get('imgIndex')))
                            var.put('_height', Js([Js(0.0), Js(0.24), Js(0.3), Js(0.3), Js(0.36), Js(0.42)]).get(var.get('imgIndex')))
                            var.put('pathName', (var.get('label')+var.get('imgIndex')))
                        else:
                            var.put('viewBoxWidth', Js([Js(0.0), Js(600.0), Js(1033.0), Js(2339.0), Js(2340.0)]).get(var.get('imgIndex')))
                            var.put('viewBoxHeight', Js([Js(0.0), Js(260.0), Js(286.0), Js(306.0), Js(312.0)]).get(var.get('imgIndex')))
                            var.put('_height', Js([Js(0.0), Js(0.26), Js(0.286), Js(0.3), Js(0.306), Js(0.34)]).get(var.get('imgIndex')))
                            var.put('pathName', (Js('tilde')+var.get('imgIndex')))
                    var.put('path', var.get('domTree_PathNode').create(var.get('pathName')))
                    var.put('svgNode', var.get('SvgNode').create(Js([var.get('path')]), Js({'width':Js('100%'),'height':(var.get('_height')+Js('em')),'viewBox':(((Js('0 0 ')+var.get('viewBoxWidth'))+Js(' '))+var.get('viewBoxHeight')),'preserveAspectRatio':Js('none')})))
                    return Js({'span':var.get('buildCommon').callprop('makeSvgSpan', Js([]), Js([var.get('svgNode')]), var.get('options')),'minWidth':Js(0.0),'height':var.get('_height')})
                else:
                    var.put('spans', Js([]))
                    var.put('data', var.get('katexImagesData').get(var.get('label')))
                    var.put('paths', var.get('data').get('0'))
                    var.put('_minWidth', var.get('data').get('1'))
                    var.put('_viewBoxHeight', var.get('data').get('2'))
                    var.put('_height2', (var.get('_viewBoxHeight')/Js(1000.0)))
                    var.put('numSvgChildren', var.get('paths').get('length'))
                    pass
                    pass
                    if PyJsStrictEq(var.get('numSvgChildren'),Js(1.0)):
                        var.put('align1', var.get('data').get('3'))
                        var.put('widthClasses', Js([Js('hide-tail')]))
                        var.put('aligns', Js([var.get('align1')]))
                    else:
                        if PyJsStrictEq(var.get('numSvgChildren'),Js(2.0)):
                            var.put('widthClasses', Js([Js('halfarrow-left'), Js('halfarrow-right')]))
                            var.put('aligns', Js([Js('xMinYMin'), Js('xMaxYMin')]))
                        else:
                            if PyJsStrictEq(var.get('numSvgChildren'),Js(3.0)):
                                var.put('widthClasses', Js([Js('brace-left'), Js('brace-center'), Js('brace-right')]))
                                var.put('aligns', Js([Js('xMinYMin'), Js('xMidYMin'), Js('xMaxYMin')]))
                            else:
                                PyJsTempException = JsToPyException(var.get('Error').create(((Js('Correct katexImagesData or update code here to support\n                    ')+var.get('numSvgChildren'))+Js(' children.'))))
                                raise PyJsTempException
                    #for JS loop
                    var.put('i', Js(0.0))
                    while (var.get('i')<var.get('numSvgChildren')):
                        try:
                            var.put('_path', var.get('domTree_PathNode').create(var.get('paths').get(var.get('i'))))
                            var.put('_svgNode', var.get('SvgNode').create(Js([var.get('_path')]), Js({'width':Js('400em'),'height':(var.get('_height2')+Js('em')),'viewBox':(((Js('0 0 ')+var.get('viewBoxWidth'))+Js(' '))+var.get('_viewBoxHeight')),'preserveAspectRatio':(var.get('aligns').get(var.get('i'))+Js(' slice'))})))
                            var.put('_span', var.get('buildCommon').callprop('makeSvgSpan', Js([var.get('widthClasses').get(var.get('i'))]), Js([var.get('_svgNode')]), var.get('options')))
                            if PyJsStrictEq(var.get('numSvgChildren'),Js(1.0)):
                                return Js({'span':var.get('_span'),'minWidth':var.get('_minWidth'),'height':var.get('_height2')})
                            else:
                                var.get('_span').get('style').put('height', (var.get('_height2')+Js('em')))
                                var.get('spans').callprop('push', var.get('_span'))
                        finally:
                                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                    return Js({'span':var.get('buildCommon').callprop('makeSpan', Js([Js('stretchy')]), var.get('spans'), var.get('options')),'minWidth':var.get('_minWidth'),'height':var.get('_height2')})
            PyJsHoisted_buildSvgSpan__.func_name = 'buildSvgSpan_'
            var.put('buildSvgSpan_', PyJsHoisted_buildSvgSpan__)
            pass
            var.put('_buildSvgSpan_', var.get('buildSvgSpan_')())
            var.put('span', var.get('_buildSvgSpan_').get('span'))
            var.put('minWidth', var.get('_buildSvgSpan_').get('minWidth'))
            var.put('height', var.get('_buildSvgSpan_').get('height'))
            var.get('span').put('height', var.get('height'))
            var.get('span').get('style').put('height', (var.get('height')+Js('em')))
            if (var.get('minWidth')>Js(0.0)):
                var.get('span').get('style').put('minWidth', (var.get('minWidth')+Js('em')))
            return var.get('span')
        PyJs_svgSpan_154_._set_name('svgSpan')
        var.put('stretchy_svgSpan', PyJs_svgSpan_154_)
        @Js
        def PyJs_encloseSpan_155_(inner, label, pad, options, this, arguments, var=var):
            var = Scope({'inner':inner, 'label':label, 'pad':pad, 'options':options, 'this':this, 'arguments':arguments, 'encloseSpan':PyJs_encloseSpan_155_}, var)
            var.registers(['label', 'pad', 'img', 'color', 'options', 'totalHeight', 'svgNode', 'inner', 'lines'])
            pass
            var.put('totalHeight', ((var.get('inner').get('height')+var.get('inner').get('depth'))+(Js(2.0)*var.get('pad'))))
            if JsRegExp('/fbox|color/').callprop('test', var.get('label')):
                var.put('img', var.get('buildCommon').callprop('makeSpan', Js([Js('stretchy'), var.get('label')]), Js([]), var.get('options')))
                if PyJsStrictEq(var.get('label'),Js('fbox')):
                    var.put('color', (var.get('options').get('color') and var.get('options').callprop('getColor')))
                    if var.get('color'):
                        var.get('img').get('style').put('borderColor', var.get('color'))
            else:
                var.put('lines', Js([]))
                if JsRegExp('/^[bx]cancel$/').callprop('test', var.get('label')):
                    var.get('lines').callprop('push', var.get('LineNode').create(Js({'x1':Js('0'),'y1':Js('0'),'x2':Js('100%'),'y2':Js('100%'),'stroke-width':Js('0.046em')})))
                if JsRegExp('/^x?cancel$/').callprop('test', var.get('label')):
                    var.get('lines').callprop('push', var.get('LineNode').create(Js({'x1':Js('0'),'y1':Js('100%'),'x2':Js('100%'),'y2':Js('0'),'stroke-width':Js('0.046em')})))
                var.put('svgNode', var.get('SvgNode').create(var.get('lines'), Js({'width':Js('100%'),'height':(var.get('totalHeight')+Js('em'))})))
                var.put('img', var.get('buildCommon').callprop('makeSvgSpan', Js([]), Js([var.get('svgNode')]), var.get('options')))
            var.get('img').put('height', var.get('totalHeight'))
            var.get('img').get('style').put('height', (var.get('totalHeight')+Js('em')))
            return var.get('img')
        PyJs_encloseSpan_155_._set_name('encloseSpan')
        var.put('stretchy_encloseSpan', PyJs_encloseSpan_155_)
        var.put('stretchy', Js({'encloseSpan':var.get('stretchy_encloseSpan'),'mathMLnode':var.get('stretchy_mathMLnode'),'svgSpan':var.get('stretchy_svgSpan')}))
        @Js
        def PyJs_htmlBuilder_156_(grp, options, this, arguments, var=var):
            var = Scope({'grp':grp, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_156_}, var)
            var.registers(['left', 'accentWrap', 'group', 'body', 'supSubGroup', 'options', 'accentBody', 'clearance', 'accentFull', 'mustShift', 'accent', 'baseGroup', 'width', 'base', 'grp', 'skew', 'baseChar', 'supSub'])
            pass
            pass
            var.put('supSub', var.get('checkNodeType')(var.get('grp'), Js('supsub')))
            pass
            if var.get('supSub'):
                var.put('group', var.get('assertNodeType')(var.get('supSub').get('base'), Js('accent')))
                var.put('base', var.get('group').get('base'))
                var.get('supSub').put('base', var.get('base'))
                var.put('supSubGroup', var.get('assertSpan')(var.get('buildHTML_buildGroup')(var.get('supSub'), var.get('options'))))
                var.get('supSub').put('base', var.get('group'))
            else:
                var.put('group', var.get('assertNodeType')(var.get('grp'), Js('accent')))
                var.put('base', var.get('group').get('base'))
            var.put('body', var.get('buildHTML_buildGroup')(var.get('base'), var.get('options').callprop('havingCrampedStyle')))
            var.put('mustShift', (var.get('group').get('isShifty') and var.get('utils').callprop('isCharacterBox', var.get('base'))))
            var.put('skew', Js(0.0))
            if var.get('mustShift'):
                var.put('baseChar', var.get('utils').callprop('getBaseElem', var.get('base')))
                var.put('baseGroup', var.get('buildHTML_buildGroup')(var.get('baseChar'), var.get('options').callprop('havingCrampedStyle')))
                var.put('skew', var.get('assertSymbolDomNode')(var.get('baseGroup')).get('skew'))
            var.put('clearance', var.get('Math').callprop('min', var.get('body').get('height'), var.get('options').callprop('fontMetrics').get('xHeight')))
            pass
            if var.get('group').get('isStretchy').neg():
                pass
                pass
                if PyJsStrictEq(var.get('group').get('label'),Js('\\vec')):
                    var.put('accent', var.get('buildCommon').callprop('staticSvg', Js('vec'), var.get('options')))
                    var.put('width', var.get('buildCommon').get('svgData').get('vec').get('1'))
                else:
                    var.put('accent', var.get('buildCommon').callprop('makeSymbol', var.get('group').get('label'), Js('Main-Regular'), var.get('group').get('mode'), var.get('options')))
                    var.get('accent').put('italic', Js(0.0))
                    var.put('width', var.get('accent').get('width'))
                var.put('accentBody', var.get('buildCommon').callprop('makeSpan', Js([Js('accent-body')]), Js([var.get('accent')])))
                var.put('accentFull', PyJsStrictEq(var.get('group').get('label'),Js('\\textcircled')))
                if var.get('accentFull'):
                    var.get('accentBody').get('classes').callprop('push', Js('accent-full'))
                    var.put('clearance', var.get('body').get('height'))
                var.put('left', var.get('skew'))
                if var.get('accentFull').neg():
                    var.put('left', (var.get('width')/Js(2.0)), '-')
                var.get('accentBody').get('style').put('left', (var.get('left')+Js('em')))
                if PyJsStrictEq(var.get('group').get('label'),Js('\\textcircled')):
                    var.get('accentBody').get('style').put('top', Js('.2em'))
                var.put('accentBody', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('firstBaseline'),'children':Js([Js({'type':Js('elem'),'elem':var.get('body')}), Js({'type':Js('kern'),'size':(-var.get('clearance'))}), Js({'type':Js('elem'),'elem':var.get('accentBody')})])}), var.get('options')))
            else:
                var.put('accentBody', var.get('stretchy').callprop('svgSpan', var.get('group'), var.get('options')))
                def PyJs_LONG_157_(var=var):
                    return var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('firstBaseline'),'children':Js([Js({'type':Js('elem'),'elem':var.get('body')}), Js({'type':Js('elem'),'elem':var.get('accentBody'),'wrapperClasses':Js([Js('svg-align')]),'wrapperStyle':(Js({'width':((Js('calc(100% - ')+(Js(2.0)*var.get('skew')))+Js('em)')),'marginLeft':((Js(2.0)*var.get('skew'))+Js('em'))}) if (var.get('skew')>Js(0.0)) else var.get('undefined'))})])}), var.get('options'))
                var.put('accentBody', PyJs_LONG_157_())
            var.put('accentWrap', var.get('buildCommon').callprop('makeSpan', Js([Js('mord'), Js('accent')]), Js([var.get('accentBody')]), var.get('options')))
            if var.get('supSubGroup'):
                var.get('supSubGroup').get('children').put('0', var.get('accentWrap'))
                var.get('supSubGroup').put('height', var.get('Math').callprop('max', var.get('accentWrap').get('height'), var.get('supSubGroup').get('height')))
                var.get('supSubGroup').get('classes').put('0', Js('mord'))
                return var.get('supSubGroup')
            else:
                return var.get('accentWrap')
        PyJs_htmlBuilder_156_._set_name('htmlBuilder')
        var.put('accent_htmlBuilder', PyJs_htmlBuilder_156_)
        @Js
        def PyJs_mathmlBuilder_158_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_158_}, var)
            var.registers(['node', 'group', 'options', 'accentNode'])
            var.put('accentNode', (var.get('stretchy').callprop('mathMLnode', var.get('group').get('label')) if var.get('group').get('isStretchy') else var.get('mathMLTree').get('MathNode').create(Js('mo'), Js([var.get('buildMathML_makeText')(var.get('group').get('label'), var.get('group').get('mode'))]))))
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mover'), Js([var.get('buildMathML_buildGroup')(var.get('group').get('base'), var.get('options')), var.get('accentNode')])))
            var.get('node').callprop('setAttribute', Js('accent'), Js('true'))
            return var.get('node')
        PyJs_mathmlBuilder_158_._set_name('mathmlBuilder')
        var.put('accent_mathmlBuilder', PyJs_mathmlBuilder_158_)
        @Js
        def PyJs_anonymous_159_(accent, this, arguments, var=var):
            var = Scope({'accent':accent, 'this':this, 'arguments':arguments}, var)
            var.registers(['accent'])
            return (Js('\\')+var.get('accent'))
        PyJs_anonymous_159_._set_name('anonymous')
        var.put('NON_STRETCHY_ACCENT_REGEX', var.get('RegExp').create(Js([Js('\\acute'), Js('\\grave'), Js('\\ddot'), Js('\\tilde'), Js('\\bar'), Js('\\breve'), Js('\\check'), Js('\\hat'), Js('\\vec'), Js('\\dot'), Js('\\mathring')]).callprop('map', PyJs_anonymous_159_).callprop('join', Js('|'))))
        def PyJs_LONG_161_(var=var):
            @Js
            def PyJs_handler_160_(context, args, this, arguments, var=var):
                var = Scope({'context':context, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_160_}, var)
                var.registers(['isShifty', 'isStretchy', 'context', 'args', 'base'])
                var.put('base', var.get('args').get('0'))
                var.put('isStretchy', var.get('NON_STRETCHY_ACCENT_REGEX').callprop('test', var.get('context').get('funcName')).neg())
                var.put('isShifty', (((var.get('isStretchy').neg() or PyJsStrictEq(var.get('context').get('funcName'),Js('\\widehat'))) or PyJsStrictEq(var.get('context').get('funcName'),Js('\\widetilde'))) or PyJsStrictEq(var.get('context').get('funcName'),Js('\\widecheck'))))
                return Js({'type':Js('accent'),'mode':var.get('context').get('parser').get('mode'),'label':var.get('context').get('funcName'),'isStretchy':var.get('isStretchy'),'isShifty':var.get('isShifty'),'base':var.get('base')})
            PyJs_handler_160_._set_name('handler')
            return var.get('defineFunction')(Js({'type':Js('accent'),'names':Js([Js('\\acute'), Js('\\grave'), Js('\\ddot'), Js('\\tilde'), Js('\\bar'), Js('\\breve'), Js('\\check'), Js('\\hat'), Js('\\vec'), Js('\\dot'), Js('\\mathring'), Js('\\widecheck'), Js('\\widehat'), Js('\\widetilde'), Js('\\overrightarrow'), Js('\\overleftarrow'), Js('\\Overrightarrow'), Js('\\overleftrightarrow'), Js('\\overgroup'), Js('\\overlinesegment'), Js('\\overleftharpoon'), Js('\\overrightharpoon')]),'props':Js({'numArgs':Js(1.0)}),'handler':PyJs_handler_160_,'htmlBuilder':var.get('accent_htmlBuilder'),'mathmlBuilder':var.get('accent_mathmlBuilder')}))
        PyJs_LONG_161_()
        def PyJs_LONG_163_(var=var):
            @Js
            def PyJs_handler_162_(context, args, this, arguments, var=var):
                var = Scope({'context':context, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_162_}, var)
                var.registers(['base', 'context', 'args'])
                var.put('base', var.get('args').get('0'))
                return Js({'type':Js('accent'),'mode':var.get('context').get('parser').get('mode'),'label':var.get('context').get('funcName'),'isStretchy':Js(False),'isShifty':Js(True),'base':var.get('base')})
            PyJs_handler_162_._set_name('handler')
            return var.get('defineFunction')(Js({'type':Js('accent'),'names':Js([Js("\\'"), Js('\\`'), Js('\\^'), Js('\\~'), Js('\\='), Js('\\u'), Js('\\.'), Js('\\"'), Js('\\r'), Js('\\H'), Js('\\v'), Js('\\textcircled')]),'props':Js({'numArgs':Js(1.0),'allowedInText':Js(True),'allowedInMath':Js(False)}),'handler':PyJs_handler_162_,'htmlBuilder':var.get('accent_htmlBuilder'),'mathmlBuilder':var.get('accent_mathmlBuilder')}))
        PyJs_LONG_163_()
        @Js
        def PyJs_handler_164_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_164_}, var)
            var.registers(['funcName', 'base', '_ref', 'args', 'parser'])
            var.put('parser', var.get('_ref').get('parser'))
            var.put('funcName', var.get('_ref').get('funcName'))
            var.put('base', var.get('args').get('0'))
            return Js({'type':Js('accentUnder'),'mode':var.get('parser').get('mode'),'label':var.get('funcName'),'base':var.get('base')})
        PyJs_handler_164_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_165_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_165_}, var)
            var.registers(['kern', 'group', 'options', 'accentBody', 'innerGroup', 'vlist'])
            var.put('innerGroup', var.get('buildHTML_buildGroup')(var.get('group').get('base'), var.get('options')))
            var.put('accentBody', var.get('stretchy').callprop('svgSpan', var.get('group'), var.get('options')))
            var.put('kern', (Js(0.12) if PyJsStrictEq(var.get('group').get('label'),Js('\\utilde')) else Js(0.0)))
            var.put('vlist', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('bottom'),'positionData':(var.get('accentBody').get('height')+var.get('kern')),'children':Js([Js({'type':Js('elem'),'elem':var.get('accentBody'),'wrapperClasses':Js([Js('svg-align')])}), Js({'type':Js('kern'),'size':var.get('kern')}), Js({'type':Js('elem'),'elem':var.get('innerGroup')})])}), var.get('options')))
            return var.get('buildCommon').callprop('makeSpan', Js([Js('mord'), Js('accentunder')]), Js([var.get('vlist')]), var.get('options'))
        PyJs_htmlBuilder_165_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_166_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_166_}, var)
            var.registers(['node', 'group', 'options', 'accentNode'])
            var.put('accentNode', var.get('stretchy').callprop('mathMLnode', var.get('group').get('label')))
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('munder'), Js([var.get('buildMathML_buildGroup')(var.get('group').get('base'), var.get('options')), var.get('accentNode')])))
            var.get('node').callprop('setAttribute', Js('accentunder'), Js('true'))
            return var.get('node')
        PyJs_mathmlBuilder_166_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('accentUnder'),'names':Js([Js('\\underleftarrow'), Js('\\underrightarrow'), Js('\\underleftrightarrow'), Js('\\undergroup'), Js('\\underlinesegment'), Js('\\utilde')]),'props':Js({'numArgs':Js(1.0)}),'handler':PyJs_handler_164_,'htmlBuilder':PyJs_htmlBuilder_165_,'mathmlBuilder':PyJs_mathmlBuilder_166_}))
        @Js
        def PyJs_paddedNode_167_(group, this, arguments, var=var):
            var = Scope({'group':group, 'this':this, 'arguments':arguments, 'paddedNode':PyJs_paddedNode_167_}, var)
            var.registers(['node', 'group'])
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mpadded'), (Js([var.get('group')]) if var.get('group') else Js([]))))
            var.get('node').callprop('setAttribute', Js('width'), Js('+0.6em'))
            var.get('node').callprop('setAttribute', Js('lspace'), Js('0.3em'))
            return var.get('node')
        PyJs_paddedNode_167_._set_name('paddedNode')
        var.put('arrow_paddedNode', PyJs_paddedNode_167_)
        def PyJs_LONG_171_(var=var):
            @Js
            def PyJs_handler_168_(_ref, args, optArgs, this, arguments, var=var):
                var = Scope({'_ref':_ref, 'args':args, 'optArgs':optArgs, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_168_}, var)
                var.registers(['funcName', 'optArgs', '_ref', 'args', 'parser'])
                var.put('parser', var.get('_ref').get('parser'))
                var.put('funcName', var.get('_ref').get('funcName'))
                return Js({'type':Js('xArrow'),'mode':var.get('parser').get('mode'),'label':var.get('funcName'),'body':var.get('args').get('0'),'below':var.get('optArgs').get('0')})
            PyJs_handler_168_._set_name('handler')
            @Js
            def PyJs_htmlBuilder_169_(group, options, this, arguments, var=var):
                var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_169_}, var)
                var.registers(['upperGroup', 'newOptions', 'group', 'options', 'arrowBody', 'upperShift', 'arrowShift', 'lowerShift', 'style', 'vlist', 'lowerGroup'])
                var.put('style', var.get('options').get('style'))
                var.put('newOptions', var.get('options').callprop('havingStyle', var.get('style').callprop('sup')))
                var.put('upperGroup', var.get('buildCommon').callprop('wrapFragment', var.get('buildHTML_buildGroup')(var.get('group').get('body'), var.get('newOptions'), var.get('options')), var.get('options')))
                var.get('upperGroup').get('classes').callprop('push', Js('x-arrow-pad'))
                pass
                if var.get('group').get('below'):
                    var.put('newOptions', var.get('options').callprop('havingStyle', var.get('style').callprop('sub')))
                    var.put('lowerGroup', var.get('buildCommon').callprop('wrapFragment', var.get('buildHTML_buildGroup')(var.get('group').get('below'), var.get('newOptions'), var.get('options')), var.get('options')))
                    var.get('lowerGroup').get('classes').callprop('push', Js('x-arrow-pad'))
                var.put('arrowBody', var.get('stretchy').callprop('svgSpan', var.get('group'), var.get('options')))
                var.put('arrowShift', ((-var.get('options').callprop('fontMetrics').get('axisHeight'))+(Js(0.5)*var.get('arrowBody').get('height'))))
                var.put('upperShift', (((-var.get('options').callprop('fontMetrics').get('axisHeight'))-(Js(0.5)*var.get('arrowBody').get('height')))-Js(0.111)))
                if ((var.get('upperGroup').get('depth')>Js(0.25)) or PyJsStrictEq(var.get('group').get('label'),Js('\\xleftequilibrium'))):
                    var.put('upperShift', var.get('upperGroup').get('depth'), '-')
                pass
                if var.get('lowerGroup'):
                    var.put('lowerShift', ((((-var.get('options').callprop('fontMetrics').get('axisHeight'))+var.get('lowerGroup').get('height'))+(Js(0.5)*var.get('arrowBody').get('height')))+Js(0.111)))
                    var.put('vlist', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('individualShift'),'children':Js([Js({'type':Js('elem'),'elem':var.get('upperGroup'),'shift':var.get('upperShift')}), Js({'type':Js('elem'),'elem':var.get('arrowBody'),'shift':var.get('arrowShift')}), Js({'type':Js('elem'),'elem':var.get('lowerGroup'),'shift':var.get('lowerShift')})])}), var.get('options')))
                else:
                    var.put('vlist', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('individualShift'),'children':Js([Js({'type':Js('elem'),'elem':var.get('upperGroup'),'shift':var.get('upperShift')}), Js({'type':Js('elem'),'elem':var.get('arrowBody'),'shift':var.get('arrowShift')})])}), var.get('options')))
                var.get('vlist').get('children').get('0').get('children').get('0').get('children').get('1').get('classes').callprop('push', Js('svg-align'))
                return var.get('buildCommon').callprop('makeSpan', Js([Js('mrel'), Js('x-arrow')]), Js([var.get('vlist')]), var.get('options'))
            PyJs_htmlBuilder_169_._set_name('htmlBuilder')
            @Js
            def PyJs_mathmlBuilder_170_(group, options, this, arguments, var=var):
                var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_170_}, var)
                var.registers(['group', 'arrowNode', 'options', 'node', 'lowerNode', 'upperNode', '_lowerNode'])
                var.put('arrowNode', var.get('stretchy').callprop('mathMLnode', var.get('group').get('label')))
                pass
                if var.get('group').get('body'):
                    var.put('upperNode', var.get('arrow_paddedNode')(var.get('buildMathML_buildGroup')(var.get('group').get('body'), var.get('options'))))
                    if var.get('group').get('below'):
                        var.put('lowerNode', var.get('arrow_paddedNode')(var.get('buildMathML_buildGroup')(var.get('group').get('below'), var.get('options'))))
                        var.put('node', var.get('mathMLTree').get('MathNode').create(Js('munderover'), Js([var.get('arrowNode'), var.get('lowerNode'), var.get('upperNode')])))
                    else:
                        var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mover'), Js([var.get('arrowNode'), var.get('upperNode')])))
                else:
                    if var.get('group').get('below'):
                        var.put('_lowerNode', var.get('arrow_paddedNode')(var.get('buildMathML_buildGroup')(var.get('group').get('below'), var.get('options'))))
                        var.put('node', var.get('mathMLTree').get('MathNode').create(Js('munder'), Js([var.get('arrowNode'), var.get('_lowerNode')])))
                    else:
                        var.put('node', var.get('arrow_paddedNode')())
                        var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mover'), Js([var.get('arrowNode'), var.get('node')])))
                return var.get('node')
            PyJs_mathmlBuilder_170_._set_name('mathmlBuilder')
            return var.get('defineFunction')(Js({'type':Js('xArrow'),'names':Js([Js('\\xleftarrow'), Js('\\xrightarrow'), Js('\\xLeftarrow'), Js('\\xRightarrow'), Js('\\xleftrightarrow'), Js('\\xLeftrightarrow'), Js('\\xhookleftarrow'), Js('\\xhookrightarrow'), Js('\\xmapsto'), Js('\\xrightharpoondown'), Js('\\xrightharpoonup'), Js('\\xleftharpoondown'), Js('\\xleftharpoonup'), Js('\\xrightleftharpoons'), Js('\\xleftrightharpoons'), Js('\\xlongequal'), Js('\\xtwoheadrightarrow'), Js('\\xtwoheadleftarrow'), Js('\\xtofrom'), Js('\\xrightleftarrows'), Js('\\xrightequilibrium'), Js('\\xleftequilibrium')]),'props':Js({'numArgs':Js(1.0),'numOptionalArgs':Js(1.0)}),'handler':PyJs_handler_168_,'htmlBuilder':PyJs_htmlBuilder_169_,'mathmlBuilder':PyJs_mathmlBuilder_170_}))
        PyJs_LONG_171_()
        @Js
        def PyJs_handler_172_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_172_}, var)
            var.registers(['code', 'i', 'group', 'arg', 'node', '_ref', 'args', 'parser', 'number'])
            var.put('parser', var.get('_ref').get('parser'))
            var.put('arg', var.get('assertNodeType')(var.get('args').get('0'), Js('ordgroup')))
            var.put('group', var.get('arg').get('body'))
            var.put('number', Js(''))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('group').get('length')):
                try:
                    var.put('node', var.get('assertNodeType')(var.get('group').get(var.get('i')), Js('textord')))
                    var.put('number', var.get('node').get('text'), '+')
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('code', var.get('parseInt')(var.get('number')))
            if var.get('isNaN')(var.get('code')):
                PyJsTempException = JsToPyException(var.get('src_ParseError').create((Js('\\@char has non-numeric argument ')+var.get('number'))))
                raise PyJsTempException
            return Js({'type':Js('textord'),'mode':var.get('parser').get('mode'),'text':var.get('String').callprop('fromCharCode', var.get('code'))})
        PyJs_handler_172_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('textord'),'names':Js([Js('\\@char')]),'props':Js({'numArgs':Js(1.0),'allowedInText':Js(True)}),'handler':PyJs_handler_172_}))
        @Js
        def PyJs_htmlBuilder_173_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_173_}, var)
            var.registers(['group', 'options', 'elements'])
            var.put('elements', var.get('buildHTML_buildExpression')(var.get('group').get('body'), var.get('options').callprop('withColor', var.get('group').get('color')), Js(False)))
            return var.get('buildCommon').callprop('makeFragment', var.get('elements'))
        PyJs_htmlBuilder_173_._set_name('htmlBuilder')
        var.put('color_htmlBuilder', PyJs_htmlBuilder_173_)
        @Js
        def PyJs_mathmlBuilder_174_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_174_}, var)
            var.registers(['node', 'inner', 'group', 'options'])
            var.put('inner', var.get('buildMathML_buildExpression')(var.get('group').get('body'), var.get('options').callprop('withColor', var.get('group').get('color'))))
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mstyle'), var.get('inner')))
            var.get('node').callprop('setAttribute', Js('mathcolor'), var.get('group').get('color'))
            return var.get('node')
        PyJs_mathmlBuilder_174_._set_name('mathmlBuilder')
        var.put('color_mathmlBuilder', PyJs_mathmlBuilder_174_)
        @Js
        def PyJs_handler_175_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_175_}, var)
            var.registers(['color', 'body', '_ref', 'args', 'parser'])
            var.put('parser', var.get('_ref').get('parser'))
            var.put('color', var.get('assertNodeType')(var.get('args').get('0'), Js('color-token')).get('color'))
            var.put('body', var.get('args').get('1'))
            return Js({'type':Js('color'),'mode':var.get('parser').get('mode'),'color':var.get('color'),'body':var.get('defineFunction_ordargument')(var.get('body'))})
        PyJs_handler_175_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('color'),'names':Js([Js('\\textcolor')]),'props':Js({'numArgs':Js(2.0),'allowedInText':Js(True),'greediness':Js(3.0),'argTypes':Js([Js('color'), Js('original')])}),'handler':PyJs_handler_175_,'htmlBuilder':var.get('color_htmlBuilder'),'mathmlBuilder':var.get('color_mathmlBuilder')}))
        @Js
        def PyJs_handler_176_(_ref2, args, this, arguments, var=var):
            var = Scope({'_ref2':_ref2, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_176_}, var)
            var.registers(['breakOnTokenText', 'color', 'body', 'args', 'parser', '_ref2'])
            var.put('parser', var.get('_ref2').get('parser'))
            var.put('breakOnTokenText', var.get('_ref2').get('breakOnTokenText'))
            var.put('color', var.get('assertNodeType')(var.get('args').get('0'), Js('color-token')).get('color'))
            var.put('body', var.get('parser').callprop('parseExpression', Js(True), var.get('breakOnTokenText')))
            return Js({'type':Js('color'),'mode':var.get('parser').get('mode'),'color':var.get('color'),'body':var.get('body')})
        PyJs_handler_176_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('color'),'names':Js([Js('\\color')]),'props':Js({'numArgs':Js(1.0),'allowedInText':Js(True),'greediness':Js(3.0),'argTypes':Js([Js('color')])}),'handler':PyJs_handler_176_,'htmlBuilder':var.get('color_htmlBuilder'),'mathmlBuilder':var.get('color_mathmlBuilder')}))
        @Js
        def PyJs_handler_177_(_ref, args, optArgs, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'optArgs':optArgs, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_177_}, var)
            var.registers(['funcName', 'size', 'newLine', 'newRow', '_ref', 'optArgs', 'args', 'parser'])
            var.put('parser', var.get('_ref').get('parser'))
            var.put('funcName', var.get('_ref').get('funcName'))
            var.put('size', var.get('optArgs').get('0'))
            var.put('newRow', PyJsStrictEq(var.get('funcName'),Js('\\cr')))
            var.put('newLine', Js(False))
            if var.get('newRow').neg():
                if (var.get('parser').get('settings').get('displayMode') and var.get('parser').get('settings').callprop('useStrictBehavior', Js('newLineInDisplayMode'), (Js('In LaTeX, \\\\ or \\newline ')+Js('does nothing in display mode')))):
                    var.put('newLine', Js(False))
                else:
                    var.put('newLine', Js(True))
            return Js({'type':Js('cr'),'mode':var.get('parser').get('mode'),'newLine':var.get('newLine'),'newRow':var.get('newRow'),'size':(var.get('size') and var.get('assertNodeType')(var.get('size'), Js('size')).get('value'))})
        PyJs_handler_177_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_178_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_178_}, var)
            var.registers(['group', 'options', 'span'])
            if var.get('group').get('newRow'):
                PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('\\cr valid only within a tabular/array environment')))
                raise PyJsTempException
            var.put('span', var.get('buildCommon').callprop('makeSpan', Js([Js('mspace')]), Js([]), var.get('options')))
            if var.get('group').get('newLine'):
                var.get('span').get('classes').callprop('push', Js('newline'))
                if var.get('group').get('size'):
                    var.get('span').get('style').put('marginTop', (var.get('units_calculateSize')(var.get('group').get('size'), var.get('options'))+Js('em')))
            return var.get('span')
        PyJs_htmlBuilder_178_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_179_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_179_}, var)
            var.registers(['node', 'group', 'options'])
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mspace')))
            if var.get('group').get('newLine'):
                var.get('node').callprop('setAttribute', Js('linebreak'), Js('newline'))
                if var.get('group').get('size'):
                    var.get('node').callprop('setAttribute', Js('height'), (var.get('units_calculateSize')(var.get('group').get('size'), var.get('options'))+Js('em')))
            return var.get('node')
        PyJs_mathmlBuilder_179_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('cr'),'names':Js([Js('\\cr'), Js('\\newline')]),'props':Js({'numArgs':Js(0.0),'numOptionalArgs':Js(1.0),'argTypes':Js([Js('size')]),'allowedInText':Js(True)}),'handler':PyJs_handler_177_,'htmlBuilder':PyJs_htmlBuilder_178_,'mathmlBuilder':PyJs_mathmlBuilder_179_}))
        @Js
        def PyJs_getMetrics_180_(symbol, font, mode, this, arguments, var=var):
            var = Scope({'symbol':symbol, 'font':font, 'mode':mode, 'this':this, 'arguments':arguments, 'getMetrics':PyJs_getMetrics_180_}, var)
            var.registers(['replace', 'mode', 'font', 'symbol', 'metrics'])
            var.put('replace', (var.get('src_symbols').get('math').get(var.get('symbol')) and var.get('src_symbols').get('math').get(var.get('symbol')).get('replace')))
            var.put('metrics', var.get('getCharacterMetrics')((var.get('replace') or var.get('symbol')), var.get('font'), var.get('mode')))
            if var.get('metrics').neg():
                PyJsTempException = JsToPyException(var.get('Error').create(((((Js('Unsupported symbol ')+var.get('symbol'))+Js(' and font size '))+var.get('font'))+Js('.'))))
                raise PyJsTempException
            return var.get('metrics')
        PyJs_getMetrics_180_._set_name('getMetrics')
        var.put('delimiter_getMetrics', PyJs_getMetrics_180_)
        @Js
        def PyJs_styleWrap_181_(delim, toStyle, options, classes, this, arguments, var=var):
            var = Scope({'delim':delim, 'toStyle':toStyle, 'options':options, 'classes':classes, 'this':this, 'arguments':arguments, 'styleWrap':PyJs_styleWrap_181_}, var)
            var.registers(['toStyle', 'newOptions', 'delimSizeMultiplier', 'options', 'span', 'classes', 'delim'])
            var.put('newOptions', var.get('options').callprop('havingBaseStyle', var.get('toStyle')))
            var.put('span', var.get('buildCommon').callprop('makeSpan', var.get('classes').callprop('concat', var.get('newOptions').callprop('sizingClasses', var.get('options'))), Js([var.get('delim')]), var.get('options')))
            var.put('delimSizeMultiplier', (var.get('newOptions').get('sizeMultiplier')/var.get('options').get('sizeMultiplier')))
            var.get('span').put('height', var.get('delimSizeMultiplier'), '*')
            var.get('span').put('depth', var.get('delimSizeMultiplier'), '*')
            var.get('span').put('maxFontSize', var.get('newOptions').get('sizeMultiplier'))
            return var.get('span')
        PyJs_styleWrap_181_._set_name('styleWrap')
        var.put('delimiter_styleWrap', PyJs_styleWrap_181_)
        @Js
        def PyJs_centerSpan_182_(span, options, style, this, arguments, var=var):
            var = Scope({'span':span, 'options':options, 'style':style, 'this':this, 'arguments':arguments, 'centerSpan':PyJs_centerSpan_182_}, var)
            var.registers(['newOptions', 'options', 'shift', 'span', 'style'])
            var.put('newOptions', var.get('options').callprop('havingBaseStyle', var.get('style')))
            var.put('shift', ((Js(1.0)-(var.get('options').get('sizeMultiplier')/var.get('newOptions').get('sizeMultiplier')))*var.get('options').callprop('fontMetrics').get('axisHeight')))
            var.get('span').get('classes').callprop('push', Js('delimcenter'))
            var.get('span').get('style').put('top', (var.get('shift')+Js('em')))
            var.get('span').put('height', var.get('shift'), '-')
            var.get('span').put('depth', var.get('shift'), '+')
        PyJs_centerSpan_182_._set_name('centerSpan')
        var.put('centerSpan', PyJs_centerSpan_182_)
        @Js
        def PyJs_makeSmallDelim_183_(delim, style, center, options, mode, classes, this, arguments, var=var):
            var = Scope({'delim':delim, 'style':style, 'center':center, 'options':options, 'mode':mode, 'classes':classes, 'this':this, 'arguments':arguments, 'makeSmallDelim':PyJs_makeSmallDelim_183_}, var)
            var.registers(['mode', 'options', 'text', 'center', 'span', 'style', 'classes', 'delim'])
            var.put('text', var.get('buildCommon').callprop('makeSymbol', var.get('delim'), Js('Main-Regular'), var.get('mode'), var.get('options')))
            var.put('span', var.get('delimiter_styleWrap')(var.get('text'), var.get('style'), var.get('options'), var.get('classes')))
            if var.get('center'):
                var.get('centerSpan')(var.get('span'), var.get('options'), var.get('style'))
            return var.get('span')
        PyJs_makeSmallDelim_183_._set_name('makeSmallDelim')
        var.put('delimiter_makeSmallDelim', PyJs_makeSmallDelim_183_)
        @Js
        def PyJs_mathrmSize_184_(value, size, mode, options, this, arguments, var=var):
            var = Scope({'value':value, 'size':size, 'mode':mode, 'options':options, 'this':this, 'arguments':arguments, 'mathrmSize':PyJs_mathrmSize_184_}, var)
            var.registers(['options', 'size', 'value', 'mode'])
            return var.get('buildCommon').callprop('makeSymbol', var.get('value'), ((Js('Size')+var.get('size'))+Js('-Regular')), var.get('mode'), var.get('options'))
        PyJs_mathrmSize_184_._set_name('mathrmSize')
        var.put('delimiter_mathrmSize', PyJs_mathrmSize_184_)
        @Js
        def PyJs_makeLargeDelim_185_(delim, size, center, options, mode, classes, this, arguments, var=var):
            var = Scope({'delim':delim, 'size':size, 'center':center, 'options':options, 'mode':mode, 'classes':classes, 'this':this, 'arguments':arguments, 'makeLargeDelim':PyJs_makeLargeDelim_185_}, var)
            var.registers(['size', 'mode', 'options', 'center', 'span', 'inner', 'classes', 'delim'])
            var.put('inner', var.get('delimiter_mathrmSize')(var.get('delim'), var.get('size'), var.get('mode'), var.get('options')))
            var.put('span', var.get('delimiter_styleWrap')(var.get('buildCommon').callprop('makeSpan', Js([Js('delimsizing'), (Js('size')+var.get('size'))]), Js([var.get('inner')]), var.get('options')), var.get('src_Style').get('TEXT'), var.get('options'), var.get('classes')))
            if var.get('center'):
                var.get('centerSpan')(var.get('span'), var.get('options'), var.get('src_Style').get('TEXT'))
            return var.get('span')
        PyJs_makeLargeDelim_185_._set_name('makeLargeDelim')
        var.put('delimiter_makeLargeDelim', PyJs_makeLargeDelim_185_)
        @Js
        def PyJs_makeInner_186_(symbol, font, mode, this, arguments, var=var):
            var = Scope({'symbol':symbol, 'font':font, 'mode':mode, 'this':this, 'arguments':arguments, 'makeInner':PyJs_makeInner_186_}, var)
            var.registers(['mode', 'font', 'sizeClass', 'symbol', 'inner'])
            pass
            if PyJsStrictEq(var.get('font'),Js('Size1-Regular')):
                var.put('sizeClass', Js('delim-size1'))
            else:
                var.put('sizeClass', Js('delim-size4'))
            var.put('inner', var.get('buildCommon').callprop('makeSpan', Js([Js('delimsizinginner'), var.get('sizeClass')]), Js([var.get('buildCommon').callprop('makeSpan', Js([]), Js([var.get('buildCommon').callprop('makeSymbol', var.get('symbol'), var.get('font'), var.get('mode'))]))])))
            return Js({'type':Js('elem'),'elem':var.get('inner')})
        PyJs_makeInner_186_._set_name('makeInner')
        var.put('delimiter_makeInner', PyJs_makeInner_186_)
        @Js
        def PyJs_makeStackedDelim_187_(delim, heightTotal, center, options, mode, classes, this, arguments, var=var):
            var = Scope({'delim':delim, 'heightTotal':heightTotal, 'center':center, 'options':options, 'mode':mode, 'classes':classes, 'this':this, 'arguments':arguments, 'makeStackedDelim':PyJs_makeStackedDelim_187_}, var)
            var.registers(['minHeight', 'topHeightTotal', 'mode', '_i', 'realHeightTotal', 'bottomHeightTotal', 'inner', 'inners', 'i', 'middleMetrics', 'middleFactor', 'newOptions', 'options', 'top', 'middleHeightTotal', 'center', 'classes', 'axisHeight', '_i2', 'repeatMetrics', 'middle', 'bottom', 'bottomMetrics', 'repeat', 'topMetrics', 'delim', 'font', 'depth', 'heightTotal', 'repeatCount', 'repeatHeightTotal'])
            pass
            pass
            pass
            pass
            var.put('top', var.put('repeat', var.put('bottom', var.get('delim'))))
            var.put('middle', var.get(u"null"))
            var.put('font', Js('Size1-Regular'))
            if PyJsStrictEq(var.get('delim'),Js('\\uparrow')):
                var.put('repeat', var.put('bottom', Js('⏐')))
            else:
                if PyJsStrictEq(var.get('delim'),Js('\\Uparrow')):
                    var.put('repeat', var.put('bottom', Js('‖')))
                else:
                    if PyJsStrictEq(var.get('delim'),Js('\\downarrow')):
                        var.put('top', var.put('repeat', Js('⏐')))
                    else:
                        if PyJsStrictEq(var.get('delim'),Js('\\Downarrow')):
                            var.put('top', var.put('repeat', Js('‖')))
                        else:
                            if PyJsStrictEq(var.get('delim'),Js('\\updownarrow')):
                                var.put('top', Js('\\uparrow'))
                                var.put('repeat', Js('⏐'))
                                var.put('bottom', Js('\\downarrow'))
                            else:
                                if PyJsStrictEq(var.get('delim'),Js('\\Updownarrow')):
                                    var.put('top', Js('\\Uparrow'))
                                    var.put('repeat', Js('‖'))
                                    var.put('bottom', Js('\\Downarrow'))
                                else:
                                    if (PyJsStrictEq(var.get('delim'),Js('[')) or PyJsStrictEq(var.get('delim'),Js('\\lbrack'))):
                                        var.put('top', Js('⎡'))
                                        var.put('repeat', Js('⎢'))
                                        var.put('bottom', Js('⎣'))
                                        var.put('font', Js('Size4-Regular'))
                                    else:
                                        if (PyJsStrictEq(var.get('delim'),Js(']')) or PyJsStrictEq(var.get('delim'),Js('\\rbrack'))):
                                            var.put('top', Js('⎤'))
                                            var.put('repeat', Js('⎥'))
                                            var.put('bottom', Js('⎦'))
                                            var.put('font', Js('Size4-Regular'))
                                        else:
                                            if (PyJsStrictEq(var.get('delim'),Js('\\lfloor')) or PyJsStrictEq(var.get('delim'),Js('⌊'))):
                                                var.put('repeat', var.put('top', Js('⎢')))
                                                var.put('bottom', Js('⎣'))
                                                var.put('font', Js('Size4-Regular'))
                                            else:
                                                if (PyJsStrictEq(var.get('delim'),Js('\\lceil')) or PyJsStrictEq(var.get('delim'),Js('⌈'))):
                                                    var.put('top', Js('⎡'))
                                                    var.put('repeat', var.put('bottom', Js('⎢')))
                                                    var.put('font', Js('Size4-Regular'))
                                                else:
                                                    if (PyJsStrictEq(var.get('delim'),Js('\\rfloor')) or PyJsStrictEq(var.get('delim'),Js('⌋'))):
                                                        var.put('repeat', var.put('top', Js('⎥')))
                                                        var.put('bottom', Js('⎦'))
                                                        var.put('font', Js('Size4-Regular'))
                                                    else:
                                                        if (PyJsStrictEq(var.get('delim'),Js('\\rceil')) or PyJsStrictEq(var.get('delim'),Js('⌉'))):
                                                            var.put('top', Js('⎤'))
                                                            var.put('repeat', var.put('bottom', Js('⎥')))
                                                            var.put('font', Js('Size4-Regular'))
                                                        else:
                                                            if (PyJsStrictEq(var.get('delim'),Js('(')) or PyJsStrictEq(var.get('delim'),Js('\\lparen'))):
                                                                var.put('top', Js('⎛'))
                                                                var.put('repeat', Js('⎜'))
                                                                var.put('bottom', Js('⎝'))
                                                                var.put('font', Js('Size4-Regular'))
                                                            else:
                                                                if (PyJsStrictEq(var.get('delim'),Js(')')) or PyJsStrictEq(var.get('delim'),Js('\\rparen'))):
                                                                    var.put('top', Js('⎞'))
                                                                    var.put('repeat', Js('⎟'))
                                                                    var.put('bottom', Js('⎠'))
                                                                    var.put('font', Js('Size4-Regular'))
                                                                else:
                                                                    if (PyJsStrictEq(var.get('delim'),Js('\\{')) or PyJsStrictEq(var.get('delim'),Js('\\lbrace'))):
                                                                        var.put('top', Js('⎧'))
                                                                        var.put('middle', Js('⎨'))
                                                                        var.put('bottom', Js('⎩'))
                                                                        var.put('repeat', Js('⎪'))
                                                                        var.put('font', Js('Size4-Regular'))
                                                                    else:
                                                                        if (PyJsStrictEq(var.get('delim'),Js('\\}')) or PyJsStrictEq(var.get('delim'),Js('\\rbrace'))):
                                                                            var.put('top', Js('⎫'))
                                                                            var.put('middle', Js('⎬'))
                                                                            var.put('bottom', Js('⎭'))
                                                                            var.put('repeat', Js('⎪'))
                                                                            var.put('font', Js('Size4-Regular'))
                                                                        else:
                                                                            if (PyJsStrictEq(var.get('delim'),Js('\\lgroup')) or PyJsStrictEq(var.get('delim'),Js('⟮'))):
                                                                                var.put('top', Js('⎧'))
                                                                                var.put('bottom', Js('⎩'))
                                                                                var.put('repeat', Js('⎪'))
                                                                                var.put('font', Js('Size4-Regular'))
                                                                            else:
                                                                                if (PyJsStrictEq(var.get('delim'),Js('\\rgroup')) or PyJsStrictEq(var.get('delim'),Js('⟯'))):
                                                                                    var.put('top', Js('⎫'))
                                                                                    var.put('bottom', Js('⎭'))
                                                                                    var.put('repeat', Js('⎪'))
                                                                                    var.put('font', Js('Size4-Regular'))
                                                                                else:
                                                                                    if (PyJsStrictEq(var.get('delim'),Js('\\lmoustache')) or PyJsStrictEq(var.get('delim'),Js('⎰'))):
                                                                                        var.put('top', Js('⎧'))
                                                                                        var.put('bottom', Js('⎭'))
                                                                                        var.put('repeat', Js('⎪'))
                                                                                        var.put('font', Js('Size4-Regular'))
                                                                                    else:
                                                                                        if (PyJsStrictEq(var.get('delim'),Js('\\rmoustache')) or PyJsStrictEq(var.get('delim'),Js('⎱'))):
                                                                                            var.put('top', Js('⎫'))
                                                                                            var.put('bottom', Js('⎩'))
                                                                                            var.put('repeat', Js('⎪'))
                                                                                            var.put('font', Js('Size4-Regular'))
            var.put('topMetrics', var.get('delimiter_getMetrics')(var.get('top'), var.get('font'), var.get('mode')))
            var.put('topHeightTotal', (var.get('topMetrics').get('height')+var.get('topMetrics').get('depth')))
            var.put('repeatMetrics', var.get('delimiter_getMetrics')(var.get('repeat'), var.get('font'), var.get('mode')))
            var.put('repeatHeightTotal', (var.get('repeatMetrics').get('height')+var.get('repeatMetrics').get('depth')))
            var.put('bottomMetrics', var.get('delimiter_getMetrics')(var.get('bottom'), var.get('font'), var.get('mode')))
            var.put('bottomHeightTotal', (var.get('bottomMetrics').get('height')+var.get('bottomMetrics').get('depth')))
            var.put('middleHeightTotal', Js(0.0))
            var.put('middleFactor', Js(1.0))
            if PyJsStrictNeq(var.get('middle'),var.get(u"null")):
                var.put('middleMetrics', var.get('delimiter_getMetrics')(var.get('middle'), var.get('font'), var.get('mode')))
                var.put('middleHeightTotal', (var.get('middleMetrics').get('height')+var.get('middleMetrics').get('depth')))
                var.put('middleFactor', Js(2.0))
            var.put('minHeight', ((var.get('topHeightTotal')+var.get('bottomHeightTotal'))+var.get('middleHeightTotal')))
            var.put('repeatCount', var.get('Math').callprop('ceil', ((var.get('heightTotal')-var.get('minHeight'))/(var.get('middleFactor')*var.get('repeatHeightTotal')))))
            var.put('realHeightTotal', (var.get('minHeight')+((var.get('repeatCount')*var.get('middleFactor'))*var.get('repeatHeightTotal'))))
            var.put('axisHeight', var.get('options').callprop('fontMetrics').get('axisHeight'))
            if var.get('center'):
                var.put('axisHeight', var.get('options').get('sizeMultiplier'), '*')
            var.put('depth', ((var.get('realHeightTotal')/Js(2.0))-var.get('axisHeight')))
            var.put('inners', Js([]))
            var.get('inners').callprop('push', var.get('delimiter_makeInner')(var.get('bottom'), var.get('font'), var.get('mode')))
            if PyJsStrictEq(var.get('middle'),var.get(u"null")):
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('repeatCount')):
                    try:
                        var.get('inners').callprop('push', var.get('delimiter_makeInner')(var.get('repeat'), var.get('font'), var.get('mode')))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            else:
                #for JS loop
                var.put('_i', Js(0.0))
                while (var.get('_i')<var.get('repeatCount')):
                    try:
                        var.get('inners').callprop('push', var.get('delimiter_makeInner')(var.get('repeat'), var.get('font'), var.get('mode')))
                    finally:
                            (var.put('_i',Js(var.get('_i').to_number())+Js(1))-Js(1))
                var.get('inners').callprop('push', var.get('delimiter_makeInner')(var.get('middle'), var.get('font'), var.get('mode')))
                #for JS loop
                var.put('_i2', Js(0.0))
                while (var.get('_i2')<var.get('repeatCount')):
                    try:
                        var.get('inners').callprop('push', var.get('delimiter_makeInner')(var.get('repeat'), var.get('font'), var.get('mode')))
                    finally:
                            (var.put('_i2',Js(var.get('_i2').to_number())+Js(1))-Js(1))
            var.get('inners').callprop('push', var.get('delimiter_makeInner')(var.get('top'), var.get('font'), var.get('mode')))
            var.put('newOptions', var.get('options').callprop('havingBaseStyle', var.get('src_Style').get('TEXT')))
            var.put('inner', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('bottom'),'positionData':var.get('depth'),'children':var.get('inners')}), var.get('newOptions')))
            return var.get('delimiter_styleWrap')(var.get('buildCommon').callprop('makeSpan', Js([Js('delimsizing'), Js('mult')]), Js([var.get('inner')]), var.get('newOptions')), var.get('src_Style').get('TEXT'), var.get('options'), var.get('classes'))
        PyJs_makeStackedDelim_187_._set_name('makeStackedDelim')
        var.put('delimiter_makeStackedDelim', PyJs_makeStackedDelim_187_)
        var.put('vbPad', Js(80.0))
        var.put('emPad', Js(0.08))
        @Js
        def PyJs_sqrtSvg_188_(sqrtName, height, viewBoxHeight, options, this, arguments, var=var):
            var = Scope({'sqrtName':sqrtName, 'height':height, 'viewBoxHeight':viewBoxHeight, 'options':options, 'this':this, 'arguments':arguments, 'sqrtSvg':PyJs_sqrtSvg_188_}, var)
            var.registers(['pathNode', 'svg', 'viewBoxHeight', 'options', 'sqrtName', 'alternate', 'vertSegment', 'height'])
            pass
            if PyJsStrictEq(var.get('sqrtName'),Js('sqrtTall')):
                var.put('vertSegment', ((var.get('viewBoxHeight')-Js(54.0))-var.get('vbPad')))
                var.put('alternate', ((((((Js('M702 ')+var.get('vbPad'))+Js('H400000v40H742v'))+var.get('vertSegment'))+Js('l-4 4-4 4c-.667.7\n-2 1.5-4 2.5s-4.167 1.833-6.5 2.5-5.5 1-9.5 1h-12l-28-84c-16.667-52-96.667\n-294.333-240-727l-212 -643 -85 170c-4-3.333-8.333-7.667-13 -13l-13-13l77-155\n 77-156c66 199.333 139 419.667 219 661 l218 661zM702 '))+var.get('vbPad'))+Js('H400000v40H742z')))
            var.put('pathNode', var.get('domTree_PathNode').create(var.get('sqrtName'), var.get('alternate')))
            var.put('svg', var.get('SvgNode').create(Js([var.get('pathNode')]), Js({'width':Js('400em'),'height':(var.get('height')+Js('em')),'viewBox':(Js('0 0 400000 ')+var.get('viewBoxHeight')),'preserveAspectRatio':Js('xMinYMin slice')})))
            return var.get('buildCommon').callprop('makeSvgSpan', Js([Js('hide-tail')]), Js([var.get('svg')]), var.get('options'))
        PyJs_sqrtSvg_188_._set_name('sqrtSvg')
        var.put('delimiter_sqrtSvg', PyJs_sqrtSvg_188_)
        @Js
        def PyJs_makeSqrtImage_189_(height, options, this, arguments, var=var):
            var = Scope({'height':height, 'options':options, 'this':this, 'arguments':arguments, 'makeSqrtImage':PyJs_makeSqrtImage_189_}, var)
            var.registers(['viewBoxHeight', 'newOptions', 'spanHeight', 'texHeight', 'options', 'sizeMultiplier', 'advanceWidth', 'span', 'height', 'delim'])
            var.put('newOptions', var.get('options').callprop('havingBaseSizing'))
            var.put('delim', var.get('traverseSequence')(Js('\\surd'), (var.get('height')*var.get('newOptions').get('sizeMultiplier')), var.get('stackLargeDelimiterSequence'), var.get('newOptions')))
            var.put('sizeMultiplier', var.get('newOptions').get('sizeMultiplier'))
            pass
            var.put('spanHeight', Js(0.0))
            var.put('texHeight', Js(0.0))
            var.put('viewBoxHeight', Js(0.0))
            pass
            if PyJsStrictEq(var.get('delim').get('type'),Js('small')):
                var.put('viewBoxHeight', (Js(1000.0)+var.get('vbPad')))
                if (var.get('height')<Js(1.0)):
                    var.put('sizeMultiplier', Js(1.0))
                else:
                    if (var.get('height')<Js(1.4)):
                        var.put('sizeMultiplier', Js(0.7))
                var.put('spanHeight', ((Js(1.0)+var.get('emPad'))/var.get('sizeMultiplier')))
                var.put('texHeight', (Js(1.0)/var.get('sizeMultiplier')))
                var.put('span', var.get('delimiter_sqrtSvg')(Js('sqrtMain'), var.get('spanHeight'), var.get('viewBoxHeight'), var.get('options')))
                var.get('span').get('style').put('minWidth', Js('0.853em'))
                var.put('advanceWidth', (Js(0.833)/var.get('sizeMultiplier')))
            else:
                if PyJsStrictEq(var.get('delim').get('type'),Js('large')):
                    var.put('viewBoxHeight', ((Js(1000.0)+var.get('vbPad'))*var.get('sizeToMaxHeight').get(var.get('delim').get('size'))))
                    var.put('texHeight', (var.get('sizeToMaxHeight').get(var.get('delim').get('size'))/var.get('sizeMultiplier')))
                    var.put('spanHeight', ((var.get('sizeToMaxHeight').get(var.get('delim').get('size'))+var.get('emPad'))/var.get('sizeMultiplier')))
                    var.put('span', var.get('delimiter_sqrtSvg')((Js('sqrtSize')+var.get('delim').get('size')), var.get('spanHeight'), var.get('viewBoxHeight'), var.get('options')))
                    var.get('span').get('style').put('minWidth', Js('1.02em'))
                    var.put('advanceWidth', (Js(1.0)/var.get('sizeMultiplier')))
                else:
                    var.put('spanHeight', (var.get('height')+var.get('emPad')))
                    var.put('texHeight', var.get('height'))
                    var.put('viewBoxHeight', (var.get('Math').callprop('floor', (Js(1000.0)*var.get('height')))+var.get('vbPad')))
                    var.put('span', var.get('delimiter_sqrtSvg')(Js('sqrtTall'), var.get('spanHeight'), var.get('viewBoxHeight'), var.get('options')))
                    var.get('span').get('style').put('minWidth', Js('0.742em'))
                    var.put('advanceWidth', Js(1.056))
            var.get('span').put('height', var.get('texHeight'))
            var.get('span').get('style').put('height', (var.get('spanHeight')+Js('em')))
            return Js({'span':var.get('span'),'advanceWidth':var.get('advanceWidth'),'ruleWidth':(var.get('options').callprop('fontMetrics').get('sqrtRuleThickness')*var.get('sizeMultiplier'))})
        PyJs_makeSqrtImage_189_._set_name('makeSqrtImage')
        var.put('makeSqrtImage', PyJs_makeSqrtImage_189_)
        var.put('stackLargeDelimiters', Js([Js('('), Js('\\lparen'), Js(')'), Js('\\rparen'), Js('['), Js('\\lbrack'), Js(']'), Js('\\rbrack'), Js('\\{'), Js('\\lbrace'), Js('\\}'), Js('\\rbrace'), Js('\\lfloor'), Js('\\rfloor'), Js('⌊'), Js('⌋'), Js('\\lceil'), Js('\\rceil'), Js('⌈'), Js('⌉'), Js('\\surd')]))
        var.put('stackAlwaysDelimiters', Js([Js('\\uparrow'), Js('\\downarrow'), Js('\\updownarrow'), Js('\\Uparrow'), Js('\\Downarrow'), Js('\\Updownarrow'), Js('|'), Js('\\|'), Js('\\vert'), Js('\\Vert'), Js('\\lvert'), Js('\\rvert'), Js('\\lVert'), Js('\\rVert'), Js('\\lgroup'), Js('\\rgroup'), Js('⟮'), Js('⟯'), Js('\\lmoustache'), Js('\\rmoustache'), Js('⎰'), Js('⎱')]))
        var.put('stackNeverDelimiters', Js([Js('<'), Js('>'), Js('\\langle'), Js('\\rangle'), Js('/'), Js('\\backslash'), Js('\\lt'), Js('\\gt')]))
        var.put('sizeToMaxHeight', Js([Js(0.0), Js(1.2), Js(1.8), Js(2.4), Js(3.0)]))
        @Js
        def PyJs_makeSizedDelim_190_(delim, size, options, mode, classes, this, arguments, var=var):
            var = Scope({'delim':delim, 'size':size, 'options':options, 'mode':mode, 'classes':classes, 'this':this, 'arguments':arguments, 'makeSizedDelim':PyJs_makeSizedDelim_190_}, var)
            var.registers(['size', 'mode', 'options', 'classes', 'delim'])
            if ((PyJsStrictEq(var.get('delim'),Js('<')) or PyJsStrictEq(var.get('delim'),Js('\\lt'))) or PyJsStrictEq(var.get('delim'),Js('⟨'))):
                var.put('delim', Js('\\langle'))
            else:
                if ((PyJsStrictEq(var.get('delim'),Js('>')) or PyJsStrictEq(var.get('delim'),Js('\\gt'))) or PyJsStrictEq(var.get('delim'),Js('⟩'))):
                    var.put('delim', Js('\\rangle'))
            if (var.get('utils').callprop('contains', var.get('stackLargeDelimiters'), var.get('delim')) or var.get('utils').callprop('contains', var.get('stackNeverDelimiters'), var.get('delim'))):
                return var.get('delimiter_makeLargeDelim')(var.get('delim'), var.get('size'), Js(False), var.get('options'), var.get('mode'), var.get('classes'))
            else:
                if var.get('utils').callprop('contains', var.get('stackAlwaysDelimiters'), var.get('delim')):
                    return var.get('delimiter_makeStackedDelim')(var.get('delim'), var.get('sizeToMaxHeight').get(var.get('size')), Js(False), var.get('options'), var.get('mode'), var.get('classes'))
                else:
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js("Illegal delimiter: '")+var.get('delim'))+Js("'"))))
                    raise PyJsTempException
        PyJs_makeSizedDelim_190_._set_name('makeSizedDelim')
        var.put('delimiter_makeSizedDelim', PyJs_makeSizedDelim_190_)
        var.put('stackNeverDelimiterSequence', Js([Js({'type':Js('small'),'style':var.get('src_Style').get('SCRIPTSCRIPT')}), Js({'type':Js('small'),'style':var.get('src_Style').get('SCRIPT')}), Js({'type':Js('small'),'style':var.get('src_Style').get('TEXT')}), Js({'type':Js('large'),'size':Js(1.0)}), Js({'type':Js('large'),'size':Js(2.0)}), Js({'type':Js('large'),'size':Js(3.0)}), Js({'type':Js('large'),'size':Js(4.0)})]))
        var.put('stackAlwaysDelimiterSequence', Js([Js({'type':Js('small'),'style':var.get('src_Style').get('SCRIPTSCRIPT')}), Js({'type':Js('small'),'style':var.get('src_Style').get('SCRIPT')}), Js({'type':Js('small'),'style':var.get('src_Style').get('TEXT')}), Js({'type':Js('stack')})]))
        var.put('stackLargeDelimiterSequence', Js([Js({'type':Js('small'),'style':var.get('src_Style').get('SCRIPTSCRIPT')}), Js({'type':Js('small'),'style':var.get('src_Style').get('SCRIPT')}), Js({'type':Js('small'),'style':var.get('src_Style').get('TEXT')}), Js({'type':Js('large'),'size':Js(1.0)}), Js({'type':Js('large'),'size':Js(2.0)}), Js({'type':Js('large'),'size':Js(3.0)}), Js({'type':Js('large'),'size':Js(4.0)}), Js({'type':Js('stack')})]))
        @Js
        def PyJs_delimTypeToFont_191_(type, this, arguments, var=var):
            var = Scope({'type':type, 'this':this, 'arguments':arguments, 'delimTypeToFont':PyJs_delimTypeToFont_191_}, var)
            var.registers(['type'])
            if PyJsStrictEq(var.get('type').get('type'),Js('small')):
                return Js('Main-Regular')
            else:
                if PyJsStrictEq(var.get('type').get('type'),Js('large')):
                    return ((Js('Size')+var.get('type').get('size'))+Js('-Regular'))
                else:
                    if PyJsStrictEq(var.get('type').get('type'),Js('stack')):
                        return Js('Size4-Regular')
                    else:
                        PyJsTempException = JsToPyException(var.get('Error').create(((Js("Add support for delim type '")+var.get('type').get('type'))+Js("' here."))))
                        raise PyJsTempException
        PyJs_delimTypeToFont_191_._set_name('delimTypeToFont')
        var.put('delimTypeToFont', PyJs_delimTypeToFont_191_)
        @Js
        def PyJs_traverseSequence_192_(delim, height, sequence, options, this, arguments, var=var):
            var = Scope({'delim':delim, 'height':height, 'sequence':sequence, 'options':options, 'this':this, 'arguments':arguments, 'traverseSequence':PyJs_traverseSequence_192_}, var)
            var.registers(['heightDepth', 'i', 'newOptions', 'options', 'start', 'sequence', 'height', 'delim', 'metrics'])
            var.put('start', var.get('Math').callprop('min', Js(2.0), (Js(3.0)-var.get('options').get('style').get('size'))))
            #for JS loop
            var.put('i', var.get('start'))
            while (var.get('i')<var.get('sequence').get('length')):
                try:
                    if PyJsStrictEq(var.get('sequence').get(var.get('i')).get('type'),Js('stack')):
                        break
                    var.put('metrics', var.get('delimiter_getMetrics')(var.get('delim'), var.get('delimTypeToFont')(var.get('sequence').get(var.get('i'))), Js('math')))
                    var.put('heightDepth', (var.get('metrics').get('height')+var.get('metrics').get('depth')))
                    if PyJsStrictEq(var.get('sequence').get(var.get('i')).get('type'),Js('small')):
                        var.put('newOptions', var.get('options').callprop('havingBaseStyle', var.get('sequence').get(var.get('i')).get('style')))
                        var.put('heightDepth', var.get('newOptions').get('sizeMultiplier'), '*')
                    if (var.get('heightDepth')>var.get('height')):
                        return var.get('sequence').get(var.get('i'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            return var.get('sequence').get((var.get('sequence').get('length')-Js(1.0)))
        PyJs_traverseSequence_192_._set_name('traverseSequence')
        var.put('traverseSequence', PyJs_traverseSequence_192_)
        @Js
        def PyJs_makeCustomSizedDelim_193_(delim, height, center, options, mode, classes, this, arguments, var=var):
            var = Scope({'delim':delim, 'height':height, 'center':center, 'options':options, 'mode':mode, 'classes':classes, 'this':this, 'arguments':arguments, 'makeCustomSizedDelim':PyJs_makeCustomSizedDelim_193_}, var)
            var.registers(['mode', 'options', 'center', 'sequence', 'delimType', 'height', 'classes', 'delim'])
            if ((PyJsStrictEq(var.get('delim'),Js('<')) or PyJsStrictEq(var.get('delim'),Js('\\lt'))) or PyJsStrictEq(var.get('delim'),Js('⟨'))):
                var.put('delim', Js('\\langle'))
            else:
                if ((PyJsStrictEq(var.get('delim'),Js('>')) or PyJsStrictEq(var.get('delim'),Js('\\gt'))) or PyJsStrictEq(var.get('delim'),Js('⟩'))):
                    var.put('delim', Js('\\rangle'))
            pass
            if var.get('utils').callprop('contains', var.get('stackNeverDelimiters'), var.get('delim')):
                var.put('sequence', var.get('stackNeverDelimiterSequence'))
            else:
                if var.get('utils').callprop('contains', var.get('stackLargeDelimiters'), var.get('delim')):
                    var.put('sequence', var.get('stackLargeDelimiterSequence'))
                else:
                    var.put('sequence', var.get('stackAlwaysDelimiterSequence'))
            var.put('delimType', var.get('traverseSequence')(var.get('delim'), var.get('height'), var.get('sequence'), var.get('options')))
            if PyJsStrictEq(var.get('delimType').get('type'),Js('small')):
                return var.get('delimiter_makeSmallDelim')(var.get('delim'), var.get('delimType').get('style'), var.get('center'), var.get('options'), var.get('mode'), var.get('classes'))
            else:
                if PyJsStrictEq(var.get('delimType').get('type'),Js('large')):
                    return var.get('delimiter_makeLargeDelim')(var.get('delim'), var.get('delimType').get('size'), var.get('center'), var.get('options'), var.get('mode'), var.get('classes'))
                else:
                    return var.get('delimiter_makeStackedDelim')(var.get('delim'), var.get('height'), var.get('center'), var.get('options'), var.get('mode'), var.get('classes'))
        PyJs_makeCustomSizedDelim_193_._set_name('makeCustomSizedDelim')
        var.put('delimiter_makeCustomSizedDelim', PyJs_makeCustomSizedDelim_193_)
        @Js
        def PyJs_makeLeftRightDelim_194_(delim, height, depth, options, mode, classes, this, arguments, var=var):
            var = Scope({'delim':delim, 'height':height, 'depth':depth, 'options':options, 'mode':mode, 'classes':classes, 'this':this, 'arguments':arguments, 'makeLeftRightDelim':PyJs_makeLeftRightDelim_194_}, var)
            var.registers(['delimiterFactor', 'axisHeight', 'mode', 'depth', 'options', 'maxDistFromAxis', 'totalHeight', 'delimiterExtend', 'height', 'classes', 'delim'])
            var.put('axisHeight', (var.get('options').callprop('fontMetrics').get('axisHeight')*var.get('options').get('sizeMultiplier')))
            var.put('delimiterFactor', Js(901.0))
            var.put('delimiterExtend', (Js(5.0)/var.get('options').callprop('fontMetrics').get('ptPerEm')))
            var.put('maxDistFromAxis', var.get('Math').callprop('max', (var.get('height')-var.get('axisHeight')), (var.get('depth')+var.get('axisHeight'))))
            var.put('totalHeight', var.get('Math').callprop('max', ((var.get('maxDistFromAxis')/Js(500.0))*var.get('delimiterFactor')), ((Js(2.0)*var.get('maxDistFromAxis'))-var.get('delimiterExtend'))))
            return var.get('delimiter_makeCustomSizedDelim')(var.get('delim'), var.get('totalHeight'), Js(True), var.get('options'), var.get('mode'), var.get('classes'))
        PyJs_makeLeftRightDelim_194_._set_name('makeLeftRightDelim')
        var.put('makeLeftRightDelim', PyJs_makeLeftRightDelim_194_)
        var.put('delimiter', Js({'sqrtImage':var.get('makeSqrtImage'),'sizedDelim':var.get('delimiter_makeSizedDelim'),'customSizedDelim':var.get('delimiter_makeCustomSizedDelim'),'leftRightDelim':var.get('makeLeftRightDelim')}))
        var.put('delimiterSizes', Js({'\\bigl':Js({'mclass':Js('mopen'),'size':Js(1.0)}),'\\Bigl':Js({'mclass':Js('mopen'),'size':Js(2.0)}),'\\biggl':Js({'mclass':Js('mopen'),'size':Js(3.0)}),'\\Biggl':Js({'mclass':Js('mopen'),'size':Js(4.0)}),'\\bigr':Js({'mclass':Js('mclose'),'size':Js(1.0)}),'\\Bigr':Js({'mclass':Js('mclose'),'size':Js(2.0)}),'\\biggr':Js({'mclass':Js('mclose'),'size':Js(3.0)}),'\\Biggr':Js({'mclass':Js('mclose'),'size':Js(4.0)}),'\\bigm':Js({'mclass':Js('mrel'),'size':Js(1.0)}),'\\Bigm':Js({'mclass':Js('mrel'),'size':Js(2.0)}),'\\biggm':Js({'mclass':Js('mrel'),'size':Js(3.0)}),'\\Biggm':Js({'mclass':Js('mrel'),'size':Js(4.0)}),'\\big':Js({'mclass':Js('mord'),'size':Js(1.0)}),'\\Big':Js({'mclass':Js('mord'),'size':Js(2.0)}),'\\bigg':Js({'mclass':Js('mord'),'size':Js(3.0)}),'\\Bigg':Js({'mclass':Js('mord'),'size':Js(4.0)})}))
        var.put('delimiters', Js([Js('('), Js('\\lparen'), Js(')'), Js('\\rparen'), Js('['), Js('\\lbrack'), Js(']'), Js('\\rbrack'), Js('\\{'), Js('\\lbrace'), Js('\\}'), Js('\\rbrace'), Js('\\lfloor'), Js('\\rfloor'), Js('⌊'), Js('⌋'), Js('\\lceil'), Js('\\rceil'), Js('⌈'), Js('⌉'), Js('<'), Js('>'), Js('\\langle'), Js('⟨'), Js('\\rangle'), Js('⟩'), Js('\\lt'), Js('\\gt'), Js('\\lvert'), Js('\\rvert'), Js('\\lVert'), Js('\\rVert'), Js('\\lgroup'), Js('\\rgroup'), Js('⟮'), Js('⟯'), Js('\\lmoustache'), Js('\\rmoustache'), Js('⎰'), Js('⎱'), Js('/'), Js('\\backslash'), Js('|'), Js('\\vert'), Js('\\|'), Js('\\Vert'), Js('\\uparrow'), Js('\\Uparrow'), Js('\\downarrow'), Js('\\Downarrow'), Js('\\updownarrow'), Js('\\Updownarrow'), Js('.')]))
        pass
        def PyJs_LONG_198_(var=var):
            @Js
            def PyJs_handler_195_(context, args, this, arguments, var=var):
                var = Scope({'context':context, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_195_}, var)
                var.registers(['context', 'delim', 'args'])
                var.put('delim', var.get('checkDelimiter')(var.get('args').get('0'), var.get('context')))
                return Js({'type':Js('delimsizing'),'mode':var.get('context').get('parser').get('mode'),'size':var.get('delimiterSizes').get(var.get('context').get('funcName')).get('size'),'mclass':var.get('delimiterSizes').get(var.get('context').get('funcName')).get('mclass'),'delim':var.get('delim').get('text')})
            PyJs_handler_195_._set_name('handler')
            @Js
            def PyJs_htmlBuilder_196_(group, options, this, arguments, var=var):
                var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_196_}, var)
                var.registers(['group', 'options'])
                if PyJsStrictEq(var.get('group').get('delim'),Js('.')):
                    return var.get('buildCommon').callprop('makeSpan', Js([var.get('group').get('mclass')]))
                return var.get('delimiter').callprop('sizedDelim', var.get('group').get('delim'), var.get('group').get('size'), var.get('options'), var.get('group').get('mode'), Js([var.get('group').get('mclass')]))
            PyJs_htmlBuilder_196_._set_name('htmlBuilder')
            @Js
            def PyJs_mathmlBuilder_197_(group, this, arguments, var=var):
                var = Scope({'group':group, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_197_}, var)
                var.registers(['node', 'group', 'children'])
                var.put('children', Js([]))
                if PyJsStrictNeq(var.get('group').get('delim'),Js('.')):
                    var.get('children').callprop('push', var.get('buildMathML_makeText')(var.get('group').get('delim'), var.get('group').get('mode')))
                var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mo'), var.get('children')))
                if (PyJsStrictEq(var.get('group').get('mclass'),Js('mopen')) or PyJsStrictEq(var.get('group').get('mclass'),Js('mclose'))):
                    var.get('node').callprop('setAttribute', Js('fence'), Js('true'))
                else:
                    var.get('node').callprop('setAttribute', Js('fence'), Js('false'))
                return var.get('node')
            PyJs_mathmlBuilder_197_._set_name('mathmlBuilder')
            return var.get('defineFunction')(Js({'type':Js('delimsizing'),'names':Js([Js('\\bigl'), Js('\\Bigl'), Js('\\biggl'), Js('\\Biggl'), Js('\\bigr'), Js('\\Bigr'), Js('\\biggr'), Js('\\Biggr'), Js('\\bigm'), Js('\\Bigm'), Js('\\biggm'), Js('\\Biggm'), Js('\\big'), Js('\\Big'), Js('\\bigg'), Js('\\Bigg')]),'props':Js({'numArgs':Js(1.0)}),'handler':PyJs_handler_195_,'htmlBuilder':PyJs_htmlBuilder_196_,'mathmlBuilder':PyJs_mathmlBuilder_197_}))
        PyJs_LONG_198_()
        pass
        @Js
        def PyJs_handler_199_(context, args, this, arguments, var=var):
            var = Scope({'context':context, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_199_}, var)
            var.registers(['context', 'args'])
            return Js({'type':Js('leftright-right'),'mode':var.get('context').get('parser').get('mode'),'delim':var.get('checkDelimiter')(var.get('args').get('0'), var.get('context')).get('text')})
        PyJs_handler_199_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('leftright-right'),'names':Js([Js('\\right')]),'props':Js({'numArgs':Js(1.0)}),'handler':PyJs_handler_199_}))
        @Js
        def PyJs_handler_200_(context, args, this, arguments, var=var):
            var = Scope({'context':context, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_200_}, var)
            var.registers(['body', 'context', 'right', 'args', 'parser', 'delim'])
            var.put('delim', var.get('checkDelimiter')(var.get('args').get('0'), var.get('context')))
            var.put('parser', var.get('context').get('parser'))
            var.get('parser').put('leftrightDepth',Js(var.get('parser').get('leftrightDepth').to_number())+Js(1))
            var.put('body', var.get('parser').callprop('parseExpression', Js(False)))
            var.get('parser').put('leftrightDepth',Js(var.get('parser').get('leftrightDepth').to_number())-Js(1))
            var.get('parser').callprop('expect', Js('\\right'), Js(False))
            var.put('right', var.get('assertNodeType')(var.get('parser').callprop('parseFunction'), Js('leftright-right')))
            return Js({'type':Js('leftright'),'mode':var.get('parser').get('mode'),'body':var.get('body'),'left':var.get('delim').get('text'),'right':var.get('right').get('delim')})
        PyJs_handler_200_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_201_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_201_}, var)
            var.registers(['i', 'innerHeight', 'middleDelim', 'group', 'hadMiddle', '_i', 'options', 'leftDelim', 'innerDepth', 'rightDelim', 'isMiddle', 'inner'])
            var.get('assertParsed')(var.get('group'))
            var.put('inner', var.get('buildHTML_buildExpression')(var.get('group').get('body'), var.get('options'), Js(True), Js([Js('mopen'), Js('mclose')])))
            var.put('innerHeight', Js(0.0))
            var.put('innerDepth', Js(0.0))
            var.put('hadMiddle', Js(False))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('inner').get('length')):
                try:
                    if var.get('inner').get(var.get('i')).get('isMiddle'):
                        var.put('hadMiddle', Js(True))
                    else:
                        var.put('innerHeight', var.get('Math').callprop('max', var.get('inner').get(var.get('i')).get('height'), var.get('innerHeight')))
                        var.put('innerDepth', var.get('Math').callprop('max', var.get('inner').get(var.get('i')).get('depth'), var.get('innerDepth')))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('innerHeight', var.get('options').get('sizeMultiplier'), '*')
            var.put('innerDepth', var.get('options').get('sizeMultiplier'), '*')
            pass
            if PyJsStrictEq(var.get('group').get('left'),Js('.')):
                var.put('leftDelim', var.get('makeNullDelimiter')(var.get('options'), Js([Js('mopen')])))
            else:
                var.put('leftDelim', var.get('delimiter').callprop('leftRightDelim', var.get('group').get('left'), var.get('innerHeight'), var.get('innerDepth'), var.get('options'), var.get('group').get('mode'), Js([Js('mopen')])))
            var.get('inner').callprop('unshift', var.get('leftDelim'))
            if var.get('hadMiddle'):
                #for JS loop
                var.put('_i', Js(1.0))
                while (var.get('_i')<var.get('inner').get('length')):
                    try:
                        var.put('middleDelim', var.get('inner').get(var.get('_i')))
                        var.put('isMiddle', var.get('middleDelim').get('isMiddle'))
                        if var.get('isMiddle'):
                            var.get('inner').put(var.get('_i'), var.get('delimiter').callprop('leftRightDelim', var.get('isMiddle').get('delim'), var.get('innerHeight'), var.get('innerDepth'), var.get('isMiddle').get('options'), var.get('group').get('mode'), Js([])))
                    finally:
                            (var.put('_i',Js(var.get('_i').to_number())+Js(1))-Js(1))
            pass
            if PyJsStrictEq(var.get('group').get('right'),Js('.')):
                var.put('rightDelim', var.get('makeNullDelimiter')(var.get('options'), Js([Js('mclose')])))
            else:
                var.put('rightDelim', var.get('delimiter').callprop('leftRightDelim', var.get('group').get('right'), var.get('innerHeight'), var.get('innerDepth'), var.get('options'), var.get('group').get('mode'), Js([Js('mclose')])))
            var.get('inner').callprop('push', var.get('rightDelim'))
            return var.get('buildCommon').callprop('makeSpan', Js([Js('minner')]), var.get('inner'), var.get('options'))
        PyJs_htmlBuilder_201_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_202_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_202_}, var)
            var.registers(['rightNode', 'leftNode', 'group', 'options', 'inner'])
            var.get('assertParsed')(var.get('group'))
            var.put('inner', var.get('buildMathML_buildExpression')(var.get('group').get('body'), var.get('options')))
            if PyJsStrictNeq(var.get('group').get('left'),Js('.')):
                var.put('leftNode', var.get('mathMLTree').get('MathNode').create(Js('mo'), Js([var.get('buildMathML_makeText')(var.get('group').get('left'), var.get('group').get('mode'))])))
                var.get('leftNode').callprop('setAttribute', Js('fence'), Js('true'))
                var.get('inner').callprop('unshift', var.get('leftNode'))
            if PyJsStrictNeq(var.get('group').get('right'),Js('.')):
                var.put('rightNode', var.get('mathMLTree').get('MathNode').create(Js('mo'), Js([var.get('buildMathML_makeText')(var.get('group').get('right'), var.get('group').get('mode'))])))
                var.get('rightNode').callprop('setAttribute', Js('fence'), Js('true'))
                var.get('inner').callprop('push', var.get('rightNode'))
            return var.get('buildMathML_makeRow')(var.get('inner'))
        PyJs_mathmlBuilder_202_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('leftright'),'names':Js([Js('\\left')]),'props':Js({'numArgs':Js(1.0)}),'handler':PyJs_handler_200_,'htmlBuilder':PyJs_htmlBuilder_201_,'mathmlBuilder':PyJs_mathmlBuilder_202_}))
        @Js
        def PyJs_handler_203_(context, args, this, arguments, var=var):
            var = Scope({'context':context, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_203_}, var)
            var.registers(['context', 'delim', 'args'])
            var.put('delim', var.get('checkDelimiter')(var.get('args').get('0'), var.get('context')))
            if var.get('context').get('parser').get('leftrightDepth').neg():
                PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('\\middle without preceding \\left'), var.get('delim')))
                raise PyJsTempException
            return Js({'type':Js('middle'),'mode':var.get('context').get('parser').get('mode'),'delim':var.get('delim').get('text')})
        PyJs_handler_203_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_204_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_204_}, var)
            var.registers(['isMiddle', 'group', 'options', 'middleDelim'])
            pass
            if PyJsStrictEq(var.get('group').get('delim'),Js('.')):
                var.put('middleDelim', var.get('makeNullDelimiter')(var.get('options'), Js([])))
            else:
                var.put('middleDelim', var.get('delimiter').callprop('sizedDelim', var.get('group').get('delim'), Js(1.0), var.get('options'), var.get('group').get('mode'), Js([])))
                var.put('isMiddle', Js({'delim':var.get('group').get('delim'),'options':var.get('options')}))
                var.get('middleDelim').put('isMiddle', var.get('isMiddle'))
            return var.get('middleDelim')
        PyJs_htmlBuilder_204_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_205_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_205_}, var)
            var.registers(['group', 'textNode', 'middleNode', 'options'])
            var.put('textNode', (var.get('buildMathML_makeText')(Js('|'), Js('text')) if (PyJsStrictEq(var.get('group').get('delim'),Js('\\vert')) or PyJsStrictEq(var.get('group').get('delim'),Js('|'))) else var.get('buildMathML_makeText')(var.get('group').get('delim'), var.get('group').get('mode'))))
            var.put('middleNode', var.get('mathMLTree').get('MathNode').create(Js('mo'), Js([var.get('textNode')])))
            var.get('middleNode').callprop('setAttribute', Js('fence'), Js('true'))
            var.get('middleNode').callprop('setAttribute', Js('lspace'), Js('0.05em'))
            var.get('middleNode').callprop('setAttribute', Js('rspace'), Js('0.05em'))
            return var.get('middleNode')
        PyJs_mathmlBuilder_205_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('middle'),'names':Js([Js('\\middle')]),'props':Js({'numArgs':Js(1.0)}),'handler':PyJs_handler_203_,'htmlBuilder':PyJs_htmlBuilder_204_,'mathmlBuilder':PyJs_mathmlBuilder_205_}))
        @Js
        def PyJs_htmlBuilder_206_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_206_}, var)
            var.registers(['label', 'img', 'isSingleChar', 'group', 'options', 'scale', 'imgShift', 'inner', 'vlist', 'vertPad'])
            var.put('inner', var.get('buildCommon').callprop('wrapFragment', var.get('buildHTML_buildGroup')(var.get('group').get('body'), var.get('options')), var.get('options')))
            var.put('label', var.get('group').get('label').callprop('substr', Js(1.0)))
            var.put('scale', var.get('options').get('sizeMultiplier'))
            pass
            var.put('imgShift', Js(0.0))
            var.put('isSingleChar', var.get('utils').callprop('isCharacterBox', var.get('group').get('body')))
            if PyJsStrictEq(var.get('label'),Js('sout')):
                var.put('img', var.get('buildCommon').callprop('makeSpan', Js([Js('stretchy'), Js('sout')])))
                var.get('img').put('height', (var.get('options').callprop('fontMetrics').get('defaultRuleThickness')/var.get('scale')))
                var.put('imgShift', ((-Js(0.5))*var.get('options').callprop('fontMetrics').get('xHeight')))
            else:
                if JsRegExp('/cancel/').callprop('test', var.get('label')):
                    if var.get('isSingleChar').neg():
                        var.get('inner').get('classes').callprop('push', Js('cancel-pad'))
                else:
                    var.get('inner').get('classes').callprop('push', Js('boxpad'))
                var.put('vertPad', Js(0.0))
                if JsRegExp('/box/').callprop('test', var.get('label')):
                    var.put('vertPad', (Js(0.3) if PyJsStrictEq(var.get('label'),Js('colorbox')) else Js(0.34)))
                else:
                    var.put('vertPad', (Js(0.2) if var.get('isSingleChar') else Js(0.0)))
                var.put('img', var.get('stretchy').callprop('encloseSpan', var.get('inner'), var.get('label'), var.get('vertPad'), var.get('options')))
                var.put('imgShift', (var.get('inner').get('depth')+var.get('vertPad')))
                if var.get('group').get('backgroundColor'):
                    var.get('img').get('style').put('backgroundColor', var.get('group').get('backgroundColor'))
                    if var.get('group').get('borderColor'):
                        var.get('img').get('style').put('borderColor', var.get('group').get('borderColor'))
            pass
            if var.get('group').get('backgroundColor'):
                var.put('vlist', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('individualShift'),'children':Js([Js({'type':Js('elem'),'elem':var.get('img'),'shift':var.get('imgShift')}), Js({'type':Js('elem'),'elem':var.get('inner'),'shift':Js(0.0)})])}), var.get('options')))
            else:
                var.put('vlist', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('individualShift'),'children':Js([Js({'type':Js('elem'),'elem':var.get('inner'),'shift':Js(0.0)}), Js({'type':Js('elem'),'elem':var.get('img'),'shift':var.get('imgShift'),'wrapperClasses':(Js([Js('svg-align')]) if JsRegExp('/cancel/').callprop('test', var.get('label')) else Js([]))})])}), var.get('options')))
            if JsRegExp('/cancel/').callprop('test', var.get('label')):
                var.get('vlist').put('height', var.get('inner').get('height'))
                var.get('vlist').put('depth', var.get('inner').get('depth'))
            if (JsRegExp('/cancel/').callprop('test', var.get('label')) and var.get('isSingleChar').neg()):
                return var.get('buildCommon').callprop('makeSpan', Js([Js('mord'), Js('cancel-lap')]), Js([var.get('vlist')]), var.get('options'))
            else:
                return var.get('buildCommon').callprop('makeSpan', Js([Js('mord')]), Js([var.get('vlist')]), var.get('options'))
        PyJs_htmlBuilder_206_._set_name('htmlBuilder')
        var.put('enclose_htmlBuilder', PyJs_htmlBuilder_206_)
        @Js
        def PyJs_mathmlBuilder_207_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_207_}, var)
            var.registers(['node', 'group', 'options', 'thk'])
            var.put('node', var.get('mathMLTree').get('MathNode').create((Js('mpadded') if (var.get('group').get('label').callprop('indexOf', Js('colorbox'))>(-Js(1.0))) else Js('menclose')), Js([var.get('buildMathML_buildGroup')(var.get('group').get('body'), var.get('options'))])))
            while 1:
                SWITCHED = False
                CONDITION = (var.get('group').get('label'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\cancel')):
                    SWITCHED = True
                    var.get('node').callprop('setAttribute', Js('notation'), Js('updiagonalstrike'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\bcancel')):
                    SWITCHED = True
                    var.get('node').callprop('setAttribute', Js('notation'), Js('downdiagonalstrike'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\sout')):
                    SWITCHED = True
                    var.get('node').callprop('setAttribute', Js('notation'), Js('horizontalstrike'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\fbox')):
                    SWITCHED = True
                    var.get('node').callprop('setAttribute', Js('notation'), Js('box'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\fcolorbox')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\colorbox')):
                    SWITCHED = True
                    var.get('node').callprop('setAttribute', Js('width'), Js('+6pt'))
                    var.get('node').callprop('setAttribute', Js('height'), Js('+6pt'))
                    var.get('node').callprop('setAttribute', Js('lspace'), Js('3pt'))
                    var.get('node').callprop('setAttribute', Js('voffset'), Js('3pt'))
                    if PyJsStrictEq(var.get('group').get('label'),Js('\\fcolorbox')):
                        var.put('thk', var.get('options').callprop('fontMetrics').get('defaultRuleThickness'))
                        var.get('node').callprop('setAttribute', Js('style'), (((Js('border: ')+var.get('thk'))+Js('em solid '))+var.get('String')(var.get('group').get('borderColor'))))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\xcancel')):
                    SWITCHED = True
                    var.get('node').callprop('setAttribute', Js('notation'), Js('updiagonalstrike downdiagonalstrike'))
                    break
                SWITCHED = True
                break
            if var.get('group').get('backgroundColor'):
                var.get('node').callprop('setAttribute', Js('mathbackground'), var.get('group').get('backgroundColor'))
            return var.get('node')
        PyJs_mathmlBuilder_207_._set_name('mathmlBuilder')
        var.put('enclose_mathmlBuilder', PyJs_mathmlBuilder_207_)
        @Js
        def PyJs_handler_208_(_ref, args, optArgs, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'optArgs':optArgs, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_208_}, var)
            var.registers(['funcName', 'color', 'body', 'optArgs', '_ref', 'args', 'parser'])
            var.put('parser', var.get('_ref').get('parser'))
            var.put('funcName', var.get('_ref').get('funcName'))
            var.put('color', var.get('assertNodeType')(var.get('args').get('0'), Js('color-token')).get('color'))
            var.put('body', var.get('args').get('1'))
            return Js({'type':Js('enclose'),'mode':var.get('parser').get('mode'),'label':var.get('funcName'),'backgroundColor':var.get('color'),'body':var.get('body')})
        PyJs_handler_208_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('enclose'),'names':Js([Js('\\colorbox')]),'props':Js({'numArgs':Js(2.0),'allowedInText':Js(True),'greediness':Js(3.0),'argTypes':Js([Js('color'), Js('text')])}),'handler':PyJs_handler_208_,'htmlBuilder':var.get('enclose_htmlBuilder'),'mathmlBuilder':var.get('enclose_mathmlBuilder')}))
        @Js
        def PyJs_handler_209_(_ref2, args, optArgs, this, arguments, var=var):
            var = Scope({'_ref2':_ref2, 'args':args, 'optArgs':optArgs, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_209_}, var)
            var.registers(['funcName', 'backgroundColor', 'body', 'borderColor', 'optArgs', 'args', 'parser', '_ref2'])
            var.put('parser', var.get('_ref2').get('parser'))
            var.put('funcName', var.get('_ref2').get('funcName'))
            var.put('borderColor', var.get('assertNodeType')(var.get('args').get('0'), Js('color-token')).get('color'))
            var.put('backgroundColor', var.get('assertNodeType')(var.get('args').get('1'), Js('color-token')).get('color'))
            var.put('body', var.get('args').get('2'))
            return Js({'type':Js('enclose'),'mode':var.get('parser').get('mode'),'label':var.get('funcName'),'backgroundColor':var.get('backgroundColor'),'borderColor':var.get('borderColor'),'body':var.get('body')})
        PyJs_handler_209_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('enclose'),'names':Js([Js('\\fcolorbox')]),'props':Js({'numArgs':Js(3.0),'allowedInText':Js(True),'greediness':Js(3.0),'argTypes':Js([Js('color'), Js('color'), Js('text')])}),'handler':PyJs_handler_209_,'htmlBuilder':var.get('enclose_htmlBuilder'),'mathmlBuilder':var.get('enclose_mathmlBuilder')}))
        @Js
        def PyJs_handler_210_(_ref3, args, this, arguments, var=var):
            var = Scope({'_ref3':_ref3, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_210_}, var)
            var.registers(['parser', '_ref3', 'args'])
            var.put('parser', var.get('_ref3').get('parser'))
            return Js({'type':Js('enclose'),'mode':var.get('parser').get('mode'),'label':Js('\\fbox'),'body':var.get('args').get('0')})
        PyJs_handler_210_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('enclose'),'names':Js([Js('\\fbox')]),'props':Js({'numArgs':Js(1.0),'argTypes':Js([Js('text')]),'allowedInText':Js(True)}),'handler':PyJs_handler_210_}))
        @Js
        def PyJs_handler_211_(_ref4, args, optArgs, this, arguments, var=var):
            var = Scope({'_ref4':_ref4, 'args':args, 'optArgs':optArgs, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_211_}, var)
            var.registers(['funcName', '_ref4', 'body', 'optArgs', 'args', 'parser'])
            var.put('parser', var.get('_ref4').get('parser'))
            var.put('funcName', var.get('_ref4').get('funcName'))
            var.put('body', var.get('args').get('0'))
            return Js({'type':Js('enclose'),'mode':var.get('parser').get('mode'),'label':var.get('funcName'),'body':var.get('body')})
        PyJs_handler_211_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('enclose'),'names':Js([Js('\\cancel'), Js('\\bcancel'), Js('\\xcancel'), Js('\\sout')]),'props':Js({'numArgs':Js(1.0)}),'handler':PyJs_handler_211_,'htmlBuilder':var.get('enclose_htmlBuilder'),'mathmlBuilder':var.get('enclose_mathmlBuilder')}))
        var.put('_environments', Js({}))
        pass
        pass
        pass
        pass
        @Js
        def PyJs_htmlBuilder_212_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_212_}, var)
            var.registers(['elem', 'arrayskip', 'arraycolsep', 'line', 'colDescr', 'r', 'colSep', 'outrow', 'col', 'vListElems', 'body', 'options', 'cols', 'colDescrNum', 'separator', '_separator', 'hline', 'rowGap', 'dashes', 'setHLinePos', 'totalHeight', 'gap', 'row', 'jot', 'offset', 'colDescriptions', 'nc', 'inrow', 'c', 'nr', 'firstSeparator', 'arstrutHeight', 'arstrutDepth', 'depth', 'lineShift', 'group', 'shift', 'baselineskip', 'hLinesBeforeRow', 'sepwidth', 'height', 'pt', 'hlines', 'elt'])
            @Js
            def PyJsHoisted_setHLinePos_(hlinesInGap, this, arguments, var=var):
                var = Scope({'hlinesInGap':hlinesInGap, 'this':this, 'arguments':arguments}, var)
                var.registers(['hlinesInGap', 'i'])
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('hlinesInGap').get('length')):
                    try:
                        if (var.get('i')>Js(0.0)):
                            var.put('totalHeight', Js(0.25), '+')
                        var.get('hlines').callprop('push', Js({'pos':var.get('totalHeight'),'isDashed':var.get('hlinesInGap').get(var.get('i'))}))
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
            PyJsHoisted_setHLinePos_.func_name = 'setHLinePos'
            var.put('setHLinePos', PyJsHoisted_setHLinePos_)
            pass
            pass
            var.put('nr', var.get('group').get('body').get('length'))
            var.put('hLinesBeforeRow', var.get('group').get('hLinesBeforeRow'))
            var.put('nc', Js(0.0))
            var.put('body', var.get('Array').create(var.get('nr')))
            var.put('hlines', Js([]))
            var.put('pt', (Js(1.0)/var.get('options').callprop('fontMetrics').get('ptPerEm')))
            var.put('arraycolsep', (Js(5.0)*var.get('pt')))
            var.put('baselineskip', (Js(12.0)*var.get('pt')))
            var.put('jot', (Js(3.0)*var.get('pt')))
            var.put('arrayskip', (var.get('group').get('arraystretch')*var.get('baselineskip')))
            var.put('arstrutHeight', (Js(0.7)*var.get('arrayskip')))
            var.put('arstrutDepth', (Js(0.3)*var.get('arrayskip')))
            var.put('totalHeight', Js(0.0))
            pass
            var.get('setHLinePos')(var.get('hLinesBeforeRow').get('0'))
            #for JS loop
            var.put('r', Js(0.0))
            while (var.get('r')<var.get('group').get('body').get('length')):
                try:
                    var.put('inrow', var.get('group').get('body').get(var.get('r')))
                    var.put('height', var.get('arstrutHeight'))
                    var.put('depth', var.get('arstrutDepth'))
                    if (var.get('nc')<var.get('inrow').get('length')):
                        var.put('nc', var.get('inrow').get('length'))
                    var.put('outrow', var.get('Array').create(var.get('inrow').get('length')))
                    #for JS loop
                    var.put('c', Js(0.0))
                    while (var.get('c')<var.get('inrow').get('length')):
                        try:
                            var.put('elt', var.get('buildHTML_buildGroup')(var.get('inrow').get(var.get('c')), var.get('options')))
                            if (var.get('depth')<var.get('elt').get('depth')):
                                var.put('depth', var.get('elt').get('depth'))
                            if (var.get('height')<var.get('elt').get('height')):
                                var.put('height', var.get('elt').get('height'))
                            var.get('outrow').put(var.get('c'), var.get('elt'))
                        finally:
                                var.put('c',Js(var.get('c').to_number())+Js(1))
                    var.put('rowGap', var.get('group').get('rowGaps').get(var.get('r')))
                    var.put('gap', Js(0.0))
                    if var.get('rowGap'):
                        var.put('gap', var.get('units_calculateSize')(var.get('rowGap'), var.get('options')))
                        if (var.get('gap')>Js(0.0)):
                            var.put('gap', var.get('arstrutDepth'), '+')
                            if (var.get('depth')<var.get('gap')):
                                var.put('depth', var.get('gap'))
                            var.put('gap', Js(0.0))
                    if var.get('group').get('addJot'):
                        var.put('depth', var.get('jot'), '+')
                    var.get('outrow').put('height', var.get('height'))
                    var.get('outrow').put('depth', var.get('depth'))
                    var.put('totalHeight', var.get('height'), '+')
                    var.get('outrow').put('pos', var.get('totalHeight'))
                    var.put('totalHeight', (var.get('depth')+var.get('gap')), '+')
                    var.get('body').put(var.get('r'), var.get('outrow'))
                    var.get('setHLinePos')(var.get('hLinesBeforeRow').get((var.get('r')+Js(1.0))))
                finally:
                        var.put('r',Js(var.get('r').to_number())+Js(1))
            var.put('offset', ((var.get('totalHeight')/Js(2.0))+var.get('options').callprop('fontMetrics').get('axisHeight')))
            var.put('colDescriptions', (var.get('group').get('cols') or Js([])))
            var.put('cols', Js([]))
            pass
            pass
            #for JS loop
            PyJsComma(var.put('c', Js(0.0)),var.put('colDescrNum', Js(0.0)))
            while ((var.get('c')<var.get('nc')) or (var.get('colDescrNum')<var.get('colDescriptions').get('length'))):
                try:
                    var.put('colDescr', (var.get('colDescriptions').get(var.get('colDescrNum')) or Js({})))
                    var.put('firstSeparator', Js(True))
                    while PyJsStrictEq(var.get('colDescr').get('type'),Js('separator')):
                        if var.get('firstSeparator').neg():
                            var.put('colSep', var.get('buildCommon').callprop('makeSpan', Js([Js('arraycolsep')]), Js([])))
                            var.get('colSep').get('style').put('width', (var.get('options').callprop('fontMetrics').get('doubleRuleSep')+Js('em')))
                            var.get('cols').callprop('push', var.get('colSep'))
                        if PyJsStrictEq(var.get('colDescr').get('separator'),Js('|')):
                            var.put('separator', var.get('buildCommon').callprop('makeSpan', Js([Js('vertical-separator')]), Js([]), var.get('options')))
                            var.get('separator').get('style').put('height', (var.get('totalHeight')+Js('em')))
                            var.get('separator').get('style').put('verticalAlign', ((-(var.get('totalHeight')-var.get('offset')))+Js('em')))
                            var.get('cols').callprop('push', var.get('separator'))
                        else:
                            if PyJsStrictEq(var.get('colDescr').get('separator'),Js(':')):
                                var.put('_separator', var.get('buildCommon').callprop('makeSpan', Js([Js('vertical-separator'), Js('vs-dashed')]), Js([]), var.get('options')))
                                var.get('_separator').get('style').put('height', (var.get('totalHeight')+Js('em')))
                                var.get('_separator').get('style').put('verticalAlign', ((-(var.get('totalHeight')-var.get('offset')))+Js('em')))
                                var.get('cols').callprop('push', var.get('_separator'))
                            else:
                                PyJsTempException = JsToPyException(var.get('src_ParseError').create((Js('Invalid separator type: ')+var.get('colDescr').get('separator'))))
                                raise PyJsTempException
                        (var.put('colDescrNum',Js(var.get('colDescrNum').to_number())+Js(1))-Js(1))
                        var.put('colDescr', (var.get('colDescriptions').get(var.get('colDescrNum')) or Js({})))
                        var.put('firstSeparator', Js(False))
                    if (var.get('c')>=var.get('nc')):
                        continue
                    var.put('sepwidth', PyJsComma(Js(0.0), Js(None)))
                    if ((var.get('c')>Js(0.0)) or var.get('group').get('hskipBeforeAndAfter')):
                        var.put('sepwidth', var.get('utils').callprop('deflt', var.get('colDescr').get('pregap'), var.get('arraycolsep')))
                        if PyJsStrictNeq(var.get('sepwidth'),Js(0.0)):
                            var.put('colSep', var.get('buildCommon').callprop('makeSpan', Js([Js('arraycolsep')]), Js([])))
                            var.get('colSep').get('style').put('width', (var.get('sepwidth')+Js('em')))
                            var.get('cols').callprop('push', var.get('colSep'))
                    var.put('col', Js([]))
                    #for JS loop
                    var.put('r', Js(0.0))
                    while (var.get('r')<var.get('nr')):
                        try:
                            var.put('row', var.get('body').get(var.get('r')))
                            var.put('elem', var.get('row').get(var.get('c')))
                            if var.get('elem').neg():
                                continue
                            var.put('shift', (var.get('row').get('pos')-var.get('offset')))
                            var.get('elem').put('depth', var.get('row').get('depth'))
                            var.get('elem').put('height', var.get('row').get('height'))
                            var.get('col').callprop('push', Js({'type':Js('elem'),'elem':var.get('elem'),'shift':var.get('shift')}))
                        finally:
                                var.put('r',Js(var.get('r').to_number())+Js(1))
                    var.put('col', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('individualShift'),'children':var.get('col')}), var.get('options')))
                    var.put('col', var.get('buildCommon').callprop('makeSpan', Js([(Js('col-align-')+(var.get('colDescr').get('align') or Js('c')))]), Js([var.get('col')])))
                    var.get('cols').callprop('push', var.get('col'))
                    if ((var.get('c')<(var.get('nc')-Js(1.0))) or var.get('group').get('hskipBeforeAndAfter')):
                        var.put('sepwidth', var.get('utils').callprop('deflt', var.get('colDescr').get('postgap'), var.get('arraycolsep')))
                        if PyJsStrictNeq(var.get('sepwidth'),Js(0.0)):
                            var.put('colSep', var.get('buildCommon').callprop('makeSpan', Js([Js('arraycolsep')]), Js([])))
                            var.get('colSep').get('style').put('width', (var.get('sepwidth')+Js('em')))
                            var.get('cols').callprop('push', var.get('colSep'))
                finally:
                        PyJsComma(var.put('c',Js(var.get('c').to_number())+Js(1)),var.put('colDescrNum',Js(var.get('colDescrNum').to_number())+Js(1)))
            var.put('body', var.get('buildCommon').callprop('makeSpan', Js([Js('mtable')]), var.get('cols')))
            if (var.get('hlines').get('length')>Js(0.0)):
                var.put('line', var.get('buildCommon').callprop('makeLineSpan', Js('hline'), var.get('options'), Js(0.05)))
                var.put('dashes', var.get('buildCommon').callprop('makeLineSpan', Js('hdashline'), var.get('options'), Js(0.05)))
                var.put('vListElems', Js([Js({'type':Js('elem'),'elem':var.get('body'),'shift':Js(0.0)})]))
                while (var.get('hlines').get('length')>Js(0.0)):
                    var.put('hline', var.get('hlines').callprop('pop'))
                    var.put('lineShift', (var.get('hline').get('pos')-var.get('offset')))
                    if var.get('hline').get('isDashed'):
                        var.get('vListElems').callprop('push', Js({'type':Js('elem'),'elem':var.get('dashes'),'shift':var.get('lineShift')}))
                    else:
                        var.get('vListElems').callprop('push', Js({'type':Js('elem'),'elem':var.get('line'),'shift':var.get('lineShift')}))
                var.put('body', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('individualShift'),'children':var.get('vListElems')}), var.get('options')))
            return var.get('buildCommon').callprop('makeSpan', Js([Js('mord')]), Js([var.get('body')]), var.get('options'))
        PyJs_htmlBuilder_212_._set_name('htmlBuilder')
        var.put('array_htmlBuilder', PyJs_htmlBuilder_212_)
        var.put('alignMap', Js({'c':Js('center '),'l':Js('left '),'r':Js('right ')}))
        @Js
        def PyJs_mathmlBuilder_213_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_213_}, var)
            var.registers(['_cols', 'i', 'menclose', 'iEnd', 'align', '_i2', '_i', 'group', 'options', 'cols', 'table', 'gap', 'spacing', 'columnLines', 'iStart', 'wrapper', 'rowLines', 'hlines', 'prevTypeWasAlign'])
            @Js
            def PyJs_anonymous_214_(row, this, arguments, var=var):
                var = Scope({'row':row, 'this':this, 'arguments':arguments}, var)
                var.registers(['row'])
                @Js
                def PyJs_anonymous_215_(cell, this, arguments, var=var):
                    var = Scope({'cell':cell, 'this':this, 'arguments':arguments}, var)
                    var.registers(['cell'])
                    return var.get('mathMLTree').get('MathNode').create(Js('mtd'), Js([var.get('buildMathML_buildGroup')(var.get('cell'), var.get('options'))]))
                PyJs_anonymous_215_._set_name('anonymous')
                return var.get('mathMLTree').get('MathNode').create(Js('mtr'), var.get('row').callprop('map', PyJs_anonymous_215_))
            PyJs_anonymous_214_._set_name('anonymous')
            var.put('table', var.get('mathMLTree').get('MathNode').create(Js('mtable'), var.get('group').get('body').callprop('map', PyJs_anonymous_214_)))
            var.put('gap', (((Js(0.16)+var.get('group').get('arraystretch'))-Js(1.0))+(Js(0.09) if var.get('group').get('addJot') else Js(0.0))))
            var.get('table').callprop('setAttribute', Js('rowspacing'), (var.get('gap')+Js('em')))
            var.put('menclose', Js(''))
            var.put('align', Js(''))
            if var.get('group').get('cols'):
                var.put('cols', var.get('group').get('cols'))
                var.put('columnLines', Js(''))
                var.put('prevTypeWasAlign', Js(False))
                var.put('iStart', Js(0.0))
                var.put('iEnd', var.get('cols').get('length'))
                if PyJsStrictEq(var.get('cols').get('0').get('type'),Js('separator')):
                    var.put('menclose', Js('top '), '+')
                    var.put('iStart', Js(1.0))
                if PyJsStrictEq(var.get('cols').get((var.get('cols').get('length')-Js(1.0))).get('type'),Js('separator')):
                    var.put('menclose', Js('bottom '), '+')
                    var.put('iEnd', Js(1.0), '-')
                #for JS loop
                var.put('i', var.get('iStart'))
                while (var.get('i')<var.get('iEnd')):
                    try:
                        if PyJsStrictEq(var.get('cols').get(var.get('i')).get('type'),Js('align')):
                            var.put('align', var.get('alignMap').get(var.get('cols').get(var.get('i')).get('align')), '+')
                            if var.get('prevTypeWasAlign'):
                                var.put('columnLines', Js('none '), '+')
                            var.put('prevTypeWasAlign', Js(True))
                        else:
                            if PyJsStrictEq(var.get('cols').get(var.get('i')).get('type'),Js('separator')):
                                if var.get('prevTypeWasAlign'):
                                    var.put('columnLines', (Js('solid ') if PyJsStrictEq(var.get('cols').get(var.get('i')).get('separator'),Js('|')) else Js('dashed ')), '+')
                                    var.put('prevTypeWasAlign', Js(False))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                var.get('table').callprop('setAttribute', Js('columnalign'), var.get('align').callprop('trim'))
                if JsRegExp('/[sd]/').callprop('test', var.get('columnLines')):
                    var.get('table').callprop('setAttribute', Js('columnlines'), var.get('columnLines').callprop('trim'))
            if PyJsStrictEq(var.get('group').get('colSeparationType'),Js('align')):
                var.put('_cols', (var.get('group').get('cols') or Js([])))
                var.put('spacing', Js(''))
                #for JS loop
                var.put('_i', Js(1.0))
                while (var.get('_i')<var.get('_cols').get('length')):
                    try:
                        var.put('spacing', (Js('0em ') if (var.get('_i')%Js(2.0)) else Js('1em ')), '+')
                    finally:
                            (var.put('_i',Js(var.get('_i').to_number())+Js(1))-Js(1))
                var.get('table').callprop('setAttribute', Js('columnspacing'), var.get('spacing').callprop('trim'))
            else:
                if PyJsStrictEq(var.get('group').get('colSeparationType'),Js('alignat')):
                    var.get('table').callprop('setAttribute', Js('columnspacing'), Js('0em'))
                else:
                    var.get('table').callprop('setAttribute', Js('columnspacing'), Js('1em'))
            var.put('rowLines', Js(''))
            var.put('hlines', var.get('group').get('hLinesBeforeRow'))
            var.put('menclose', (Js('left ') if (var.get('hlines').get('0').get('length')>Js(0.0)) else Js('')), '+')
            var.put('menclose', (Js('right ') if (var.get('hlines').get((var.get('hlines').get('length')-Js(1.0))).get('length')>Js(0.0)) else Js('')), '+')
            #for JS loop
            var.put('_i2', Js(1.0))
            while (var.get('_i2')<(var.get('hlines').get('length')-Js(1.0))):
                try:
                    var.put('rowLines', (Js('none ') if PyJsStrictEq(var.get('hlines').get(var.get('_i2')).get('length'),Js(0.0)) else (Js('dashed ') if var.get('hlines').get(var.get('_i2')).get('0') else Js('solid '))), '+')
                finally:
                        (var.put('_i2',Js(var.get('_i2').to_number())+Js(1))-Js(1))
            if JsRegExp('/[sd]/').callprop('test', var.get('rowLines')):
                var.get('table').callprop('setAttribute', Js('rowlines'), var.get('rowLines').callprop('trim'))
            if PyJsStrictEq(var.get('menclose'),Js('')):
                return var.get('table')
            else:
                var.put('wrapper', var.get('mathMLTree').get('MathNode').create(Js('menclose'), Js([var.get('table')])))
                var.get('wrapper').callprop('setAttribute', Js('notation'), var.get('menclose').callprop('trim'))
                return var.get('wrapper')
        PyJs_mathmlBuilder_213_._set_name('mathmlBuilder')
        var.put('array_mathmlBuilder', PyJs_mathmlBuilder_213_)
        @Js
        def PyJs_alignedHandler_216_(context, args, this, arguments, var=var):
            var = Scope({'context':context, 'args':args, 'this':this, 'arguments':arguments, 'alignedHandler':PyJs_alignedHandler_216_}, var)
            var.registers(['numMaths', 'i', 'align', 'emptyGroup', 'arg0', 'context', 'textord', 'pregap', 'cols', 'res', 'numCols', 'isAligned', 'args', 'ordgroup', '_i4'])
            var.put('cols', Js([]))
            var.put('res', var.get('parseArray')(var.get('context').get('parser'), Js({'cols':var.get('cols'),'addJot':Js(True)}), Js('display')))
            pass
            var.put('numCols', Js(0.0))
            var.put('emptyGroup', Js({'type':Js('ordgroup'),'mode':var.get('context').get('mode'),'body':Js([])}))
            var.put('ordgroup', var.get('checkNodeType')(var.get('args').get('0'), Js('ordgroup')))
            if var.get('ordgroup'):
                var.put('arg0', Js(''))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('ordgroup').get('body').get('length')):
                    try:
                        var.put('textord', var.get('assertNodeType')(var.get('ordgroup').get('body').get(var.get('i')), Js('textord')))
                        var.put('arg0', var.get('textord').get('text'), '+')
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                var.put('numMaths', var.get('Number')(var.get('arg0')))
                var.put('numCols', (var.get('numMaths')*Js(2.0)))
            var.put('isAligned', var.get('numCols').neg())
            @Js
            def PyJs_anonymous_217_(row, this, arguments, var=var):
                var = Scope({'row':row, 'this':this, 'arguments':arguments}, var)
                var.registers(['curMaths', 'styling', '_i3', 'row', '_ordgroup'])
                #for JS loop
                var.put('_i3', Js(1.0))
                while (var.get('_i3')<var.get('row').get('length')):
                    try:
                        var.put('styling', var.get('assertNodeType')(var.get('row').get(var.get('_i3')), Js('styling')))
                        var.put('_ordgroup', var.get('assertNodeType')(var.get('styling').get('body').get('0'), Js('ordgroup')))
                        var.get('_ordgroup').get('body').callprop('unshift', var.get('emptyGroup'))
                    finally:
                            var.put('_i3', Js(2.0), '+')
                if var.get('isAligned').neg():
                    var.put('curMaths', (var.get('row').get('length')/Js(2.0)))
                    if (var.get('numMaths')<var.get('curMaths')):
                        PyJsTempException = JsToPyException(var.get('src_ParseError').create((Js('Too many math in a row: ')+(((Js('expected ')+var.get('numMaths'))+Js(', but got '))+var.get('curMaths'))), var.get('row').get('0')))
                        raise PyJsTempException
                else:
                    if (var.get('numCols')<var.get('row').get('length')):
                        var.put('numCols', var.get('row').get('length'))
            PyJs_anonymous_217_._set_name('anonymous')
            var.get('res').get('body').callprop('forEach', PyJs_anonymous_217_)
            #for JS loop
            var.put('_i4', Js(0.0))
            while (var.get('_i4')<var.get('numCols')):
                try:
                    var.put('align', Js('r'))
                    var.put('pregap', Js(0.0))
                    if PyJsStrictEq((var.get('_i4')%Js(2.0)),Js(1.0)):
                        var.put('align', Js('l'))
                    else:
                        if ((var.get('_i4')>Js(0.0)) and var.get('isAligned')):
                            var.put('pregap', Js(1.0))
                    var.get('cols').put(var.get('_i4'), Js({'type':Js('align'),'align':var.get('align'),'pregap':var.get('pregap'),'postgap':Js(0.0)}))
                finally:
                        var.put('_i4',Js(var.get('_i4').to_number())+Js(1))
            var.get('res').put('colSeparationType', (Js('align') if var.get('isAligned') else Js('alignat')))
            return var.get('res')
        PyJs_alignedHandler_216_._set_name('alignedHandler')
        var.put('array_alignedHandler', PyJs_alignedHandler_216_)
        @Js
        def PyJs_handler_218_(context, args, this, arguments, var=var):
            var = Scope({'context':context, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_218_}, var)
            var.registers(['context', 'colalign', 'cols', 'res', 'args', 'symNode'])
            var.put('symNode', var.get('checkSymbolNodeType')(var.get('args').get('0')))
            var.put('colalign', (Js([var.get('args').get('0')]) if var.get('symNode') else var.get('assertNodeType')(var.get('args').get('0'), Js('ordgroup')).get('body')))
            @Js
            def PyJs_anonymous_219_(nde, this, arguments, var=var):
                var = Scope({'nde':nde, 'this':this, 'arguments':arguments}, var)
                var.registers(['node', 'nde', 'ca'])
                var.put('node', var.get('assertSymbolNodeType')(var.get('nde')))
                var.put('ca', var.get('node').get('text'))
                if PyJsStrictNeq(Js('lcr').callprop('indexOf', var.get('ca')),(-Js(1.0))):
                    return Js({'type':Js('align'),'align':var.get('ca')})
                else:
                    if PyJsStrictEq(var.get('ca'),Js('|')):
                        return Js({'type':Js('separator'),'separator':Js('|')})
                    else:
                        if PyJsStrictEq(var.get('ca'),Js(':')):
                            return Js({'type':Js('separator'),'separator':Js(':')})
                PyJsTempException = JsToPyException(var.get('src_ParseError').create((Js('Unknown column alignment: ')+var.get('ca')), var.get('nde')))
                raise PyJsTempException
            PyJs_anonymous_219_._set_name('anonymous')
            var.put('cols', var.get('colalign').callprop('map', PyJs_anonymous_219_))
            var.put('res', Js({'cols':var.get('cols'),'hskipBeforeAndAfter':Js(True)}))
            return var.get('parseArray')(var.get('context').get('parser'), var.get('res'), var.get('dCellStyle')(var.get('context').get('envName')))
        PyJs_handler_218_._set_name('handler')
        var.get('defineEnvironment')(Js({'type':Js('array'),'names':Js([Js('array'), Js('darray')]),'props':Js({'numArgs':Js(1.0)}),'handler':PyJs_handler_218_,'htmlBuilder':var.get('array_htmlBuilder'),'mathmlBuilder':var.get('array_mathmlBuilder')}))
        @Js
        def PyJs_handler_220_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_220_}, var)
            var.registers(['res', 'context', 'payload', 'delimiters'])
            var.put('delimiters', Js({'matrix':var.get(u"null"),'pmatrix':Js([Js('('), Js(')')]),'bmatrix':Js([Js('['), Js(']')]),'Bmatrix':Js([Js('\\{'), Js('\\}')]),'vmatrix':Js([Js('|'), Js('|')]),'Vmatrix':Js([Js('\\Vert'), Js('\\Vert')])}).get(var.get('context').get('envName')))
            var.put('payload', Js({'hskipBeforeAndAfter':Js(False)}))
            var.put('res', var.get('parseArray')(var.get('context').get('parser'), var.get('payload'), var.get('dCellStyle')(var.get('context').get('envName'))))
            return (Js({'type':Js('leftright'),'mode':var.get('context').get('mode'),'body':Js([var.get('res')]),'left':var.get('delimiters').get('0'),'right':var.get('delimiters').get('1')}) if var.get('delimiters') else var.get('res'))
        PyJs_handler_220_._set_name('handler')
        var.get('defineEnvironment')(Js({'type':Js('array'),'names':Js([Js('matrix'), Js('pmatrix'), Js('bmatrix'), Js('Bmatrix'), Js('vmatrix'), Js('Vmatrix')]),'props':Js({'numArgs':Js(0.0)}),'handler':PyJs_handler_220_,'htmlBuilder':var.get('array_htmlBuilder'),'mathmlBuilder':var.get('array_mathmlBuilder')}))
        @Js
        def PyJs_handler_221_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_221_}, var)
            var.registers(['res', 'context', 'payload'])
            var.put('payload', Js({'arraystretch':Js(1.2),'cols':Js([Js({'type':Js('align'),'align':Js('l'),'pregap':Js(0.0),'postgap':Js(1.0)}), Js({'type':Js('align'),'align':Js('l'),'pregap':Js(0.0),'postgap':Js(0.0)})])}))
            var.put('res', var.get('parseArray')(var.get('context').get('parser'), var.get('payload'), var.get('dCellStyle')(var.get('context').get('envName'))))
            return Js({'type':Js('leftright'),'mode':var.get('context').get('mode'),'body':Js([var.get('res')]),'left':Js('\\{'),'right':Js('.')})
        PyJs_handler_221_._set_name('handler')
        var.get('defineEnvironment')(Js({'type':Js('array'),'names':Js([Js('cases'), Js('dcases')]),'props':Js({'numArgs':Js(0.0)}),'handler':PyJs_handler_221_,'htmlBuilder':var.get('array_htmlBuilder'),'mathmlBuilder':var.get('array_mathmlBuilder')}))
        var.get('defineEnvironment')(Js({'type':Js('array'),'names':Js([Js('aligned')]),'props':Js({'numArgs':Js(0.0)}),'handler':var.get('array_alignedHandler'),'htmlBuilder':var.get('array_htmlBuilder'),'mathmlBuilder':var.get('array_mathmlBuilder')}))
        @Js
        def PyJs_handler_222_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_222_}, var)
            var.registers(['res', 'context'])
            var.put('res', Js({'cols':Js([Js({'type':Js('align'),'align':Js('c')})]),'addJot':Js(True)}))
            return var.get('parseArray')(var.get('context').get('parser'), var.get('res'), Js('display'))
        PyJs_handler_222_._set_name('handler')
        var.get('defineEnvironment')(Js({'type':Js('array'),'names':Js([Js('gathered')]),'props':Js({'numArgs':Js(0.0)}),'handler':PyJs_handler_222_,'htmlBuilder':var.get('array_htmlBuilder'),'mathmlBuilder':var.get('array_mathmlBuilder')}))
        var.get('defineEnvironment')(Js({'type':Js('array'),'names':Js([Js('alignedat')]),'props':Js({'numArgs':Js(1.0)}),'handler':var.get('array_alignedHandler'),'htmlBuilder':var.get('array_htmlBuilder'),'mathmlBuilder':var.get('array_mathmlBuilder')}))
        @Js
        def PyJs_handler_223_(context, args, this, arguments, var=var):
            var = Scope({'context':context, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_223_}, var)
            var.registers(['context', 'args'])
            PyJsTempException = JsToPyException(var.get('src_ParseError').create((var.get('context').get('funcName')+Js(' valid only within array environment'))))
            raise PyJsTempException
        PyJs_handler_223_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('text'),'names':Js([Js('\\hline'), Js('\\hdashline')]),'props':Js({'numArgs':Js(0.0),'allowedInText':Js(True),'allowedInMath':Js(True)}),'handler':PyJs_handler_223_}))
        var.put('environments', var.get('_environments'))
        var.put('src_environments', var.get('environments'))
        @Js
        def PyJs_handler_224_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_224_}, var)
            var.registers(['funcName', 'i', '_parser$parseArgument', 'nameGroup', 'end', '_args', 'context', 'endNameToken', 'env', 'optArgs', 'envName', '_ref', 'result', 'args', 'parser'])
            var.put('parser', var.get('_ref').get('parser'))
            var.put('funcName', var.get('_ref').get('funcName'))
            var.put('nameGroup', var.get('args').get('0'))
            if PyJsStrictNeq(var.get('nameGroup').get('type'),Js('ordgroup')):
                PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('Invalid environment name'), var.get('nameGroup')))
                raise PyJsTempException
            var.put('envName', Js(''))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('nameGroup').get('body').get('length')):
                try:
                    var.put('envName', var.get('assertNodeType')(var.get('nameGroup').get('body').get(var.get('i')), Js('textord')).get('text'), '+')
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            if PyJsStrictEq(var.get('funcName'),Js('\\begin')):
                if var.get('src_environments').callprop('hasOwnProperty', var.get('envName')).neg():
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create((Js('No such environment: ')+var.get('envName')), var.get('nameGroup')))
                    raise PyJsTempException
                var.put('env', var.get('src_environments').get(var.get('envName')))
                var.put('_parser$parseArgument', var.get('parser').callprop('parseArguments', ((Js('\\begin{')+var.get('envName'))+Js('}')), var.get('env')))
                var.put('_args', var.get('_parser$parseArgument').get('args'))
                var.put('optArgs', var.get('_parser$parseArgument').get('optArgs'))
                var.put('context', Js({'mode':var.get('parser').get('mode'),'envName':var.get('envName'),'parser':var.get('parser')}))
                var.put('result', var.get('env').callprop('handler', var.get('context'), var.get('_args'), var.get('optArgs')))
                var.get('parser').callprop('expect', Js('\\end'), Js(False))
                var.put('endNameToken', var.get('parser').get('nextToken'))
                var.put('end', var.get('assertNodeType')(var.get('parser').callprop('parseFunction'), Js('environment')))
                if PyJsStrictNeq(var.get('end').get('name'),var.get('envName')):
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(((((Js('Mismatch: \\begin{')+var.get('envName'))+Js('} matched by \\end{'))+var.get('end').get('name'))+Js('}')), var.get('endNameToken')))
                    raise PyJsTempException
                return var.get('result')
            return Js({'type':Js('environment'),'mode':var.get('parser').get('mode'),'name':var.get('envName'),'nameGroup':var.get('nameGroup')})
        PyJs_handler_224_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('environment'),'names':Js([Js('\\begin'), Js('\\end')]),'props':Js({'numArgs':Js(1.0),'argTypes':Js([Js('text')])}),'handler':PyJs_handler_224_}))
        var.put('mclass_makeSpan', var.get('buildCommon').get('makeSpan'))
        pass
        pass
        @Js
        def PyJs_handler_225_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_225_}, var)
            var.registers(['funcName', 'body', '_ref', 'args', 'parser'])
            var.put('parser', var.get('_ref').get('parser'))
            var.put('funcName', var.get('_ref').get('funcName'))
            var.put('body', var.get('args').get('0'))
            return Js({'type':Js('mclass'),'mode':var.get('parser').get('mode'),'mclass':(Js('m')+var.get('funcName').callprop('substr', Js(5.0))),'body':var.get('defineFunction_ordargument')(var.get('body'))})
        PyJs_handler_225_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('mclass'),'names':Js([Js('\\mathord'), Js('\\mathbin'), Js('\\mathrel'), Js('\\mathopen'), Js('\\mathclose'), Js('\\mathpunct'), Js('\\mathinner')]),'props':Js({'numArgs':Js(1.0)}),'handler':PyJs_handler_225_,'htmlBuilder':var.get('mclass_htmlBuilder'),'mathmlBuilder':var.get('mclass_mathmlBuilder')}))
        @Js
        def PyJs_binrelClass_226_(arg, this, arguments, var=var):
            var = Scope({'arg':arg, 'this':this, 'arguments':arguments, 'binrelClass':PyJs_binrelClass_226_}, var)
            var.registers(['arg', 'atom'])
            var.put('atom', (var.get('arg').get('body').get('0') if (PyJsStrictEq(var.get('arg').get('type'),Js('ordgroup')) and var.get('arg').get('body').get('length')) else var.get('arg')))
            if (PyJsStrictEq(var.get('atom').get('type'),Js('atom')) and (PyJsStrictEq(var.get('atom').get('family'),Js('bin')) or PyJsStrictEq(var.get('atom').get('family'),Js('rel')))):
                return (Js('m')+var.get('atom').get('family'))
            else:
                return Js('mord')
        PyJs_binrelClass_226_._set_name('binrelClass')
        var.put('binrelClass', PyJs_binrelClass_226_)
        @Js
        def PyJs_handler_227_(_ref2, args, this, arguments, var=var):
            var = Scope({'_ref2':_ref2, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_227_}, var)
            var.registers(['parser', 'args', '_ref2'])
            var.put('parser', var.get('_ref2').get('parser'))
            return Js({'type':Js('mclass'),'mode':var.get('parser').get('mode'),'mclass':var.get('binrelClass')(var.get('args').get('0')),'body':Js([var.get('args').get('1')])})
        PyJs_handler_227_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('mclass'),'names':Js([Js('\\@binrel')]),'props':Js({'numArgs':Js(2.0)}),'handler':PyJs_handler_227_}))
        @Js
        def PyJs_handler_228_(_ref3, args, this, arguments, var=var):
            var = Scope({'_ref3':_ref3, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_228_}, var)
            var.registers(['shiftedArg', 'funcName', 'baseArg', 'baseOp', '_ref3', 'mclass', 'args', 'parser', 'supsub'])
            var.put('parser', var.get('_ref3').get('parser'))
            var.put('funcName', var.get('_ref3').get('funcName'))
            var.put('baseArg', var.get('args').get('1'))
            var.put('shiftedArg', var.get('args').get('0'))
            pass
            if PyJsStrictNeq(var.get('funcName'),Js('\\stackrel')):
                var.put('mclass', var.get('binrelClass')(var.get('baseArg')))
            else:
                var.put('mclass', Js('mrel'))
            var.put('baseOp', Js({'type':Js('ordgroup'),'mode':var.get('baseArg').get('mode'),'limits':Js(True),'alwaysHandleSupSub':Js(True),'parentIsSupSub':Js(False),'symbol':Js(False),'suppressBaseShift':PyJsStrictNeq(var.get('funcName'),Js('\\stackrel')),'body':var.get('defineFunction_ordargument')(var.get('baseArg'))}))
            var.put('supsub', Js({'type':Js('supsub'),'mode':var.get('shiftedArg').get('mode'),'base':var.get('baseOp'),'text':var.get('funcName'),'sup':(var.get(u"null") if PyJsStrictEq(var.get('funcName'),Js('\\underset')) else var.get('shiftedArg')),'sub':(var.get('shiftedArg') if PyJsStrictEq(var.get('funcName'),Js('\\underset')) else var.get(u"null"))}))
            return Js({'type':Js('mclass'),'mode':var.get('parser').get('mode'),'mclass':var.get('mclass'),'body':Js([var.get('supsub')])})
        PyJs_handler_228_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('mclass'),'names':Js([Js('\\stackrel'), Js('\\overset'), Js('\\underset')]),'props':Js({'numArgs':Js(2.0)}),'handler':PyJs_handler_228_,'htmlBuilder':var.get('mclass_htmlBuilder'),'mathmlBuilder':var.get('mclass_mathmlBuilder')}))
        @Js
        def PyJs_htmlBuilder_229_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_229_}, var)
            var.registers(['font', 'group', 'options', 'newOptions'])
            var.put('font', var.get('group').get('font'))
            var.put('newOptions', var.get('options').callprop('withFont', var.get('font')))
            return var.get('buildHTML_buildGroup')(var.get('group').get('body'), var.get('newOptions'))
        PyJs_htmlBuilder_229_._set_name('htmlBuilder')
        var.put('font_htmlBuilder', PyJs_htmlBuilder_229_)
        @Js
        def PyJs_mathmlBuilder_230_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_230_}, var)
            var.registers(['font', 'group', 'options', 'newOptions'])
            var.put('font', var.get('group').get('font'))
            var.put('newOptions', var.get('options').callprop('withFont', var.get('font')))
            return var.get('buildMathML_buildGroup')(var.get('group').get('body'), var.get('newOptions'))
        PyJs_mathmlBuilder_230_._set_name('mathmlBuilder')
        var.put('font_mathmlBuilder', PyJs_mathmlBuilder_230_)
        var.put('fontAliases', Js({'\\Bbb':Js('\\mathbb'),'\\bold':Js('\\mathbf'),'\\frak':Js('\\mathfrak'),'\\bm':Js('\\boldsymbol')}))
        def PyJs_LONG_232_(var=var):
            @Js
            def PyJs_handler_231_(_ref, args, this, arguments, var=var):
                var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_231_}, var)
                var.registers(['funcName', 'func', 'body', '_ref', 'args', 'parser'])
                var.put('parser', var.get('_ref').get('parser'))
                var.put('funcName', var.get('_ref').get('funcName'))
                var.put('body', var.get('args').get('0'))
                var.put('func', var.get('funcName'))
                if var.get('fontAliases').contains(var.get('func')):
                    var.put('func', var.get('fontAliases').get(var.get('func')))
                return Js({'type':Js('font'),'mode':var.get('parser').get('mode'),'font':var.get('func').callprop('slice', Js(1.0)),'body':var.get('body')})
            PyJs_handler_231_._set_name('handler')
            return var.get('defineFunction')(Js({'type':Js('font'),'names':Js([Js('\\mathrm'), Js('\\mathit'), Js('\\mathbf'), Js('\\mathnormal'), Js('\\mathbb'), Js('\\mathcal'), Js('\\mathfrak'), Js('\\mathscr'), Js('\\mathsf'), Js('\\mathtt'), Js('\\Bbb'), Js('\\bold'), Js('\\frak')]),'props':Js({'numArgs':Js(1.0),'greediness':Js(2.0)}),'handler':PyJs_handler_231_,'htmlBuilder':var.get('font_htmlBuilder'),'mathmlBuilder':var.get('font_mathmlBuilder')}))
        PyJs_LONG_232_()
        @Js
        def PyJs_handler_233_(_ref2, args, this, arguments, var=var):
            var = Scope({'_ref2':_ref2, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_233_}, var)
            var.registers(['body', 'parser', 'args', '_ref2'])
            var.put('parser', var.get('_ref2').get('parser'))
            var.put('body', var.get('args').get('0'))
            return Js({'type':Js('mclass'),'mode':var.get('parser').get('mode'),'mclass':var.get('binrelClass')(var.get('body')),'body':Js([Js({'type':Js('font'),'mode':var.get('parser').get('mode'),'font':Js('boldsymbol'),'body':var.get('body')})])})
        PyJs_handler_233_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('mclass'),'names':Js([Js('\\boldsymbol'), Js('\\bm')]),'props':Js({'numArgs':Js(1.0),'greediness':Js(2.0)}),'handler':PyJs_handler_233_}))
        @Js
        def PyJs_handler_234_(_ref3, args, this, arguments, var=var):
            var = Scope({'_ref3':_ref3, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_234_}, var)
            var.registers(['funcName', 'breakOnTokenText', 'mode', 'body', 'style', '_ref3', 'args', 'parser'])
            var.put('parser', var.get('_ref3').get('parser'))
            var.put('funcName', var.get('_ref3').get('funcName'))
            var.put('breakOnTokenText', var.get('_ref3').get('breakOnTokenText'))
            var.put('mode', var.get('parser').get('mode'))
            var.put('body', var.get('parser').callprop('parseExpression', Js(True), var.get('breakOnTokenText')))
            var.put('style', (Js('math')+var.get('funcName').callprop('slice', Js(1.0))))
            return Js({'type':Js('font'),'mode':var.get('mode'),'font':var.get('style'),'body':Js({'type':Js('ordgroup'),'mode':var.get('parser').get('mode'),'body':var.get('body')})})
        PyJs_handler_234_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('font'),'names':Js([Js('\\rm'), Js('\\sf'), Js('\\tt'), Js('\\bf'), Js('\\it')]),'props':Js({'numArgs':Js(0.0),'allowedInText':Js(True)}),'handler':PyJs_handler_234_,'htmlBuilder':var.get('font_htmlBuilder'),'mathmlBuilder':var.get('font_mathmlBuilder')}))
        @Js
        def PyJs_adjustStyle_235_(size, originalStyle, this, arguments, var=var):
            var = Scope({'size':size, 'originalStyle':originalStyle, 'this':this, 'arguments':arguments, 'adjustStyle':PyJs_adjustStyle_235_}, var)
            var.registers(['style', 'size', 'originalStyle'])
            var.put('style', var.get('originalStyle'))
            if PyJsStrictEq(var.get('size'),Js('display')):
                var.put('style', (var.get('style').callprop('text') if (var.get('style').get('id')>=var.get('src_Style').get('SCRIPT').get('id')) else var.get('src_Style').get('DISPLAY')))
            else:
                if (PyJsStrictEq(var.get('size'),Js('text')) and PyJsStrictEq(var.get('style').get('size'),var.get('src_Style').get('DISPLAY').get('size'))):
                    var.put('style', var.get('src_Style').get('TEXT'))
                else:
                    if PyJsStrictEq(var.get('size'),Js('script')):
                        var.put('style', var.get('src_Style').get('SCRIPT'))
                    else:
                        if PyJsStrictEq(var.get('size'),Js('scriptscript')):
                            var.put('style', var.get('src_Style').get('SCRIPTSCRIPT'))
            return var.get('style')
        PyJs_adjustStyle_235_._set_name('adjustStyle')
        var.put('genfrac_adjustStyle', PyJs_adjustStyle_235_)
        @Js
        def PyJs_htmlBuilder_236_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_236_}, var)
            var.registers(['nstyle', 'midShift', 'candidateClearance', 'rule', 'leftDelim', 'hStrut', 'frac', 'newOptions', 'options', 'denomShift', 'ruleSpacing', 'denomm', 'dstyle', 'axisHeight', 'numShift', 'clearance', 'rightDelim', 'delimSize', 'numerm', 'ruleWidth', 'group', 'dStrut', 'style'])
            var.put('style', var.get('genfrac_adjustStyle')(var.get('group').get('size'), var.get('options').get('style')))
            var.put('nstyle', var.get('style').callprop('fracNum'))
            var.put('dstyle', var.get('style').callprop('fracDen'))
            pass
            var.put('newOptions', var.get('options').callprop('havingStyle', var.get('nstyle')))
            var.put('numerm', var.get('buildHTML_buildGroup')(var.get('group').get('numer'), var.get('newOptions'), var.get('options')))
            if var.get('group').get('continued'):
                var.put('hStrut', (Js(8.5)/var.get('options').callprop('fontMetrics').get('ptPerEm')))
                var.put('dStrut', (Js(3.5)/var.get('options').callprop('fontMetrics').get('ptPerEm')))
                var.get('numerm').put('height', (var.get('hStrut') if (var.get('numerm').get('height')<var.get('hStrut')) else var.get('numerm').get('height')))
                var.get('numerm').put('depth', (var.get('dStrut') if (var.get('numerm').get('depth')<var.get('dStrut')) else var.get('numerm').get('depth')))
            var.put('newOptions', var.get('options').callprop('havingStyle', var.get('dstyle')))
            var.put('denomm', var.get('buildHTML_buildGroup')(var.get('group').get('denom'), var.get('newOptions'), var.get('options')))
            pass
            pass
            pass
            if var.get('group').get('hasBarLine'):
                if var.get('group').get('barSize'):
                    var.put('ruleWidth', var.get('units_calculateSize')(var.get('group').get('barSize'), var.get('options')))
                    var.put('rule', var.get('buildCommon').callprop('makeLineSpan', Js('frac-line'), var.get('options'), var.get('ruleWidth')))
                else:
                    var.put('rule', var.get('buildCommon').callprop('makeLineSpan', Js('frac-line'), var.get('options')))
                var.put('ruleWidth', var.get('rule').get('height'))
                var.put('ruleSpacing', var.get('rule').get('height'))
            else:
                var.put('rule', var.get(u"null"))
                var.put('ruleWidth', Js(0.0))
                var.put('ruleSpacing', var.get('options').callprop('fontMetrics').get('defaultRuleThickness'))
            pass
            pass
            pass
            if (PyJsStrictEq(var.get('style').get('size'),var.get('src_Style').get('DISPLAY').get('size')) or PyJsStrictEq(var.get('group').get('size'),Js('display'))):
                var.put('numShift', var.get('options').callprop('fontMetrics').get('num1'))
                if (var.get('ruleWidth')>Js(0.0)):
                    var.put('clearance', (Js(3.0)*var.get('ruleSpacing')))
                else:
                    var.put('clearance', (Js(7.0)*var.get('ruleSpacing')))
                var.put('denomShift', var.get('options').callprop('fontMetrics').get('denom1'))
            else:
                if (var.get('ruleWidth')>Js(0.0)):
                    var.put('numShift', var.get('options').callprop('fontMetrics').get('num2'))
                    var.put('clearance', var.get('ruleSpacing'))
                else:
                    var.put('numShift', var.get('options').callprop('fontMetrics').get('num3'))
                    var.put('clearance', (Js(3.0)*var.get('ruleSpacing')))
                var.put('denomShift', var.get('options').callprop('fontMetrics').get('denom2'))
            pass
            if var.get('rule').neg():
                var.put('candidateClearance', ((var.get('numShift')-var.get('numerm').get('depth'))-(var.get('denomm').get('height')-var.get('denomShift'))))
                if (var.get('candidateClearance')<var.get('clearance')):
                    var.put('numShift', (Js(0.5)*(var.get('clearance')-var.get('candidateClearance'))), '+')
                    var.put('denomShift', (Js(0.5)*(var.get('clearance')-var.get('candidateClearance'))), '+')
                var.put('frac', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('individualShift'),'children':Js([Js({'type':Js('elem'),'elem':var.get('denomm'),'shift':var.get('denomShift')}), Js({'type':Js('elem'),'elem':var.get('numerm'),'shift':(-var.get('numShift'))})])}), var.get('options')))
            else:
                var.put('axisHeight', var.get('options').callprop('fontMetrics').get('axisHeight'))
                if (((var.get('numShift')-var.get('numerm').get('depth'))-(var.get('axisHeight')+(Js(0.5)*var.get('ruleWidth'))))<var.get('clearance')):
                    var.put('numShift', (var.get('clearance')-((var.get('numShift')-var.get('numerm').get('depth'))-(var.get('axisHeight')+(Js(0.5)*var.get('ruleWidth'))))), '+')
                if (((var.get('axisHeight')-(Js(0.5)*var.get('ruleWidth')))-(var.get('denomm').get('height')-var.get('denomShift')))<var.get('clearance')):
                    var.put('denomShift', (var.get('clearance')-((var.get('axisHeight')-(Js(0.5)*var.get('ruleWidth')))-(var.get('denomm').get('height')-var.get('denomShift')))), '+')
                var.put('midShift', (-(var.get('axisHeight')-(Js(0.5)*var.get('ruleWidth')))))
                var.put('frac', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('individualShift'),'children':Js([Js({'type':Js('elem'),'elem':var.get('denomm'),'shift':var.get('denomShift')}), Js({'type':Js('elem'),'elem':var.get('rule'),'shift':var.get('midShift')}), Js({'type':Js('elem'),'elem':var.get('numerm'),'shift':(-var.get('numShift'))})])}), var.get('options')))
            var.put('newOptions', var.get('options').callprop('havingStyle', var.get('style')))
            var.get('frac').put('height', (var.get('newOptions').get('sizeMultiplier')/var.get('options').get('sizeMultiplier')), '*')
            var.get('frac').put('depth', (var.get('newOptions').get('sizeMultiplier')/var.get('options').get('sizeMultiplier')), '*')
            pass
            if PyJsStrictEq(var.get('style').get('size'),var.get('src_Style').get('DISPLAY').get('size')):
                var.put('delimSize', var.get('options').callprop('fontMetrics').get('delim1'))
            else:
                var.put('delimSize', var.get('options').callprop('fontMetrics').get('delim2'))
            pass
            pass
            if (var.get('group').get('leftDelim')==var.get(u"null")):
                var.put('leftDelim', var.get('makeNullDelimiter')(var.get('options'), Js([Js('mopen')])))
            else:
                var.put('leftDelim', var.get('delimiter').callprop('customSizedDelim', var.get('group').get('leftDelim'), var.get('delimSize'), Js(True), var.get('options').callprop('havingStyle', var.get('style')), var.get('group').get('mode'), Js([Js('mopen')])))
            if var.get('group').get('continued'):
                var.put('rightDelim', var.get('buildCommon').callprop('makeSpan', Js([])))
            else:
                if (var.get('group').get('rightDelim')==var.get(u"null")):
                    var.put('rightDelim', var.get('makeNullDelimiter')(var.get('options'), Js([Js('mclose')])))
                else:
                    var.put('rightDelim', var.get('delimiter').callprop('customSizedDelim', var.get('group').get('rightDelim'), var.get('delimSize'), Js(True), var.get('options').callprop('havingStyle', var.get('style')), var.get('group').get('mode'), Js([Js('mclose')])))
            return var.get('buildCommon').callprop('makeSpan', Js([Js('mord')]).callprop('concat', var.get('newOptions').callprop('sizingClasses', var.get('options'))), Js([var.get('leftDelim'), var.get('buildCommon').callprop('makeSpan', Js([Js('mfrac')]), Js([var.get('frac')])), var.get('rightDelim')]), var.get('options'))
        PyJs_htmlBuilder_236_._set_name('htmlBuilder')
        var.put('genfrac_htmlBuilder', PyJs_htmlBuilder_236_)
        @Js
        def PyJs_mathmlBuilder_237_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_237_}, var)
            var.registers(['ruleWidth', 'rightOp', 'group', 'options', 'withDelims', 'node', 'leftOp', 'style', 'isDisplay'])
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mfrac'), Js([var.get('buildMathML_buildGroup')(var.get('group').get('numer'), var.get('options')), var.get('buildMathML_buildGroup')(var.get('group').get('denom'), var.get('options'))])))
            if var.get('group').get('hasBarLine').neg():
                var.get('node').callprop('setAttribute', Js('linethickness'), Js('0px'))
            else:
                if var.get('group').get('barSize'):
                    var.put('ruleWidth', var.get('units_calculateSize')(var.get('group').get('barSize'), var.get('options')))
                    var.get('node').callprop('setAttribute', Js('linethickness'), (var.get('ruleWidth')+Js('em')))
            var.put('style', var.get('genfrac_adjustStyle')(var.get('group').get('size'), var.get('options').get('style')))
            if PyJsStrictNeq(var.get('style').get('size'),var.get('options').get('style').get('size')):
                var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mstyle'), Js([var.get('node')])))
                var.put('isDisplay', (Js('true') if PyJsStrictEq(var.get('style').get('size'),var.get('src_Style').get('DISPLAY').get('size')) else Js('false')))
                var.get('node').callprop('setAttribute', Js('displaystyle'), var.get('isDisplay'))
                var.get('node').callprop('setAttribute', Js('scriptlevel'), Js('0'))
            if ((var.get('group').get('leftDelim')!=var.get(u"null")) or (var.get('group').get('rightDelim')!=var.get(u"null"))):
                var.put('withDelims', Js([]))
                if (var.get('group').get('leftDelim')!=var.get(u"null")):
                    var.put('leftOp', var.get('mathMLTree').get('MathNode').create(Js('mo'), Js([var.get('mathMLTree').get('TextNode').create(var.get('group').get('leftDelim').callprop('replace', Js('\\'), Js('')))])))
                    var.get('leftOp').callprop('setAttribute', Js('fence'), Js('true'))
                    var.get('withDelims').callprop('push', var.get('leftOp'))
                var.get('withDelims').callprop('push', var.get('node'))
                if (var.get('group').get('rightDelim')!=var.get(u"null")):
                    var.put('rightOp', var.get('mathMLTree').get('MathNode').create(Js('mo'), Js([var.get('mathMLTree').get('TextNode').create(var.get('group').get('rightDelim').callprop('replace', Js('\\'), Js('')))])))
                    var.get('rightOp').callprop('setAttribute', Js('fence'), Js('true'))
                    var.get('withDelims').callprop('push', var.get('rightOp'))
                return var.get('buildMathML_makeRow')(var.get('withDelims'))
            return var.get('node')
        PyJs_mathmlBuilder_237_._set_name('mathmlBuilder')
        var.put('genfrac_mathmlBuilder', PyJs_mathmlBuilder_237_)
        def PyJs_LONG_239_(var=var):
            @Js
            def PyJs_handler_238_(_ref, args, this, arguments, var=var):
                var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_238_}, var)
                var.registers(['funcName', 'numer', 'size', 'hasBarLine', 'leftDelim', 'denom', '_ref', 'rightDelim', 'args', 'parser'])
                var.put('parser', var.get('_ref').get('parser'))
                var.put('funcName', var.get('_ref').get('funcName'))
                var.put('numer', var.get('args').get('0'))
                var.put('denom', var.get('args').get('1'))
                pass
                var.put('leftDelim', var.get(u"null"))
                var.put('rightDelim', var.get(u"null"))
                var.put('size', Js('auto'))
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('funcName'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('\\cfrac')):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('\\dfrac')):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('\\frac')):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('\\tfrac')):
                        SWITCHED = True
                        var.put('hasBarLine', Js(True))
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('\\\\atopfrac')):
                        SWITCHED = True
                        var.put('hasBarLine', Js(False))
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('\\dbinom')):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('\\binom')):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('\\tbinom')):
                        SWITCHED = True
                        var.put('hasBarLine', Js(False))
                        var.put('leftDelim', Js('('))
                        var.put('rightDelim', Js(')'))
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('\\\\bracefrac')):
                        SWITCHED = True
                        var.put('hasBarLine', Js(False))
                        var.put('leftDelim', Js('\\{'))
                        var.put('rightDelim', Js('\\}'))
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('\\\\brackfrac')):
                        SWITCHED = True
                        var.put('hasBarLine', Js(False))
                        var.put('leftDelim', Js('['))
                        var.put('rightDelim', Js(']'))
                        break
                    if True:
                        SWITCHED = True
                        PyJsTempException = JsToPyException(var.get('Error').create(Js('Unrecognized genfrac command')))
                        raise PyJsTempException
                    SWITCHED = True
                    break
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('funcName'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('\\cfrac')):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('\\dfrac')):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('\\dbinom')):
                        SWITCHED = True
                        var.put('size', Js('display'))
                        break
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('\\tfrac')):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('\\tbinom')):
                        SWITCHED = True
                        var.put('size', Js('text'))
                        break
                    SWITCHED = True
                    break
                return Js({'type':Js('genfrac'),'mode':var.get('parser').get('mode'),'continued':PyJsStrictEq(var.get('funcName'),Js('\\cfrac')),'numer':var.get('numer'),'denom':var.get('denom'),'hasBarLine':var.get('hasBarLine'),'leftDelim':var.get('leftDelim'),'rightDelim':var.get('rightDelim'),'size':var.get('size'),'barSize':var.get(u"null")})
            PyJs_handler_238_._set_name('handler')
            return var.get('defineFunction')(Js({'type':Js('genfrac'),'names':Js([Js('\\cfrac'), Js('\\dfrac'), Js('\\frac'), Js('\\tfrac'), Js('\\dbinom'), Js('\\binom'), Js('\\tbinom'), Js('\\\\atopfrac'), Js('\\\\bracefrac'), Js('\\\\brackfrac')]),'props':Js({'numArgs':Js(2.0),'greediness':Js(2.0)}),'handler':PyJs_handler_238_,'htmlBuilder':var.get('genfrac_htmlBuilder'),'mathmlBuilder':var.get('genfrac_mathmlBuilder')}))
        PyJs_LONG_239_()
        @Js
        def PyJs_handler_240_(_ref2, this, arguments, var=var):
            var = Scope({'_ref2':_ref2, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_240_}, var)
            var.registers(['funcName', 'replaceWith', 'token', 'parser', '_ref2'])
            var.put('parser', var.get('_ref2').get('parser'))
            var.put('funcName', var.get('_ref2').get('funcName'))
            var.put('token', var.get('_ref2').get('token'))
            pass
            while 1:
                SWITCHED = False
                CONDITION = (var.get('funcName'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\over')):
                    SWITCHED = True
                    var.put('replaceWith', Js('\\frac'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\choose')):
                    SWITCHED = True
                    var.put('replaceWith', Js('\\binom'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\atop')):
                    SWITCHED = True
                    var.put('replaceWith', Js('\\\\atopfrac'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\brace')):
                    SWITCHED = True
                    var.put('replaceWith', Js('\\\\bracefrac'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\brack')):
                    SWITCHED = True
                    var.put('replaceWith', Js('\\\\brackfrac'))
                    break
                if True:
                    SWITCHED = True
                    PyJsTempException = JsToPyException(var.get('Error').create(Js('Unrecognized infix genfrac command')))
                    raise PyJsTempException
                SWITCHED = True
                break
            return Js({'type':Js('infix'),'mode':var.get('parser').get('mode'),'replaceWith':var.get('replaceWith'),'token':var.get('token')})
        PyJs_handler_240_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('infix'),'names':Js([Js('\\over'), Js('\\choose'), Js('\\atop'), Js('\\brace'), Js('\\brack')]),'props':Js({'numArgs':Js(0.0),'infix':Js(True)}),'handler':PyJs_handler_240_}))
        var.put('stylArray', Js([Js('display'), Js('text'), Js('script'), Js('scriptscript')]))
        @Js
        def PyJs_delimFromValue_241_(delimString, this, arguments, var=var):
            var = Scope({'delimString':delimString, 'this':this, 'arguments':arguments, 'delimFromValue':PyJs_delimFromValue_241_}, var)
            var.registers(['delimString', 'delim'])
            var.put('delim', var.get(u"null"))
            if (var.get('delimString').get('length')>Js(0.0)):
                var.put('delim', var.get('delimString'))
                var.put('delim', (var.get(u"null") if PyJsStrictEq(var.get('delim'),Js('.')) else var.get('delim')))
            return var.get('delim')
        PyJs_delimFromValue_241_._set_name('delimFromValue')
        var.put('delimFromValue', PyJs_delimFromValue_241_)
        @Js
        def PyJs_handler_242_(_ref3, args, this, arguments, var=var):
            var = Scope({'_ref3':_ref3, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_242_}, var)
            var.registers(['numer', 'size', 'leftNode', 'rightNode', 'styl', 'barNode', 'hasBarLine', 'leftDelim', 'denom', '_ref3', 'rightDelim', 'barSize', 'textOrd', 'parser', 'args'])
            var.put('parser', var.get('_ref3').get('parser'))
            var.put('numer', var.get('args').get('4'))
            var.put('denom', var.get('args').get('5'))
            var.put('leftNode', var.get('checkNodeType')(var.get('args').get('0'), Js('atom')))
            if var.get('leftNode'):
                var.put('leftNode', var.get('assertAtomFamily')(var.get('args').get('0'), Js('open')))
            var.put('leftDelim', (var.get('delimFromValue')(var.get('leftNode').get('text')) if var.get('leftNode') else var.get(u"null")))
            var.put('rightNode', var.get('checkNodeType')(var.get('args').get('1'), Js('atom')))
            if var.get('rightNode'):
                var.put('rightNode', var.get('assertAtomFamily')(var.get('args').get('1'), Js('close')))
            var.put('rightDelim', (var.get('delimFromValue')(var.get('rightNode').get('text')) if var.get('rightNode') else var.get(u"null")))
            var.put('barNode', var.get('assertNodeType')(var.get('args').get('2'), Js('size')))
            pass
            var.put('barSize', var.get(u"null"))
            if var.get('barNode').get('isBlank'):
                var.put('hasBarLine', Js(True))
            else:
                var.put('barSize', var.get('barNode').get('value'))
                var.put('hasBarLine', (var.get('barSize').get('number')>Js(0.0)))
            var.put('size', Js('auto'))
            var.put('styl', var.get('checkNodeType')(var.get('args').get('3'), Js('ordgroup')))
            if var.get('styl'):
                if (var.get('styl').get('body').get('length')>Js(0.0)):
                    var.put('textOrd', var.get('assertNodeType')(var.get('styl').get('body').get('0'), Js('textord')))
                    var.put('size', var.get('stylArray').get(var.get('Number')(var.get('textOrd').get('text'))))
            else:
                var.put('styl', var.get('assertNodeType')(var.get('args').get('3'), Js('textord')))
                var.put('size', var.get('stylArray').get(var.get('Number')(var.get('styl').get('text'))))
            return Js({'type':Js('genfrac'),'mode':var.get('parser').get('mode'),'numer':var.get('numer'),'denom':var.get('denom'),'continued':Js(False),'hasBarLine':var.get('hasBarLine'),'barSize':var.get('barSize'),'leftDelim':var.get('leftDelim'),'rightDelim':var.get('rightDelim'),'size':var.get('size')})
        PyJs_handler_242_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('genfrac'),'names':Js([Js('\\genfrac')]),'props':Js({'numArgs':Js(6.0),'greediness':Js(6.0),'argTypes':Js([Js('math'), Js('math'), Js('size'), Js('text'), Js('math'), Js('math')])}),'handler':PyJs_handler_242_,'htmlBuilder':var.get('genfrac_htmlBuilder'),'mathmlBuilder':var.get('genfrac_mathmlBuilder')}))
        @Js
        def PyJs_handler_243_(_ref4, args, this, arguments, var=var):
            var = Scope({'_ref4':_ref4, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_243_}, var)
            var.registers(['funcName', '_ref4', 'args', 'token', 'parser'])
            var.put('parser', var.get('_ref4').get('parser'))
            var.put('funcName', var.get('_ref4').get('funcName'))
            var.put('token', var.get('_ref4').get('token'))
            return Js({'type':Js('infix'),'mode':var.get('parser').get('mode'),'replaceWith':Js('\\\\abovefrac'),'size':var.get('assertNodeType')(var.get('args').get('0'), Js('size')).get('value'),'token':var.get('token')})
        PyJs_handler_243_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('infix'),'names':Js([Js('\\above')]),'props':Js({'numArgs':Js(1.0),'argTypes':Js([Js('size')]),'infix':Js(True)}),'handler':PyJs_handler_243_}))
        @Js
        def PyJs_handler_244_(_ref5, args, this, arguments, var=var):
            var = Scope({'_ref5':_ref5, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_244_}, var)
            var.registers(['funcName', 'numer', 'hasBarLine', 'denom', 'barSize', '_ref5', 'args', 'parser'])
            var.put('parser', var.get('_ref5').get('parser'))
            var.put('funcName', var.get('_ref5').get('funcName'))
            var.put('numer', var.get('args').get('0'))
            var.put('barSize', var.get('assert')(var.get('assertNodeType')(var.get('args').get('1'), Js('infix')).get('size')))
            var.put('denom', var.get('args').get('2'))
            var.put('hasBarLine', (var.get('barSize').get('number')>Js(0.0)))
            return Js({'type':Js('genfrac'),'mode':var.get('parser').get('mode'),'numer':var.get('numer'),'denom':var.get('denom'),'continued':Js(False),'hasBarLine':var.get('hasBarLine'),'barSize':var.get('barSize'),'leftDelim':var.get(u"null"),'rightDelim':var.get(u"null"),'size':Js('auto')})
        PyJs_handler_244_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('genfrac'),'names':Js([Js('\\\\abovefrac')]),'props':Js({'numArgs':Js(3.0),'argTypes':Js([Js('math'), Js('size'), Js('math')])}),'handler':PyJs_handler_244_,'htmlBuilder':var.get('genfrac_htmlBuilder'),'mathmlBuilder':var.get('genfrac_mathmlBuilder')}))
        @Js
        def PyJs_htmlBuilder_245_(grp, options, this, arguments, var=var):
            var = Scope({'grp':grp, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_245_}, var)
            var.registers(['grp', 'braceBody', 'group', 'body', 'supSubGroup', 'options', 'vSpan', 'style', 'vlist', 'supSub'])
            var.put('style', var.get('options').get('style'))
            pass
            pass
            var.put('supSub', var.get('checkNodeType')(var.get('grp'), Js('supsub')))
            if var.get('supSub'):
                var.put('supSubGroup', (var.get('buildHTML_buildGroup')(var.get('supSub').get('sup'), var.get('options').callprop('havingStyle', var.get('style').callprop('sup')), var.get('options')) if var.get('supSub').get('sup') else var.get('buildHTML_buildGroup')(var.get('supSub').get('sub'), var.get('options').callprop('havingStyle', var.get('style').callprop('sub')), var.get('options'))))
                var.put('group', var.get('assertNodeType')(var.get('supSub').get('base'), Js('horizBrace')))
            else:
                var.put('group', var.get('assertNodeType')(var.get('grp'), Js('horizBrace')))
            var.put('body', var.get('buildHTML_buildGroup')(var.get('group').get('base'), var.get('options').callprop('havingBaseStyle', var.get('src_Style').get('DISPLAY'))))
            var.put('braceBody', var.get('stretchy').callprop('svgSpan', var.get('group'), var.get('options')))
            pass
            if var.get('group').get('isOver'):
                var.put('vlist', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('firstBaseline'),'children':Js([Js({'type':Js('elem'),'elem':var.get('body')}), Js({'type':Js('kern'),'size':Js(0.1)}), Js({'type':Js('elem'),'elem':var.get('braceBody')})])}), var.get('options')))
                var.get('vlist').get('children').get('0').get('children').get('0').get('children').get('1').get('classes').callprop('push', Js('svg-align'))
            else:
                var.put('vlist', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('bottom'),'positionData':((var.get('body').get('depth')+Js(0.1))+var.get('braceBody').get('height')),'children':Js([Js({'type':Js('elem'),'elem':var.get('braceBody')}), Js({'type':Js('kern'),'size':Js(0.1)}), Js({'type':Js('elem'),'elem':var.get('body')})])}), var.get('options')))
                var.get('vlist').get('children').get('0').get('children').get('0').get('children').get('0').get('classes').callprop('push', Js('svg-align'))
            if var.get('supSubGroup'):
                var.put('vSpan', var.get('buildCommon').callprop('makeSpan', Js([Js('mord'), (Js('mover') if var.get('group').get('isOver') else Js('munder'))]), Js([var.get('vlist')]), var.get('options')))
                if var.get('group').get('isOver'):
                    var.put('vlist', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('firstBaseline'),'children':Js([Js({'type':Js('elem'),'elem':var.get('vSpan')}), Js({'type':Js('kern'),'size':Js(0.2)}), Js({'type':Js('elem'),'elem':var.get('supSubGroup')})])}), var.get('options')))
                else:
                    def PyJs_LONG_246_(var=var):
                        return var.put('vlist', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('bottom'),'positionData':(((var.get('vSpan').get('depth')+Js(0.2))+var.get('supSubGroup').get('height'))+var.get('supSubGroup').get('depth')),'children':Js([Js({'type':Js('elem'),'elem':var.get('supSubGroup')}), Js({'type':Js('kern'),'size':Js(0.2)}), Js({'type':Js('elem'),'elem':var.get('vSpan')})])}), var.get('options')))
                    PyJs_LONG_246_()
            return var.get('buildCommon').callprop('makeSpan', Js([Js('mord'), (Js('mover') if var.get('group').get('isOver') else Js('munder'))]), Js([var.get('vlist')]), var.get('options'))
        PyJs_htmlBuilder_245_._set_name('htmlBuilder')
        var.put('horizBrace_htmlBuilder', PyJs_htmlBuilder_245_)
        @Js
        def PyJs_mathmlBuilder_247_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_247_}, var)
            var.registers(['group', 'options', 'accentNode'])
            var.put('accentNode', var.get('stretchy').callprop('mathMLnode', var.get('group').get('label')))
            return var.get('mathMLTree').get('MathNode').create((Js('mover') if var.get('group').get('isOver') else Js('munder')), Js([var.get('buildMathML_buildGroup')(var.get('group').get('base'), var.get('options')), var.get('accentNode')]))
        PyJs_mathmlBuilder_247_._set_name('mathmlBuilder')
        var.put('horizBrace_mathmlBuilder', PyJs_mathmlBuilder_247_)
        @Js
        def PyJs_handler_248_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_248_}, var)
            var.registers(['parser', 'funcName', '_ref', 'args'])
            var.put('parser', var.get('_ref').get('parser'))
            var.put('funcName', var.get('_ref').get('funcName'))
            return Js({'type':Js('horizBrace'),'mode':var.get('parser').get('mode'),'label':var.get('funcName'),'isOver':JsRegExp('/^\\\\over/').callprop('test', var.get('funcName')),'base':var.get('args').get('0')})
        PyJs_handler_248_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('horizBrace'),'names':Js([Js('\\overbrace'), Js('\\underbrace')]),'props':Js({'numArgs':Js(1.0)}),'handler':PyJs_handler_248_,'htmlBuilder':var.get('horizBrace_htmlBuilder'),'mathmlBuilder':var.get('horizBrace_mathmlBuilder')}))
        @Js
        def PyJs_handler_249_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_249_}, var)
            var.registers(['body', '_ref', 'args', 'parser', 'href'])
            var.put('parser', var.get('_ref').get('parser'))
            var.put('body', var.get('args').get('1'))
            var.put('href', var.get('assertNodeType')(var.get('args').get('0'), Js('url')).get('url'))
            return Js({'type':Js('href'),'mode':var.get('parser').get('mode'),'href':var.get('href'),'body':var.get('defineFunction_ordargument')(var.get('body'))})
        PyJs_handler_249_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_250_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_250_}, var)
            var.registers(['group', 'options', 'elements'])
            var.put('elements', var.get('buildHTML_buildExpression')(var.get('group').get('body'), var.get('options'), Js(False)))
            return var.get('buildCommon').callprop('makeAnchor', var.get('group').get('href'), Js([]), var.get('elements'), var.get('options'))
        PyJs_htmlBuilder_250_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_251_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_251_}, var)
            var.registers(['group', 'options', 'math'])
            var.put('math', var.get('buildExpressionRow')(var.get('group').get('body'), var.get('options')))
            if var.get('math').instanceof(var.get('mathMLTree_MathNode')).neg():
                var.put('math', var.get('mathMLTree_MathNode').create(Js('mrow'), Js([var.get('math')])))
            var.get('math').callprop('setAttribute', Js('href'), var.get('group').get('href'))
            return var.get('math')
        PyJs_mathmlBuilder_251_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('href'),'names':Js([Js('\\href')]),'props':Js({'numArgs':Js(2.0),'argTypes':Js([Js('url'), Js('original')]),'allowedInText':Js(True)}),'handler':PyJs_handler_249_,'htmlBuilder':PyJs_htmlBuilder_250_,'mathmlBuilder':PyJs_mathmlBuilder_251_}))
        @Js
        def PyJs_handler_252_(_ref2, args, this, arguments, var=var):
            var = Scope({'_ref2':_ref2, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_252_}, var)
            var.registers(['c', 'i', 'body', 'chars', 'args', 'parser', 'href', '_ref2'])
            var.put('parser', var.get('_ref2').get('parser'))
            var.put('href', var.get('assertNodeType')(var.get('args').get('0'), Js('url')).get('url'))
            var.put('chars', Js([]))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('href').get('length')):
                try:
                    var.put('c', var.get('href').get(var.get('i')))
                    if PyJsStrictEq(var.get('c'),Js('~')):
                        var.put('c', Js('\\textasciitilde'))
                    var.get('chars').callprop('push', Js({'type':Js('textord'),'mode':Js('text'),'text':var.get('c')}))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('body', Js({'type':Js('text'),'mode':var.get('parser').get('mode'),'font':Js('\\texttt'),'body':var.get('chars')}))
            return Js({'type':Js('href'),'mode':var.get('parser').get('mode'),'href':var.get('href'),'body':var.get('defineFunction_ordargument')(var.get('body'))})
        PyJs_handler_252_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('href'),'names':Js([Js('\\url')]),'props':Js({'numArgs':Js(1.0),'argTypes':Js([Js('url')]),'allowedInText':Js(True)}),'handler':PyJs_handler_252_}))
        @Js
        def PyJs_handler_253_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_253_}, var)
            var.registers(['parser', '_ref', 'args'])
            var.put('parser', var.get('_ref').get('parser'))
            return Js({'type':Js('htmlmathml'),'mode':var.get('parser').get('mode'),'html':var.get('defineFunction_ordargument')(var.get('args').get('0')),'mathml':var.get('defineFunction_ordargument')(var.get('args').get('1'))})
        PyJs_handler_253_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_254_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_254_}, var)
            var.registers(['group', 'options', 'elements'])
            var.put('elements', var.get('buildHTML_buildExpression')(var.get('group').get('html'), var.get('options'), Js(False)))
            return var.get('buildCommon').callprop('makeFragment', var.get('elements'))
        PyJs_htmlBuilder_254_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_255_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_255_}, var)
            var.registers(['group', 'options'])
            return var.get('buildExpressionRow')(var.get('group').get('mathml'), var.get('options'))
        PyJs_mathmlBuilder_255_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('htmlmathml'),'names':Js([Js('\\html@mathml')]),'props':Js({'numArgs':Js(2.0),'allowedInText':Js(True)}),'handler':PyJs_handler_253_,'htmlBuilder':PyJs_htmlBuilder_254_,'mathmlBuilder':PyJs_mathmlBuilder_255_}))
        @Js
        def PyJs_handler_256_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_256_}, var)
            var.registers(['funcName', 'mathFunction', 'size', 'muUnit', '_ref', 'args', 'parser'])
            var.put('parser', var.get('_ref').get('parser'))
            var.put('funcName', var.get('_ref').get('funcName'))
            var.put('size', var.get('assertNodeType')(var.get('args').get('0'), Js('size')))
            if var.get('parser').get('settings').get('strict'):
                var.put('mathFunction', PyJsStrictEq(var.get('funcName').get('1'),Js('m')))
                var.put('muUnit', PyJsStrictEq(var.get('size').get('value').get('unit'),Js('mu')))
                if var.get('mathFunction'):
                    if var.get('muUnit').neg():
                        var.get('parser').get('settings').callprop('reportNonstrict', Js('mathVsTextUnits'), (((Js("LaTeX's ")+var.get('funcName'))+Js(' supports only mu units, '))+((Js('not ')+var.get('size').get('value').get('unit'))+Js(' units'))))
                    if PyJsStrictNeq(var.get('parser').get('mode'),Js('math')):
                        var.get('parser').get('settings').callprop('reportNonstrict', Js('mathVsTextUnits'), ((Js("LaTeX's ")+var.get('funcName'))+Js(' works only in math mode')))
                else:
                    if var.get('muUnit'):
                        var.get('parser').get('settings').callprop('reportNonstrict', Js('mathVsTextUnits'), ((Js("LaTeX's ")+var.get('funcName'))+Js(" doesn't support mu units")))
            return Js({'type':Js('kern'),'mode':var.get('parser').get('mode'),'dimension':var.get('size').get('value')})
        PyJs_handler_256_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_257_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_257_}, var)
            var.registers(['group', 'options'])
            return var.get('buildCommon').callprop('makeGlue', var.get('group').get('dimension'), var.get('options'))
        PyJs_htmlBuilder_257_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_258_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_258_}, var)
            var.registers(['group', 'options', 'dimension'])
            var.put('dimension', var.get('units_calculateSize')(var.get('group').get('dimension'), var.get('options')))
            return var.get('mathMLTree').get('SpaceNode').create(var.get('dimension'))
        PyJs_mathmlBuilder_258_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('kern'),'names':Js([Js('\\kern'), Js('\\mkern'), Js('\\hskip'), Js('\\mskip')]),'props':Js({'numArgs':Js(1.0),'argTypes':Js([Js('size')]),'allowedInText':Js(True)}),'handler':PyJs_handler_256_,'htmlBuilder':PyJs_htmlBuilder_257_,'mathmlBuilder':PyJs_mathmlBuilder_258_}))
        @Js
        def PyJs_handler_259_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_259_}, var)
            var.registers(['funcName', 'body', '_ref', 'args', 'parser'])
            var.put('parser', var.get('_ref').get('parser'))
            var.put('funcName', var.get('_ref').get('funcName'))
            var.put('body', var.get('args').get('0'))
            return Js({'type':Js('lap'),'mode':var.get('parser').get('mode'),'alignment':var.get('funcName').callprop('slice', Js(5.0)),'body':var.get('body')})
        PyJs_handler_259_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_260_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_260_}, var)
            var.registers(['group', 'options', 'node', 'inner', 'fix', 'strut'])
            pass
            if PyJsStrictEq(var.get('group').get('alignment'),Js('clap')):
                var.put('inner', var.get('buildCommon').callprop('makeSpan', Js([]), Js([var.get('buildHTML_buildGroup')(var.get('group').get('body'), var.get('options'))])))
                var.put('inner', var.get('buildCommon').callprop('makeSpan', Js([Js('inner')]), Js([var.get('inner')]), var.get('options')))
            else:
                var.put('inner', var.get('buildCommon').callprop('makeSpan', Js([Js('inner')]), Js([var.get('buildHTML_buildGroup')(var.get('group').get('body'), var.get('options'))])))
            var.put('fix', var.get('buildCommon').callprop('makeSpan', Js([Js('fix')]), Js([])))
            var.put('node', var.get('buildCommon').callprop('makeSpan', Js([var.get('group').get('alignment')]), Js([var.get('inner'), var.get('fix')]), var.get('options')))
            var.put('strut', var.get('buildCommon').callprop('makeSpan', Js([Js('strut')])))
            var.get('strut').get('style').put('height', ((var.get('node').get('height')+var.get('node').get('depth'))+Js('em')))
            var.get('strut').get('style').put('verticalAlign', ((-var.get('node').get('depth'))+Js('em')))
            var.get('node').get('children').callprop('unshift', var.get('strut'))
            var.put('node', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('firstBaseline'),'children':Js([Js({'type':Js('elem'),'elem':var.get('node')})])}), var.get('options')))
            return var.get('buildCommon').callprop('makeSpan', Js([Js('mord')]), Js([var.get('node')]), var.get('options'))
        PyJs_htmlBuilder_260_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_261_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_261_}, var)
            var.registers(['node', 'group', 'options', 'offset'])
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mpadded'), Js([var.get('buildMathML_buildGroup')(var.get('group').get('body'), var.get('options'))])))
            if PyJsStrictNeq(var.get('group').get('alignment'),Js('rlap')):
                var.put('offset', (Js('-1') if PyJsStrictEq(var.get('group').get('alignment'),Js('llap')) else Js('-0.5')))
                var.get('node').callprop('setAttribute', Js('lspace'), (var.get('offset')+Js('width')))
            var.get('node').callprop('setAttribute', Js('width'), Js('0px'))
            return var.get('node')
        PyJs_mathmlBuilder_261_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('lap'),'names':Js([Js('\\mathllap'), Js('\\mathrlap'), Js('\\mathclap')]),'props':Js({'numArgs':Js(1.0),'allowedInText':Js(True)}),'handler':PyJs_handler_259_,'htmlBuilder':PyJs_htmlBuilder_260_,'mathmlBuilder':PyJs_mathmlBuilder_261_}))
        @Js
        def PyJs_handler_262_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_262_}, var)
            var.registers(['funcName', 'body', 'outerMode', '_ref', 'args', 'parser', 'close'])
            var.put('funcName', var.get('_ref').get('funcName'))
            var.put('parser', var.get('_ref').get('parser'))
            var.put('outerMode', var.get('parser').get('mode'))
            var.get('parser').callprop('switchMode', Js('math'))
            var.put('close', (Js('\\)') if PyJsStrictEq(var.get('funcName'),Js('\\(')) else Js('$')))
            var.put('body', var.get('parser').callprop('parseExpression', Js(False), var.get('close')))
            var.get('parser').callprop('expect', var.get('close'), Js(False))
            var.get('parser').callprop('switchMode', var.get('outerMode'))
            var.get('parser').callprop('consume')
            return Js({'type':Js('styling'),'mode':var.get('parser').get('mode'),'style':Js('text'),'body':var.get('body')})
        PyJs_handler_262_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('styling'),'names':Js([Js('\\('), Js('$')]),'props':Js({'numArgs':Js(0.0),'allowedInText':Js(True),'allowedInMath':Js(False),'consumeMode':Js('math')}),'handler':PyJs_handler_262_}))
        @Js
        def PyJs_handler_263_(context, args, this, arguments, var=var):
            var = Scope({'context':context, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_263_}, var)
            var.registers(['context', 'args'])
            PyJsTempException = JsToPyException(var.get('src_ParseError').create((Js('Mismatched ')+var.get('context').get('funcName'))))
            raise PyJsTempException
        PyJs_handler_263_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('text'),'names':Js([Js('\\)'), Js('\\]')]),'props':Js({'numArgs':Js(0.0),'allowedInText':Js(True),'allowedInMath':Js(False)}),'handler':PyJs_handler_263_}))
        @Js
        def PyJs_chooseMathStyle_264_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'chooseMathStyle':PyJs_chooseMathStyle_264_}, var)
            var.registers(['group', 'options'])
            while 1:
                SWITCHED = False
                CONDITION = (var.get('options').get('style').get('size'))
                if SWITCHED or PyJsStrictEq(CONDITION, var.get('src_Style').get('DISPLAY').get('size')):
                    SWITCHED = True
                    return var.get('group').get('display')
                if SWITCHED or PyJsStrictEq(CONDITION, var.get('src_Style').get('TEXT').get('size')):
                    SWITCHED = True
                    return var.get('group').get('text')
                if SWITCHED or PyJsStrictEq(CONDITION, var.get('src_Style').get('SCRIPT').get('size')):
                    SWITCHED = True
                    return var.get('group').get('script')
                if SWITCHED or PyJsStrictEq(CONDITION, var.get('src_Style').get('SCRIPTSCRIPT').get('size')):
                    SWITCHED = True
                    return var.get('group').get('scriptscript')
                if True:
                    SWITCHED = True
                    return var.get('group').get('text')
                SWITCHED = True
                break
        PyJs_chooseMathStyle_264_._set_name('chooseMathStyle')
        var.put('mathchoice_chooseMathStyle', PyJs_chooseMathStyle_264_)
        @Js
        def PyJs_handler_265_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_265_}, var)
            var.registers(['parser', '_ref', 'args'])
            var.put('parser', var.get('_ref').get('parser'))
            return Js({'type':Js('mathchoice'),'mode':var.get('parser').get('mode'),'display':var.get('defineFunction_ordargument')(var.get('args').get('0')),'text':var.get('defineFunction_ordargument')(var.get('args').get('1')),'script':var.get('defineFunction_ordargument')(var.get('args').get('2')),'scriptscript':var.get('defineFunction_ordargument')(var.get('args').get('3'))})
        PyJs_handler_265_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_266_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_266_}, var)
            var.registers(['body', 'group', 'options', 'elements'])
            var.put('body', var.get('mathchoice_chooseMathStyle')(var.get('group'), var.get('options')))
            var.put('elements', var.get('buildHTML_buildExpression')(var.get('body'), var.get('options'), Js(False)))
            return var.get('buildCommon').callprop('makeFragment', var.get('elements'))
        PyJs_htmlBuilder_266_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_267_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_267_}, var)
            var.registers(['body', 'group', 'options'])
            var.put('body', var.get('mathchoice_chooseMathStyle')(var.get('group'), var.get('options')))
            return var.get('buildExpressionRow')(var.get('body'), var.get('options'))
        PyJs_mathmlBuilder_267_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('mathchoice'),'names':Js([Js('\\mathchoice')]),'props':Js({'numArgs':Js(4.0)}),'handler':PyJs_handler_265_,'htmlBuilder':PyJs_htmlBuilder_266_,'mathmlBuilder':PyJs_mathmlBuilder_267_}))
        var.put('noSuccessor', Js([Js('\\smallint')]))
        @Js
        def PyJs_htmlBuilder_268_(grp, options, this, arguments, var=var):
            var = Scope({'grp':grp, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_268_}, var)
            var.registers(['elem', 'oval', 'sub', 'baseShift', 'sup', 'inner', 'stash', 'subGroup', 'i', 'options', 'top', '_elem', 'base', '_bottom', 'large', 'output', 'finalGroup', 'italic', 'bottom', 'grp', 'fontName', 'supGroup', 'group', 'slant', 'hasLimits', 'style', 'supSub'])
            pass
            pass
            var.put('hasLimits', Js(False))
            pass
            var.put('supSub', var.get('checkNodeType')(var.get('grp'), Js('supsub')))
            if var.get('supSub'):
                var.put('supGroup', var.get('supSub').get('sup'))
                var.put('subGroup', var.get('supSub').get('sub'))
                var.put('group', var.get('assertNodeType')(var.get('supSub').get('base'), Js('op')))
                var.put('hasLimits', Js(True))
            else:
                var.put('group', var.get('assertNodeType')(var.get('grp'), Js('op')))
            var.put('style', var.get('options').get('style'))
            var.put('large', Js(False))
            if ((PyJsStrictEq(var.get('style').get('size'),var.get('src_Style').get('DISPLAY').get('size')) and var.get('group').get('symbol')) and var.get('utils').callprop('contains', var.get('noSuccessor'), var.get('group').get('name')).neg()):
                var.put('large', Js(True))
            pass
            if var.get('group').get('symbol'):
                var.put('fontName', (Js('Size2-Regular') if var.get('large') else Js('Size1-Regular')))
                var.put('stash', Js(''))
                if (PyJsStrictEq(var.get('group').get('name'),Js('\\oiint')) or PyJsStrictEq(var.get('group').get('name'),Js('\\oiiint'))):
                    var.put('stash', var.get('group').get('name').callprop('substr', Js(1.0)))
                    var.get('group').put('name', (Js('\\iint') if PyJsStrictEq(var.get('stash'),Js('oiint')) else Js('\\iiint')))
                var.put('base', var.get('buildCommon').callprop('makeSymbol', var.get('group').get('name'), var.get('fontName'), Js('math'), var.get('options'), Js([Js('mop'), Js('op-symbol'), (Js('large-op') if var.get('large') else Js('small-op'))])))
                if (var.get('stash').get('length')>Js(0.0)):
                    var.put('italic', var.get('base').get('italic'))
                    var.put('oval', var.get('buildCommon').callprop('staticSvg', ((var.get('stash')+Js('Size'))+(Js('2') if var.get('large') else Js('1'))), var.get('options')))
                    var.put('base', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('individualShift'),'children':Js([Js({'type':Js('elem'),'elem':var.get('base'),'shift':Js(0.0)}), Js({'type':Js('elem'),'elem':var.get('oval'),'shift':(Js(0.08) if var.get('large') else Js(0.0))})])}), var.get('options')))
                    var.get('group').put('name', (Js('\\')+var.get('stash')))
                    var.get('base').get('classes').callprop('unshift', Js('mop'))
                    var.get('base').put('italic', var.get('italic'))
            else:
                if var.get('group').get('body'):
                    var.put('inner', var.get('buildHTML_buildExpression')(var.get('group').get('body'), var.get('options'), Js(True)))
                    if (PyJsStrictEq(var.get('inner').get('length'),Js(1.0)) and var.get('inner').get('0').instanceof(var.get('domTree_SymbolNode'))):
                        var.put('base', var.get('inner').get('0'))
                        var.get('base').get('classes').put('0', Js('mop'))
                    else:
                        var.put('base', var.get('buildCommon').callprop('makeSpan', Js([Js('mop')]), var.get('buildCommon').callprop('tryCombineChars', var.get('inner')), var.get('options')))
                else:
                    var.put('output', Js([]))
                    #for JS loop
                    var.put('i', Js(1.0))
                    while (var.get('i')<var.get('group').get('name').get('length')):
                        try:
                            var.get('output').callprop('push', var.get('buildCommon').callprop('mathsym', var.get('group').get('name').get(var.get('i')), var.get('group').get('mode')))
                        finally:
                                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                    var.put('base', var.get('buildCommon').callprop('makeSpan', Js([Js('mop')]), var.get('output'), var.get('options')))
            var.put('baseShift', Js(0.0))
            var.put('slant', Js(0.0))
            if (((var.get('base').instanceof(var.get('domTree_SymbolNode')) or PyJsStrictEq(var.get('group').get('name'),Js('\\oiint'))) or PyJsStrictEq(var.get('group').get('name'),Js('\\oiiint'))) and var.get('group').get('suppressBaseShift').neg()):
                var.put('baseShift', (((var.get('base').get('height')-var.get('base').get('depth'))/Js(2.0))-var.get('options').callprop('fontMetrics').get('axisHeight')))
                var.put('slant', var.get('base').get('italic'))
            if var.get('hasLimits'):
                var.put('base', var.get('buildCommon').callprop('makeSpan', Js([]), Js([var.get('base')])))
                pass
                pass
                if var.get('supGroup'):
                    var.put('elem', var.get('buildHTML_buildGroup')(var.get('supGroup'), var.get('options').callprop('havingStyle', var.get('style').callprop('sup')), var.get('options')))
                    var.put('sup', Js({'elem':var.get('elem'),'kern':var.get('Math').callprop('max', var.get('options').callprop('fontMetrics').get('bigOpSpacing1'), (var.get('options').callprop('fontMetrics').get('bigOpSpacing3')-var.get('elem').get('depth')))}))
                if var.get('subGroup'):
                    var.put('_elem', var.get('buildHTML_buildGroup')(var.get('subGroup'), var.get('options').callprop('havingStyle', var.get('style').callprop('sub')), var.get('options')))
                    var.put('sub', Js({'elem':var.get('_elem'),'kern':var.get('Math').callprop('max', var.get('options').callprop('fontMetrics').get('bigOpSpacing2'), (var.get('options').callprop('fontMetrics').get('bigOpSpacing4')-var.get('_elem').get('height')))}))
                pass
                if (var.get('sup') and var.get('sub')):
                    var.put('bottom', (((((var.get('options').callprop('fontMetrics').get('bigOpSpacing5')+var.get('sub').get('elem').get('height'))+var.get('sub').get('elem').get('depth'))+var.get('sub').get('kern'))+var.get('base').get('depth'))+var.get('baseShift')))
                    def PyJs_LONG_269_(var=var):
                        return var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('bottom'),'positionData':var.get('bottom'),'children':Js([Js({'type':Js('kern'),'size':var.get('options').callprop('fontMetrics').get('bigOpSpacing5')}), Js({'type':Js('elem'),'elem':var.get('sub').get('elem'),'marginLeft':((-var.get('slant'))+Js('em'))}), Js({'type':Js('kern'),'size':var.get('sub').get('kern')}), Js({'type':Js('elem'),'elem':var.get('base')}), Js({'type':Js('kern'),'size':var.get('sup').get('kern')}), Js({'type':Js('elem'),'elem':var.get('sup').get('elem'),'marginLeft':(var.get('slant')+Js('em'))}), Js({'type':Js('kern'),'size':var.get('options').callprop('fontMetrics').get('bigOpSpacing5')})])}), var.get('options'))
                    var.put('finalGroup', PyJs_LONG_269_())
                else:
                    if var.get('sub'):
                        var.put('top', (var.get('base').get('height')-var.get('baseShift')))
                        def PyJs_LONG_270_(var=var):
                            return var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('top'),'positionData':var.get('top'),'children':Js([Js({'type':Js('kern'),'size':var.get('options').callprop('fontMetrics').get('bigOpSpacing5')}), Js({'type':Js('elem'),'elem':var.get('sub').get('elem'),'marginLeft':((-var.get('slant'))+Js('em'))}), Js({'type':Js('kern'),'size':var.get('sub').get('kern')}), Js({'type':Js('elem'),'elem':var.get('base')})])}), var.get('options'))
                        var.put('finalGroup', PyJs_LONG_270_())
                    else:
                        if var.get('sup'):
                            var.put('_bottom', (var.get('base').get('depth')+var.get('baseShift')))
                            def PyJs_LONG_271_(var=var):
                                return var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('bottom'),'positionData':var.get('_bottom'),'children':Js([Js({'type':Js('elem'),'elem':var.get('base')}), Js({'type':Js('kern'),'size':var.get('sup').get('kern')}), Js({'type':Js('elem'),'elem':var.get('sup').get('elem'),'marginLeft':(var.get('slant')+Js('em'))}), Js({'type':Js('kern'),'size':var.get('options').callprop('fontMetrics').get('bigOpSpacing5')})])}), var.get('options'))
                            var.put('finalGroup', PyJs_LONG_271_())
                        else:
                            return var.get('base')
                return var.get('buildCommon').callprop('makeSpan', Js([Js('mop'), Js('op-limits')]), Js([var.get('finalGroup')]), var.get('options'))
            else:
                if var.get('baseShift'):
                    var.get('base').get('style').put('position', Js('relative'))
                    var.get('base').get('style').put('top', (var.get('baseShift')+Js('em')))
                return var.get('base')
        PyJs_htmlBuilder_268_._set_name('htmlBuilder')
        var.put('op_htmlBuilder', PyJs_htmlBuilder_268_)
        @Js
        def PyJs_mathmlBuilder_272_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_272_}, var)
            var.registers(['node', 'group', 'options', 'operator'])
            pass
            if var.get('group').get('symbol'):
                var.put('node', var.get('mathMLTree_MathNode').create(Js('mo'), Js([var.get('buildMathML_makeText')(var.get('group').get('name'), var.get('group').get('mode'))])))
                if var.get('utils').callprop('contains', var.get('noSuccessor'), var.get('group').get('name')):
                    var.get('node').callprop('setAttribute', Js('largeop'), Js('false'))
            else:
                if var.get('group').get('body'):
                    var.put('node', var.get('mathMLTree_MathNode').create(Js('mo'), var.get('buildMathML_buildExpression')(var.get('group').get('body'), var.get('options'))))
                else:
                    var.put('node', var.get('mathMLTree_MathNode').create(Js('mi'), Js([var.get('mathMLTree_TextNode').create(var.get('group').get('name').callprop('slice', Js(1.0)))])))
                    var.put('operator', var.get('mathMLTree_MathNode').create(Js('mo'), Js([var.get('buildMathML_makeText')(Js('\u2061'), Js('text'))])))
                    if var.get('group').get('parentIsSupSub'):
                        var.put('node', var.get('mathMLTree_MathNode').create(Js('mo'), Js([var.get('node'), var.get('operator')])))
                    else:
                        var.put('node', var.get('newDocumentFragment')(Js([var.get('node'), var.get('operator')])))
            return var.get('node')
        PyJs_mathmlBuilder_272_._set_name('mathmlBuilder')
        var.put('op_mathmlBuilder', PyJs_mathmlBuilder_272_)
        var.put('singleCharBigOps', Js({'∏':Js('\\prod'),'∐':Js('\\coprod'),'∑':Js('\\sum'),'⋀':Js('\\bigwedge'),'⋁':Js('\\bigvee'),'⋂':Js('\\bigcap'),'⋃':Js('\\bigcup'),'⨀':Js('\\bigodot'),'⨁':Js('\\bigoplus'),'⨂':Js('\\bigotimes'),'⨄':Js('\\biguplus'),'⨆':Js('\\bigsqcup')}))
        def PyJs_LONG_274_(var=var):
            @Js
            def PyJs_handler_273_(_ref, args, this, arguments, var=var):
                var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_273_}, var)
                var.registers(['funcName', 'fName', '_ref', 'args', 'parser'])
                var.put('parser', var.get('_ref').get('parser'))
                var.put('funcName', var.get('_ref').get('funcName'))
                var.put('fName', var.get('funcName'))
                if PyJsStrictEq(var.get('fName').get('length'),Js(1.0)):
                    var.put('fName', var.get('singleCharBigOps').get(var.get('fName')))
                return Js({'type':Js('op'),'mode':var.get('parser').get('mode'),'limits':Js(True),'parentIsSupSub':Js(False),'symbol':Js(True),'name':var.get('fName')})
            PyJs_handler_273_._set_name('handler')
            return var.get('defineFunction')(Js({'type':Js('op'),'names':Js([Js('\\coprod'), Js('\\bigvee'), Js('\\bigwedge'), Js('\\biguplus'), Js('\\bigcap'), Js('\\bigcup'), Js('\\intop'), Js('\\prod'), Js('\\sum'), Js('\\bigotimes'), Js('\\bigoplus'), Js('\\bigodot'), Js('\\bigsqcup'), Js('\\smallint'), Js('∏'), Js('∐'), Js('∑'), Js('⋀'), Js('⋁'), Js('⋂'), Js('⋃'), Js('⨀'), Js('⨁'), Js('⨂'), Js('⨄'), Js('⨆')]),'props':Js({'numArgs':Js(0.0)}),'handler':PyJs_handler_273_,'htmlBuilder':var.get('op_htmlBuilder'),'mathmlBuilder':var.get('op_mathmlBuilder')}))
        PyJs_LONG_274_()
        @Js
        def PyJs_handler_275_(_ref2, args, this, arguments, var=var):
            var = Scope({'_ref2':_ref2, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_275_}, var)
            var.registers(['body', 'parser', 'args', '_ref2'])
            var.put('parser', var.get('_ref2').get('parser'))
            var.put('body', var.get('args').get('0'))
            return Js({'type':Js('op'),'mode':var.get('parser').get('mode'),'limits':Js(False),'parentIsSupSub':Js(False),'symbol':Js(False),'body':var.get('defineFunction_ordargument')(var.get('body'))})
        PyJs_handler_275_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('op'),'names':Js([Js('\\mathop')]),'props':Js({'numArgs':Js(1.0)}),'handler':PyJs_handler_275_,'htmlBuilder':var.get('op_htmlBuilder'),'mathmlBuilder':var.get('op_mathmlBuilder')}))
        var.put('singleCharIntegrals', Js({'∫':Js('\\int'),'∬':Js('\\iint'),'∭':Js('\\iiint'),'∮':Js('\\oint'),'∯':Js('\\oiint'),'∰':Js('\\oiiint')}))
        def PyJs_LONG_277_(var=var):
            @Js
            def PyJs_handler_276_(_ref3, this, arguments, var=var):
                var = Scope({'_ref3':_ref3, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_276_}, var)
                var.registers(['parser', 'funcName', '_ref3'])
                var.put('parser', var.get('_ref3').get('parser'))
                var.put('funcName', var.get('_ref3').get('funcName'))
                return Js({'type':Js('op'),'mode':var.get('parser').get('mode'),'limits':Js(False),'parentIsSupSub':Js(False),'symbol':Js(False),'name':var.get('funcName')})
            PyJs_handler_276_._set_name('handler')
            return var.get('defineFunction')(Js({'type':Js('op'),'names':Js([Js('\\arcsin'), Js('\\arccos'), Js('\\arctan'), Js('\\arctg'), Js('\\arcctg'), Js('\\arg'), Js('\\ch'), Js('\\cos'), Js('\\cosec'), Js('\\cosh'), Js('\\cot'), Js('\\cotg'), Js('\\coth'), Js('\\csc'), Js('\\ctg'), Js('\\cth'), Js('\\deg'), Js('\\dim'), Js('\\exp'), Js('\\hom'), Js('\\ker'), Js('\\lg'), Js('\\ln'), Js('\\log'), Js('\\sec'), Js('\\sin'), Js('\\sinh'), Js('\\sh'), Js('\\tan'), Js('\\tanh'), Js('\\tg'), Js('\\th')]),'props':Js({'numArgs':Js(0.0)}),'handler':PyJs_handler_276_,'htmlBuilder':var.get('op_htmlBuilder'),'mathmlBuilder':var.get('op_mathmlBuilder')}))
        PyJs_LONG_277_()
        @Js
        def PyJs_handler_278_(_ref4, this, arguments, var=var):
            var = Scope({'_ref4':_ref4, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_278_}, var)
            var.registers(['parser', 'funcName', '_ref4'])
            var.put('parser', var.get('_ref4').get('parser'))
            var.put('funcName', var.get('_ref4').get('funcName'))
            return Js({'type':Js('op'),'mode':var.get('parser').get('mode'),'limits':Js(True),'parentIsSupSub':Js(False),'symbol':Js(False),'name':var.get('funcName')})
        PyJs_handler_278_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('op'),'names':Js([Js('\\det'), Js('\\gcd'), Js('\\inf'), Js('\\lim'), Js('\\max'), Js('\\min'), Js('\\Pr'), Js('\\sup')]),'props':Js({'numArgs':Js(0.0)}),'handler':PyJs_handler_278_,'htmlBuilder':var.get('op_htmlBuilder'),'mathmlBuilder':var.get('op_mathmlBuilder')}))
        @Js
        def PyJs_handler_279_(_ref5, this, arguments, var=var):
            var = Scope({'_ref5':_ref5, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_279_}, var)
            var.registers(['_ref5', 'parser', 'funcName', 'fName'])
            var.put('parser', var.get('_ref5').get('parser'))
            var.put('funcName', var.get('_ref5').get('funcName'))
            var.put('fName', var.get('funcName'))
            if PyJsStrictEq(var.get('fName').get('length'),Js(1.0)):
                var.put('fName', var.get('singleCharIntegrals').get(var.get('fName')))
            return Js({'type':Js('op'),'mode':var.get('parser').get('mode'),'limits':Js(False),'parentIsSupSub':Js(False),'symbol':Js(True),'name':var.get('fName')})
        PyJs_handler_279_._set_name('handler')
        var.get('defineFunction')(Js({'type':Js('op'),'names':Js([Js('\\int'), Js('\\iint'), Js('\\iiint'), Js('\\oint'), Js('\\oiint'), Js('\\oiiint'), Js('∫'), Js('∬'), Js('∭'), Js('∮'), Js('∯'), Js('∰')]),'props':Js({'numArgs':Js(0.0)}),'handler':PyJs_handler_279_,'htmlBuilder':var.get('op_htmlBuilder'),'mathmlBuilder':var.get('op_mathmlBuilder')}))
        @Js
        def PyJs_handler_280_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_280_}, var)
            var.registers(['body', 'parser', '_ref', 'args'])
            var.put('parser', var.get('_ref').get('parser'))
            var.put('body', var.get('args').get('0'))
            return Js({'type':Js('operatorname'),'mode':var.get('parser').get('mode'),'body':var.get('defineFunction_ordargument')(var.get('body'))})
        PyJs_handler_280_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_281_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_281_}, var)
            var.registers(['i', 'expression', 'body', 'group', 'child', 'options'])
            if (var.get('group').get('body').get('length')>Js(0.0)):
                @Js
                def PyJs_anonymous_282_(child, this, arguments, var=var):
                    var = Scope({'child':child, 'this':this, 'arguments':arguments}, var)
                    var.registers(['child', 'childText'])
                    var.put('childText', var.get('child').get('text'))
                    if PyJsStrictEq(var.get('childText',throw=False).typeof(),Js('string')):
                        return Js({'type':Js('textord'),'mode':var.get('child').get('mode'),'text':var.get('childText')})
                    else:
                        return var.get('child')
                PyJs_anonymous_282_._set_name('anonymous')
                var.put('body', var.get('group').get('body').callprop('map', PyJs_anonymous_282_))
                var.put('expression', var.get('buildHTML_buildExpression')(var.get('body'), var.get('options').callprop('withFont', Js('mathrm')), Js(True)))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('expression').get('length')):
                    try:
                        var.put('child', var.get('expression').get(var.get('i')))
                        if var.get('child').instanceof(var.get('domTree_SymbolNode')):
                            var.get('child').put('text', var.get('child').get('text').callprop('replace', JsRegExp('/\\u2212/'), Js('-')).callprop('replace', JsRegExp('/\\u2217/'), Js('*')))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                return var.get('buildCommon').callprop('makeSpan', Js([Js('mop')]), var.get('expression'), var.get('options'))
            else:
                return var.get('buildCommon').callprop('makeSpan', Js([Js('mop')]), Js([]), var.get('options'))
        PyJs_htmlBuilder_281_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_283_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_283_}, var)
            var.registers(['i', 'expression', 'group', 'options', 'child', 'isAllString', 'operator', 'node', 'identifier', 'word'])
            var.put('expression', var.get('buildMathML_buildExpression')(var.get('group').get('body'), var.get('options').callprop('withFont', Js('mathrm'))))
            var.put('isAllString', Js(True))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('expression').get('length')):
                try:
                    var.put('node', var.get('expression').get(var.get('i')))
                    if var.get('node').instanceof(var.get('mathMLTree').get('SpaceNode')):
                        pass
                    else:
                        if var.get('node').instanceof(var.get('mathMLTree').get('MathNode')):
                            while 1:
                                SWITCHED = False
                                CONDITION = (var.get('node').get('type'))
                                if SWITCHED or PyJsStrictEq(CONDITION, Js('mi')):
                                    SWITCHED = True
                                    pass
                                if SWITCHED or PyJsStrictEq(CONDITION, Js('mn')):
                                    SWITCHED = True
                                    pass
                                if SWITCHED or PyJsStrictEq(CONDITION, Js('ms')):
                                    SWITCHED = True
                                    pass
                                if SWITCHED or PyJsStrictEq(CONDITION, Js('mspace')):
                                    SWITCHED = True
                                    pass
                                if SWITCHED or PyJsStrictEq(CONDITION, Js('mtext')):
                                    SWITCHED = True
                                    break
                                if SWITCHED or PyJsStrictEq(CONDITION, Js('mo')):
                                    SWITCHED = True
                                    var.put('child', var.get('node').get('children').get('0'))
                                    if (PyJsStrictEq(var.get('node').get('children').get('length'),Js(1.0)) and var.get('child').instanceof(var.get('mathMLTree').get('TextNode'))):
                                        var.get('child').put('text', var.get('child').get('text').callprop('replace', JsRegExp('/\\u2212/'), Js('-')).callprop('replace', JsRegExp('/\\u2217/'), Js('*')))
                                    else:
                                        var.put('isAllString', Js(False))
                                    break
                                if True:
                                    SWITCHED = True
                                    var.put('isAllString', Js(False))
                                SWITCHED = True
                                break
                        else:
                            var.put('isAllString', Js(False))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            if var.get('isAllString'):
                @Js
                def PyJs_anonymous_284_(node, this, arguments, var=var):
                    var = Scope({'node':node, 'this':this, 'arguments':arguments}, var)
                    var.registers(['node'])
                    return var.get('node').callprop('toText')
                PyJs_anonymous_284_._set_name('anonymous')
                var.put('word', var.get('expression').callprop('map', PyJs_anonymous_284_).callprop('join', Js('')))
                var.put('expression', Js([var.get('mathMLTree').get('TextNode').create(var.get('word'))]))
            var.put('identifier', var.get('mathMLTree').get('MathNode').create(Js('mi'), var.get('expression')))
            var.get('identifier').callprop('setAttribute', Js('mathvariant'), Js('normal'))
            var.put('operator', var.get('mathMLTree').get('MathNode').create(Js('mo'), Js([var.get('buildMathML_makeText')(Js('\u2061'), Js('text'))])))
            return var.get('mathMLTree').callprop('newDocumentFragment', Js([var.get('identifier'), var.get('operator')]))
        PyJs_mathmlBuilder_283_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('operatorname'),'names':Js([Js('\\operatorname')]),'props':Js({'numArgs':Js(1.0)}),'handler':PyJs_handler_280_,'htmlBuilder':PyJs_htmlBuilder_281_,'mathmlBuilder':PyJs_mathmlBuilder_283_}))
        @Js
        def PyJs_htmlBuilder_285_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_285_}, var)
            var.registers(['group', 'options'])
            if var.get('group').get('semisimple'):
                return var.get('buildCommon').callprop('makeFragment', var.get('buildHTML_buildExpression')(var.get('group').get('body'), var.get('options'), Js(False)))
            return var.get('buildCommon').callprop('makeSpan', Js([Js('mord')]), var.get('buildHTML_buildExpression')(var.get('group').get('body'), var.get('options'), Js(True)), var.get('options'))
        PyJs_htmlBuilder_285_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_286_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_286_}, var)
            var.registers(['group', 'options'])
            return var.get('buildExpressionRow')(var.get('group').get('body'), var.get('options'))
        PyJs_mathmlBuilder_286_._set_name('mathmlBuilder')
        var.get('defineFunctionBuilders')(Js({'type':Js('ordgroup'),'htmlBuilder':PyJs_htmlBuilder_285_,'mathmlBuilder':PyJs_mathmlBuilder_286_}))
        @Js
        def PyJs_handler_287_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_287_}, var)
            var.registers(['body', 'parser', '_ref', 'args'])
            var.put('parser', var.get('_ref').get('parser'))
            var.put('body', var.get('args').get('0'))
            return Js({'type':Js('overline'),'mode':var.get('parser').get('mode'),'body':var.get('body')})
        PyJs_handler_287_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_288_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_288_}, var)
            var.registers(['group', 'options', 'line', 'innerGroup', 'vlist'])
            var.put('innerGroup', var.get('buildHTML_buildGroup')(var.get('group').get('body'), var.get('options').callprop('havingCrampedStyle')))
            var.put('line', var.get('buildCommon').callprop('makeLineSpan', Js('overline-line'), var.get('options')))
            var.put('vlist', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('firstBaseline'),'children':Js([Js({'type':Js('elem'),'elem':var.get('innerGroup')}), Js({'type':Js('kern'),'size':(Js(3.0)*var.get('line').get('height'))}), Js({'type':Js('elem'),'elem':var.get('line')}), Js({'type':Js('kern'),'size':var.get('line').get('height')})])}), var.get('options')))
            return var.get('buildCommon').callprop('makeSpan', Js([Js('mord'), Js('overline')]), Js([var.get('vlist')]), var.get('options'))
        PyJs_htmlBuilder_288_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_289_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_289_}, var)
            var.registers(['node', 'group', 'options', 'operator'])
            var.put('operator', var.get('mathMLTree').get('MathNode').create(Js('mo'), Js([var.get('mathMLTree').get('TextNode').create(Js('‾'))])))
            var.get('operator').callprop('setAttribute', Js('stretchy'), Js('true'))
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mover'), Js([var.get('buildMathML_buildGroup')(var.get('group').get('body'), var.get('options')), var.get('operator')])))
            var.get('node').callprop('setAttribute', Js('accent'), Js('true'))
            return var.get('node')
        PyJs_mathmlBuilder_289_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('overline'),'names':Js([Js('\\overline')]),'props':Js({'numArgs':Js(1.0)}),'handler':PyJs_handler_287_,'htmlBuilder':PyJs_htmlBuilder_288_,'mathmlBuilder':PyJs_mathmlBuilder_289_}))
        @Js
        def PyJs_handler_290_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_290_}, var)
            var.registers(['body', 'parser', '_ref', 'args'])
            var.put('parser', var.get('_ref').get('parser'))
            var.put('body', var.get('args').get('0'))
            return Js({'type':Js('phantom'),'mode':var.get('parser').get('mode'),'body':var.get('defineFunction_ordargument')(var.get('body'))})
        PyJs_handler_290_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_291_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_291_}, var)
            var.registers(['group', 'options', 'elements'])
            var.put('elements', var.get('buildHTML_buildExpression')(var.get('group').get('body'), var.get('options').callprop('withPhantom'), Js(False)))
            return var.get('buildCommon').callprop('makeFragment', var.get('elements'))
        PyJs_htmlBuilder_291_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_292_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_292_}, var)
            var.registers(['group', 'inner', 'options'])
            var.put('inner', var.get('buildMathML_buildExpression')(var.get('group').get('body'), var.get('options')))
            return var.get('mathMLTree').get('MathNode').create(Js('mphantom'), var.get('inner'))
        PyJs_mathmlBuilder_292_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('phantom'),'names':Js([Js('\\phantom')]),'props':Js({'numArgs':Js(1.0),'allowedInText':Js(True)}),'handler':PyJs_handler_290_,'htmlBuilder':PyJs_htmlBuilder_291_,'mathmlBuilder':PyJs_mathmlBuilder_292_}))
        @Js
        def PyJs_handler_293_(_ref2, args, this, arguments, var=var):
            var = Scope({'_ref2':_ref2, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_293_}, var)
            var.registers(['body', 'parser', 'args', '_ref2'])
            var.put('parser', var.get('_ref2').get('parser'))
            var.put('body', var.get('args').get('0'))
            return Js({'type':Js('hphantom'),'mode':var.get('parser').get('mode'),'body':var.get('body')})
        PyJs_handler_293_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_294_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_294_}, var)
            var.registers(['node', 'group', 'i', 'options'])
            var.put('node', var.get('buildCommon').callprop('makeSpan', Js([]), Js([var.get('buildHTML_buildGroup')(var.get('group').get('body'), var.get('options').callprop('withPhantom'))])))
            var.get('node').put('height', Js(0.0))
            var.get('node').put('depth', Js(0.0))
            if var.get('node').get('children'):
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('node').get('children').get('length')):
                    try:
                        var.get('node').get('children').get(var.get('i')).put('height', Js(0.0))
                        var.get('node').get('children').get(var.get('i')).put('depth', Js(0.0))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('node', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('firstBaseline'),'children':Js([Js({'type':Js('elem'),'elem':var.get('node')})])}), var.get('options')))
            return var.get('buildCommon').callprop('makeSpan', Js([Js('mord')]), Js([var.get('node')]), var.get('options'))
        PyJs_htmlBuilder_294_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_295_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_295_}, var)
            var.registers(['group', 'options', 'node', 'inner', 'phantom'])
            var.put('inner', var.get('buildMathML_buildExpression')(var.get('defineFunction_ordargument')(var.get('group').get('body')), var.get('options')))
            var.put('phantom', var.get('mathMLTree').get('MathNode').create(Js('mphantom'), var.get('inner')))
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mpadded'), Js([var.get('phantom')])))
            var.get('node').callprop('setAttribute', Js('height'), Js('0px'))
            var.get('node').callprop('setAttribute', Js('depth'), Js('0px'))
            return var.get('node')
        PyJs_mathmlBuilder_295_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('hphantom'),'names':Js([Js('\\hphantom')]),'props':Js({'numArgs':Js(1.0),'allowedInText':Js(True)}),'handler':PyJs_handler_293_,'htmlBuilder':PyJs_htmlBuilder_294_,'mathmlBuilder':PyJs_mathmlBuilder_295_}))
        @Js
        def PyJs_handler_296_(_ref3, args, this, arguments, var=var):
            var = Scope({'_ref3':_ref3, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_296_}, var)
            var.registers(['body', 'parser', '_ref3', 'args'])
            var.put('parser', var.get('_ref3').get('parser'))
            var.put('body', var.get('args').get('0'))
            return Js({'type':Js('vphantom'),'mode':var.get('parser').get('mode'),'body':var.get('body')})
        PyJs_handler_296_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_297_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_297_}, var)
            var.registers(['group', 'inner', 'fix', 'options'])
            var.put('inner', var.get('buildCommon').callprop('makeSpan', Js([Js('inner')]), Js([var.get('buildHTML_buildGroup')(var.get('group').get('body'), var.get('options').callprop('withPhantom'))])))
            var.put('fix', var.get('buildCommon').callprop('makeSpan', Js([Js('fix')]), Js([])))
            return var.get('buildCommon').callprop('makeSpan', Js([Js('mord'), Js('rlap')]), Js([var.get('inner'), var.get('fix')]), var.get('options'))
        PyJs_htmlBuilder_297_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_298_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_298_}, var)
            var.registers(['group', 'options', 'node', 'inner', 'phantom'])
            var.put('inner', var.get('buildMathML_buildExpression')(var.get('defineFunction_ordargument')(var.get('group').get('body')), var.get('options')))
            var.put('phantom', var.get('mathMLTree').get('MathNode').create(Js('mphantom'), var.get('inner')))
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mpadded'), Js([var.get('phantom')])))
            var.get('node').callprop('setAttribute', Js('width'), Js('0px'))
            return var.get('node')
        PyJs_mathmlBuilder_298_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('vphantom'),'names':Js([Js('\\vphantom')]),'props':Js({'numArgs':Js(1.0),'allowedInText':Js(True)}),'handler':PyJs_handler_296_,'htmlBuilder':PyJs_htmlBuilder_297_,'mathmlBuilder':PyJs_mathmlBuilder_298_}))
        pass
        var.put('sizeFuncs', Js([Js('\\tiny'), Js('\\sixptsize'), Js('\\scriptsize'), Js('\\footnotesize'), Js('\\small'), Js('\\normalsize'), Js('\\large'), Js('\\Large'), Js('\\LARGE'), Js('\\huge'), Js('\\Huge')]))
        @Js
        def PyJs_htmlBuilder_299_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_299_}, var)
            var.registers(['newOptions', 'group', 'options'])
            var.put('newOptions', var.get('options').callprop('havingSize', var.get('group').get('size')))
            return var.get('sizingGroup')(var.get('group').get('body'), var.get('newOptions'), var.get('options'))
        PyJs_htmlBuilder_299_._set_name('htmlBuilder')
        var.put('sizing_htmlBuilder', PyJs_htmlBuilder_299_)
        @Js
        def PyJs_handler_300_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_300_}, var)
            var.registers(['funcName', 'breakOnTokenText', 'body', '_ref', 'args', 'parser'])
            var.put('breakOnTokenText', var.get('_ref').get('breakOnTokenText'))
            var.put('funcName', var.get('_ref').get('funcName'))
            var.put('parser', var.get('_ref').get('parser'))
            var.put('body', var.get('parser').callprop('parseExpression', Js(False), var.get('breakOnTokenText')))
            return Js({'type':Js('sizing'),'mode':var.get('parser').get('mode'),'size':(var.get('sizeFuncs').callprop('indexOf', var.get('funcName'))+Js(1.0)),'body':var.get('body')})
        PyJs_handler_300_._set_name('handler')
        @Js
        def PyJs_mathmlBuilder_301_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_301_}, var)
            var.registers(['newOptions', 'group', 'options', 'node', 'inner'])
            var.put('newOptions', var.get('options').callprop('havingSize', var.get('group').get('size')))
            var.put('inner', var.get('buildMathML_buildExpression')(var.get('group').get('body'), var.get('newOptions')))
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mstyle'), var.get('inner')))
            var.get('node').callprop('setAttribute', Js('mathsize'), (var.get('newOptions').get('sizeMultiplier')+Js('em')))
            return var.get('node')
        PyJs_mathmlBuilder_301_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('sizing'),'names':var.get('sizeFuncs'),'props':Js({'numArgs':Js(0.0),'allowedInText':Js(True)}),'handler':PyJs_handler_300_,'htmlBuilder':var.get('sizing_htmlBuilder'),'mathmlBuilder':PyJs_mathmlBuilder_301_}))
        @Js
        def PyJs_handler_302_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_302_}, var)
            var.registers(['body', '_ref', 'args', 'parser', 'amount'])
            var.put('parser', var.get('_ref').get('parser'))
            var.put('amount', var.get('assertNodeType')(var.get('args').get('0'), Js('size')).get('value'))
            var.put('body', var.get('args').get('1'))
            return Js({'type':Js('raisebox'),'mode':var.get('parser').get('mode'),'dy':var.get('amount'),'body':var.get('body')})
        PyJs_handler_302_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_303_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_303_}, var)
            var.registers(['body', 'group', 'options', 'text', 'dy', 'sizedText'])
            var.put('text', Js({'type':Js('text'),'mode':var.get('group').get('mode'),'body':var.get('defineFunction_ordargument')(var.get('group').get('body')),'font':Js('mathrm')}))
            var.put('sizedText', Js({'type':Js('sizing'),'mode':var.get('group').get('mode'),'body':Js([var.get('text')]),'size':Js(6.0)}))
            var.put('body', var.get('sizing_htmlBuilder')(var.get('sizedText'), var.get('options')))
            var.put('dy', var.get('units_calculateSize')(var.get('group').get('dy'), var.get('options')))
            return var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('shift'),'positionData':(-var.get('dy')),'children':Js([Js({'type':Js('elem'),'elem':var.get('body')})])}), var.get('options'))
        PyJs_htmlBuilder_303_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_304_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_304_}, var)
            var.registers(['node', 'group', 'dy', 'options'])
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mpadded'), Js([var.get('buildMathML_buildGroup')(var.get('group').get('body'), var.get('options'))])))
            var.put('dy', (var.get('group').get('dy').get('number')+var.get('group').get('dy').get('unit')))
            var.get('node').callprop('setAttribute', Js('voffset'), var.get('dy'))
            return var.get('node')
        PyJs_mathmlBuilder_304_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('raisebox'),'names':Js([Js('\\raisebox')]),'props':Js({'numArgs':Js(2.0),'argTypes':Js([Js('size'), Js('text')]),'allowedInText':Js(True)}),'handler':PyJs_handler_302_,'htmlBuilder':PyJs_htmlBuilder_303_,'mathmlBuilder':PyJs_mathmlBuilder_304_}))
        @Js
        def PyJs_handler_305_(_ref, args, optArgs, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'optArgs':optArgs, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_305_}, var)
            var.registers(['shift', 'optArgs', '_ref', 'width', 'args', 'parser', 'height'])
            var.put('parser', var.get('_ref').get('parser'))
            var.put('shift', var.get('optArgs').get('0'))
            var.put('width', var.get('assertNodeType')(var.get('args').get('0'), Js('size')))
            var.put('height', var.get('assertNodeType')(var.get('args').get('1'), Js('size')))
            return Js({'type':Js('rule'),'mode':var.get('parser').get('mode'),'shift':(var.get('shift') and var.get('assertNodeType')(var.get('shift'), Js('size')).get('value')),'width':var.get('width').get('value'),'height':var.get('height').get('value')})
        PyJs_handler_305_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_306_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_306_}, var)
            var.registers(['group', 'options', 'shift', 'rule', 'width', 'height'])
            var.put('rule', var.get('buildCommon').callprop('makeSpan', Js([Js('mord'), Js('rule')]), Js([]), var.get('options')))
            var.put('width', var.get('units_calculateSize')(var.get('group').get('width'), var.get('options')))
            var.put('height', var.get('units_calculateSize')(var.get('group').get('height'), var.get('options')))
            var.put('shift', (var.get('units_calculateSize')(var.get('group').get('shift'), var.get('options')) if var.get('group').get('shift') else Js(0.0)))
            var.get('rule').get('style').put('borderRightWidth', (var.get('width')+Js('em')))
            var.get('rule').get('style').put('borderTopWidth', (var.get('height')+Js('em')))
            var.get('rule').get('style').put('bottom', (var.get('shift')+Js('em')))
            var.get('rule').put('width', var.get('width'))
            var.get('rule').put('height', (var.get('height')+var.get('shift')))
            var.get('rule').put('depth', (-var.get('shift')))
            var.get('rule').put('maxFontSize', ((var.get('height')*Js(1.125))*var.get('options').get('sizeMultiplier')))
            return var.get('rule')
        PyJs_htmlBuilder_306_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_307_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_307_}, var)
            var.registers(['color', 'group', 'options', 'rule', 'shift', 'width', 'height', 'wrapper'])
            var.put('width', var.get('units_calculateSize')(var.get('group').get('width'), var.get('options')))
            var.put('height', var.get('units_calculateSize')(var.get('group').get('height'), var.get('options')))
            var.put('shift', (var.get('units_calculateSize')(var.get('group').get('shift'), var.get('options')) if var.get('group').get('shift') else Js(0.0)))
            var.put('color', ((var.get('options').get('color') and var.get('options').callprop('getColor')) or Js('black')))
            var.put('rule', var.get('mathMLTree').get('MathNode').create(Js('mspace')))
            var.get('rule').callprop('setAttribute', Js('mathbackground'), var.get('color'))
            var.get('rule').callprop('setAttribute', Js('width'), (var.get('width')+Js('em')))
            var.get('rule').callprop('setAttribute', Js('height'), (var.get('height')+Js('em')))
            var.put('wrapper', var.get('mathMLTree').get('MathNode').create(Js('mpadded'), Js([var.get('rule')])))
            if (var.get('shift')>=Js(0.0)):
                var.get('wrapper').callprop('setAttribute', Js('height'), ((Js('+')+var.get('shift'))+Js('em')))
            else:
                var.get('wrapper').callprop('setAttribute', Js('height'), (var.get('shift')+Js('em')))
                var.get('wrapper').callprop('setAttribute', Js('depth'), ((Js('+')+(-var.get('shift')))+Js('em')))
            var.get('wrapper').callprop('setAttribute', Js('voffset'), (var.get('shift')+Js('em')))
            return var.get('wrapper')
        PyJs_mathmlBuilder_307_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('rule'),'names':Js([Js('\\rule')]),'props':Js({'numArgs':Js(2.0),'numOptionalArgs':Js(1.0),'argTypes':Js([Js('size'), Js('size'), Js('size')])}),'handler':PyJs_handler_305_,'htmlBuilder':PyJs_htmlBuilder_306_,'mathmlBuilder':PyJs_mathmlBuilder_307_}))
        @Js
        def PyJs_handler_308_(_ref, args, optArgs, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'optArgs':optArgs, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_308_}, var)
            var.registers(['smashHeight', 'i', 'body', 'tbArg', 'node', 'smashDepth', 'letter', 'optArgs', '_ref', 'args', 'parser'])
            var.put('parser', var.get('_ref').get('parser'))
            var.put('smashHeight', Js(False))
            var.put('smashDepth', Js(False))
            var.put('tbArg', (var.get('optArgs').get('0') and var.get('assertNodeType')(var.get('optArgs').get('0'), Js('ordgroup'))))
            if var.get('tbArg'):
                var.put('letter', Js(''))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('tbArg').get('body').get('length')):
                    try:
                        var.put('node', var.get('tbArg').get('body').get(var.get('i')))
                        var.put('letter', var.get('node').get('text'))
                        if PyJsStrictEq(var.get('letter'),Js('t')):
                            var.put('smashHeight', Js(True))
                        else:
                            if PyJsStrictEq(var.get('letter'),Js('b')):
                                var.put('smashDepth', Js(True))
                            else:
                                var.put('smashHeight', Js(False))
                                var.put('smashDepth', Js(False))
                                break
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
            else:
                var.put('smashHeight', Js(True))
                var.put('smashDepth', Js(True))
            var.put('body', var.get('args').get('0'))
            return Js({'type':Js('smash'),'mode':var.get('parser').get('mode'),'body':var.get('body'),'smashHeight':var.get('smashHeight'),'smashDepth':var.get('smashDepth')})
        PyJs_handler_308_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_309_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_309_}, var)
            var.registers(['i', 'group', '_i', 'smashedNode', 'options', 'node'])
            var.put('node', var.get('buildCommon').callprop('makeSpan', Js([]), Js([var.get('buildHTML_buildGroup')(var.get('group').get('body'), var.get('options'))])))
            if (var.get('group').get('smashHeight').neg() and var.get('group').get('smashDepth').neg()):
                return var.get('node')
            if var.get('group').get('smashHeight'):
                var.get('node').put('height', Js(0.0))
                if var.get('node').get('children'):
                    #for JS loop
                    var.put('i', Js(0.0))
                    while (var.get('i')<var.get('node').get('children').get('length')):
                        try:
                            var.get('node').get('children').get(var.get('i')).put('height', Js(0.0))
                        finally:
                                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            if var.get('group').get('smashDepth'):
                var.get('node').put('depth', Js(0.0))
                if var.get('node').get('children'):
                    #for JS loop
                    var.put('_i', Js(0.0))
                    while (var.get('_i')<var.get('node').get('children').get('length')):
                        try:
                            var.get('node').get('children').get(var.get('_i')).put('depth', Js(0.0))
                        finally:
                                (var.put('_i',Js(var.get('_i').to_number())+Js(1))-Js(1))
            var.put('smashedNode', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('firstBaseline'),'children':Js([Js({'type':Js('elem'),'elem':var.get('node')})])}), var.get('options')))
            return var.get('buildCommon').callprop('makeSpan', Js([Js('mord')]), Js([var.get('smashedNode')]), var.get('options'))
        PyJs_htmlBuilder_309_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_310_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_310_}, var)
            var.registers(['node', 'group', 'options'])
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mpadded'), Js([var.get('buildMathML_buildGroup')(var.get('group').get('body'), var.get('options'))])))
            if var.get('group').get('smashHeight'):
                var.get('node').callprop('setAttribute', Js('height'), Js('0px'))
            if var.get('group').get('smashDepth'):
                var.get('node').callprop('setAttribute', Js('depth'), Js('0px'))
            return var.get('node')
        PyJs_mathmlBuilder_310_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('smash'),'names':Js([Js('\\smash')]),'props':Js({'numArgs':Js(1.0),'numOptionalArgs':Js(1.0),'allowedInText':Js(True)}),'handler':PyJs_handler_308_,'htmlBuilder':PyJs_htmlBuilder_309_,'mathmlBuilder':PyJs_mathmlBuilder_310_}))
        @Js
        def PyJs_handler_311_(_ref, args, optArgs, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'optArgs':optArgs, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_311_}, var)
            var.registers(['index', 'body', 'optArgs', '_ref', 'args', 'parser'])
            var.put('parser', var.get('_ref').get('parser'))
            var.put('index', var.get('optArgs').get('0'))
            var.put('body', var.get('args').get('0'))
            return Js({'type':Js('sqrt'),'mode':var.get('parser').get('mode'),'body':var.get('body'),'index':var.get('index')})
        PyJs_handler_311_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_312_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_312_}, var)
            var.registers(['delimDepth', 'ruleWidth', 'rootVListWrap', 'img', 'body', 'minDelimiterHeight', 'phi', 'newOptions', 'lineClearance', 'theta', 'rootVList', 'group', 'toShift', 'advanceWidth', 'options', '_delimiter$sqrtImage', 'imgShift', 'inner', 'rootm', 'metrics'])
            var.put('inner', var.get('buildHTML_buildGroup')(var.get('group').get('body'), var.get('options').callprop('havingCrampedStyle')))
            if PyJsStrictEq(var.get('inner').get('height'),Js(0.0)):
                var.get('inner').put('height', var.get('options').callprop('fontMetrics').get('xHeight'))
            var.put('inner', var.get('buildCommon').callprop('wrapFragment', var.get('inner'), var.get('options')))
            var.put('metrics', var.get('options').callprop('fontMetrics'))
            var.put('theta', var.get('metrics').get('defaultRuleThickness'))
            var.put('phi', var.get('theta'))
            if (var.get('options').get('style').get('id')<var.get('src_Style').get('TEXT').get('id')):
                var.put('phi', var.get('options').callprop('fontMetrics').get('xHeight'))
            var.put('lineClearance', (var.get('theta')+(var.get('phi')/Js(4.0))))
            var.put('minDelimiterHeight', (((var.get('inner').get('height')+var.get('inner').get('depth'))+var.get('lineClearance'))+var.get('theta')))
            var.put('_delimiter$sqrtImage', var.get('delimiter').callprop('sqrtImage', var.get('minDelimiterHeight'), var.get('options')))
            var.put('img', var.get('_delimiter$sqrtImage').get('span'))
            var.put('ruleWidth', var.get('_delimiter$sqrtImage').get('ruleWidth'))
            var.put('advanceWidth', var.get('_delimiter$sqrtImage').get('advanceWidth'))
            var.put('delimDepth', (var.get('img').get('height')-var.get('ruleWidth')))
            if (var.get('delimDepth')>((var.get('inner').get('height')+var.get('inner').get('depth'))+var.get('lineClearance'))):
                var.put('lineClearance', ((((var.get('lineClearance')+var.get('delimDepth'))-var.get('inner').get('height'))-var.get('inner').get('depth'))/Js(2.0)))
            var.put('imgShift', (((var.get('img').get('height')-var.get('inner').get('height'))-var.get('lineClearance'))-var.get('ruleWidth')))
            var.get('inner').get('style').put('paddingLeft', (var.get('advanceWidth')+Js('em')))
            var.put('body', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('firstBaseline'),'children':Js([Js({'type':Js('elem'),'elem':var.get('inner'),'wrapperClasses':Js([Js('svg-align')])}), Js({'type':Js('kern'),'size':(-(var.get('inner').get('height')+var.get('imgShift')))}), Js({'type':Js('elem'),'elem':var.get('img')}), Js({'type':Js('kern'),'size':var.get('ruleWidth')})])}), var.get('options')))
            if var.get('group').get('index').neg():
                return var.get('buildCommon').callprop('makeSpan', Js([Js('mord'), Js('sqrt')]), Js([var.get('body')]), var.get('options'))
            else:
                var.put('newOptions', var.get('options').callprop('havingStyle', var.get('src_Style').get('SCRIPTSCRIPT')))
                var.put('rootm', var.get('buildHTML_buildGroup')(var.get('group').get('index'), var.get('newOptions'), var.get('options')))
                var.put('toShift', (Js(0.6)*(var.get('body').get('height')-var.get('body').get('depth'))))
                var.put('rootVList', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('shift'),'positionData':(-var.get('toShift')),'children':Js([Js({'type':Js('elem'),'elem':var.get('rootm')})])}), var.get('options')))
                var.put('rootVListWrap', var.get('buildCommon').callprop('makeSpan', Js([Js('root')]), Js([var.get('rootVList')])))
                return var.get('buildCommon').callprop('makeSpan', Js([Js('mord'), Js('sqrt')]), Js([var.get('rootVListWrap'), var.get('body')]), var.get('options'))
        PyJs_htmlBuilder_312_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_313_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_313_}, var)
            var.registers(['body', 'index', 'group', 'options'])
            var.put('body', var.get('group').get('body'))
            var.put('index', var.get('group').get('index'))
            return (var.get('mathMLTree').get('MathNode').create(Js('mroot'), Js([var.get('buildMathML_buildGroup')(var.get('body'), var.get('options')), var.get('buildMathML_buildGroup')(var.get('index'), var.get('options'))])) if var.get('index') else var.get('mathMLTree').get('MathNode').create(Js('msqrt'), Js([var.get('buildMathML_buildGroup')(var.get('body'), var.get('options'))])))
        PyJs_mathmlBuilder_313_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('sqrt'),'names':Js([Js('\\sqrt')]),'props':Js({'numArgs':Js(1.0),'numOptionalArgs':Js(1.0)}),'handler':PyJs_handler_311_,'htmlBuilder':PyJs_htmlBuilder_312_,'mathmlBuilder':PyJs_mathmlBuilder_313_}))
        var.put('styling_styleMap', Js({'display':var.get('src_Style').get('DISPLAY'),'text':var.get('src_Style').get('TEXT'),'script':var.get('src_Style').get('SCRIPT'),'scriptscript':var.get('src_Style').get('SCRIPTSCRIPT')}))
        @Js
        def PyJs_handler_314_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_314_}, var)
            var.registers(['funcName', 'breakOnTokenText', 'body', 'style', '_ref', 'args', 'parser'])
            var.put('breakOnTokenText', var.get('_ref').get('breakOnTokenText'))
            var.put('funcName', var.get('_ref').get('funcName'))
            var.put('parser', var.get('_ref').get('parser'))
            var.put('body', var.get('parser').callprop('parseExpression', Js(True), var.get('breakOnTokenText')))
            var.put('style', var.get('funcName').callprop('slice', Js(1.0), (var.get('funcName').get('length')-Js(5.0))))
            return Js({'type':Js('styling'),'mode':var.get('parser').get('mode'),'style':var.get('style'),'body':var.get('body')})
        PyJs_handler_314_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_315_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_315_}, var)
            var.registers(['newOptions', 'group', 'newStyle', 'options'])
            var.put('newStyle', var.get('styling_styleMap').get(var.get('group').get('style')))
            var.put('newOptions', var.get('options').callprop('havingStyle', var.get('newStyle')).callprop('withFont', Js('')))
            return var.get('sizingGroup')(var.get('group').get('body'), var.get('newOptions'), var.get('options'))
        PyJs_htmlBuilder_315_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_316_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_316_}, var)
            var.registers(['newStyle', 'styleAttributes', 'newOptions', 'group', 'options', 'node', 'inner', 'styleMap', 'attr'])
            var.put('styleMap', Js({'display':var.get('src_Style').get('DISPLAY'),'text':var.get('src_Style').get('TEXT'),'script':var.get('src_Style').get('SCRIPT'),'scriptscript':var.get('src_Style').get('SCRIPTSCRIPT')}))
            var.put('newStyle', var.get('styleMap').get(var.get('group').get('style')))
            var.put('newOptions', var.get('options').callprop('havingStyle', var.get('newStyle')))
            var.put('inner', var.get('buildMathML_buildExpression')(var.get('group').get('body'), var.get('newOptions')))
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mstyle'), var.get('inner')))
            var.put('styleAttributes', Js({'display':Js([Js('0'), Js('true')]),'text':Js([Js('0'), Js('false')]),'script':Js([Js('1'), Js('false')]),'scriptscript':Js([Js('2'), Js('false')])}))
            var.put('attr', var.get('styleAttributes').get(var.get('group').get('style')))
            var.get('node').callprop('setAttribute', Js('scriptlevel'), var.get('attr').get('0'))
            var.get('node').callprop('setAttribute', Js('displaystyle'), var.get('attr').get('1'))
            return var.get('node')
        PyJs_mathmlBuilder_316_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('styling'),'names':Js([Js('\\displaystyle'), Js('\\textstyle'), Js('\\scriptstyle'), Js('\\scriptscriptstyle')]),'props':Js({'numArgs':Js(0.0),'allowedInText':Js(True)}),'handler':PyJs_handler_314_,'htmlBuilder':PyJs_htmlBuilder_315_,'mathmlBuilder':PyJs_mathmlBuilder_316_}))
        @Js
        def PyJs_htmlBuilderDelegate_317_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilderDelegate':PyJs_htmlBuilderDelegate_317_}, var)
            var.registers(['delegate', 'group', 'options', 'base', 'isSup'])
            var.put('base', var.get('group').get('base'))
            if var.get('base').neg():
                return var.get(u"null")
            else:
                if PyJsStrictEq(var.get('base').get('type'),Js('op')):
                    var.put('delegate', (var.get('base').get('limits') and (PyJsStrictEq(var.get('options').get('style').get('size'),var.get('src_Style').get('DISPLAY').get('size')) or var.get('base').get('alwaysHandleSupSub'))))
                    return (var.get('op_htmlBuilder') if var.get('delegate') else var.get(u"null"))
                else:
                    if PyJsStrictEq(var.get('base').get('type'),Js('accent')):
                        return (var.get('accent_htmlBuilder') if var.get('utils').callprop('isCharacterBox', var.get('base').get('base')) else var.get(u"null"))
                    else:
                        if PyJsStrictEq(var.get('base').get('type'),Js('horizBrace')):
                            var.put('isSup', var.get('group').get('sub').neg())
                            return (var.get('horizBrace_htmlBuilder') if PyJsStrictEq(var.get('isSup'),var.get('base').get('isOver')) else var.get(u"null"))
                        else:
                            return var.get(u"null")
        PyJs_htmlBuilderDelegate_317_._set_name('htmlBuilderDelegate')
        var.put('supsub_htmlBuilderDelegate', PyJs_htmlBuilderDelegate_317_)
        @Js
        def PyJs_htmlBuilder_318_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_318_}, var)
            var.registers(['_vlistElem', 'minSupShift', 'mclass', 'psi', 'supm', 'newOptions', 'options', 'valueSub', 'builderDelegate', 'base', 'vlistElem', 'multiplier', 'valueBase', 'maxWidth', 'subm', 'marginLeft', 'supShift', 'subShift', 'supsub', '_newOptions', 'ruleWidth', 'isCharacterBox', 'marginRight', 'group', 'isOiint', 'valueSup', 'metrics'])
            var.put('builderDelegate', var.get('supsub_htmlBuilderDelegate')(var.get('group'), var.get('options')))
            if var.get('builderDelegate'):
                return var.get('builderDelegate')(var.get('group'), var.get('options'))
            var.put('valueBase', var.get('group').get('base'))
            var.put('valueSup', var.get('group').get('sup'))
            var.put('valueSub', var.get('group').get('sub'))
            var.put('base', var.get('buildHTML_buildGroup')(var.get('valueBase'), var.get('options')))
            pass
            pass
            var.put('metrics', var.get('options').callprop('fontMetrics'))
            var.put('supShift', Js(0.0))
            var.put('subShift', Js(0.0))
            var.put('isCharacterBox', (var.get('valueBase') and var.get('utils').callprop('isCharacterBox', var.get('valueBase'))))
            if var.get('valueSup'):
                var.put('newOptions', var.get('options').callprop('havingStyle', var.get('options').get('style').callprop('sup')))
                var.put('supm', var.get('buildHTML_buildGroup')(var.get('valueSup'), var.get('newOptions'), var.get('options')))
                if var.get('isCharacterBox').neg():
                    var.put('supShift', (var.get('base').get('height')-((var.get('newOptions').callprop('fontMetrics').get('supDrop')*var.get('newOptions').get('sizeMultiplier'))/var.get('options').get('sizeMultiplier'))))
            if var.get('valueSub'):
                var.put('_newOptions', var.get('options').callprop('havingStyle', var.get('options').get('style').callprop('sub')))
                var.put('subm', var.get('buildHTML_buildGroup')(var.get('valueSub'), var.get('_newOptions'), var.get('options')))
                if var.get('isCharacterBox').neg():
                    var.put('subShift', (var.get('base').get('depth')+((var.get('_newOptions').callprop('fontMetrics').get('subDrop')*var.get('_newOptions').get('sizeMultiplier'))/var.get('options').get('sizeMultiplier'))))
            pass
            if PyJsStrictEq(var.get('options').get('style'),var.get('src_Style').get('DISPLAY')):
                var.put('minSupShift', var.get('metrics').get('sup1'))
            else:
                if var.get('options').get('style').get('cramped'):
                    var.put('minSupShift', var.get('metrics').get('sup3'))
                else:
                    var.put('minSupShift', var.get('metrics').get('sup2'))
            var.put('multiplier', var.get('options').get('sizeMultiplier'))
            var.put('marginRight', (((Js(0.5)/var.get('metrics').get('ptPerEm'))/var.get('multiplier'))+Js('em')))
            var.put('marginLeft', var.get(u"null"))
            if var.get('subm'):
                var.put('isOiint', (((var.get('group').get('base') and PyJsStrictEq(var.get('group').get('base').get('type'),Js('op'))) and var.get('group').get('base').get('name')) and (PyJsStrictEq(var.get('group').get('base').get('name'),Js('\\oiint')) or PyJsStrictEq(var.get('group').get('base').get('name'),Js('\\oiiint')))))
                if (var.get('base').instanceof(var.get('domTree_SymbolNode')) or var.get('isOiint')):
                    var.put('marginLeft', ((-var.get('base').get('italic'))+Js('em')))
            pass
            if (var.get('supm') and var.get('subm')):
                var.put('supShift', var.get('Math').callprop('max', var.get('supShift'), var.get('minSupShift'), (var.get('supm').get('depth')+(Js(0.25)*var.get('metrics').get('xHeight')))))
                var.put('subShift', var.get('Math').callprop('max', var.get('subShift'), var.get('metrics').get('sub2')))
                var.put('ruleWidth', var.get('metrics').get('defaultRuleThickness'))
                var.put('maxWidth', (Js(4.0)*var.get('ruleWidth')))
                if (((var.get('supShift')-var.get('supm').get('depth'))-(var.get('subm').get('height')-var.get('subShift')))<var.get('maxWidth')):
                    var.put('subShift', ((var.get('maxWidth')-(var.get('supShift')-var.get('supm').get('depth')))+var.get('subm').get('height')))
                    var.put('psi', ((Js(0.8)*var.get('metrics').get('xHeight'))-(var.get('supShift')-var.get('supm').get('depth'))))
                    if (var.get('psi')>Js(0.0)):
                        var.put('supShift', var.get('psi'), '+')
                        var.put('subShift', var.get('psi'), '-')
                var.put('vlistElem', Js([Js({'type':Js('elem'),'elem':var.get('subm'),'shift':var.get('subShift'),'marginRight':var.get('marginRight'),'marginLeft':var.get('marginLeft')}), Js({'type':Js('elem'),'elem':var.get('supm'),'shift':(-var.get('supShift')),'marginRight':var.get('marginRight')})]))
                var.put('supsub', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('individualShift'),'children':var.get('vlistElem')}), var.get('options')))
            else:
                if var.get('subm'):
                    var.put('subShift', var.get('Math').callprop('max', var.get('subShift'), var.get('metrics').get('sub1'), (var.get('subm').get('height')-(Js(0.8)*var.get('metrics').get('xHeight')))))
                    var.put('_vlistElem', Js([Js({'type':Js('elem'),'elem':var.get('subm'),'marginLeft':var.get('marginLeft'),'marginRight':var.get('marginRight')})]))
                    var.put('supsub', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('shift'),'positionData':var.get('subShift'),'children':var.get('_vlistElem')}), var.get('options')))
                else:
                    if var.get('supm'):
                        var.put('supShift', var.get('Math').callprop('max', var.get('supShift'), var.get('minSupShift'), (var.get('supm').get('depth')+(Js(0.25)*var.get('metrics').get('xHeight')))))
                        var.put('supsub', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('shift'),'positionData':(-var.get('supShift')),'children':Js([Js({'type':Js('elem'),'elem':var.get('supm'),'marginRight':var.get('marginRight')})])}), var.get('options')))
                    else:
                        PyJsTempException = JsToPyException(var.get('Error').create(Js('supsub must have either sup or sub.')))
                        raise PyJsTempException
            var.put('mclass', (var.get('getTypeOfDomTree')(var.get('base'), Js('right')) or Js('mord')))
            return var.get('buildCommon').callprop('makeSpan', Js([var.get('mclass')]), Js([var.get('base'), var.get('buildCommon').callprop('makeSpan', Js([Js('msupsub')]), Js([var.get('supsub')]))]), var.get('options'))
        PyJs_htmlBuilder_318_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_319_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_319_}, var)
            var.registers(['children', 'isBrace', 'nodeType', '_base2', 'group', 'options', '_base', 'node', 'horizBrace', 'isOver', 'base', 'isSup'])
            var.put('isBrace', Js(False))
            pass
            pass
            var.put('horizBrace', var.get('checkNodeType')(var.get('group').get('base'), Js('horizBrace')))
            if var.get('horizBrace'):
                var.put('isSup', var.get('group').get('sup').neg().neg())
                if PyJsStrictEq(var.get('isSup'),var.get('horizBrace').get('isOver')):
                    var.put('isBrace', Js(True))
                    var.put('isOver', var.get('horizBrace').get('isOver'))
            if (var.get('group').get('base') and PyJsStrictEq(var.get('group').get('base').get('type'),Js('op'))):
                var.get('group').get('base').put('parentIsSupSub', Js(True))
            var.put('children', Js([var.get('buildMathML_buildGroup')(var.get('group').get('base'), var.get('options'))]))
            if var.get('group').get('sub'):
                var.get('children').callprop('push', var.get('buildMathML_buildGroup')(var.get('group').get('sub'), var.get('options')))
            if var.get('group').get('sup'):
                var.get('children').callprop('push', var.get('buildMathML_buildGroup')(var.get('group').get('sup'), var.get('options')))
            pass
            if var.get('isBrace'):
                var.put('nodeType', (Js('mover') if var.get('isOver') else Js('munder')))
            else:
                if var.get('group').get('sub').neg():
                    var.put('base', var.get('group').get('base'))
                    if (((var.get('base') and PyJsStrictEq(var.get('base').get('type'),Js('op'))) and var.get('base').get('limits')) and (PyJsStrictEq(var.get('options').get('style'),var.get('src_Style').get('DISPLAY')) or var.get('base').get('alwaysHandleSupSub'))):
                        var.put('nodeType', Js('mover'))
                    else:
                        var.put('nodeType', Js('msup'))
                else:
                    if var.get('group').get('sup').neg():
                        var.put('_base', var.get('group').get('base'))
                        if (((var.get('_base') and PyJsStrictEq(var.get('_base').get('type'),Js('op'))) and var.get('_base').get('limits')) and (PyJsStrictEq(var.get('options').get('style'),var.get('src_Style').get('DISPLAY')) or var.get('_base').get('alwaysHandleSupSub'))):
                            var.put('nodeType', Js('munder'))
                        else:
                            var.put('nodeType', Js('msub'))
                    else:
                        var.put('_base2', var.get('group').get('base'))
                        if (((var.get('_base2') and PyJsStrictEq(var.get('_base2').get('type'),Js('op'))) and var.get('_base2').get('limits')) and PyJsStrictEq(var.get('options').get('style'),var.get('src_Style').get('DISPLAY'))):
                            var.put('nodeType', Js('munderover'))
                        else:
                            var.put('nodeType', Js('msubsup'))
            var.put('node', var.get('mathMLTree').get('MathNode').create(var.get('nodeType'), var.get('children')))
            return var.get('node')
        PyJs_mathmlBuilder_319_._set_name('mathmlBuilder')
        var.get('defineFunctionBuilders')(Js({'type':Js('supsub'),'htmlBuilder':PyJs_htmlBuilder_318_,'mathmlBuilder':PyJs_mathmlBuilder_319_}))
        @Js
        def PyJs_htmlBuilder_320_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_320_}, var)
            var.registers(['group', 'options'])
            return var.get('buildCommon').callprop('mathsym', var.get('group').get('text'), var.get('group').get('mode'), var.get('options'), Js([(Js('m')+var.get('group').get('family'))]))
        PyJs_htmlBuilder_320_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_321_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_321_}, var)
            var.registers(['node', 'group', 'variant', 'options'])
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mo'), Js([var.get('buildMathML_makeText')(var.get('group').get('text'), var.get('group').get('mode'))])))
            if PyJsStrictEq(var.get('group').get('family'),Js('bin')):
                var.put('variant', var.get('buildMathML_getVariant')(var.get('group'), var.get('options')))
                if PyJsStrictEq(var.get('variant'),Js('bold-italic')):
                    var.get('node').callprop('setAttribute', Js('mathvariant'), var.get('variant'))
            else:
                if PyJsStrictEq(var.get('group').get('family'),Js('punct')):
                    var.get('node').callprop('setAttribute', Js('separator'), Js('true'))
                else:
                    if (PyJsStrictEq(var.get('group').get('family'),Js('open')) or PyJsStrictEq(var.get('group').get('family'),Js('close'))):
                        var.get('node').callprop('setAttribute', Js('stretchy'), Js('false'))
            return var.get('node')
        PyJs_mathmlBuilder_321_._set_name('mathmlBuilder')
        var.get('defineFunctionBuilders')(Js({'type':Js('atom'),'htmlBuilder':PyJs_htmlBuilder_320_,'mathmlBuilder':PyJs_mathmlBuilder_321_}))
        var.put('defaultVariant', Js({'mi':Js('italic'),'mn':Js('normal'),'mtext':Js('normal')}))
        @Js
        def PyJs_htmlBuilder_322_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_322_}, var)
            var.registers(['group', 'options'])
            return var.get('buildCommon').callprop('makeOrd', var.get('group'), var.get('options'), Js('mathord'))
        PyJs_htmlBuilder_322_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_323_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_323_}, var)
            var.registers(['node', 'group', 'variant', 'options'])
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mi'), Js([var.get('buildMathML_makeText')(var.get('group').get('text'), var.get('group').get('mode'), var.get('options'))])))
            var.put('variant', (var.get('buildMathML_getVariant')(var.get('group'), var.get('options')) or Js('italic')))
            if PyJsStrictNeq(var.get('variant'),var.get('defaultVariant').get(var.get('node').get('type'))):
                var.get('node').callprop('setAttribute', Js('mathvariant'), var.get('variant'))
            return var.get('node')
        PyJs_mathmlBuilder_323_._set_name('mathmlBuilder')
        var.get('defineFunctionBuilders')(Js({'type':Js('mathord'),'htmlBuilder':PyJs_htmlBuilder_322_,'mathmlBuilder':PyJs_mathmlBuilder_323_}))
        @Js
        def PyJs_htmlBuilder_324_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_324_}, var)
            var.registers(['group', 'options'])
            return var.get('buildCommon').callprop('makeOrd', var.get('group'), var.get('options'), Js('textord'))
        PyJs_htmlBuilder_324_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_325_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_325_}, var)
            var.registers(['variant', 'group', 'options', 'text', 'node'])
            var.put('text', var.get('buildMathML_makeText')(var.get('group').get('text'), var.get('group').get('mode'), var.get('options')))
            var.put('variant', (var.get('buildMathML_getVariant')(var.get('group'), var.get('options')) or Js('normal')))
            pass
            if PyJsStrictEq(var.get('group').get('mode'),Js('text')):
                var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mtext'), Js([var.get('text')])))
            else:
                if JsRegExp('/[0-9]/').callprop('test', var.get('group').get('text')):
                    var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mn'), Js([var.get('text')])))
                else:
                    if PyJsStrictEq(var.get('group').get('text'),Js('\\prime')):
                        var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mo'), Js([var.get('text')])))
                    else:
                        var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mi'), Js([var.get('text')])))
            if PyJsStrictNeq(var.get('variant'),var.get('defaultVariant').get(var.get('node').get('type'))):
                var.get('node').callprop('setAttribute', Js('mathvariant'), var.get('variant'))
            return var.get('node')
        PyJs_mathmlBuilder_325_._set_name('mathmlBuilder')
        var.get('defineFunctionBuilders')(Js({'type':Js('textord'),'htmlBuilder':PyJs_htmlBuilder_324_,'mathmlBuilder':PyJs_mathmlBuilder_325_}))
        var.put('cssSpace', Js({'\\nobreak':Js('nobreak'),'\\allowbreak':Js('allowbreak')}))
        var.put('regularSpace', Js({' ':Js({}),'\\ ':Js({}),'~':Js({'className':Js('nobreak')}),'\\space':Js({}),'\\nobreakspace':Js({'className':Js('nobreak')})}))
        @Js
        def PyJs_htmlBuilder_326_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_326_}, var)
            var.registers(['ord', 'group', 'options', 'className'])
            if var.get('regularSpace').callprop('hasOwnProperty', var.get('group').get('text')):
                var.put('className', (var.get('regularSpace').get(var.get('group').get('text')).get('className') or Js('')))
                if PyJsStrictEq(var.get('group').get('mode'),Js('text')):
                    var.put('ord', var.get('buildCommon').callprop('makeOrd', var.get('group'), var.get('options'), Js('textord')))
                    var.get('ord').get('classes').callprop('push', var.get('className'))
                    return var.get('ord')
                else:
                    return var.get('buildCommon').callprop('makeSpan', Js([Js('mspace'), var.get('className')]), Js([var.get('buildCommon').callprop('mathsym', var.get('group').get('text'), var.get('group').get('mode'), var.get('options'))]), var.get('options'))
            else:
                if var.get('cssSpace').callprop('hasOwnProperty', var.get('group').get('text')):
                    return var.get('buildCommon').callprop('makeSpan', Js([Js('mspace'), var.get('cssSpace').get(var.get('group').get('text'))]), Js([]), var.get('options'))
                else:
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js('Unknown type of space "')+var.get('group').get('text'))+Js('"'))))
                    raise PyJsTempException
        PyJs_htmlBuilder_326_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_327_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_327_}, var)
            var.registers(['node', 'group', 'options'])
            pass
            if var.get('regularSpace').callprop('hasOwnProperty', var.get('group').get('text')):
                var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mtext'), Js([var.get('mathMLTree').get('TextNode').create(Js('\xa0'))])))
            else:
                if var.get('cssSpace').callprop('hasOwnProperty', var.get('group').get('text')):
                    return var.get('mathMLTree').get('MathNode').create(Js('mspace'))
                else:
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js('Unknown type of space "')+var.get('group').get('text'))+Js('"'))))
                    raise PyJsTempException
            return var.get('node')
        PyJs_mathmlBuilder_327_._set_name('mathmlBuilder')
        var.get('defineFunctionBuilders')(Js({'type':Js('spacing'),'htmlBuilder':PyJs_htmlBuilder_326_,'mathmlBuilder':PyJs_mathmlBuilder_327_}))
        @Js
        def PyJs_pad_328_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments, 'pad':PyJs_pad_328_}, var)
            var.registers(['padNode'])
            var.put('padNode', var.get('mathMLTree').get('MathNode').create(Js('mtd'), Js([])))
            var.get('padNode').callprop('setAttribute', Js('width'), Js('50%'))
            return var.get('padNode')
        PyJs_pad_328_._set_name('pad')
        var.put('tag_pad', PyJs_pad_328_)
        @Js
        def PyJs_mathmlBuilder_329_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_329_}, var)
            var.registers(['group', 'options', 'table'])
            def PyJs_LONG_330_(var=var):
                return var.get('mathMLTree').get('MathNode').create(Js('mtable'), Js([var.get('mathMLTree').get('MathNode').create(Js('mtr'), Js([var.get('tag_pad')(), var.get('mathMLTree').get('MathNode').create(Js('mtd'), Js([var.get('buildExpressionRow')(var.get('group').get('body'), var.get('options'))])), var.get('tag_pad')(), var.get('mathMLTree').get('MathNode').create(Js('mtd'), Js([var.get('buildExpressionRow')(var.get('group').get('tag'), var.get('options'))]))]))]))
            var.put('table', PyJs_LONG_330_())
            var.get('table').callprop('setAttribute', Js('width'), Js('100%'))
            return var.get('table')
        PyJs_mathmlBuilder_329_._set_name('mathmlBuilder')
        var.get('defineFunctionBuilders')(Js({'type':Js('tag'),'mathmlBuilder':PyJs_mathmlBuilder_329_}))
        var.put('textFontFamilies', Js({'\\text':var.get('undefined'),'\\textrm':Js('textrm'),'\\textsf':Js('textsf'),'\\texttt':Js('texttt'),'\\textnormal':Js('textrm')}))
        var.put('textFontWeights', Js({'\\textbf':Js('textbf'),'\\textmd':Js('textmd')}))
        var.put('textFontShapes', Js({'\\textit':Js('textit'),'\\textup':Js('textup')}))
        @Js
        def PyJs_optionsWithFont_331_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'optionsWithFont':PyJs_optionsWithFont_331_}, var)
            var.registers(['font', 'group', 'options'])
            var.put('font', var.get('group').get('font'))
            if var.get('font').neg():
                return var.get('options')
            else:
                if var.get('textFontFamilies').get(var.get('font')):
                    return var.get('options').callprop('withTextFontFamily', var.get('textFontFamilies').get(var.get('font')))
                else:
                    if var.get('textFontWeights').get(var.get('font')):
                        return var.get('options').callprop('withTextFontWeight', var.get('textFontWeights').get(var.get('font')))
                    else:
                        return var.get('options').callprop('withTextFontShape', var.get('textFontShapes').get(var.get('font')))
        PyJs_optionsWithFont_331_._set_name('optionsWithFont')
        var.put('optionsWithFont', PyJs_optionsWithFont_331_)
        def PyJs_LONG_335_(var=var):
            @Js
            def PyJs_handler_332_(_ref, args, this, arguments, var=var):
                var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_332_}, var)
                var.registers(['funcName', 'body', '_ref', 'args', 'parser'])
                var.put('parser', var.get('_ref').get('parser'))
                var.put('funcName', var.get('_ref').get('funcName'))
                var.put('body', var.get('args').get('0'))
                return Js({'type':Js('text'),'mode':var.get('parser').get('mode'),'body':var.get('defineFunction_ordargument')(var.get('body')),'font':var.get('funcName')})
            PyJs_handler_332_._set_name('handler')
            @Js
            def PyJs_htmlBuilder_333_(group, options, this, arguments, var=var):
                var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_333_}, var)
                var.registers(['newOptions', 'inner', 'group', 'options'])
                var.put('newOptions', var.get('optionsWithFont')(var.get('group'), var.get('options')))
                var.put('inner', var.get('buildHTML_buildExpression')(var.get('group').get('body'), var.get('newOptions'), Js(True)))
                return var.get('buildCommon').callprop('makeSpan', Js([Js('mord'), Js('text')]), var.get('buildCommon').callprop('tryCombineChars', var.get('inner')), var.get('newOptions'))
            PyJs_htmlBuilder_333_._set_name('htmlBuilder')
            @Js
            def PyJs_mathmlBuilder_334_(group, options, this, arguments, var=var):
                var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_334_}, var)
                var.registers(['newOptions', 'group', 'options'])
                var.put('newOptions', var.get('optionsWithFont')(var.get('group'), var.get('options')))
                return var.get('buildExpressionRow')(var.get('group').get('body'), var.get('newOptions'))
            PyJs_mathmlBuilder_334_._set_name('mathmlBuilder')
            return var.get('defineFunction')(Js({'type':Js('text'),'names':Js([Js('\\text'), Js('\\textrm'), Js('\\textsf'), Js('\\texttt'), Js('\\textnormal'), Js('\\textbf'), Js('\\textmd'), Js('\\textit'), Js('\\textup')]),'props':Js({'numArgs':Js(1.0),'argTypes':Js([Js('text')]),'greediness':Js(2.0),'allowedInText':Js(True),'consumeMode':Js('text')}),'handler':PyJs_handler_332_,'htmlBuilder':PyJs_htmlBuilder_333_,'mathmlBuilder':PyJs_mathmlBuilder_334_}))
        PyJs_LONG_335_()
        @Js
        def PyJs_handler_336_(_ref, args, this, arguments, var=var):
            var = Scope({'_ref':_ref, 'args':args, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_336_}, var)
            var.registers(['parser', '_ref', 'args'])
            var.put('parser', var.get('_ref').get('parser'))
            return Js({'type':Js('underline'),'mode':var.get('parser').get('mode'),'body':var.get('args').get('0')})
        PyJs_handler_336_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_337_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_337_}, var)
            var.registers(['group', 'options', 'line', 'innerGroup', 'vlist'])
            var.put('innerGroup', var.get('buildHTML_buildGroup')(var.get('group').get('body'), var.get('options')))
            var.put('line', var.get('buildCommon').callprop('makeLineSpan', Js('underline-line'), var.get('options')))
            var.put('vlist', var.get('buildCommon').callprop('makeVList', Js({'positionType':Js('top'),'positionData':var.get('innerGroup').get('height'),'children':Js([Js({'type':Js('kern'),'size':var.get('line').get('height')}), Js({'type':Js('elem'),'elem':var.get('line')}), Js({'type':Js('kern'),'size':(Js(3.0)*var.get('line').get('height'))}), Js({'type':Js('elem'),'elem':var.get('innerGroup')})])}), var.get('options')))
            return var.get('buildCommon').callprop('makeSpan', Js([Js('mord'), Js('underline')]), Js([var.get('vlist')]), var.get('options'))
        PyJs_htmlBuilder_337_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_338_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_338_}, var)
            var.registers(['node', 'group', 'options', 'operator'])
            var.put('operator', var.get('mathMLTree').get('MathNode').create(Js('mo'), Js([var.get('mathMLTree').get('TextNode').create(Js('‾'))])))
            var.get('operator').callprop('setAttribute', Js('stretchy'), Js('true'))
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('munder'), Js([var.get('buildMathML_buildGroup')(var.get('group').get('body'), var.get('options')), var.get('operator')])))
            var.get('node').callprop('setAttribute', Js('accentunder'), Js('true'))
            return var.get('node')
        PyJs_mathmlBuilder_338_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('underline'),'names':Js([Js('\\underline')]),'props':Js({'numArgs':Js(1.0),'allowedInText':Js(True)}),'handler':PyJs_handler_336_,'htmlBuilder':PyJs_htmlBuilder_337_,'mathmlBuilder':PyJs_mathmlBuilder_338_}))
        @Js
        def PyJs_handler_339_(context, args, optArgs, this, arguments, var=var):
            var = Scope({'context':context, 'args':args, 'optArgs':optArgs, 'this':this, 'arguments':arguments, 'handler':PyJs_handler_339_}, var)
            var.registers(['context', 'optArgs', 'args'])
            PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('\\verb ended by end of line instead of matching delimiter')))
            raise PyJsTempException
        PyJs_handler_339_._set_name('handler')
        @Js
        def PyJs_htmlBuilder_340_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'htmlBuilder':PyJs_htmlBuilder_340_}, var)
            var.registers(['c', 'i', 'body', 'newOptions', 'group', 'text', 'options'])
            var.put('text', var.get('makeVerb')(var.get('group')))
            var.put('body', Js([]))
            var.put('newOptions', var.get('options').callprop('havingStyle', var.get('options').get('style').callprop('text')))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('text').get('length')):
                try:
                    var.put('c', var.get('text').get(var.get('i')))
                    if PyJsStrictEq(var.get('c'),Js('~')):
                        var.put('c', Js('\\textasciitilde'))
                    var.get('body').callprop('push', var.get('buildCommon').callprop('makeSymbol', var.get('c'), Js('Typewriter-Regular'), var.get('group').get('mode'), var.get('newOptions'), Js([Js('mord'), Js('texttt')])))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            return var.get('buildCommon').callprop('makeSpan', Js([Js('mord'), Js('text')]).callprop('concat', var.get('newOptions').callprop('sizingClasses', var.get('options'))), var.get('buildCommon').callprop('tryCombineChars', var.get('body')), var.get('newOptions'))
        PyJs_htmlBuilder_340_._set_name('htmlBuilder')
        @Js
        def PyJs_mathmlBuilder_341_(group, options, this, arguments, var=var):
            var = Scope({'group':group, 'options':options, 'this':this, 'arguments':arguments, 'mathmlBuilder':PyJs_mathmlBuilder_341_}, var)
            var.registers(['node', 'group', 'text', 'options'])
            var.put('text', var.get('mathMLTree').get('TextNode').create(var.get('makeVerb')(var.get('group'))))
            var.put('node', var.get('mathMLTree').get('MathNode').create(Js('mtext'), Js([var.get('text')])))
            var.get('node').callprop('setAttribute', Js('mathvariant'), Js('monospace'))
            return var.get('node')
        PyJs_mathmlBuilder_341_._set_name('mathmlBuilder')
        var.get('defineFunction')(Js({'type':Js('verb'),'names':Js([Js('\\verb')]),'props':Js({'numArgs':Js(0.0),'allowedInText':Js(True)}),'handler':PyJs_handler_339_,'htmlBuilder':PyJs_htmlBuilder_340_,'mathmlBuilder':PyJs_mathmlBuilder_341_}))
        @Js
        def PyJs_makeVerb_342_(group, this, arguments, var=var):
            var = Scope({'group':group, 'this':this, 'arguments':arguments, 'makeVerb':PyJs_makeVerb_342_}, var)
            var.registers(['group'])
            return var.get('group').get('body').callprop('replace', JsRegExp('/ /g'), (Js('␣') if var.get('group').get('star') else Js('\xa0')))
        PyJs_makeVerb_342_._set_name('makeVerb')
        var.put('makeVerb', PyJs_makeVerb_342_)
        var.put('functions', var.get('_functions'))
        var.put('src_functions', var.get('functions'))
        var.put('spaceRegexString', Js('[ \r\n\t]'))
        var.put('controlWordRegexString', Js('\\\\[a-zA-Z@]+'))
        var.put('controlSymbolRegexString', Js('\\\\[^\ud800-\udfff]'))
        var.put('controlWordWhitespaceRegexString', (((Js('')+var.get('controlWordRegexString'))+var.get('spaceRegexString'))+Js('*')))
        var.put('controlWordWhitespaceRegex', var.get('RegExp').create(((((Js('^(')+var.get('controlWordRegexString'))+Js(')'))+var.get('spaceRegexString'))+Js('*$'))))
        var.put('combiningDiacriticalMarkString', Js('[̀-ͯ]'))
        var.put('combiningDiacriticalMarksEndRegex', var.get('RegExp').create((var.get('combiningDiacriticalMarkString')+Js('+$'))))
        def PyJs_LONG_343_(var=var):
            return ((((((((((Js('(')+var.get('spaceRegexString'))+Js('+)|'))+Js('([!-\\[\\]-‧\u202a-\ud7ff豈-\uffff]'))+(var.get('combiningDiacriticalMarkString')+Js('*')))+Js('|[\ud800-\udbff][\udc00-\udfff]'))+(var.get('combiningDiacriticalMarkString')+Js('*')))+Js('|\\\\verb\\*([^]).*?\\3'))+Js('|\\\\verb([^*a-zA-Z]).*?\\4'))+(Js('|')+var.get('controlWordWhitespaceRegexString')))+((Js('|')+var.get('controlSymbolRegexString'))+Js(')')))
        var.put('tokenRegexString', PyJs_LONG_343_())
        @Js
        def PyJs_anonymous_344_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['_proto', 'Lexer'])
            @Js
            def PyJsHoisted_Lexer_(input, settings, this, arguments, var=var):
                var = Scope({'input':input, 'settings':settings, 'this':this, 'arguments':arguments}, var)
                var.registers(['input', 'settings'])
                var.get(u"this").put('input', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('settings', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('tokenRegex', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('catcodes', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('input', var.get('input'))
                var.get(u"this").put('settings', var.get('settings'))
                var.get(u"this").put('tokenRegex', var.get('RegExp').create(var.get('tokenRegexString'), Js('g')))
                var.get(u"this").put('catcodes', Js({'%':Js(14.0)}))
            PyJsHoisted_Lexer_.func_name = 'Lexer'
            var.put('Lexer', PyJsHoisted_Lexer_)
            pass
            var.put('_proto', var.get('Lexer').get('prototype'))
            @Js
            def PyJs_setCatcode_345_(char, code, this, arguments, var=var):
                var = Scope({'char':char, 'code':code, 'this':this, 'arguments':arguments, 'setCatcode':PyJs_setCatcode_345_}, var)
                var.registers(['char', 'code'])
                var.get(u"this").get('catcodes').put(var.get('char'), var.get('code'))
            PyJs_setCatcode_345_._set_name('setCatcode')
            var.get('_proto').put('setCatcode', PyJs_setCatcode_345_)
            @Js
            def PyJs_lex_346_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'lex':PyJs_lex_346_}, var)
                var.registers(['input', 'text', 'pos', 'nlIndex', 'controlMatch', 'match'])
                var.put('input', var.get(u"this").get('input'))
                var.put('pos', var.get(u"this").get('tokenRegex').get('lastIndex'))
                if PyJsStrictEq(var.get('pos'),var.get('input').get('length')):
                    return var.get('Token_Token').create(Js('EOF'), var.get('SourceLocation').create(var.get(u"this"), var.get('pos'), var.get('pos')))
                var.put('match', var.get(u"this").get('tokenRegex').callprop('exec', var.get('input')))
                if (PyJsStrictEq(var.get('match'),var.get(u"null")) or PyJsStrictNeq(var.get('match').get('index'),var.get('pos'))):
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js("Unexpected character: '")+var.get('input').get(var.get('pos')))+Js("'")), var.get('Token_Token').create(var.get('input').get(var.get('pos')), var.get('SourceLocation').create(var.get(u"this"), var.get('pos'), (var.get('pos')+Js(1.0))))))
                    raise PyJsTempException
                var.put('text', (var.get('match').get('2') or Js(' ')))
                if PyJsStrictEq(var.get(u"this").get('catcodes').get(var.get('text')),Js(14.0)):
                    var.put('nlIndex', var.get('input').callprop('indexOf', Js('\n'), var.get(u"this").get('tokenRegex').get('lastIndex')))
                    if PyJsStrictEq(var.get('nlIndex'),(-Js(1.0))):
                        var.get(u"this").get('tokenRegex').put('lastIndex', var.get('input').get('length'))
                        var.get(u"this").get('settings').callprop('reportNonstrict', Js('commentAtEnd'), (Js('% comment has no terminating newline; LaTeX would ')+Js('fail because of commenting the end of math mode (e.g. $)')))
                    else:
                        var.get(u"this").get('tokenRegex').put('lastIndex', (var.get('nlIndex')+Js(1.0)))
                    return var.get(u"this").callprop('lex')
                var.put('controlMatch', var.get('text').callprop('match', var.get('controlWordWhitespaceRegex')))
                if var.get('controlMatch'):
                    var.put('text', var.get('controlMatch').get('1'))
                return var.get('Token_Token').create(var.get('text'), var.get('SourceLocation').create(var.get(u"this"), var.get('pos'), var.get(u"this").get('tokenRegex').get('lastIndex')))
            PyJs_lex_346_._set_name('lex')
            var.get('_proto').put('lex', PyJs_lex_346_)
            return var.get('Lexer')
        PyJs_anonymous_344_._set_name('anonymous')
        var.put('Lexer_Lexer', PyJs_anonymous_344_())
        @Js
        def PyJs_anonymous_347_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['_proto', 'Namespace'])
            @Js
            def PyJsHoisted_Namespace_(builtins, globalMacros, this, arguments, var=var):
                var = Scope({'builtins':builtins, 'globalMacros':globalMacros, 'this':this, 'arguments':arguments}, var)
                var.registers(['builtins', 'globalMacros'])
                if PyJsStrictEq(var.get('builtins'),PyJsComma(Js(0.0), Js(None))):
                    var.put('builtins', Js({}))
                if PyJsStrictEq(var.get('globalMacros'),PyJsComma(Js(0.0), Js(None))):
                    var.put('globalMacros', Js({}))
                var.get(u"this").put('current', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('builtins', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('undefStack', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('current', var.get('globalMacros'))
                var.get(u"this").put('builtins', var.get('builtins'))
                var.get(u"this").put('undefStack', Js([]))
            PyJsHoisted_Namespace_.func_name = 'Namespace'
            var.put('Namespace', PyJsHoisted_Namespace_)
            pass
            var.put('_proto', var.get('Namespace').get('prototype'))
            @Js
            def PyJs_beginGroup_348_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'beginGroup':PyJs_beginGroup_348_}, var)
                var.registers([])
                var.get(u"this").get('undefStack').callprop('push', Js({}))
            PyJs_beginGroup_348_._set_name('beginGroup')
            var.get('_proto').put('beginGroup', PyJs_beginGroup_348_)
            @Js
            def PyJs_endGroup_349_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'endGroup':PyJs_endGroup_349_}, var)
                var.registers(['undefs', 'undef'])
                if PyJsStrictEq(var.get(u"this").get('undefStack').get('length'),Js(0.0)):
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create((Js('Unbalanced namespace destruction: attempt ')+Js('to pop global namespace; please report this as a bug'))))
                    raise PyJsTempException
                var.put('undefs', var.get(u"this").get('undefStack').callprop('pop'))
                for PyJsTemp in var.get('undefs'):
                    var.put('undef', PyJsTemp)
                    if var.get('undefs').callprop('hasOwnProperty', var.get('undef')):
                        if PyJsStrictEq(var.get('undefs').get(var.get('undef')),var.get('undefined')):
                            var.get(u"this").get('current').delete(var.get('undef'))
                        else:
                            var.get(u"this").get('current').put(var.get('undef'), var.get('undefs').get(var.get('undef')))
            PyJs_endGroup_349_._set_name('endGroup')
            var.get('_proto').put('endGroup', PyJs_endGroup_349_)
            @Js
            def PyJs_has_350_(name, this, arguments, var=var):
                var = Scope({'name':name, 'this':this, 'arguments':arguments, 'has':PyJs_has_350_}, var)
                var.registers(['name'])
                return (var.get(u"this").get('current').callprop('hasOwnProperty', var.get('name')) or var.get(u"this").get('builtins').callprop('hasOwnProperty', var.get('name')))
            PyJs_has_350_._set_name('has')
            var.get('_proto').put('has', PyJs_has_350_)
            @Js
            def PyJs_get_351_(name, this, arguments, var=var):
                var = Scope({'name':name, 'this':this, 'arguments':arguments, 'get':PyJs_get_351_}, var)
                var.registers(['name'])
                if var.get(u"this").get('current').callprop('hasOwnProperty', var.get('name')):
                    return var.get(u"this").get('current').get(var.get('name'))
                else:
                    return var.get(u"this").get('builtins').get(var.get('name'))
            PyJs_get_351_._set_name('get')
            var.get('_proto').put('get', PyJs_get_351_)
            @Js
            def PyJs_set_352_(name, value, PyJsArg_676c6f62616c_, this, arguments, var=var):
                var = Scope({'name':name, 'value':value, 'global':PyJsArg_676c6f62616c_, 'this':this, 'arguments':arguments, 'set':PyJs_set_352_}, var)
                var.registers(['i', 'top', 'name', 'global', 'value'])
                if PyJsStrictEq(var.get('global'),PyJsComma(Js(0.0), Js(None))):
                    var.put('global', Js(False))
                if var.get('global'):
                    #for JS loop
                    var.put('i', Js(0.0))
                    while (var.get('i')<var.get(u"this").get('undefStack').get('length')):
                        try:
                            var.get(u"this").get('undefStack').get(var.get('i')).delete(var.get('name'))
                        finally:
                                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                    if (var.get(u"this").get('undefStack').get('length')>Js(0.0)):
                        var.get(u"this").get('undefStack').get((var.get(u"this").get('undefStack').get('length')-Js(1.0))).put(var.get('name'), var.get('value'))
                else:
                    var.put('top', var.get(u"this").get('undefStack').get((var.get(u"this").get('undefStack').get('length')-Js(1.0))))
                    if (var.get('top') and var.get('top').callprop('hasOwnProperty', var.get('name')).neg()):
                        var.get('top').put(var.get('name'), var.get(u"this").get('current').get(var.get('name')))
                var.get(u"this").get('current').put(var.get('name'), var.get('value'))
            PyJs_set_352_._set_name('set')
            var.get('_proto').put('set', PyJs_set_352_)
            return var.get('Namespace')
        PyJs_anonymous_347_._set_name('anonymous')
        var.put('Namespace_Namespace', PyJs_anonymous_347_())
        var.put('builtinMacros', Js({}))
        var.put('macros', var.get('builtinMacros'))
        pass
        @Js
        def PyJs_anonymous_353_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments}, var)
            var.registers(['context', 'args'])
            var.put('args', var.get('context').callprop('consumeArgs', Js(2.0)))
            return Js({'tokens':var.get('args').get('0'),'numArgs':Js(0.0)})
        PyJs_anonymous_353_._set_name('anonymous')
        var.get('defineMacro')(Js('\\@firstoftwo'), PyJs_anonymous_353_)
        @Js
        def PyJs_anonymous_354_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments}, var)
            var.registers(['context', 'args'])
            var.put('args', var.get('context').callprop('consumeArgs', Js(2.0)))
            return Js({'tokens':var.get('args').get('1'),'numArgs':Js(0.0)})
        PyJs_anonymous_354_._set_name('anonymous')
        var.get('defineMacro')(Js('\\@secondoftwo'), PyJs_anonymous_354_)
        @Js
        def PyJs_anonymous_355_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments}, var)
            var.registers(['nextToken', 'context', 'args'])
            var.put('args', var.get('context').callprop('consumeArgs', Js(3.0)))
            var.put('nextToken', var.get('context').callprop('future'))
            if (PyJsStrictEq(var.get('args').get('0').get('length'),Js(1.0)) and PyJsStrictEq(var.get('args').get('0').get('0').get('text'),var.get('nextToken').get('text'))):
                return Js({'tokens':var.get('args').get('1'),'numArgs':Js(0.0)})
            else:
                return Js({'tokens':var.get('args').get('2'),'numArgs':Js(0.0)})
        PyJs_anonymous_355_._set_name('anonymous')
        var.get('defineMacro')(Js('\\@ifnextchar'), PyJs_anonymous_355_)
        var.get('defineMacro')(Js('\\@ifstar'), Js('\\@ifnextchar *{\\@firstoftwo{#1}}'))
        @Js
        def PyJs_anonymous_356_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments}, var)
            var.registers(['context', 'args'])
            var.put('args', var.get('context').callprop('consumeArgs', Js(2.0)))
            if PyJsStrictEq(var.get('context').get('mode'),Js('text')):
                return Js({'tokens':var.get('args').get('0'),'numArgs':Js(0.0)})
            else:
                return Js({'tokens':var.get('args').get('1'),'numArgs':Js(0.0)})
        PyJs_anonymous_356_._set_name('anonymous')
        var.get('defineMacro')(Js('\\TextOrMath'), PyJs_anonymous_356_)
        var.put('digitToNumber', Js({'0':Js(0.0),'1':Js(1.0),'2':Js(2.0),'3':Js(3.0),'4':Js(4.0),'5':Js(5.0),'6':Js(6.0),'7':Js(7.0),'8':Js(8.0),'9':Js(9.0),'a':Js(10.0),'A':Js(10.0),'b':Js(11.0),'B':Js(11.0),'c':Js(12.0),'C':Js(12.0),'d':Js(13.0),'D':Js(13.0),'e':Js(14.0),'E':Js(14.0),'f':Js(15.0),'F':Js(15.0)}))
        @Js
        def PyJs_anonymous_357_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments}, var)
            var.registers(['digit', 'context', 'token', 'base', 'number'])
            var.put('token', var.get('context').callprop('popToken'))
            pass
            var.put('number', Js(''))
            if PyJsStrictEq(var.get('token').get('text'),Js("'")):
                var.put('base', Js(8.0))
                var.put('token', var.get('context').callprop('popToken'))
            else:
                if PyJsStrictEq(var.get('token').get('text'),Js('"')):
                    var.put('base', Js(16.0))
                    var.put('token', var.get('context').callprop('popToken'))
                else:
                    if PyJsStrictEq(var.get('token').get('text'),Js('`')):
                        var.put('token', var.get('context').callprop('popToken'))
                        if PyJsStrictEq(var.get('token').get('text').get('0'),Js('\\')):
                            var.put('number', var.get('token').get('text').callprop('charCodeAt', Js(1.0)))
                        else:
                            if PyJsStrictEq(var.get('token').get('text'),Js('EOF')):
                                PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('\\char` missing argument')))
                                raise PyJsTempException
                            else:
                                var.put('number', var.get('token').get('text').callprop('charCodeAt', Js(0.0)))
                    else:
                        var.put('base', Js(10.0))
            if var.get('base'):
                var.put('number', var.get('digitToNumber').get(var.get('token').get('text')))
                if ((var.get('number')==var.get(u"null")) or (var.get('number')>=var.get('base'))):
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create((((Js('Invalid base-')+var.get('base'))+Js(' digit '))+var.get('token').get('text'))))
                    raise PyJsTempException
                pass
                while ((var.put('digit', var.get('digitToNumber').get(var.get('context').callprop('future').get('text')))!=var.get(u"null")) and (var.get('digit')<var.get('base'))):
                    var.put('number', var.get('base'), '*')
                    var.put('number', var.get('digit'), '+')
                    var.get('context').callprop('popToken')
            return ((Js('\\@char{')+var.get('number'))+Js('}'))
        PyJs_anonymous_357_._set_name('anonymous')
        var.get('defineMacro')(Js('\\char'), PyJs_anonymous_357_)
        @Js
        def PyJs_InlineNonPyName_358_(context, PyJsArg_676c6f62616c_, this, arguments, var=var):
            var = Scope({'context':context, 'global':PyJsArg_676c6f62616c_, 'this':this, 'arguments':arguments, 'def':PyJs_InlineNonPyName_358_}, var)
            var.registers(['context', 'arg', 'name', 'numArgs', 'global'])
            var.put('arg', var.get('context').callprop('consumeArgs', Js(1.0)).get('0'))
            if PyJsStrictNeq(var.get('arg').get('length'),Js(1.0)):
                PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js("\\gdef's first argument must be a macro name")))
                raise PyJsTempException
            var.put('name', var.get('arg').get('0').get('text'))
            var.put('numArgs', Js(0.0))
            var.put('arg', var.get('context').callprop('consumeArgs', Js(1.0)).get('0'))
            while (PyJsStrictEq(var.get('arg').get('length'),Js(1.0)) and PyJsStrictEq(var.get('arg').get('0').get('text'),Js('#'))):
                var.put('arg', var.get('context').callprop('consumeArgs', Js(1.0)).get('0'))
                if PyJsStrictNeq(var.get('arg').get('length'),Js(1.0)):
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js('Invalid argument number length "')+var.get('arg').get('length'))+Js('"'))))
                    raise PyJsTempException
                if JsRegExp('/^[1-9]$/').callprop('test', var.get('arg').get('0').get('text')).neg():
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js('Invalid argument number "')+var.get('arg').get('0').get('text'))+Js('"'))))
                    raise PyJsTempException
                (var.put('numArgs',Js(var.get('numArgs').to_number())+Js(1))-Js(1))
                if PyJsStrictNeq(var.get('parseInt')(var.get('arg').get('0').get('text')),var.get('numArgs')):
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js('Argument number "')+var.get('arg').get('0').get('text'))+Js('" out of order'))))
                    raise PyJsTempException
                var.put('arg', var.get('context').callprop('consumeArgs', Js(1.0)).get('0'))
            var.get('context').get('macros').callprop('set', var.get('name'), Js({'tokens':var.get('arg'),'numArgs':var.get('numArgs')}), var.get('global'))
            return Js('')
        PyJs_InlineNonPyName_358_._set_name('def')
        var.put('macros_def', PyJs_InlineNonPyName_358_)
        @Js
        def PyJs_anonymous_359_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments}, var)
            var.registers(['context'])
            return var.get('macros_def')(var.get('context'), Js(True))
        PyJs_anonymous_359_._set_name('anonymous')
        var.get('defineMacro')(Js('\\gdef'), PyJs_anonymous_359_)
        @Js
        def PyJs_anonymous_360_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments}, var)
            var.registers(['context'])
            return var.get('macros_def')(var.get('context'), Js(False))
        PyJs_anonymous_360_._set_name('anonymous')
        var.get('defineMacro')(Js('\\def'), PyJs_anonymous_360_)
        @Js
        def PyJs_anonymous_361_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments}, var)
            var.registers(['command', 'context', 'next'])
            var.put('next', var.get('context').callprop('consumeArgs', Js(1.0)).get('0'))
            if PyJsStrictNeq(var.get('next').get('length'),Js(1.0)):
                PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('Invalid command after \\global')))
                raise PyJsTempException
            var.put('command', var.get('next').get('0').get('text'))
            if PyJsStrictEq(var.get('command'),Js('\\def')):
                return var.get('macros_def')(var.get('context'), Js(True))
            else:
                PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js("Invalid command '")+var.get('command'))+Js("' after \\global"))))
                raise PyJsTempException
        PyJs_anonymous_361_._set_name('anonymous')
        var.get('defineMacro')(Js('\\global'), PyJs_anonymous_361_)
        @Js
        def PyJs_newcommand_362_(context, existsOK, nonexistsOK, this, arguments, var=var):
            var = Scope({'context':context, 'existsOK':existsOK, 'nonexistsOK':nonexistsOK, 'this':this, 'arguments':arguments, 'newcommand':PyJs_newcommand_362_}, var)
            var.registers(['argText', 'context', 'arg', 'nonexistsOK', 'name', 'token', 'numArgs', 'existsOK', 'exists'])
            var.put('arg', var.get('context').callprop('consumeArgs', Js(1.0)).get('0'))
            if PyJsStrictNeq(var.get('arg').get('length'),Js(1.0)):
                PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js("\\newcommand's first argument must be a macro name")))
                raise PyJsTempException
            var.put('name', var.get('arg').get('0').get('text'))
            var.put('exists', var.get('context').callprop('isDefined', var.get('name')))
            if (var.get('exists') and var.get('existsOK').neg()):
                PyJsTempException = JsToPyException(var.get('src_ParseError').create((((Js('\\newcommand{')+var.get('name'))+Js('} attempting to redefine '))+(var.get('name')+Js('; use \\renewcommand')))))
                raise PyJsTempException
            if (var.get('exists').neg() and var.get('nonexistsOK').neg()):
                PyJsTempException = JsToPyException(var.get('src_ParseError').create((((((Js('\\renewcommand{')+var.get('name'))+Js('} when command '))+var.get('name'))+Js(' '))+Js('does not yet exist; use \\newcommand'))))
                raise PyJsTempException
            var.put('numArgs', Js(0.0))
            var.put('arg', var.get('context').callprop('consumeArgs', Js(1.0)).get('0'))
            if (PyJsStrictEq(var.get('arg').get('length'),Js(1.0)) and PyJsStrictEq(var.get('arg').get('0').get('text'),Js('['))):
                var.put('argText', Js(''))
                var.put('token', var.get('context').callprop('expandNextToken'))
                while (PyJsStrictNeq(var.get('token').get('text'),Js(']')) and PyJsStrictNeq(var.get('token').get('text'),Js('EOF'))):
                    var.put('argText', var.get('token').get('text'), '+')
                    var.put('token', var.get('context').callprop('expandNextToken'))
                if var.get('argText').callprop('match', JsRegExp('/^\\s*[0-9]+\\s*$/')).neg():
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create((Js('Invalid number of arguments: ')+var.get('argText'))))
                    raise PyJsTempException
                var.put('numArgs', var.get('parseInt')(var.get('argText')))
                var.put('arg', var.get('context').callprop('consumeArgs', Js(1.0)).get('0'))
            var.get('context').get('macros').callprop('set', var.get('name'), Js({'tokens':var.get('arg'),'numArgs':var.get('numArgs')}))
            return Js('')
        PyJs_newcommand_362_._set_name('newcommand')
        var.put('macros_newcommand', PyJs_newcommand_362_)
        @Js
        def PyJs_anonymous_363_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments}, var)
            var.registers(['context'])
            return var.get('macros_newcommand')(var.get('context'), Js(False), Js(True))
        PyJs_anonymous_363_._set_name('anonymous')
        var.get('defineMacro')(Js('\\newcommand'), PyJs_anonymous_363_)
        @Js
        def PyJs_anonymous_364_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments}, var)
            var.registers(['context'])
            return var.get('macros_newcommand')(var.get('context'), Js(True), Js(False))
        PyJs_anonymous_364_._set_name('anonymous')
        var.get('defineMacro')(Js('\\renewcommand'), PyJs_anonymous_364_)
        @Js
        def PyJs_anonymous_365_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments}, var)
            var.registers(['context'])
            return var.get('macros_newcommand')(var.get('context'), Js(True), Js(True))
        PyJs_anonymous_365_._set_name('anonymous')
        var.get('defineMacro')(Js('\\providecommand'), PyJs_anonymous_365_)
        var.get('defineMacro')(Js('\\bgroup'), Js('{'))
        var.get('defineMacro')(Js('\\egroup'), Js('}'))
        var.get('defineMacro')(Js('\\lq'), Js('`'))
        var.get('defineMacro')(Js('\\rq'), Js("'"))
        var.get('defineMacro')(Js('\\aa'), Js('\\r a'))
        var.get('defineMacro')(Js('\\AA'), Js('\\r A'))
        var.get('defineMacro')(Js('\\textcopyright'), Js('\\html@mathml{\\textcircled{c}}{\\char`©}'))
        var.get('defineMacro')(Js('\\copyright'), Js('\\TextOrMath{\\textcopyright}{\\text{\\textcopyright}}'))
        var.get('defineMacro')(Js('\\textregistered'), Js('\\html@mathml{\\textcircled{\\scriptsize R}}{\\char`®}'))
        var.get('defineMacro')(Js('ℬ'), Js('\\mathscr{B}'))
        var.get('defineMacro')(Js('ℰ'), Js('\\mathscr{E}'))
        var.get('defineMacro')(Js('ℱ'), Js('\\mathscr{F}'))
        var.get('defineMacro')(Js('ℋ'), Js('\\mathscr{H}'))
        var.get('defineMacro')(Js('ℐ'), Js('\\mathscr{I}'))
        var.get('defineMacro')(Js('ℒ'), Js('\\mathscr{L}'))
        var.get('defineMacro')(Js('ℳ'), Js('\\mathscr{M}'))
        var.get('defineMacro')(Js('ℛ'), Js('\\mathscr{R}'))
        var.get('defineMacro')(Js('ℭ'), Js('\\mathfrak{C}'))
        var.get('defineMacro')(Js('ℌ'), Js('\\mathfrak{H}'))
        var.get('defineMacro')(Js('ℨ'), Js('\\mathfrak{Z}'))
        var.get('defineMacro')(Js('\\Bbbk'), Js('\\Bbb{k}'))
        var.get('defineMacro')(Js('·'), Js('\\cdotp'))
        var.get('defineMacro')(Js('≘'), ((Js('\\html@mathml{')+Js('\\mathrel{=\\kern{-1em}\\raisebox{0.4em}{$\\scriptsize\\frown$}}'))+Js('}{\\mathrel{\\char`≘}}')))
        var.get('defineMacro')(Js('≙'), Js('\\html@mathml{\\stackrel{\\tiny\\wedge}{=}}{\\mathrel{\\char`≘}}'))
        var.get('defineMacro')(Js('≚'), Js('\\html@mathml{\\stackrel{\\tiny\\vee}{=}}{\\mathrel{\\char`≚}}'))
        var.get('defineMacro')(Js('≛'), (Js('\\html@mathml{\\stackrel{\\scriptsize\\star}{=}}')+Js('{\\mathrel{\\char`≛}}')))
        var.get('defineMacro')(Js('≝'), (Js('\\html@mathml{\\stackrel{\\tiny\\mathrm{def}}{=}}')+Js('{\\mathrel{\\char`≝}}')))
        var.get('defineMacro')(Js('≞'), (Js('\\html@mathml{\\stackrel{\\tiny\\mathrm{m}}{=}}')+Js('{\\mathrel{\\char`≞}}')))
        var.get('defineMacro')(Js('≟'), Js('\\html@mathml{\\stackrel{\\tiny?}{=}}{\\mathrel{\\char`≟}}'))
        var.get('defineMacro')(Js('⟂'), Js('\\perp'))
        var.get('defineMacro')(Js('‼'), Js('\\mathclose{!\\mkern-0.8mu!}'))
        var.get('defineMacro')(Js('∌'), Js('\\notni'))
        var.get('defineMacro')(Js('⌜'), Js('\\ulcorner'))
        var.get('defineMacro')(Js('⌝'), Js('\\urcorner'))
        var.get('defineMacro')(Js('⌞'), Js('\\llcorner'))
        var.get('defineMacro')(Js('⌟'), Js('\\lrcorner'))
        var.get('defineMacro')(Js('©'), Js('\\copyright'))
        var.get('defineMacro')(Js('®'), Js('\\textregistered'))
        var.get('defineMacro')(Js('️'), Js('\\textregistered'))
        var.get('defineMacro')(Js('\\vdots'), Js('\\mathord{\\varvdots\\rule{0pt}{15pt}}'))
        var.get('defineMacro')(Js('⋮'), Js('\\vdots'))
        var.get('defineMacro')(Js('\\varGamma'), Js('\\mathit{\\Gamma}'))
        var.get('defineMacro')(Js('\\varDelta'), Js('\\mathit{\\Delta}'))
        var.get('defineMacro')(Js('\\varTheta'), Js('\\mathit{\\Theta}'))
        var.get('defineMacro')(Js('\\varLambda'), Js('\\mathit{\\Lambda}'))
        var.get('defineMacro')(Js('\\varXi'), Js('\\mathit{\\Xi}'))
        var.get('defineMacro')(Js('\\varPi'), Js('\\mathit{\\Pi}'))
        var.get('defineMacro')(Js('\\varSigma'), Js('\\mathit{\\Sigma}'))
        var.get('defineMacro')(Js('\\varUpsilon'), Js('\\mathit{\\Upsilon}'))
        var.get('defineMacro')(Js('\\varPhi'), Js('\\mathit{\\Phi}'))
        var.get('defineMacro')(Js('\\varPsi'), Js('\\mathit{\\Psi}'))
        var.get('defineMacro')(Js('\\varOmega'), Js('\\mathit{\\Omega}'))
        var.get('defineMacro')(Js('\\colon'), (Js('\\nobreak\\mskip2mu\\mathpunct{}')+Js('\\mathchoice{\\mkern-3mu}{\\mkern-3mu}{}{}{:}\\mskip6mu')))
        var.get('defineMacro')(Js('\\boxed'), Js('\\fbox{$\\displaystyle{#1}$}'))
        var.get('defineMacro')(Js('\\iff'), Js('\\DOTSB\\;\\Longleftrightarrow\\;'))
        var.get('defineMacro')(Js('\\implies'), Js('\\DOTSB\\;\\Longrightarrow\\;'))
        var.get('defineMacro')(Js('\\impliedby'), Js('\\DOTSB\\;\\Longleftarrow\\;'))
        var.put('dotsByToken', Js({',':Js('\\dotsc'),'\\not':Js('\\dotsb'),'+':Js('\\dotsb'),'=':Js('\\dotsb'),'<':Js('\\dotsb'),'>':Js('\\dotsb'),'-':Js('\\dotsb'),'*':Js('\\dotsb'),':':Js('\\dotsb'),'\\DOTSB':Js('\\dotsb'),'\\coprod':Js('\\dotsb'),'\\bigvee':Js('\\dotsb'),'\\bigwedge':Js('\\dotsb'),'\\biguplus':Js('\\dotsb'),'\\bigcap':Js('\\dotsb'),'\\bigcup':Js('\\dotsb'),'\\prod':Js('\\dotsb'),'\\sum':Js('\\dotsb'),'\\bigotimes':Js('\\dotsb'),'\\bigoplus':Js('\\dotsb'),'\\bigodot':Js('\\dotsb'),'\\bigsqcup':Js('\\dotsb'),'\\And':Js('\\dotsb'),'\\longrightarrow':Js('\\dotsb'),'\\Longrightarrow':Js('\\dotsb'),'\\longleftarrow':Js('\\dotsb'),'\\Longleftarrow':Js('\\dotsb'),'\\longleftrightarrow':Js('\\dotsb'),'\\Longleftrightarrow':Js('\\dotsb'),'\\mapsto':Js('\\dotsb'),'\\longmapsto':Js('\\dotsb'),'\\hookrightarrow':Js('\\dotsb'),'\\doteq':Js('\\dotsb'),'\\mathbin':Js('\\dotsb'),'\\mathrel':Js('\\dotsb'),'\\relbar':Js('\\dotsb'),'\\Relbar':Js('\\dotsb'),'\\xrightarrow':Js('\\dotsb'),'\\xleftarrow':Js('\\dotsb'),'\\DOTSI':Js('\\dotsi'),'\\int':Js('\\dotsi'),'\\oint':Js('\\dotsi'),'\\iint':Js('\\dotsi'),'\\iiint':Js('\\dotsi'),'\\iiiint':Js('\\dotsi'),'\\idotsint':Js('\\dotsi'),'\\DOTSX':Js('\\dotsx')}))
        @Js
        def PyJs_anonymous_366_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments}, var)
            var.registers(['context', 'next', 'thedots'])
            var.put('thedots', Js('\\dotso'))
            var.put('next', var.get('context').callprop('expandAfterFuture').get('text'))
            if var.get('dotsByToken').contains(var.get('next')):
                var.put('thedots', var.get('dotsByToken').get(var.get('next')))
            else:
                if PyJsStrictEq(var.get('next').callprop('substr', Js(0.0), Js(4.0)),Js('\\not')):
                    var.put('thedots', Js('\\dotsb'))
                else:
                    if var.get('src_symbols').get('math').contains(var.get('next')):
                        if var.get('utils').callprop('contains', Js([Js('bin'), Js('rel')]), var.get('src_symbols').get('math').get(var.get('next')).get('group')):
                            var.put('thedots', Js('\\dotsb'))
            return var.get('thedots')
        PyJs_anonymous_366_._set_name('anonymous')
        var.get('defineMacro')(Js('\\dots'), PyJs_anonymous_366_)
        var.put('spaceAfterDots', Js({')':Js(True),']':Js(True),'\\rbrack':Js(True),'\\}':Js(True),'\\rbrace':Js(True),'\\rangle':Js(True),'\\rceil':Js(True),'\\rfloor':Js(True),'\\rgroup':Js(True),'\\rmoustache':Js(True),'\\right':Js(True),'\\bigr':Js(True),'\\biggr':Js(True),'\\Bigr':Js(True),'\\Biggr':Js(True),'$':Js(True),';':Js(True),'.':Js(True),',':Js(True)}))
        @Js
        def PyJs_anonymous_367_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments}, var)
            var.registers(['context', 'next'])
            var.put('next', var.get('context').callprop('future').get('text'))
            if var.get('spaceAfterDots').contains(var.get('next')):
                return Js('\\ldots\\,')
            else:
                return Js('\\ldots')
        PyJs_anonymous_367_._set_name('anonymous')
        var.get('defineMacro')(Js('\\dotso'), PyJs_anonymous_367_)
        @Js
        def PyJs_anonymous_368_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments}, var)
            var.registers(['context', 'next'])
            var.put('next', var.get('context').callprop('future').get('text'))
            if (var.get('spaceAfterDots').contains(var.get('next')) and PyJsStrictNeq(var.get('next'),Js(','))):
                return Js('\\ldots\\,')
            else:
                return Js('\\ldots')
        PyJs_anonymous_368_._set_name('anonymous')
        var.get('defineMacro')(Js('\\dotsc'), PyJs_anonymous_368_)
        @Js
        def PyJs_anonymous_369_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments}, var)
            var.registers(['context', 'next'])
            var.put('next', var.get('context').callprop('future').get('text'))
            if var.get('spaceAfterDots').contains(var.get('next')):
                return Js('\\@cdots\\,')
            else:
                return Js('\\@cdots')
        PyJs_anonymous_369_._set_name('anonymous')
        var.get('defineMacro')(Js('\\cdots'), PyJs_anonymous_369_)
        var.get('defineMacro')(Js('\\dotsb'), Js('\\cdots'))
        var.get('defineMacro')(Js('\\dotsm'), Js('\\cdots'))
        var.get('defineMacro')(Js('\\dotsi'), Js('\\!\\cdots'))
        var.get('defineMacro')(Js('\\dotsx'), Js('\\ldots\\,'))
        var.get('defineMacro')(Js('\\DOTSI'), Js('\\relax'))
        var.get('defineMacro')(Js('\\DOTSB'), Js('\\relax'))
        var.get('defineMacro')(Js('\\DOTSX'), Js('\\relax'))
        var.get('defineMacro')(Js('\\tmspace'), Js('\\TextOrMath{\\kern#1#3}{\\mskip#1#2}\\relax'))
        var.get('defineMacro')(Js('\\,'), Js('\\tmspace+{3mu}{.1667em}'))
        var.get('defineMacro')(Js('\\thinspace'), Js('\\,'))
        var.get('defineMacro')(Js('\\>'), Js('\\mskip{4mu}'))
        var.get('defineMacro')(Js('\\:'), Js('\\tmspace+{4mu}{.2222em}'))
        var.get('defineMacro')(Js('\\medspace'), Js('\\:'))
        var.get('defineMacro')(Js('\\;'), Js('\\tmspace+{5mu}{.2777em}'))
        var.get('defineMacro')(Js('\\thickspace'), Js('\\;'))
        var.get('defineMacro')(Js('\\!'), Js('\\tmspace-{3mu}{.1667em}'))
        var.get('defineMacro')(Js('\\negthinspace'), Js('\\!'))
        var.get('defineMacro')(Js('\\negmedspace'), Js('\\tmspace-{4mu}{.2222em}'))
        var.get('defineMacro')(Js('\\negthickspace'), Js('\\tmspace-{5mu}{.277em}'))
        var.get('defineMacro')(Js('\\enspace'), Js('\\kern.5em '))
        var.get('defineMacro')(Js('\\enskip'), Js('\\hskip.5em\\relax'))
        var.get('defineMacro')(Js('\\quad'), Js('\\hskip1em\\relax'))
        var.get('defineMacro')(Js('\\qquad'), Js('\\hskip2em\\relax'))
        var.get('defineMacro')(Js('\\tag'), Js('\\@ifstar\\tag@literal\\tag@paren'))
        var.get('defineMacro')(Js('\\tag@paren'), Js('\\tag@literal{({#1})}'))
        @Js
        def PyJs_anonymous_370_(context, this, arguments, var=var):
            var = Scope({'context':context, 'this':this, 'arguments':arguments}, var)
            var.registers(['context'])
            if var.get('context').get('macros').callprop('get', Js('\\df@tag')):
                PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('Multiple \\tag')))
                raise PyJsTempException
            return Js('\\gdef\\df@tag{\\text{#1}}')
        PyJs_anonymous_370_._set_name('anonymous')
        var.get('defineMacro')(Js('\\tag@literal'), PyJs_anonymous_370_)
        var.get('defineMacro')(Js('\\bmod'), ((Js('\\mathchoice{\\mskip1mu}{\\mskip1mu}{\\mskip5mu}{\\mskip5mu}')+Js('\\mathbin{\\rm mod}'))+Js('\\mathchoice{\\mskip1mu}{\\mskip1mu}{\\mskip5mu}{\\mskip5mu}')))
        var.get('defineMacro')(Js('\\pod'), (Js('\\allowbreak')+Js('\\mathchoice{\\mkern18mu}{\\mkern8mu}{\\mkern8mu}{\\mkern8mu}(#1)')))
        var.get('defineMacro')(Js('\\pmod'), Js('\\pod{{\\rm mod}\\mkern6mu#1}'))
        var.get('defineMacro')(Js('\\mod'), ((Js('\\allowbreak')+Js('\\mathchoice{\\mkern18mu}{\\mkern12mu}{\\mkern12mu}{\\mkern12mu}'))+Js('{\\rm mod}\\,\\,#1')))
        var.get('defineMacro')(Js('\\pmb'), ((((Js('\\html@mathml{\\@binrel{#1}{')+Js('\\mathrlap{#1}'))+Js('\\mathrlap{\\mkern0.4mu\\raisebox{0.4mu}{$#1$}}'))+Js('{\\mkern0.8mu#1}'))+Js('}}{\\mathbf{#1}}')))
        var.get('defineMacro')(Js('\\\\'), Js('\\newline'))
        var.get('defineMacro')(Js('\\TeX'), ((Js('\\textrm{\\html@mathml{')+Js('T\\kern-.1667em\\raisebox{-.5ex}{E}\\kern-.125emX'))+Js('}{TeX}}')))
        var.put('latexRaiseA', ((var.get('fontMetricsData').get('Main-Regular').get(Js('T').callprop('charCodeAt', Js(0.0))).get('1')-(Js(0.7)*var.get('fontMetricsData').get('Main-Regular').get(Js('A').callprop('charCodeAt', Js(0.0))).get('1')))+Js('em')))
        var.get('defineMacro')(Js('\\LaTeX'), ((Js('\\textrm{\\html@mathml{')+((Js('L\\kern-.36em\\raisebox{')+var.get('latexRaiseA'))+Js('}{\\scriptsize A}')))+Js('\\kern-.15em\\TeX}{LaTeX}}')))
        var.get('defineMacro')(Js('\\KaTeX'), ((Js('\\textrm{\\html@mathml{')+((Js('K\\kern-.17em\\raisebox{')+var.get('latexRaiseA'))+Js('}{\\scriptsize A}')))+Js('\\kern-.15em\\TeX}{KaTeX}}')))
        var.get('defineMacro')(Js('\\hspace'), Js('\\@ifstar\\@hspacer\\@hspace'))
        var.get('defineMacro')(Js('\\@hspace'), Js('\\hskip #1\\relax'))
        var.get('defineMacro')(Js('\\@hspacer'), Js('\\rule{0pt}{0pt}\\hskip #1\\relax'))
        var.get('defineMacro')(Js('\\ordinarycolon'), Js(':'))
        var.get('defineMacro')(Js('\\vcentcolon'), Js('\\mathrel{\\mathop\\ordinarycolon}'))
        var.get('defineMacro')(Js('\\dblcolon'), ((Js('\\html@mathml{')+Js('\\mathrel{\\vcentcolon\\mathrel{\\mkern-.9mu}\\vcentcolon}}'))+Js('{\\mathop{\\char"2237}}')))
        var.get('defineMacro')(Js('\\coloneqq'), ((Js('\\html@mathml{')+Js('\\mathrel{\\vcentcolon\\mathrel{\\mkern-1.2mu}=}}'))+Js('{\\mathop{\\char"2254}}')))
        var.get('defineMacro')(Js('\\Coloneqq'), ((Js('\\html@mathml{')+Js('\\mathrel{\\dblcolon\\mathrel{\\mkern-1.2mu}=}}'))+Js('{\\mathop{\\char"2237\\char"3d}}')))
        var.get('defineMacro')(Js('\\coloneq'), ((Js('\\html@mathml{')+Js('\\mathrel{\\vcentcolon\\mathrel{\\mkern-1.2mu}\\mathrel{-}}}'))+Js('{\\mathop{\\char"3a\\char"2212}}')))
        var.get('defineMacro')(Js('\\Coloneq'), ((Js('\\html@mathml{')+Js('\\mathrel{\\dblcolon\\mathrel{\\mkern-1.2mu}\\mathrel{-}}}'))+Js('{\\mathop{\\char"2237\\char"2212}}')))
        var.get('defineMacro')(Js('\\eqqcolon'), ((Js('\\html@mathml{')+Js('\\mathrel{=\\mathrel{\\mkern-1.2mu}\\vcentcolon}}'))+Js('{\\mathop{\\char"2255}}')))
        var.get('defineMacro')(Js('\\Eqqcolon'), ((Js('\\html@mathml{')+Js('\\mathrel{=\\mathrel{\\mkern-1.2mu}\\dblcolon}}'))+Js('{\\mathop{\\char"3d\\char"2237}}')))
        var.get('defineMacro')(Js('\\eqcolon'), ((Js('\\html@mathml{')+Js('\\mathrel{\\mathrel{-}\\mathrel{\\mkern-1.2mu}\\vcentcolon}}'))+Js('{\\mathop{\\char"2239}}')))
        var.get('defineMacro')(Js('\\Eqcolon'), ((Js('\\html@mathml{')+Js('\\mathrel{\\mathrel{-}\\mathrel{\\mkern-1.2mu}\\dblcolon}}'))+Js('{\\mathop{\\char"2212\\char"2237}}')))
        var.get('defineMacro')(Js('\\colonapprox'), ((Js('\\html@mathml{')+Js('\\mathrel{\\vcentcolon\\mathrel{\\mkern-1.2mu}\\approx}}'))+Js('{\\mathop{\\char"3a\\char"2248}}')))
        var.get('defineMacro')(Js('\\Colonapprox'), ((Js('\\html@mathml{')+Js('\\mathrel{\\dblcolon\\mathrel{\\mkern-1.2mu}\\approx}}'))+Js('{\\mathop{\\char"2237\\char"2248}}')))
        var.get('defineMacro')(Js('\\colonsim'), ((Js('\\html@mathml{')+Js('\\mathrel{\\vcentcolon\\mathrel{\\mkern-1.2mu}\\sim}}'))+Js('{\\mathop{\\char"3a\\char"223c}}')))
        var.get('defineMacro')(Js('\\Colonsim'), ((Js('\\html@mathml{')+Js('\\mathrel{\\dblcolon\\mathrel{\\mkern-1.2mu}\\sim}}'))+Js('{\\mathop{\\char"2237\\char"223c}}')))
        var.get('defineMacro')(Js('∷'), Js('\\dblcolon'))
        var.get('defineMacro')(Js('∹'), Js('\\eqcolon'))
        var.get('defineMacro')(Js('≔'), Js('\\coloneqq'))
        var.get('defineMacro')(Js('≕'), Js('\\eqqcolon'))
        var.get('defineMacro')(Js('⩴'), Js('\\Coloneqq'))
        var.get('defineMacro')(Js('\\ratio'), Js('\\vcentcolon'))
        var.get('defineMacro')(Js('\\coloncolon'), Js('\\dblcolon'))
        var.get('defineMacro')(Js('\\colonequals'), Js('\\coloneqq'))
        var.get('defineMacro')(Js('\\coloncolonequals'), Js('\\Coloneqq'))
        var.get('defineMacro')(Js('\\equalscolon'), Js('\\eqqcolon'))
        var.get('defineMacro')(Js('\\equalscoloncolon'), Js('\\Eqqcolon'))
        var.get('defineMacro')(Js('\\colonminus'), Js('\\coloneq'))
        var.get('defineMacro')(Js('\\coloncolonminus'), Js('\\Coloneq'))
        var.get('defineMacro')(Js('\\minuscolon'), Js('\\eqcolon'))
        var.get('defineMacro')(Js('\\minuscoloncolon'), Js('\\Eqcolon'))
        var.get('defineMacro')(Js('\\coloncolonapprox'), Js('\\Colonapprox'))
        var.get('defineMacro')(Js('\\coloncolonsim'), Js('\\Colonsim'))
        var.get('defineMacro')(Js('\\simcolon'), Js('\\mathrel{\\sim\\mathrel{\\mkern-1.2mu}\\vcentcolon}'))
        var.get('defineMacro')(Js('\\simcoloncolon'), Js('\\mathrel{\\sim\\mathrel{\\mkern-1.2mu}\\dblcolon}'))
        var.get('defineMacro')(Js('\\approxcolon'), Js('\\mathrel{\\approx\\mathrel{\\mkern-1.2mu}\\vcentcolon}'))
        var.get('defineMacro')(Js('\\approxcoloncolon'), Js('\\mathrel{\\approx\\mathrel{\\mkern-1.2mu}\\dblcolon}'))
        var.get('defineMacro')(Js('\\notni'), Js('\\html@mathml{\\not\\ni}{\\mathrel{\\char`∌}}'))
        var.get('defineMacro')(Js('\\limsup'), Js('\\DOTSB\\mathop{\\operatorname{lim\\,sup}}\\limits'))
        var.get('defineMacro')(Js('\\liminf'), Js('\\DOTSB\\mathop{\\operatorname{lim\\,inf}}\\limits'))
        var.get('defineMacro')(Js('\\gvertneqq'), Js('\\html@mathml{\\@gvertneqq}{≩}'))
        var.get('defineMacro')(Js('\\lvertneqq'), Js('\\html@mathml{\\@lvertneqq}{≨}'))
        var.get('defineMacro')(Js('\\ngeqq'), Js('\\html@mathml{\\@ngeqq}{≱}'))
        var.get('defineMacro')(Js('\\ngeqslant'), Js('\\html@mathml{\\@ngeqslant}{≱}'))
        var.get('defineMacro')(Js('\\nleqq'), Js('\\html@mathml{\\@nleqq}{≰}'))
        var.get('defineMacro')(Js('\\nleqslant'), Js('\\html@mathml{\\@nleqslant}{≰}'))
        var.get('defineMacro')(Js('\\nshortmid'), Js('\\html@mathml{\\@nshortmid}{∤}'))
        var.get('defineMacro')(Js('\\nshortparallel'), Js('\\html@mathml{\\@nshortparallel}{∦}'))
        var.get('defineMacro')(Js('\\nsubseteqq'), Js('\\html@mathml{\\@nsubseteqq}{⊈}'))
        var.get('defineMacro')(Js('\\nsupseteqq'), Js('\\html@mathml{\\@nsupseteqq}{⊉}'))
        var.get('defineMacro')(Js('\\varsubsetneq'), Js('\\html@mathml{\\@varsubsetneq}{⊊}'))
        var.get('defineMacro')(Js('\\varsubsetneqq'), Js('\\html@mathml{\\@varsubsetneqq}{⫋}'))
        var.get('defineMacro')(Js('\\varsupsetneq'), Js('\\html@mathml{\\@varsupsetneq}{⊋}'))
        var.get('defineMacro')(Js('\\varsupsetneqq'), Js('\\html@mathml{\\@varsupsetneqq}{⫌}'))
        var.get('defineMacro')(Js('\\llbracket'), ((Js('\\html@mathml{')+Js('\\mathopen{[\\mkern-3.2mu[}}'))+Js('{\\mathopen{\\char`⟦}}')))
        var.get('defineMacro')(Js('\\rrbracket'), ((Js('\\html@mathml{')+Js('\\mathclose{]\\mkern-3.2mu]}}'))+Js('{\\mathclose{\\char`⟧}}')))
        var.get('defineMacro')(Js('⟦'), Js('\\llbracket'))
        var.get('defineMacro')(Js('⟧'), Js('\\rrbracket'))
        var.get('defineMacro')(Js('\\lBrace'), ((Js('\\html@mathml{')+Js('\\mathopen{\\{\\mkern-3.2mu[}}'))+Js('{\\mathopen{\\char`⦃}}')))
        var.get('defineMacro')(Js('\\rBrace'), ((Js('\\html@mathml{')+Js('\\mathclose{]\\mkern-3.2mu\\}}}'))+Js('{\\mathclose{\\char`⦄}}')))
        var.get('defineMacro')(Js('⦃'), Js('\\lBrace'))
        var.get('defineMacro')(Js('⦄'), Js('\\rBrace'))
        var.get('defineMacro')(Js('\\darr'), Js('\\downarrow'))
        var.get('defineMacro')(Js('\\dArr'), Js('\\Downarrow'))
        var.get('defineMacro')(Js('\\Darr'), Js('\\Downarrow'))
        var.get('defineMacro')(Js('\\lang'), Js('\\langle'))
        var.get('defineMacro')(Js('\\rang'), Js('\\rangle'))
        var.get('defineMacro')(Js('\\uarr'), Js('\\uparrow'))
        var.get('defineMacro')(Js('\\uArr'), Js('\\Uparrow'))
        var.get('defineMacro')(Js('\\Uarr'), Js('\\Uparrow'))
        var.get('defineMacro')(Js('\\N'), Js('\\mathbb{N}'))
        var.get('defineMacro')(Js('\\R'), Js('\\mathbb{R}'))
        var.get('defineMacro')(Js('\\Z'), Js('\\mathbb{Z}'))
        var.get('defineMacro')(Js('\\alef'), Js('\\aleph'))
        var.get('defineMacro')(Js('\\alefsym'), Js('\\aleph'))
        var.get('defineMacro')(Js('\\Alpha'), Js('\\mathrm{A}'))
        var.get('defineMacro')(Js('\\Beta'), Js('\\mathrm{B}'))
        var.get('defineMacro')(Js('\\bull'), Js('\\bullet'))
        var.get('defineMacro')(Js('\\Chi'), Js('\\mathrm{X}'))
        var.get('defineMacro')(Js('\\clubs'), Js('\\clubsuit'))
        var.get('defineMacro')(Js('\\cnums'), Js('\\mathbb{C}'))
        var.get('defineMacro')(Js('\\Complex'), Js('\\mathbb{C}'))
        var.get('defineMacro')(Js('\\Dagger'), Js('\\ddagger'))
        var.get('defineMacro')(Js('\\diamonds'), Js('\\diamondsuit'))
        var.get('defineMacro')(Js('\\empty'), Js('\\emptyset'))
        var.get('defineMacro')(Js('\\Epsilon'), Js('\\mathrm{E}'))
        var.get('defineMacro')(Js('\\Eta'), Js('\\mathrm{H}'))
        var.get('defineMacro')(Js('\\exist'), Js('\\exists'))
        var.get('defineMacro')(Js('\\harr'), Js('\\leftrightarrow'))
        var.get('defineMacro')(Js('\\hArr'), Js('\\Leftrightarrow'))
        var.get('defineMacro')(Js('\\Harr'), Js('\\Leftrightarrow'))
        var.get('defineMacro')(Js('\\hearts'), Js('\\heartsuit'))
        var.get('defineMacro')(Js('\\image'), Js('\\Im'))
        var.get('defineMacro')(Js('\\infin'), Js('\\infty'))
        var.get('defineMacro')(Js('\\Iota'), Js('\\mathrm{I}'))
        var.get('defineMacro')(Js('\\isin'), Js('\\in'))
        var.get('defineMacro')(Js('\\Kappa'), Js('\\mathrm{K}'))
        var.get('defineMacro')(Js('\\larr'), Js('\\leftarrow'))
        var.get('defineMacro')(Js('\\lArr'), Js('\\Leftarrow'))
        var.get('defineMacro')(Js('\\Larr'), Js('\\Leftarrow'))
        var.get('defineMacro')(Js('\\lrarr'), Js('\\leftrightarrow'))
        var.get('defineMacro')(Js('\\lrArr'), Js('\\Leftrightarrow'))
        var.get('defineMacro')(Js('\\Lrarr'), Js('\\Leftrightarrow'))
        var.get('defineMacro')(Js('\\Mu'), Js('\\mathrm{M}'))
        var.get('defineMacro')(Js('\\natnums'), Js('\\mathbb{N}'))
        var.get('defineMacro')(Js('\\Nu'), Js('\\mathrm{N}'))
        var.get('defineMacro')(Js('\\Omicron'), Js('\\mathrm{O}'))
        var.get('defineMacro')(Js('\\plusmn'), Js('\\pm'))
        var.get('defineMacro')(Js('\\rarr'), Js('\\rightarrow'))
        var.get('defineMacro')(Js('\\rArr'), Js('\\Rightarrow'))
        var.get('defineMacro')(Js('\\Rarr'), Js('\\Rightarrow'))
        var.get('defineMacro')(Js('\\real'), Js('\\Re'))
        var.get('defineMacro')(Js('\\reals'), Js('\\mathbb{R}'))
        var.get('defineMacro')(Js('\\Reals'), Js('\\mathbb{R}'))
        var.get('defineMacro')(Js('\\Rho'), Js('\\mathrm{P}'))
        var.get('defineMacro')(Js('\\sdot'), Js('\\cdot'))
        var.get('defineMacro')(Js('\\sect'), Js('\\S'))
        var.get('defineMacro')(Js('\\spades'), Js('\\spadesuit'))
        var.get('defineMacro')(Js('\\sub'), Js('\\subset'))
        var.get('defineMacro')(Js('\\sube'), Js('\\subseteq'))
        var.get('defineMacro')(Js('\\supe'), Js('\\supseteq'))
        var.get('defineMacro')(Js('\\Tau'), Js('\\mathrm{T}'))
        var.get('defineMacro')(Js('\\thetasym'), Js('\\vartheta'))
        var.get('defineMacro')(Js('\\weierp'), Js('\\wp'))
        var.get('defineMacro')(Js('\\Zeta'), Js('\\mathrm{Z}'))
        var.get('defineMacro')(Js('\\argmin'), Js('\\DOTSB\\mathop{\\operatorname{arg\\,min}}\\limits'))
        var.get('defineMacro')(Js('\\argmax'), Js('\\DOTSB\\mathop{\\operatorname{arg\\,max}}\\limits'))
        var.get('defineMacro')(Js('\\blue'), Js('\\textcolor{##6495ed}{#1}'))
        var.get('defineMacro')(Js('\\orange'), Js('\\textcolor{##ffa500}{#1}'))
        var.get('defineMacro')(Js('\\pink'), Js('\\textcolor{##ff00af}{#1}'))
        var.get('defineMacro')(Js('\\red'), Js('\\textcolor{##df0030}{#1}'))
        var.get('defineMacro')(Js('\\green'), Js('\\textcolor{##28ae7b}{#1}'))
        var.get('defineMacro')(Js('\\gray'), Js('\\textcolor{gray}{##1}'))
        var.get('defineMacro')(Js('\\purple'), Js('\\textcolor{##9d38bd}{#1}'))
        var.get('defineMacro')(Js('\\blueA'), Js('\\textcolor{##ccfaff}{#1}'))
        var.get('defineMacro')(Js('\\blueB'), Js('\\textcolor{##80f6ff}{#1}'))
        var.get('defineMacro')(Js('\\blueC'), Js('\\textcolor{##63d9ea}{#1}'))
        var.get('defineMacro')(Js('\\blueD'), Js('\\textcolor{##11accd}{#1}'))
        var.get('defineMacro')(Js('\\blueE'), Js('\\textcolor{##0c7f99}{#1}'))
        var.get('defineMacro')(Js('\\tealA'), Js('\\textcolor{##94fff5}{#1}'))
        var.get('defineMacro')(Js('\\tealB'), Js('\\textcolor{##26edd5}{#1}'))
        var.get('defineMacro')(Js('\\tealC'), Js('\\textcolor{##01d1c1}{#1}'))
        var.get('defineMacro')(Js('\\tealD'), Js('\\textcolor{##01a995}{#1}'))
        var.get('defineMacro')(Js('\\tealE'), Js('\\textcolor{##208170}{#1}'))
        var.get('defineMacro')(Js('\\greenA'), Js('\\textcolor{##b6ffb0}{#1}'))
        var.get('defineMacro')(Js('\\greenB'), Js('\\textcolor{##8af281}{#1}'))
        var.get('defineMacro')(Js('\\greenC'), Js('\\textcolor{##74cf70}{#1}'))
        var.get('defineMacro')(Js('\\greenD'), Js('\\textcolor{##1fab54}{#1}'))
        var.get('defineMacro')(Js('\\greenE'), Js('\\textcolor{##0d923f}{#1}'))
        var.get('defineMacro')(Js('\\goldA'), Js('\\textcolor{##ffd0a9}{#1}'))
        var.get('defineMacro')(Js('\\goldB'), Js('\\textcolor{##ffbb71}{#1}'))
        var.get('defineMacro')(Js('\\goldC'), Js('\\textcolor{##ff9c39}{#1}'))
        var.get('defineMacro')(Js('\\goldD'), Js('\\textcolor{##e07d10}{#1}'))
        var.get('defineMacro')(Js('\\goldE'), Js('\\textcolor{##a75a05}{#1}'))
        var.get('defineMacro')(Js('\\redA'), Js('\\textcolor{##fca9a9}{#1}'))
        var.get('defineMacro')(Js('\\redB'), Js('\\textcolor{##ff8482}{#1}'))
        var.get('defineMacro')(Js('\\redC'), Js('\\textcolor{##f9685d}{#1}'))
        var.get('defineMacro')(Js('\\redD'), Js('\\textcolor{##e84d39}{#1}'))
        var.get('defineMacro')(Js('\\redE'), Js('\\textcolor{##bc2612}{#1}'))
        var.get('defineMacro')(Js('\\maroonA'), Js('\\textcolor{##ffbde0}{#1}'))
        var.get('defineMacro')(Js('\\maroonB'), Js('\\textcolor{##ff92c6}{#1}'))
        var.get('defineMacro')(Js('\\maroonC'), Js('\\textcolor{##ed5fa6}{#1}'))
        var.get('defineMacro')(Js('\\maroonD'), Js('\\textcolor{##ca337c}{#1}'))
        var.get('defineMacro')(Js('\\maroonE'), Js('\\textcolor{##9e034e}{#1}'))
        var.get('defineMacro')(Js('\\purpleA'), Js('\\textcolor{##ddd7ff}{#1}'))
        var.get('defineMacro')(Js('\\purpleB'), Js('\\textcolor{##c6b9fc}{#1}'))
        var.get('defineMacro')(Js('\\purpleC'), Js('\\textcolor{##aa87ff}{#1}'))
        var.get('defineMacro')(Js('\\purpleD'), Js('\\textcolor{##7854ab}{#1}'))
        var.get('defineMacro')(Js('\\purpleE'), Js('\\textcolor{##543b78}{#1}'))
        var.get('defineMacro')(Js('\\mintA'), Js('\\textcolor{##f5f9e8}{#1}'))
        var.get('defineMacro')(Js('\\mintB'), Js('\\textcolor{##edf2df}{#1}'))
        var.get('defineMacro')(Js('\\mintC'), Js('\\textcolor{##e0e5cc}{#1}'))
        var.get('defineMacro')(Js('\\grayA'), Js('\\textcolor{##f6f7f7}{#1}'))
        var.get('defineMacro')(Js('\\grayB'), Js('\\textcolor{##f0f1f2}{#1}'))
        var.get('defineMacro')(Js('\\grayC'), Js('\\textcolor{##e3e5e6}{#1}'))
        var.get('defineMacro')(Js('\\grayD'), Js('\\textcolor{##d6d8da}{#1}'))
        var.get('defineMacro')(Js('\\grayE'), Js('\\textcolor{##babec2}{#1}'))
        var.get('defineMacro')(Js('\\grayF'), Js('\\textcolor{##888d93}{#1}'))
        var.get('defineMacro')(Js('\\grayG'), Js('\\textcolor{##626569}{#1}'))
        var.get('defineMacro')(Js('\\grayH'), Js('\\textcolor{##3b3e40}{#1}'))
        var.get('defineMacro')(Js('\\grayI'), Js('\\textcolor{##21242c}{#1}'))
        var.get('defineMacro')(Js('\\kaBlue'), Js('\\textcolor{##314453}{#1}'))
        var.get('defineMacro')(Js('\\kaGreen'), Js('\\textcolor{##71B307}{#1}'))
        var.put('implicitCommands', Js({'\\relax':Js(True),'^':Js(True),'_':Js(True),'\\limits':Js(True),'\\nolimits':Js(True)}))
        @Js
        def PyJs_anonymous_371_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['_proto', 'MacroExpander'])
            @Js
            def PyJsHoisted_MacroExpander_(input, settings, mode, this, arguments, var=var):
                var = Scope({'input':input, 'settings':settings, 'mode':mode, 'this':this, 'arguments':arguments}, var)
                var.registers(['input', 'settings', 'mode'])
                var.get(u"this").put('settings', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('expansionCount', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('lexer', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('macros', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('stack', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('mode', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('settings', var.get('settings'))
                var.get(u"this").put('expansionCount', Js(0.0))
                var.get(u"this").callprop('feed', var.get('input'))
                var.get(u"this").put('macros', var.get('Namespace_Namespace').create(var.get('macros'), var.get('settings').get('macros')))
                var.get(u"this").put('mode', var.get('mode'))
                var.get(u"this").put('stack', Js([]))
            PyJsHoisted_MacroExpander_.func_name = 'MacroExpander'
            var.put('MacroExpander', PyJsHoisted_MacroExpander_)
            pass
            var.put('_proto', var.get('MacroExpander').get('prototype'))
            @Js
            def PyJs_feed_372_(input, this, arguments, var=var):
                var = Scope({'input':input, 'this':this, 'arguments':arguments, 'feed':PyJs_feed_372_}, var)
                var.registers(['input'])
                var.get(u"this").put('lexer', var.get('Lexer_Lexer').create(var.get('input'), var.get(u"this").get('settings')))
            PyJs_feed_372_._set_name('feed')
            var.get('_proto').put('feed', PyJs_feed_372_)
            @Js
            def PyJs_switchMode_373_(newMode, this, arguments, var=var):
                var = Scope({'newMode':newMode, 'this':this, 'arguments':arguments, 'switchMode':PyJs_switchMode_373_}, var)
                var.registers(['newMode'])
                var.get(u"this").put('mode', var.get('newMode'))
            PyJs_switchMode_373_._set_name('switchMode')
            var.get('_proto').put('switchMode', PyJs_switchMode_373_)
            @Js
            def PyJs_beginGroup_374_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'beginGroup':PyJs_beginGroup_374_}, var)
                var.registers([])
                var.get(u"this").get('macros').callprop('beginGroup')
            PyJs_beginGroup_374_._set_name('beginGroup')
            var.get('_proto').put('beginGroup', PyJs_beginGroup_374_)
            @Js
            def PyJs_endGroup_375_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'endGroup':PyJs_endGroup_375_}, var)
                var.registers([])
                var.get(u"this").get('macros').callprop('endGroup')
            PyJs_endGroup_375_._set_name('endGroup')
            var.get('_proto').put('endGroup', PyJs_endGroup_375_)
            @Js
            def PyJs_future_376_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'future':PyJs_future_376_}, var)
                var.registers([])
                if PyJsStrictEq(var.get(u"this").get('stack').get('length'),Js(0.0)):
                    var.get(u"this").callprop('pushToken', var.get(u"this").get('lexer').callprop('lex'))
                return var.get(u"this").get('stack').get((var.get(u"this").get('stack').get('length')-Js(1.0)))
            PyJs_future_376_._set_name('future')
            var.get('_proto').put('future', PyJs_future_376_)
            @Js
            def PyJs_popToken_377_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'popToken':PyJs_popToken_377_}, var)
                var.registers([])
                var.get(u"this").callprop('future')
                return var.get(u"this").get('stack').callprop('pop')
            PyJs_popToken_377_._set_name('popToken')
            var.get('_proto').put('popToken', PyJs_popToken_377_)
            @Js
            def PyJs_pushToken_378_(token, this, arguments, var=var):
                var = Scope({'token':token, 'this':this, 'arguments':arguments, 'pushToken':PyJs_pushToken_378_}, var)
                var.registers(['token'])
                var.get(u"this").get('stack').callprop('push', var.get('token'))
            PyJs_pushToken_378_._set_name('pushToken')
            var.get('_proto').put('pushToken', PyJs_pushToken_378_)
            @Js
            def PyJs_pushTokens_379_(tokens, this, arguments, var=var):
                var = Scope({'tokens':tokens, 'this':this, 'arguments':arguments, 'pushTokens':PyJs_pushTokens_379_}, var)
                var.registers(['tokens', '_this$stack'])
                pass
                var.put('_this$stack', var.get(u"this").get('stack')).get('push').callprop('apply', var.get('_this$stack'), var.get('tokens'))
            PyJs_pushTokens_379_._set_name('pushTokens')
            var.get('_proto').put('pushTokens', PyJs_pushTokens_379_)
            @Js
            def PyJs_consumeSpaces_380_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'consumeSpaces':PyJs_consumeSpaces_380_}, var)
                var.registers(['token'])
                #for JS loop
                
                while 1:
                    var.put('token', var.get(u"this").callprop('future'))
                    if PyJsStrictEq(var.get('token').get('text'),Js(' ')):
                        var.get(u"this").get('stack').callprop('pop')
                    else:
                        break
                
            PyJs_consumeSpaces_380_._set_name('consumeSpaces')
            var.get('_proto').put('consumeSpaces', PyJs_consumeSpaces_380_)
            @Js
            def PyJs_consumeArgs_381_(numArgs, this, arguments, var=var):
                var = Scope({'numArgs':numArgs, 'this':this, 'arguments':arguments, 'consumeArgs':PyJs_consumeArgs_381_}, var)
                var.registers(['i', 'depth', 'startOfArg', 'arg', 'args', 'numArgs', 'tok'])
                var.put('args', Js([]))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('numArgs')):
                    try:
                        var.get(u"this").callprop('consumeSpaces')
                        var.put('startOfArg', var.get(u"this").callprop('popToken'))
                        if PyJsStrictEq(var.get('startOfArg').get('text'),Js('{')):
                            var.put('arg', Js([]))
                            var.put('depth', Js(1.0))
                            while PyJsStrictNeq(var.get('depth'),Js(0.0)):
                                var.put('tok', var.get(u"this").callprop('popToken'))
                                var.get('arg').callprop('push', var.get('tok'))
                                if PyJsStrictEq(var.get('tok').get('text'),Js('{')):
                                    var.put('depth',Js(var.get('depth').to_number())+Js(1))
                                else:
                                    if PyJsStrictEq(var.get('tok').get('text'),Js('}')):
                                        var.put('depth',Js(var.get('depth').to_number())-Js(1))
                                    else:
                                        if PyJsStrictEq(var.get('tok').get('text'),Js('EOF')):
                                            PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('End of input in macro argument'), var.get('startOfArg')))
                                            raise PyJsTempException
                            var.get('arg').callprop('pop')
                            var.get('arg').callprop('reverse')
                            var.get('args').put(var.get('i'), var.get('arg'))
                        else:
                            if PyJsStrictEq(var.get('startOfArg').get('text'),Js('EOF')):
                                PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('End of input expecting macro argument')))
                                raise PyJsTempException
                            else:
                                var.get('args').put(var.get('i'), Js([var.get('startOfArg')]))
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
                return var.get('args')
            PyJs_consumeArgs_381_._set_name('consumeArgs')
            var.get('_proto').put('consumeArgs', PyJs_consumeArgs_381_)
            @Js
            def PyJs_expandOnce_382_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'expandOnce':PyJs_expandOnce_382_}, var)
                var.registers(['i', 'topToken', 'tokens', '_tokens', 'expansion', 'args', 'name', 'tok'])
                var.put('topToken', var.get(u"this").callprop('popToken'))
                var.put('name', var.get('topToken').get('text'))
                var.put('expansion', var.get(u"this").callprop('_getExpansion', var.get('name')))
                if (var.get('expansion')==var.get(u"null")):
                    var.get(u"this").callprop('pushToken', var.get('topToken'))
                    return var.get('topToken')
                (var.get(u"this").put('expansionCount',Js(var.get(u"this").get('expansionCount').to_number())+Js(1))-Js(1))
                if (var.get(u"this").get('expansionCount')>var.get(u"this").get('settings').get('maxExpand')):
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create((Js('Too many expansions: infinite loop or ')+Js('need to increase maxExpand setting'))))
                    raise PyJsTempException
                var.put('tokens', var.get('expansion').get('tokens'))
                if var.get('expansion').get('numArgs'):
                    var.put('args', var.get(u"this").callprop('consumeArgs', var.get('expansion').get('numArgs')))
                    var.put('tokens', var.get('tokens').callprop('slice'))
                    #for JS loop
                    var.put('i', (var.get('tokens').get('length')-Js(1.0)))
                    while (var.get('i')>=Js(0.0)):
                        try:
                            var.put('tok', var.get('tokens').get(var.get('i')))
                            if PyJsStrictEq(var.get('tok').get('text'),Js('#')):
                                if PyJsStrictEq(var.get('i'),Js(0.0)):
                                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('Incomplete placeholder at end of macro body'), var.get('tok')))
                                    raise PyJsTempException
                                var.put('tok', var.get('tokens').get(var.put('i',Js(var.get('i').to_number())-Js(1))))
                                if PyJsStrictEq(var.get('tok').get('text'),Js('#')):
                                    var.get('tokens').callprop('splice', (var.get('i')+Js(1.0)), Js(1.0))
                                else:
                                    if JsRegExp('/^[1-9]$/').callprop('test', var.get('tok').get('text')):
                                        pass
                                        var.put('_tokens', var.get('tokens')).get('splice').callprop('apply', var.get('_tokens'), Js([var.get('i'), Js(2.0)]).callprop('concat', var.get('args').get(((+var.get('tok').get('text'))-Js(1.0)))))
                                    else:
                                        PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('Not a valid argument number'), var.get('tok')))
                                        raise PyJsTempException
                        finally:
                                var.put('i',Js(var.get('i').to_number())-Js(1))
                var.get(u"this").callprop('pushTokens', var.get('tokens'))
                return var.get('tokens')
            PyJs_expandOnce_382_._set_name('expandOnce')
            var.get('_proto').put('expandOnce', PyJs_expandOnce_382_)
            @Js
            def PyJs_expandAfterFuture_383_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'expandAfterFuture':PyJs_expandAfterFuture_383_}, var)
                var.registers([])
                var.get(u"this").callprop('expandOnce')
                return var.get(u"this").callprop('future')
            PyJs_expandAfterFuture_383_._set_name('expandAfterFuture')
            var.get('_proto').put('expandAfterFuture', PyJs_expandAfterFuture_383_)
            @Js
            def PyJs_expandNextToken_384_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'expandNextToken':PyJs_expandNextToken_384_}, var)
                var.registers(['expanded'])
                #for JS loop
                
                while 1:
                    var.put('expanded', var.get(u"this").callprop('expandOnce'))
                    if var.get('expanded').instanceof(var.get('Token_Token')):
                        if PyJsStrictEq(var.get('expanded').get('text'),Js('\\relax')):
                            var.get(u"this").get('stack').callprop('pop')
                        else:
                            return var.get(u"this").get('stack').callprop('pop')
                
                PyJsTempException = JsToPyException(var.get('Error').create())
                raise PyJsTempException
            PyJs_expandNextToken_384_._set_name('expandNextToken')
            var.get('_proto').put('expandNextToken', PyJs_expandNextToken_384_)
            @Js
            def PyJs_expandMacro_385_(name, this, arguments, var=var):
                var = Scope({'name':name, 'this':this, 'arguments':arguments, 'expandMacro':PyJs_expandMacro_385_}, var)
                var.registers(['expanded', 'oldStackLength', 'output', 'name'])
                if var.get(u"this").get('macros').callprop('get', var.get('name')).neg():
                    return var.get('undefined')
                var.put('output', Js([]))
                var.put('oldStackLength', var.get(u"this").get('stack').get('length'))
                var.get(u"this").callprop('pushToken', var.get('Token_Token').create(var.get('name')))
                while (var.get(u"this").get('stack').get('length')>var.get('oldStackLength')):
                    var.put('expanded', var.get(u"this").callprop('expandOnce'))
                    if var.get('expanded').instanceof(var.get('Token_Token')):
                        var.get('output').callprop('push', var.get(u"this").get('stack').callprop('pop'))
                return var.get('output')
            PyJs_expandMacro_385_._set_name('expandMacro')
            var.get('_proto').put('expandMacro', PyJs_expandMacro_385_)
            @Js
            def PyJs_expandMacroAsText_386_(name, this, arguments, var=var):
                var = Scope({'name':name, 'this':this, 'arguments':arguments, 'expandMacroAsText':PyJs_expandMacroAsText_386_}, var)
                var.registers(['tokens', 'name'])
                var.put('tokens', var.get(u"this").callprop('expandMacro', var.get('name')))
                if var.get('tokens'):
                    @Js
                    def PyJs_anonymous_387_(token, this, arguments, var=var):
                        var = Scope({'token':token, 'this':this, 'arguments':arguments}, var)
                        var.registers(['token'])
                        return var.get('token').get('text')
                    PyJs_anonymous_387_._set_name('anonymous')
                    return var.get('tokens').callprop('map', PyJs_anonymous_387_).callprop('join', Js(''))
                else:
                    return var.get('tokens')
            PyJs_expandMacroAsText_386_._set_name('expandMacroAsText')
            var.get('_proto').put('expandMacroAsText', PyJs_expandMacroAsText_386_)
            @Js
            def PyJs__getExpansion_388_(name, this, arguments, var=var):
                var = Scope({'name':name, 'this':this, 'arguments':arguments, '_getExpansion':PyJs__getExpansion_388_}, var)
                var.registers(['expanded', 'bodyLexer', 'tokens', 'definition', 'expansion', 'name', 'numArgs', 'stripped', 'tok'])
                var.put('definition', var.get(u"this").get('macros').callprop('get', var.get('name')))
                if (var.get('definition')==var.get(u"null")):
                    return var.get('definition')
                var.put('expansion', (var.get('definition')(var.get(u"this")) if PyJsStrictEq(var.get('definition',throw=False).typeof(),Js('function')) else var.get('definition')))
                if PyJsStrictEq(var.get('expansion',throw=False).typeof(),Js('string')):
                    var.put('numArgs', Js(0.0))
                    if PyJsStrictNeq(var.get('expansion').callprop('indexOf', Js('#')),(-Js(1.0))):
                        var.put('stripped', var.get('expansion').callprop('replace', JsRegExp('/##/g'), Js('')))
                        while PyJsStrictNeq(var.get('stripped').callprop('indexOf', (Js('#')+(var.get('numArgs')+Js(1.0)))),(-Js(1.0))):
                            var.put('numArgs',Js(var.get('numArgs').to_number())+Js(1))
                    var.put('bodyLexer', var.get('Lexer_Lexer').create(var.get('expansion'), var.get(u"this").get('settings')))
                    var.put('tokens', Js([]))
                    var.put('tok', var.get('bodyLexer').callprop('lex'))
                    while PyJsStrictNeq(var.get('tok').get('text'),Js('EOF')):
                        var.get('tokens').callprop('push', var.get('tok'))
                        var.put('tok', var.get('bodyLexer').callprop('lex'))
                    var.get('tokens').callprop('reverse')
                    var.put('expanded', Js({'tokens':var.get('tokens'),'numArgs':var.get('numArgs')}))
                    return var.get('expanded')
                return var.get('expansion')
            PyJs__getExpansion_388_._set_name('_getExpansion')
            var.get('_proto').put('_getExpansion', PyJs__getExpansion_388_)
            @Js
            def PyJs_isDefined_389_(name, this, arguments, var=var):
                var = Scope({'name':name, 'this':this, 'arguments':arguments, 'isDefined':PyJs_isDefined_389_}, var)
                var.registers(['name'])
                return ((((var.get(u"this").get('macros').callprop('has', var.get('name')) or var.get('src_functions').callprop('hasOwnProperty', var.get('name'))) or var.get('src_symbols').get('math').callprop('hasOwnProperty', var.get('name'))) or var.get('src_symbols').get('text').callprop('hasOwnProperty', var.get('name'))) or var.get('implicitCommands').callprop('hasOwnProperty', var.get('name')))
            PyJs_isDefined_389_._set_name('isDefined')
            var.get('_proto').put('isDefined', PyJs_isDefined_389_)
            return var.get('MacroExpander')
        PyJs_anonymous_371_._set_name('anonymous')
        var.put('MacroExpander_MacroExpander', PyJs_anonymous_371_())
        var.put('unicodeAccents', Js({'́':Js({'text':Js("\\'"),'math':Js('\\acute')}),'̀':Js({'text':Js('\\`'),'math':Js('\\grave')}),'̈':Js({'text':Js('\\"'),'math':Js('\\ddot')}),'̃':Js({'text':Js('\\~'),'math':Js('\\tilde')}),'̄':Js({'text':Js('\\='),'math':Js('\\bar')}),'̆':Js({'text':Js('\\u'),'math':Js('\\breve')}),'̌':Js({'text':Js('\\v'),'math':Js('\\check')}),'̂':Js({'text':Js('\\^'),'math':Js('\\hat')}),'̇':Js({'text':Js('\\.'),'math':Js('\\dot')}),'̊':Js({'text':Js('\\r'),'math':Js('\\mathring')}),'̋':Js({'text':Js('\\H')})}))
        var.put('unicodeSymbols', Js({'á':Js('á'),'à':Js('à'),'ä':Js('ä'),'ǟ':Js('ǟ'),'ã':Js('ã'),'ā':Js('ā'),'ă':Js('ă'),'ắ':Js('ắ'),'ằ':Js('ằ'),'ẵ':Js('ẵ'),'ǎ':Js('ǎ'),'â':Js('â'),'ấ':Js('ấ'),'ầ':Js('ầ'),'ẫ':Js('ẫ'),'ȧ':Js('ȧ'),'ǡ':Js('ǡ'),'å':Js('å'),'ǻ':Js('ǻ'),'ḃ':Js('ḃ'),'ć':Js('ć'),'č':Js('č'),'ĉ':Js('ĉ'),'ċ':Js('ċ'),'ď':Js('ď'),'ḋ':Js('ḋ'),'é':Js('é'),'è':Js('è'),'ë':Js('ë'),'ẽ':Js('ẽ'),'ē':Js('ē'),'ḗ':Js('ḗ'),'ḕ':Js('ḕ'),'ĕ':Js('ĕ'),'ě':Js('ě'),'ê':Js('ê'),'ế':Js('ế'),'ề':Js('ề'),'ễ':Js('ễ'),'ė':Js('ė'),'ḟ':Js('ḟ'),'ǵ':Js('ǵ'),'ḡ':Js('ḡ'),'ğ':Js('ğ'),'ǧ':Js('ǧ'),'ĝ':Js('ĝ'),'ġ':Js('ġ'),'ḧ':Js('ḧ'),'ȟ':Js('ȟ'),'ĥ':Js('ĥ'),'ḣ':Js('ḣ'),'í':Js('í'),'ì':Js('ì'),'ï':Js('ï'),'ḯ':Js('ḯ'),'ĩ':Js('ĩ'),'ī':Js('ī'),'ĭ':Js('ĭ'),'ǐ':Js('ǐ'),'î':Js('î'),'ǰ':Js('ǰ'),'ĵ':Js('ĵ'),'ḱ':Js('ḱ'),'ǩ':Js('ǩ'),'ĺ':Js('ĺ'),'ľ':Js('ľ'),'ḿ':Js('ḿ'),'ṁ':Js('ṁ'),'ń':Js('ń'),'ǹ':Js('ǹ'),'ñ':Js('ñ'),'ň':Js('ň'),'ṅ':Js('ṅ'),'ó':Js('ó'),'ò':Js('ò'),'ö':Js('ö'),'ȫ':Js('ȫ'),'õ':Js('õ'),'ṍ':Js('ṍ'),'ṏ':Js('ṏ'),'ȭ':Js('ȭ'),'ō':Js('ō'),'ṓ':Js('ṓ'),'ṑ':Js('ṑ'),'ŏ':Js('ŏ'),'ǒ':Js('ǒ'),'ô':Js('ô'),'ố':Js('ố'),'ồ':Js('ồ'),'ỗ':Js('ỗ'),'ȯ':Js('ȯ'),'ȱ':Js('ȱ'),'ő':Js('ő'),'ṕ':Js('ṕ'),'ṗ':Js('ṗ'),'ŕ':Js('ŕ'),'ř':Js('ř'),'ṙ':Js('ṙ'),'ś':Js('ś'),'ṥ':Js('ṥ'),'š':Js('š'),'ṧ':Js('ṧ'),'ŝ':Js('ŝ'),'ṡ':Js('ṡ'),'ẗ':Js('ẗ'),'ť':Js('ť'),'ṫ':Js('ṫ'),'ú':Js('ú'),'ù':Js('ù'),'ü':Js('ü'),'ǘ':Js('ǘ'),'ǜ':Js('ǜ'),'ǖ':Js('ǖ'),'ǚ':Js('ǚ'),'ũ':Js('ũ'),'ṹ':Js('ṹ'),'ū':Js('ū'),'ṻ':Js('ṻ'),'ŭ':Js('ŭ'),'ǔ':Js('ǔ'),'û':Js('û'),'ů':Js('ů'),'ű':Js('ű'),'ṽ':Js('ṽ'),'ẃ':Js('ẃ'),'ẁ':Js('ẁ'),'ẅ':Js('ẅ'),'ŵ':Js('ŵ'),'ẇ':Js('ẇ'),'ẘ':Js('ẘ'),'ẍ':Js('ẍ'),'ẋ':Js('ẋ'),'ý':Js('ý'),'ỳ':Js('ỳ'),'ÿ':Js('ÿ'),'ỹ':Js('ỹ'),'ȳ':Js('ȳ'),'ŷ':Js('ŷ'),'ẏ':Js('ẏ'),'ẙ':Js('ẙ'),'ź':Js('ź'),'ž':Js('ž'),'ẑ':Js('ẑ'),'ż':Js('ż'),'Á':Js('Á'),'À':Js('À'),'Ä':Js('Ä'),'Ǟ':Js('Ǟ'),'Ã':Js('Ã'),'Ā':Js('Ā'),'Ă':Js('Ă'),'Ắ':Js('Ắ'),'Ằ':Js('Ằ'),'Ẵ':Js('Ẵ'),'Ǎ':Js('Ǎ'),'Â':Js('Â'),'Ấ':Js('Ấ'),'Ầ':Js('Ầ'),'Ẫ':Js('Ẫ'),'Ȧ':Js('Ȧ'),'Ǡ':Js('Ǡ'),'Å':Js('Å'),'Ǻ':Js('Ǻ'),'Ḃ':Js('Ḃ'),'Ć':Js('Ć'),'Č':Js('Č'),'Ĉ':Js('Ĉ'),'Ċ':Js('Ċ'),'Ď':Js('Ď'),'Ḋ':Js('Ḋ'),'É':Js('É'),'È':Js('È'),'Ë':Js('Ë'),'Ẽ':Js('Ẽ'),'Ē':Js('Ē'),'Ḗ':Js('Ḗ'),'Ḕ':Js('Ḕ'),'Ĕ':Js('Ĕ'),'Ě':Js('Ě'),'Ê':Js('Ê'),'Ế':Js('Ế'),'Ề':Js('Ề'),'Ễ':Js('Ễ'),'Ė':Js('Ė'),'Ḟ':Js('Ḟ'),'Ǵ':Js('Ǵ'),'Ḡ':Js('Ḡ'),'Ğ':Js('Ğ'),'Ǧ':Js('Ǧ'),'Ĝ':Js('Ĝ'),'Ġ':Js('Ġ'),'Ḧ':Js('Ḧ'),'Ȟ':Js('Ȟ'),'Ĥ':Js('Ĥ'),'Ḣ':Js('Ḣ'),'Í':Js('Í'),'Ì':Js('Ì'),'Ï':Js('Ï'),'Ḯ':Js('Ḯ'),'Ĩ':Js('Ĩ'),'Ī':Js('Ī'),'Ĭ':Js('Ĭ'),'Ǐ':Js('Ǐ'),'Î':Js('Î'),'İ':Js('İ'),'Ĵ':Js('Ĵ'),'Ḱ':Js('Ḱ'),'Ǩ':Js('Ǩ'),'Ĺ':Js('Ĺ'),'Ľ':Js('Ľ'),'Ḿ':Js('Ḿ'),'Ṁ':Js('Ṁ'),'Ń':Js('Ń'),'Ǹ':Js('Ǹ'),'Ñ':Js('Ñ'),'Ň':Js('Ň'),'Ṅ':Js('Ṅ'),'Ó':Js('Ó'),'Ò':Js('Ò'),'Ö':Js('Ö'),'Ȫ':Js('Ȫ'),'Õ':Js('Õ'),'Ṍ':Js('Ṍ'),'Ṏ':Js('Ṏ'),'Ȭ':Js('Ȭ'),'Ō':Js('Ō'),'Ṓ':Js('Ṓ'),'Ṑ':Js('Ṑ'),'Ŏ':Js('Ŏ'),'Ǒ':Js('Ǒ'),'Ô':Js('Ô'),'Ố':Js('Ố'),'Ồ':Js('Ồ'),'Ỗ':Js('Ỗ'),'Ȯ':Js('Ȯ'),'Ȱ':Js('Ȱ'),'Ő':Js('Ő'),'Ṕ':Js('Ṕ'),'Ṗ':Js('Ṗ'),'Ŕ':Js('Ŕ'),'Ř':Js('Ř'),'Ṙ':Js('Ṙ'),'Ś':Js('Ś'),'Ṥ':Js('Ṥ'),'Š':Js('Š'),'Ṧ':Js('Ṧ'),'Ŝ':Js('Ŝ'),'Ṡ':Js('Ṡ'),'Ť':Js('Ť'),'Ṫ':Js('Ṫ'),'Ú':Js('Ú'),'Ù':Js('Ù'),'Ü':Js('Ü'),'Ǘ':Js('Ǘ'),'Ǜ':Js('Ǜ'),'Ǖ':Js('Ǖ'),'Ǚ':Js('Ǚ'),'Ũ':Js('Ũ'),'Ṹ':Js('Ṹ'),'Ū':Js('Ū'),'Ṻ':Js('Ṻ'),'Ŭ':Js('Ŭ'),'Ǔ':Js('Ǔ'),'Û':Js('Û'),'Ů':Js('Ů'),'Ű':Js('Ű'),'Ṽ':Js('Ṽ'),'Ẃ':Js('Ẃ'),'Ẁ':Js('Ẁ'),'Ẅ':Js('Ẅ'),'Ŵ':Js('Ŵ'),'Ẇ':Js('Ẇ'),'Ẍ':Js('Ẍ'),'Ẋ':Js('Ẋ'),'Ý':Js('Ý'),'Ỳ':Js('Ỳ'),'Ÿ':Js('Ÿ'),'Ỹ':Js('Ỹ'),'Ȳ':Js('Ȳ'),'Ŷ':Js('Ŷ'),'Ẏ':Js('Ẏ'),'Ź':Js('Ź'),'Ž':Js('Ž'),'Ẑ':Js('Ẑ'),'Ż':Js('Ż'),'ά':Js('ά'),'ὰ':Js('ὰ'),'ᾱ':Js('ᾱ'),'ᾰ':Js('ᾰ'),'έ':Js('έ'),'ὲ':Js('ὲ'),'ή':Js('ή'),'ὴ':Js('ὴ'),'ί':Js('ί'),'ὶ':Js('ὶ'),'ϊ':Js('ϊ'),'ΐ':Js('ΐ'),'ῒ':Js('ῒ'),'ῑ':Js('ῑ'),'ῐ':Js('ῐ'),'ό':Js('ό'),'ὸ':Js('ὸ'),'ύ':Js('ύ'),'ὺ':Js('ὺ'),'ϋ':Js('ϋ'),'ΰ':Js('ΰ'),'ῢ':Js('ῢ'),'ῡ':Js('ῡ'),'ῠ':Js('ῠ'),'ώ':Js('ώ'),'ὼ':Js('ὼ'),'Ύ':Js('Ύ'),'Ὺ':Js('Ὺ'),'Ϋ':Js('Ϋ'),'Ῡ':Js('Ῡ'),'Ῠ':Js('Ῠ'),'Ώ':Js('Ώ'),'Ὼ':Js('Ὼ')}))
        @Js
        def PyJs_anonymous_390_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['Parser', '_proto'])
            @Js
            def PyJsHoisted_Parser_(input, settings, this, arguments, var=var):
                var = Scope({'input':input, 'settings':settings, 'this':this, 'arguments':arguments}, var)
                var.registers(['input', 'settings'])
                var.get(u"this").put('mode', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('gullet', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('settings', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('leftrightDepth', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('nextToken', PyJsComma(Js(0.0), Js(None)))
                var.get(u"this").put('mode', Js('math'))
                var.get(u"this").put('gullet', var.get('MacroExpander_MacroExpander').create(var.get('input'), var.get('settings'), var.get(u"this").get('mode')))
                var.get(u"this").put('settings', var.get('settings'))
                var.get(u"this").put('leftrightDepth', Js(0.0))
            PyJsHoisted_Parser_.func_name = 'Parser'
            var.put('Parser', PyJsHoisted_Parser_)
            pass
            var.put('_proto', var.get('Parser').get('prototype'))
            @Js
            def PyJs_expect_391_(text, consume, this, arguments, var=var):
                var = Scope({'text':text, 'consume':consume, 'this':this, 'arguments':arguments, 'expect':PyJs_expect_391_}, var)
                var.registers(['text', 'consume'])
                if PyJsStrictEq(var.get('consume'),PyJsComma(Js(0.0), Js(None))):
                    var.put('consume', Js(True))
                if PyJsStrictNeq(var.get(u"this").get('nextToken').get('text'),var.get('text')):
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(((((Js("Expected '")+var.get('text'))+Js("', got '"))+var.get(u"this").get('nextToken').get('text'))+Js("'")), var.get(u"this").get('nextToken')))
                    raise PyJsTempException
                if var.get('consume'):
                    var.get(u"this").callprop('consume')
            PyJs_expect_391_._set_name('expect')
            var.get('_proto').put('expect', PyJs_expect_391_)
            @Js
            def PyJs_consume_392_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'consume':PyJs_consume_392_}, var)
                var.registers([])
                var.get(u"this").put('nextToken', var.get(u"this").get('gullet').callprop('expandNextToken'))
            PyJs_consume_392_._set_name('consume')
            var.get('_proto').put('consume', PyJs_consume_392_)
            @Js
            def PyJs_switchMode_393_(newMode, this, arguments, var=var):
                var = Scope({'newMode':newMode, 'this':this, 'arguments':arguments, 'switchMode':PyJs_switchMode_393_}, var)
                var.registers(['newMode'])
                var.get(u"this").put('mode', var.get('newMode'))
                var.get(u"this").get('gullet').callprop('switchMode', var.get('newMode'))
            PyJs_switchMode_393_._set_name('switchMode')
            var.get('_proto').put('switchMode', PyJs_switchMode_393_)
            @Js
            def PyJs_parse_394_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'parse':PyJs_parse_394_}, var)
                var.registers(['parse'])
                var.get(u"this").get('gullet').callprop('beginGroup')
                if var.get(u"this").get('settings').get('colorIsTextColor'):
                    var.get(u"this").get('gullet').get('macros').callprop('set', Js('\\color'), Js('\\textcolor'))
                var.get(u"this").callprop('consume')
                var.put('parse', var.get(u"this").callprop('parseExpression', Js(False)))
                var.get(u"this").callprop('expect', Js('EOF'), Js(False))
                var.get(u"this").get('gullet').callprop('endGroup')
                return var.get('parse')
            PyJs_parse_394_._set_name('parse')
            var.get('_proto').put('parse', PyJs_parse_394_)
            @Js
            def PyJs_parseExpression_395_(breakOnInfix, breakOnTokenText, this, arguments, var=var):
                var = Scope({'breakOnInfix':breakOnInfix, 'breakOnTokenText':breakOnTokenText, 'this':this, 'arguments':arguments, 'parseExpression':PyJs_parseExpression_395_}, var)
                var.registers(['breakOnTokenText', 'breakOnInfix', 'atom', 'body', 'lex'])
                var.put('body', Js([]))
                while Js(True):
                    if PyJsStrictEq(var.get(u"this").get('mode'),Js('math')):
                        var.get(u"this").callprop('consumeSpaces')
                    var.put('lex', var.get(u"this").get('nextToken'))
                    if PyJsStrictNeq(var.get('Parser').get('endOfExpression').callprop('indexOf', var.get('lex').get('text')),(-Js(1.0))):
                        break
                    if (var.get('breakOnTokenText') and PyJsStrictEq(var.get('lex').get('text'),var.get('breakOnTokenText'))):
                        break
                    if ((var.get('breakOnInfix') and var.get('src_functions').get(var.get('lex').get('text'))) and var.get('src_functions').get(var.get('lex').get('text')).get('infix')):
                        break
                    var.put('atom', var.get(u"this").callprop('parseAtom', var.get('breakOnTokenText')))
                    if var.get('atom').neg():
                        break
                    var.get('body').callprop('push', var.get('atom'))
                if PyJsStrictEq(var.get(u"this").get('mode'),Js('text')):
                    var.get(u"this").callprop('formLigatures', var.get('body'))
                return var.get(u"this").callprop('handleInfixNodes', var.get('body'))
            PyJs_parseExpression_395_._set_name('parseExpression')
            var.get('_proto').put('parseExpression', PyJs_parseExpression_395_)
            @Js
            def PyJs_handleInfixNodes_396_(body, this, arguments, var=var):
                var = Scope({'body':body, 'this':this, 'arguments':arguments, 'handleInfixNodes':PyJs_handleInfixNodes_396_}, var)
                var.registers(['funcName', 'denomNode', 'i', 'numerBody', 'body', 'node', 'numerNode', 'overIndex', '_node', 'denomBody'])
                var.put('overIndex', (-Js(1.0)))
                pass
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('body').get('length')):
                    try:
                        var.put('node', var.get('checkNodeType')(var.get('body').get(var.get('i')), Js('infix')))
                        if var.get('node'):
                            if PyJsStrictNeq(var.get('overIndex'),(-Js(1.0))):
                                PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('only one infix operator per group'), var.get('node').get('token')))
                                raise PyJsTempException
                            var.put('overIndex', var.get('i'))
                            var.put('funcName', var.get('node').get('replaceWith'))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                if (PyJsStrictNeq(var.get('overIndex'),(-Js(1.0))) and var.get('funcName')):
                    pass
                    pass
                    var.put('numerBody', var.get('body').callprop('slice', Js(0.0), var.get('overIndex')))
                    var.put('denomBody', var.get('body').callprop('slice', (var.get('overIndex')+Js(1.0))))
                    if (PyJsStrictEq(var.get('numerBody').get('length'),Js(1.0)) and PyJsStrictEq(var.get('numerBody').get('0').get('type'),Js('ordgroup'))):
                        var.put('numerNode', var.get('numerBody').get('0'))
                    else:
                        var.put('numerNode', Js({'type':Js('ordgroup'),'mode':var.get(u"this").get('mode'),'body':var.get('numerBody')}))
                    if (PyJsStrictEq(var.get('denomBody').get('length'),Js(1.0)) and PyJsStrictEq(var.get('denomBody').get('0').get('type'),Js('ordgroup'))):
                        var.put('denomNode', var.get('denomBody').get('0'))
                    else:
                        var.put('denomNode', Js({'type':Js('ordgroup'),'mode':var.get(u"this").get('mode'),'body':var.get('denomBody')}))
                    pass
                    if PyJsStrictEq(var.get('funcName'),Js('\\\\abovefrac')):
                        var.put('_node', var.get(u"this").callprop('callFunction', var.get('funcName'), Js([var.get('numerNode'), var.get('body').get(var.get('overIndex')), var.get('denomNode')]), Js([])))
                    else:
                        var.put('_node', var.get(u"this").callprop('callFunction', var.get('funcName'), Js([var.get('numerNode'), var.get('denomNode')]), Js([])))
                    return Js([var.get('_node')])
                else:
                    return var.get('body')
            PyJs_handleInfixNodes_396_._set_name('handleInfixNodes')
            var.get('_proto').put('handleInfixNodes', PyJs_handleInfixNodes_396_)
            @Js
            def PyJs_handleSupSubscript_397_(name, this, arguments, var=var):
                var = Scope({'name':name, 'this':this, 'arguments':arguments, 'handleSupSubscript':PyJs_handleSupSubscript_397_}, var)
                var.registers(['group', 'symbolToken', 'symbol', 'name'])
                var.put('symbolToken', var.get(u"this").get('nextToken'))
                var.put('symbol', var.get('symbolToken').get('text'))
                var.get(u"this").callprop('consume')
                var.get(u"this").callprop('consumeSpaces')
                var.put('group', var.get(u"this").callprop('parseGroup', var.get('name'), Js(False), var.get('Parser').get('SUPSUB_GREEDINESS')))
                if var.get('group').neg():
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js("Expected group after '")+var.get('symbol'))+Js("'")), var.get('symbolToken')))
                    raise PyJsTempException
                return var.get('group')
            PyJs_handleSupSubscript_397_._set_name('handleSupSubscript')
            var.get('_proto').put('handleSupSubscript', PyJs_handleSupSubscript_397_)
            @Js
            def PyJs_handleUnsupportedCmd_398_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'handleUnsupportedCmd':PyJs_handleUnsupportedCmd_398_}, var)
                var.registers(['i', 'text', 'textordArray', 'textNode', 'colorNode'])
                var.put('text', var.get(u"this").get('nextToken').get('text'))
                var.put('textordArray', Js([]))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('text').get('length')):
                    try:
                        var.get('textordArray').callprop('push', Js({'type':Js('textord'),'mode':Js('text'),'text':var.get('text').get(var.get('i'))}))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                var.put('textNode', Js({'type':Js('text'),'mode':var.get(u"this").get('mode'),'body':var.get('textordArray')}))
                var.put('colorNode', Js({'type':Js('color'),'mode':var.get(u"this").get('mode'),'color':var.get(u"this").get('settings').get('errorColor'),'body':Js([var.get('textNode')])}))
                var.get(u"this").callprop('consume')
                return var.get('colorNode')
            PyJs_handleUnsupportedCmd_398_._set_name('handleUnsupportedCmd')
            var.get('_proto').put('handleUnsupportedCmd', PyJs_handleUnsupportedCmd_398_)
            @Js
            def PyJs_parseAtom_399_(breakOnTokenText, this, arguments, var=var):
                var = Scope({'breakOnTokenText':breakOnTokenText, 'this':this, 'arguments':arguments, 'parseAtom':PyJs_parseAtom_399_}, var)
                var.registers(['primes', 'breakOnTokenText', 'opNode', 'lex', 'superscript', 'prime', 'base', 'subscript', 'limits'])
                var.put('base', var.get(u"this").callprop('parseGroup', Js('atom'), Js(False), var.get(u"null"), var.get('breakOnTokenText')))
                if PyJsStrictEq(var.get(u"this").get('mode'),Js('text')):
                    return var.get('base')
                pass
                pass
                while Js(True):
                    var.get(u"this").callprop('consumeSpaces')
                    var.put('lex', var.get(u"this").get('nextToken'))
                    if (PyJsStrictEq(var.get('lex').get('text'),Js('\\limits')) or PyJsStrictEq(var.get('lex').get('text'),Js('\\nolimits'))):
                        var.put('opNode', var.get('checkNodeType')(var.get('base'), Js('op')))
                        if var.get('opNode'):
                            var.put('limits', PyJsStrictEq(var.get('lex').get('text'),Js('\\limits')))
                            var.get('opNode').put('limits', var.get('limits'))
                            var.get('opNode').put('alwaysHandleSupSub', Js(True))
                        else:
                            PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('Limit controls must follow a math operator'), var.get('lex')))
                            raise PyJsTempException
                        var.get(u"this").callprop('consume')
                    else:
                        if PyJsStrictEq(var.get('lex').get('text'),Js('^')):
                            if var.get('superscript'):
                                PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('Double superscript'), var.get('lex')))
                                raise PyJsTempException
                            var.put('superscript', var.get(u"this").callprop('handleSupSubscript', Js('superscript')))
                        else:
                            if PyJsStrictEq(var.get('lex').get('text'),Js('_')):
                                if var.get('subscript'):
                                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('Double subscript'), var.get('lex')))
                                    raise PyJsTempException
                                var.put('subscript', var.get(u"this").callprop('handleSupSubscript', Js('subscript')))
                            else:
                                if PyJsStrictEq(var.get('lex').get('text'),Js("'")):
                                    if var.get('superscript'):
                                        PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('Double superscript'), var.get('lex')))
                                        raise PyJsTempException
                                    var.put('prime', Js({'type':Js('textord'),'mode':var.get(u"this").get('mode'),'text':Js('\\prime')}))
                                    var.put('primes', Js([var.get('prime')]))
                                    var.get(u"this").callprop('consume')
                                    while PyJsStrictEq(var.get(u"this").get('nextToken').get('text'),Js("'")):
                                        var.get('primes').callprop('push', var.get('prime'))
                                        var.get(u"this").callprop('consume')
                                    if PyJsStrictEq(var.get(u"this").get('nextToken').get('text'),Js('^')):
                                        var.get('primes').callprop('push', var.get(u"this").callprop('handleSupSubscript', Js('superscript')))
                                    var.put('superscript', Js({'type':Js('ordgroup'),'mode':var.get(u"this").get('mode'),'body':var.get('primes')}))
                                else:
                                    break
                if (var.get('superscript') or var.get('subscript')):
                    return Js({'type':Js('supsub'),'mode':var.get(u"this").get('mode'),'base':var.get('base'),'sup':var.get('superscript'),'sub':var.get('subscript')})
                else:
                    return var.get('base')
            PyJs_parseAtom_399_._set_name('parseAtom')
            var.get('_proto').put('parseAtom', PyJs_parseAtom_399_)
            @Js
            def PyJs_parseFunction_400_(breakOnTokenText, name, greediness, this, arguments, var=var):
                var = Scope({'breakOnTokenText':breakOnTokenText, 'name':name, 'greediness':greediness, 'this':this, 'arguments':arguments, 'parseFunction':PyJs_parseFunction_400_}, var)
                var.registers(['greediness', 'oldMode', 'breakOnTokenText', 'func', '_this$parseArguments', 'optArgs', 'token', 'args', 'name', 'funcData'])
                var.put('token', var.get(u"this").get('nextToken'))
                var.put('func', var.get('token').get('text'))
                var.put('funcData', var.get('src_functions').get(var.get('func')))
                if var.get('funcData').neg():
                    return var.get(u"null")
                if ((var.get('greediness')!=var.get(u"null")) and (var.get('funcData').get('greediness')<=var.get('greediness'))):
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create((((Js("Got function '")+var.get('func'))+Js("' with no arguments"))+((Js(' as ')+var.get('name')) if var.get('name') else Js(''))), var.get('token')))
                    raise PyJsTempException
                else:
                    if (PyJsStrictEq(var.get(u"this").get('mode'),Js('text')) and var.get('funcData').get('allowedInText').neg()):
                        PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js("Can't use function '")+var.get('func'))+Js("' in text mode")), var.get('token')))
                        raise PyJsTempException
                    else:
                        if (PyJsStrictEq(var.get(u"this").get('mode'),Js('math')) and PyJsStrictEq(var.get('funcData').get('allowedInMath'),Js(False))):
                            PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js("Can't use function '")+var.get('func'))+Js("' in math mode")), var.get('token')))
                            raise PyJsTempException
                if (var.get('funcData').get('argTypes') and PyJsStrictEq(var.get('funcData').get('argTypes').get('0'),Js('url'))):
                    var.get(u"this").get('gullet').get('lexer').callprop('setCatcode', Js('%'), Js(13.0))
                if var.get('funcData').get('consumeMode'):
                    var.put('oldMode', var.get(u"this").get('mode'))
                    var.get(u"this").callprop('switchMode', var.get('funcData').get('consumeMode'))
                    var.get(u"this").callprop('consume')
                    var.get(u"this").callprop('switchMode', var.get('oldMode'))
                else:
                    var.get(u"this").callprop('consume')
                var.put('_this$parseArguments', var.get(u"this").callprop('parseArguments', var.get('func'), var.get('funcData')))
                var.put('args', var.get('_this$parseArguments').get('args'))
                var.put('optArgs', var.get('_this$parseArguments').get('optArgs'))
                return var.get(u"this").callprop('callFunction', var.get('func'), var.get('args'), var.get('optArgs'), var.get('token'), var.get('breakOnTokenText'))
            PyJs_parseFunction_400_._set_name('parseFunction')
            var.get('_proto').put('parseFunction', PyJs_parseFunction_400_)
            @Js
            def PyJs_callFunction_401_(name, args, optArgs, token, breakOnTokenText, this, arguments, var=var):
                var = Scope({'name':name, 'args':args, 'optArgs':optArgs, 'token':token, 'breakOnTokenText':breakOnTokenText, 'this':this, 'arguments':arguments, 'callFunction':PyJs_callFunction_401_}, var)
                var.registers(['breakOnTokenText', 'func', 'context', 'optArgs', 'args', 'name', 'token'])
                var.put('context', Js({'funcName':var.get('name'),'parser':var.get(u"this"),'token':var.get('token'),'breakOnTokenText':var.get('breakOnTokenText')}))
                var.put('func', var.get('src_functions').get(var.get('name')))
                if (var.get('func') and var.get('func').get('handler')):
                    return var.get('func').callprop('handler', var.get('context'), var.get('args'), var.get('optArgs'))
                else:
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create((Js('No function handler for ')+var.get('name'))))
                    raise PyJsTempException
            PyJs_callFunction_401_._set_name('callFunction')
            var.get('_proto').put('callFunction', PyJs_callFunction_401_)
            @Js
            def PyJs_parseArguments_402_(func, funcData, this, arguments, var=var):
                var = Scope({'func':func, 'funcData':funcData, 'this':this, 'arguments':arguments, 'parseArguments':PyJs_parseArguments_402_}, var)
                var.registers(['i', 'argType', 'func', 'totalArgs', 'arg', 'optArgs', 'args', 'nextToken', 'baseGreediness', 'funcData', 'isOptional'])
                var.put('totalArgs', (var.get('funcData').get('numArgs')+var.get('funcData').get('numOptionalArgs')))
                if PyJsStrictEq(var.get('totalArgs'),Js(0.0)):
                    return Js({'args':Js([]),'optArgs':Js([])})
                var.put('baseGreediness', var.get('funcData').get('greediness'))
                var.put('args', Js([]))
                var.put('optArgs', Js([]))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('totalArgs')):
                    try:
                        var.put('argType', (var.get('funcData').get('argTypes') and var.get('funcData').get('argTypes').get(var.get('i'))))
                        var.put('isOptional', (var.get('i')<var.get('funcData').get('numOptionalArgs')))
                        if ((var.get('i')>Js(0.0)) and var.get('isOptional').neg()):
                            var.get(u"this").callprop('consumeSpaces')
                        if ((PyJsStrictEq(var.get('i'),Js(0.0)) and var.get('isOptional').neg()) and PyJsStrictEq(var.get(u"this").get('mode'),Js('math'))):
                            var.get(u"this").callprop('consumeSpaces')
                        var.put('nextToken', var.get(u"this").get('nextToken'))
                        var.put('arg', var.get(u"this").callprop('parseGroupOfType', ((Js("argument to '")+var.get('func'))+Js("'")), var.get('argType'), var.get('isOptional'), var.get('baseGreediness')))
                        if var.get('arg').neg():
                            if var.get('isOptional'):
                                var.get('optArgs').callprop('push', var.get(u"null"))
                                continue
                            PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js("Expected group after '")+var.get('func'))+Js("'")), var.get('nextToken')))
                            raise PyJsTempException
                        (var.get('optArgs') if var.get('isOptional') else var.get('args')).callprop('push', var.get('arg'))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                return Js({'args':var.get('args'),'optArgs':var.get('optArgs')})
            PyJs_parseArguments_402_._set_name('parseArguments')
            var.get('_proto').put('parseArguments', PyJs_parseArguments_402_)
            @Js
            def PyJs_parseGroupOfType_403_(name, type, optional, greediness, this, arguments, var=var):
                var = Scope({'name':name, 'type':type, 'optional':optional, 'greediness':greediness, 'this':this, 'arguments':arguments, 'parseGroupOfType':PyJs_parseGroupOfType_403_}, var)
                var.registers(['greediness', 'type', 'optional', 'name', 'token'])
                while 1:
                    SWITCHED = False
                    CONDITION = (var.get('type'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('color')):
                        SWITCHED = True
                        return var.get(u"this").callprop('parseColorGroup', var.get('optional'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('size')):
                        SWITCHED = True
                        return var.get(u"this").callprop('parseSizeGroup', var.get('optional'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('url')):
                        SWITCHED = True
                        return var.get(u"this").callprop('parseUrlGroup', var.get('optional'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('math')):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('text')):
                        SWITCHED = True
                        return var.get(u"this").callprop('parseGroup', var.get('name'), var.get('optional'), var.get('greediness'), var.get('undefined'), var.get('type'))
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('raw')):
                        SWITCHED = True
                        if (var.get('optional') and PyJsStrictEq(var.get(u"this").get('nextToken').get('text'),Js('{'))):
                            return var.get(u"null")
                        var.put('token', var.get(u"this").callprop('parseStringGroup', Js('raw'), var.get('optional'), Js(True)))
                        if var.get('token'):
                            return Js({'type':Js('raw'),'mode':Js('text'),'string':var.get('token').get('text')})
                        else:
                            PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('Expected raw group'), var.get(u"this").get('nextToken')))
                            raise PyJsTempException
                    if SWITCHED or PyJsStrictEq(CONDITION, Js('original')):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, var.get(u"null")):
                        SWITCHED = True
                        pass
                    if SWITCHED or PyJsStrictEq(CONDITION, var.get('undefined')):
                        SWITCHED = True
                        return var.get(u"this").callprop('parseGroup', var.get('name'), var.get('optional'), var.get('greediness'))
                    if True:
                        SWITCHED = True
                        PyJsTempException = JsToPyException(var.get('src_ParseError').create((Js('Unknown group type as ')+var.get('name')), var.get(u"this").get('nextToken')))
                        raise PyJsTempException
                    SWITCHED = True
                    break
            PyJs_parseGroupOfType_403_._set_name('parseGroupOfType')
            var.get('_proto').put('parseGroupOfType', PyJs_parseGroupOfType_403_)
            @Js
            def PyJs_consumeSpaces_404_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'consumeSpaces':PyJs_consumeSpaces_404_}, var)
                var.registers([])
                while PyJsStrictEq(var.get(u"this").get('nextToken').get('text'),Js(' ')):
                    var.get(u"this").callprop('consume')
            PyJs_consumeSpaces_404_._set_name('consumeSpaces')
            var.get('_proto').put('consumeSpaces', PyJs_consumeSpaces_404_)
            @Js
            def PyJs_parseStringGroup_405_(modeName, optional, raw, this, arguments, var=var):
                var = Scope({'modeName':modeName, 'optional':optional, 'raw':raw, 'this':this, 'arguments':arguments, 'parseStringGroup':PyJs_parseStringGroup_405_}, var)
                var.registers(['groupEnd', 'optional', 'nested', 'modeName', 'outerMode', 'str', 'firstToken', 'lastToken', 'nextToken', 'raw', 'groupBegin'])
                var.put('groupBegin', (Js('[') if var.get('optional') else Js('{')))
                var.put('groupEnd', (Js(']') if var.get('optional') else Js('}')))
                var.put('nextToken', var.get(u"this").get('nextToken'))
                if PyJsStrictNeq(var.get('nextToken').get('text'),var.get('groupBegin')):
                    if var.get('optional'):
                        return var.get(u"null")
                    else:
                        if ((var.get('raw') and PyJsStrictNeq(var.get('nextToken').get('text'),Js('EOF'))) and JsRegExp('/[^{}[\\]]/').callprop('test', var.get('nextToken').get('text'))):
                            var.get(u"this").get('gullet').get('lexer').callprop('setCatcode', Js('%'), Js(14.0))
                            var.get(u"this").callprop('consume')
                            return var.get('nextToken')
                var.put('outerMode', var.get(u"this").get('mode'))
                var.get(u"this").put('mode', Js('text'))
                var.get(u"this").callprop('expect', var.get('groupBegin'))
                var.put('str', Js(''))
                var.put('firstToken', var.get(u"this").get('nextToken'))
                var.put('nested', Js(0.0))
                var.put('lastToken', var.get('firstToken'))
                while ((var.get('raw') and (var.get('nested')>Js(0.0))) or PyJsStrictNeq(var.get(u"this").get('nextToken').get('text'),var.get('groupEnd'))):
                    while 1:
                        SWITCHED = False
                        CONDITION = (var.get(u"this").get('nextToken').get('text'))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('EOF')):
                            SWITCHED = True
                            PyJsTempException = JsToPyException(var.get('src_ParseError').create((Js('Unexpected end of input in ')+var.get('modeName')), var.get('firstToken').callprop('range', var.get('lastToken'), var.get('str'))))
                            raise PyJsTempException
                        if SWITCHED or PyJsStrictEq(CONDITION, var.get('groupBegin')):
                            SWITCHED = True
                            (var.put('nested',Js(var.get('nested').to_number())+Js(1))-Js(1))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, var.get('groupEnd')):
                            SWITCHED = True
                            (var.put('nested',Js(var.get('nested').to_number())-Js(1))+Js(1))
                            break
                        SWITCHED = True
                        break
                    var.put('lastToken', var.get(u"this").get('nextToken'))
                    var.put('str', var.get('lastToken').get('text'), '+')
                    var.get(u"this").callprop('consume')
                var.get(u"this").put('mode', var.get('outerMode'))
                var.get(u"this").get('gullet').get('lexer').callprop('setCatcode', Js('%'), Js(14.0))
                var.get(u"this").callprop('expect', var.get('groupEnd'))
                return var.get('firstToken').callprop('range', var.get('lastToken'), var.get('str'))
            PyJs_parseStringGroup_405_._set_name('parseStringGroup')
            var.get('_proto').put('parseStringGroup', PyJs_parseStringGroup_405_)
            @Js
            def PyJs_parseRegexGroup_406_(regex, modeName, this, arguments, var=var):
                var = Scope({'regex':regex, 'modeName':modeName, 'this':this, 'arguments':arguments, 'parseRegexGroup':PyJs_parseRegexGroup_406_}, var)
                var.registers(['regex', 'modeName', 'outerMode', 'str', 'firstToken', 'lastToken'])
                var.put('outerMode', var.get(u"this").get('mode'))
                var.get(u"this").put('mode', Js('text'))
                var.put('firstToken', var.get(u"this").get('nextToken'))
                var.put('lastToken', var.get('firstToken'))
                var.put('str', Js(''))
                while (PyJsStrictNeq(var.get(u"this").get('nextToken').get('text'),Js('EOF')) and var.get('regex').callprop('test', (var.get('str')+var.get(u"this").get('nextToken').get('text')))):
                    var.put('lastToken', var.get(u"this").get('nextToken'))
                    var.put('str', var.get('lastToken').get('text'), '+')
                    var.get(u"this").callprop('consume')
                if PyJsStrictEq(var.get('str'),Js('')):
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(((((Js('Invalid ')+var.get('modeName'))+Js(": '"))+var.get('firstToken').get('text'))+Js("'")), var.get('firstToken')))
                    raise PyJsTempException
                var.get(u"this").put('mode', var.get('outerMode'))
                return var.get('firstToken').callprop('range', var.get('lastToken'), var.get('str'))
            PyJs_parseRegexGroup_406_._set_name('parseRegexGroup')
            var.get('_proto').put('parseRegexGroup', PyJs_parseRegexGroup_406_)
            @Js
            def PyJs_parseColorGroup_407_(optional, this, arguments, var=var):
                var = Scope({'optional':optional, 'this':this, 'arguments':arguments, 'parseColorGroup':PyJs_parseColorGroup_407_}, var)
                var.registers(['res', 'optional', 'match', 'color'])
                var.put('res', var.get(u"this").callprop('parseStringGroup', Js('color'), var.get('optional')))
                if var.get('res').neg():
                    return var.get(u"null")
                var.put('match', JsRegExp('/^(#[a-f0-9]{3}|#?[a-f0-9]{6}|[a-z]+)$/i').callprop('exec', var.get('res').get('text')))
                if var.get('match').neg():
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js("Invalid color: '")+var.get('res').get('text'))+Js("'")), var.get('res')))
                    raise PyJsTempException
                var.put('color', var.get('match').get('0'))
                if JsRegExp('/^[0-9a-f]{6}$/i').callprop('test', var.get('color')):
                    var.put('color', (Js('#')+var.get('color')))
                return Js({'type':Js('color-token'),'mode':var.get(u"this").get('mode'),'color':var.get('color')})
            PyJs_parseColorGroup_407_._set_name('parseColorGroup')
            var.get('_proto').put('parseColorGroup', PyJs_parseColorGroup_407_)
            @Js
            def PyJs_parseSizeGroup_408_(optional, this, arguments, var=var):
                var = Scope({'optional':optional, 'this':this, 'arguments':arguments, 'parseSizeGroup':PyJs_parseSizeGroup_408_}, var)
                var.registers(['optional', 'data', 'res', 'isBlank', 'match'])
                pass
                var.put('isBlank', Js(False))
                if (var.get('optional').neg() and PyJsStrictNeq(var.get(u"this").get('nextToken').get('text'),Js('{'))):
                    var.put('res', var.get(u"this").callprop('parseRegexGroup', JsRegExp('/^[-+]? *(?:$|\\d+|\\d+\\.\\d*|\\.\\d*) *[a-z]{0,2} *$/'), Js('size')))
                else:
                    var.put('res', var.get(u"this").callprop('parseStringGroup', Js('size'), var.get('optional')))
                if var.get('res').neg():
                    return var.get(u"null")
                if (var.get('optional').neg() and PyJsStrictEq(var.get('res').get('text').get('length'),Js(0.0))):
                    var.get('res').put('text', Js('0pt'))
                    var.put('isBlank', Js(True))
                var.put('match', JsRegExp('/([-+]?) *(\\d+(?:\\.\\d*)?|\\.\\d+) *([a-z]{2})/').callprop('exec', var.get('res').get('text')))
                if var.get('match').neg():
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js("Invalid size: '")+var.get('res').get('text'))+Js("'")), var.get('res')))
                    raise PyJsTempException
                var.put('data', Js({'number':(+(var.get('match').get('1')+var.get('match').get('2'))),'unit':var.get('match').get('3')}))
                if var.get('validUnit')(var.get('data')).neg():
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js("Invalid unit: '")+var.get('data').get('unit'))+Js("'")), var.get('res')))
                    raise PyJsTempException
                return Js({'type':Js('size'),'mode':var.get(u"this").get('mode'),'value':var.get('data'),'isBlank':var.get('isBlank')})
            PyJs_parseSizeGroup_408_._set_name('parseSizeGroup')
            var.get('_proto').put('parseSizeGroup', PyJs_parseSizeGroup_408_)
            @Js
            def PyJs_parseUrlGroup_409_(optional, this, arguments, var=var):
                var = Scope({'optional':optional, 'this':this, 'arguments':arguments, 'parseUrlGroup':PyJs_parseUrlGroup_409_}, var)
                var.registers(['protocol', 'optional', 'res', 'url', 'allowed'])
                var.put('res', var.get(u"this").callprop('parseStringGroup', Js('url'), var.get('optional'), Js(True)))
                if var.get('res').neg():
                    return var.get(u"null")
                var.put('url', var.get('res').get('text').callprop('replace', JsRegExp('/\\\\([#$%&~_^{}])/g'), Js('$1')))
                var.put('protocol', JsRegExp('/^\\s*([^\\\\/#]*?)(?::|&#0*58|&#x0*3a)/i').callprop('exec', var.get('url')))
                var.put('protocol', (var.get('protocol').get('1') if (var.get('protocol')!=var.get(u"null")) else Js('_relative')))
                var.put('allowed', var.get(u"this").get('settings').get('allowedProtocols'))
                if (var.get('utils').callprop('contains', var.get('allowed'), Js('*')).neg() and var.get('utils').callprop('contains', var.get('allowed'), var.get('protocol')).neg()):
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js("Forbidden protocol '")+var.get('protocol'))+Js("'")), var.get('res')))
                    raise PyJsTempException
                return Js({'type':Js('url'),'mode':var.get(u"this").get('mode'),'url':var.get('url')})
            PyJs_parseUrlGroup_409_._set_name('parseUrlGroup')
            var.get('_proto').put('parseUrlGroup', PyJs_parseUrlGroup_409_)
            @Js
            def PyJs_parseGroup_410_(name, optional, greediness, breakOnTokenText, mode, this, arguments, var=var):
                var = Scope({'name':name, 'optional':optional, 'greediness':greediness, 'breakOnTokenText':breakOnTokenText, 'mode':mode, 'this':this, 'arguments':arguments, 'parseGroup':PyJs_parseGroup_410_}, var)
                var.registers(['greediness', 'breakOnTokenText', 'expression', 'groupEnd', 'mode', 'optional', 'text', 'outerMode', 'result', 'firstToken', 'lastToken', 'name'])
                var.put('outerMode', var.get(u"this").get('mode'))
                var.put('firstToken', var.get(u"this").get('nextToken'))
                var.put('text', var.get('firstToken').get('text'))
                if var.get('mode'):
                    var.get(u"this").callprop('switchMode', var.get('mode'))
                pass
                pass
                if (PyJsStrictEq(var.get('text'),Js('[')) if var.get('optional') else (PyJsStrictEq(var.get('text'),Js('{')) or PyJsStrictEq(var.get('text'),Js('\\begingroup')))):
                    var.put('groupEnd', var.get('Parser').get('endOfGroup').get(var.get('text')))
                    var.get(u"this").get('gullet').callprop('beginGroup')
                    var.get(u"this").callprop('consume')
                    var.put('expression', var.get(u"this").callprop('parseExpression', Js(False), var.get('groupEnd')))
                    var.put('lastToken', var.get(u"this").get('nextToken'))
                    var.get(u"this").get('gullet').callprop('endGroup')
                    var.put('result', Js({'type':Js('ordgroup'),'mode':var.get(u"this").get('mode'),'loc':var.get('SourceLocation').callprop('range', var.get('firstToken'), var.get('lastToken')),'body':var.get('expression'),'semisimple':(PyJsStrictEq(var.get('text'),Js('\\begingroup')) or var.get('undefined'))}))
                else:
                    if var.get('optional'):
                        var.put('result', var.get(u"null"))
                    else:
                        var.put('result', (var.get(u"this").callprop('parseFunction', var.get('breakOnTokenText'), var.get('name'), var.get('greediness')) or var.get(u"this").callprop('parseSymbol')))
                        if (((var.get('result')==var.get(u"null")) and PyJsStrictEq(var.get('text').get('0'),Js('\\'))) and var.get('implicitCommands').callprop('hasOwnProperty', var.get('text')).neg()):
                            if var.get(u"this").get('settings').get('throwOnError'):
                                PyJsTempException = JsToPyException(var.get('src_ParseError').create((Js('Undefined control sequence: ')+var.get('text')), var.get('firstToken')))
                                raise PyJsTempException
                            var.put('result', var.get(u"this").callprop('handleUnsupportedCmd'))
                if var.get('mode'):
                    var.get(u"this").callprop('switchMode', var.get('outerMode'))
                if var.get('groupEnd'):
                    var.get(u"this").callprop('expect', var.get('groupEnd'))
                return var.get('result')
            PyJs_parseGroup_410_._set_name('parseGroup')
            var.get('_proto').put('parseGroup', PyJs_parseGroup_410_)
            @Js
            def PyJs_formLigatures_411_(group, this, arguments, var=var):
                var = Scope({'group':group, 'this':this, 'arguments':arguments, 'formLigatures':PyJs_formLigatures_411_}, var)
                var.registers(['i', 'group', 'a', 'v', 'n'])
                var.put('n', (var.get('group').get('length')-Js(1.0)))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('n')):
                    try:
                        var.put('a', var.get('group').get(var.get('i')))
                        var.put('v', var.get('a').get('text'))
                        if (PyJsStrictEq(var.get('v'),Js('-')) and PyJsStrictEq(var.get('group').get((var.get('i')+Js(1.0))).get('text'),Js('-'))):
                            if (((var.get('i')+Js(1.0))<var.get('n')) and PyJsStrictEq(var.get('group').get((var.get('i')+Js(2.0))).get('text'),Js('-'))):
                                var.get('group').callprop('splice', var.get('i'), Js(3.0), Js({'type':Js('textord'),'mode':Js('text'),'loc':var.get('SourceLocation').callprop('range', var.get('a'), var.get('group').get((var.get('i')+Js(2.0)))),'text':Js('---')}))
                                var.put('n', Js(2.0), '-')
                            else:
                                var.get('group').callprop('splice', var.get('i'), Js(2.0), Js({'type':Js('textord'),'mode':Js('text'),'loc':var.get('SourceLocation').callprop('range', var.get('a'), var.get('group').get((var.get('i')+Js(1.0)))),'text':Js('--')}))
                                var.put('n', Js(1.0), '-')
                        if ((PyJsStrictEq(var.get('v'),Js("'")) or PyJsStrictEq(var.get('v'),Js('`'))) and PyJsStrictEq(var.get('group').get((var.get('i')+Js(1.0))).get('text'),var.get('v'))):
                            var.get('group').callprop('splice', var.get('i'), Js(2.0), Js({'type':Js('textord'),'mode':Js('text'),'loc':var.get('SourceLocation').callprop('range', var.get('a'), var.get('group').get((var.get('i')+Js(1.0)))),'text':(var.get('v')+var.get('v'))}))
                            var.put('n', Js(1.0), '-')
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
            PyJs_formLigatures_411_._set_name('formLigatures')
            var.get('_proto').put('formLigatures', PyJs_formLigatures_411_)
            @Js
            def PyJs_parseSymbol_412_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'parseSymbol':PyJs_parseSymbol_412_}, var)
                var.registers(['loc', 'family', 'i', 'nucleus', 's', 'group', 'star', 'text', 'arg', 'symbol', 'accent', 'command', 'match'])
                var.put('nucleus', var.get(u"this").get('nextToken'))
                var.put('text', var.get('nucleus').get('text'))
                if JsRegExp('/^\\\\verb[^a-zA-Z]/').callprop('test', var.get('text')):
                    var.get(u"this").callprop('consume')
                    var.put('arg', var.get('text').callprop('slice', Js(5.0)))
                    var.put('star', PyJsStrictEq(var.get('arg').callprop('charAt', Js(0.0)),Js('*')))
                    if var.get('star'):
                        var.put('arg', var.get('arg').callprop('slice', Js(1.0)))
                    if ((var.get('arg').get('length')<Js(2.0)) or PyJsStrictNeq(var.get('arg').callprop('charAt', Js(0.0)),var.get('arg').callprop('slice', (-Js(1.0))))):
                        PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('\\verb assertion failed --\n                    please report what input caused this bug')))
                        raise PyJsTempException
                    var.put('arg', var.get('arg').callprop('slice', Js(1.0), (-Js(1.0))))
                    return Js({'type':Js('verb'),'mode':Js('text'),'body':var.get('arg'),'star':var.get('star')})
                if (var.get('unicodeSymbols').callprop('hasOwnProperty', var.get('text').get('0')) and var.get('src_symbols').get(var.get(u"this").get('mode')).get(var.get('text').get('0')).neg()):
                    if (var.get(u"this").get('settings').get('strict') and PyJsStrictEq(var.get(u"this").get('mode'),Js('math'))):
                        var.get(u"this").get('settings').callprop('reportNonstrict', Js('unicodeTextInMathMode'), (((Js('Accented Unicode text character "')+var.get('text').get('0'))+Js('" used in '))+Js('math mode')), var.get('nucleus'))
                    var.put('text', (var.get('unicodeSymbols').get(var.get('text').get('0'))+var.get('text').callprop('substr', Js(1.0))))
                var.put('match', var.get('combiningDiacriticalMarksEndRegex').callprop('exec', var.get('text')))
                if var.get('match'):
                    var.put('text', var.get('text').callprop('substring', Js(0.0), var.get('match').get('index')))
                    if PyJsStrictEq(var.get('text'),Js('i')):
                        var.put('text', Js('ı'))
                    else:
                        if PyJsStrictEq(var.get('text'),Js('j')):
                            var.put('text', Js('ȷ'))
                pass
                if var.get('src_symbols').get(var.get(u"this").get('mode')).get(var.get('text')):
                    if ((var.get(u"this").get('settings').get('strict') and PyJsStrictEq(var.get(u"this").get('mode'),Js('math'))) and (var.get('extraLatin').callprop('indexOf', var.get('text'))>=Js(0.0))):
                        var.get(u"this").get('settings').callprop('reportNonstrict', Js('unicodeTextInMathMode'), (((Js('Latin-1/Unicode text character "')+var.get('text').get('0'))+Js('" used in '))+Js('math mode')), var.get('nucleus'))
                    var.put('group', var.get('src_symbols').get(var.get(u"this").get('mode')).get(var.get('text')).get('group'))
                    var.put('loc', var.get('SourceLocation').callprop('range', var.get('nucleus')))
                    pass
                    if var.get('ATOMS').callprop('hasOwnProperty', var.get('group')):
                        var.put('family', var.get('group'))
                        var.put('s', Js({'type':Js('atom'),'mode':var.get(u"this").get('mode'),'family':var.get('family'),'loc':var.get('loc'),'text':var.get('text')}))
                    else:
                        var.put('s', Js({'type':var.get('group'),'mode':var.get(u"this").get('mode'),'loc':var.get('loc'),'text':var.get('text')}))
                    var.put('symbol', var.get('s'))
                else:
                    if (var.get('text').callprop('charCodeAt', Js(0.0))>=Js(128)):
                        if var.get(u"this").get('settings').get('strict'):
                            if var.get('supportedCodepoint')(var.get('text').callprop('charCodeAt', Js(0.0))).neg():
                                var.get(u"this").get('settings').callprop('reportNonstrict', Js('unknownSymbol'), (((Js('Unrecognized Unicode character "')+var.get('text').get('0'))+Js('"'))+((Js(' (')+var.get('text').callprop('charCodeAt', Js(0.0)))+Js(')'))), var.get('nucleus'))
                            else:
                                if PyJsStrictEq(var.get(u"this").get('mode'),Js('math')):
                                    var.get(u"this").get('settings').callprop('reportNonstrict', Js('unicodeTextInMathMode'), ((Js('Unicode text character "')+var.get('text').get('0'))+Js('" used in math mode')), var.get('nucleus'))
                        var.put('symbol', Js({'type':Js('textord'),'mode':var.get(u"this").get('mode'),'loc':var.get('SourceLocation').callprop('range', var.get('nucleus')),'text':var.get('text')}))
                    else:
                        return var.get(u"null")
                var.get(u"this").callprop('consume')
                if var.get('match'):
                    #for JS loop
                    var.put('i', Js(0.0))
                    while (var.get('i')<var.get('match').get('0').get('length')):
                        try:
                            var.put('accent', var.get('match').get('0').get(var.get('i')))
                            if var.get('unicodeAccents').get(var.get('accent')).neg():
                                PyJsTempException = JsToPyException(var.get('src_ParseError').create(((Js("Unknown accent ' ")+var.get('accent'))+Js("'")), var.get('nucleus')))
                                raise PyJsTempException
                            var.put('command', var.get('unicodeAccents').get(var.get('accent')).get(var.get(u"this").get('mode')))
                            if var.get('command').neg():
                                PyJsTempException = JsToPyException(var.get('src_ParseError').create(((((Js('Accent ')+var.get('accent'))+Js(' unsupported in '))+var.get(u"this").get('mode'))+Js(' mode')), var.get('nucleus')))
                                raise PyJsTempException
                            var.put('symbol', Js({'type':Js('accent'),'mode':var.get(u"this").get('mode'),'loc':var.get('SourceLocation').callprop('range', var.get('nucleus')),'label':var.get('command'),'isStretchy':Js(False),'isShifty':Js(True),'base':var.get('symbol')}))
                        finally:
                                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                return var.get('symbol')
            PyJs_parseSymbol_412_._set_name('parseSymbol')
            var.get('_proto').put('parseSymbol', PyJs_parseSymbol_412_)
            return var.get('Parser')
        PyJs_anonymous_390_._set_name('anonymous')
        var.put('Parser_Parser', PyJs_anonymous_390_())
        var.get('Parser_Parser').put('endOfExpression', Js([Js('}'), Js('\\endgroup'), Js('\\end'), Js('\\right'), Js('&')]))
        var.get('Parser_Parser').put('endOfGroup', Js({'[':Js(']'),'{':Js('}'),'\\begingroup':Js('\\endgroup')}))
        var.get('Parser_Parser').put('SUPSUB_GREEDINESS', Js(1.0))
        @Js
        def PyJs_parseTree_413_(toParse, settings, this, arguments, var=var):
            var = Scope({'toParse':toParse, 'settings':settings, 'this':this, 'arguments':arguments, 'parseTree':PyJs_parseTree_413_}, var)
            var.registers(['toParse', 'parser', 'tree', 'settings'])
            if (PyJsStrictEq(var.get('toParse',throw=False).typeof(),Js('string')) or var.get('toParse').instanceof(var.get('String'))).neg():
                PyJsTempException = JsToPyException(var.get('TypeError').create(Js('KaTeX can only parse string typed expression')))
                raise PyJsTempException
            var.put('parser', var.get('Parser_Parser').create(var.get('toParse'), var.get('settings')))
            var.get('parser').get('gullet').get('macros').get('current').delete('\\df@tag')
            var.put('tree', var.get('parser').callprop('parse'))
            if var.get('parser').get('gullet').get('macros').callprop('get', Js('\\df@tag')):
                if var.get('settings').get('displayMode').neg():
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js('\\tag works only in display equations')))
                    raise PyJsTempException
                var.get('parser').get('gullet').callprop('feed', Js('\\df@tag'))
                var.put('tree', Js([Js({'type':Js('tag'),'mode':Js('text'),'body':var.get('tree'),'tag':var.get('parser').callprop('parse')})]))
            return var.get('tree')
        PyJs_parseTree_413_._set_name('parseTree')
        var.put('parseTree_parseTree', PyJs_parseTree_413_)
        var.put('src_parseTree', var.get('parseTree_parseTree'))
        @Js
        def PyJs_render_414_(expression, baseNode, options, this, arguments, var=var):
            var = Scope({'expression':expression, 'baseNode':baseNode, 'options':options, 'this':this, 'arguments':arguments, 'render':PyJs_render_414_}, var)
            var.registers(['node', 'options', 'expression', 'baseNode'])
            var.get('baseNode').put('textContent', Js(''))
            var.put('node', var.get('katex_renderToDomTree')(var.get('expression'), var.get('options')).callprop('toNode'))
            var.get('baseNode').callprop('appendChild', var.get('node'))
        PyJs_render_414_._set_name('render')
        var.put('katex_render', PyJs_render_414_)
        if PyJsStrictNeq(var.get('document',throw=False).typeof(),Js('undefined')):
            if PyJsStrictNeq(var.get('document').get('compatMode'),Js('CSS1Compat')):
                (PyJsStrictNeq(var.get('console',throw=False).typeof(),Js('undefined')) and var.get('console').callprop('warn', (Js("Warning: KaTeX doesn't work in quirks mode. Make sure your ")+Js('website has a suitable doctype.'))))
                @Js
                def PyJs_render_415_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments, 'render':PyJs_render_415_}, var)
                    var.registers([])
                    PyJsTempException = JsToPyException(var.get('src_ParseError').create(Js("KaTeX doesn't work in quirks mode.")))
                    raise PyJsTempException
                PyJs_render_415_._set_name('render')
                var.put('katex_render', PyJs_render_415_)
        @Js
        def PyJs_renderToString_416_(expression, options, this, arguments, var=var):
            var = Scope({'expression':expression, 'options':options, 'this':this, 'arguments':arguments, 'renderToString':PyJs_renderToString_416_}, var)
            var.registers(['options', 'markup', 'expression'])
            var.put('markup', var.get('katex_renderToDomTree')(var.get('expression'), var.get('options')).callprop('toMarkup'))
            return var.get('markup')
        PyJs_renderToString_416_._set_name('renderToString')
        var.put('renderToString', PyJs_renderToString_416_)
        @Js
        def PyJs_generateParseTree_417_(expression, options, this, arguments, var=var):
            var = Scope({'expression':expression, 'options':options, 'this':this, 'arguments':arguments, 'generateParseTree':PyJs_generateParseTree_417_}, var)
            var.registers(['settings', 'options', 'expression'])
            var.put('settings', var.get('src_Settings').create(var.get('options')))
            return var.get('src_parseTree')(var.get('expression'), var.get('settings'))
        PyJs_generateParseTree_417_._set_name('generateParseTree')
        var.put('katex_generateParseTree', PyJs_generateParseTree_417_)
        @Js
        def PyJs_renderError_418_(error, expression, options, this, arguments, var=var):
            var = Scope({'error':error, 'expression':expression, 'options':options, 'this':this, 'arguments':arguments, 'renderError':PyJs_renderError_418_}, var)
            var.registers(['node', 'options', 'expression', 'error'])
            if (var.get('options').get('throwOnError') or var.get('error').instanceof(var.get('src_ParseError')).neg()):
                PyJsTempException = JsToPyException(var.get('error'))
                raise PyJsTempException
            var.put('node', var.get('buildCommon').callprop('makeSpan', Js([Js('katex-error')]), Js([var.get('domTree_SymbolNode').create(var.get('expression'))])))
            var.get('node').callprop('setAttribute', Js('title'), var.get('error').callprop('toString'))
            var.get('node').callprop('setAttribute', Js('style'), (Js('color:')+var.get('options').get('errorColor')))
            return var.get('node')
        PyJs_renderError_418_._set_name('renderError')
        var.put('katex_renderError', PyJs_renderError_418_)
        @Js
        def PyJs_renderToDomTree_419_(expression, options, this, arguments, var=var):
            var = Scope({'expression':expression, 'options':options, 'this':this, 'arguments':arguments, 'renderToDomTree':PyJs_renderToDomTree_419_}, var)
            var.registers(['settings', 'options', 'expression', 'tree'])
            var.put('settings', var.get('src_Settings').create(var.get('options')))
            try:
                var.put('tree', var.get('src_parseTree')(var.get('expression'), var.get('settings')))
                return var.get('buildTree_buildTree')(var.get('tree'), var.get('expression'), var.get('settings'))
            except PyJsException as PyJsTempException:
                PyJsHolder_6572726f72_72941069 = var.own.get('error')
                var.force_own_put('error', PyExceptionToJs(PyJsTempException))
                try:
                    return var.get('katex_renderError')(var.get('error'), var.get('expression'), var.get('settings'))
                finally:
                    if PyJsHolder_6572726f72_72941069 is not None:
                        var.own['error'] = PyJsHolder_6572726f72_72941069
                    else:
                        del var.own['error']
                    del PyJsHolder_6572726f72_72941069
        PyJs_renderToDomTree_419_._set_name('renderToDomTree')
        var.put('katex_renderToDomTree', PyJs_renderToDomTree_419_)
        @Js
        def PyJs_renderToHTMLTree_420_(expression, options, this, arguments, var=var):
            var = Scope({'expression':expression, 'options':options, 'this':this, 'arguments':arguments, 'renderToHTMLTree':PyJs_renderToHTMLTree_420_}, var)
            var.registers(['settings', 'options', 'expression', 'tree'])
            var.put('settings', var.get('src_Settings').create(var.get('options')))
            try:
                var.put('tree', var.get('src_parseTree')(var.get('expression'), var.get('settings')))
                return var.get('buildTree_buildHTMLTree')(var.get('tree'), var.get('expression'), var.get('settings'))
            except PyJsException as PyJsTempException:
                PyJsHolder_6572726f72_69532139 = var.own.get('error')
                var.force_own_put('error', PyExceptionToJs(PyJsTempException))
                try:
                    return var.get('katex_renderError')(var.get('error'), var.get('expression'), var.get('settings'))
                finally:
                    if PyJsHolder_6572726f72_69532139 is not None:
                        var.own['error'] = PyJsHolder_6572726f72_69532139
                    else:
                        del var.own['error']
                    del PyJsHolder_6572726f72_69532139
        PyJs_renderToHTMLTree_420_._set_name('renderToHTMLTree')
        var.put('katex_renderToHTMLTree', PyJs_renderToHTMLTree_420_)
        var.put('katex_0', Js({'version':Js('0.10.2'),'render':var.get('katex_render'),'renderToString':var.get('renderToString'),'ParseError':var.get('src_ParseError'),'__parse':var.get('katex_generateParseTree'),'__renderToDomTree':var.get('katex_renderToDomTree'),'__renderToHTMLTree':var.get('katex_renderToHTMLTree'),'__setFontMetrics':var.get('setFontMetrics'),'__defineSymbol':var.get('defineSymbol'),'__defineMacro':var.get('defineMacro'),'__domTree':Js({'Span':var.get('domTree_Span'),'Anchor':var.get('domTree_Anchor'),'SymbolNode':var.get('domTree_SymbolNode'),'SvgNode':var.get('SvgNode'),'PathNode':var.get('domTree_PathNode'),'LineNode':var.get('LineNode')})}))
        var.put('katex_webpack', var.get('__webpack_exports__').put('default', var.get('katex_0')))
    PyJs_anonymous_2_._set_name('anonymous')
    @Js
    def PyJs_anonymous_421_(modules, this, arguments, var=var):
        var = Scope({'modules':modules, 'this':this, 'arguments':arguments}, var)
        var.registers(['installedModules', 'modules', '__webpack_require__'])
        @Js
        def PyJsHoisted___webpack_require___(moduleId, this, arguments, var=var):
            var = Scope({'moduleId':moduleId, 'this':this, 'arguments':arguments}, var)
            var.registers(['moduleId', 'module'])
            if var.get('installedModules').get(var.get('moduleId')):
                return var.get('installedModules').get(var.get('moduleId')).get('exports')
            var.put('module', var.get('installedModules').put(var.get('moduleId'), Js({'i':var.get('moduleId'),'l':Js(False),'exports':Js({})})))
            var.get('modules').get(var.get('moduleId')).callprop('call', var.get('module').get('exports'), var.get('module'), var.get('module').get('exports'), var.get('__webpack_require__'))
            var.get('module').put('l', Js(True))
            return var.get('module').get('exports')
        PyJsHoisted___webpack_require___.func_name = '__webpack_require__'
        var.put('__webpack_require__', PyJsHoisted___webpack_require___)
        var.put('installedModules', Js({}))
        pass
        var.get('__webpack_require__').put('m', var.get('modules'))
        var.get('__webpack_require__').put('c', var.get('installedModules'))
        @Js
        def PyJs_anonymous_422_(exports, name, getter, this, arguments, var=var):
            var = Scope({'exports':exports, 'name':name, 'getter':getter, 'this':this, 'arguments':arguments}, var)
            var.registers(['exports', 'getter', 'name'])
            if var.get('__webpack_require__').callprop('o', var.get('exports'), var.get('name')).neg():
                var.get('Object').callprop('defineProperty', var.get('exports'), var.get('name'), Js({'enumerable':Js(True),'get':var.get('getter')}))
        PyJs_anonymous_422_._set_name('anonymous')
        var.get('__webpack_require__').put('d', PyJs_anonymous_422_)
        @Js
        def PyJs_anonymous_423_(exports, this, arguments, var=var):
            var = Scope({'exports':exports, 'this':this, 'arguments':arguments}, var)
            var.registers(['exports'])
            if (PyJsStrictNeq(var.get('Symbol',throw=False).typeof(),Js('undefined')) and var.get('Symbol').get('toStringTag')):
                var.get('Object').callprop('defineProperty', var.get('exports'), var.get('Symbol').get('toStringTag'), Js({'value':Js('Module')}))
            var.get('Object').callprop('defineProperty', var.get('exports'), Js('__esModule'), Js({'value':Js(True)}))
        PyJs_anonymous_423_._set_name('anonymous')
        var.get('__webpack_require__').put('r', PyJs_anonymous_423_)
        @Js
        def PyJs_anonymous_424_(value, mode, this, arguments, var=var):
            var = Scope({'value':value, 'mode':mode, 'this':this, 'arguments':arguments}, var)
            var.registers(['ns', 'key', 'value', 'mode'])
            if (var.get('mode')&Js(1.0)):
                var.put('value', var.get('__webpack_require__')(var.get('value')))
            if (var.get('mode')&Js(8.0)):
                return var.get('value')
            if ((((var.get('mode')&Js(4.0)) and PyJsStrictEq(var.get('value',throw=False).typeof(),Js('object'))) and var.get('value')) and var.get('value').get('__esModule')):
                return var.get('value')
            var.put('ns', var.get('Object').callprop('create', var.get(u"null")))
            var.get('__webpack_require__').callprop('r', var.get('ns'))
            var.get('Object').callprop('defineProperty', var.get('ns'), Js('default'), Js({'enumerable':Js(True),'value':var.get('value')}))
            if ((var.get('mode')&Js(2.0)) and (var.get('value',throw=False).typeof()!=Js('string'))):
                for PyJsTemp in var.get('value'):
                    var.put('key', PyJsTemp)
                    @Js
                    def PyJs_anonymous_425_(key, this, arguments, var=var):
                        var = Scope({'key':key, 'this':this, 'arguments':arguments}, var)
                        var.registers(['key'])
                        return var.get('value').get(var.get('key'))
                    PyJs_anonymous_425_._set_name('anonymous')
                    var.get('__webpack_require__').callprop('d', var.get('ns'), var.get('key'), PyJs_anonymous_425_.callprop('bind', var.get(u"null"), var.get('key')))
            return var.get('ns')
        PyJs_anonymous_424_._set_name('anonymous')
        var.get('__webpack_require__').put('t', PyJs_anonymous_424_)
        @Js
        def PyJs_anonymous_426_(module, this, arguments, var=var):
            var = Scope({'module':module, 'this':this, 'arguments':arguments}, var)
            var.registers(['getter', 'module'])
            @Js
            def PyJs_getDefault_427_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'getDefault':PyJs_getDefault_427_}, var)
                var.registers([])
                return var.get('module').get('default')
            PyJs_getDefault_427_._set_name('getDefault')
            @Js
            def PyJs_getModuleExports_428_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'getModuleExports':PyJs_getModuleExports_428_}, var)
                var.registers([])
                return var.get('module')
            PyJs_getModuleExports_428_._set_name('getModuleExports')
            var.put('getter', (PyJs_getDefault_427_ if (var.get('module') and var.get('module').get('__esModule')) else PyJs_getModuleExports_428_))
            var.get('__webpack_require__').callprop('d', var.get('getter'), Js('a'), var.get('getter'))
            return var.get('getter')
        PyJs_anonymous_426_._set_name('anonymous')
        var.get('__webpack_require__').put('n', PyJs_anonymous_426_)
        @Js
        def PyJs_anonymous_429_(object, property, this, arguments, var=var):
            var = Scope({'object':object, 'property':property, 'this':this, 'arguments':arguments}, var)
            var.registers(['property', 'object'])
            return var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get('object'), var.get('property'))
        PyJs_anonymous_429_._set_name('anonymous')
        var.get('__webpack_require__').put('o', PyJs_anonymous_429_)
        var.get('__webpack_require__').put('p', Js(''))
        return var.get('__webpack_require__')(var.get('__webpack_require__').put('s', Js(1.0)))
    PyJs_anonymous_421_._set_name('anonymous')
    return PyJs_anonymous_421_(Js([PyJs_anonymous_1_, PyJs_anonymous_2_])).get('default')
PyJs_anonymous_0_._set_name('anonymous')
@Js
def PyJs_webpackUniversalModuleDefinition_430_(root, factory, this, arguments, var=var):
    var = Scope({'root':root, 'factory':factory, 'this':this, 'arguments':arguments, 'webpackUniversalModuleDefinition':PyJs_webpackUniversalModuleDefinition_430_}, var)
    var.registers(['factory', 'root'])
    if (PyJsStrictEq(var.get('exports',throw=False).typeof(),Js('object')) and PyJsStrictEq(var.get('module',throw=False).typeof(),Js('object'))):
        var.get('module').put('exports', var.get('factory')())
    else:
        if (PyJsStrictEq(var.get('define',throw=False).typeof(),Js('function')) and var.get('define').get('amd')):
            var.get('define')(Js([]), var.get('factory'))
        else:
            if PyJsStrictEq(var.get('exports',throw=False).typeof(),Js('object')):
                var.get('exports').put('katex', var.get('factory')())
            else:
                var.get('root').put('katex', var.get('factory')())
PyJs_webpackUniversalModuleDefinition_430_._set_name('webpackUniversalModuleDefinition')
PyJs_webpackUniversalModuleDefinition_430_((var.get('self') if PyJsStrictNeq(var.get('self',throw=False).typeof(),Js('undefined')) else var.get(u"this")), PyJs_anonymous_0_)
pass


# Add lib to the module scope
watex = var.to_python()