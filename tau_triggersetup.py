from code_generation.configuration import Configuration
from code_generation.modifiers import EraModifier, SampleModifier


def add_diTauTriggerSetup(configuration: Configuration):
    ## MT, MM scope trigger setup
    configuration.add_config_parameters(
        ["emt", "met", "mmt", "mtt", "mme"],
        {
            "singlemoun_trigger": EraModifier(
                {
                    "2018": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.5,
                        },
                        {
                            "flagname": "trg_single_mu27",
                            "hlt_path": "HLT_IsoMu27",
                            "ptcut": 28,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.5,
                        },
                    ],
                    "2017": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.5,
                        },
                        {
                            "flagname": "trg_single_mu27",
                            "hlt_path": "HLT_IsoMu27",
                            "ptcut": 28,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.5,
                        },
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_single_mu22",
                            "hlt_path": "HLT_IsoMu22",
                            "ptcut": 23,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.5,
                        },
                        {
                            "flagname": "trg_single_mu22_tk",
                            "hlt_path": "HLT_IsoTkMu22",
                            "ptcut": 23,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.5,
                        },
                        {
                            "flagname": "trg_single_mu22_eta2p1",
                            "hlt_path": "HLT_IsoMu22_eta2p1",
                            "ptcut": 23,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.5,
                        },
                        {
                            "flagname": "trg_single_mu22_tk_eta2p1",
                            "hlt_path": "HLT_IsoTkMu22_eta2p1",
                            "ptcut": 23,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.5,
                        },
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.5,
                        },
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_single_mu22",
                            "hlt_path": "HLT_IsoMu22",
                            "ptcut": 23,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.5,
                        },
                        {
                            "flagname": "trg_single_mu22_tk",
                            "hlt_path": "HLT_IsoTkMu22",
                            "ptcut": 23,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.5,
                        },
                        {
                            "flagname": "trg_single_mu22_eta2p1",
                            "hlt_path": "HLT_IsoMu22_eta2p1",
                            "ptcut": 23,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.5,
                        },
                        {
                            "flagname": "trg_single_mu22_tk_eta2p1",
                            "hlt_path": "HLT_IsoTkMu22_eta2p1",
                            "ptcut": 23,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.5,
                        },
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.5,
                        },
                    ],
                }
            ),
        },
    )
    ## ET, EE scope trigger setup
    configuration.add_config_parameters(
        ["emt", "met", "ett", "eem"],
        {
            "singleelectron_trigger": EraModifier(
                {
                    "2018": [
                        {
                            "flagname": "trg_single_ele27",
                            "hlt_path": "HLT_Ele27_WPTight_Gsf",
                            "ptcut": 28,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.5,
                        },
                        {
                            "flagname": "trg_single_ele32",
                            "hlt_path": "HLT_Ele32_WPTight_Gsf",
                            "ptcut": 33,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.5,
                        },
                        {
                            "flagname": "trg_single_ele35",
                            "hlt_path": "HLT_Ele35_WPTight_Gsf",
                            "ptcut": 36,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.5,
                        },
                    ],
                    "2017": [
                        {
                            "flagname": "trg_single_ele27",
                            "hlt_path": "HLT_Ele27_WPTight_Gsf",
                            "ptcut": 28,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.5,
                        },
                        {
                            "flagname": "trg_single_ele32",
                            "hlt_path": "HLT_Ele32_WPTight_Gsf",
                            "ptcut": 33,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.5,
                        },
                        {
                            "flagname": "trg_single_ele35",
                            "hlt_path": "HLT_Ele35_WPTight_Gsf",
                            "ptcut": 36,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.5,
                        },
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_single_ele25",
                            "hlt_path": "HLT_Ele25_eta2p1_WPTight_Gsf",
                            "ptcut": 26,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.5,
                        },
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_single_ele25",
                            "hlt_path": "HLT_Ele25_eta2p1_WPTight_Gsf",
                            "ptcut": 26,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.5,
                        },
                    ],
                }
            ),
        },
    )

    return configuration
