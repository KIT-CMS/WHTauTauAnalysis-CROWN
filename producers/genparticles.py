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
    scopes=["emt"],
)
MTGenPair = Producer(
    name="MTGenPair",
    call="ditau_pairselection::buildgenpair({df}, {input}, {output})",
    input=[q.dileptonpair, nanoAOD.Muon_indexToGen, nanoAOD.Tau_indexToGen],
    output=[q.gen_dileptonpair],
    scopes=["mt"],
)
ETGenPair = Producer(
    name="ETGenPair",
    call="ditau_pairselection::buildgenpair({df}, {input}, {output})",
    input=[q.dileptonpair, nanoAOD.Electron_indexToGen, nanoAOD.Tau_indexToGen],
    output=[q.gen_dileptonpair],
    scopes=["et"],
)
TTGenPair = Producer(
    name="TTGenPair",
    call="ditau_pairselection::buildgenpair({df}, {input}, {output})",
    input=[q.dileptonpair, nanoAOD.Tau_indexToGen, nanoAOD.Tau_indexToGen],
    output=[q.gen_dileptonpair],
    scopes=["tt"],
)
EMGenPair = Producer(
    name="EMGenPair",
    call="ditau_pairselection::buildgenpair({df}, {input}, {output})",
    input=[q.dileptonpair, nanoAOD.Electron_indexToGen, nanoAOD.Muon_indexToGen],
    output=[q.gen_dileptonpair],
    scopes=["em"],
)
MuMuGenPair = Producer(
    name="MuMuGenPair",
    call="ditau_pairselection::buildgenpair({df}, {input}, {output})",
    input=[q.dileptonpair, nanoAOD.Muon_indexToGen, nanoAOD.Muon_indexToGen],
    output=[q.gen_dileptonpair],
    scopes=["mm"],
)
ElElGenPair = Producer(
    name="ElElGenPair",
    call="ditau_pairselection::buildgenpair({df}, {input}, {output})",
    input=[q.dileptonpair, nanoAOD.Electron_indexToGen, nanoAOD.Electron_indexToGen],
    output=[q.gen_dileptonpair],
    scopes=["ee"],
)
MuMuTrueGenPair = Producer(
    name="GenPair",
    call="ditau_pairselection::buildtruegenpair({df}, {input}, {output}, {truegen_mother_pdgid}, {truegen_daughter_1_pdgid}, {truegen_daugher_2_pdgid})",
    input=[
        nanoAOD.GenParticle_statusFlags,
        nanoAOD.GenParticle_status,
        nanoAOD.GenParticle_pdgId,
        nanoAOD.GenParticle_motheridx,
        nanoAOD.GenParticle_pt,
    ],
    output=[q.truegenpair],
    scopes=["mm"],
)
####################
# Set of general producers for Gen DiTauPair Quantities
####################

LVGenParticle1 = Producer(
    name="LVGenParticle1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.gen_dileptonpair,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_1],
    scopes=["mt", "et", "tt", "em", "mm", "ee"],
)
LVGenParticleWH1 = Producer(
    name="LVGenParticleWH1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.gen_leptontriple,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_1],
    scopes=["emt"],
)
LVGenParticle2 = Producer(
    name="LVGenParticle2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.gen_dileptonpair,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_2],
    scopes=["mt", "et", "tt", "em", "mm", "ee"],
)
LVGenParticleWH2 = Producer(
    name="LVGenParticleWH2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.gen_leptontriple,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_2],
    scopes=["emt"],
)
LVGenParticleWH3 = Producer(
    name="LVGenParticleWH3",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.gen_leptontriple,
        nanoAOD.GenParticle_pt,
        nanoAOD.GenParticle_eta,
        nanoAOD.GenParticle_phi,
        nanoAOD.GenParticle_mass,
    ],
    output=[q.gen_p4_3],
    scopes=["emt"],
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
    scopes=["emt"],
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
    scopes=["emt"],
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
    scopes=["emt"],
)
gen_pt_1 = Producer(
    name="gen_pt_1",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.gen_p4_1],
    output=[q.gen_pt_1],
    scopes=["mt", "et", "tt", "em", "mm", "emt"],
)
gen_pt_2 = Producer(
    name="gen_pt_2",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.gen_p4_2],
    output=[q.gen_pt_2],
    scopes=["mt", "et", "tt", "em", "mm", "emt"],
)
gen_pt_3 = Producer(
    name="gen_pt_3",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.gen_p4_3],
    output=[q.gen_pt_3],
    scopes=["emt"],
)
gen_eta_1 = Producer(
    name="gen_eta_1",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.gen_p4_1],
    output=[q.gen_eta_1],
    scopes=["mt", "et", "tt", "em", "mm", "emt"],
)
gen_eta_2 = Producer(
    name="gen_eta_2",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.gen_p4_2],
    output=[q.gen_eta_2],
    scopes=["mt", "et", "tt", "em", "mm", "emt"],
)
gen_eta_3 = Producer(
    name="gen_eta_3",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.gen_p4_3],
    output=[q.gen_eta_3],
    scopes=["emt"],
)
gen_phi_1 = Producer(
    name="gen_phi_1",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.gen_p4_1],
    output=[q.gen_phi_1],
    scopes=["mt", "et", "tt", "em", "mm", "emt"],
)
gen_phi_2 = Producer(
    name="gen_phi_2",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.gen_p4_2],
    output=[q.gen_phi_2],
    scopes=["mt", "et", "tt", "em", "mm", "emt"],
)
gen_phi_3 = Producer(
    name="gen_phi_2",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.gen_p4_3],
    output=[q.gen_phi_3],
    scopes=["emt"],
)
gen_mass_1 = Producer(
    name="gen_mass_1",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.gen_p4_1],
    output=[q.gen_mass_1],
    scopes=["mt", "et", "tt", "em", "mm", "emt"],
)
gen_mass_2 = Producer(
    name="gen_mass_2",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.gen_p4_2],
    output=[q.gen_mass_2],
    scopes=["mt", "et", "tt", "em", "mm", "emt"],
)
gen_mass_3 = Producer(
    name="gen_mass_3",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.gen_p4_3],
    output=[q.gen_mass_3],
    scopes=["emt"],
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
    scopes=["emt"],
)
gen_pdgid_2 = Producer(
    name="gen_pdgid_2",
    call="quantities::pdgid({df}, {output}, 1, {input})",
    input=[q.gen_dileptonpair, nanoAOD.GenParticle_pdgId],
    output=[q.gen_pdgid_2],
    scopes=["mt", "et", "tt", "em", "mm", "emt"],
)
gen_pdgid_WH_2 = Producer(
    name="gen_pdgid_WH_2",
    call="quantities::pdgid({df}, {output}, 1, {input})",
    input=[q.gen_leptontriple, nanoAOD.GenParticle_pdgId],
    output=[q.gen_pdgid_2],
    scopes=["emt"],
)
gen_pdgid_WH_3 = Producer(
    name="gen_pdgid_WH_3",
    call="quantities::pdgid({df}, {output}, 2, {input})",
    input=[q.gen_leptontriple, nanoAOD.GenParticle_pdgId],
    output=[q.gen_pdgid_3],
    scopes=["emt"],
)
gen_m_vis = Producer(
    name="gen_m_vis",
    call="quantities::m_vis({df}, {output}, {input_vec})",
    input=[q.gen_p4_1, q.gen_p4_2],
    output=[q.gen_m_vis],
    scopes=["mt", "et", "tt", "em", "mm"],
)
gen_m_vis_WH = Producer(
    name="gen_m_vis_WH",
    call="quantities::m_vis({df}, {output}, {input_vec})",
    input=[q.gen_p4_2, q.gen_p4_3],
    output=[q.gen_m_vis],
    scopes=["emt"],
)
# gen_match_2 = Producer(
#     name="gen_match_2",
#     call="quantities::tau::genmatch({df}, {output}, 1, {input})",
#     input=[q.dileptonpair, nanoAOD.Tau_genMatch],
#     output=[q.gen_match_2],
#     scopes=["mt", "et", "tt"],
# )
gen_taujet_pt_1 = Producer(
    name="gen_taujet_pt_1",
    call="quantities::tau::matching_genjet_pt({df}, {output}, 0, {input})",
    input=[
        q.dileptonpair,
        nanoAOD.Tau_associatedJet,
        nanoAOD.Jet_associatedGenJet,
        nanoAOD.GenJet_pt,
    ],
    output=[q.gen_taujet_pt_1],
    scopes=["tt"],
)
gen_taujet_pt_2 = Producer(
    name="gen_taujet_pt_2",
    call="quantities::tau::matching_genjet_pt({df}, {output}, 1, {input})",
    input=[
        q.dileptonpair,
        nanoAOD.Tau_associatedJet,
        nanoAOD.Jet_associatedGenJet,
        nanoAOD.GenJet_pt,
    ],
    output=[q.gen_taujet_pt_2],
    scopes=["mt", "et", "tt"],
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
    scopes=["emt"],
)
UnrollGenMuLV1 = ProducerGroup(
    name="UnrollGenMuLV1",
    call=None,
    input=None,
    output=None,
    scopes=["mt", "mm"],
    subproducers=[gen_pt_1, gen_eta_1, gen_phi_1, gen_mass_1, gen_pdgid_1],
)
UnrollGenMuLV2 = ProducerGroup(
    name="UnrollGenMuLV2",
    call=None,
    input=None,
    output=None,
    scopes=["em", "mm"],
    subproducers=[gen_pt_2, gen_eta_2, gen_phi_2, gen_mass_2, gen_pdgid_2],
)
UnrollGenMuWHLV2 = ProducerGroup(
    name="UnrollGenMuWHLV2",
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
    scopes=["em", "ee", "et"],
    subproducers=[gen_pt_1, gen_eta_1, gen_phi_1, gen_mass_1, gen_pdgid_1],
)
UnrollGenElWHLV1 = ProducerGroup(
    name="UnrollGenElWHLV1",
    call=None,
    input=None,
    output=None,
    scopes=["emt"],
    subproducers=[gen_pt_1, gen_eta_1, gen_phi_1, gen_mass_1, gen_pdgid_WH_1],
)
UnrollGenElLV2 = ProducerGroup(
    name="UnrollGenElLV2",
    call=None,
    input=None,
    output=None,
    scopes=["ee"],
    subproducers=[gen_pt_2, gen_eta_2, gen_phi_2, gen_mass_2, gen_pdgid_WH_2],
)
UnrollGenTauLV1 = ProducerGroup(
    name="UnrollGenTauLV1",
    call=None,
    input=None,
    output=None,
    scopes=["tt"],
    subproducers=[
        gen_pt_1,
        gen_eta_1,
        gen_phi_1,
        gen_mass_1,
        gen_pdgid_1,
        gen_taujet_pt_1,
    ],
)
UnrollGenTauLV2 = ProducerGroup(
    name="UnrollGenLV2",
    call=None,
    input=None,
    output=None,
    scopes=["mt", "et", "tt"],
    subproducers=[
        gen_pt_2,
        gen_eta_2,
        gen_phi_2,
        gen_mass_2,
        gen_pdgid_2,
        gen_taujet_pt_2,
    ],
)
UnrollGenTauWHLV3 = ProducerGroup(
    name="UnrollGenLV3",
    call=None,
    input=None,
    output=None,
    scopes=["emt"],
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
        LVGenParticleWH1,
        LVGenParticleWH2,
        LVGenParticleWH3,
        UnrollGenElWHLV1,
        UnrollGenMuWHLV2,
        UnrollGenTauWHLV3,
        gen_m_vis_WH,
    ],
)
MTGenDiTauPairQuantities = ProducerGroup(
    name="MTGenDiTauPairQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["mt"],
    subproducers=[
        MTGenPair,
        LVGenParticle1,
        LVGenParticle2,
        UnrollGenMuLV1,
        UnrollGenTauLV2,
        gen_m_vis,
    ],
)
ETGenDiTauPairQuantities = ProducerGroup(
    name="ETGenDiTauPairQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["et"],
    subproducers=[
        ETGenPair,
        LVGenParticle1,
        LVGenParticle2,
        UnrollGenElLV1,
        UnrollGenTauLV2,
        gen_m_vis,
    ],
)
TTGenDiTauPairQuantities = ProducerGroup(
    name="TTGenDiTauPairQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["tt"],
    subproducers=[
        TTGenPair,
        LVGenParticle1,
        LVGenParticle2,
        UnrollGenTauLV1,
        UnrollGenTauLV2,
        gen_m_vis,
    ],
)
EMGenDiTauPairQuantities = ProducerGroup(
    name="EMGenDiTauPairQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["em"],
    subproducers=[
        EMGenPair,
        LVGenParticle1,
        LVGenParticle2,
        UnrollGenElLV1,
        UnrollGenMuLV2,
        gen_m_vis,
    ],
)
ElElGenPairQuantities = ProducerGroup(
    name="ElElGenPairQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["ee"],
    subproducers=[
        ElElGenPair,
        LVGenParticle1,
        LVGenParticle2,
        UnrollGenElLV1,
        UnrollGenElLV2,
        gen_m_vis,
    ],
)
MuMuGenPairQuantities = ProducerGroup(
    name="MuMuGenPairQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["mm"],
    subproducers=[
        MuMuGenPair,
        LVGenParticle1,
        LVGenParticle2,
        UnrollGenMuLV1,
        UnrollGenMuLV2,
        gen_m_vis,
    ],
)
MuMuTrueGenDiTauPairQuantities = ProducerGroup(
    name="MuMuGenPairQuantities",
    call=None,
    input=None,
    output=None,
    scopes=["mm"],
    subproducers=[
        MuMuTrueGenPair,
        LVTrueGenParticle1,
        LVTrueGenParticle2,
        UnrollGenMuLV1,
        UnrollGenMuLV2,
        gen_m_vis,
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
    scopes=["mt", "et", "tt", "em", "ee", "mm", "emt"],
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
    scopes=["mt", "et", "tt", "em", "ee", "mm", "emt"],
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
    scopes=["mt", "et", "tt", "em", "ee", "mm", "emt"],
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
    scopes=["emt"],
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
    scopes=["emt"],
    subproducers=[
        GenPairForGenMatching,
        GenMatchP1,
        GenMatchP2,
        GenMatchP3,
    ],
)
