from . import text

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
WF_INPUT = 'wfinput'
F_INPUT = 'finput'

SELRES ='sel-res'
HIDDEN_SOURCE_BUTTON = 'ghost-busters'


# input ids, names, and units for big column inputs
# grouped as dictionaries with associated text to avoid inconsistencies between ids and text
IMPACT_INPUT_SEL={'id':'impSEL','name':'SEL_{ss}','unit':text.SELunits}
IMPACT_INPUT_PEAK={'id':'impPEAK','name':"L_{peak}",'unit':text.Lunits}
IMPACT_INPUT_RMS={'id':'impRMS','name':"L_{rms}",'unit':text.Lunits}
IMPACT_INPUT_RANGE={'id':'impRANGE','name':"Range of source levels",'unit':"meters",'value':10.0}
IMPACT_INPUT_NPILES={'id':'impNPILES','name':"Number of Piles",'unit':"#"}
IMPACT_INPUT_NSTRIKES={'id':'impNSTRIKES','name':"Strikes per pile",'unit':"#"}
IMPACT_INPUT_WF = {'name':"Weighting Frequency",'id':'impWF','unit':'KHz','value':2.0}

impactInputDict = [IMPACT_INPUT_SEL,
                   IMPACT_INPUT_PEAK,
                   IMPACT_INPUT_RMS,
                   IMPACT_INPUT_RANGE,
                   IMPACT_INPUT_NPILES,
                   IMPACT_INPUT_NSTRIKES,
                   IMPACT_INPUT_WF]

DTH_INPUT_SEL={'id':'dthSEL','name':'SEL_{ss}','unit':text.SELunits}
DTH_INPUT_PEAK={'id':'dthPEAK','name':"L_{peak}",'unit':text.Lunits}
DTH_INPUT_RMS={'id':'dthRMS','name':"L_{rms}",'unit':text.Lunits}
DTH_INPUT_RANGE={'id':'dthRANGE','name':"Range of source levels",'unit':"meters",'value':10.0}
DTH_INPUT_NPILES={'id':'dthNPILES','name':"Number of Piles",'unit':"#"}
DTH_INPUT_RATE={'id':'dthRATE','name':"Strike Rate",'unit':"Per Second"}
DTH_INPUT_TIME={'id':'dthTIME','name':"Time Per Pile",'unit':"Min."}
DTH_INPUT_WF = {'name':"Weighting Frequency",'id':'dthWF','unit':'KHz','value':2.0}

DTH_InputDict =   [DTH_INPUT_SEL,
                   DTH_INPUT_PEAK,
                   DTH_INPUT_RMS,
                   DTH_INPUT_RANGE,
                   DTH_INPUT_NPILES,
                   DTH_INPUT_TIME,
                   DTH_INPUT_RATE,
                   DTH_INPUT_WF]

VIBRATORY_INPUT_RMS={'id':'vibRMS','name':"Lrms",'unit':text.Lunits}
VIBRATORY_INPUT_RANGE={'id':'vibRANGE','name':"Range of source levels",'unit':"meters",'value':10.0}
VIBRATORY_INPUT_NPILES={'id':'vibNPILES','name':"Number of Piles",'unit':"#"}
VIBRATORY_INPUT_TIME={'id':'vibTIME','name':"Time Per Pile",'unit':"Min."}
VIBRATORY_INPUT_WF = {'name':"Weighting Frequency",'id':'vibWF','unit':'KHz','value':2.0}

vibratoryInputDict = [VIBRATORY_INPUT_RMS,
                      VIBRATORY_INPUT_RANGE,
                      VIBRATORY_INPUT_NPILES,
                      VIBRATORY_INPUT_TIME,
                      VIBRATORY_INPUT_WF]
