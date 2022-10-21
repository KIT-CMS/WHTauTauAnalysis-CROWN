from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup

####################
# Set of producers to get the genParticles from the ditaupair
####################
EMTGenTriple = Producer(
    name="EMTGenTriple",
    call="whtautau_tripleselection::buildgentriple({df}, {input}, {output})",
    input=[
        q.leptontriple,
        nanoAOD.Electron_indexToGen,
        nanoAOD.Muon_indexToGen,
        nanoAOD.Tau_indexToGen,
    ],
    output=[q.gen_leptontriple],
    scopes=["emt", "met"],
)
EMTTrueGenTriple = Producer(
    name="EMTTrueGenTriple",
    call="whtautau_tripleselection::buildtruegentriple({df}, {input}, {output}, {truegen_mother_pdgid_1}, {truegen_mother_pdgid_23},{truegen_daughter_1_pdgid}, {truegen_daugher_2_pdgid}, {truegen_daugher_3_pdgid})",
    input=[
        nanoAOD.GenParticle_statusFlags,
        nanoAOD.GenParticle_status,
        nanoAOD.GenParticle_pdgId,
        nanoAOD.GenParticle_motheridx,
        nanoAOD.GenParticle_pt,
    ],
    output=[q.truegentriple],
    scopes=["emt", "met"],
)
####################
# Set of general producers for Gen DiTauPair Quantities
####################
LVGenParticle1 = Producer(
    name="LVGenParticle1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.gen_leptontriple,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_1],
    scopes=["emt", "met"],
)
LVGenParticle2 = Producer(
    name="LVGenParticle2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.gen_leptontriple,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_2],
    scopes=["emt", "met"],
)
LVGenParticle3 = Producer(
    name="LVGenParticle3",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.gen_leptontriple,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_3],
    scopes=["emt", "met"],
)
LVTrueGenParticle1 = Producer(
    name="LVTrueGenParticle1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.truegenpair,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_1],
    scopes=["mt", "et", "tt", "em", "mm", "ee"],
)
LVTrueGenParticle_WH1 = Producer(
    name="LVTrueGenParticleWH1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.truegentriple,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_1],
    scopes=["emt", "met"],
)
LVTrueGenParticle2 = Producer(
    name="LVTrueGenParticle2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.truegenpair,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_2],
    scopes=["mt", "et", "tt", "em", "mm"],
)
LVTrueGenParticleWH2 = Producer(
    name="LVTrueGenParticleWH2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.truegentriple,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_2],
    scopes=["emt", "met"],
)
LVTrueGenParticleWH3 = Producer(
    name="LVTrueGenParticleWH3",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.truegentriple,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_3],
    scopes=["emt", "met"],
)
gen_pt_1 = Producer(
    name="gen_pt_1",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.gen_p4_1],
    output=[q.gen_pt_1],
    scopes=["mt", "et", "tt", "em", "mm", "emt", "met"],
)
gen_pt_2 = Producer(
    name="gen_pt_2",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.gen_p4_2],
    output=[q.gen_pt_2],
    scopes=["mt", "et", "tt", "em", "mm", "emt", "met"],
)
gen_pt_3 = Producer(
    name="gen_pt_3",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.gen_p4_3],
    output=[q.gen_pt_3],
    scopes=["emt", "met"],
)
gen_eta_1 = Producer(
    name="gen_eta_1",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.gen_p4_1],
    output=[q.gen_eta_1],
    scopes=["mt", "et", "tt", "em", "mm", "emt", "met"],
)
gen_eta_2 = Producer(
    name="gen_eta_2",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.gen_p4_2],
    output=[q.gen_eta_2],
    scopes=["mt", "et", "tt", "em", "mm", "emt", "met"],
)
gen_eta_3 = Producer(
    name="gen_eta_3",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.gen_p4_3],
    output=[q.gen_eta_3],
    scopes=["emt", "met"],
)
gen_phi_1 = Producer(
    name="gen_phi_1",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.gen_p4_1],
    output=[q.gen_phi_1],
    scopes=["mt", "et", "tt", "em", "mm", "emt", "met", "met"],
)
gen_phi_2 = Producer(
    name="gen_phi_2",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.gen_p4_2],
    output=[q.gen_phi_2],
    scopes=["mt", "et", "tt", "em", "mm", "emt", "met"],
)
gen_phi_3 = Producer(
    name="gen_phi_2",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.gen_p4_3],
    output=[q.gen_phi_3],
    scopes=["emt", "met"],
)
gen_mass_1 = Producer(
    name="gen_mass_1",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.gen_p4_1],
    output=[q.gen_mass_1],
    scopes=["mt", "et", "tt", "em", "mm", "emt", "met"],
)
gen_mass_2 = Producer(
    name="gen_mass_2",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.gen_p4_2],
    output=[q.gen_mass_2],
    scopes=["mt", "et", "tt", "em", "mm", "emt", "met"],
)
gen_mass_3 = Producer(
    name="gen_mass_3",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.gen_p4_3],
    output=[q.gen_mass_3],
    scopes=["emt", "met"],
)
gen_pdgid_1 = Producer(
    name="gen_pdgid_1",
    call="quantities::pdgid({df}, {output}, 0, {input})",
    input=[q.gen_dileptonpair, nanoAOD.GenParticle_pdgId],
    output=[q.gen_pdgid_1],
    scopes=["mt", "et", "tt", "em", "mm"],
)
gen_pdgid_WH_1 = Producer(
    name="gen_pdgid_WH_1",
    call="quantities::pdgid({df}, {output}, 0, {input})",
    input=[q.gen_leptontriple, nanoAOD.GenParticle_pdgId],
    output=[q.gen_pdgid_1],
    scopes=["emt", "met"],
)
gen_pdgid_2 = Producer(
    name="gen_pdgid_2",
    call="quantities::pdgid({df}, {output}, 1, {input})",
    input=[q.gen_dileptonpair, nanoAOD.GenParticle_pdgId],
    output=[q.gen_pdgid_2],
    scopes=["mt", "et", "tt", "em", "mm", "emt", "met"],
)
gen_pdgid_WH_2 = Producer(
    name="gen_pdgid_WH_2",
    call="quantities::pdgid({df}, {output}, 1, {input})",
    input=[q.gen_leptontriple, nanoAOD.GenParticle_pdgId],
    output=[q.gen_pdgid_2],
    scopes=["emt", "met"],
)
gen_pdgid_WH_3 = Producer(
    name="gen_pdgid_WH_3",
    call="quantities::pdgid({df}, {output}, 2, {input})",
    input=[q.gen_leptontriple, nanoAOD.GenParticle_pdgId],
    output=[q.gen_pdgid_3],
    scopes=["emt", "met"],
)
gen_m_vis_WH = Producer(
    name="gen_m_vis_WH",
    call="quantities::m_vis({df}, {output}, {input_vec})",
    input=[q.gen_p4_2, q.gen_p4_3],
    output=[q.gen_m_vis],
    scopes=["emt", "met"],
)
gen_taujet_WH_pt_3 = Producer(
    name="gen_taujet_WH_pt_3",
    call="quantities::tau::matching_genjet_pt({df}, {output}, 2, {input})",
    input=[
        q.leptontriple,
        nanoAOD.Tau_associatedJet,
        nanoAOD.Jet_associatedGenJet,
        nanoAOD.GenJet_pt,
    ],
    output=[q.gen_taujet_pt_3],
    scopes=["emt", "met"],
)
UnrollGenMuLV2 = ProducerGroup(
    name="UnrollGenMuLV2",
    call=None,
    input=None,
    output=None,
    scopes=["emt"],
    subproducers=[gen_pt_2, gen_eta_2, gen_phi_2, gen_mass_2, gen_pdgid_WH_2],
)
UnrollGenElLV1 = ProducerGroup(
    name="UnrollGenElLV1",
    call=None,
    input=None,
    output=None,
    scopes=["emt"],
    subproducers=[gen_pt_1, gen_eta_1, gen_phi_1, gen_mass_1, gen_pdgid_WH_1],
)
UnrollGenMuLV1 = ProducerGroup(
    name="UnrollGenMuLV1",
    call=None,
    input=None,
    output=None,
    scopes=["met"],
    subproducers=[gen_pt_1, gen_eta_1, gen_phi_1, gen_mass_1, gen_pdgid_WH_1],
)
UnrollGenElLV2 = ProducerGroup(
    name="UnrollGenElLV2",
    call=None,
    input=None,
    output=None,
    scopes=["met"],
    subproducers=[gen_pt_2, gen_eta_2, gen_phi_2, gen_mass_2, gen_pdgid_WH_2],
)
UnrollGenTauLV3 = ProducerGroup(
    name="UnrollGenLV3",
    call=None,
    input=None,
    output=None,
    scopes=["emt", "met"],
    subproducers=[
        gen_pt_3,
        gen_eta_3,
        gen_phi_3,
        gen_mass_3,
        gen_pdgid_WH_3,
        gen_taujet_WH_pt_3,
    ],
)
EMTGenTripleQuantities = ProducerGroup(
    name="EMTGenTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["emt"],
    subproducers=[
        EMTGenTriple,
        LVGenParticle1,
        LVGenParticle2,
        LVGenParticle3,
        UnrollGenElLV1,
        UnrollGenMuLV2,
        UnrollGenTauLV3,
        gen_m_vis_WH,
    ],
)
METGenTripleQuantities = ProducerGroup(
    name="METGenTripleQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["met"],
    subproducers=[
        EMTGenTriple,
        LVGenParticle1,
        LVGenParticle2,
        LVGenParticle3,
        UnrollGenElLV2,
        UnrollGenMuLV1,
        UnrollGenTauLV3,
        gen_m_vis_WH,
    ],
)
#######################
# DiTau Genmatching
#######################

GenPairForGenMatching = Producer(
    name="GenPairForGenMatching",
    call="genmatching::tau::hadronicGenTaus({df}, {output}, {input})",
    input=[
        nanoAOD.GenParticle_pdgId,
        nanoAOD.GenParticle_statusFlags,
        nanoAOD.GenParticle_motheridx,
    ],
    output=[q.hadronic_gen_taus],
    scopes=["mt", "et", "tt", "em", "ee", "mm", "emt", "met"],
)
GenMatchP1 = Producer(
    name="GenMatchP1",
    call="genmatching::tau::genmatching({df}, {output}, {input})",
    input=[
        q.hadronic_gen_taus,
        nanoAOD.GenParticle_pdgId,
        nanoAOD.GenParticle_statusFlags,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
        nanoAOD.GenParticle_motheridx,
        nanoAOD.GenParticle_status,
        q.p4_1,
    ],
    output=[q.gen_match_1],
    scopes=["mt", "et", "tt", "em", "ee", "mm", "emt", "met"],
)

GenMatchP2 = Producer(
    name="GenMatchP2",
    call="genmatching::tau::genmatching({df}, {output}, {input})",
    input=[
        q.hadronic_gen_taus,
        nanoAOD.GenParticle_pdgId,
        nanoAOD.GenParticle_statusFlags,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
        nanoAOD.GenParticle_motheridx,
        nanoAOD.GenParticle_status,
        q.p4_2,
    ],
    output=[q.gen_match_2],
    scopes=["mt", "et", "tt", "em", "ee", "mm", "emt", "met"],
)

GenMatchP3 = Producer(
    name="GenMatch_WH_P3",
    call="genmatching::tau::genmatching({df}, {output}, {input})",
    input=[
        q.hadronic_gen_taus,
        nanoAOD.GenParticle_pdgId,
        nanoAOD.GenParticle_statusFlags,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
        nanoAOD.GenParticle_motheridx,
        nanoAOD.GenParticle_status,
        q.p4_3,
    ],
    output=[q.gen_match_3],
    scopes=["emt", "met"],
)

# GenMatching = ProducerGroup(
#     name="GenMatching",
#     call=None,
#     input=None,
#     output=None,
#     scopes=["mt", "et", "tt", "em", "ee", "mm"],
#     subproducers=[
#         GenPairForGenMatching,
#         GenMatchP1,
#         GenMatchP2,
#     ],
# )
GenMatching = ProducerGroup(
    name="GenMatching",
    call=None,
    input=None,
    output=None,
    scopes=["emt", "met"],
    subproducers=[
        GenPairForGenMatching,
        GenMatchP1,
        GenMatchP2,
        GenMatchP3,
    ],
)
