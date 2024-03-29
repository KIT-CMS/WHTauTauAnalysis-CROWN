from code_generation.configuration import Configuration
from code_generation.systematics import SystematicShift
from .producers import scalefactors as scalefactors
from .producers import tripleselection as tripleselection
from .producers import muons as muons
from .producers import electrons as electrons
from .producers import taus as taus


def add_tauVariations(configuration: Configuration, sample: str):
    if sample == "embedding" or sample == "embedding_mc" or sample == "data":
        return configuration
    #########################
    # TauvsMuID scale factor shifts
    #########################
    # vsJet shifts et/mt, tau pt dependent
    configuration.add_shift(
        SystematicShift(
            name="vsJetTau30to35Down",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsjet_tau30to35": "down"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsJetTauID_lt_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsJetTau30to35Up",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsjet_tau30to35": "up"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsJetTauID_lt_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsJetTau35to40Down",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsjet_tau35to40": "down"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsJetTauID_lt_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsJetTau35to40Up",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsjet_tau35to40": "up"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsJetTauID_lt_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsJetTau40to500Down",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsjet_tau40to500": "down"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsJetTauID_lt_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsJetTau40to500Up",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsjet_tau40to500": "up"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsJetTauID_lt_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsJetTau500to1000Down",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsjet_tau500to1000": "down"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsJetTauID_lt_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsJetTau500to1000Up",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsjet_tau500to1000": "up"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsJetTauID_lt_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsJetTau1000toInfDown",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsjet_tau1000toinf": "down"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsJetTauID_lt_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsJetTau1000toInfUp",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsjet_tau1000toinf": "up"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsJetTauID_lt_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsJetTauDM0Down",
            shift_config={("ett", "mtt"): {"tau_sf_vsjet_tauDM0": "down"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsJetTauID_tt_SF,
                    scalefactors.Tau_2_VsJetTauID_tt_SF,
                ]
            },
        )
    )
    # vsJet shifts tt, tau dm dependent
    configuration.add_shift(
        SystematicShift(
            name="vsJetTauDM0Up",
            shift_config={("ett", "mtt"): {"tau_sf_vsjet_tauDM0": "up"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsJetTauID_tt_SF,
                    scalefactors.Tau_2_VsJetTauID_tt_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsJetTauDM1Down",
            shift_config={("ett", "mtt"): {"tau_sf_vsjet_tauDM1": "down"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsJetTauID_tt_SF,
                    scalefactors.Tau_2_VsJetTauID_tt_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsJetTauDM1Up",
            shift_config={("ett", "mtt"): {"tau_sf_vsjet_tauDM1": "up"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsJetTauID_tt_SF,
                    scalefactors.Tau_2_VsJetTauID_tt_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsJetTauDM10Down",
            shift_config={("ett", "mtt"): {"tau_sf_vsjet_tauDM10": "down"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsJetTauID_tt_SF,
                    scalefactors.Tau_2_VsJetTauID_tt_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsJetTauDM10Up",
            shift_config={("ett", "mtt"): {"tau_sf_vsjet_tauDM10": "up"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsJetTauID_tt_SF,
                    scalefactors.Tau_2_VsJetTauID_tt_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsJetTauDM11Down",
            shift_config={("ett", "mtt"): {"tau_sf_vsjet_tauDM11": "down"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsJetTauID_tt_SF,
                    scalefactors.Tau_2_VsJetTauID_tt_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsJetTauDM11Up",
            shift_config={("ett", "mtt"): {"tau_sf_vsjet_tauDM11": "up"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsJetTauID_tt_SF,
                    scalefactors.Tau_2_VsJetTauID_tt_SF,
                ]
            },
        )
    )
    #########################
    # TauvsEleID scale factor shifts
    #########################
    configuration.add_shift(
        SystematicShift(
            name="vsEleBarrelDown",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsele_barrel": "down"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsEleTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsEleBarrelUp",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsele_barrel": "up"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsEleTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsEleEndcapDown",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsele_endcap": "down"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsEleTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsEleEndcapUp",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsele_endcap": "up"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsEleTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsEleBarrelDown",
            shift_config={("ett", "mtt"): {"tau_sf_vsele_barrel": "down"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsEleTauID_SF,
                    scalefactors.Tau_2_VsEleTauID_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsEleBarrelUp",
            shift_config={("ett", "mtt"): {"tau_sf_vsele_barrel": "up"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsEleTauID_SF,
                    scalefactors.Tau_2_VsEleTauID_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsEleEndcapDown",
            shift_config={("ett", "mtt"): {"tau_sf_vsele_endcap": "down"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsEleTauID_SF,
                    scalefactors.Tau_2_VsEleTauID_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsEleEndcapUp",
            shift_config={("ett", "mtt"): {"tau_sf_vsele_endcap": "up"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsEleTauID_SF,
                    scalefactors.Tau_2_VsEleTauID_SF,
                ]
            },
        )
    )
    #########################
    # TauvsMuID scale factor shifts
    #########################
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel1Down",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsmu_wheel1": "down"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel1Up",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsmu_wheel1": "up"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel2Down",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsmu_wheel2": "down"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel2Up",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsmu_wheel2": "up"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel3Down",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsmu_wheel3": "down"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel3Up",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsmu_wheel3": "up"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel4Down",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsmu_wheel4": "down"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel4Up",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsmu_wheel4": "up"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel5Down",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsmu_wheel5": "down"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel5Up",
            shift_config={("emt", "met", "mmt"): {"tau_sf_vsmu_wheel5": "up"}},
            producers={("emt", "met", "mmt"): scalefactors.Tau_3_VsMuTauID_SF},
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel1Down",
            shift_config={("ett", "mtt"): {"tau_sf_vsmu_wheel1": "down"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsMuTauID_SF,
                    scalefactors.Tau_2_VsMuTauID_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel1Up",
            shift_config={("ett", "mtt"): {"tau_sf_vsmu_wheel1": "up"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsMuTauID_SF,
                    scalefactors.Tau_2_VsMuTauID_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel2Down",
            shift_config={("ett", "mtt"): {"tau_sf_vsmu_wheel2": "down"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsMuTauID_SF,
                    scalefactors.Tau_2_VsMuTauID_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel2Up",
            shift_config={("ett", "mtt"): {"tau_sf_vsmu_wheel2": "up"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsMuTauID_SF,
                    scalefactors.Tau_2_VsMuTauID_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel3Down",
            shift_config={("ett", "mtt"): {"tau_sf_vsmu_wheel3": "down"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsMuTauID_SF,
                    scalefactors.Tau_2_VsMuTauID_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel3Up",
            shift_config={("ett", "mtt"): {"tau_sf_vsmu_wheel3": "up"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsMuTauID_SF,
                    scalefactors.Tau_2_VsMuTauID_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel4Down",
            shift_config={("ett", "mtt"): {"tau_sf_vsmu_wheel4": "down"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsMuTauID_SF,
                    scalefactors.Tau_2_VsMuTauID_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel4Up",
            shift_config={("ett", "mtt"): {"tau_sf_vsmu_wheel4": "up"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsMuTauID_SF,
                    scalefactors.Tau_2_VsMuTauID_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel5Down",
            shift_config={("ett", "mtt"): {"tau_sf_vsmu_wheel5": "down"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsMuTauID_SF,
                    scalefactors.Tau_2_VsMuTauID_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="vsMuWheel5Up",
            shift_config={("ett", "mtt"): {"tau_sf_vsmu_wheel5": "up"}},
            producers={
                ("ett", "mtt"): [
                    scalefactors.Tau_3_VsMuTauID_SF,
                    scalefactors.Tau_2_VsMuTauID_SF,
                ]
            },
        )
    )
    #########################
    # TES Shifts
    #########################
    configuration.add_shift(
        SystematicShift(
            name="tauEs1prong0pizeroDown",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {"tau_ES_shift_DM0": "down"}
            },
            producers={
                ("emt", "met", "mmt", "mtt", "ett"): taus.TauPtCorrection_genTau
            },
            ignore_producers={
                "emt": [
                    tripleselection.LVEl1,
                    tripleselection.LVMu2,
                    electrons.VetoElectrons,
                    muons.VetoMuons,
                ],
                "met": [
                    tripleselection.LVMu1,
                    tripleselection.LVEl2,
                    muons.VetoMuons,
                    electrons.VetoElectrons,
                ],
                "mmt": [
                    tripleselection.LVMu1,
                    tripleselection.LVMu2,
                    muons.VetoMuons,
                ],
                "mtt": [
                    tripleselection.LVMu1,
                    muons.VetoMuons,
                ],
                "ett": [
                    tripleselection.LVEl1,
                    electrons.VetoElectrons,
                ],
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="tauEs1prong0pizeroUp",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {"tau_ES_shift_DM0": "up"}
            },
            producers={
                ("emt", "met", "mmt", "mtt", "ett"): taus.TauPtCorrection_genTau
            },
            ignore_producers={
                "emt": [
                    tripleselection.LVEl1,
                    tripleselection.LVMu2,
                    electrons.VetoElectrons,
                    muons.VetoMuons,
                ],
                "met": [
                    tripleselection.LVMu1,
                    tripleselection.LVEl2,
                    muons.VetoMuons,
                    electrons.VetoElectrons,
                ],
                "mmt": [
                    tripleselection.LVMu1,
                    tripleselection.LVMu2,
                    muons.VetoMuons,
                ],
                "mtt": [
                    tripleselection.LVMu1,
                    muons.VetoMuons,
                ],
                "ett": [
                    tripleselection.LVEl1,
                    electrons.VetoElectrons,
                ],
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="tauEs1prong1pizeroDown",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {"tau_ES_shift_DM1": "down"}
            },
            producers={
                ("emt", "met", "mmt", "mtt", "ett"): taus.TauPtCorrection_genTau
            },
            ignore_producers={
                "emt": [
                    tripleselection.LVEl1,
                    tripleselection.LVMu2,
                    electrons.VetoElectrons,
                    muons.VetoMuons,
                ],
                "met": [
                    tripleselection.LVMu1,
                    tripleselection.LVEl2,
                    muons.VetoMuons,
                    electrons.VetoElectrons,
                ],
                "mmt": [
                    tripleselection.LVMu1,
                    tripleselection.LVMu2,
                    muons.VetoMuons,
                ],
                "mtt": [
                    tripleselection.LVMu1,
                    muons.VetoMuons,
                ],
                "ett": [
                    tripleselection.LVEl1,
                    electrons.VetoElectrons,
                ],
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="tauEs1prong1pizeroUp",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {"tau_ES_shift_DM1": "up"}
            },
            producers={
                ("emt", "met", "mmt", "mtt", "ett"): taus.TauPtCorrection_genTau
            },
            ignore_producers={
                "emt": [
                    tripleselection.LVEl1,
                    tripleselection.LVMu2,
                    electrons.VetoElectrons,
                    muons.VetoMuons,
                ],
                "met": [
                    tripleselection.LVMu1,
                    tripleselection.LVEl2,
                    muons.VetoMuons,
                    electrons.VetoElectrons,
                ],
                "mmt": [
                    tripleselection.LVMu1,
                    tripleselection.LVMu2,
                    muons.VetoMuons,
                ],
                "mtt": [
                    tripleselection.LVMu1,
                    muons.VetoMuons,
                ],
                "ett": [
                    tripleselection.LVEl1,
                    electrons.VetoElectrons,
                ],
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="tauEs3prong0pizeroDown",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {"tau_ES_shift_DM10": "down"}
            },
            producers={
                ("emt", "met", "mmt", "mtt", "ett"): taus.TauPtCorrection_genTau
            },
            ignore_producers={
                "emt": [
                    tripleselection.LVEl1,
                    tripleselection.LVMu2,
                    electrons.VetoElectrons,
                    muons.VetoMuons,
                ],
                "met": [
                    tripleselection.LVMu1,
                    tripleselection.LVEl2,
                    muons.VetoMuons,
                    electrons.VetoElectrons,
                ],
                "mmt": [
                    tripleselection.LVMu1,
                    tripleselection.LVMu2,
                    muons.VetoMuons,
                ],
                "mtt": [
                    tripleselection.LVMu1,
                    muons.VetoMuons,
                ],
                "ett": [
                    tripleselection.LVEl1,
                    electrons.VetoElectrons,
                ],
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="tauEs3prong0pizeroUp",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {"tau_ES_shift_DM10": "up"}
            },
            producers={
                ("emt", "met", "mmt", "mtt", "ett"): taus.TauPtCorrection_genTau
            },
            ignore_producers={
                "emt": [
                    tripleselection.LVEl1,
                    tripleselection.LVMu2,
                    electrons.VetoElectrons,
                    muons.VetoMuons,
                ],
                "met": [
                    tripleselection.LVMu1,
                    tripleselection.LVEl2,
                    muons.VetoMuons,
                    electrons.VetoElectrons,
                ],
                "mmt": [
                    tripleselection.LVMu1,
                    tripleselection.LVMu2,
                    muons.VetoMuons,
                ],
                "mtt": [
                    tripleselection.LVMu1,
                    muons.VetoMuons,
                ],
                "ett": [
                    tripleselection.LVEl1,
                    electrons.VetoElectrons,
                ],
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="tauEs3prong1pizeroDown",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {"tau_ES_shift_DM11": "down"}
            },
            producers={
                ("emt", "met", "mmt", "mtt", "ett"): taus.TauPtCorrection_genTau
            },
            ignore_producers={
                "emt": [
                    tripleselection.LVEl1,
                    tripleselection.LVMu2,
                    electrons.VetoElectrons,
                    muons.VetoMuons,
                ],
                "met": [
                    tripleselection.LVMu1,
                    tripleselection.LVEl2,
                    muons.VetoMuons,
                    electrons.VetoElectrons,
                ],
                "mmt": [
                    tripleselection.LVMu1,
                    tripleselection.LVMu2,
                    muons.VetoMuons,
                ],
                "mtt": [
                    tripleselection.LVMu1,
                    muons.VetoMuons,
                ],
                "ett": [
                    tripleselection.LVEl1,
                    electrons.VetoElectrons,
                ],
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="tauEs3prong1pizeroUp",
            shift_config={
                ("emt", "met", "mmt", "mtt", "ett"): {"tau_ES_shift_DM11": "up"}
            },
            producers={
                ("emt", "met", "mmt", "mtt", "ett"): taus.TauPtCorrection_genTau
            },
            ignore_producers={
                "emt": [
                    tripleselection.LVEl1,
                    tripleselection.LVMu2,
                    electrons.VetoElectrons,
                    muons.VetoMuons,
                ],
                "met": [
                    tripleselection.LVMu1,
                    tripleselection.LVEl2,
                    muons.VetoMuons,
                    electrons.VetoElectrons,
                ],
                "mmt": [
                    tripleselection.LVMu1,
                    tripleselection.LVMu2,
                    muons.VetoMuons,
                ],
                "mtt": [
                    tripleselection.LVMu1,
                    muons.VetoMuons,
                ],
                "ett": [
                    tripleselection.LVEl1,
                    electrons.VetoElectrons,
                ],
            },
        )
    )

    return configuration
