from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, Filter

####################
# Set of producers used for contruction of MT good pairs and the coressponding lorentz vectors
####################

EMTTripleSelection = Producer(
    name="EMTTripleSelection",
    call="whtautau_tripleselection::elemutau::TripleSelection({df}, {input_vec}, {output}, {tripleselection_min_dR_leptau}, {tripleselection_min_dR_leplep})",
    input=[
        q.Tau_pt_corrected,
        nanoAOD.Tau_eta,
        nanoAOD.Tau_phi,
        nanoAOD.Tau_mass,
        nanoAOD.Tau_IDraw,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        q.good_electrons_mask,
        q.good_muons_mask,
        q.good_taus_mask,
    ],
    output=[q.leptontriple],
    scopes=["emt"],
)
METTripleSelection = Producer(
    name="METTripleSelection",
    call="whtautau_tripleselection::mueletau::TripleSelection({df}, {input_vec}, {output}, {tripleselection_min_dR_leptau}, {tripleselection_min_dR_leplep})",
    input=[
        q.Tau_pt_corrected,
        nanoAOD.Tau_eta,
        nanoAOD.Tau_phi,
        nanoAOD.Tau_mass,
        nanoAOD.Tau_IDraw,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        q.good_electrons_mask,
        q.good_muons_mask,
        q.good_taus_mask,
    ],
    output=[q.leptontriple],
    scopes=["met"],
)
EMTTripleSelectionWOEle = Producer(
    name="EMTTripleSelectionWOEle",
    call="whtautau_tripleselection::elemutau::TripleSelectionWOEle({df}, {input_vec}, {output}, {tripleselection_min_dR_leptau})",
    input=[
        q.Tau_pt_corrected,
        nanoAOD.Tau_eta,
        nanoAOD.Tau_phi,
        nanoAOD.Tau_mass,
        nanoAOD.Tau_IDraw,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
        nanoAOD.Electron_iso,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        q.good_electrons_mask,
        q.good_muons_mask,
        q.good_taus_mask,
    ],
    output=[q.leptontriple],
    scopes=["emt"],
)

GoodTripleFlag = Producer(
    name="GoodTripleFlag",
    call="whtautau_tripleselection::flagGoodTriples({df}, {output}, {input})",
    input=[q.leptontriple],
    output=[],
    scopes=["emt", "met"],
)

GoodTripleFilter = Filter(
    name="GoodTripleFilter",
    call='basefunctions::FilterFlagsAny({df}, "GoodTriples", {input})',
    input=[],
    scopes=["emt", "met"],
    subproducers=[GoodTripleFlag],
)
LVMu1 = Producer(
    name="LVMu2",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.p4_1],
    scopes=["met"],
)
LVMu2 = Producer(
    name="LVMu2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.p4_2],
    scopes=["emt"],
)
LVEl2 = Producer(
    name="LVEl2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[q.p4_2],
    scopes=["met"],
)
LVEl1 = Producer(
    name="LVEl1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[q.p4_1],
    scopes=["emt"],
)
LVTau3 = Producer(
    name="LVTau3",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.leptontriple,
        q.Tau_pt_corrected,
        nanoAOD.Tau_eta,
        nanoAOD.Tau_phi,
        q.Tau_mass_corrected,
    ],
    output=[q.p4_3],
    scopes=["emt", "met"],
)
## uncorrected versions of all particles, used for MET propagation
LVMu1Uncorrected = Producer(
    name="LVMu1Uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.p4_1_uncorrected],
    scopes=["met"],
)
LVMu2Uncorrected = Producer(
    name="LVMu2Uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
    ],
    output=[q.p4_2_uncorrected],
    scopes=["emt"],
)
LVEl2Uncorrected = Producer(
    name="LVEl1Uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[q.p4_2_uncorrected],
    scopes=["met"],
)
LVEl1Uncorrected = Producer(
    name="LVEl1Uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[q.p4_1_uncorrected],
    scopes=["emt"],
)
LVTau3Uncorrected = Producer(
    name="LVTau3Uncorrected",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Tau_pt,
        nanoAOD.Tau_eta,
        nanoAOD.Tau_phi,
        nanoAOD.Tau_mass,
    ],
    output=[q.p4_3_uncorrected],
    scopes=["emt", "met"],
)
