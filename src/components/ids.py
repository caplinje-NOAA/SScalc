from . import text
from ..calculator.data import pileDrivingDefaults


CONFIGURE_SOURCES_CANVAS = "source-canvas"
CONFIGURE_SOURCES_BUTTON = "config-sources-button"
N_SOURCES_INPUT = "number-sources-input"
SOURCE_TYPE_DROPDOWN_CONTAINER="source-type-dropdown-container"
SAVE_CONIG_BUTTON = 'save-config-button'
SOURCE_TYPES = 'source-type-selectors'
CONFIG_DISPLAY = 'config-display'
CANVAS_ALERT = 'canvas-alert'
INPUTS_DIV='inputs-div'
CALCULATE_BUTTON='calculate-button'
RESULTS_DIV = 'results-div'
WF_RADIO = 'wf-radio'
F_RADIO = 'f-radio'

SELRES ='sel-res'
HIDDEN_SOURCE_BUTTON = 'ghost-busters'

IMPACT = 'impact'
VIBRATORY = 'vibratory'
DTH = 'DTH'
SEL = 'SEL'
PEAK = 'PEAK'
RMS = 'RMS'
RANGE = 'RANGE'
NPILES = 'NPILES'
NSTRIKES = 'NSTRIKES'
WF = 'WF'
RATE = 'RATE'
TIME = 'TIME'
F='TL-coef'


WF_INPUT =          {'parameter':WF, 'name':'Weighting Frequency', 'unit':'KHz'}
F_INPUT_BYSOURCE =  {'parameter':F, 'name':'Transmission Loss Coef.', 'unit':'dB','value':pileDrivingDefaults.F}


# input ids, names, and units for big column inputs
# grouped as dictionaries with associated text to avoid inconsistencies between ids and text
IMPACT_INPUT_SEL =       {'sourceType':IMPACT,    'parameter':SEL,     'name':'SEL_{ss}',              'unit':text.SELunits}
IMPACT_INPUT_PEAK =      {'sourceType':IMPACT,    'parameter':PEAK,    'name':"L_{peak}",              'unit':text.Lunits}
IMPACT_INPUT_RMS =       {'sourceType':IMPACT,    'parameter':RMS,     'name':"L_{rms}",               'unit':text.Lunits}
IMPACT_INPUT_RANGE =     {'sourceType':IMPACT,    'parameter':RANGE,   'name':"Range of source levels",'unit':"meters",   'value':pileDrivingDefaults.measurement_range}
IMPACT_INPUT_NPILES =    {'sourceType':IMPACT,    'parameter':NPILES,  'name':"Number of Piles",       'unit':"#"}
IMPACT_INPUT_NSTRIKES =  {'sourceType':IMPACT,    'parameter':NSTRIKES,'name':"Strikes per pile",      'unit':"#"}


impactInputDict = [IMPACT_INPUT_SEL,
 #                  IMPACT_INPUT_PEAK,
#                   IMPACT_INPUT_RMS,
                   IMPACT_INPUT_RANGE,
                   IMPACT_INPUT_NPILES,
                   IMPACT_INPUT_NSTRIKES]

DTH_INPUT_SEL =     {'sourceType':DTH,    'parameter':SEL,     'name':'SEL_{ss}',                  'unit':text.SELunits}
DTH_INPUT_PEAK =    {'sourceType':DTH,    'parameter':PEAK,    'name':"L_{peak}",                  'unit':text.Lunits}
DTH_INPUT_RMS =     {'sourceType':DTH,    'parameter':RMS,     'name':"L_{rms}",                   'unit':text.Lunits}
DTH_INPUT_RANGE =   {'sourceType':DTH,    'parameter':RANGE,   'name':"Range of source levels",    'unit':"meters",    'value':pileDrivingDefaults.measurement_range}
DTH_INPUT_NPILES =  {'sourceType':DTH,    'parameter':NPILES,  'name':"Number of Piles",           'unit':"#"}
DTH_INPUT_RATE =    {'sourceType':DTH,    'parameter':RATE,    'name':"Strike Rate",               'unit':"Per Second"}
DTH_INPUT_TIME =    {'sourceType':DTH,    'parameter':TIME,    'name':"Time Per Pile",             'unit':"Min."}


DTH_InputDict =   [DTH_INPUT_SEL,
 #                  DTH_INPUT_PEAK,
 #                  DTH_INPUT_RMS,
                   DTH_INPUT_RANGE,
                   DTH_INPUT_NPILES,
                   DTH_INPUT_TIME,
                   DTH_INPUT_RATE]

VIBRATORY_INPUT_RMS =   {'sourceType':VIBRATORY,    'parameter':RMS,     'name':"Lrms",                      'unit':text.Lunits}
VIBRATORY_INPUT_RANGE = {'sourceType':VIBRATORY,    'parameter':RANGE,   'name':"Range of source levels",    'unit':"meters",    'value':pileDrivingDefaults.measurement_range}
VIBRATORY_INPUT_NPILES ={'sourceType':VIBRATORY,    'parameter':NPILES,  'name':"Number of Piles",           'unit':"#"}
VIBRATORY_INPUT_TIME =  {'sourceType':VIBRATORY,    'parameter':TIME,    'name':"Time Per Pile",             'unit':"Min."}


vibratoryInputDict = [VIBRATORY_INPUT_RMS,
                      VIBRATORY_INPUT_RANGE,
                      VIBRATORY_INPUT_NPILES,
                      VIBRATORY_INPUT_TIME]
