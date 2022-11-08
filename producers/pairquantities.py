from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup, ExtendedVectorProducer


####################
# Set of general producers for DiTauPair Quantities
####################

pt_1 = Producer(
    name="pt_1",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.p4_1],
    output=[q.pt_1],
    scopes=["mt", "et", "tt", "em", "ee", "mm", "emt", "met", "mmt"],
)
pt_2 = Producer(
    name="pt_2",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.p4_2],
    output=[q.pt_2],
    scopes=["mt", "et", "tt", "em", "ee", "mm", "emt", "met", "mmt"],
)
pt_3 = Producer(
    name="pt_3",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.p4_3],
    output=[q.pt_3],
    scopes=["emt", "met", "mmt"],
)
eta_1 = Producer(
    name="eta_1",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.p4_1],
    output=[q.eta_1],
    scopes=["mt", "et", "tt", "em", "ee", "mm", "emt", "met", "mmt"],
)
eta_2 = Producer(
    name="eta_2",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.p4_2],
    output=[q.eta_2],
    scopes=["mt", "et", "tt", "em", "ee", "mm", "emt", "met", "mmt"],
)
eta_3 = Producer(
    name="eta_3",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.p4_3],
    output=[q.eta_3],
    scopes=["emt", "met", "mmt"],
)
phi_1 = Producer(
    name="phi_1",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.p4_1],
    output=[q.phi_1],
    scopes=["mt", "et", "tt", "em", "ee", "mm", "emt", "met", "mmt"],
)
phi_2 = Producer(
    name="phi_2",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.p4_2],
    output=[q.phi_2],
    scopes=["mt", "et", "tt", "em", "ee", "mm", "emt", "met", "mmt"],
)
phi_3 = Producer(
    name="phi_3",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.p4_3],
    output=[q.phi_3],
    scopes=["emt", "met", "mmt"],
)
mass_1 = Producer(
    name="mass_1",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.p4_1],
    output=[q.mass_1],
    scopes=["emt", "met", "mmt"],
)
mass_2 = Producer(
    name="mass_2",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.p4_2],
    output=[q.mass_2],
    scopes=["mt", "et", "tt", "em", "ee", "mm", "emt", "met", "mmt"],
)
mass_3 = Producer(
    name="mass_3",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.p4_3],
    output=[q.mass_3],
    scopes=["emt", "met", "mmt"],
)
m_vis = Producer(
    name="m_vis",
    call="quantities::m_vis({df}, {output}, {input_vec})",
    input=[q.p4_2, q.p4_3],
    output=[q.m_vis],
    scopes=["emt", "met", "mmt"],
)
pt_vis = Producer(
    name="pt_vis",
    call="quantities::pt_vis({df}, {output}, {input_vec})",
    input=[q.p4_2, q.p4_3],
    output=[q.pt_vis],
    scopes=["emt", "met", "mmt"],
)
p4_miss_lt = Producer(
    name="p4_miss_lt",
    call="lorentzvectors::p4_miss_lt({df}, {output}, {input_vec})",
    input=[q.p4_2, q.p4_3],
    output=[q.p4_miss_lt],
    scopes=["emt", "met", "mmt"],
)
m_tt_lt = Producer(
    name="mt_tt_lt",
    call="quantities::m_tt_lt({df}, {output}, {input_vec})",
    input=[q.p4_2, q.p4_3, q.p4_miss_lt],
    output=[q.m_tt_lt],
    scopes=["emt", "met", "mmt"],
)
pt_W_lt = Producer(
    name="pt_W_lt",
    call="quantities::pt_W_lt({df}, {output}, {input_vec})",
    input=[q.p4_1, q.met_p4_recoilcorrected, q.p4_miss_lt],
    output=[q.pt_W_lt],
    scopes=["emt", "met", "mmt"],
)
deltaR_ditaupair = Producer(
    name="deltaR_ditaupair",
    call="quantities::deltaR({df}, {output}, {input})",
    input=[q.p4_1, q.p4_2],
    output=[q.deltaR_ditaupair],
    scopes=["mt", "et", "tt", "em", "ee", "mm"],
)
deltaR_13 = Producer(
    name="deltaR_13",
    call="quantities::deltaR({df}, {output}, {input})",
    input=[q.p4_1, q.p4_3],
    output=[q.deltaR_13],
    scopes=["emt", "met", "mmt"],
)
deltaR_23 = Producer(
    name="deltaR_23",
    call="quantities::deltaR({df}, {output}, {input})",
    input=[q.p4_2, q.p4_3],
    output=[q.deltaR_23],
    scopes=["emt", "met", "mmt"],
)
deltaR_12 = Producer(
    name="deltaR_12",
    call="quantities::deltaR({df}, {output}, {input})",
    input=[q.p4_1, q.p4_2],
    output=[q.deltaR_12],
    scopes=["emt", "met", "mmt"],
)
deltaPhi_12 = Producer(
    name="deltaPhi_12",
    call="quantities::deltaPhi({df}, {output}, {input})",
    input=[q.p4_1, q.p4_2],
    output=[q.deltaPhi_12],
    scopes=["emt", "met", "mmt"],
)
deltaPhi_13 = Producer(
    name="deltaPhi_13",
    call="quantities::deltaPhi({df}, {output}, {input})",
    input=[q.p4_1, q.p4_3],
    output=[q.deltaPhi_13],
    scopes=["emt", "met", "mmt"],
)
deltaPhi_WH = Producer(
    name="deltaPhi_WH",
    call="quantities::deltaPhi_WH({df}, {output}, {input})",
    input=[q.p4_1, q.p4_2, q.p4_3],
    output=[q.deltaPhi_WH],
    scopes=["emt", "met", "mmt"],
)
eta_vis = Producer(
    name="eta_vis",
    call="quantities::eta_vis({df}, {output}, {input_vec})",
    input=[q.p4_2, q.p4_3],
    output=[q.eta_vis],
    scopes=["emt", "met", "mmt"],
)
phi_vis = Producer(
    name="phi_vis",
    call="quantities::phi_vis({df}, {output}, {input_vec})",
    input=[q.p4_2, q.p4_3],
    output=[q.phi_vis],
    scopes=["emt", "met", "mmt"],
)
Lt = Producer(
    name="Lt",
    call="quantities::Lt({df}, {output}, {input})",
    input=[q.pt_1, q.pt_2, q.pt_3],
    output=[q.Lt],
    scopes=["emt", "met", "mmt"],
)

####################
# Set of channel specific producers
####################
muon_dxy_wh_1 = Producer(
    name="muon_dxy_wh_1",
    call="quantities::dxy({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Muon_dxy],
    output=[q.dxy_1],
    scopes=["met", "mmt"],
)
muon_dxy_wh_2 = Producer(
    name="muon_dxy_wh_2",
    call="quantities::dxy({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Muon_dxy],
    output=[q.dxy_2],
    scopes=["emt", "mmt"],
)
muon_is_global_wh_1 = Producer(
    name="muon_is_global_wh_1",
    call="quantities::muon::is_global({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Muon_isGlobal],
    output=[q.is_global_1],
    scopes=["met", "mmt"],
)
muon_is_global_wh_2 = Producer(
    name="muon_is_global_wh_2",
    call="quantities::muon::is_global({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Muon_isGlobal],
    output=[q.is_global_2],
    scopes=["emt", "mmt"],
)
electron_dxy_wh_1 = Producer(
    name="electron_dxy_1",
    call="quantities::dxy({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Electron_dxy],
    output=[q.dxy_1],
    scopes=["emt"],
)
electron_dxy_wh_2 = Producer(
    name="electron_dxy_2",
    call="quantities::dxy({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Electron_dxy],
    output=[q.dxy_2],
    scopes=["met"],
)
tau_dxy_3 = Producer(
    name="tau_dxy_3",
    call="quantities::dxy({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Tau_dxy],
    output=[q.dxy_3],
    scopes=["emt", "met", "mmt"],
)
muon_dz_wh_1 = Producer(
    name="muon_dz_wh_1",
    call="quantities::dz({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Muon_dz],
    output=[q.dz_1],
    scopes=["met", "mmt"],
)
muon_dz_wh_2 = Producer(
    name="muon_dz_wh_2",
    call="quantities::dz({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Muon_dz],
    output=[q.dz_2],
    scopes=["emt", "mmt"],
)
electron_dz_wh_1 = Producer(
    name="electron_dz_wh_1",
    call="quantities::dz({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Electron_dz],
    output=[q.dz_1],
    scopes=["emt"],
)
electron_dz_wh_2 = Producer(
    name="electron_dz_wh_2",
    call="quantities::dz({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Electron_dz],
    output=[q.dz_2],
    scopes=["met"],
)
tau_dz_3 = Producer(
    name="tau_dz_3",
    call="quantities::dz({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Tau_dz],
    output=[q.dz_3],
    scopes=["emt", "met", "mmt"],
)
muon_q_wh_1 = Producer(
    name="muon_q_wh_1",
    call="quantities::charge({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Muon_charge],
    output=[q.q_1],
    scopes=["met", "mmt"],
)
muon_q_wh_2 = Producer(
    name="muon_q_wh_2",
    call="quantities::charge({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Muon_charge],
    output=[q.q_2],
    scopes=["emt", "mmt"],
)
electron_q_wh_1 = Producer(
    name="electron_q_wh_1",
    call="quantities::charge({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Electron_charge],
    output=[q.q_1],
    scopes=["emt"],
)
electron_q_wh_2 = Producer(
    name="electron_q_wh_2",
    call="quantities::charge({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Electron_charge],
    output=[q.q_2],
    scopes=["met"],
)
tau_q_3 = Producer(
    name="tau_q_3",
    call="quantities::charge({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Tau_charge],
    output=[q.q_3],
    scopes=["emt", "met", "mmt"],
)
muon_iso_wh_1 = Producer(
    name="muon_iso_wh_1",
    call="quantities::isolation({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Muon_iso],
    output=[q.iso_1],
    scopes=["met", "mmt"],
)
muon_iso_wh_2 = Producer(
    name="muon_iso_wh_2",
    call="quantities::isolation({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Muon_iso],
    output=[q.iso_2],
    scopes=["emt", "mmt"],
)
electron_iso_wh_1 = Producer(
    name="electron_iso_wh_1",
    call="quantities::isolation({df}, {output}, 0, {input})",
    input=[q.leptontriple, nanoAOD.Electron_iso],
    output=[q.iso_1],
    scopes=["emt"],
)
electron_iso_wh_2 = Producer(
    name="electron_iso_wh_2",
    call="quantities::isolation({df}, {output}, 1, {input})",
    input=[q.leptontriple, nanoAOD.Electron_iso],
    output=[q.iso_2],
    scopes=["met"],
)
tau_iso_3 = Producer(
    name="tau_iso_3",
    call="quantities::isolation({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Tau_IDraw],
    output=[q.iso_3],
    scopes=["emt", "met", "mmt"],
)
tau_decaymode_3 = Producer(
    name="taudecaymode_3",
    call="quantities::tau::decaymode({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Tau_decayMode],
    output=[q.decaymode_3],
    scopes=["emt", "met", "mmt"],
)
tau_gen_match_3 = Producer(
    name="taugen_match_3",
    call="quantities::tau::genmatch({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Tau_genMatch],
    output=[q.tau_gen_match_3],
    scopes=["emt", "met", "mmt"],
)
taujet_pt_3 = Producer(
    name="taujet_pt_3",
    call="quantities::tau::matching_jet_pt({df}, {output}, 2, {input})",
    input=[q.leptontriple, nanoAOD.Tau_associatedJet, nanoAOD.Jet_pt],
    output=[q.taujet_pt_3],
    scopes=["emt", "met", "mmt"],
)
VsJetTauIDFlag_3 = ExtendedVectorProducer(
    name="VsJetTauIDFlag_3",
    call="quantities::tau::TauIDFlag({df}, {output}, 2, {input}, {vsjet_tau_id_WPbit})",
    input=[q.leptontriple, nanoAOD.Tau_ID_vsJet],
    output="tau_3_vsjet_id_outputname",
    scope=["emt", "met", "mmt"],
    vec_config="vsjet_tau_id",
)
VsEleTauIDFlag_3 = ExtendedVectorProducer(
    name="VsEleTauIDFlag_3",
    call="quantities::tau::TauIDFlag({df}, {output}, 2, {input}, {vsele_tau_id_WPbit})",
    input=[q.leptontriple, nanoAOD.Tau_ID_vsEle],
    output="tau_3_vsele_id_outputname",
    scope=["emt", "met", "mmt"],
    vec_config="vsele_tau_id",
)
VsMuTauIDFlag_3 = ExtendedVectorProducer(
    name="VsMuTauIDFlag_3",
    call="quantities::tau::TauIDFlag({df}, {output}, 2, {input}, {vsmu_tau_id_WPbit})",
    input=[q.leptontriple, nanoAOD.Tau_ID_vsMu],
    output="tau_3_vsmu_id_outputname",
    scope=["emt", "met", "mmt"],
    vec_config="vsmu_tau_id",
)
UnrollMuLV1 = ProducerGroup(
    name="UnrollMuLV1",
    call=None,
    input=None,
    output=None,
    scopes=["met", "mmt"],
    subproducers=[
        pt_1,
        eta_1,
        phi_1,
        mass_1,
        muon_dxy_wh_1,
        muon_dz_wh_1,
        muon_q_wh_1,
        muon_iso_wh_1,
        muon_is_global_wh_1,
    ],
)
UnrollMuLV2 = ProducerGroup(
    name="UnrollMuLV2",
    call=None,
    input=None,
    output=None,
    scopes=["emt", "mmt"],
    subproducers=[
        pt_2,
        eta_2,
        phi_2,
        mass_2,
        muon_dxy_wh_2,
        muon_dz_wh_2,
        muon_q_wh_2,
        muon_iso_wh_2,
        muon_is_global_wh_2,
    ],
)
UnrollElLV1 = ProducerGroup(
    name="UnrollElLV1",
    call=None,
    input=None,
    output=None,
    scopes=["emt"],
    subproducers=[
        pt_1,
        eta_1,
        phi_1,
        mass_1,
        electron_dxy_wh_1,
        electron_dz_wh_1,
        electron_q_wh_1,
        electron_iso_wh_1,
    ],
)
UnrollElLV2 = ProducerGroup(
    name="UnrollElLV2",
    call=None,
    input=None,
    output=None,
    scopes=["met"],
    subproducers=[
        pt_2,
        eta_2,
        phi_2,
        mass_2,
        electron_dxy_wh_2,
        electron_dz_wh_2,
        electron_q_wh_2,
        electron_iso_wh_2,
    ],
)
UnrollTauLV3 = ProducerGroup(
    name="UnrollLV3",
    call=None,
    input=None,
    output=None,
    scopes=["emt", "met", "mmt"],
    subproducers=[
        pt_3,
        eta_3,
        phi_3,
        mass_3,
        tau_dxy_3,
        tau_dz_3,
        tau_q_3,
        tau_iso_3,
        tau_decaymode_3,
        tau_gen_match_3,
        taujet_pt_3,
        VsJetTauIDFlag_3,
        VsEleTauIDFlag_3,
        VsMuTauIDFlag_3,
    ],
)
#####################
# Producer Groups
#####################
EMTTripleQuantities = ProducerGroup(
    name="EMTTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["emt"],
    subproducers=[
        UnrollElLV1,
        UnrollMuLV2,
        UnrollTauLV3,
        m_vis,
        p4_miss_lt,
        m_tt_lt,
        pt_W_lt,
        pt_vis,
        eta_vis,
        phi_vis,
        Lt,
        deltaR_12,
        deltaR_13,
        deltaR_23,
        deltaPhi_12,
        deltaPhi_13,
        deltaPhi_WH,
    ],
)
METTripleQuantities = ProducerGroup(
    name="METTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["met"],
    subproducers=[
        UnrollElLV2,
        UnrollMuLV1,
        UnrollTauLV3,
        m_vis,
        p4_miss_lt,
        m_tt_lt,
        pt_W_lt,
        pt_vis,
        eta_vis,
        phi_vis,
        Lt,
        deltaR_12,
        deltaR_13,
        deltaR_23,
        deltaPhi_12,
        deltaPhi_13,
        deltaPhi_WH,
    ],
)
MMTTripleQuantities = ProducerGroup(
    name="MMTTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["mmt"],
    subproducers=[
        UnrollMuLV2,
        UnrollMuLV1,
        UnrollTauLV3,
        m_vis,
        p4_miss_lt,
        m_tt_lt,
        pt_W_lt,
        pt_vis,
        eta_vis,
        phi_vis,
        Lt,
        deltaR_12,
        deltaR_13,
        deltaR_23,
        deltaPhi_12,
        deltaPhi_13,
        deltaPhi_WH,
    ],
)
## advanced event quantities (can be caluculated when ditau pair and met and all jets are determined)
## leptons: q.p4_1, q.p4_2
## met: met_p4_recoilcorrected
## jets: good_jet_collection (if only the leading two are needed: q.jet_p4_1, q.jet_p4_2
## bjets: gen_bjet_collection

Pzetamissvis = Producer(
    name="Pzetamissvis",
    call="quantities::pzetamissvis({df}, {output}, {input})",
    input=[q.p4_1, q.p4_2, q.met_p4_recoilcorrected],
    output=[q.pzetamissvis],
    scopes=["mt", "et", "tt", "em", "ee", "mm"],
)
mTdileptonMET = Producer(
    name="mTdileptonMET",
    call="quantities::mTdileptonMET({df}, {output}, {input})",
    input=[q.p4_1, q.p4_2, q.met_p4_recoilcorrected],
    output=[q.mTdileptonMET],
    scopes=["mt", "et", "tt", "em", "ee", "mm"],
)
mt_1 = Producer(
    name="mt_1",
    call="quantities::mT({df}, {output}, {input})",
    input=[q.p4_1, q.met_p4_recoilcorrected],
    output=[q.mt_1],
    scopes=["mt", "et", "tt", "em", "ee", "mm", "emt", "met", "mmt"],
)
mt_2 = Producer(
    name="mt_2",
    call="quantities::mT({df}, {output}, {input})",
    input=[q.p4_2, q.met_p4_recoilcorrected],
    output=[q.mt_2],
    scopes=["mt", "et", "tt", "em", "ee", "mm", "emt", "met", "mmt"],
)
mt_3 = Producer(
    name="mt_3",
    call="quantities::mT({df}, {output}, {input})",
    input=[q.p4_3, q.met_p4_recoilcorrected],
    output=[q.mt_3],
    scopes=["emt", "met", "mmt"],
)
mt = ProducerGroup(
    name="mt",
    call=None,
    input=None,
    output=None,
    scopes=["emt", "met", "mmt"],
    subproducers=[mt_1, mt_2, mt_3],
)
